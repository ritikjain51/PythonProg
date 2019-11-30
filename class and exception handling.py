Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
 Name:asd address:adas contact123122
>>> f = open('file.txt', 'w')
>>> f.write('Data')
4
>>> f.write()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f.write()
TypeError: write() takes exactly one argument (0 given)
>>> f.write('')
0
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
 Name:asd address:adas contact123122
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
 Name:asd address:adas contact123122
>>> s.get_gender()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.get_gender()
AttributeError: 'student' object has no attribute 'get_gender'
>>> s.get_roll_number()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.get_roll_number()
AttributeError: 'student' object has no attribute 'get_roll_number'
>>> print (s)
 Name:asd address:adas contact123122
>>> s
 Name:asd address:adas contact123122
>>> s.put_gender('F')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.put_gender('F')
AttributeError: 'student' object has no attribute 'put_gender'
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Nameasd addressadas contact123122 genderM roll_number1231
>>> s.get_gender()
'M'
>>> s.get_roll_number()
1231
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Nameasd addressadas contact123122 genderM roll_number1231
>>> s.save_file()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.save_file()
  File "C:\Users\dell\Desktop\opps_task.py", line 103, in save_file
    f.write(self)
TypeError: write() argument must be str, not student
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Nameasd addressadas contact123122 genderM roll_number1231
>>> s.save_file()
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Name:asd address:adas contact:123122 gender:M roll_number:1231
>>> s.save_file()
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Name:asd address:adas contact:123122 gender:M roll_number:1231
>>> s.save_file()
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Name:asd address:adas contact:123122 gender:M roll_number:1231
>>> f = s.save_file()
>>> f.mode
'a+'
>>> f.write('data')
4
>>> f.close()
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Name:asd address:adas contact:123122 gender:M roll_number:1231
>>> f = s.save_file()
>>> f.close()
>>> f = s.save_file()
>>> f.close()
>>> 
================ RESTART: C:\Users\dell\Desktop\opps_task.py ================
Name:asd address:adas contact:123122 gender:M roll_number:1231
>>> s.save_file()
>>> s = student('Ritik', 'asbffsfa', 124124, 'M', 124151)
>>> s.save_file()
>>> s = student('Nama', 'asbffsfa', 124124, 'M', 124151)
>>> s.save_file()
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
Here, i found an error
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
division by zero
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
Sir! Something went wrong.
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
division by zero
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
'list' object has no attribute 'sadsa'
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
5 5
Sir! Something went wrong.
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
Traceback (most recent call last):
  File "C:/Users/dell/Desktop/exceptional_handling.py", line 18, in <module>
    print (5 + str(5))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
unsupported operand type(s) for +: 'int' and 'str'
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
[Errno 2] No such file or directory: 'f1.txt'
>>> a = []
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> x
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
sadad
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
sadad
'_io.TextIOWrapper' object has no attribute 'append'
<_io.TextIOWrapper name='file.txt' mode='w+' encoding='cp1252'>
>>> 
=========== RESTART: C:/Users/dell/Desktop/exceptional_handling.py ===========
sadad
'_io.TextIOWrapper' object has no attribute 'append'
<_io.TextIOWrapper name='file.txt' mode='w+' encoding='cp1252'>
>>> f.closed
True
>>> f = open('file.txt')
>>> f.closed
False
>>> f.close()
>>> f.closed
True
>>> 
