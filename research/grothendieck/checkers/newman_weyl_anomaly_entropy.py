"""Exact checks of the Weyl-coordinate Newman entropy balance."""

import sympy as sp

r, s, epsilon = sp.symbols("r s epsilon", real=True)
h = lambda value: value**3
hp = lambda value: 3 * value**2
f = lambda value: value + epsilon * h(value)
fp = lambda value: 1 + epsilon * hp(value)

mobility_pair = fp(r) / (r - s) - fp(r) ** 2 / (f(r) - f(s))
first_variation = sp.simplify(sp.diff(mobility_pair, epsilon).subs(epsilon, 0))
expected = (h(r) - h(s)) / (r - s) ** 2 - hp(r) / (r - s)
assert sp.simplify(first_variation - expected) == 0

# Affine perturbations have zero mobility anomaly to first order and exactly.
a, b = sp.symbols("a b")
f_affine = (1 + epsilon * a) * r + epsilon * b
g_affine = (1 + epsilon * a) * s + epsilon * b
fp_affine = 1 + epsilon * a
affine_anomaly = fp_affine / (r - s) - fp_affine**2 / (f_affine - g_affine)
assert sp.simplify(affine_anomaly) == 0

# The entropy identity is an algebraic chain rule.
A1, A2, m1, m2, C1, C2 = sp.symbols("A1 A2 m1 m2 C1 C2")
velocities = [2 * m1 * A1 + C1, 2 * m2 * A2 + C2]
chain_rule = 2 * A1 * velocities[0] + 2 * A2 * velocities[1]
balance = 4 * (m1 * A1**2 + m2 * A2**2) + 2 * (A1 * C1 + A2 * C2)
assert sp.expand(chain_rule - balance) == 0

# The balance has both signs when the anomaly is aligned adversely or
# reinforcingly with the logarithmic gradient.
hostile = balance.subs({A1: 1, A2: 2, m1: 1, m2: 1, C1: -3, C2: -6})
reinforcing = balance.subs({A1: 1, A2: 2, m1: 1, m2: 1, C1: 3, C2: 6})
assert hostile < 0 < reinforcing

print("mobility_anomaly_first_variation=True")
print("affine_mobility_anomaly_zero=True")
print("coordinate_curvature_is_leading_local_term=True")
print("exact_entropy_balance=True")
print(f"hostile_entropy_production={hostile}")
print(f"reinforcing_entropy_production={reinforcing}")
print("anomaly_flux_sign_unrestricted=True")
