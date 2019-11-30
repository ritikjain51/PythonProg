Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = [1,2,3,4]
>>> str(s)
'[1, 2, 3, 4]'
>>> repr(s)
'[1, 2, 3, 4]'
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> try:
	raise OverLimitException('Value does not exist')
except OverLimitException as e:
	print (e.msg)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    raise OverLimitException('Value does not exist')
OverLimitException: <unprintable OverLimitException object>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#7>", line 4, in <module>
    print (e.msg)
AttributeError: 'OverLimitException' object has no attribute 'msg'
>>> try:
	raise OverLimitException('Value does not exist')
except OverLimitException as e:
	print (str(e))

	
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    raise OverLimitException('Value does not exist')
OverLimitException: <unprintable OverLimitException object>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#9>", line 4, in <module>
    print (str(e))
  File "C:/Users/dell/Desktop/Exception_library.py", line 55, in __str__
    return 'Exception Occured: ' + self.msg
AttributeError: 'OverLimitException' object has no attribute 'msg'
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> try:
	raise OverLimitException('Value does not exist')
except OverLimitException as e:
	print (e.msg)

	
Value does not exist
>>> try:
	raise StudentNotExistError('Value does not exist')
except StudentNotExistError as e:
	print (str(e))

	
Student ('Value does not exist',) doesn't exist
>>> try:
	raise StudentNotExistError('18UCSA164')
except StudentNotExistError as e:
	print (str(e))

	
Student ('18UCSA164',) doesn't exist
>>> try:
	raise BookNotAvailableException('18UCSA164')
except BookNotAvailableException as e:
	print (str(e))

	
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    raise BookNotAvailableException('18UCSA164')
BookNotAvailableException: <unprintable BookNotAvailableException object>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#17>", line 4, in <module>
    print (str(e))
  File "C:/Users/dell/Desktop/Exception_library.py", line 72, in __str__
    return self.msg
AttributeError: 'BookNotAvailableException' object has no attribute 'msg'
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> try:
	raise BookNotAvailableException('18UCSA164')
except BookNotAvailableException as e:
	print (str(e))

	
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    raise BookNotAvailableException('18UCSA164')
BookNotAvailableException: <unprintable BookNotAvailableException object>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#19>", line 4, in <module>
    print (str(e))
  File "C:/Users/dell/Desktop/Exception_library.py", line 72, in __str__
    return self.msg
AttributeError: 'BookNotAvailableException' object has no attribute 'msg'
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> try:
	raise BookNotAvailableException('18UCSA164')
except BookNotAvailableException as e:
	print (str(e))

	
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    raise BookNotAvailableException('18UCSA164')
BookNotAvailableException: <unprintable BookNotAvailableException object>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 4, in <module>
    print (str(e))
TypeError: __str__ returned non-string (type tuple)
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> try:
	raise BookNotAvailableException('18UCSA164')
except BookNotAvailableException as e:
	print (str(e))

	
18UCSA164
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> try:
	raise BookNotAvailableException('18UCSA164')
except Exception as e:
	print (str(e))

	
18UCSA164
>>> e
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> try:
	raise BookNotAvailableException('18UCSA164')
except Exception as e:
	print (e)

	
18UCSA164
>>> AttributeError('has')
AttributeError('has')
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik')
Roll Number not defined
>>> type(s)
<class '__main__.Student'>
>>> s
<__main__.Student object at 0x000002841421C978>
>>> s.name
'Ritik'
>>> s.roll
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.roll
AttributeError: 'Student' object has no attribute 'roll'
>>> s = Student('Ritik', '17MCa0093')
>>> s.get_name()
'Ritik'
>>> s.get_rollnum()
'17MCa0093'
>>> s.get_issued_books()
0
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> b = Book('3 Idiots', 'afbshu')
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> b = Book('3 Idiots', 'afbshu')
>>> i = IssueBook()
>>> i.get_deadline()
'Maximum days for Book return: 15'
>>> i.get_finePerDay()
'Fine for each day after 15days is: 2'
>>> i.issue_book(s, b)
>>> b.get_available()
False
>>> 
>>> 
>>> b = Book('Iron Fist', 'afbshu')
>>> b.get_available()
True
>>> i.issue_book(s, b)
>>> b.get_available()
False
>>> s.get_issued_books()
0
>>> s.books
[<__main__.Book object at 0x0000011D8AB55E80>, <__main__.Book object at 0x0000011D8AB55A58>]
>>> for i in s.books:
	print(i.get_bookname())

	
