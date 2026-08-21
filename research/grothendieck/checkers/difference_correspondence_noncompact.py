"""Exact finite-window falsifier for the noncompact difference pullback."""

import sympy as sp

M = sp.symbols("M", integer=True, nonnegative=True)

# For f=delta_0 on Z, Df is the diagonal indicator. In [-M,M]^2 there are
# exactly 2M+1 diagonal points, while ||f||^2=1.
window_norm_squared = 2 * M + 1
assert sp.limit(window_norm_squared, M, sp.oo) == sp.oo
assert window_norm_squared.subs(M, 0) == 1
assert window_norm_squared.subs(M, 10) == 21

# Finite cyclic quotients reproduce the same fiber-volume factor.
for order in (2, 3, 5, 7):
    incidence = sp.zeros(order * order, order)
    for a in range(order):
        for b in range(order):
            incidence[a * order + b, (a - b) % order] = 1
    assert incidence.T * incidence == order * sp.eye(order)
    normalized = incidence / sp.sqrt(order)
    assert sp.simplify(normalized.T * normalized - sp.eye(order)) == sp.zeros(order)
    print(f"cyclic_order={order} fiber_volume={order} normalized_isometry=True")

print(f"integer_window_diagonal_norm_squared={window_norm_squared}")
print("noncompact_difference_pullback_bounded=False")
print("relative_or_semifinite_normalization_required=True")
print("physical_relative_chain_pushforward_constructed=False")

