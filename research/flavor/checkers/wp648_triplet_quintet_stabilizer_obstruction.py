"""Exact WP648 stabilizer obstruction for one real triplet plus quintet."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
q1, q2, v, a, b = sp.symbols("q1 q2 v a b", real=True, nonzero=True)
Q = sp.diag(q1, q2, -q1-q2)
n = sp.Matrix([0, 0, v])
P = a*Q+b*Q**2
R = sp.diag(-1, -1, 1)
orientation_equation = sp.simplify(n.cross(P*n))
checks = {
    "quintet_is_symmetric_traceless": Q == Q.T and sp.trace(Q) == 0,
    "generic_stationary_eigenaxis_solves_orientation_equation": orientation_equation == sp.zeros(3, 1),
    "half_turn_is_proper_rotation": R.T*R == sp.eye(3) and sp.det(R) == 1,
    "half_turn_is_nonidentity": R != sp.eye(3),
    "half_turn_fixes_triplet": R*n == n,
    "half_turn_fixes_quintet": sp.simplify(R*Q*R.T-Q) == sp.zeros(3),
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP648", "status": "PASS", "checks": checks,
    "field_content": "one real SO(3) triplet n plus one real symmetric-traceless quintet Q",
    "renormalizable_orientation_invariants": ["n^T Q n", "n^T Q^2 n"],
    "generic_stationarity": "n is an eigenvector of aQ+bQ^2; for nondegenerate polynomial spectrum it is an eigenvector of Q",
    "residual_stabilizer_witness": "R=diag(-1,-1,1) in the Q eigenbasis with n parallel to e3",
    "classification": "dynamical symmetry breaking and rigidification, but not a faithful oriented frame and not a physical16 selector",
    "smallest_exact_falsifier": "a generic stationary nondegenerate one-triplet/one-quintet vacuum with trivial SO(3) stabilizer",
    "remaining_gate": "add an independently sourced second noncollinear vector or tensor, then derive rather than fit the relative vacuum and matching law",
}
(ROOT / "results" / "wp648_triplet_quintet_stabilizer_obstruction.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
