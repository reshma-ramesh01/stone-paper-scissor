import random
options=["stone","paper","scissor"]
choice=random.choice(options)
user=input("stone / paper / scissor ? ")
if user in options:
    while True:
        if user==choice:
            print("It's a draw..!")
            break
        elif user=="stone" and choice=="scissor" or \
             user=="scissor" and choice=="paper" or \
             user=="paper" and choice=="stone":
            print("User : "+user+"\nComputer : "+choice)     
            print("You Win")
            break
        else:
            print("User : "+user+"\nComputer : "+choice)     
            print("Computer Wins")
            break
else:
     print("INVALID INPUT..!")
