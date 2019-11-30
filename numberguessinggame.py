#number gassing game
winning_number=33
user_input=int(input("guess a number between 1 and 100:"))
if user_input==winning_number:
    print("you win !!!")
else:
    if user_input < winning_number:
        print("too low:")
    else:
          print("too high")

    
