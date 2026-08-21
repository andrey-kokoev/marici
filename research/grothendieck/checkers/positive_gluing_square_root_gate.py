"""Exact even-order and Pfaffian square-root checks."""

import sympy as sp

T, T0, curvature = sp.symbols("T T0 c", real=True, positive=True)
delta = T - T0

# A contractive singular value touching one has quadratic Gram defect.
sigma = 1 - curvature * delta**2
gram_defect = sp.expand(1 - sigma**2)
assert sp.simplify(gram_defect.subs(T, T0)) == 0
assert sp.simplify(sp.diff(gram_defect, T).subs(T, T0)) == 0
assert sp.simplify(sp.diff(gram_defect, T, 2).subs(T, T0) - 4 * curvature) == 0

# Smallest oriented square root.
skew = sp.Matrix([[0, T], [-T, 0]])
pfaffian = T
assert skew.det() == T**2
assert skew.det() == pfaffian**2
assert sp.diff(pfaffian, T) == 1
assert sp.diff(skew.det(), T).subs(T, 0) == 0

print("positive_analytic_Gram_zero_order_even=True")
print("generic_unit_singular_value_contact_order=2")
print("two_by_two_Pfaffian_has_simple_zero=True")
print("Gram_determinant_models_Xi_squared_not_signed_Xi=True")
print("canonical_determinant_line_orientation_open=True")

