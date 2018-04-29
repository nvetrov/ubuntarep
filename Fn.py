"""
Исключение
l = [1, 9]
try:
    raise IndexError(print(l[1]),'cool')
except IndexError as e:
    print('Иди в жопу',e)
else:
    print('Все идиёт по плану')
finally:
    print('finally')

# try:
#     3 / 'asd'
# except TypeError as i_knew_it:
#         print(i_knew_it)
#         print()


# try:
#     d = {'key':33}
#     print(d['does not exist'])
# except ZeroDivisionError:
#     print("This won't be called")
#
# try:
#     d = {'key':33}
#     print(d['does not exist!'])
# except KeyError as e:
#     print("Got it",e)
"""



# try:
#     a = 1 / int(input('x: '))
# except ZeroDivisionError as e:
#     print('/0')
#     print(e)
# except TypeError:
#     print('Wring type',a)
# except ValueError:
#     print('Bad input',a)


"""
import requests
L = 0
Total = 0
count = 0
FileName = 'dataset_3378_2.txt'
with open(FileName, 'r') as inf:
     url = inf.readline().strip()
r = requests.get(url)
text = r.text.splitlines()
for line in text:
    count += 1
L = (len(r.text.splitlines()))
with open('new.txt', 'w') as f:
      f.write(r.text)
num_lines = sum(1 for line in open('new.txt'))
with open('send.txt', 'w') as ansfile:
      ansfile.writelines(str(num_lines))
print("num_lines = sum(1 for line in open('new.txt')) = {}".format(num_lines))
print("L = (len(r.text.splitlines())){}".format(L))
print("text = r.text.splitlines() for line in text:count += 1 = {}".format(L))
print(r.text.count('\n'))
if (url == r.url) is True and (L == count == num_lines):
    print("Correct")
else:
    print('Wrong, redo it!')

"""


# r = requests.get('https://api.github.com/events')
# r = requests.get('https://api.github.com/user', auth=('nvetrov@gmail.com', 'C1vmdpalc33'))
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# print(r.status_code) # 200 все хорошо.
# print(r.headers['content-type'])
# print(r.encoding)
# parsed_string = {}
# kol = 0
# parsed_string = json.loads(r.text)
# for key,value in parsed_string.items():
#     # if key == plane:
#        print(str(kol) + ")",key,value,sep=':')
#        kol += 1
# print('---------------------')
# print(r.headers.get('content-type'))

# print(parsed_string['login'])


#
# with open('hello.txt', 'a') as f:
#      f.write("Hello World3\n")

# fh = open("hello.txt",'a')
# lines_of_text = ['One line of text here', 'and another line here', 'and yet another here', 'and so on and so forth']
# fh.writelines(lines_of_text)
# fh.close()
#
# fh = open("hello.txt", 'r')
# print(fh.readline())
# fh.close()

# import requests
# r = requests.get('https://api.github.com/user', auth=('nvetrov@gmail.com', 'C1vmdpalc33'))
# print(r.status_code) # 200 все хорошо.
# print(r.headers['content-type'])
# print(r.encoding)
# # print(r.text)

"""
#  Исключение
try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred!")
finally:
    file_handler.close()
"""

# a=[1, 2, 3]
# b="xyz"
# c=(None, True)
#
# res=list(zip(a, b, c))
# print(res)
# [(1, 'x', None), (2, 'y', True)]

"""
from functools import reduce
items=[1, 2, 3]
sum_all=reduce(lambda x, y: x + y, items)

print(sum_all)
# Вычисление наибольшего элемента в списке при помощи reduce:
from functolls import reduce
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a,b: a if (a > b) else b, items)

print (all_max)

"""

"""
l1=[1, 2, 3]
l2=[4, 5, 6]

new_list=list(map(lambda x, y: x + y, l1, l2))
print(new_list)
"""
# for key,value in T.items():
#     print(key,value)

# print(r.json())
#
# a = (dir('requests'))
# for i in a:
#     print(i)
# splitlines
# def update_dictionary(d, key, value):
#     key += key * (key not in d)
#     d[key] = d.get(key, []) + [value]

'''
# -*- coding: utf8 -*
'''

# help("modules")
# print(dir('requests'))
# import  sys
# l = 0
# with open('file.txt', 'r') as file_handle:
#     for line in file_handle:
#         # print(line)
#         if line != '\n':
#             l += 1
#
# print(l)

# 'Лучшие'
# import sys
# for i in sys.argv[1:]:
#     print(i, end=" ")
#
#
# import sys
# s = ''
# for i in range(1, len(sys.argv)):
#     s += sys.argv[i]+' '
# print(s, end=' ')


# A = {'ab' : 'ba', 'aa' : 'aa', 'bb' : 'bb', 'ba' : 'ab'}
# key = 'ab'
# if key in A:
#     del A[key]
# try:
#      del A[key]
# except KeyError:
#        print('There is no element with key "' + key + '" in dict')
# print(A)




# l1 = list()
# l1 += [1,2,3]
# l1.append(4)
# l1[0] = 11
# print(len(l1))
# print(l1)
# print(l1[3])
# l1[3] = "Иди в жопу"
# print(l1)
# l1.remove(l1[3])
# print(l1)
# # import sys

    # s2 = inf.readline().strip() # брать все служебные символы при чтение строки   '\t abc \ n'.strip() -> 'abc'

# tuple1 = (1, 2, 'string', 'one more', False, None)
# print(tuple1)
# new_tuple = tuple()
#
# for item in tuple1:
#     # if item in tuple1:
#     if not isinstance(item, str) and item != False and item != None:
#         new_tuple += (item,)
# print(new_tuple)

# def unique(lst):
#     seen = set()
#     result = []
#     for x in lst:
#         if x in seen:
#             continue
#         seen.add(x)
#         result.append(x)
#     return result
#
# command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
#
# c1 = command1.split(",")
# c2 = command2.split(",")
# ss = tuple()
# ss = (12,)
#
# print (ss)
# filtered_data = []
# filtered_data2 = []
#
# for i in c1:
#         if i.isalnum() == True:
#            filtered_data.append(i)
#            # a1 = ' '.join(filtered_data)
# # print(aa)
# for j in c2:
#         if j.isalnum() == True:
#            filtered_data2.append(j)
#            # a2 = ' '.join(filtered_data2)
#
# S = unique(filtered_data + filtered_data2)
# print(S)




