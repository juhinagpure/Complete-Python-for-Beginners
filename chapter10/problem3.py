class Demo:
    a = 4  # Class attribute

# Creating an object of the class
o = Demo()

# Since 'a' is not defined in the object yet, it prints the class attribute
print(o.a)  # Output: 4

# Now we assign a new value to 'a' using the object 'o'
# This creates an instance attribute 'a' that overrides the class attribute for this object
o.a = 0

# Now, it prints the instance (object) attribute 'a', not the class one
print(o.a)  # Output: 0
