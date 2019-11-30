

a=int(input("enter a number to check->"))
if (a>1):
        for i in range(2,a):
          if (a % i==0):
              print("the number is prime")
              break
          else:
              print("the number is not prime")
        else:
              print(a,"is not a prime number")
              
           
              
              
             
  
           