# from itertools import groupby
#
# command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
#
# command = command1.split(",")
# command += command2.split(",")
# # print(command)
# filtered_data = []
#
# for i in command:
#         if i.isalnum() == True:
#            filtered_data.append(i)
#            aa = ' '.join(filtered_data)
# print(aa)

"""
Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля, находит для переданного
ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.

Sample Input:

10.0


"""
# import math
#
# r = float(input())
#
# print(float(2 * math.pi * r))
#
#




"""
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
которая выводит все позиции, на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""

















'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно).
На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

a = int(input())
b = ''

for i in range(1, a + 1):
    b += (str(i) + ' ') * i
strLength = a * 2 if a < 47 else (a - 46) * 3 + 46 * 2
print(b[:strLength], end='')

'''
#
# n = int(input())
# cnt = 0
#
# for i in range(n+1):
#     for k in range(i):
#         print(i, end=' ')
#         cnt += 1
#         if cnt == n: break
#     if cnt == n: break


# n, s = int(input()), []
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         s.append(str(i))
# print(' '.join(s[0:n]))

#
# p = []
# t = []
# M = []
# n = int(input())
# l = len(t)
# k = 0
# m = 2
# for h in range(1,n+1):
#     p.append(str(h))
# for i in range(0,len(p)):
#     if i==0:
#         t.insert(l,p[i])
#         k = 0
#     elif i==1:
#         while i>=k:
#             l = len(t)
#             t.insert(l,p[i])
#             k +=1
#         k -=2
#     elif i>1:
#         while i>=k:
#             l = len(t)
#             t.insert(l,p[i])
#             k +=1
#         k =i-m
#         m +=1
#     l = len(t)
# x = len(t)
# if len(t)==1:
#     print(1)
# else:
#     for j in range (0,x-1):
#         M.append(t[j])
#     for g in range(0,n):
#         print(M[g],end=' ')
#
#






"""
На , ,пишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения,
а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка.
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
def modify_list(l):
    l[:] = [(i // 2) for i in l if i % 2 == 0]


# # Рещение
# def modify_list(l):
#      i = len(l) - 1
#      while i != -1:
#           if l[i] % 2 != 0:
#              del l[i]
#           else:
#                l[i] = l[i] // 2
#           i -= 1


# l = [1, 2, 3, 4, 5, 6]
# l = [10, 5, 8, 3]
# for x in range(len(l) - 1, -1, -1):
#      if l[x] % 2==0:
#           l[x]=l[x] // 2
#      else:
#           del (l[x])
#
# print(l)               # [5, 4]


# lst = [1, 2, 3, 4, 5, 6]
# lst = [10, 5, 8, 3]
# i = len(lst) - 1
# while i != -1:
#      if lst[i] % 2 != 0:
#          del lst[i]
#      else:
#          lst[i] = lst[i] // 2
#      i -= 1
# print(lst)
#




# # def modify_list(l):
# # lst = [10, 5, 8, 3]
# lst = [1, 2, 3, 4, 5, 6]
# for i in range(len(lst) - 1, -1, -1):
#       if lst[i] % 2 == 0:
#            del lst[i]
#       else:
#            lst[i] = lst[i] // 2
# print(lst)


"""

# file = open("C:\\Users\\nvetr\\Desktop\\text.txt", "r")
#
# print(file.name)

# print(file.read(4))
# print(file.tell())
# print(file.seek(2))
# file.close()

# s = input("Слово:")
# print(s[0] + '*' * (len(s) - 1) + s[-1])
# for i in s:
#     print(i)


# s.isdigit() - Состоит ли (под)строка из цифр
# s.isalpha() -  Состоит ли строка из букв
# new = []
# import os, sys
# from copy import copy
# with open('text.txt')as inf:
#     for line in inf:
#         line = line.strip()
#         print(line)
#         print(type(line))
# for i in range(len(line) - 1):
#     if line[i].isalpha() == True:
#        print(line[i], i,"Число")
#     else:
#         print(line[i], i, "Символ")
#         new += line
# print(new)
# for s in len(line) - 1:
#
#     if s.isalpha() == True:
#         new += s
#     else:
#
#         new += (str(i) for i in () * sum )
#
# print(new, end='')


"""
Работа с файлом. Чтение из файла

import sys
# with open('text.txt') as inf:
#     s1 = inf.readline()
#     s2 = inf.readline().strip() # брать все служебные символы при чтение строки   '\t abc \ n'.strip() -> 'abc'
    #  Здесь файл уже закрыть
import os
# print(os.path.join('.', 'dirname', 'filename.txt') )   # './dirname/filename.txt'
# Чтение
# with open('input.txt') as inf:
#     for line in inf:
#         line = line.strip()
#         print(line)
# Запись
ouf = open('file.txt', 'w')
ouf.write('Some text \n')
ouf.write(str(25)) #Число
ouf.close()

with open('file.txt', 'w') as ouf:
     ouf.write('Some.txt\n')
     ouf.write(str(25))
"""



# def f(x):
#     return x**2
#
# # d = {}
# # for i in range(int(input())):
# #     x = int(input())
# #     if x not in d:
# #         d[x] = f(x)
# #     print(d[x])
#
# d = {}
# n = int(input())
# for count in range(n):
#     count = int(input())  #фокус
#     if count not in d:
#         d[count] = f(count)
#     print(d[count])


'''


def f(x):
    return x**2

d={}
k=[]
n=int(input())
for i in range(n):
    x = int(input())
    k.append(x)
for j in range(0, len(k)):
    key=k[j]
    if key in d:
        print(d[key])
    elif key not in d:
        p=k[j]
        d[key]=f(p)
        print(d.get(key))
'''

"""
lst = input().lower().split()
d = {}
for i in lst:
    d[i] = lst.count(i)
for i in d:
    print(i, d[i])
"""

'''
def hist(s):
    d = dict() #создаем словарь
    for c in s.lower().split(): #..Из полученой строки, в нижнем регистре, по словам
        if c not in d:d[c] = 1  #нет в словаре - добавим первое значение
        else:d[c] += 1          #есть - прибавим счетчик
    return d
#end 
for key, value in hist(input()).items(): print(key, value) #и выведем как надо

'''

# n=''
# n = str(input())
# # n = "a aa abC aa ac abc bcd a"
# m = [] #инициализация списка
# m.append([str(s.lower()) for s in n.split()])
# d = {} #инициализация пустого словаря
# li = len(m)
# lj = len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p]+=1
#         else:
#             d[p] = 1
# for key,value in d.items():
#    print(key,value)
#


'''

d = {}
print(update_dictionary(C)  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key.
Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].
'''
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2*key in d:
#         d[2*key] += [value]
#     else:
#         d[2*key] = [value]
# x = {}
# print(update_dictionary(x, 1, -1))  # None
# print(x)                            # {2: [-1]}
# update_dictionary(x, 2, -2)
# print(x)                            # {2: [-1, -2]}
# update_dictionary(x, 1, -3)        # {2: [-1, -2, -3]}
# print(x)


# import math
# d = dict(n = 1, m = 'bnw')
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#    if not math.isnan(value):
#        filtered_data.append(value)
# print(filtered_data)
#
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#    print('What is your {0}?  It is {1}.'.format(q, a))

# S = {'Numers': 1, 'Letters': "A"}
# a = dict(one=1, two=2, three=3)
# print(a)
# print(S)
# for i in list(range(2, 11)):
#    S['Numbers'] = i
#
# for e in S.values():
#     print(e, end='\n')
#
# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
""""
Словарь.
Словарь помагает хранить множество пар:ключ - значение.
# dict, {}
# d = {'Возраст': 33, 'Вес': 70, 'Пол': 'М'}
# print(d['Возраст'])
# d['ФИО'] = {'Ветров Николай Владимирович'}
# name = d.get('ФИО')
# print(name)
# d.clear()
# d = {'C': 14, 'A':12, 'T': 9, 'G':17}
# for key in d:
#     print(key, end=';')
# for key in d.keys():
#     print(key, end='|')
# for value in d.values():
#     print(value, end='/')
# for key,value in d.items():
#     print(key,value, end=';')
#
"""

"""
Множество  позволяют хранить некий набор данных и
быстро отвечать на запрос - присутствует этот элемент в этом наборе данных.

set - множество
s = set() #создать пустое множество.
s.add()
s.remove() # Если нет элемента, то возращает ошибку
s.discard()# Если нет элемента, то НЕ возращает ошибку
s.clear() # Очищает весь список.


basket = {'Банан', 'Апельсин', 'Мандарин'}
for x in basket:
    print(x)


if 'Мандарин' and 'Банан' in basket:
    print("Мандарин в карзине")
else:
     print('Нет мандарина')

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
      print(f)
"""

# def modify_list(l):
#     for element in range(l):
#         if  element  % 2 == 0:
#


# # https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
# from PIL import Image
# import os, sys
#
# size = (128, 128)
#
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             im = Image.open(infile)
#             im.thumbnail(size)
#             im.save(outfile, "JPEG")
#         except IOError:
#             print("cannot create thumbnail for", infile)

# images = ["A.jpg","B.jpg","C.jpg"]
# resize_images(images)


# from PIL import Image
# im = Image.open("LM logo.jpg")
# im.show()

# import usethis
# print(__name__)
#


# Импортирую свой модуль
# from myVolumes import *
# print(sphere_vol(4))
# print(cube_vol(1,2,3))
# print(cone_vol(3,4))

# import myVolumes
# print(dir(myVolumes))
# print(myVolumes.sphere_vol(1))

#


"""
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# http://localhost:8000/


# import shutil
#
# shutil.copyfile('hi.py', 'mytest.py')

# import math
# from math import pi
# from math import *
#
# print(sin(pi))
# print(factorial(6))
"""

"""
Рекурсия
# def count_vowels(s, i = 0):
#     if (i == len(s)): return 0
#     # pass
#     c = s[i]
#     if c in 'aeiou':
#       return count_vowels(s, i + 1) + 1
    return count_vowels(s, i+1) + 0
# print(count_vowels('hello'))
# print(count_vowels('world'))

#  didit_sumls
# 345 -> 3+4+5 = 12
# 345
# 34
# 3
# 0
# def didit_sum(n):
#     if n == 0: return 0
#     return didit_sum(n // 10) + n % 10
# # print(didit_sum(345))
#
# # 0 1 2 3 4 5 6 ...
# # 1 1 2 3 5 8 13 ...
# def fib(n):
#     if n == 0 or n==1:
#         return 1
#     return fib(n-2) + fib(n-1)
#
# for i in range(10):
#     print(fib(i), end ='|')
#



# def exponentiate(b,e):
#     #Base case
#     if (e == 0): return 1
#      #recursive call
#     return exponentiate(b, e-1) * b
#
# print(exponentiate(2,3))


# def double(n):
#     if n == 0:
#         return 0
#     return double(n-1) + 4
#
# print (double(3))
# alpha="abcdefghijklmnopqrstuvwxyz"  # length 26
#
#
# def encrypt(s, shift=3):
#     encrypted_str=""
#     for c in s:
#         index=alpha.index(c)
#         shifted_index=(index + shift) % len(alpha)
#         encrypted_str+=alpha[shifted_index]
#     return encrypted_str
#
# def decrypt(e, shift=3):
#     decrypted_str=""
#     for c in e:
#         index=alpha.index(c)
#         shifted_index=(index - shift) % len(alpha)
#         decrypted_str+=alpha[shifted_index]
#     return decrypted_str
#
# print(encrypt("abc"))
# print(decrypt("def"))

# print(encrypt("helloworld"))
# print(decrypt("khoorzruog"))
# print(decrypt(encrypt("aaabbbccczzz")))

# def reverse(s):
#     # pass
#     new_str = ""
#     for i in range(len(s)):
#         new_str += s[len(s) - i - 1]
#     return new_str
# # print(reverse("123"))
# # print(reverse("ABC"))


# def is_palindrome2(s):
#
#     if s == s[::-1]:
#         print("Yes this is a palindrome")
#     else:
#         print("No this is not a palindrom=")
#
#
#
# def is_palindrome(p):
#     for i in range(len(p) // 2):
#         if p[i] != p[len(p) - i - 1]:
#             print("No this is not a palindrome ")
#             return #exit function
#     print("Yes this is a palindrome")
#
# is_palindrome2("12345654321")
# is_palindrome("12345654321")


# def is_even(number):
#     if number % 2 == 0:
#         print("{:d} is even".format(number))
#
#         return True
#     else:
#         print("{:d} is odd".format(number))
#     # return False
#

# import datetime as dt
#
# def record_time(message, time = dt.datetime.now()):
#     #save to file
#     print("{:}, time: {:}".format(message, time))
# record_time("Это утро", "Feb 22nd 1988")


# def add(a,b,c):
#     return a+b+c
# print(add(1,2,3))
# def add(*numbers):
#     total = 0
#     for n in numbers:
#          total += n
#     return total
# print(add(1,2,3,4,5,6))
# print("a", 'b','cat', "dog')
"""

"""
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
 (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
"""

"""
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.



# numbers = 0
# l = []
# while True:
#     n = int(input())
#     numbers += n
#     l.append(n ** 2)
#     if numbers == 0:
#         break
# print(sum(l))



# a = [int(input())]
# y = 0
# for i in a:
#      if sum(a) != 0:
#         a.append(int(input()))
#      else:
#          for j in a:
#              j *= j
#              y += j
# print(y)
# a = [int(input())]
# x = 0
# for i in a:
#     if sum(a) != 0:
#         a.append(int(input()))
#     else:
#         for q in a:
#             q *= q
#             x += q
# print(x)
"""

# c = [S[i] for i*i in range(1,len(S))]
# print(S)

"""
На пальцах:
список - - - - - [a,   b,  c,   d]
индексы - - - -[0,   1,  2,   3] -- этими мы обычно оперируем
индексы - - - -[-4, -3, -2,  -1] -- а иногда удобнее этими

"""

"""
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка,
являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
Sample Input 1:

1 3 5 6 10
Sample Output 1:

13 6 9 15 7
Sample Input 2:

10
Sample Output 2:

10

# Мой
Num = [int(i) for i in (input().split())]
dd = []
L = len(Num)
j = 0
k = 0
Last = 0

if L == 1:
   print(Num[0])
else:
    for index in range(len(Num) - 1):
        dd.append(Num[index - 1] + Num[index + 1])

while k < len(Num):
     if k == len(Num) - 2:
         Last = Num[k]
     k += 1

dd.append(Num[0] + Last)
if L != 1:
    print(' '.join(str(x) for x in dd))


"""
# a = [int(i) for i in input().split()]
# if len(a) <2: print(a[0]) #из одного..
# else:
#   b=[a[i] for i in range(-1,len(a)-1)] #соседи слева
#   c=[a[i] for i in range(1,len(a))]    #соседи справа
#   c +=[a[0]]
#   for i in range(0,len(a)):
#     print(b[i]+c[i],end=' ') #что и требовалось...

#
# st=[int(i) for i in input().split()]
# l=len(st)
# st.insert(0,st[-1])
# st.append(st[1])
# i=1
# if l==1:
#   print(st[1])
# else:
#   while i!=l+1:
#     print(st[i-1]+st[i+1],end=' ')
#     i+=1


# 1-е место
# line=list(map(int, input().split()))
# l=len(line)
# if l<3:
#     print(*line[::-1])
# else:
#     ans=[line[(i-1)%l]+line[(i+1)%l] for i in range(l)]
#     print(*ans)
#

# numbers = [int (k) for k in input().split()]
# lenn = len(numbers)
# first = 0
# last = 0
# i = 0
# if lenn == 1:
#     print (numbers[0], end = ' ')
# elif lenn == 2:
#     print (numbers[0], numbers[1], end = ' ')
# else:
#         first = numbers[-1] + numbers[1]
#         print (first, end = ' ')
#         last = numbers[0] + numbers[-2]
#         for j in numbers[1:-1]:
#             j = numbers[i] + numbers[i + 2]
#             print (j, end = ' ')
#             i += 1
#         print (last, end = ' ')


# y = float(input())
# def f(x):
#
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     if -2 < x <= 2:
#         return -(x / 2)
#     if x > 2:
#         return (x - 2) ** 2 + 1
#
# print(f(y))

# def f(x):
#     if x <= -2:
#         return 1 - (x+2)**2
#     if x <= 2:
#         return -x/2
#     return (x-2)**2 + 1


# def min2(a, b):
#     if a <= b:
#         return a
#     else:
#         return b
# x, y = input().split()
# m = min2(x,y)
# print("Минимальное число из {} и {} это".format(x,y), m)
# m = min2(min2(1,2),0)
# print(m)
#

"""
Сапёр игра
Дано: Ввод 5 строк 4 столбоц 4 мин   Вывод  *21 , где * - мина   и  "."  если нулевое число мин.
Давайте посроем поле 2=х мерный список 5,4.
Заполним всю матрицу  заполним нулями и  в дальнейшнм будем в каждой ячейки матрицы накапливать значение соответствующие
числу  мин в соседних клитках.

Прочитаем координаты мин и занисем эти значение == -1.
мин.

i - номер строки
j = стодбец

a b 0         Слева сверху(a):  i -1 , j -1 ;   Ваше на 1 ячейку(b):  i - 1 , j
d X e  --->   Слева ячейка(d):  i -1,  j + 1    Справа  i + 1, j + 1
0 0 0

Надо перебрать все клетки  ij <= 1

Мы рассматриваем: i+di, j+dj, где di и dj : -1 до 1 пробегают по значениям.

Есть мина?: увеличиваем счетчик на 1,  else: переходим дальше.

"""
# from random import randrange                               # Импортируем функцию генерации случайных чисел
#
# rows, cols, mines = (int(i) for i in input().split())     # Количество строк, столбцов, мин.
# field = [[0 for col in range(cols)] for row in range(rows)] # Заполняем поле нулями
# mine_table = []
# for mine in range(mines):                                 # Случайным образом ставим мины
#     row = randrange(0, rows)
#     col = randrange(0, cols)
#     if (row, col) not in mine_table:                       # Если координат мин нет, добавляем их в таблицу
#         mine_table.append((row, col))
#         field[row][col] = "*"
#
# for row, col in mine_table:                               # Перебираем таблицу координат мин
#     for row_i in range(-1, 2):
#         temp_row = row + row_i
#         for col_j in range(-1, 2):
#             temp_col = col + col_j
#             if 0 <= temp_row < rows and 0 <= temp_col < cols and field[temp_row][temp_col] != '*': # Проверяем границу поля,
#                 field[temp_row][temp_col] += 1                                                     # а также что нет мины.
#
# for i in range(rows):                                     # Печатаем поле
#     for j in range(cols):
#         if field[i][j] == 0:
#             print(".", end=" ")
#         else:
#             print(field[i][j], end=" ")
#     print()
#
# mine_table.sort()                                         # Сортируем таблицу координат мин
# print(mine_table)                                         # Печатаем таблицу координат для проверки


# from pprint import pprint as pretty_print
# from copy import copy, deepcopy

# A = [[0] * n for i in range(n)]
# A = [[0 for j in range(n)] for i in range(n)]
# pretty_print(A)


# L = [int(i) for i in input().split()]
# # set возвращает тот же лист без повторений, например а=(1, 3 ,1 2), set(а)=(1, 3, 2)
# # duplicates = {}
# s = []
# for i in set(L):
#   if L.count(i) > 1:
#       s.append(i)
# print(s)


"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

L = [(i) for i in input().split()]

# duplicates = {}
s = []
for i in L:
       if i not in s and L.count(i) > 1:
          s.append(i)
consonants = ' '.join(s)
print(consonants)
"""

# from itertools import groupby
# for el, group in groupby(sorted(L)):
#     count = len(list(group))
#     if count > 1:
#         duplicates[el] = count # element -> number of occurrences
#
# print(duplicates) # -> {10: 3, 123: 2}


# from collections import Counter
# counter = Counter(A)
# print(counter)

# counter = {}
#
# for elem in A:
#     counter[elem] = counter.get(elem, 0) + 1
#
# doubles = {element: count for element, count in counter.items() if count > 1}
#
# print(doubles)


""""
a=input()
s=1
a=a+'0'
for j in range (0,len(a)-1):
    if a[j]==a[j+1]:
     s+=1
    else:
     print((a[j]+str(s)),end='')
     s=1
"""
""""
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
new = []
s = input()
s = s + "." # <---- Без точки не мог дого понять как это поправить.
count = 1
j = 1
for i in list(range(len(s) - 1)):
    if s[i] == s[i + j]:
        count += 1
        # print(i, s[i])
    if not s[i] == s[i + j]:
        new.append(s[i] + str(count))
        count = 1
consonants = ''.join(new)
print(consonants)

"""

# s = []
# s += 'aaaabbcaa'
# news = []
# count = 0
# for i in range(len(s)-1):
#     if s
#         count =


# numbers = [1,2,3,4,5,6,7,8,9]
# total = 0
#
# for n in numbers:
#     if n % 2 == 0:
#         total += n
# print(total)
# alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# vowels = 'aeiouAEIOU'
# my_string = "Packt publishing rocks!"
#
# characters = []
#
# for ch in my_string:
#     if ch not in vowels and ch in alpha:
#         characters.append(ch)
# consonants = ''.join(characters)
# print(consonants)


# # Исключение
# my_list = [1,2,3,4,5]
# my_tuple = (2,7,8,9,10) #Кортеж
# my_string = "Hellow World!"
#
# list_iterator = iter(my_list)
#
# while True:
#   try:
#     next_elem = next(list_iterator)
#     print(next_elem)
#   except StopIteration:
#       break

# index = 0
# names = ["Коля", "Саша","Вася","Миша"]
# while index <len(names):
#      name = names[index]
#      index += 1
#      print(name)
# # 1 - 10
# total = 0
# v = 1
# while  v <= 10:
#     total += v
#     v+=1
# print(total)

#
# l = [1,3,5,7,9,11]
#
# for index in range(len(l)):
#     print("index: {:d}, element: {:d}".format(index, l[index]))

# s = "hello world"
# a = [4, 6, 9]
# print ( 9 in a)
# print ( 5 in a)
# print ( 4 in a)
# print ( "ello" in s )


#  calc
# import sys # sys.exit() quits the program
#
# line = input()
# split = line.split()
#
# if len(split) != 3:
#     print("Wrong format",split)
#     sys.exit()
#
# left = int(split[0])
# op = split[1]
# right = int(split[2])
# val = 0
# if op == '+':
#      val = left + right
# elif op == '-':
#      val = left - right
# elif op == '*':
#      val = left * right
# elif op == '/':
#     if right == 0:
#          print("Деление на нуль")
#          sys.exit()
#     val = left / right
# else:
#       print("Unknown operator:{operator}".format(operator=op))
#       sys.exit()
# print("{line_expr} = {value:.2f}".format(line_expr=line, value = val))


"""
Так как про метод isdigit() я уже рассказывал, перейдем к остальным:

isalpha() возвращает True, если строка состоит только из букв, в противном случае - False
isalnum() возвращает True, если строка состоит из цифр и букв, в противном случае - False
islower() возвращает True, если строка состоит из символов в нижнем регистре, в противном случае - False
isupper() возвращает True, если строка состоит из символов в верхнем регистре, в противном случае - False
isspace() возвращает True, если строка состоит из неотображаемых символов (пробелы, перевод страницы, новая строка и т.д.), в противном случае - False
istitle() возвращает True, если в строке слова начинаются с заглавной буквы, в противном случае - False
print(string.islower())
print(string.isupper())
print(string.istitle())
print(string.isspace())
True
True
True
False
False
False
"""
# name = (input())
# if name.istitle() == True:
#      print("Слово начинается с заглавное буквы")
# else:
#      print("Слово начинается с прописной  буквы")


# #Температура
# tmp = """
#     (-∞ , -30] ОЧЕНЬ холодно!
#     (-30 , 0) ХОЛОДНО
#     0          нуль
#     (0, 20)  замечательно
#     [20, 40)  ЖАРКО
#     [40 , ∞)  ОЧЕНЬ жарко!
#      """
# print(tmp)
# t = int(input("Введите температуру:"))
#
# if (t <= -30):
#     print("ОЧЕНЬ холодно!", t)
# if ( t < 0 ):
#     if (t > -30):
#         print("Холодно", t)
# if (t == 0):
#     print("Нуль", t)
# if (t > 0):
#     if (t < 20):
#         print("замечательно", t)
# if (t >= 20):
#     if (t < 40):
#         print("ЖАРКО")
# if (t >= 40):
#         print("Очень Жарко", t)


# name = "Николай"
# age = 35
# if age == 35:
#     print("Age is equal to 33")
#     if name == "Николай":
#         print("Привет,", name + str('!'))
#     else: print(name)
# else:
#     print(age)


# a = list(range(0,10))
# print(a[0:5])
# print(a[2:len(a)])
# print(a[:])
# print(a[::2])
# print(a[0:6:2])
# print(a[-1])
# print(a[-2])
# print(a[2:-2])
# print(a[::-1])


#
# from pprint import pprint as pretty_print
# from copy import copy, deepcopy
# nums_2d = [
#      [1,2,3,4,5,6,7],
#      [8,9,10,11,12,13,14,15],
#      [16,17,18,19,20,21,22]
#         ]
# # print(nums_2d)
# # print(nums_2d[1][3])
# # print(nums_2d[1][1])
# # print()
# nums_2d[2][1] = - 5 # before 17
# # pretty_print(nums_2d)
#
# letters = ["A","B","C","D","E"]
# # letters_2d = [letters,letters,letters]
# letters_2d = [copy(letters),copy(letters),copy(letters)]
# pretty_print(letters_2d)
# letters_2d[0][0] = 'F'
# print()
# pretty_print(letters_2d)


# numbers = [3.14, -5, 10, 10**4, 17]
# hello_world = "HelloWorld"
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))
# print(max(hello_world))
# print(min(hello_world))
# print(len(hello_world))
# 1.2345e3
# a = 0.0012345 * 10 ** 6
# b = 0
# b = 12345 / 10000000
#
# # b = 2345е3=0.0012345=12345/10000000
# print(b)
# print(a)

# alpha1 = ["a","f","b","e","d"]
# alpha2 = ["g","i","h"]
# alpha3 = "jklmnopqrstuvwxyz"
# alpha1.sort()
# alpha2.sort()
# # alpha3.sort()
# print(alpha1,alpha2,alpha3,sep="\n")
# alpha1.insert(2, "c")
# print(alpha1)
# alpha1 = ''.join(alpha1)
# alpha2 = ''.join(alpha2)
# print(alpha1)
# print(alpha2)
# alphabet = (alpha1 + alpha2 + alpha3)
# print(alphabet)

# number = [5, -6 , 2, 4, -5, 1]
# names = ["Зачет", "One", "Two"]
# print(names)
# del names[1]
# print(names)


# ВЫВОД  ФОРМАТОВ
# n = 11
# f = 1.23456e3
# s = "Python"
# print("my numbers is {:d}".format(n))
# print("my numbers is {:f}".format(f))
# print("my numbers is {:.3f}".format(f))
# print("my numbers is {:020.3f}".format(f))
# print("{name} own(s) {amount} of {object}".format(
#         name = "Nikolay",
#         amount = 32,
#         object = "human"))


# There are many format types such as:
# e - exponents
# b - binary (base 2)
# o -  octal (base 8)
# d  - decimal (base 10)
# x  - hexadeimal (base 16)
#  f - float (decimal numbers)
#  s - string
# Двухмерные массивы
# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# # print(a)
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row],[col] = -1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for  di in range(-1, 2):
#                  for dj in range(-1, 2):
#                      ai = i + di
#                      aj = j + dj
#                      #(ai, aj)
#                      if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
# print()
#


