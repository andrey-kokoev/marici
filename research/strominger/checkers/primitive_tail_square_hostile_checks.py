#!/usr/bin/env python3
"""Test whether the C square persists under legal repeated tail powers."""

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
RESULT = ROOT / "research/strominger/results/primitive_tail_square_hostile_checks.json"


def power_word(generator, exponent):
    letter = generator if exponent > 0 else -generator
    return (letter,) * abs(exponent)


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


with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))

records = []
for left_power, right_power in itertools.product((-2, -1, 1, 2), repeat=2):
    word = state["abstract_commutator"](
        state["abstract_commutator"]((3,), power_word(1, left_power)),
        state["abstract_commutator"]((3,), power_word(2, right_power)),
    )
    legal = all(state["substitute_free"](word, face) == () for face in state["moore_faces"])
    response = state["reflection_response_matrix"](
        state["expand_pure"](state["abstract_to_pure"](word))
    )
    full = [[response[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    relational = [
        [response[i][j] - response[3][j] - int(i == j) for j in range(3)]
        for i in range(3)
    ]
    kernel = primitive_cross(relational[0], relational[1])
    lift = [
        sum(full[i][j] * kernel[j] for j in range(3))
        for i in range(4)
    ]
    content = math.gcd(*(abs(entry) for row in full for entry in row))
    target_index = abs(lift[0]) // content
    records.append(
        {
            "left_power": left_power,
            "right_power": right_power,
            "legal_moore_cycle": legal,
            "primitive_unit_tails": abs(left_power) == abs(right_power) == 1,
            "opposite_polarity": left_power * right_power < 0,
            "full_matrix_content": content,
            "cyclic_target_index": target_index,
            "twice_a_square": is_twice_square(target_index),
        }
    )

by_powers = {(record["left_power"], record["right_power"]): record for record in records}
gates = {
    "all_sixteen_power_words_remain_legal_moore_cycles": all(
        record["legal_moore_cycle"] for record in records
    ),
    "primitive_opposite_tail_indices_are_twice_squares": (
        by_powers[(1, -1)]["cyclic_target_index"] == 1568
        and by_powers[(-1, 1)]["cyclic_target_index"] == 2592
        and by_powers[(1, -1)]["twice_a_square"]
        and by_powers[(-1, 1)]["twice_a_square"]
    ),
    "nonprimitive_opposite_tail_power_two_breaks_twice_square_law": (
        by_powers[(2, -2)]["cyclic_target_index"] == 363
        and by_powers[(-2, 2)]["cyclic_target_index"] == 15987
        and not by_powers[(2, -2)]["twice_a_square"]
        and not by_powers[(-2, 2)]["twice_a_square"]
    ),
    "legal_mixed_power_extensions_also_break_the_square_law": any(
        record["legal_moore_cycle"] and not record["twice_a_square"]
        for record in records
        if abs(record["left_power"]) != abs(record["right_power"])
    ),
    "matrix_content_is_not_stable_beyond_primitive_tails": any(
        record["full_matrix_content"] != 768 for record in records
        if not record["primitive_unit_tails"]
    ),
}

payload = {
    "schema": "marici.strominger.primitive_tail_square_hostile_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "ramification_conjecture_status": "refuted",
    "interpretation": (
        "Repeated tail powers preserve the Moore deletion condition but destroy "
        "the twice-square cyclic target law. The square is therefore not a "
        "universal second-order intersection multiplicity of the Moore-cycle "
        "family. It is specific to the primitive unit-tail C stratum, whose "
        "atomicity must enter any explanation."
    ),
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}

RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
