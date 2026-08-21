"""Exact Gram and adjoint audit for finite divisor zeta transforms."""

import sympy as sp


def divisor_matrix(size: int) -> sp.Matrix:
    return sp.Matrix(size, size, lambda row, col: 1 if (row + 1) % (col + 1) == 0 else 0)


for size in (2, 4, 8, 12):
    matrix = divisor_matrix(size)
    gram = matrix.T * matrix
    expected = sp.Matrix(
        size,
        size,
        lambda row, col: size // sp.ilcm(row + 1, col + 1),
    )
    assert gram == expected
    assert matrix.inv() != matrix.T
    assert gram != sp.eye(size)
    print(f"size={size} gram_off_diagonal={gram[0, 1]} Mobius_inverse_is_adjoint=False")

# Positive diagonal weights cannot kill the overlap of columns 1 and 2.
w = sp.symbols("w1:7", positive=True)
matrix = divisor_matrix(6)
weighted_gram = matrix.T * sp.diag(*w) * matrix
assert weighted_gram[0, 1] == w[1] + w[3] + w[5]
assert weighted_gram[0, 1] > 0

print("positive_diagonal_reweighting_isometry=False")
print("polar_normalization_available_but_nonlocal=True")
print("Hermitian_Xi_norm_identification_open=True")

