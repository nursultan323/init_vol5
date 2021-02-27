# списки

# list = [1, 2, 3, 4, 5, 6,]
# list2 = [1, abc, [1, 2, 3,], (1, 2, 3,)]
# print(type(list2))
# print(len(list_))
# text = 'hello'
# print(text[0])
# print(text[-1])
# print(text[-5])
# print(text[0:4])
# print(text[:8:2])
# print(text[::-1])
# print(text[-1] + text[2])
# print(list2[-1])
# print(len(list2))
# print(list2[2][2])
# print(list2[2][-1])

# method append

# list1 = [1,2,3,4,5,6]
# list1.append(10)
# print(list1)

# method extend

# list1 = [1,2,3,4]
# list2 = [0,9,8,7]
# list1.extend(list2)
# print(list1 + list2)

# metod insert

# cars = ['mesrds', 'honda', 'subaru']
# cars.insert(1, 'toyota')
# print(cars)

# method remove

# cars.remove('honda')
# print(cars)

# method pop

# list_ = [1,2,3,4,5,6,7,8,9]
# last_element = list_.pop()
# print(list_)
# print(last_element)
# x = list_.pop(0)
# print(x)

# method index

# students = ['Шабан', 'Махмуд', 'Тариель', 'Жазгуль', 'Алтынай', 'Махмуд']
# print(students.index('Махмуд'))

# method count

# print(students.count(123))
# print(len(students))

# method reverse разворачивает список

# students.reverse()
# print(students)

# method sort

# students = ['Шабан', 'Махмуд', 'Тариель', 'Жазгуль', 'Алтынай', 'Махмуд']
# students.sort(key=len) # по длине
# students.sort()_# сортирует по алфавиту
# print(students)
# numbers = [1,5,3,7,0,5,7,3,4,6]
# numbers.sort()
# print(numbers)

# method clear

# nambers.clear()
# print(nambers)
# del nambers
# print(numbers)

# diapazon = list(range(50))
# print(diapazon)

# TUPLE - КОРТКЖ
# new_tuple = (1,2,3,4,5,76,1,2,3,4,1,2)
# new_tuple2 = tuple()
# print(tuple(new_tuple))
# print(dir(tuple))
# print(new_tuple.count(1))
# print(new_tuple.index(2))
#
# new_list = list(new_tuple)
# print(type(new_tuple))
# print(new_list)
# new_tuple.append(99)

# словари - dictionary

# dict = {}
# dict2 = dict()
# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrgizstan', 'Kiev': 'Ukraine'}
# print(capitals)
# print(len(capitals))
# print(dir(list))

# method fromkets

# dictionary = dict.fromkeys(['key1', 'key2'], 'value')
# print(dictionary)

# method get() получает по ключу значения

# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrgizstan', 'Kiev': 'Ukraine'}
# print(capitals.get('Bishkek'))

# method keys выводит все ключу
# print(capitals.keys())

# method values выводит все значения
# print(capitals.values())
# print(capitals['Moscow'])
# print((capitals[Almaty])) #KeyError такого нет

# method items() возвращает паты ключ значение

# pairs = capitals.items()
# print(pairs)

# method pop удаляет коюч и значение возвращает значение

# val = capitals.pop('Moscow')
# print(val)
# print(capitals)

# method popitem вырезает последнее значение

# last_pair = capitals.popitem()
# print(type(last_pair))
# print(capitals)

# method update
# capitals2= {'Washington': 'USA', 'Paris': 'France'}
# capitals.update({'Washington': 'USA', 'Paris': 'France'})
# print(capitals)

# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrgizstan', 'Kiev': 'Ukraine'}
# capitals = dict(Moscow='Russia', Bishkek='Kyrgizstan')
# capitals = dict([
#     ('Moscow', 'Russia')
#     ('Bishkek', 'Kyrgizstan')
# ])

# students = {'python': {'a': 'b', 'c': 'd'}}

