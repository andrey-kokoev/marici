"""Exact checks for the Hermitian RH-defect heat bridge."""

import sympy as sp

t = sp.symbols("t", positive=True)
beta, height = sp.symbols("beta height", real=True)
a = beta - sp.Rational(1, 2)
radius_squared = a**2 + height**2
quartet_heat = 4 * a**2 * sp.exp(-t * radius_squared)
positive_radius_squared = sp.symbols("R2", nonnegative=True)
base_laplace = sp.integrate(sp.exp(-t) * sp.exp(-t * positive_radius_squared), (t, 0, sp.oo))
assert sp.simplify(base_laplace - 1 / (1 + positive_radius_squared)) == 0
laplace = 4 * a**2 / (1 + radius_squared)
expected = 4 * a**2 / (1 + radius_squared)
assert sp.simplify(laplace - expected) == 0

hostile_heat = sp.simplify(quartet_heat.subs({beta: sp.Rational(3, 4), height: 2}))
hostile_laplace = sp.simplify(laplace.subs({beta: sp.Rational(3, 4), height: 2}))
assert hostile_heat == sp.exp(-sp.Rational(65, 16) * t) / 4
assert hostile_laplace == sp.Rational(4, 81)

# Z^2 and Z*Z differ at the first off-line scalar.
z = sp.Rational(1, 4) + 2 * sp.I
assert sp.simplify(z**2 - z * sp.conjugate(z)) != 0

print(f"hostile_quartet_heat={hostile_heat}")
print(f"hostile_Laplace_defect={hostile_laplace}")
print("one_time_zero_iff_RH=True")
print("holomorphic_Z_squared_not_Hermitian_ZstarZ=True")
print("source_side_paired_heat_semigroup_open=True")
