Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,3,34,5,6,7]
>>> b = a
>>> a is b
True
>>> a[0] = "Hello"
>>> a
['Hello', 3, 34, 5, 6, 7]
>>> b
['Hello', 3, 34, 5, 6, 7]
>>> c = a[:]
>>> c
['Hello', 3, 34, 5, 6, 7]
>>> a is c
False
>>> a[0] = 0
>>> a
[0, 3, 34, 5, 6, 7]
>>> c
['Hello', 3, 34, 5, 6, 7]
>>> b
[0, 3, 34, 5, 6, 7]
>>> a = [12,3,34,[5,6,7],10,11]
>>> a[3]
[5, 6, 7]
>>> b = a
>>> b
[12, 3, 34, [5, 6, 7], 10, 11]
>>> a
[12, 3, 34, [5, 6, 7], 10, 11]
>>> c = a[:]
>>> c
[12, 3, 34, [5, 6, 7], 10, 11]
>>> a
[12, 3, 34, [5, 6, 7], 10, 11]
>>> a[0] = "Hello"
>>> a
['Hello', 3, 34, [5, 6, 7], 10, 11]
>>> c
[12, 3, 34, [5, 6, 7], 10, 11]
>>> a[3][0] = "Hello"
>>> a
['Hello', 3, 34, ['Hello', 6, 7], 10, 11]
>>> b
['Hello', 3, 34, ['Hello', 6, 7], 10, 11]
>>> c
[12, 3, 34, ['Hello', 6, 7], 10, 11]
>>> a[3]
['Hello', 6, 7]
>>> import copy
>>> c = copy.deepcopy(a)
>>> c
['Hello', 3, 34, ['Hello', 6, 7], 10, 11]
>>> a
['Hello', 3, 34, ['Hello', 6, 7], 10, 11]
>>> a[3][0] = "Bye"
>>> a
['Hello', 3, 34, ['Bye', 6, 7], 10, 11]
>>> c
['Hello', 3, 34, ['Hello', 6, 7], 10, 11]
>>> 