# поиск минимального значение в списке
# a = [int(i) for i in input().split()]
# m = a[0]
# for element in a:
#     if m > element:
#        m = element
# print(m)


# i = 0
# cnt = 0
# j = 0
# gemone2 = []
# while j <= (len(gemone) - 1):
#      print(gemone[j])
#      j += 1
#


# 1  Выбираем из двух чисел наибольшее и проверяем, делится ли оно на меньшее.
#    Если делится, то это число и есть НОК этих двух чисел.
#
# 2  Если наибольшее число не делится на меньшее, умножаем его на 2
#    и проверяем, делится ли теперь.
#
# 3  Если после умножения на два новое число не делится на меньшее, умножаем
#    на 3,4,5 и так далее до тех пор, пока новое число не станет делится
#    на меньшее. Это новое число и есть НОК (наименьшее общее кратное).
#
# a = int(input()) #биологи
# b = int(input()) #информатики
#
# m = max(a, b)
# n = min(a, b)
# i = 1
# while i <= n:
#  if (m * i) % n == 0:
#     d = (m * i)
#     break
#  else:
#    i += 1
#
# print(d)


'''
Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится спать после полуночи в H часов и M минут.
Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через X минут после того,
 как она ляжет спать.
На стандартный ввод, каждое в своей строке, подаются значения X, H и M. Гарантируется, что Катя должна проснуться в тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.
'''

