class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __len__(self):
        return len(self.vec)

# Example
v = Vector([7, 8, 10])
print("Dimension of vector:", len(v))
