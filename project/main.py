import random

computer=random.choice([1, -1, 0]) 
print("Welcome to Snake Water Gun Game")
youstr=input("Enter your choice :")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake", -1:"water", 0:"gun"}

you=youDict[youstr]

print(f"you choose {reverseDict[you]}\n computer choose {reverseDict[computer]}")
if(computer==you):
    print("It's a tie")
else:
    
    if(computer==-1 and you==1):
        print("you win!")

    elif(computer==-1 and you==0):
        print("you Lose !")

    elif(computer==-1 and you==-1):
        print("you Lose!")

    elif(computer==1 and you==0):
        print("You win!")

    elif(computer==0 and you==-1):
        print("you win!")

    elif (computer==0 and you==1):
        print("You lose!")

    else:
        print("something went wrong")