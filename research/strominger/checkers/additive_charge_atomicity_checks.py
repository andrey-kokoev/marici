#!/usr/bin/env python3
"""Test the additive charge law underlying non-compositional atomicity."""

from __future__ import annotations

import itertools
import json


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


I = [[1, 0], [0, 1]]
N = [[1, -1], [1, -1]]


def E(a):
    return [[I[i][j] + a * N[i][j] for j in range(2)] for i in range(2)]


def fox_power(exponent):
    # Laurent-polynomial dictionary for d(x^n)/dx.
    if exponent > 0:
        return {k: 1 for k in range(exponent)}
    if exponent < 0:
        return {k: -1 for k in range(exponent, 0)}
    return {}


def shift(poly, exponent):
    return {k + exponent: v for k, v in poly.items()}


def add(left, right):
    out = dict(left)
    for k, value in right.items():
        out[k] = out.get(k, 0) + value
        if out[k] == 0:
            del out[k]
    return out


values = range(-3, 4)
records = []
for a, b in itertools.product(values, repeat=2):
    response_exact = mmul(E(a), E(b)) == E(a + b)
    fox_chain = add(fox_power(a), shift(fox_power(b), a)) == fox_power(a + b)
    records.append({
        "left_charge": a,
        "right_charge": b,
        "effective_charge": a + b,
        "response_composition_exact": response_exact,
        "fox_cocycle_exact": fox_chain,
        "left_atomic": abs(a) == 1,
        "right_atomic": abs(b) == 1,
        "composite_atomic": abs(a + b) == 1,
    })

primitive_to_nonprimitive = [r for r in records if r["left_atomic"] and r["right_atomic"] and not r["composite_atomic"]]
nonprimitive_to_primitive = [r for r in records if not (r["left_atomic"] and r["right_atomic"]) and r["composite_atomic"]]
cancellation_to_identity = [r for r in records if r["left_atomic"] and r["right_atomic"] and r["effective_charge"] == 0]

gates = {
    "response_charge_is_additive_on_all_49_pairs": all(r["response_composition_exact"] for r in records),
    "fox_derivative_obeys_cocycle_on_all_49_pairs": all(r["fox_cocycle_exact"] for r in records),
    "atomic_factors_can_produce_nonatomic_composite": bool(primitive_to_nonprimitive),
    "nonatomic_factors_can_produce_atomic_composite": bool(nonprimitive_to_primitive),
    "opposite_atomic_charges_cancel_to_identity": bool(cancellation_to_identity),
    "atomicity_equals_unit_locus_of_effective_charge": all(r["composite_atomic"] == (abs(r["effective_charge"]) == 1) for r in records),
}

payload = {
    "schema": "marici.strominger.additive_charge_atomicity_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "atomicity_is_a_unit_stratum_of_an_additive_charge_not_a_compositional_capability",
    "bounded_family": {"charges": [-3, -2, -1, 0, 1, 2, 3], "pair_count": len(records)},
    "witnesses": {
        "atomic_to_nonatomic": primitive_to_nonprimitive[:4],
        "nonatomic_to_atomic": nonprimitive_to_primitive[:4],
        "cancellation_to_identity": cancellation_to_identity,
    },
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "Both the nilpotent response family and the one-generator Fox calculus "
        "factor through an additive integer charge. Atomicity is the inverse "
        "image of the units +/-1. Since that unit locus is not closed under "
        "addition, atomic morphisms do not form a subcategory. A compiler must "
        "carry and recompute effective charge rather than compose atomic flags."
    ),
}
print(json.dumps(payload, indent=2))
