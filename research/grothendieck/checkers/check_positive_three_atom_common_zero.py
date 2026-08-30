from fractions import Fraction


class Qsqrt5:
    def __init__(self, rational, radical=0):
        self.a = Fraction(rational)
        self.b = Fraction(radical)

    def __add__(self, other):
        other = other if isinstance(other, Qsqrt5) else Qsqrt5(other)
        return Qsqrt5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __mul__(self, other):
        other = other if isinstance(other, Qsqrt5) else Qsqrt5(other)
        return Qsqrt5(
            self.a * other.a + 5 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Qsqrt5) else Qsqrt5(other)
        return self.a == other.a and self.b == other.b


y_large = Qsqrt5(Fraction(-3, 2), Fraction(-1, 2))
y_small = Qsqrt5(Fraction(-3, 2), Fraction(1, 2))

assert y_large * y_small == 1
assert 1 + 3 * y_large + y_large * y_large == 0
assert 1 + 3 * y_small + y_small * y_small == 0

print("positive_weights=1,3,1")
print("halfline_polynomial=P(y)=1+3y+y^2")
print("reciprocal_identity=y^2*P(1/y)=P(y)")
print("common_roots=(-3+sqrt(5))/2,(-3-sqrt(5))/2")
print("off_seam_common_zero=yes")
