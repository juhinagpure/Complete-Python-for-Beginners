try:
    a=int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("I am inside the else block")
    print("Thank you")