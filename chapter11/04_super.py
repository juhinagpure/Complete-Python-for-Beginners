class Employee:
    def __init__(self):
        print("Employee constructor called")
    a=1

class programmer(Employee):
    def __init__(self):
        print("programmer constructor called")
    b=2

class Manager(programmer):
    def __init__(self):
        super().__init__()
        print("Manager constructor called")
    c=3

# o=Employee()
# print(o.a) #prints the a attribute


# o=programmer()
# print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)  # prints the a, b, and c attributes from Employee, programmer, and Manager respectively