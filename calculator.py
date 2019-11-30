#calculator
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
choice=input("choose a symbol(+,-,*,/):")
c=0;
if choice=='+':
 c=a+b;
elif choice=='-':
 c=a-b;
elif choice=='*':
 c=a*b;
elif choice=='/':
 c=a/b;
else:
 wrong;
print(f"value of {a}{choice}{b}={c}")
