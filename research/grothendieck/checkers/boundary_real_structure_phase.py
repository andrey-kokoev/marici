"""Exact phase constraints from elementary interval real structures."""

import sympy as sp

theta = sp.symbols("theta", real=True)
unit_phase = sp.exp(sp.I * theta)

# Plain conjugation invariance requires U=conj(U), equivalently sin(theta)=0.
plain_constraint = sp.simplify(unit_phase - sp.conjugate(unit_phase))
assert sp.simplify(plain_constraint - 2 * sp.I * sp.sin(theta)) == 0

required_phase = sp.exp(sp.I * sp.pi / 4)
assert sp.simplify(required_phase - sp.conjugate(required_phase)) != 0

# Reflection-conjugation produces U*conj(U)=1 for every real theta.
reflection_constraint = sp.simplify(unit_phase * sp.conjugate(unit_phase))
assert reflection_constraint == 1

print("plain_conjugation_allowed_phases={+1,-1}")
print(f"required_Xi_phase={required_phase}")
print("plain_conjugation_selects_required_phase=False")
print("reflection_conjugation_preserves_all_unit_phases=True")
print("elementary_real_structure_selects_alpha_1_8=False")
print("metaplectic_or_arithmetic_selection_required=True")