# x = int(input())
# h = int(input())
# m = int(input())
# a = (h * 60 + m) + x
# xh = (a // 60)
# xm = (a % 60)
# print(xh,xm,sep='\n')

# # print('hour',)
# # if (h >= 0) and (60 > m >= 0):

# x = int(input())

# x = int(input())
# h = (x // 60)
# m = (x % 60)
# # print('hour',)
# # if (h >= 0) and (60 > m >= 0):
#
# print(int(h))
# print(int(m))


'''[a; b] = {х : α ≤ х ≤ b} — отрезок (сегмент, замкнутый промежуток);
(a; ) = {х : а < х < b} — интервал (открытый промежуток);
[a;b) = {х : а ≤ х < b};
(a; b] = {х : а < х ≤ b} — полуоткрытые интервалы (или полуоткрытые отрезки);
(-∞; b] = {х : х ≤ b};                           [α, +∞) = {х : х ≥ α};
(-∞; b) = {х : х <b};                         (а, +∞) = {х : х > а};
(-∞, ∞) = {х : -∞<х<+∞} = R — бесконечные интервалы (промежутки).
 Просто запомните, что для круглых скобок "()" строгая < или >. Для квадратных скобок "[]" нестрогая <= или >=.
Задача (−15,12]∪(14,17)∪[19,+∞)
'''
# x = int(input())
# print((-15) < x <= 12 or 14 < x <17 or 19 <= x)


