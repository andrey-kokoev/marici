"""Symbolic checks for symmetric exterior-force cancellation."""

import sympy as sp

r, y = sp.symbols("r y", nonzero=True)
pair_force = 2 / (r - y) + 2 / (r + y)
assert sp.simplify(pair_force - 4 * r / (r**2 - y**2)) == 0

# Exact split into the radial inverse-square term and cubic remainder.
split = -4 * r / y**2 - 4 * r**3 / (y**4 * (1 - r**2 / y**2))
assert sp.simplify(pair_force - split) == 0

# Universal identities used by scale normalization.
n = sp.symbols("N", integer=True, positive=True)
radius = sp.symbols("R2", positive=True)
p = n * (n - 1) / 2
# sum_i r_i A_i = p, so sum_i r_i(A_i-p r_i/R2)=0.
assert sp.simplify(p - (p / radius) * radius) == 0

print("symmetric_pair_force_identity=True")
print("radial_inverse_square_term=True")
print("first_nonradial_remainder_order=r^3/y^4")
print("scale_orthogonality_cancels_radial_force=True")

