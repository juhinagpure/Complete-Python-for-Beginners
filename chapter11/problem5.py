class Vector:
    def __init__(self, vec):
        self.vec = vec  # List representing the vector

    def __add__(self, other):
        # Element-wise addition
        new_vec = [a + b for a, b in zip(self.vec, other.vec)]
        return Vector(new_vec)

    def __mul__(self, other):
        # Dot product
        return sum(a * b for a, b in zip(self.vec, other.vec))

    def __str__(self):
        # Display in 7i + 8j + 10k format
        symbols = ['i', 'j', 'k']
        return " + ".join([f"{self.vec[i]}{symbols[i]}" for i in range(len(self.vec))])


# Example usage
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print("Vector 1:", v1)             # Output: 7i + 8j + 10k
print("Vector 2:", v2)             # Output: 1i + 2j + 3k
print("Sum:", v1 + v2)             # Output: 8i + 10j + 13k
print("Dot Product:", v1 * v2)     # Output: 53
