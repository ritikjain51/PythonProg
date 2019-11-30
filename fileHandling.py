##print ('Previously in my file')
##f = open('test.txt')
##print(f.read())
##f.close()
##
##f = open('test.txt', 'w+')
####f.write('Hello World! How are you!')
####f.writelines('How are you!')
##f.write('Hello Samyak!!')
##
##f.close()
##
##print ('After Writing in the file')
##f = open('test.txt')
##print(f.readlines())
##f.close()
##
##
#### Append function
##
##f = open('test.txt', 'a')
##f.write('Hello')
##f.close()
##
##
##print ('After Appending in the file')
##f = open('test.txt')
##print(f.readlines())
##f.close()
##
#### Seek function
##
##f = open('test.txt')
##
##'''
##!!Hello']
##>>> f
##<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
##>>> f.read()
##'Hello Samyak!!Hello'
##>>> f.read()
##''
##>>> f.seek(0)
##0
##>>> f.read()
##'Hello Samyak!!Hello'
##>>> f.seek(6)
##6
##>>> f.read()
##'Samyak!!Hello'
##>>> f.writable()
##False
##>>> f.readable()
##True
##>>> f.errors
##'strict'
##>>> f.fileno
##<built-in method fileno of _io.TextIOWrapper object at 0x00000168217DC558>
##>>> f.fileno()
##3
##>>> f.line_buffering
##False
##>>> f1 = open('test.txt', buffering = 10)
##>>> f1.read()
##'Hello Samyak!!Hello'
##>>> f.line_buffering
##False
##>>> f1.line_buffering
##False
##>>> f1
##<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
##>>> print (f1)
##<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
##>>> f1.mode
##'r'
##>>> f1.seekable
##<built-in method seekable of _io.TextIOWrapper object at 0x0000016820EEEDC8>
##>>> f1.seekable()
##True
##>>> f.tell()
##19
##>>> f.read()
##''
##>>> f.seek(0)
##0
##>>> f.tell()
##0
##>>> f.seek(4)
##4
##>>> f.tell()
##4
##>>> f.encoding
##'cp1252'
##>>> f1.close()
##>>> f1 = open('test.txt', encoding = 'UTF-8')
##>>> f1.encoding
##'UTF-8'
##>>> f.name
##'test.txt'
##>>> 
##'''
##


import os


print (os.listdir('.'))

print (os.getcwd())

print (os.path.exists('.\\ritik'))

##print(os.mkdir('naman'))

##os.mkdir('./naman1/f1/f2')

os.makedirs('./naman1/f1/f2')

