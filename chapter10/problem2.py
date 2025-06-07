class Calculator:
    def __init__(self, n):  # Corrected constructor
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square root is {self.n ** 0.5}")

# Create object and call methods
a = Calculator(5)
a.square()
a.cube()
a.square_root()
