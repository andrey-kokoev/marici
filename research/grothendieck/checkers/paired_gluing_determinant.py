"""Exact finite Schur-complement and global-zero checks."""

import sympy as sp

A = sp.diag(2, 3)
B = sp.diag(5, 7)
C = sp.Matrix([[1, 2], [0, 1]])
block = A.row_join(C).col_join(C.T.row_join(B))
schur = B - C.T * A.inv() * C
assert sp.simplify(block.det() - A.det() * schur.det()) == 0

# Individually invertible identity blocks acquire a coupled zero when one
# singular value reaches one.
identity = sp.eye(2)
threshold_coupling = sp.diag(1, sp.Rational(1, 2))
threshold_block = identity.row_join(threshold_coupling).col_join(
    threshold_coupling.T.row_join(identity)
)
assert identity.det() == 1
assert threshold_block.det() == 0
assert (identity - threshold_coupling.T * threshold_coupling).det() == 0

# Below threshold the block is positive definite; above it is indefinite.
below = sp.diag(sp.Rational(1, 2), sp.Rational(1, 3))
below_block = identity.row_join(below).col_join(below.T.row_join(identity))
assert all(below_block[:index, :index].det() > 0 for index in range(1, 5))

above = sp.diag(sp.Rational(3, 2), sp.Rational(1, 3))
above_block = identity.row_join(above).col_join(above.T.row_join(identity))
assert any(value < 0 for value in above_block.eigenvals())

print("Schur_complement_determinant_identity=True")
print("nonzero_local_blocks_can_have_zero_coupled_determinant=True")
print("coupled_zero_at_singular_value_one=True")
print("block_positivity_equivalent_to_contraction=True")
print("Xi_gluing_operator_constructed=False")

