"""Small hostile tests for complex lattice-divergence continuations."""

import sympy as sp

w = 1 + sp.I
holomorphic_real_part = sp.simplify(2 * sp.re(w - 1 - sp.log(w)))
assert sp.simplify(holomorphic_real_part + sp.log(2)) == 0
assert holomorphic_real_part < 0

x = sp.symbols("x", positive=True)
radial = x - 1 - sp.log(x)
assert sp.simplify(sp.diff(radial, x) - (1 - 1 / x)) == 0
assert sp.simplify(sp.diff(radial, x, 2) - 1 / x**2) == 0
assert radial.subs(x, 1) == 0

theta = sp.symbols("theta", real=True)
unit_phase = sp.exp(sp.I * theta)
radial_on_rotation = sp.simplify(sp.Abs(unit_phase) ** 2 - 1 - sp.log(sp.Abs(unit_phase) ** 2))
assert radial_on_rotation == 0

print(f"hostile_gap_multiplier={w}")
print(f"holomorphic_real_part={holomorphic_real_part}")
print("holomorphic_positivity=False")
print("Hermitian_radial_divergence_nonnegative=True")
print("Hermitian_radial_rotation_blind=True")
print("phase_sensitive_reflection_pairing_required=True")
