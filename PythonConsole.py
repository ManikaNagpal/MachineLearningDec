Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3]
>>> for i,j in enumerate(a):
	print(i,j)

	
0 1
1 2
2 3
>>> arr = [[1,2], [3,4], [5,6]]
>>> for i,j in enumerate(arr):
	print(i,j)

	
0 [1, 2]
1 [3, 4]
2 [5, 6]
>>> def func_1(address):
	print(address)

	
>>> func_1('xyz', 'abc')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    func_1('xyz', 'abc')
TypeError: func_1() takes 1 positional argument but 2 were given
>>> def func_1(*address):
	print(address)

	
>>> func_1('xyz', 'abc')
('xyz', 'abc')
>>> def sum(x,y):
	return x + y

>>> sum(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sum(1,2,3,4)
TypeError: sum() takes 2 positional arguments but 4 were given
>>> def sum(x,y, *z):
	return x + y

>>> sum(1,2,3,4)
3
>>> def sum(**z):
	print(z)

	
>>> sum(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sum(1,2,3,4)
TypeError: sum() takes 0 positional arguments but 4 were given
>>> def sum(z):
	print(z)

	
>>> d = {"id" : 101, "name" : "Ram"}
>>> sum(**d)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sum(**d)
TypeError: sum() got an unexpected keyword argument 'id'
>>> sum(d)
{'id': 101, 'name': 'Ram'}
>>> def sum(**z):
	print(z)

	
>>> sum
<function sum at 0x000001AD4D432BF8>
>>> sum()
{}
>>> sum(d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sum(d)
TypeError: sum() takes 0 positional arguments but 1 was given
>>> def sum(d,**z):
	print(z)

	
>>> sum(d)
{}
>>> def sum(d,**z):
	print(d,z)

	
>>> sum(d)
{'id': 101, 'name': 'Ram'} {}
>>> def sum(*x):
	print(x)

	
>>> sum(d)
({'id': 101, 'name': 'Ram'},)
>>> def sum(**kwargs):
	print(kwargs)

	
>>> sum('name' = "Ram")
SyntaxError: keyword can't be an expression
>>> def sum_1(**k):
	print(k)

	
>>> sum('name' = "Ram")
SyntaxError: keyword can't be an expression
>>> sum_1('name' = "Ram")
SyntaxError: keyword can't be an expression
>>> sum_1(name = "Ram")
{'name': 'Ram'}
>>> d
{'id': 101, 'name': 'Ram'}
>>> import pandas as pd
>>> dataset = pd.DataFrame(d)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dataset = pd.DataFrame(d)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 275, in __init__
    mgr = self._init_dict(data, index, columns, dtype=dtype)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 411, in _init_dict
    return _arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 5496, in _arrays_to_mgr
    index = extract_index(arrays)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 5535, in extract_index
    raise ValueError('If using all scalar values, you must pass'
ValueError: If using all scalar values, you must pass an index
>>> dataset = pd.DataFrame({'id' : [101,102,103], 'name' : ['Ram', 'Shyam', 'Amit']})
>>> dataset
    id   name
0  101    Ram
1  102  Shyam
2  103   Amit
>>> sum_1(d = dataset)
{'d':     id   name
0  101    Ram
1  102  Shyam
2  103   Amit}
>>> 
