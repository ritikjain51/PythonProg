Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=[[1,2,3,4],"hello",50,(5,6,7,8)]
>>> 
>>> x
[[1, 2, 3, 4], 'hello', 50, (5, 6, 7, 8)]
>>> for i in x:
	if (type(i) == int):
		print (i)
	else:
		print(i[::-1])
