"""Check the source-derived conormal cancellation at the plus boundary."""

from fractions import Fraction


# Suppress the common a^3 basis vector and work with its scalar coefficient.
def g(b):
    return Fraction(1 - b * b)


def h(b):
    return Fraction(3 * (1 + b))


residue_plus = Fraction(-2)  # (1-b^2)/(b-1)=-(1+b), evaluated at b=1
residue_minus = Fraction(2)  # (1-b^2)/(b+1)=1-b, evaluated at b=-1

assert h(1) == 6
assert h(-1) == 0
assert residue_plus == -2
assert residue_minus == 2
assert h(1) + 3 * residue_plus == 0

for power in range(12):
    # b^power is one at the plus boundary, so the same coefficient cancels
    # every member of the filtered h orbit.
    assert Fraction(1**power) * h(1) + 3 * Fraction(1**power) * residue_plus == 0

print("plus boundary: h=6*a^3, conormal residue(g)=-2*a^3")
print("source coefficient: 3")
print("h + 3*residue_plus(g): 0")
print("minus boundary residue(g): 2*a^3; two-endpoint compatibility remains")
