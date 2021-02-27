# Chapter 1.1

# №1



# №2

# print(36/5)
# 7.2

# №3

# string = 'cdr'
# if string[:]==string[::-1]:
#      print("palindrome")
# else:
#      print("not palindrome")

# №4

# a = 'I'
# b = ' love'
# c = ' Java'
# d = ' Python'
# print(a + b)
# print(a + b + d)

# №5

# name = imput'Sultan'
# print(name * 10)

# №6

# text = 'hello world'

# №7
# №8
# №9



# №10




# №11
# №12


# Chapter 1.2

# №1

# list_ = [1, 2, 2, 4, 11, 2, 3, 1]
# list_ = set(list_)
# print(list_)

# №2

# s = ['John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom']


# №3

# num_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_.reverse()
# print(num_)

# №4



# №5



# №6



# №7

dictionary = dict.fromkeys(['key1', 'key2'], 'value')
print(dictionary)

# №8



# №9



# №10



# №11



# №12



# №13



# №14



# №15



# №16



# №17

# a, b, c =imput("введите числа через пробел: ").split()
# print('Количество положительных чисел')

# №18



# №19



# №20



# №21



# №22


# пример
# def burger(func):
#   def bur(*a, **b):
#     print('Верхняя булочка')
#     func(*a, **b)
#     print('Нижняя булочка')
#   return bur
#
# def kotleta(k):
#   def kot(*a, **b):
#     print('курочка')
#     k(*a, **b)
#     print('говядина')
#   return kot
#
# @burger
# @kotleta
#
# def nachinka(cheese, tomatoes, cucumber, sous):
#     print( '\n', cheese,'\n', tomatoes,'\n', cucumber,'\n', sous,'\n',)
#
# nachinka('Сыр','Помидоры','Огурцы', 'Соус')