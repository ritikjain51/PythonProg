
import re
a="i am atul kumar. hello sir how are you"
obj=re.compile(r'hello')  #r means raw string
res=obj.search(a)
print(res.group())


import re
a="i am atul kumar. hello 91-9887340701 sir how are you"
obj=re.compile(r'\d\d-\d{10}')  #returns only 1st match no 
res=obj.search(a)
print(res.group())


import re
a="i am atul kumar.  atul atul hello 91-9887340701 atul  sir how are you"
obj=re.findall(r'atul',a)
print(obj)


import re
a="i am atul kumar. ; at;ul atul hello # 91-9887340701 a,tul  s+ir how= are you"
obj=re.findall(r'[:;,=(#$@%&*]',a)
print(obj)


import re
a="i am atul kumar. ; at;ul@gmail.com atul hello@abc.com # 91-9887340701 a,tul  s+ir@yahoo.com how= are you"
obj=re.findall(r'[\w\.]+@[\w\.]+',a)
print(obj)


import re
a="i am atul kumar.  atul atul hello 91-9887340701 atul  sir how are you"
obj=re.sub('atul','batul',a)
print(obj)


import re
a="i am@ at#$ul kumar. ; at;ul@gmail.com atul hello@abc.com, # 91-98==8734=0701 a,tul  s+ir@yahoo.com how= are you"
obj=re.compile(r'[;:,/\)(*%#$@=_]')
newo=obj.sub('',a)
print(newo)







