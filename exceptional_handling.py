'''
Exceptions are the errors which being break by the program or user.

We have to handle the exception to excecute our program or software smoothly.

In exception handling we have 3 main blocks.

    1. Try block
    2. Except block / Catch block
    3. Finally block

Keywords to use in Exceptional Handling.
try, except, finally, raise
'''

try:

    raise IOError('sadad')
    open('f1.txt')
    print (5 + str(5))
    raise RuntimeError('Sir! Something went wrong.')
    
except ZeroDivisionError as e:
    print (str(e))
except RuntimeError as e:
    print (str(e))
except AttributeError as e:
    print (str(e))
except TypeError as e:
    print (str(e))
except FileNotFoundError as e:
    print (str(e))
except Exception as e:
    print (str(e))



try:
    f = open('file.txt', 'w+')
    f.append('asdas')
    f.close()
except Exception as e:
    print (str(e))
finally:
    f.close()

print (f)



'''

Task:



'''
try:
    f = open('nmn.txt','w+')
    f.append('aaaaaa')
    f.close()
except Exception as e:
    print (str(e))
finally:
    f.close()
print (f)
    
