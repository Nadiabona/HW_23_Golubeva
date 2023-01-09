import os
from typing import Optional
from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query


def read_file(file_name: str):
    data_path = os.path.join('data', file_name)
    with open(data_path) as file:

        for line in file:
            yield line


CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit' : limit_query,
    'map' : map_query,
    'sort': sort_query,
    'regex': regex_query
}


def build_query(cmd: str, value: str, file_name: str, data: Optional[list[str]]):
    # type: ignore[operator]
    if data is None:  # значит это вызов первой функции
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

        # TODO: маршрутизация
    return list(CMD_TO_FUNCTIONS[cmd](value = value, data = prepared_data))














































# вариант, когда мы делали по доному-двум без вызова по чепочке
# def build_query(cmd:str, value:str, file_name:str):
#         with open(file_name) as file:
#                 return list(filter_query(value, file)) #надо преобраховать в список, потому что фильтр в json запаковать не можем, это генератор, для этог его нужо преобразовать в список
