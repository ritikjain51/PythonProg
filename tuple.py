Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4,5,6,7,8,9)
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a.count(6)
1
>>> a.index(5)
4
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a(5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a(5)
TypeError: 'tuple' object is not callable
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a[5]
6
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a[1:7]
(2, 3, 4, 5, 6, 7)
>>> 
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a[1:8:2]
(2, 4, 6, 8)
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a.index(3)
2
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a[2]
3
>>> 
