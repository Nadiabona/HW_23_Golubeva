import re
from typing import Iterable
def regex_query(value, data: Iterable[str]):
    regex = re.compile(value)
    return filter(lambda x: regex.search(x), data)
    #return filter(lambda x: (re.match(regex,x) is not None, data))

def filter_query(value, data:Iterable[str]):
    return filter(lambda x: value in x, data) #data - казываем, по чему мы перечисляемся, х - строка из data

def unique_query(data, *args, **kwargs):
    return set(data)

def limit_query(value, data):
    limit: int = int(value)
    return list(data[:limit])#преобразуем в список, потому что в данных может быть генератор отзезаем col_number у колонки

def map_query(value, data):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number],data) #сплитуем по пробелу и берем конкретный номер колонки

def sort_query(value, data):
    reverse = value == 'desc' #в cmd будет приходить либо asc либо что-то другое, понять как сортировать
    return sorted(data, reverse = reverse) #сюда приходит флаг reverse
#
#res = filter_query("POST", 'data/apache_logs.txt')