# b = input();
# if (int(b[0])+int(b[1])+int(b[2]) == int(b[3])+int(b[4])+int(b[5])):
#     print("Счастливый");
# else:
#     print("Обычный");

# ''''Решил''''
# ticket = input()
# i = 0
# j = len(ticket)
# sum = 0
# sum2 = 0
#
# while i < j:
#    if i < j / 2:
#       sum += int(ticket[i])
#       i += 1
#    else:
#        sum2 += int(ticket[i])
#        i += 1
# if sum == sum2:
#       print('Счастливый')
# else: print('Обычный')

#
# if (ticket[0] + ticket[1] + ticket[2]) == (ticket[3] + ticket[4] + ticket[5]):
#     print("Счастливый")
# else: print("Обычный")


# n = int(input()) b =(int(i) for i in input().split())
# ''''Сдал'''
# n=int(input())
# for n in a:
#      if (n % 10) == 1 and not(n % 100) == 11: print(n,"программист")
#      elif ((n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4)) and (not(n % 100) == 12 and not(n % 100) == 13 and not(n % 100) == 14):print(n,"программиста")
#      else: print(n,"программистов")


# n = int(input())
# if (n % 10 == 1 and n%100 != 11):
#     print(n, 'программист')
# elif (n % 10 in [2, 3, 4] and not n % 100 in [12, 13, 14] ):
#     print(n, 'программиста')
# else:
#     print(n, 'программистов')

