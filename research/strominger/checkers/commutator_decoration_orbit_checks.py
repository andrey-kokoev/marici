#!/usr/bin/env python3
"""Constructor orbit for repeated neutral commutator decoration."""

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


def elementary(index, parameter=1):
    matrix = [[int(i == j) for j in range(4)] for i in range(4)]
    matrix[index][index] = 1 + parameter
    matrix[index][index + 1] = -parameter
    matrix[index + 1][index] = parameter
    matrix[index + 1][index + 1] = 1 - parameter
    return matrix


def response(sigma_word):
    total = [[int(i == j) for j in range(4)] for i in range(4)]
    for letter in sigma_word:
        total = multiply(elementary(abs(letter) - 1, 1 if letter > 0 else -1), total)
    return total


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def d2(matrix):
    values = []
    for rows in itertools.combinations(range(3), 2):
        for columns in itertools.combinations(range(3), 2):
            values.append(det2([[matrix[i][j] for j in columns] for i in rows]))
    return math.gcd(*(abs(x) for x in values))


def d3(matrix):
    values = [det3([[matrix[i][j] for j in range(3)] for i in rows]) for rows in itertools.combinations(range(4), 3)]
    return math.gcd(*(abs(x) for x in values))


def inverse(word):
    return tuple(-letter for letter in reversed(word))


def word_power(word, exponent):
    atom = word if exponent >= 0 else inverse(word)
    return atom * abs(exponent)


commutator = state["abstract_commutator"]((1,), (2,))
commutator_response = response(
    state["expand_pure"](state["abstract_to_pure"](commutator))
)


def modular_order(matrix, modulus, bound=100):
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    power = identity
    reduced = [[value % modulus for value in row] for row in matrix]
    for exponent in range(1, bound + 1):
        power = [[value % modulus for value in row] for row in multiply(power, reduced)]
        if power == identity:
            return exponent
    return None


commutator_order_mod_3 = modular_order(commutator_response, 3)
commutator_order_mod_9 = modular_order(commutator_response, 9)
records = []
for exponent in range(-3, 4):
    tail = (1,) + word_power(commutator, exponent)
    abstract = state["abstract_commutator"](
        state["abstract_commutator"]((3,), tail),
        state["abstract_commutator"]((3,), (-2,)),
    )
    pure = state["abstract_to_pure"](abstract)
    sigma = state["expand_pure"](pure)
    matrix = response(sigma)
    full = [[matrix[i][j] - int(i == j) for j in range(3)] for i in range(4)]
    relational = [[full[i][j] - full[3][j] for j in range(3)] for i in range(3)]
    divisor_1 = math.gcd(*(abs(x) for row in full for x in row))
    divisor_2 = d2(relational)
    divisor_3 = d3(full)
    index = divisor_3 // (divisor_2 * divisor_1)
    records.append({
        "decoration_exponent": exponent,
        "tail_charge": [1, 0, 0],
        "sigma_word_length": len(sigma),
        "relational_determinant": det3(relational),
        "d1": divisor_1,
        "d2": divisor_2,
        "d3": divisor_3,
        "snake_index": index,
    })


def is_square(value):
    root = math.isqrt(value)
    return root * root == value


equal_mod_9_jet_pairs = [
    {
        "left_exponent": left["decoration_exponent"],
        "right_exponent": right["decoration_exponent"],
        "same_response_jet_mod_9": True,
        "same_snake_square_class": is_square(left["snake_index"] * right["snake_index"]),
    }
    for left, right in itertools.combinations(records, 2)
    if (left["decoration_exponent"] - right["decoration_exponent"]) % 3 == 0
]

ratios_constant = all(
    records[i + 1]["snake_index"] * records[i - 1]["snake_index"] == records[i]["snake_index"] ** 2
    for i in range(1, len(records) - 1)
)
gates = {
    "all_orbit_points_have_same_abelian_charge": all(r["tail_charge"] == [1, 0, 0] for r in records),
    "snake_rank_defect_persists_across_orbit": all(r["relational_determinant"] == 0 for r in records),
    "charge_neutral_decoration_changes_matrix_content": len({r["d1"] for r in records}) > 1,
    "observed_content_obeys_modulus_three_rule": all(
        r["d1"] == (2304 if r["decoration_exponent"] % 3 == 2 else 768)
        for r in records
    ),
    "commutator_is_identity_mod_3_but_has_order_3_mod_9": (
        commutator_order_mod_3 == 1 and commutator_order_mod_9 == 3
    ),
    "smith_indices_are_pairwise_distinct": len({r["snake_index"] for r in records}) == len(records),
    "simple_multiplicative_character_law_is_falsified": not ratios_constant,
    "mod_9_jet_does_not_determine_snake_square_class": all(
        not pair["same_snake_square_class"] for pair in equal_mod_9_jet_pairs
    ),
}
payload = {
    "schema": "marici.strominger.commutator_decoration_orbit_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "neutral_decoration_preserves_snake_existence_but_changes_every_smith_layer",
    "commutator_response_order_mod_3": commutator_order_mod_3,
    "commutator_response_order_mod_9": commutator_order_mod_9,
    "records": records,
    "equal_mod_9_jet_pairs": equal_mod_9_jet_pairs,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "Repeated attachment of one charge-neutral commutator preserves the "
        "reflection rank defect, but changes matrix content with an observed "
        "modulus-three law and produces distinct Smith indices that do not follow "
        "a constant multiplicative character. The local constructor acts before "
        "every determinantal gcd reduction; its observable arithmetic is nonlinear."
    ),
}
print(json.dumps(payload, indent=2))
