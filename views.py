from pyexpat.errors import messages

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema, BatchRequestSchema

main_bp = Blueprint('main', __name__)

#FILE_NAME = 'data/apache_logs.txt'

@main_bp.route ('/perform_query', methods = ['POST'])
def perform_query():
    #TODO принять запрос от пользователя
    data = request.json
    #обработать запрос, валидировать значения

    try:
        validated_data = BatchRequestSchema().load(data) #здесь нам возвращается словарь, где лежат queries
    except ValidationError as error:
        print(error.messages)
        return jsonify(error, messages), 400 #то есть валидаци типов проходит до наше валидации


    #Делаем вызов по цепочке - то есть резульиат 1 функции засовываем во вторую и так далее
    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd = query['cmd'],
            value = query['value'],
            file_name = query['file_name'],
            data = result
        )

    return jsonify(result)

    #вариант когда был вызов 1 или 2 запросов)
    # return jsonify(build_query(
    #     cmd = validated_data['cmd1'],
    #     value = validated_data['value1'],
    #     file_name = 'data/apache_logs.txt',
    #     ),
    # )
