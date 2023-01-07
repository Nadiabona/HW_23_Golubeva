# import re
#
# data_1 = ['1.181.2.178 [17/May/2015:20:05:36] "GET / HTTP/1.1" 200',
# '1.125.2.148 [17/May/2015:20:05:19] "GET /?flav=rss20 HTTP/1.1" 200',
# '1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200',
# '1.163.30.77 [17/May/2015:20:05:37] "GET /blog/dot.html HTTP/1.1" 200']


# for i in data_1:
#     print (re.match(r"^(.+)\.(png|jpeg)",i))

# res1 = [x for x in data_1 if x is not None]
# print(res1)


# res = [x for x in data_1 if (re.match(r"^(.+)\.(png|jpeg)",x)) is not None]
# print (res)
#
# return filter(lambda x: value in x, data)
#def filter_query(value, data): #data - Iterable[str]
    #return filter(lambda x: value in x, data) #data - казываем, по чему мы перечисляемся, х - строка из data