"""Exact phase arithmetic for the Fresnel/Maslov 1/8 candidate."""

import sympy as sp

principal_fresnel_phase = sp.exp(sp.I * sp.pi / 4)
continued_square_root = sp.sqrt(sp.I)
assert sp.simplify(sp.re(continued_square_root) - sp.sqrt(2) / 2) == 0
assert sp.simplify(sp.im(continued_square_root) - sp.sqrt(2) / 2) == 0

alpha = sp.Rational(1, 8)
assert sp.simplify(sp.exp(2 * sp.pi * sp.I * alpha) - principal_fresnel_phase) == 0
assert 1 - alpha == sp.Rational(7, 8)

for signature in range(-4, 5):
    phase = sp.exp(sp.I * sp.pi * signature / 4)
    assert sp.simplify(phase**8 - 1) == 0

opposite_phase = sp.exp(-sp.I * sp.pi / 4)
assert sp.simplify(principal_fresnel_phase * opposite_phase - 1) == 0
assert sp.simplify(principal_fresnel_phase - opposite_phase) != 0

print(f"signature_plus_one_phase={principal_fresnel_phase}")
print(f"Maslov_boundary_offset={alpha}")
print("phase_space_constant_minus_offset=7/8")
print("metaplectic_phases_are_eighth_roots=True")
print("orientation_reversal_changes_phase=True")
print("Xi_Maslov_signature_constructed=False")
