"""Exact hostile showing A3 endpoint data forgets pure-braid coherence."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "pure_braid_a3_coherence_checks.json"

I4 = sp.eye(4)
roots = sp.Matrix([
    [1, 0, 0],
    [-1, 1, 0],
    [0, -1, 1],
    [0, 0, -1],
])
left_inverse = (roots.T * roots).inv() * roots.T


def adjacent_swap(index):
    matrix = sp.eye(4)
    matrix[index, index] = 0
    matrix[index + 1, index + 1] = 0
    matrix[index, index + 1] = 1
    matrix[index + 1, index] = 1
    return matrix


permutation_generators = [adjacent_swap(i) for i in range(3)]
a3_generators = [sp.simplify(left_inverse * generator * roots) for generator in permutation_generators]
I3 = sp.eye(3)

sigma1_squared_endpoint = permutation_generators[0] ** 2
sigma1_squared_a3 = a3_generators[0] ** 2
sigma1_squared_exponent_sum = 2
pairwise_winding_count = len(list(__import__("itertools").combinations(range(4), 2)))

checks = {
    "projected_generators_preserve_A3_integrally": all(all(entry.is_Integer for entry in M) for M in a3_generators),
    "projected_generators_satisfy_adjacent_braid_relations": all(a3_generators[i] * a3_generators[i + 1] * a3_generators[i] == a3_generators[i + 1] * a3_generators[i] * a3_generators[i + 1] for i in range(2)),
    "distant_generators_commute": a3_generators[0] * a3_generators[2] == a3_generators[2] * a3_generators[0],
    "Weyl_projection_adds_involutive_relations": all(M**2 == I3 for M in a3_generators),
    "pure_braid_sigma1_squared_has_identity_endpoint_permutation": sigma1_squared_endpoint == I4,
    "pure_braid_sigma1_squared_is_invisible_on_A3": sigma1_squared_a3 == I3,
    "exponent_sum_proves_sigma1_squared_nontrivial_in_local_B4": sigma1_squared_exponent_sum != 0,
    "endpoint_and_A3_observations_alias_identity_and_pure_braid": sigma1_squared_endpoint == I4 and sigma1_squared_a3 == I3 and sigma1_squared_exponent_sum != 0,
    "four_strands_have_six_pairwise_winding_coordinates": pairwise_winding_count == 6,
    "three_static_A3_coordinates_do_not_equal_six_path_winding_coordinates": roots.rank() == 3 and pairwise_winding_count == 6,
}

payload = {
    "schema": "marici.strominger.pure-braid-a3-coherence.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "projection": {
        "local_path_group": "Artin braid group B4 in a disk chart of the celestial sphere",
        "endpoint_group": "S4",
        "lattice_action": "S4 acting on A3",
        "forgotten_kernel": "pure braid group P4",
        "smallest_hostile_word": "sigma_1^2",
        "hostile_exponent_sum": sigma1_squared_exponent_sum,
    },
    "next_witness": {
        "type": "BraidWitness",
        "fields": ["configuration_path_class", "Artin_word", "endpoint_permutation", "pure_braid_class", "attachment_holonomy"],
        "local_abelian_pairwise_winding_count": pairwise_winding_count,
    },
    "claim_boundary": "the six pairwise winding coordinates classify the abelianization of local pure-braid data, not the full nonabelian pure braid group; no identification with Aspect's 3+2+1 ports is asserted",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
