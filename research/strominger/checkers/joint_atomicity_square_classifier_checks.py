#!/usr/bin/env python3
"""Joint hostile for word and response atomicity in the C square law."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/eta_squared_faithful_artin_action_checks.py"
RESULT = ROOT / "research/strominger/results/joint_atomicity_square_classifier_checks.json"

with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))


def power_word(generator, exponent):
    return ((generator if exponent > 0 else -generator),) * abs(exponent)


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


def response(sigma_word, parameter):
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
for parameter, left_power, right_power in itertools.product((-2, -1, 1, 2), repeat=3):
    word = state["abstract_commutator"](
        state["abstract_commutator"]((3,), power_word(1, left_power)),
        state["abstract_commutator"]((3,), power_word(2, right_power)),
    )
    sigma_word = state["expand_pure"](state["abstract_to_pure"](word))
    matrix = response(sigma_word, parameter)
    full = [[matrix[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    relational = [[full[i][j] - full[3][j] for j in range(3)] for i in range(3)]
    kernel = primitive_cross(relational[0], relational[1])
    lift = [sum(full[i][j] * kernel[j] for j in range(3)) for i in range(4)]
    content = math.gcd(*(abs(value) for row in full for value in row))
    target_index = abs(lift[0]) // content
    primitive_transvection = abs(parameter) == 1
    fox_unit_tails = abs(left_power) == abs(right_power) == 1
    anti_invariant = left_power * right_power < 0
    predicted = primitive_transvection and fox_unit_tails and anti_invariant
    observed = is_twice_square(target_index)
    records.append(
        {
            "parameter": parameter,
            "left_power": left_power,
            "right_power": right_power,
            "primitive_transvection": primitive_transvection,
            "fox_unit_tails": fox_unit_tails,
            "anti_invariant": anti_invariant,
            "predicted_twice_square": predicted,
            "observed_twice_square": observed,
            "cyclic_target_index": target_index,
        }
    )

matches = [record for record in records if record["predicted_twice_square"] == record["observed_twice_square"]]
false_positives = [record for record in records if record["observed_twice_square"] and not record["predicted_twice_square"]]
false_negatives = [record for record in records if record["predicted_twice_square"] and not record["observed_twice_square"]]
gates = {
    "all_sixty_four_joint_deformations_are_covered": len(records) == 64,
    "joint_atomicity_classifier_has_no_false_positive": not false_positives,
    "joint_atomicity_classifier_has_no_false_negative": not false_negatives,
    "all_cases_match_the_conjunction": len(matches) == len(records),
}

payload = {
    "schema": "marici.strominger.joint_atomicity_square_classifier_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classifier_status": "exact_on_joint_bounded_family" if len(matches) == len(records) else "falsified",
    "interpretation": (
        "In the 64-case joint deformation family, the twice-square cyclic target "
        "law holds exactly on the intersection of primitive elementary "
        "transvections, unit Fox tail derivatives, and anti-invariant tail "
        "polarity. No interaction between nonprimitive word and response data "
        "accidentally restores the law."
    ),
    "match_count": len(matches),
    "false_positives": false_positives,
    "false_negatives": false_negatives,
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in payload.items() if key != "records"}, indent=2))