# + Если у вас что- то не получается, проверьте по таким числам: 0, 1, 10, 9, 11, 14, 16, 20, 21, 60, 92, 100, 700, 101, 999, 1000, 754, 689
# Решено
# n = int(input())
# if not(0 <= n <= 1000): exit()
# if (n % 10) == 1 and not(n % 100) == 11: print(n,"программист")
# if ((n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4)) and (not(n % 100) == 12 and not(n % 100) == 13 and not(n % 100) == 14):
#     print(n,"программиста")
# if not((n % 10) == 1 and not(n % 100) == 11 or ((n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4)) and (not(n % 100) == 12 and not(n % 100) == 13 and not(n % 100) == 14)):
#     print(n,"программистов")


#
#
# fi = (input())
# pi = 3.14
# if fi == "треугольник":
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2.0
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(S)
# elif fi == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     S = a * b
#     print(S)
# else:
#     a = float(input())
#     r = a * a * pi
#     print(r)

# s = {1: lambda r: 3.14  * r**2, 2: lambda a, b: a * b, 3: lambda a, b, c: ((a+b+c)/2*(b+c-a)/2*(a+c-b)/2*(a+b-c)/2)**0.5}
# f = {'круг': 1, 'прямоугольник': 2, 'треугольник': 3}
# args = [float(input()) for _ in range(f[input()])]
# print(s[len(args)](*args))


