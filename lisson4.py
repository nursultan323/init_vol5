# фунции

# def my_funs():
#     print('hello world')
#
# my_funs()

# def my_funs(name):
#     print(f"Hello, me name is {name}")
#
# my_funs("Sultan")

# def add(num1, num2):
#     print(num1 + num2)
# add(1, 2)
# add(44,55)

# def add(num1, num2, num3):
#     result = num1 + num2 + num3
#     return f"Результат сложение чисел: {result}"
# print(add(10, 20, 30))

# figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
#
# if figure == '1':
#   a = float(input("Ширина: "))
#   b = float(input("Высота: "))
#   print("Площадь: %.2f" % (a*b))
# elif figure == '2':
#   a = float(input("Основание: "))
#   h = float(input("Высота: "))
#   print("Площадь: %.2f" % (0.5 * a * h))
# elif figure == '3':
#   r = float(input("Радиус: "))
#   print("Площадь: %.2f" % (3.14 * r**2))
# else:
#   print("Ошибка ввода")
#

  # def rectangle():
  #     a = float(input("Ширина: "))
  #     b = float(input("Высота: "))
  #     print("Площадь: %.2f" % (a * b))
  #
  #
  # def triangle():
  #     a = float(input("Основание: "))
  #     h = float(input("Высота: "))
  #     print("Площадь: %.2f" % (0.5 * a * h))
  #
  #
  # def circle():
  #     r = float(input("Радиус: "))
  #     print("Площадь: %.2f" % (3.14 * r ** 2))
#
#
# def add(q, w, e, r,):
#     return q + w + e + r
# print(add(1, 2, 3, 4))
#
# def add(*args):
#     resulta = 0
#     for i in args:
#         for x in i:
#             # result = result + i
#             result += x
#         return result
#     # nums = list(range(20))
#     # print(add(nums))
#
# def add1(*args):
#     result = 1
#     for i in args:
#         result = i + result
#         return  result
# print(add(1, 2, 3, 4, 5, 6))
#
# num = 100
#
# def myfunc():
#     num = 200
#     print(num)
#     def func2():
#         num = 300
#         print(num)
#     func2()
# myfunc()
# print(num)

# полиморфизм
# def add(x, y):
#     return x + y
# print(add(12, 22))
# print(add('22', '33'))

# point = input('is year leap: ')
# if point == 'год':
#     print('True')
# else:
#     print('False')

# import calendar
#
# def is_leap(a):
#     return'Bискосный'\
#     if calendar.isleap(a) \
#     else 'Hе вискосный'
# print(is_leap(2021))

# def is_year_leap(year):
#     if year % 4  != 0:
#         print('Обычный')
#     elif year % 100 == 0:
#         if year % 400 == 0:
#             print(f'{year} год Високосный')
#         else:
#             print('Обычный')
#     else:
#         print(f'{year} год Високосный')
#
# is_year_leap(int(input('Введите год: ')))

# Рекурсия

# import time
# def short_story():
#     print("У попа была собака, он ее любил.")
#     print("Она съела кусок мяса, он ее убил,")
#     print("В землю закопал и надпись написал:")
#     time.sleep(1)
#     short_story()
#
#
# short_story()


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         # print(n)
#         return n + factorial(n - 1)
# print(factorial(11000))
#
# from datetime import datetime
# start1 = datetime.now()
#
# list_ = []
# for i in range(2000000):
#     list_.append(i)
# # print(list_)
#
# stop1 = datetime.now()
# start2 = datetime.now()
#
# list1 = [i for i in range(2000000)]
# # print(list1)
# stop2 = datetime.now()
#
# print(f"res1 = {stop1 - start1}")
# print(f"res2 {stop2 - start2}")

# old_list =['1',

# old_list =['1', '2', '3', '4', '5', '6', '7']
# new_list =list(map(int, old_list))
# print(new_list)
#
# def func_upper(word):
#     return word.upper()
#
# list_ = list('hello world')
# print(list_)
#
# new_list = list(map(func_upper, list_))
# print(new_list)

# mixed =['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
#
# zolushka =list(filter(lambda x: x == 'мак', mixed))
# print(zolushka)

# фильтр
# list_ = [i for i in range(100)]
# my_func = lambda x: x % 2 == 0
# even_nambers = list(filter(my_func, list_))
# print(list_)
# print(even_nambers)

# zip
# a =[1,2,3]
# b ="xyz"
# c =(None, True)
# res =list(zip(a, b, c))
# print(res)

# a =[1,2,3,4,5,6,7,8]
# b ="qwertyui"
# c =(None, True, False, None, True, False)
# res =tuple(zip(a, b, c))
# print(res)

# capitals = dict(zip(['Russia', 'Kyrgizstan', 'USA'], ('Moscow', 'Bishkek', 'Washington')))
# print(capitals)
