class Programmer:
    company = "Microsoft"  # Class attribute

    # Constructor with correct syntax
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

# Creating an object
p = Programmer("Harry", 1200000, 123456)

# Printing values
print(p.name, p.salary, p.pin)
