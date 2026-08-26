import hashlib
import json
from pathlib import Path

import sympy as sp


def incidence(vertex_count, edges):
    matrix = sp.zeros(vertex_count, len(edges))
    for column, (tail, head) in enumerate(edges):
        matrix[tail, column] = 1
        matrix[head, column] = -1
    return matrix


triangle_edges = [(0, 1), (1, 2), (0, 2)]
B_triangle = incidence(3, triangle_edges)
triangle_cycle = sp.Matrix([1, 1, -1])
assert B_triangle.rank() == 2
assert B_triangle * triangle_cycle == sp.zeros(3, 1)
assert len(triangle_edges) - B_triangle.rank() == 1

tree_edges = [(0, 1), (1, 2)]
B_tree = incidence(3, tree_edges)
assert B_tree.rank() == 2
assert len(tree_edges) - B_tree.rank() == 0

k4_edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]
B_k4 = incidence(4, k4_edges)
assert B_k4.rank() == 3
assert len(k4_edges) - B_k4.rank() == 3

# Gauge increments are B^T alpha; cycle pairing annihilates them.
a0, a1, a2 = sp.symbols("a0 a1 a2", real=True)
alpha = sp.Matrix([a0, a1, a2])
gauge_increment = B_triangle.T * alpha
assert sp.simplify((triangle_cycle.T * gauge_increment)[0]) == 0

payload = {
    "status": "pass",
    "theorem": "the_blown_up_zero_fiber_remembers_only_cycle_phase",
    "triangle": {"edges": 3, "effective_gauge_rank": 2, "zero_fiber_rank": 1},
    "tree": {"edges": 2, "effective_gauge_rank": 2, "zero_fiber_rank": 0},
    "K4": {"edges": 6, "effective_gauge_rank": 3, "zero_fiber_rank": 3},
    "triangle_cycle_vector": [1, 1, -1],
    "cycle_annihilates_gauge_increment": True,
    "complex_zero_fiber": "H^1(G; U(1))",
    "real_zero_fiber": "H^1(G; C2)",
    "blowup_repairs_amplitude": False,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "blown-up-zero-fiber.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
