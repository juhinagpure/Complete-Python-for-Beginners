# Define a class named Employee
class Employee:
    # Class attributes (shared by all instances unless overridden)
    name = "Harry"
    language = "Python"
    salary = 1200000

    # Constructor method (called automatically when object is created)
    def __init__(self): #dunder method which is automatically called
        print("I am creating an object")

    # Instance method to print info
    def getInfo(self):
        # Accessing attributes using 'self'
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method (does not use self or cls)
    @staticmethod
    def greet():
        print("Hello Good morning")

# Create an object of Employee class
harry = Employee()

# Assigning a new value to the instance attribute 'name'
harry.name = "Harry"

# ✅ Correct print syntax — remove quotes from variable names
print(harry.name, harry.salary)
