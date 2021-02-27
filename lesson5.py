# обёртка
# from datetime import datetime
#
# def timeit(func):
#     def wrapper():
#         start = datetime.now()
#         func
#         print(datetime.now() - start)
#     return wrapper
#
# @timeit
# def one():
#     l = []
#     for i in range(10000):
#         l.append(i)
#     return l
#
# @timeit
# def two():
#     l = [i for i in range(10000)]
#     return  l
#
# one()
# two()

# пример
# def make_upper(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
#
# def make_lower(func):
#     def wrapper():
#         return func().lower()
#     return wrapper
#
# @make_upper
# def hello():
#     return "Hello World"
#
# @make_lower
# def myfunc():
#     return "I Like Python"
#
# x = make_lower(myfunc)()
# print(x)


