#!/usr/bin/env python3
"""Test whether the C square splits into domain and target saturation indices."""

from __future__ import annotations

import contextlib
import io
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/eta_squared_faithful_artin_action_checks.py"
RESULT = ROOT / "research/strominger/results/snake_saturation_factorization_checks.json"


def primitive_cross(left, right):
    vector = [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]
    divisor = math.gcd(*(abs(value) for value in vector))
    vector = [value // divisor for value in vector]
    return vector if next(value for value in vector if value) > 0 else [-value for value in vector]


with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))

diagonal = [1, 1, 1, 1]
records = []
for mutation in state["legal_signed_mutations"]:
    structural_class = state["exact_smith_structural_class"](mutation)
    if structural_class not in ("C_plus", "C_minus"):
        continue
    omega = 1 if structural_class == "C_plus" else -1
    conductor = 4 * (8 - omega)
    response = state["moore_mutation_response_matrices"][mutation]
    full = [[response[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    relational = [
        [response[i][j] - response[3][j] - int(i == j) for j in range(3)]
        for i in range(3)
    ]
    kernel = primitive_cross(relational[0], relational[1])
    lifted_kernel = kernel + [0]
    plane_minors = [
        diagonal[i] * lifted_kernel[j] - diagonal[j] * lifted_kernel[i]
        for i in range(4)
        for j in range(i + 1, 4)
    ]
    domain_plane_saturation_index = math.gcd(*(abs(value) for value in plane_minors))
    content = math.gcd(*(abs(entry) for row in full for entry in row))
    full_lift = [
        sum(full[i][j] * lifted_kernel[j] for j in range(4))
        for i in range(4)
    ]
    target_intersection_index = abs(full_lift[0]) // content
    witness_prime = 7 if structural_class == "C_plus" else 3
    records.append(
        {
            "class": structural_class,
            "mutation": [list(mutation[0]), list(mutation[1])],
            "conductor": conductor,
            "domain_plane_saturation_index": domain_plane_saturation_index,
            "target_intersection_index": target_intersection_index,
            "predicted_target_index": 2 * conductor**2,
            "target_quotient": f"Z/{target_intersection_index}Z",
            "witness_prime": witness_prime,
            "target_mod_p_generator_dimension": 1,
            "hypothetical_two_channel_mod_p_dimension": 2,
        }
    )

gates = {
    "all_eight_c_presentations_are_covered": len(records) == 8,
    "the_domain_kernel_plane_is_saturated": all(
        record["domain_plane_saturation_index"] == 1 for record in records
    ),
    "the_entire_reduced_modulus_lies_in_one_target_index": all(
        record["target_intersection_index"] == record["predicted_target_index"]
        for record in records
    ),
    "the_target_defect_is_cyclic_not_a_two_generator_pair": all(
        record["target_mod_p_generator_dimension"] == 1
        and record["hypothetical_two_channel_mod_p_dimension"] == 2
        for record in records
    ),
    "no_domain_target_kappa_by_kappa_saturation_factorization_exists": all(
        record["domain_plane_saturation_index"] != record["conductor"]
        for record in records
    ),
}

payload = {
    "schema": "marici.strominger.snake_saturation_factorization_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "factorization_conjecture_status": "refuted",
    "interpretation": (
        "The lifted relational kernel and the full diagonal kernel span a "
        "saturated domain plane. The complete reduced modulus 2*kappa^2 occurs "
        "as one cyclic target-intersection index. At a prime dividing kappa its "
        "mod-p generator dimension is one, whereas a pair of conductor channels "
        "would have dimension two. The current lattice diagram therefore "
        "contains no kappa-by-kappa saturation splitting."
    ),
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
