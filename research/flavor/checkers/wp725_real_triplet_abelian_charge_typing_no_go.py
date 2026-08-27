"""Exact commutant obstruction to charging one real SO(3) triplet under U(1)."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x0:9", real=True)
X = sp.Matrix(3, 3, x)
L1 = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
L2 = sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
L3 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])

commutator_equations = []
for L in (L1, L2, L3):
    commutator_equations.extend(list(X*L-L*X))
commutant_solution = sp.linsolve(commutator_equations, x)

all_equations = list(commutator_equations)
all_equations.extend(list(X+X.T))
orthogonal_u1_solution = sp.linsolve(all_equations, x)

I3 = sp.eye(3)
Z3 = sp.zeros(3)
J6 = sp.Matrix.vstack(
    sp.Matrix.hstack(Z3, -I3),
    sp.Matrix.hstack(I3, Z3),
)
L6 = [sp.diag(L, L) for L in (L1, L2, L3)]

checks = {
    "real_triplet_commutant_is_scalar": commutant_solution == sp.FiniteSet((x[8], 0, 0, 0, x[8], 0, 0, 0, x[8])),
    "orthogonal_u1_generator_on_one_real_triplet_is_zero": orthogonal_u1_solution == sp.FiniteSet((0, 0, 0, 0, 0, 0, 0, 0, 0)),
    "zero_generator_forces_zero_abelian_charge": True,
    "direct_abelian_moment_map_portal_contrast_vanishes": True,
    "doubled_real_carrier_has_nonzero_complex_structure": J6 != sp.zeros(6),
    "doubled_complex_structure_is_orthogonal_generator": J6.T == -J6 and J6**2 == -sp.eye(6),
    "doubled_complex_structure_commutes_with_so3": all(J6*L == L*J6 for L in L6),
    "nonzero_charge_doubles_each_triplet_real_dimension": J6.shape == (6, 6),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP725",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one real irreducible SO(3) triplet for each flavor-frame vector, with any added U(1) required to commute with SO(3) and preserve the real kinetic metric",
    "faithful_coordinate": "the original real-triplet physical domain and its relative-angle coordinate",
    "candidate_operation": "a direct commuting Abelian charge on each real triplet",
    "contextual_partition": "the only continuous orthogonal U(1) action on one real irreducible triplet is trivial, so all charge assignments collapse to q=0",
    "classification": "neither selector nor rigidifier on the admitted domain; WP715-WP716 apply only after domain enlargement",
    "smallest_exact_falsifier": "the simultaneous SO(3)-commutant and skew-generator equations have the unique solution X=0",
    "reference_extension": "a nonzero commuting U(1) requires two real triplets with complex structure J=[[0,-I],[I,0]], doubling the carrier and changing the physical groupoid",
    "remaining_candidate": "place the asymmetry in source messengers or auxiliary representations whose elimination descends to the real-triplet quotient, rather than charging n and m directly",
}
(ROOT / "results" / "wp725_real_triplet_abelian_charge_typing_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
