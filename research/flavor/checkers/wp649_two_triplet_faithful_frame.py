"""Exact WP649 positive two-triplet faithful-frame construction."""
import json
import runpy
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x0:6", real=True)
n, m = sp.Matrix(x[:3]), sp.Matrix(x[3:])
potential = (n.dot(n)-1)**2 + (m.dot(m)-1)**2 + (n.dot(m))**2
vacuum_values = dict(zip(x, [1, 0, 0, 0, 1, 0]))
gradient = sp.Matrix([sp.diff(potential, z) for z in x]).subs(vacuum_values)
hessian = sp.hessian(potential, x).subs(vacuum_values)
n0, m0 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])

# Infinitesimal stabilizer map omega -> (omega cross n, omega cross m).
w1, w2, w3 = sp.symbols("w1 w2 w3")
w = sp.Matrix([w1, w2, w3])
stabilizer_map = sp.Matrix.vstack(w.cross(n0), w.cross(m0)).jacobian([w1, w2, w3])

wp646 = runpy.run_path(str(ROOT / "checkers" / "wp646_nonaligned_word_response_ladder.py"))
words = [sp.eye(3), wp646["J"][0], wp646["J"][1]]
response = wp646["response"](words)

checks = {
    "vacuum_is_stationary": gradient == sp.zeros(6, 1),
    "vacuum_is_orthonormal_ordered_pair": n0.dot(n0) == 1 and m0.dot(m0) == 1 and n0.dot(m0) == 0,
    "hessian_has_three_goldstones": len(hessian.nullspace()) == 3,
    "hessian_has_three_positive_physical_modes": hessian.eigenvals() == {sp.Integer(8): 2, sp.Integer(4): 1, sp.Integer(0): 3},
    "infinitesimal_stabilizer_is_trivial": stabilizer_map.rank() == 3,
    "derived_third_axis_completes_oriented_frame": sp.Matrix.hstack(n0, m0, n0.cross(m0)) == sp.eye(3),
    "two_triplet_word_response_shape_is_ten_by_twelve": response.shape == (10, 12),
    "two_triplet_word_response_rank_is_eight": response.rank() == 8,
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP649", "status": "PASS", "checks": checks,
    "source_action": "(|n|^2-1)^2+(|m|^2-1)^2+(n dot m)^2",
    "vacuum": "ordered orthonormal pair; third axis n cross m is derived",
    "stabilizer": "trivial in SO(3)",
    "hessian_spectrum": {"zero_goldstones": 3, "positive_physical": [4, 8, 8]},
    "induced_words_per_sector": ["I", "J_n", "J_m"],
    "exact_hostile_witness_response_rank": 8,
    "classification": "source-generated faithful frame and presentation rigidifier; not a physical16 selector",
    "smallest_exact_falsifier": "a nonidentity SO(3) rotation fixing both ordered noncollinear triplets",
    "remaining_gate": "derive the sector coupling coefficients and a detector-typed matching law; test any resulting relation across all 1210 sheets",
}
(ROOT / "results" / "wp649_two_triplet_faithful_frame.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
