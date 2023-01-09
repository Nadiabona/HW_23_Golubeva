import os

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
        return jsonify(error, messages), 400



    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd = query['cmd'],
            value = query['value'],
            file_name = query['file_name'],

            data = result
        )