# Формула герона треугольник, когда стороны известны
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2.0
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)


# Високосный год
#  n = int(input())
# if (1900 <= n <= 3000):
#     if (((n % 4) == 0) and not(n % 100) == 0) or (n % 400) == 0:
#         print('Високосный')
#     else:
#         print('Обычный')


# if (900 <= n <= 3000):
#     if ((n % 4) and (n % 100) == 0) or (n % 400) == 0:
#         print('Високосный')
#     else:
#         print('Обычный')

'''
x + y	Сложение
x * y	Умножение
x / y	Деление
x // y	Получение целой части от деления
x % y	Остаток от деления
'''

# A, где  хотя бы A часов в сутки.
# B,  но пересыпать тоже вредно и не стоит спать более B часов
# H,  Сейчас Аня спит H часов в сутки

# A = int(input()) # Рекомендации
# B = int(input()) # Вредно столько спать
# H = int(input()) # Сколько сплю сейчас
#
# if ((A <= H) and (H <= B)):
#     print('Это нормально')
# elif (H < A):
#     print('Недосып')
# else:
#     print('Пересып')

#
# a = int(input())
# b = int(input())
# x = int(input())
# print(("Недосып", "Это нормально", "Пересып")[(x > b) - (x < a) + 1])
#
# То, что в скобках — это tuple (по сути неизменяемый список). В квадратных скобках, соответственно, индекс.
#
# При недосыпе получается: False − True + 1 = 0 − 1 + 1 = 0
#
# При нормальном сне: False − False + 1 = 0 − 0 + 1 = 1
#
# При пересыпе: True – False + 1 = 1 − 0 + 1 = 2


# if ((A <= H) and (H <= B)) == True:
#     print('Это нормально')
# elif (H < A):
#     print('Недосып')
# elif (H > B):
#     print('Пересып')


