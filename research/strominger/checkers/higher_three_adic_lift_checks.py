#!/usr/bin/env python3
"""Hostile test of higher 3-adic lifting and Smith-valuation cancellation."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

multiply = source["multiply"]
C, Ci = source["C"], source["Ci"]
X, Xi = source["X"], source["Xi"]
Z, Zi = source["Z"], source["Zi"]
right_block, right_block_i = source["right_block"], source["right_block_i"]
anti_commutator = source["anti_commutator"]
I4 = [[int(i == j) for j in range(4)] for i in range(4)]


def fast_power(matrix, inverse, exponent):
    atom = matrix if exponent >= 0 else inverse
    e = abs(exponent)
    total = I4
    while e:
        if e & 1:
            total = multiply(atom, total)
        atom = multiply(atom, atom)
        e >>= 1
    return total


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def d2(matrix):
    values = []
    for rows in itertools.combinations(range(3), 2):
        for columns in itertools.combinations(range(3), 2):
            values.append(det2([[matrix[i][j] for j in columns] for i in rows]))
    return math.gcd(*(abs(v) for v in values))


def d3(matrix):
    values = [
        det3([[matrix[i][j] for j in range(3)] for i in rows])
        for rows in itertools.combinations(range(4), 3)
    ]
    return math.gcd(*(abs(v) for v in values))


def valuation(value, prime=3):
    if value == 0:
        return None
    value = abs(value)
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


cache = {}


def packet(exponent):
    if exponent in cache:
        return cache[exponent]
    U = fast_power(C, Ci, exponent)
    V = fast_power(Ci, C, exponent)
    tail = multiply(U, X)
    tail_i = multiply(Xi, V)
    left = anti_commutator(Z, Zi, tail, tail_i)
    left_i = anti_commutator(tail, tail_i, Z, Zi)
    A = anti_commutator(left, left_i, right_block, right_block_i)
    full = [[A[i][j] - int(i == j) for j in range(3)] for i in range(4)]
    relational = [[full[i][j] - full[3][j] for j in range(3)] for i in range(3)]
    divisor_1 = math.gcd(*(abs(v) for row in full for v in row))
    divisor_2 = d2(relational)
    divisor_3 = d3(full)
    index = divisor_3 // (divisor_2 * divisor_1)
    result = {
        "exponent": exponent,
        "v3_d1": valuation(divisor_1),
        "v3_d2": valuation(divisor_2),
        "v3_d3": valuation(divisor_3),
        "v3_snake_index": valuation(index),
        "rank_defect": det3(relational) == 0,
    }
    cache[exponent] = result
    return result


levels = []
residue = 2
modulus = 3
target_valuation = 3
for level in range(2, 7):
    candidates = [residue + digit * modulus for digit in range(3)]
    records = [packet(n) for n in candidates]
    deeper = [r["exponent"] for r in records if r["v3_d1"] >= target_valuation]
    levels.append({
        "level": level,
        "input_residue": residue,
        "input_modulus": modulus,
        "candidate_modulus": modulus * 3,
        "target_v3_d1": target_valuation,
        "records": records,
        "deeper_lifts": deeper,
        "unique_deeper_lift": len(deeper) == 1,
    })
    if len(deeper) != 1:
        break
    residue = deeper[0]
    modulus *= 3
    target_valuation += 1

all_records = [record for level in levels for record in level["records"]]
predictions = {
    "unique_content_hensel_lift":
        bool(levels) and len(levels[0]["deeper_lifts"]) == 1,
    "persistent_smith_three_adic_cancellation":
        all(r["v3_snake_index"] == 0 for r in all_records),
}
gates = {
    "all_three_first_lifts_were_evaluated":
        bool(levels) and len(levels[0]["records"]) == 3,
    "content_hensel_lift_prediction_is_falsified":
        bool(levels) and levels[0]["deeper_lifts"] == [],
    "persistent_cancellation_prediction_is_falsified":
        any(r["v3_snake_index"] != 0 for r in all_records),
    "first_cancellation_failure_within_the_lift_fiber_is_n8":
        [r["exponent"] for r in all_records if r["v3_snake_index"] != 0] == [8],
    "first_jet_content_selection_remains_valid":
        all(r["v3_d1"] == 2 for r in all_records),
    "rank_defect_persists_on_every_candidate":
        all(r["rank_defect"] for r in all_records),
}

payload = {
    "schema": "marici.strominger.higher_three_adic_lift_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "content_tower_terminates_and_smith_cancellation_breaks_at_n8",
    "predictions": predictions,
    "levels": levels,
    "final_residue": residue,
    "final_modulus": modulus,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The first exceptional content fiber has no deeper content lift: all "
        "three representatives retain v3(d1)=2. Higher minors nevertheless split "
        "the fiber, and n=8 is the first tested lift where one factor of 3 survives "
        "the Smith ratio. Both bold higher-order predictions are falsified."
    ),
}
print(json.dumps(payload, indent=2))