3 Idiots
Iron Fist
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> s.book_issued = 5
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> i.issue_book(s, b)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    i.issue_book(s, b)
  File "C:/Users/dell/Desktop/Exception_library.py", line 196, in issue_book
    if(student.get_issued_books() >= 5):
TypeError: '>=' not supported between instances of 'list' and 'int'
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> s.book_issued = 5
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> i.issue_book(s, b)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    i.issue_book(s, b)
  File "C:/Users/dell/Desktop/Exception_library.py", line 196, in issue_book
    if(student.get_issued_books() >= 5):
TypeError: '>=' not supported between instances of 'list' and 'int'
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> s.book_issued = 5
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> i.issue_book(s, b)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    i.issue_book(s, b)
  File "C:/Users/dell/Desktop/Exception_library.py", line 197, in issue_book
    raise OverLimitException(f'{student.get_rollnum()} already have {student.get_totalIssuedBooks()}')
OverLimitException: Exception Occured: 17MCa0093 already have 5
>>> s.book_issued = 0
>>> b.put_available(False)
>>> i.issue_book(s, b)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    i.issue_book(s, b)
  File "C:/Users/dell/Desktop/Exception_library.py", line 200, in issue_book
    raise BookNotAvailableException ('book.get_bookid() does not available')
BookNotAvailableException: book.get_bookid() does not available
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> s.book_issued = 0
>>> b.put_available(False)
>>> i.issue_book(s, b)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    i.issue_book(s, b)
  File "C:/Users/dell/Desktop/Exception_library.py", line 200, in issue_book
    raise BookNotAvailableException ('{book.get_bookid()} does not available')
BookNotAvailableException: {book.get_bookid()} does not available
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> b.put_available(False)
>>> i.issue_book(s, b)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    i.issue_book(s, b)
  File "C:/Users/dell/Desktop/Exception_library.py", line 200, in issue_book
    raise BookNotAvailableException (f'{book.get_bookid()} does not available')
BookNotAvailableException: afbshu does not available
>>> b.put_available(True)
>>> i.issue_book(s, b)
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> i.issue_book(s, b)
Book issued!
>>> s.get_issued_books()
[<__main__.Book object at 0x000001610A4FEC88>]
>>> s.get_issued_books()[0].name
'Iron Fist'
>>> datetime.date()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    datetime.date()
TypeError: descriptor 'date' of 'datetime.datetime' object needs an argument
>>> datetime.date
<method 'date' of 'datetime.datetime' objects>
>>> datetime.date()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    datetime.date()
TypeError: descriptor 'date' of 'datetime.datetime' object needs an argument
>>> datetime.time()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    datetime.time()
TypeError: descriptor 'time' of 'datetime.datetime' object needs an argument
>>> datetime()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    datetime()
TypeError: function missing required argument 'year' (pos 1)
>>> datetime.now()
datetime.datetime(2019, 5, 29, 17, 38, 29, 539665)
>>> 
============ RESTART: C:/Users/dell/Desktop/Exception_library.py ============
>>> s = Student('Ritik', '17MCa0093')
>>> b = Book('Iron Fist', 'afbshu')
>>> i = IssueBook()
>>> i.issue_book(s, b)
Book issued!
>>> s.get_issued_books()
[(datetime.datetime(2019, 5, 29, 17, 39, 25, 36826), <__main__.Book object at 0x000001D2A5D2EE10>)]
>>> s.get_issued_books()[0][0].strftime()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    s.get_issued_books()[0][0].strftime()
TypeError: strftime() missing required argument 'format' (pos 1)
>>> s.get_issued_books()[0][0].strftime('%Y %M %d')
'2019 39 29'
>>> s.get_issued_books()[0][0].strftime('%Y %m %d')
'2019 05 29'
>>> s.get_issued_books()[0][0].strftime('%H %m %s')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s.get_issued_books()[0][0].strftime('%H %m %s')
ValueError: Invalid format string
>>> s.get_issued_books()[0][0].strftime('%H %M')
'17 39'
>>> s.get_issued_books()[0][0].strftime('%h %M')
'May 39'
>>> s.get_issued_books()[0][0].strftime('%H %M')
'17 39'
>>> 
