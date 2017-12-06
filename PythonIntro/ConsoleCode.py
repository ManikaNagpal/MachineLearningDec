Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> a = 10
>>> b = 12
>>> print(a+b)
22
>>> a = 13
>>> b = 5
>>> a/b
2.6
>>> a//b
2
>>> a*a
169
>>> a*a*a
2197
>>> a**8
815730721
>>> type(a)
<class 'int'>
>>> a = "Hello"
>>> type()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(a)
<class 'str'>
>>> a = "10"
>>> int(a)
10
>>> a = "Hello"
>>> a[0]
'H'
>>> a[1]
'e'
>>> a = "Hello world"
>>> a[0:4]
'Hell'
>>> a[0:]
'Hello world'
>>> a[:10]
'Hello worl'
>>> a[:100]
'Hello world'
>>> type(a)
<class 'str'>
>>> id(a)
2045177668656
>>> a = 10
>>> id(a)
1516423120
>>> id(10)
1516423120
>>> c = 10
>>> id(c)
1516423120
>>> i = c
>>> list_1 = [1,2,3,4,5,"Hello", "Hi",10.5,True]
>>> type(list_1)
<class 'list'>
>>> tuple_1 = (1,2,3,4,5,"Hello", "Hi",10.5,True)
>>> type(tuple_1)
<class 'tuple'>
>>> list_1[0]
1
>>> list_[0:5]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list_[0:5]
NameError: name 'list_' is not defined
>>> list_1[0:5]
[1, 2, 3, 4, 5]
>>> list_1[-1]
True
>>> list_1[-2]
10.5
>>> list_1[0:-1]
[1, 2, 3, 4, 5, 'Hello', 'Hi', 10.5]
>>> list_1[::-1]
[True, 10.5, 'Hi', 'Hello', 5, 4, 3, 2, 1]
>>> list_1[-1:0]
[]
>>> list_1 = [12,11,56,1,5,67,23,22,9]
>>> list_1.sort()
>>> list_1
[1, 5, 9, 11, 12, 22, 23, 56, 67]
>>> list_1.sort(reverse = True)
>>> list_1
[67, 56, 23, 22, 12, 11, 9, 5, 1]
>>> list_1 = [12,11,56,1,5,67,23,22,9]
>>> list_2 = sorted(list_1)
>>> list_2
[1, 5, 9, 11, 12, 22, 23, 56, 67]
>>> list_1
[12, 11, 56, 1, 5, 67, 23, 22, 9]
>>> tuple_1[0]
1
>>> list_1[0] =
SyntaxError: invalid syntax
>>> list_1[0] = "Hello"
>>> list_1
['Hello', 11, 56, 1, 5, 67, 23, 22, 9]
>>> tuple_1[0] = "Hello"
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    tuple_1[0] = "Hello"
TypeError: 'tuple' object does not support item assignment
>>> dict_1 = {"id":101, "name": "Ram", "age":21}
>>> dict_1
{'id': 101, 'name': 'Ram', 'age': 21}
>>> dict_1[0]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dict_1[0]
KeyError: 0
>>> dict_1['id']
101
>>> dict_1['salary'] = 12000
>>> dict_1
{'id': 101, 'name': 'Ram', 'age': 21, 'salary': 12000}
>>> set_1 = {12,11,45,56,87}
>>> 
