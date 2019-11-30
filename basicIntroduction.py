"""
python: its a very high level language programming. in this we makes program
to teach a machine what we actually wants.

why python?
1)its a syntax free language
2)we can integrate it with different technologies and hardware
3)its huge collection of library makes every task easy.
4)its a reference(address) based language. dynamic updation no data type require

features:
comments:
# single line comment
""""""multi line comment
''''''multi line comment

indent block: to define the scope of something we use indent block. 1tab space
4 space from space bar

if():
    dffgr
    sdffgf
    dfg
dfd     #if terminated

vriables: memory location where we can store our values

types of variables:
local
a=20
b=30.03

global
global a


operator: these are the symbols in the prgram use for computation purpose:
arithmetic: + - * / // % ** << >>
logical: and or not
relational: == < > <= >= !=
assignment: = += -= *= &= |= <<= >>=
a+=1-------------------a=a+1
special operator: these results in the form of true and false.
1)identity: is is not
a=10
print(a is 10)      ####True
print(a is 20)      ####False

2)membership operator:in not in
a=[4,2,4,5,6,4,2,1,1]
print(4 in a)   ####True
print(44 in a)   ####False





outputting and inputting:
inputting:
syntax:
variable=input("string for user understanding")
a=input("enter a no:-")

bydefault type of a will be a string.
so casting is require:
variable=type(variable)###type: int str float
a=int(a)


outputting:
syntax:
print("string to print",variable)


use of end and sep


print("hello","hie",sep='#')



print("hello",end=' ')
print("bie")

use of % and format to write something in between string:

%: %d %s %f  integer,string,float respectively


a="samyak"
b="are"
print("hello mr %s how %s you"%(a,b))

format:


a="samyak"
b="are"
print("hello mr {0} how {1} you".format(a,b))

array:its a collection of similar datatypes.

categories:
list: indexed, ordered, duplicate allow, changebale
tuple: indexed, ordered, duplicate allow, non changebale
set: unindexed, un ordered, duplicate not allow, non changebale
dict: unindexed, unordered, duplicate not allow, changebale

list:
syntax: 1D list
name=[paramters]

a=[4,2,4,5,6,7,8,9,7,5,3]
a[0]------4


2D list:
name=[[c1,c2,c3...],[c1,c2,c3...],.....]

a=[[4,2],[6,4]]

a[row][colmn]

a[0][0]----4

list using predefined method:

a=list((5,3,5,65,7,6,4,3,2,21))

tuple:
syntax:  tuple
name=(paramters)
a=(4,2,4,5,6,7,8,9,7,5,3)
a[0]------4


tuple using predefined method:

a=tuple((5,3,5,65,7,6,4,3,2,21))

set:
syntax:  set
name={paramters}
a={4,2,4,5,6,7,8,9,7,5,3}


set using predefined method:

a=set((5,3,5,65,7,6,4,3,2,21))



dict:
syntax:  dict
name={key:values}
a={1:'hie',10:'bie'}


set using predefined method:

a=dict(({1:'hie',10:'bie'}))
