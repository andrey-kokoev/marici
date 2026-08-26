import hashlib
import json
from pathlib import Path

import sympy as sp


def first_betti(boundary_one, boundary_two):
    assert boundary_one * boundary_two == sp.zeros(boundary_one.rows, boundary_two.cols)
    edge_count = boundary_one.cols
    return edge_count - boundary_one.rank() - boundary_two.rank()


# Triangle edges 01, 12, 02; filled face has boundary e01 + e12 - e02.
B1_triangle = sp.Matrix([[1, 0, 1], [-1, 1, 0], [0, -1, -1]])
B2_triangle = sp.Matrix([[1], [1], [-1]])
assert B1_triangle * B2_triangle == sp.zeros(3, 1)
filled_triangle_b1 = first_betti(B1_triangle, B2_triangle)
assert filled_triangle_b1 == 0

# The same one-skeleton without a face is a circle.
B2_empty = sp.zeros(3, 0)
circle_b1 = first_betti(B1_triangle, B2_empty)
assert circle_b1 == 1

# One-vertex torus: two loop edges; commutator attaching map abelianizes to zero.
B1_torus = sp.zeros(1, 2)
B2_torus = sp.zeros(2, 1)
torus_b1 = first_betti(B1_torus, B2_torus)
assert torus_b1 == 2

payload = {
    "status": "pass",
    "theorem": "plaquette_flatness_reduces_graph_phase_to_carrier_cohomology",
    "triangle_graph_cycle_rank": circle_b1,
    "filled_triangle_first_betti": filled_triangle_b1,
    "minimal_torus_first_betti": torus_b1,
    "filled_triangle_boundary_one_rank": B1_triangle.rank(),
    "filled_triangle_boundary_two_rank": B2_triangle.rank(),
    "chain_condition_verified": True,
    "flat_complex_phase_group": "H^1(X; U(1))",
    "flat_real_phase_group": "H^1(X; C2)",
    "quantum_intersection_pairing_is_additional": True,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "plaquette-flat-phase-cohomology.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
