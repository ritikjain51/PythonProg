Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3,4,5,6,7,8,9,99,100]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100]
>>> a.append(101)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> b=a.copy()
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> b.clear()
>>> b
[]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> a.count(9)
1
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> a.extend=(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.extend=(b)
AttributeError: 'list' object attribute 'extend' is read-only
>>> b=a.extend(a)
>>> b
>>> 
>>> b=a.copy()
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> b=a.extend(a)
>>> b
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> a.index(9)
8
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> a.insert(2,999)
>>> a
[1, 2, 999, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> a.pop(888)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop(888)
IndexError: pop index out of range
>>> a.remove(999)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 101]
>>> a.reverse()
>>> a
[101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1, 101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1, 101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1, 101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> a
[101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1, 101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1, 101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1, 101, 100, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> a.sort()
>>> a
[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 99, 99, 99, 99, 100, 100, 100, 100, 101, 101, 101, 101]
>>> 
