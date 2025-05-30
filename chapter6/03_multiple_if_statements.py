a=int(input("Enter your age "))

#if statement no:1
if(a%2==0):
    print("You have entered an even number")

#End of if statement no :1 

#if statement no:2
if(a>=18):
    print("You are eligible to vote")
    print("Good for you")
elif(a<0):
    print("Invalid age")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("You are not eligible to vote")
#End of if statement no:2

print("End of program")