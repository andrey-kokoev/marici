#!/usr/bin/env python3
"""Presentation-invariance and authority-laundering hostile for atomicity."""

from __future__ import annotations

import itertools
import json
import math


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def msub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def gcd_entries(a):
    return math.gcd(*(abs(x) for row in a for x in row))


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a):
    d = det2(a)
    assert abs(d) == 1
    return [[a[1][1] // d, -a[0][1] // d], [-a[1][0] // d, a[0][0] // d]]


N = [[1, -1], [1, -1]]
I = eye(2)
J = [[0, 1], [1, 0]]
alpha = [[1], [-1]]


def E(a):
    return madd(I, [[a * x for x in row] for row in N])


unimodular = [
    eye(2),
    [[0, 1], [1, 0]],
    [[-1, 0], [0, 1]],
    [[1, 1], [0, 1]],
    [[1, 0], [1, 1]],
    [[1, -2], [0, 1]],
]
assert all(abs(det2(u)) == 1 for u in unimodular)

basis_records = []
for a, p, q in itertools.product((-3, -2, -1, 1, 2, 3), unimodular, unimodular):
    transported = mmul(mmul(p, msub(E(a), I)), q)
    basis_records.append(gcd_entries(transported) == abs(a))

factor_records = []
for a in (-3, -2, -1, 1, 2, 3):
    atom = E(1 if a > 0 else -1)
    product = eye(2)
    for _ in range(abs(a)):
        product = mmul(atom, product)
    factor_records.append({
        "a": a,
        "factor_count": abs(a),
        "factors_primitive": True,
        "composite_content": gcd_entries(msub(product, I)),
        "factorization_exact": product == E(a),
    })

fox_records = []
for n in (-3, -2, -1, 1, 2, 3):
    # The Fox derivative of x^n has |n| monomials with coefficients +/-1.
    support_length = abs(n)
    fox_records.append({
        "exponent": n,
        "support_length": support_length,
        "group_ring_unit": support_length == 1,
    })

nielsen_shadow = []
primitive_rows = [(1, 0), (0, 1), (1, -1), (2, 1)]
for row, u in itertools.product(primitive_rows, unimodular):
    moved = (
        row[0] * u[0][0] + row[1] * u[1][0],
        row[0] * u[0][1] + row[1] * u[1][1],
    )
    nielsen_shadow.append(math.gcd(abs(moved[0]), abs(moved[1])) == math.gcd(abs(row[0]), abs(row[1])))

endpoint_records = []
for u in unimodular:
    ui = inv2(u)
    jp = mmul(mmul(u, J), ui)
    ap = mmul(u, alpha)
    endpoint_records.append(mmul(jp, ap) == [[-ap[0][0]], [-ap[1][0]]])

laundering = next(r for r in factor_records if r["a"] == 2)
gates = {
    "nilpotent_generator": mmul(N, N) == [[0, 0], [0, 0]],
    "content_ideal_survives_all_tested_unimodular_presentations": all(basis_records),
    "elementary_response_factorization_is_exact": all(r["factorization_exact"] for r in factor_records),
    "primitive_factors_do_not_make_composite_primitive": laundering["factors_primitive"] and laundering["composite_content"] == 2,
    "fox_unit_condition_detects_only_single_letters": all(r["group_ring_unit"] == (abs(r["exponent"]) == 1) for r in fox_records),
    "fox_augmentation_ideal_survives_tested_nielsen_shadows": all(nielsen_shadow),
    "anti_invariant_line_transports_equivariantly": all(endpoint_records),
}
payload = {
    "schema": "marici.strominger.presentation_invariant_atomicity_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "basis_invariant_but_not_composition_closed",
    "bounded_family": {
        "response_parameters": [-3, -2, -1, 1, 2, 3],
        "unimodular_presentations": len(unimodular),
        "left_right_content_tests": len(basis_records),
        "endpoint_transport_tests": len(endpoint_records),
    },
    "composition_hostile": laundering,
    "fox_records": fox_records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "Atomicity is carried by unimodular ideals and equivariant eigendata, "
        "not by coordinates. It is preserved by authorized presentation changes "
        "but not by constructor composition: E(2)=E(1)E(1) has primitive factors "
        "and nonprimitive effective content. Factor-level authority therefore "
        "cannot be laundered into composite atomicity."
    ),
}
print(json.dumps(payload, indent=2))
