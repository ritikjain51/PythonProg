Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=["hello","(1,2,3,4)","50","[1,2,3,4]"]
>>> s="|"
>>> x
['hello', '(1,2,3,4)', '50', '[1,2,3,4]']
>>> s
'|'
>>> s.join(x)
'hello|(1,2,3,4)|50|[1,2,3,4]'
>>> x = ['hello', (1,2,3,4), 50, [5,6,7,8]]
>>> '|'.join(x[0])
'h|e|l|l|o'
>>> '|'.join(x[1])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    '|'.join(x[1])
TypeError: sequence item 0: expected str instance, int found
>>> '|'.join([str(i) for i in x[1]])
'1|2|3|4'
>>> for i in x:
	if (type(i) == str):
		print ('|'.join(i), end = "")
	else:
		print ('|'.join([str(j) for j in i]), end = '')

		
h|e|l|l|o1|2|3|4Traceback (most recent call last):
  File "<pyshell#16>", line 5, in <module>
    print ('|'.join([str(j) for j in i]), end = '')
TypeError: 'int' object is not iterable
>>> for i in x:
	if (type(i) == str):
		print ('|'.join(i), end = "")
	elif (type(i) == int):
		print (f'|{i}')
	else:
		print ('|'.join([str(j) for j in i]), end = '')
	print ('|')

	
h|e|l|l|o|
1|2|3|4|
|50
|
5|6|7|8|
>>> for i in x:
	if (type(i) == str):
		print ('|'.join(i), end = "")
	elif (type(i) == int):
		print (f'|{i}', end = '')
	else:
		print ('|'.join([str(j) for j in i]), end = '')
	print ('|', end = '')

	
h|e|l|l|o|1|2|3|4||50|5|6|7|8|
>>> for i in x:
	if (type(i) == str):
		print ('|'.join(i), end = "")
	elif (type(i) == int):
		print (f'{i}', end = '')
	else:
		print ('|'.join([str(j) for j in i]), end = '')
	print ('|', end = '')

	
h|e|l|l|o|1|2|3|4|50|5|6|7|8|
>>>  
