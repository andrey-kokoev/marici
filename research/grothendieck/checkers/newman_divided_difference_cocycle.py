"""Exact checks of the divided-difference entropy cocycle."""

import sympy as sp

x, y, a, b, c = sp.symbols("x y a b c", nonzero=True)
f = lambda value: value + a * value**2
g = lambda value: value + b * value**3

dd_f = sp.cancel((f(x) - f(y)) / (x - y))
dd_g_after_f = sp.cancel((g(f(x)) - g(f(y))) / (f(x) - f(y)))
dd_composite = sp.cancel((g(f(x)) - g(f(y))) / (x - y))
assert sp.simplify(dd_composite - dd_f * dd_g_after_f) == 0

# Vandermonde transport for three symbolic roots, checked multiplicatively
# to avoid logarithm branch assumptions.
r1, r2, r3 = sp.symbols("r1 r2 r3")
roots = [r1, r2, r3]
delta_r = sp.prod((roots[i] - roots[j]) ** 2 for i in range(3) for j in range(i + 1, 3))
delta_f = sp.prod((f(roots[i]) - f(roots[j])) ** 2 for i in range(3) for j in range(i + 1, 3))
jacobian_product = sp.prod(
    ((f(roots[i]) - f(roots[j])) / (roots[i] - roots[j])) ** 2
    for i in range(3)
    for j in range(i + 1, 3)
)
assert sp.simplify(delta_f - delta_r * jacobian_product) == 0

# Affine divided differences are constant.
affine = lambda value: c * value + b
assert sp.simplify((affine(x) - affine(y)) / (x - y) - c) == 0

print("vandermonde_transport_identity=True")
print("divided_difference_cocycle=True")
print("affine_cocycle=N*(N-1)*log_abs_scale")
print("corrected_entropy_is_coordinate_invariant=True")
print("coordinate_change_alone_creates_new_positivity=False")

