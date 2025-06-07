class Employee:
    name = "Harry"
    language = "Python"  # class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print(f"Hello Good morning")
        
harry = Employee()
# harry.language = "javascript"  # instance attribute


# Call using class
# Employee.getInfo(harry)

# OR call directly
harry.getInfo()
harry.greet()
