a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(f"The sum of {a} and {b} is {a+b}")

if(b==0):
    raise ZeroDivisionError("You cannot divide by zero!")
else:
    print(f"The division of {a} by {b} is {a/b}")