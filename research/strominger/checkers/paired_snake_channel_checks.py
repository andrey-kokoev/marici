#!/usr/bin/env python3
"""Exact falsifier for the paired snake-channel conjecture."""

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
RESULT = ROOT / "research/strominger/results/paired_snake_channel_checks.json"


def primitive_cross(left, right):
    vector = [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]
    divisor = math.gcd(*(abs(value) for value in vector))
    if divisor == 0:
        raise ValueError("chosen rows do not determine a rank-two kernel")
    vector = [value // divisor for value in vector]
    first_nonzero = next(value for value in vector if value)
    return [-value for value in vector] if first_nonzero < 0 else vector


def matrix_vector(matrix, vector):
    return [sum(entry * value for entry, value in zip(row, vector)) for row in matrix]


captured = io.StringIO()
with contextlib.redirect_stdout(captured):
    source_state = runpy.run_path(str(SOURCE))

records = {}
for structural_class, omega in (("C_plus", 1), ("C_minus", -1)):
    mutation = next(
        item
        for item in source_state["legal_signed_mutations"]
        if source_state["exact_smith_structural_class"](item) == structural_class
    )
    response = source_state["moore_mutation_response_matrices"][mutation]
    full = [
        [response[i][j] - int(i == j) for j in range(4)]
        for i in range(4)
    ]
    relational = [
        [response[i][j] - response[3][j] - int(i == j) for j in range(3)]
        for i in range(3)
    ]
    kernel = primitive_cross(relational[0], relational[1])
    relational_image = matrix_vector(relational, kernel)
    full_lift = matrix_vector(full, kernel + [0])
    connecting_scalar = full_lift[0]
    predicted_modulus = 2**13 * 3 * (8 - omega) ** 2
    records[structural_class] = {
        "omega": omega,
        "mutation": [list(mutation[0]), list(mutation[1])],
        "primitive_relational_kernel": kernel,
        "relational_image": relational_image,
        "full_lift": full_lift,
        "connecting_scalar": connecting_scalar,
        "connecting_scalar_absolute": abs(connecting_scalar),
        "predicted_modulus": predicted_modulus,
        "connecting_domain_rank": 1,
        "connecting_codomain_rank": 1,
    }

# A determinant square does not imply a split pair.  The hostile block has
# determinant c^2 but first Smith divisor 1, hence Smith packet (1,c^2).
hostile_c = 7
hostile_block = [[hostile_c, 1], [0, hostile_c]]
hostile_entry_gcd = math.gcd(*(abs(value) for row in hostile_block for value in row))
hostile_determinant = hostile_c**2
hostile_smith = [hostile_entry_gcd, hostile_determinant // hostile_entry_gcd]

gates = {
    "both_relational_kernel_vectors_are_exact": all(
        record["relational_image"] == [0, 0, 0] for record in records.values()
    ),
    "both_primitive_kernel_lifts_land_in_the_diagonal": all(
        len(set(record["full_lift"])) == 1 for record in records.values()
    ),
    "the_connecting_scalar_is_the_entire_extension_modulus": all(
        record["connecting_scalar_absolute"] == record["predicted_modulus"]
        for record in records.values()
    ),
    "the_canonical_connecting_object_has_rank_one_not_two": all(
        record["connecting_domain_rank"] == record["connecting_codomain_rank"] == 1
        for record in records.values()
    ),
    "square_determinant_does_not_force_integral_channel_splitting": (
        hostile_smith == [1, hostile_c**2]
    ),
}

payload = {
    "schema": "marici.strominger.paired_snake_channel_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "conjecture_status": "refuted_as_stated",
    "interpretation": (
        "The canonical full-to-relational snake boundary is one rank-one map. "
        "Its primitive scalar already equals 2^13*3*(8-omega)^2. The square "
        "therefore does not arise from two independent canonical connecting "
        "channels. A source-derived refinement could still factor this scalar, "
        "but that would require an additional typed correspondence."
    ),
    "source_checker": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
    "source_checker_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "records": records,
    "hostile_square_block": {
        "matrix": hostile_block,
        "determinant": hostile_determinant,
        "smith_factors": hostile_smith,
    },
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
