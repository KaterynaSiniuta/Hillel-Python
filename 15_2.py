from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    def __mul__(self, other):
        """Множення дробів."""
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __add__(self, other):
        """Додавання дробів."""
        if isinstance(other, Fraction):
            new_a = self.a * other.b + self.b * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __sub__(self, other):
        """Віднімання дробів."""
        if isinstance(other, Fraction):
            new_a = self.a * other.b - self.b * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __eq__(self, other):
        """Перевірка рівності дробів."""
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return NotImplemented

    def __gt__(self, other):
        """Перевірка, чи більше поточний дріб."""
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return NotImplemented

    def __lt__(self, other):
        """Перевірка, чи менше поточний дріб."""
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

