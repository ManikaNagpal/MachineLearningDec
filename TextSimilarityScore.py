Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str_1 = "Hello this is python programming and python is used for machine learning"
>>> word_tokens = str_1.split()
>>> word_tokens
['Hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> word_tokens = set(str_1.split())
>>> word_tokens
{'is', 'python', 'machine', 'programming', 'Hello', 'this', 'for', 'learning', 'and', 'used'}
>>> str_2 = "This is R Programming and R is used for data analysis"
>>> from collections import *
>>> def DistCalc(str_1, str_2):
	str_split_1 = set(str_1.split())
	str_split_2 = set(str_2.split())
	return len(str_split_1 & str_split_2) / len(str_split_1 | str_split_2)

>>> DistCalc("Hello","Hello")
1.0
>>> DistCalc("Hello","Hello World")
0.5
>>> DistCalc("Hello Everyone","Hello World")
0.3333333333333333
>>> DistCalc(str_1, str_2)
0.26666666666666666
>>> str_1 & str_2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str_1 & str_2
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> set(str_1) & set(str_2)
{'o', 'l', 'n', 'd', 'i', 'a', 'g', 's', 'r', ' ', 'h', 'm', 'f', 't', 'y', 'u', 'e'}
>>> str_!
SyntaxError: invalid syntax
>>> str_1
'Hello this is python programming and python is used for machine learning'
>>> x = set(str_1.split())
>>> x
{'is', 'python', 'machine', 'programming', 'Hello', 'this', 'for', 'learning', 'and', 'used'}
>>> y = set(str_2.split())
>>> y
{'is', 'analysis', 'for', 'and', 'used', 'R', 'This', 'Programming', 'data'}
>>> x & y
{'is', 'for', 'and', 'used'}
>>> x = set(str_1.lower().split())
>>> x
{'is', 'python', 'machine', 'programming', 'this', 'for', 'learning', 'hello', 'and', 'used'}
>>> y = set(str_2.lower().split())
>>> x
{'is', 'python', 'machine', 'programming', 'this', 'for', 'learning', 'hello', 'and', 'used'}
>>> y
{'is', 'analysis', 'programming', 'this', 'for', 'and', 'used', 'r', 'data'}
>>> x & y
{'is', 'this', 'programming', 'for', 'and', 'used'}
>>> x | y
{'is', 'python', 'analysis', 'machine', 'programming', 'this', 'for', 'learning', 'hello', 'and', 'used', 'r', 'data'}
>>> len(x & y) / len(x | y)
0.46153846153846156
>>> 
