x=["hello",(1,2,3,4),50,[5,6,7,8]]
for i in x:
	if (type(i) == str):
		print ('|'.join(i), end = "")
	elif (type(i) == int):
		print (f'{i}', end = '')
	else:
		print ('|'.join([str(j) for j in i]), end = '')
	print ('|', end = '')
