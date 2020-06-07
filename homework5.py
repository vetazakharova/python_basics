class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f"{self.a} + {self.b} * i"

    def __add__(self, other):
        return f"The sum of two complex numbers is {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"The multiplication of two complex numbers is {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a} * i"

    def __str__(self):
        return f"z = {self.a} + {self.b} * i"

z1 = ComplexNum(6, 5)
z2 = ComplexNum(4, 3)
print(z1 + z2)
print(z1 * z2)
