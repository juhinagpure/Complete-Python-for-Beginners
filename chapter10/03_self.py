# Define a class named Employee
class Employee:
    # Class attributes (shared by all instances unless overridden)
    name = "Harry"
    language = "Python"
    salary = 1200000

    # Instance method to print info
    def getInfo(self):
        # Accessing attributes using 'self'
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method (does not use self or cls)
    @staticmethod
    def greet():
        print("Hello Good morning")

# Creating an object of Employee class
harry = Employee()

# Call the instance method using object
harry.getInfo()

# Call the static method using object (can also use Employee.greet())
harry.greet()
