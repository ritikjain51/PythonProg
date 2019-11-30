a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=int(input("enter the value of d:"))
if(a>b):
    if (a>c):
        if(a>d):
           print("a is maximum");
if((b>a) and (b>c) and(b>d)):
 print("b is maximum");
if((c>a) and (c>b) and (c>d)):
 print("c is maximum");
else:
   print("d is maximum"); 
