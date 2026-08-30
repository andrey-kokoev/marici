from fractions import Fraction


def mat_vec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


pullback = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
]
section_transfer = [
    [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
]
average_transfer = [
    [Fraction(1, 2), Fraction(0), Fraction(1, 2), Fraction(0)],
    [Fraction(0), Fraction(1, 2), Fraction(0), Fraction(1, 2)],
]


def compose(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


identity_2 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
assert compose(section_transfer, pullback) == identity_2
assert compose(average_transfer, pullback) == identity_2

delta_G = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
delta_H = [Fraction(1), Fraction(0)]
assert mat_vec(section_transfer, delta_G) == delta_H
assert mat_vec(average_transfer, delta_G) == [Fraction(1, 2), Fraction(0)]

# Nontrivial kernel translation swaps 0<->2 and 1<->3.
probe = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
translated = [probe[2], probe[3], probe[0], probe[1]]
assert mat_vec(section_transfer, translated) != mat_vec(section_transfer, probe)
assert mat_vec(average_transfer, translated) == mat_vec(average_transfer, probe)

print({
    "surjection": "C4->C2",
    "section_left_inverse": True,
    "section_preserves_delta": True,
    "section_kernel_equivariant": False,
    "average_left_inverse": True,
    "average_preserves_delta": False,
    "average_kernel_equivariant": True,
    "checks": "pass",
})