'''
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал
(−15,12]∪(14,17)∪[19,+∞)

и False в противном случае (регистр символов имеет значение).

Обратите внимание на разные скобки, используемые для обозначения интервалов.
В задании используются полуоткрытые и открытые интервалы. Подробнее про это вы можете прочитать, например, на википедии (полуинтервал, промежуток).

[a; b] = {х : α ≤ х ≤ b} — отрезок (сегмент, замкнутый промежуток);
(a; ) = {х : а < х < b} — интервал (открытый промежуток);
[a;b) = {х : а ≤ х < b};
(a; b] = {х : а < х ≤ b} — полуоткрытые интервалы (или полуоткрытые отрезки);
(-∞; b] = {х : х ≤ b};                           [α, +∞) = {х : х ≥ α};
(-∞; b) = {х : х <b};                         (а, +∞) = {х : х > а};
(-∞, ∞) = {х : -∞<х<+∞} = R — бесконечные интервалы (промежутки).
'''

# (−15,12]∪(14,17)∪[19,+∞)
# n = int(input())
# for n in range(-20, 21):
#         print((-15 < n <= 12) or (14 < n > 17) or (n >= 19), n)
#


# a,b,c = int(input()), int(input()), int(input())
# mylist = []
# mylist += [a,b,c]
# aa = max(mylist)
# bb = min(mylist)
# print(aa,bb, (a + b + c) - max(mylist) - min(mylist), sep='\n')

'''
a, b, c = int(input()), int(input()), int(input())
x = max(a, b, c)
y = min(a, b, c)
z = (a + b + c) - (x + y)
print (str(x) + "\n" + str (y) + "\n" + str(z))
'''

'''
x = [int(input()) for i in range(3)]
print(max(x),"\n", min(x),"\n", sum(x) - max(x) - min(x))
'''
'''
Лучший результат
a,b,c = int(input()), int(input()), int(input())

if a < b:
	a, b = b, a
if a < c:
	a, c = c, a
if b > c:
	b, c = c, b
print(a)
print(b)
print(c)
'''

'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.

# '''
# a, b =(int(i) for i in input().split())
# mylist = []
# a = int(input())
# b = int(input())
# c = int(input())
# aa = a
# bb = b
# cc = c
# mylist += [a]
# mylist += [b]
# mylist += [c]
# Ma = max(mylist)
# Mi = min(mylist)
# # print(mylist)
# i = 1
#
#


# def max2(z):
#         s=0
#         b=0
#         for x in range(len(z)):
#             if z[x] > s:
#                 s=z[x]
#                 b=x
#         print b


# Алгоритм является однопроходным поэтому может работать на произвольно большом вводе.
# def my_max(iterable):
#     it = iter(iterable)   # получаем итератор
#     try:
#         max_ = next(it)   # получаем первый элемент
#     except StopIteration: # пустой ввод -- нет элементов
#         raise ValueError('max() arg has no items')
#     for item in it:       # для каждого из оставшихся элементов
#         if max_ < item:   # если элемент больше,
#             max_ = item   # он становится новым максимумом
#     return max_


# # Задача: (−15,12]∪(14,17)∪[19,+∞)
# ''''' Подсказка:
# Когда там скобка "("  большее а когда скобка "]" то это меньше или равон. Например
#  (−15,12] это значит что хх больше чем 15 и меньше или равно 12.'''''
#
# # n = int(input())
# a = list(range(-100,100))
# countFalse = 0
# countTrue = 0
# f = []
# t = []
# for n in a:
#     if ((-15 < n <= 12) or (14 < n > 17) or (19 < n )) == True:
#        # print('True',n)
#        countTrue += 1
#        t += n
#     else:
#          # print('False',n)
#          countTrue += 1
#          f += n
# # print(countTrue,countTrue)
# print(t,'\n',f)


# a = 3
# b = 4
# c = 5
# p = (float((a+b+c) / 2))
# x = p * (p - a) * (p - b) * (p - c)
# S = (pow(x, 0.5))
# print(S)


# Списки / list / массив
# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=9
# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# print(areas[:6])
# print(areas[::-4])


# print(list(range(1, 8)))

# total = 0
# for i in range(1, 5):
#     total += i
# print(total)
#


# s = list(range(1, 5))
# print(s)
# print(type(s))


# Циклы

# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)

# import logging
# # logging.basicConfig(filename='test', level=logging.debug,
# #                     format='%(asctime)s:%(levelname)s:%(message)s')
#
# given_list = [7,5,4,4,3,1,-2,-3,-5, -7] # count i < 0
# j = len(given_list) - 1
# total2 = 0
# while given_list[j] < 0:
#     total2 += given_list[j]
#     j -= 1
# logging.warning(print(total2))

# Итого1 = 0
# for i in range(1,100):
#     if i % 3 == 0 or i % 5 == 0:
#         Итого1 += i
# print(Итого1)


# 4Просуммировать элеметы 1..100, где они делятся на 4 и 5.
# Итого = 0
# for i in range(1,100):
#     if i % 3 == 0:
#         Итого += i
#     elif i % 5 == 0:
#         Итого += i
# print(Итого)


# 3
# given_list2 = [5,4,4,3,1,-2,-3,-5]
# total5 = 0
# i = 0
# while True: # True always == true
#     total5 += given_list2[i]
#     i += 1
#     if given_list2[i] <= 0:
#         break
# print(total5)


# 2
# given_list2 = [5,4,4,3,1,-2,-3,-5]
# total4 = 0
# for element in given_list2:
#     if element <= 0:
#         break
#     total4 += element
# print(total4)

# 1
# given_list = [5, 4, 4, 3, 1]
# total3 = 0
# i = 0
# # given_list = [5, 4, 4, 3, 1, -2, -3, -5]  while given_list[i] > 0:
# while i < len(given_list) and given_list[i] > 0:
#        total3 += given_list[i]
#        i += 1
# print(given_list)
# print(total3)
# print(type(total3))
# [5, 4, 4, 3, 1, -2, -3, -5]
# 17
# <class 'int'>
