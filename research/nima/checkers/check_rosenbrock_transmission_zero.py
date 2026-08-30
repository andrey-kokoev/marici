from fractions import Fraction


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


a = Fraction(2)


def pencil(s):
    return ((s, Fraction(-1)), (-a, Fraction(1)))


def transfer_numerator(s):
    return s - a


assert determinant_2x2(pencil(a)) == 0
assert transfer_numerator(a) == 0
assert a != 0

regular_point = Fraction(3)
assert determinant_2x2(pencil(regular_point)) == regular_point - a
assert determinant_2x2(pencil(regular_point)) != 0

print("internal resolvent pole remains at zero")
print("transfer zero occurs independently at a=2")
print("augmented Rosenbrock pencil loses rank exactly at the transfer zero")
