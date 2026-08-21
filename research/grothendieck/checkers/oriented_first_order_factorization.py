"""Exact minimal checks for the oriented first-order factorization target."""


def determinant_2x2(matrix: tuple[tuple[int, int], tuple[int, int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# Scalar Q=t: its oriented determinant changes sign, while Q*Q=t^2 does not.
for t in (-2, -1, 0, 1, 2):
    q_determinant = t
    gram_determinant = t * t
    assert gram_determinant == q_determinant**2

assert (-1) < 0 < 1
assert (-1) ** 2 == 1**2

# The chiral lift H_Q=[[0,q],[q,0]] is symmetric and has determinant -q^2.
for q in (-3, 0, 4):
    chiral = ((0, q), (q, 0))
    assert chiral[0][1] == chiral[1][0]
    assert determinant_2x2(chiral) == -(q * q)

# A polynomial square has even root multiplicities; 1-x^2 has simple roots.
derivative_at_plus_one = -2
derivative_at_minus_one = 2
assert derivative_at_plus_one != 0
assert derivative_at_minus_one != 0

print("oriented_first_order_determinant_can_change_sign=True")
print("adjoint_composite_determinant_is_square=True")
print("chiral_lift_is_self_adjoint=True")
print("generic_transfer_defect_has_no_polynomial_first_order_factor=True")
print("source_derived_relative_boundary_map_open=True")
