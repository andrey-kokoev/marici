#!/usr/bin/env python3
"""Locate the exact arrow converting the source 3-adic jet into a content jump."""

from __future__ import annotations

import contextlib
import io
import json
import math
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/commutator_decoration_orbit_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

state = source["state"]
commutator = source["commutator"]
C = source["commutator_response"]
response = source["response"]
word_power = source["word_power"]
d2 = source["d2"]
d3 = source["d3"]
det3 = source["det3"]
I4 = [[int(i == j) for j in range(4)] for i in range(4)]


def mod_matrix(A, modulus):
    return [[v % modulus for v in row] for row in A]


def add_mod(A, B, modulus):
    return [[(A[i][j] + B[i][j]) % modulus for j in range(len(A[0]))] for i in range(len(A))]


def scale_mod(k, A, modulus):
    return [[(k * v) % modulus for v in row] for row in A]


def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def all_zero(A):
    return all(v == 0 for row in A for v in row)


def valuation(value, prime):
    if value == 0:
        return None
    count = 0
    value = abs(value)
    while value % prime == 0:
        value //= prime
        count += 1
    return count


source_difference = subtract(C, I4)
source_jet_integral = all(v % 3 == 0 for row in source_difference for v in row)
J = mod_matrix([[v // 3 for v in row] for row in source_difference], 3)

stage_records = []
full_packets = {}
jet_packets = {}
for exponent in [0, 1, 2]:
    tail = (1,) + word_power(commutator, exponent)
    abstract = state["abstract_commutator"](
        state["abstract_commutator"]((3,), tail),
        state["abstract_commutator"]((3,), (-2,)),
    )
    sigma = state["expand_pure"](state["abstract_to_pure"](abstract))
    matrix = response(sigma)
    full = [[matrix[i][j] - int(i == j) for j in range(3)] for i in range(4)]
    relational = [[full[i][j] - full[3][j] for j in range(3)] for i in range(3)]
    divisor_1 = math.gcd(*(abs(v) for row in full for v in row))
    divisor_2 = d2(relational)
    divisor_3 = d3(full)
    index = divisor_3 // (divisor_2 * divisor_1)
    divisible_by_3 = all(v % 3 == 0 for row in full for v in row)
    jet = mod_matrix([[v // 3 for v in row] for row in full], 3)
    full_packets[exponent] = full
    jet_packets[exponent] = jet
    stage_records.append({
        "exponent_class": exponent,
        "source_jet": scale_mod(exponent, J, 3),
        "nested_response_jet": jet,
        "nested_response_jet_is_zero": all_zero(jet),
        "v3_d1": valuation(divisor_1, 3),
        "v3_d2": valuation(divisor_2, 3),
        "v3_d3": valuation(divisor_3, 3),
        "v3_snake_index": valuation(index, 3),
        "rank_defect_persists": det3(relational) == 0,
        "full_packet_divisible_by_3": divisible_by_3,
    })

K = add_mod(jet_packets[1], scale_mod(-1, jet_packets[0], 3), 3)
affine_response_law = all(
    jet_packets[n] == add_mod(jet_packets[0], scale_mod(n, K, 3), 3)
    for n in [0, 1, 2]
)

gates = {
    "source_response_lies_in_first_congruence_subgroup":
        source_jet_integral and not all_zero(J),
    "source_jet_carries_all_three_exponent_classes":
        len({json.dumps(scale_mod(n, J, 3)) for n in [0, 1, 2]}) == 3,
    "nested_readout_is_affine_on_the_first_jet": affine_response_law,
    "nested_readout_selects_exactly_class_two_as_zero":
        [r["exponent_class"] for r in stage_records if r["nested_response_jet_is_zero"]] == [2],
    "content_jump_is_exactly_the_zero_jet_condition": all(
        (r["v3_d1"] >= 2) == r["nested_response_jet_is_zero"]
        for r in stage_records
    ),
    "rank_defect_precedes_and_survives_the_three_adic_selection":
        all(r["rank_defect_persists"] for r in stage_records),
    "smith_ratio_cancels_the_three_adic_valuation":
        all(r["v3_snake_index"] == 0 for r in stage_records),
}

payload = {
    "schema": "marici.strominger.three_adic_conversion_law_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "nested_readout_affinely_selects_one_source_jet_class_and_content_exposes_it",
    "source_law": "C=I+3J mod 9, hence C^n=I+3nJ mod 9",
    "readout_law": "B_n=B_0+nK mod 3 for B_n=(A_n-I)/3 mod 3",
    "selected_class": 2,
    "stage_records": stage_records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The source action already carries three distinct first congruence jets. "
        "The nested commutator readout maps them affinely and sends exactly class "
        "two to the zero response jet. Determinantal content does not create the "
        "selection; it exposes zero-jet divisibility as extra factors of 3. "
        "The final Smith ratio cancels those valuations and is 3-adically blind."
    ),
}
print(json.dumps(payload, indent=2))
