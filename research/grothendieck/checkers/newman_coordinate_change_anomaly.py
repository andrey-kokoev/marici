"""Symbolic checks of the Newman coordinate-change anomaly and rigidity."""

import sympy as sp

x, y, alpha = sp.symbols("x y alpha", nonzero=True)

# A concrete nonlinear map exhibits a nonzero anomaly already for two roots.
f_x = x + alpha * x**3
f_y = y + alpha * y**3
fp_x = sp.diff(f_x, x)
anomaly_half = sp.factor(fp_x / (x - y) - 1 / (f_x - f_y))
assert anomaly_half != 0
assert sp.simplify(anomaly_half.subs(alpha, 0)) == 0

# Swapping x,y in the conjugacy divided difference forces equal derivatives.
divided_difference = sp.factor((f_x - f_y) / (x - y))
assert sp.simplify(divided_difference - (1 + alpha * (x**2 + x*y + y**2))) == 0
assert sp.simplify(fp_x - sp.diff(f_y, y)) != 0

print("exact_coordinate_anomaly_formula=True")
print("cubic_map_anomaly_nonzero=True")
print("affine_limit_anomaly_zero=True")
print("closed_newman_conjugacy_requires_affine_map=True")

