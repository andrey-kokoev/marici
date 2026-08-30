"""Exact tradeoff between forbidding the correlation quartic and frame rigidity."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
n1, n2, n3, m1, m2, m3 = sp.symbols("n1 n2 n3 m1 m2 m3", real=True)
fields = (n1, n2, n3, m1, m2, m3)
n = sp.Matrix([n1, n2, n3])
m = sp.Matrix([m1, m2, m3])
a = n.dot(n)
b = m.dot(m)
c = n.dot(m)

V_norm = (a-1)**2 + (b-1)**2
V_frame = V_norm + c**2
vacuum = {n1: 1, n2: 0, n3: 0, m1: 0, m2: 1, m3: 0}

H_norm = sp.hessian(V_norm, fields).subs(vacuum)
H_frame = sp.hessian(V_frame, fields).subs(vacuum)
spec_norm = sorted([value for value, multiplicity in H_norm.eigenvals().items() for _ in range(multiplicity)])
spec_frame = sorted([value for value, multiplicity in H_frame.eigenvals().items() for _ in range(multiplicity)])

# One independent rotation changes only m and demonstrates noninvariance of c^2.
aligned = {n1: 1, n2: 0, n3: 0, m1: 1, m2: 0, m3: 0}
independently_rotated = vacuum

# Diagonal infinitesimal rotations act as (omega cross n, omega cross m).
wx, wy, wz = sp.symbols("omega_x omega_y omega_z", real=True)
omega = sp.Matrix([wx, wy, wz])
orbit_map = sp.Matrix.vstack(omega.cross(n), omega.cross(m)).subs(vacuum)
orbit_jacobian = orbit_map.jacobian((wx, wy, wz))

checks = {
    "correlation_changes_under_independent_rotation": (c**2).subs(aligned) == 1 and (c**2).subs(independently_rotated) == 0,
    "norm_quartics_survive_independent_rotation": V_norm.subs(aligned) == V_norm.subs(independently_rotated),
    "norm_only_hessian_has_four_zeros": spec_norm == [0, 0, 0, 0, 8, 8],
    "diagonal_rotation_orbit_has_dimension_three": orbit_jacobian.rank() == 3,
    "one_norm_only_zero_is_physical": len(H_norm.nullspace())-orbit_jacobian.rank() == 1,
    "correlation_quartic_lifts_physical_angle": spec_frame == [0, 0, 0, 4, 8, 8],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP706",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the WP649/WP661 ordered two-triplet scalar frame and its common diagonal SO(3) flavor interface",
    "candidate_protecting_symmetry": "independent SO(3)_n x SO(3)_m rotations forbid (n dot m)^2 but exceed the admitted common flavor symmetry",
    "contextual_partition": "the enlarged symmetry identifies relative orientations in the isolated scalar theory, while the common quark/messenger interface restores their physical relevance and permits the quartic",
    "classification": "candidate slice protector and frame rigidifier are incompatible in the current grammar; neither produces a completed selector",
    "smallest_exact_falsifier": "without (n dot m)^2 the Hessian has four zeros but the diagonal orbit has dimension three, leaving one physical angular modulus",
    "remaining_gate": "a distinct source symmetry or grading must forbid lambda_c, retain a common physical flavor interface, lift the relative angle by another source term, and survive RG and thresholds",
}
(ROOT / "results" / "wp706_c_forbidding_symmetry_tradeoff.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
