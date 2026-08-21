"""Exact constant and quasiperiodic-boundary checks for the 1/8 gate."""

import sympy as sp

pi = sp.pi
theta_constant = -pi / 8
counting_constant = sp.simplify(1 + theta_constant / pi)
assert counting_constant == sp.Rational(7, 8)

alpha = sp.Rational(1, 8)
boundary_phase = sp.simplify(sp.exp(2 * pi * sp.I * alpha))
assert sp.simplify(boundary_phase - sp.exp(sp.I * pi / 4)) == 0
assert sp.simplify(1 - alpha - counting_constant) == 0

# The boundary family is genuinely tunable: distinct phases give distinct
# spectral offsets for every mode.
n, length = sp.symbols("n L", integer=True, positive=True)
eigenvalue = lambda phase: 2 * pi * (n + phase) / length
assert sp.simplify(eigenvalue(sp.Rational(1, 8)) - eigenvalue(sp.Rational(1, 4))) != 0

print(f"Stirling_theta_constant={theta_constant}")
print(f"Xi_counting_constant={counting_constant}")
print(f"required_boundary_alpha={alpha}")
print(f"required_boundary_phase={boundary_phase}")
print("boundary_phase_family_tunable=True")
print("canonical_phase_derivation_open=True")

