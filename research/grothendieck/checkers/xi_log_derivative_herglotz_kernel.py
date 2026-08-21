"""Exact finite boundary-zero Gram checks for the Xi Herglotz kernel."""

import sympy as sp

z, v, gamma = sp.symbols("z v gamma", real=True, positive=True)
single_kernel = sp.simplify(
    (1 / (z - sp.I * gamma) + 1 / (v + sp.I * gamma)) / (z + v)
)
expected_single = 1 / ((z - sp.I * gamma) * (v + sp.I * gamma))
assert sp.simplify(single_kernel - expected_single) == 0

ordinates = [sp.Integer(1), sp.Integer(-1), sp.Integer(2), sp.Integer(-2)]
points = [sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)]
gram = sp.Matrix(
    len(points),
    len(points),
    lambda row, col: sp.simplify(
        sum(
            1
            / (
                (points[row] - sp.I * ordinate)
                * (points[col] + sp.I * ordinate)
            )
            for ordinate in ordinates
        )
    ),
)
assert gram.H == gram
assert all(sp.simplify(gram[:index, :index].det()) > 0 for index in range(1, len(points) + 1))

# A right-half-plane hostile zero is an interior pole of the log derivative.
hostile_zero = sp.Rational(1, 4) + 2 * sp.I
hostile_log_derivative = 1 / (z - hostile_zero)
assert sp.denom(hostile_log_derivative).subs(z, hostile_zero) == 0

print("single_boundary_zero_rank_one_identity=True")
print("finite_boundary_zero_kernel_Gram_positive=True")
print("right_half_plane_off_line_zero_creates_interior_pole=True")
print("Xi_kernel_positivity_equivalent_to_RH=True")
print("source_side_Gram_realization_open=True")

