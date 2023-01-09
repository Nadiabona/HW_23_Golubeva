import re
from typing import Iterable
def regex_query(value, data: Iterable[str]):
    regex = re.compile(value)
    return filter(lambda x: regex.search(x), data)

def filter_query(value, data:Iterable[str]):
    return filter(lambda x: value in x, data)

def unique_query(data, *args, **kwargs):
    return set(data)

def limit_query(value, data):
    limit: int = int(value)
    return list(data[:limit])

def map_query(value, data):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number],data)

def sort_query(value, data):
    reverse = value == 'desc'
    return sorted(data, reverse = reverse)

