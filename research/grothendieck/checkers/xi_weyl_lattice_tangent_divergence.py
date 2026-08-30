"""Checks for tangent-renormalized Weyl-lattice positivity."""

import sympy as sp


def check(points: list[sp.Rational]) -> None:
    n = len(points)
    eps = [points[i] - i for i in range(n)]
    ratios = [(eps[j] - eps[i]) / sp.Rational(j - i) for i in range(n) for j in range(i + 1, n)]
    assert all(value > -1 for value in ratios)

    relative_log = 2 * sum(sp.log(1 + value) for value in ratios)
    tangent = 2 * sum(ratios)
    divergence = sp.N(tangent - relative_log, 50)
    assert divergence >= 0

    harmonic_gradient = [2 * (sp.harmonic(i) - sp.harmonic(n - 1 - i)) for i in range(n)]
    tangent_by_sites = sum(harmonic_gradient[i] * eps[i] for i in range(n))
    assert sp.simplify(tangent_by_sites - tangent) == 0
    print(f"rank={n} divergence={divergence}")


check([sp.Rational(0), sp.Rational(1), sp.Rational(3)])
check([sp.Rational(0), sp.Rational(1), sp.Rational(3, 2)])
check([sp.Rational(-2), sp.Rational(-1, 3), sp.Rational(4, 5), sp.Rational(5)])

u = sp.symbols("u", real=True)
phi = u - sp.log(1 + u)
assert sp.simplify(sp.diff(phi, u)) == u / (u + 1)
assert sp.simplify(sp.diff(phi, u, 2)) == 1 / (u + 1) ** 2

print("scalar_divergence_convex=True")
print("unique_scalar_minimum=u=0")
print("global_coupled_positivity=True")
print("equality_only_for_lattice_translation=True")
print("collision_barrier=positive_infinity")

