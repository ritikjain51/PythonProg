

x=[["0,0","0,1","0,2"],
   ["1,0","1,1","1,2"],
   ["2,0","2,1","2,2"]]
for i in range(len(x)):
    print(x[i][:])
def inputting(aa,bb):
    a=int(input("user {0} please enter the coordinates".format(aa)))
    b=int(input("user {0} please enter the coordinates".format(aa)))    
    x[a][b]=bb
    for i in range(len(x)):
       print(x[i][:])
for i in range(5):
    inputting(1,'X')
    inputting(2,'0')
def check(bb):
        if(x[0][0]=='X' and x[0][1]=='X'and x[0][2]=='X'):
         print("user 1 wins the game")
        elif(x[1][0]=='X' and x[1][1]=='X'and x[1][2]=='X'):
         print("user 1 wins the game")
        elif(x[2][0]=='X' and x[2][1]=='X' and x[2][1]=='X'):
         print("user 1 wins the game")
        elif(x[0][0]=='0' and x[0][1]=='0'and x[0][2]=='0'):
         print("user 2 wins the game")
        elif(x[1][0]=='0' and x[1][1]=='0'and x[1][2]=='0'):
         print("user 2 wins the game")
        elif(x[2][0]=='0' and x[2][1]=='0' and x[2][1]=='0'):
         print("user 2 wins the game")
        elif(x[0][0]=='X' and x[1][1]=='X' and x[2][2]=='X'):
         print("user 1 wins the game")
        elif(x[0][0]=='0' and x[1][1]=='0'and x[2][2]=='0'):
         print("user 2 wins the game")
        
        
        
     

