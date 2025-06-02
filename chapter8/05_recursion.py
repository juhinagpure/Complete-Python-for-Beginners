
# factorial(1)=1
# factorial(2)=2*1
# factorial(3)=3*2*1
# factorial(4)=4*3*2*1   
# factorial(5)=5*4*3*2*1

# factorial(n)=n*(n-1)*(n-2)*...*3*2*1

# factorial(n)=n*factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n=int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")
    