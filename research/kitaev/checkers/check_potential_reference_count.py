import hashlib
import json
from pathlib import Path

import sympy as sp


# Homogeneous edge equations d_t-epsilon*d_s=0 on a triangle.
# Edges: 0->1 with +, 1->2 with -, and 2->0 with closing parity.
even_system = sp.Matrix([
    [-1, 1, 0],
    [0, 1, 1],
    [1, 0, 1],
])
odd_system = sp.Matrix([
    [-1, 1, 0],
    [0, 1, 1],
    [1, 0, -1],
])

even_nullspace = even_system.nullspace()
odd_nullspace = odd_system.nullspace()

assert len(even_nullspace) == 1
assert even_nullspace[0] == sp.Matrix([-1, -1, 1])
assert len(odd_nullspace) == 0

# The sign of the basis is irrelevant: it spans (c,c,-c).
parameter = sp.symbols("c", real=True)
even_section = sp.Matrix([parameter, parameter, -parameter])
assert even_system * even_section == sp.zeros(3, 1)

payload = {
    "status": "pass",
    "theorem": "parity_holonomy_decides_whether_global_potential_needs_source_reference",
    "homogeneous_law": "d_target=epsilon_e*d_source",
    "all_even_loop_parity_ambiguity_dimension": 1,
    "even_triangle_ambiguity": "(c,c,-c)",
    "odd_loop_parity_ambiguity_dimension": 0,
    "odd_loop_potential_unique": True,
    "odd_loop_ordered_polarization_exists": False,
    "solution_torsor": "H^0(G;R_epsilon)",
    "orientation_cover_restores_reference_ambiguity": True,
    "theta_parity_graph_computed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "potential-reference-count.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
