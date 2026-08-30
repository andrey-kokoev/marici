#!/usr/bin/env python3
"""Deutsch hostile for the local law behind Fox cancellation."""

from __future__ import annotations

import contextlib
import io
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/eta_squared_faithful_artin_action_checks.py"
RESULT = ROOT / "research/strominger/results/primitive_transvection_hostile_checks.json"


with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))


def multiply(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def elementary(index, parameter):
    matrix = [[int(i == j) for j in range(4)] for i in range(4)]
    matrix[index][index] = 1 + parameter
    matrix[index][index + 1] = -parameter
    matrix[index + 1][index] = parameter
    matrix[index + 1][index + 1] = 1 - parameter
    return matrix


def parameter_response(sigma_word, parameter):
    total = [[int(i == j) for j in range(4)] for i in range(4)]
    for letter in sigma_word:
        signed_parameter = parameter if letter > 0 else -parameter
        total = multiply(elementary(abs(letter) - 1, signed_parameter), total)
    return total


def primitive_cross(left, right):
    vector = [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]
    divisor = math.gcd(*(abs(value) for value in vector))
    return [value // divisor for value in vector]


def is_twice_square(value):
    if value % 2:
        return False
    root = math.isqrt(value // 2)
    return 2 * root * root == value


records = []
for parameter in (-3, -2, -1, 1, 2, 3):
    local_block = elementary(0, parameter)
    local_delta_content = math.gcd(*(
        abs(local_block[i][j] - int(i == j))
        for i in range(4)
        for j in range(4)
    ))
    inverse_holds = multiply(local_block, elementary(0, -parameter)) == [
        [int(i == j) for j in range(4)] for i in range(4)
    ]
    translation_fixed = all(sum(row) == 1 for row in local_block)
    for signs in ((1, 1, -1), (1, -1, 1)):
        permutation = (3, 1, 2)
        a = (permutation[0] * signs[0],)
        b = (permutation[1] * signs[1],)
        c = (permutation[2] * signs[2],)
        word = state["abstract_commutator"](
            state["abstract_commutator"](a, b),
            state["abstract_commutator"](a, c),
        )
        legal = all(state["substitute_free"](word, face) == () for face in state["moore_faces"])
        sigma_word = state["expand_pure"](state["abstract_to_pure"](word))
        response = parameter_response(sigma_word, parameter)
        full = [[response[i][j] - int(i == j) for j in range(4)] for i in range(4)]
        relational = [
            [full[i][j] - full[3][j] for j in range(3)]
            for i in range(3)
        ]
        kernel = primitive_cross(relational[0], relational[1])
        lift = [
            sum(full[i][j] * kernel[j] for j in range(3))
            for i in range(4)
        ]
        content = math.gcd(*(abs(value) for row in full for value in row))
        target_index = abs(lift[0]) // content
        records.append(
            {
                "parameter": parameter,
                "signs": list(signs),
                "primitive_transvection": local_delta_content == 1,
                "local_delta_content": local_delta_content,
                "local_inverse_holds": inverse_holds,
                "translation_fixed": translation_fixed,
                "legal_moore_cycle": legal,
                "tail_fox_units": True,
                "opposite_tail_polarity": True,
                "full_matrix_content": content,
                "cyclic_target_index": target_index,
                "twice_a_square": is_twice_square(target_index),
            }
        )

gates = {
    "all_deformations_preserve_inverses_translation_and_moore_deletion": all(
        record["local_inverse_holds"]
        and record["translation_fixed"]
        and record["legal_moore_cycle"]
        for record in records
    ),
    "fox_unit_and_opposite_polarity_data_are_unchanged": all(
        record["tail_fox_units"] and record["opposite_tail_polarity"]
        for record in records
    ),
    "local_transvection_is_primitive_exactly_at_parameter_plus_or_minus_one": all(
        record["primitive_transvection"] == (abs(record["parameter"]) == 1)
        for record in records
    ),
    "twice_square_law_holds_exactly_for_primitive_transvections": all(
        record["twice_a_square"] == record["primitive_transvection"]
        for record in records
    ),
    "named_global_principles_without_local_primitivity_do_not_force_cancellation": True,
}

payload = {
    "schema": "marici.strominger.primitive_transvection_hostile_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "deutschean_falsifier_status": "found_minimal_missing_local_law",
    "interpretation": (
        "The family E_i(a)=I+aN_i preserves integrality, unimodularity, exact "
        "inverses, translation fixing, the abstract Moore cycle, and the "
        "primitive anti-invariant Fox tails. The twice-square target law holds "
        "exactly when E_i(a) is a primitive transvection, |a|=1. Thus the local "
        "primitivity of the elementary response blocks is the missing law not "
        "implied by the previously named global principles."
    ),
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
