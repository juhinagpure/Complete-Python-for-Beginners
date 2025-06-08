class Employee:
    a=1

class programmer(Employee):
    b=2

class Manager(programmer):
    c=3

o=Employee()
print(o.a) #prints the a attribute
# print(o.b) #prints the b attribute, which is not defined in Employee, so it will raise an AttributeError

o=programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)  # prints the a, b, and c attributes from Employee, programmer, and Manager respectively