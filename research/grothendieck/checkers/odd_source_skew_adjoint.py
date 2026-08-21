"""Exact finite convolution checks for the odd-source vanishing mechanism."""

import sympy as sp


def convolution_matrix(kernel: list[sp.Expr]) -> sp.Matrix:
    order = len(kernel)
    return sp.Matrix(order, order, lambda row, col: kernel[(row - col) % order])


# C2 hostile branch: inversion fixes the nonzero element, so a real odd
# kernel is necessarily zero.
c2_value = sp.symbols("a", real=True)
assert sp.solve(sp.Eq(c2_value, -c2_value), c2_value) == [0]

for kernel in (
    [sp.Integer(0), sp.Integer(1), sp.Integer(-1)],
    [sp.Integer(0), sp.Integer(2), sp.Integer(0), sp.Integer(-2)],
    [sp.Integer(0), sp.Integer(1), sp.Integer(3), sp.Integer(-3), sp.Integer(-1)],
):
    matrix = convolution_matrix(kernel)
    assert matrix.T == -matrix
    assert matrix.H == -matrix
    characteristic = matrix.charpoly().as_expr()
    print(f"cyclic_order={len(kernel)} skew_adjoint=True characteristic={characteristic}")

print("C2_odd_real_kernel_trivial=True")
print("source_leg_antisymmetry_forces_spectral_imaginarity=True")
print("Xi_operator_equivalence_constructed=False")
print("physical_relative_chain_pushforward_constructed=False")
