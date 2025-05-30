a=int(input("Enter your age "))

if(a>18):
    print("You are eligible to vote")
    print("Good for you")
elif(a<0):
    print("Invalid age")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("You are not eligible to vote")

print("End of program")