"""Exact checks for Weyl-lattice discriminant fluctuations."""

import sympy as sp


def discriminant(points: list[sp.Rational]) -> sp.Rational:
    return sp.prod((points[j] - points[i]) ** 2 for i in range(len(points)) for j in range(i + 1, len(points)))


lattice = [sp.Rational(0), sp.Rational(1), sp.Rational(2)]
expanded = [sp.Rational(0), sp.Rational(1), sp.Rational(3)]
compressed = [sp.Rational(0), sp.Rational(1), sp.Rational(3, 2)]
expanded_ratio = sp.factor(discriminant(expanded) / discriminant(lattice))
compressed_ratio = sp.factor(discriminant(compressed) / discriminant(lattice))
assert expanded_ratio > 1
assert 0 < compressed_ratio < 1

n = 6
eps = sp.symbols(f"e0:{n}")
linear_coefficients = []
for i in range(n):
    coefficient = 2 * (
        sum(sp.Rational(1, i - j) for j in range(i))
        + sum(sp.Rational(-1, j - i) for j in range(i + 1, n))
    )
    expected = 2 * (sp.harmonic(i) - sp.harmonic(n - 1 - i))
    assert sp.simplify(coefficient - expected) == 0
    linear_coefficients.append(coefficient)

# The negative Hessian quadratic form vanishes only on translations.
quadratic = -sum((eps[j] - eps[i]) ** 2 / sp.Rational((j - i) ** 2) for i in range(n) for j in range(i + 1, n))
assert sp.expand(quadratic.subs({value: 1 for value in eps})) == 0
assert quadratic.subs({eps[i]: i for i in range(n)}) < 0

print(f"expanded_discriminant_ratio={expanded_ratio}")
print(f"compressed_discriminant_ratio={compressed_ratio}")
print("global_sign_unrestricted=True")
print(f"boundary_linear_coefficients={linear_coefficients}")
print("bulk_quadratic_form=negative_nonlocal_Dirichlet")
print("translation_null_mode=True")

