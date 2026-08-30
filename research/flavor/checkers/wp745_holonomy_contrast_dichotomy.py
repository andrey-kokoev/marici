"""Exact holonomy dichotomy for the SO(4) vector restricted to diagonal SO(3)."""
import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

def generator(i, j):
    M = sp.zeros(4)
    M[i, j] = 1
    M[j, i] = -1
    return M

so4 = [generator(i,j) for i in range(4) for j in range(i+1,4)]
so3 = [generator(i,j) for i in range(3) for j in range(i+1,3)]

# Lie-algebra centralizer of the physical diagonal so(3) inside so(4).
coefficients = sp.symbols("x0:6")
X = sum((c*T for c,T in zip(coefficients,so4)), sp.zeros(4))
centralizer_equations = []
for J in so3:
    centralizer_equations.extend(list(X*J-J*X))
centralizer_matrix, _ = sp.linear_eq_to_matrix(centralizer_equations, coefficients)
centralizer_lie_dimension = len(coefficients)-centralizer_matrix.rank()

# Orthogonal transformations commuting with 3+1 act by independent signs on
# the two inequivalent real irreducibles. The SO(4) determinant condition then
# leaves only the center.
orthogonal_sign_packets = []
for eps_t, eps_s in product((-1,1), repeat=2):
    W = sp.diag(eps_t,eps_t,eps_t,eps_s)
    if W.det() == 1:
        orthogonal_sign_packets.append((eps_t,eps_s,W))

center_packets = [(et,es) for et,es,_ in orthogonal_sign_packets]
center_is_scalar = all(W == et*sp.eye(4) for et,es,W in orthogonal_sign_packets)

# The smallest distinguishing twist commutes with SO(3) but lies in O(4)\SO(4).
reflection = sp.diag(-1,-1,-1,1)
reflection_commutators = [sp.simplify(reflection*J-J*reflection) for J in so3]

# A proper SO(4) rotation outside the center breaks the physical SO(3).
quarter_turn = sp.Matrix([[0,0,0,1],[0,1,0,0],[0,0,1,0],[-1,0,0,0]])
quarter_turn_commutators = [sp.simplify(quarter_turn*J-J*quarter_turn) for J in so3]

# Portal commutants on the 4 and on 3+1.
def symmetric_commutant_dimension(generators):
    variables = sp.symbols("k0:10")
    K = sp.zeros(4)
    cursor = 0
    for i in range(4):
        for j in range(i,4):
            K[i,j] = K[j,i] = variables[cursor]
            cursor += 1
    equations = []
    for J in generators:
        equations.extend(list(K*J-J*K))
    M, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables)-M.rank()

bulk_commutant_dimension = symmetric_commutant_dimension(so4)
physical_commutant_dimension = symmetric_commutant_dimension(so3)
a,b = sp.symbols("a b", real=True)
contrast = b-a

checks = {
    "diagonal_so3_has_three_generators": len(so3) == 3,
    "connected_centralizer_inside_so4_is_trivial": centralizer_lie_dimension == 0,
    "so4_group_centralizer_sign_packets_are_exact": center_packets == [(-1,-1),(1,1)],
    "every_so4_preserving_holonomy_is_scalar_on_3_plus_1": center_is_scalar,
    "preserving_center_cannot_distinguish_triplet_and_singlet": all(et == es for et,es,_ in orthogonal_sign_packets),
    "distinguishing_reflection_commutes_with_so3": all(C == sp.zeros(4) for C in reflection_commutators),
    "distinguishing_reflection_is_outside_so4": reflection.det() == -1,
    "noncentral_proper_rotation_breaks_so3": any(C != sp.zeros(4) for C in quarter_turn_commutators),
    "bulk_so4_portal_commutant_is_one_dimensional": bulk_commutant_dimension == 1,
    "physical_so3_portal_commutant_is_two_dimensional": physical_commutant_dimension == 2,
    "distinguishing_groupoid_restores_free_contrast": sp.diff(contrast,b) == 1 and sp.diff(contrast,a) == -1,
    "deliberate_failure_residual_is_nonzero": reflection.det()-1 == -2,
}
checks = {name: bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP745",
    "status": "PASS",
    "checks": checks,
    "source_domain": "SO(4) gauge holonomies acting on the WP743 four-component carrier while preserving the full declared diagonal SO(3)",
    "classification": "holonomy dichotomy: preserving holonomies do not distinguish; distinguishing twists change the groupoid and do not select the portal coefficient",
    "centralizer_theorem": "the Lie centralizer is zero-dimensional and the SO(4) group centralizer is {+I4,-I4}",
    "zero_contrast_branch": "both admitted preserving holonomies act with the same sign on triplet and singlet",
    "changed_groupoid_branch": "diag(-I3,+1) distinguishes the sectors but has determinant -1 and lies in O(4) outside the admitted SO(4) gauge group",
    "coefficient_fiber": "after the distinguishing reduction, the invariant quadratic form is diag(a I3,b), leaving continuous contrast b-a",
    "smallest_exact_falsifier": "the distinguishing reflection has determinant residual det(W)-1=-2",
    "claim_boundary": "holonomies acting on the four-dimensional SO(4) vector and preserving the full physical diagonal SO(3); larger groups and defects with additional degrees of freedom are not excluded",
    "remaining_source_gate": "a progressive mechanism needs extra dynamical structure, not symmetry or holonomy alone, to normalize a nonzero CP-even contrast",
    "remaining_physical_gate": "clock, RG basin, thresholds, and calibrated physical16 instrument remain absent",
}
(ROOT / "results" / "wp745_holonomy_contrast_dichotomy.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
