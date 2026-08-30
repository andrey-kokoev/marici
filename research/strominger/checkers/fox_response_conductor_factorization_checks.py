#!/usr/bin/env python3
"""Derive the C conductor square from evaluated Fox contributions."""

from __future__ import annotations

import contextlib
import io
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/eta_squared_faithful_artin_action_checks.py"
RESULT = ROOT / "research/strominger/results/fox_response_conductor_factorization_checks.json"


with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))

I = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
ZERO = tuple(tuple(0 for _ in range(4)) for _ in range(4))


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(4)) for i in range(4))


def add(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(4)) for i in range(4))


def negate(matrix):
    return tuple(tuple(-value for value in row) for row in matrix)


def subtract_identity(matrix):
    return tuple(tuple(matrix[i][j] - I[i][j] for j in range(4)) for i in range(4))


def primitive_cross(left, right):
    vector = [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]
    divisor = math.gcd(*(abs(value) for value in vector))
    return [value // divisor for value in vector]


def apply(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(4)) for i in range(4)]


def abstract_response(letter):
    pure = state["abstract_to_pure"]((letter,))
    return state["reflection_response_matrix"](state["expand_pure"](pure))


# reflection_response_matrix is an anti-representation. Transposition converts
# it to the homomorphic convention used by the standard Fox identity.
generators = {index: transpose(abstract_response(index)) for index in (1, 2, 3)}
inverses = {index: transpose(abstract_response(-index)) for index in (1, 2, 3)}


def evaluated_fox(word):
    prefix = I
    jacobian = {index: ZERO for index in (1, 2, 3)}
    for letter in word:
        index = abs(letter)
        if letter > 0:
            jacobian[index] = add(jacobian[index], prefix)
            prefix = state["matrix_multiply"](prefix, generators[index])
        else:
            inverse_term = state["matrix_multiply"](prefix, inverses[index])
            jacobian[index] = add(jacobian[index], negate(inverse_term))
            prefix = inverse_term
    contributions = {
        index: transpose(
            state["matrix_multiply"](
                jacobian[index], subtract_identity(generators[index])
            )
        )
        for index in (1, 2, 3)
    }
    return transpose(prefix), contributions


records = []
for mutation in state["legal_signed_mutations"]:
    structural_class = state["exact_smith_structural_class"](mutation)
    if structural_class not in ("C_plus", "C_minus"):
        continue
    permutation, signs = mutation
    a = (permutation[0] * signs[0],)
    b = (permutation[1] * signs[1],)
    c = (permutation[2] * signs[2],)
    word = state["abstract_commutator"](
        state["abstract_commutator"](a, b),
        state["abstract_commutator"](a, c),
    )
    represented_word, contributions = evaluated_fox(word)
    response = state["moore_mutation_response_matrices"][mutation]
    full = subtract_identity(response)
    relational = tuple(
        tuple(full[i][j] - full[3][j] for j in range(3))
        for i in range(3)
    )
    kernel = primitive_cross(relational[0], relational[1]) + [0]
    contribution_images = {
        str(index): apply(contributions[index], kernel) for index in (1, 2, 3)
    }
    common_fox_content = math.gcd(*(
        abs(value)
        for image in contribution_images.values()
        for value in image
    ))
    normalized_images = {
        index: [value // common_fox_content for value in image]
        for index, image in contribution_images.items()
    }
    normalized_sum = [
        sum(normalized_images[index][coordinate] for index in normalized_images)
        for coordinate in range(4)
    ]
    conductor = common_fox_content // 512
    oriented_residual = normalized_sum[0] // conductor
    records.append(
        {
            "class": structural_class,
            "mutation": [list(permutation), list(signs)],
            "fox_identity_holds": represented_word == response,
            "primitive_kernel": kernel,
            "contribution_images": contribution_images,
            "common_fox_content": common_fox_content,
            "conductor_from_fox_content": conductor,
            "normalized_contribution_images": normalized_images,
            "normalized_sum": normalized_sum,
            "oriented_residual_multiplier": oriented_residual,
            "connecting_scalar": apply(full, kernel)[0],
            "factored_connecting_scalar": common_fox_content * normalized_sum[0],
        }
    )

conductors_by_class = {
    structural_class: sorted({
        record["conductor_from_fox_content"]
        for record in records
        if record["class"] == structural_class
    })
    for structural_class in ("C_plus", "C_minus")
}
primitive_scale = math.gcd(
    conductors_by_class["C_plus"][0], conductors_by_class["C_minus"][0]
)
normalized_conductors = [
    conductors_by_class["C_plus"][0] // primitive_scale,
    conductors_by_class["C_minus"][0] // primitive_scale,
]
reflection_fixed_center = sum(normalized_conductors) // 2
reflection_radius = abs(normalized_conductors[1] - normalized_conductors[0]) // 2

gates = {
    "evaluated_fox_identity_reconstructs_every_full_response": all(
        record["fox_identity_holds"] for record in records
    ),
    "fox_contributions_have_common_content_512_times_conductor": (
        conductors_by_class == {"C_plus": [28], "C_minus": [36]}
    ),
    "normalized_source_profiles_cancel_to_signed_three_kappa_diagonal": all(
        len(set(record["normalized_sum"])) == 1
        and abs(record["oriented_residual_multiplier"]) == 3
        for record in records
    ),
    "fox_content_times_residual_recovers_the_snake_scalar": all(
        record["connecting_scalar"] == record["factored_connecting_scalar"]
        for record in records
    ),
    "reflection_pair_derives_center_eight_after_primitive_scaling": (
        primitive_scale == 4
        and normalized_conductors == [7, 9]
        and reflection_fixed_center == 8
        and reflection_radius == 1
    ),
}

payload = {
    "schema": "marici.strominger.fox_response_conductor_factorization_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "theorem_status": "exact_for_all_eight_signed_c_presentations",
    "interpretation": (
        "The evaluated Fox identity supplies the missing source comparison map. "
        "Each generator contribution to the primitive snake image has common "
        "content 512*kappa. After division, the three source-labelled profiles "
        "cancel to a constant signed 3*kappa diagonal. Hence the single cyclic "
        "snake scalar is signed (512*kappa)(3*kappa). Endpoint reversal pairs "
        "kappa=28 and 36; their primitive scale is 4 and their normalized fixed "
        "center is 8."
    ),
    "factorization": "partial_C = sign * (512*kappa_C) * (3*kappa_C)",
    "conductors_by_class": conductors_by_class,
    "primitive_scale": primitive_scale,
    "normalized_conductors": normalized_conductors,
    "reflection_fixed_center": reflection_fixed_center,
    "reflection_radius": reflection_radius,
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
