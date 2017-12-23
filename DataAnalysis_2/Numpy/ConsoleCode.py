Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,14,100,101,102,105]
>>> numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,14,100,101,102,105])
array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  14,
       100, 101, 102, 105])
>>> np_arr = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,14,100,101,102,105])
>>> list_1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 100, 101, 102, 105]
>>> np_arr
array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  14,
       100, 101, 102, 105])
>>> type(list_1)
<class 'list'>
>>> type(np_arr)
<class 'numpy.ndarray'>
>>> import sys
>>> sys.getsizeof(list_1)
200
>>> sys.getsizeof(np_arr)
164
>>> np_arr[0]
1
>>> np_arr[-1]
105
>>> np_arr[0:5]
array([1, 2, 3, 4, 5])
>>> np_arr[0:]
array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  14,
       100, 101, 102, 105])
>>> np_arr[1:9:2]
array([2, 4, 6, 8])
>>> np_arr[::-1]
array([105, 102, 101, 100,  14,  12,  11,  10,   9,   8,   7,   6,   5,
         4,   3,   2,   1])
>>> np_arr.sort()
>>> np_arr
array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  14,
       100, 101, 102, 105])
>>> np_arr2 = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
>>> print(np_arr2)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> list_2 = [[1,2,3], [4,5,6], [7,8,9]]
>>> list_2
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> print(list_2)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> np_arr2.shape
(3, 3)
>>> np_arr2.ndim
2
>>> print(np_arr2)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> np_arr2[1,2]
6
>>> np_arr2[1,1]
5
>>> np_arr[1][1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    np_arr[1][1]
IndexError: invalid index to scalar variable.
>>> np_arr2[1][1]
5
>>> np_arr2[2][1]
8
>>> print(np_arr2)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> np_arr2[:, 1]
array([2, 5, 8])
>>> np_arr2[:, 0:2]
array([[1, 2],
       [4, 5],
       [7, 8]])
>>> np_arr2.transpose
<built-in method transpose of numpy.ndarray object at 0x0000021269BA7F80>
>>> np_arr2.transpose()
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
>>> np_arr2.max()
9
>>> np_arr2.min()
1
>>> np_arr2.mean()
5.0
>>> np_arr2.std()
2.5819888974716112
>>> np_arr2.dtype
dtype('int32')
>>> import matplotlib.pyplot as plt
>>> x = numpy.array([1,2,3,4,5,6,7,8,9,10])
>>> numpy.random.random(4)
array([ 0.18254928,  0.2972173 ,  0.03421014,  0.87886255])
>>> numpy.random.random(4) * 10
array([ 1.0027337 ,  7.95550224,  2.86354803,  8.79791938])
>>> numpy.random.random(4) * 100
array([ 62.38405366,  62.05840489,  64.411429  ,  30.44903115])
>>> numpy.random.randint(4) * 100
0
>>> numpy.random.randint(1,100)
87
>>> numpy.random.randint(5)
4
>>> numpy.random.randint(0,5)
1
>>> numpy.random.randint(0,5)
3
>>> numpy.random.randint(0,5)
2
>>> numpy.random.randint(0,100,10)
array([ 2, 59, 30, 29, 66, 27, 98, 52, 89, 43])
>>> y = numpy.random.randint(0,100,10)
>>> x
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> y
array([37, 22, 26, 21, 65, 34, 67, 30, 65, 64])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002126BC08710>]
>>> plt.show()
>>> x.shape
(10,)
>>> a = 10,
>>> a
(10,)
>>> np_arr2
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np_arr2.shape
(3, 3)
>>> 
