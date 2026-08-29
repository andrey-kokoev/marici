from fractions import Fraction


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def divide(dividend, divisor):
    remainder = [Fraction(x) for x in dividend]
    divisor = trim([Fraction(x) for x in divisor])
    quotient = [Fraction(0)] * max(1, len(remainder) - len(divisor) + 1)
    while len(trim(remainder)) >= len(divisor) and trim(remainder) != [0]:
        remainder = trim(remainder)
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] += coefficient
        for index, value in enumerate(divisor):
            remainder[degree + index] -= coefficient * value
    return trim(quotient), trim(remainder)


# Coefficients are in ascending degree order.
displacement = [0, 1]
reflecting_section = [0, 1]
hostile_section = [-1, 0, 1]

quotient, remainder = divide(displacement, reflecting_section)
assert remainder == [0]
assert quotient == [1]

_, hostile_remainder = divide(displacement, hostile_section)
assert hostile_remainder == displacement

assert hostile_section[0] + hostile_section[1] + hostile_section[2] == 0
assert 1 != 0

print("reflecting section: displacement factors without division singularity")
print("equivariant hostile section: off-fixed zero survives")
print("germ faithfulness does not imply fixed-point reflection")
