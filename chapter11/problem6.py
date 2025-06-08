class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        symbols = ['i', 'j', 'k']
        return " + ".join([f"{self.vec[i]}{symbols[i]}" for i in range(len(self.vec))])

# Example
v = Vector([7, 8, 10])
print(v)
