#factorial
#using while loop
n=int(input("enter a number:"))
total =1
i = 1
while i<=n-1:
      total += total*i
      i += 1
print("factorial of",n,"is",total)
    

#using for loop
n=int(input("enter a number:"))
total = 1
for i in range(n,0,-1):
    total += total*i
print("factorial of",n,"is",total)
