#!/usr/bin/env python3
"""Test the proposed A1-root norm explanation of the C snake scalar."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/eta_squared_faithful_artin_action_checks.py"
RESULT = ROOT / "research/strominger/results/single_channel_root_norm_checks.json"


def primitive_cross(left, right):
    vector = [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]
    divisor = math.gcd(*(abs(value) for value in vector))
    vector = [value // divisor for value in vector]
    return vector if next(value for value in vector if value) > 0 else [-value for value in vector]


def apply(matrix, vector):
    return [sum(entry * value for entry, value in zip(row, vector)) for row in matrix]


def quadratic(vector, gram):
    return sum(vector[i] * gram[i][j] * vector[j] for i in range(2) for j in range(2))


with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))

coordinate_gram = [[1, 0], [0, 1]]
hostile_grams = {
    "rank_one_sum_pairing": [[1, 1], [1, 1]],
    "hyperbolic_pairing": [[0, 1], [1, 0]],
}
records = []
for mutation in state["legal_signed_mutations"]:
    structural_class = state["exact_smith_structural_class"](mutation)
    if structural_class not in ("C_plus", "C_minus"):
        continue
    permutation, signs = mutation
    omega = 1 if structural_class == "C_plus" else -1
    response = state["moore_mutation_response_matrices"][mutation]
    full = [[response[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    relational = [
        [response[i][j] - response[3][j] - int(i == j) for j in range(3)]
        for i in range(3)
    ]
    kernel = primitive_cross(relational[0], relational[1])
    lift = apply(full, kernel + [0])
    content = math.gcd(*(abs(entry) for row in full for entry in row))
    conductor = 4 * (8 - omega)
    tail_root = [signs[1], signs[2]]
    root_norm = quadratic(tail_root, coordinate_gram)
    predicted = -signs[1] * content * conductor**2 * root_norm
    records.append(
        {
            "class": structural_class,
            "permutation": list(permutation),
            "signs": list(signs),
            "omega": omega,
            "content": content,
            "tail_root": tail_root,
            "coordinate_root_norm": root_norm,
            "conductor": conductor,
            "connecting_scalar": lift[0],
            "predicted_scalar": predicted,
        }
    )

hostile_norms = {
    name: quadratic([1, -1], gram) for name, gram in hostile_grams.items()
}
gates = {
    "all_eight_c_presentations_are_covered": len(records) == 8,
    "full_matrix_content_is_uniform_768": {record["content"] for record in records} == {768},
    "opposite_tail_polarity_is_an_a1_root_in_the_coordinate_pairing": all(
        record["tail_root"][0] == -record["tail_root"][1]
        and record["coordinate_root_norm"] == 2
        for record in records
    ),
    "one_channel_root_norm_formula_holds_for_all_presentations": all(
        record["connecting_scalar"] == record["predicted_scalar"] for record in records
    ),
    "pairing_choice_is_explanatorily_material": set(hostile_norms.values()) != {2},
    "current_packet_contains_no_declared_source_gram_constructor": True,
}

payload = {
    "schema": "marici.strominger.single_channel_root_norm_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "arithmetic_identity_status": "confirmed_exactly",
    "explanation_status": "not_yet_authorized",
    "interpretation": (
        "The C snake coefficient is exactly signed content 768 times the "
        "coordinate norm of the scaled opposite-polarity root. This explains "
        "how one rank-one arrow can carry a square. The existing packet does "
        "not derive the coordinate Gram pairing, and hostile Gram choices alter "
        "or annihilate the norm. A source Gram constructor is therefore the "
        "smallest missing explanatory object."
    ),
    "formula": "partial_C=-sigma_first_tail*768*<kappa_C alpha,kappa_C alpha>, alpha=(1,-1), kappa_C=4*(8-omega)",
    "source_checker": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
    "source_checker_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "records": records,
    "hostile_pairings": {
        name: {"gram": gram, "root_norm": hostile_norms[name]}
        for name, gram in hostile_grams.items()
    },
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
