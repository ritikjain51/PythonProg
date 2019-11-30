Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4]
>>> type(a) == list
True
>>> type(a) == int
False
>>> 
=================== RESTART: C:/Users/dell/Desktop/base.py ===================
>>> 
=================== RESTART: C:/Users/dell/Desktop/base.py ===================
>>> a = 'hello'
>>> type(a)
<class 'str'>
>>> b = "world"
>>> type(b)
<class 'str'>
>>> a.capitalize()
'Hello'
>>> e = "Hello World. I am from samyak"
>>> e.capitalize()
'Hello world. i am from samyak'
>>> a.upper()
'HELLO'
>>> a.lower()
'hello'
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isalpha()
True
>>> a.isalnum()
True
>>> d = '12345'
>>> d.isalnum()
True
>>> a.isascii()
True
>>> 'Hello.i am'.capitalize()
'Hello.i am'
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.count()
TypeError: count() takes at least 1 argument (0 given)
>>> a.count('h')
1
>>> a
'hello'
>>> a.count('H')
0
>>> a.encode()
b'hello'
>>> a.encode('ascii')
b'hello'
>>> import re
>>> re.IGNORECASE
<RegexFlag.IGNORECASE: 2>
>>> r = re.compile('\S')
>>> a += b
>>> a
'helloworld'
>>> a = 'Hello World'
>>> a
'Hello World'
>>> r.find(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    r.find(a)
AttributeError: 're.Pattern' object has no attribute 'find'
>>> r.findall(a)
['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
>>> r = re.compile('\S*')
>>> r.findall(a)
['Hello', '', 'World', '']
>>> r = re.compile('\S@\S')
>>> c = 'samyak@samyakinfortech.com'
>>> r.findall(c)
['k@s']
>>> r = re.compile('\S@\S?')
>>> r.findall(c)
['k@s']
>>> r = re.compile('\S*@\S*')
>>> r.findall(c)
['samyak@samyakinfortech.com']
>>> e = a + c + b
>>> e
'Hello Worldsamyak@samyakinfortech.comworld'
>>> r.findall(e)
['Worldsamyak@samyakinfortech.comworld']
>>> 
