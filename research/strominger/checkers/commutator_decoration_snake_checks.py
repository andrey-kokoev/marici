#!/usr/bin/env python3
"""Insert charge-neutral commutator decorations into the magnetic C source."""

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
with contextlib.redirect_stdout(io.StringIO()):
    state = runpy.run_path(str(SOURCE))


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


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
        total = multiply(elementary(abs(letter) - 1, parameter if letter > 0 else -parameter), total)
    return total


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def determinantal_divisor_2(matrix):
    minors = []
    for rows in itertools.combinations(range(len(matrix)), 2):
        for columns in itertools.combinations(range(len(matrix[0])), 2):
            minors.append(det2([[matrix[i][j] for j in columns] for i in rows]))
    return math.gcd(*(abs(value) for value in minors))


def determinantal_divisor_3(matrix):
    minors = [
        det3([[matrix[i][j] for j in range(3)] for i in rows])
        for rows in itertools.combinations(range(len(matrix)), 3)
    ]
    return math.gcd(*(abs(value) for value in minors))


def cross(left, right):
    return [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]


def inverse_word(word):
    return tuple(-letter for letter in reversed(word))


def is_twice_square(value):
    if value is None or value % 2:
        return False
    root = math.isqrt(value // 2)
    return 2 * root * root == value


def abelianization(word):
    return [sum(1 if x == g else -1 if x == -g else 0 for x in word) for g in (1, 2, 3)]


comm12 = state["abstract_commutator"]((1,), (2,))
tails = {
    "baseline": (1,),
    "right_commutator_decorated": (1,) + comm12,
    "left_commutator_decorated": comm12 + (1,),
    "commutator_conjugate": comm12 + (1,) + inverse_word(comm12),
}
records = []
for name, left_tail in tails.items():
    for parameter in (-1, 1):
        abstract = state["abstract_commutator"](
            state["abstract_commutator"]((3,), left_tail),
            state["abstract_commutator"]((3,), (-2,)),
        )
        pure = state["abstract_to_pure"](abstract)
        sigma = state["expand_pure"](pure)
        matrix = response(sigma, parameter)
        full = [[matrix[i][j] - int(i == j) for j in range(4)] for i in range(4)]
        relational = [[full[i][j] - full[3][j] for j in range(3)] for i in range(3)]
        determinant = det3(relational)
        candidate = cross(relational[0], relational[1])
        divisor = math.gcd(*(abs(x) for x in candidate))
        kernel = [x // divisor for x in candidate] if divisor else None
        annihilated = kernel is not None and all(sum(row[j] * kernel[j] for j in range(3)) == 0 for row in relational)
        lift = [sum(full[i][j] * kernel[j] for j in range(3)) for i in range(4)] if annihilated else None
        content = math.gcd(*(abs(value) for row in full for value in row))
        divisor_2 = determinantal_divisor_2(relational)
        divisor_3 = determinantal_divisor_3([row[:3] for row in full])
        smith_snake_index = divisor_3 // (divisor_2 * content)
        target_index = abs(lift[0]) // content if lift and len(set(lift)) == 1 else None
        records.append({
            "tail": name,
            "parameter": parameter,
            "tail_charge": abelianization(left_tail),
            "pure_word_length": len(pure),
            "sigma_word_length": len(sigma),
            "relational_determinant": determinant,
            "relational_kernel": kernel if annihilated else None,
            "lift": lift,
            "full_content": content,
            "relational_determinantal_divisor_2": divisor_2,
            "full_determinantal_divisor_3": divisor_3,
            "smith_snake_index": smith_snake_index,
            "cyclic_target_index": target_index,
            "twice_square": is_twice_square(target_index),
        })

baseline = [r for r in records if r["tail"] == "baseline"]
decorated = [r for r in records if r["tail"] != "baseline"]
gates = {
    "all_tail_charges_are_identical": all(r["tail_charge"] == [1, 0, 0] for r in records),
    "baseline_has_relational_kernel": all(r["relational_kernel"] is not None for r in baseline),
    "decorations_change_the_source_presentation": len({(r["pure_word_length"], r["sigma_word_length"]) for r in records}) > 1,
    "at_least_one_charge_neutral_decoration_changes_the_snake_readout": any(
        r["relational_kernel"] != baseline[0 if r["parameter"] == -1 else 1]["relational_kernel"]
        or r["cyclic_target_index"] != baseline[0 if r["parameter"] == -1 else 1]["cyclic_target_index"]
        for r in decorated
    ),
    "baseline_is_twice_square": all(r["twice_square"] for r in baseline),
    "charge_neutral_decorations_leave_twice_square_stratum": all(not r["twice_square"] for r in decorated),
    "smith_determinantal_ratio_recovers_every_snake_index": all(
        r["smith_snake_index"] == r["cyclic_target_index"] for r in records
    ),
}
payload = {
    "schema": "marici.strominger.commutator_decoration_snake_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "fox_fiber_is_visible_to_the_magnetic_snake_readout",
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
