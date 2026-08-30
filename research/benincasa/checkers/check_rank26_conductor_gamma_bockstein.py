#!/usr/bin/env python3
"""Lift the rank-26 presentation to dual gamma and audit its exact-relation Bockstein."""

from __future__ import annotations

import importlib
import json
import os
from itertools import product
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
suffix = "" if P == 32009 else f"-p{P}"
SOURCE_POINT = tuple(int(os.environ.get(name, default)) for name, default in (
    ("MARICI_SOURCE_X", "2"), ("MARICI_SOURCE_Y", "3"), ("MARICI_SOURCE_Z", "4")
))
point_suffix = "" if SOURCE_POINT == (2, 3, 4) else "-at-" + "-".join(map(str, SOURCE_POINT))
OUT = ROOT / "research" / "benincasa" / "results" / f"rank26-conductor-gamma-bockstein{suffix}{point_suffix}.json"
os.environ["MARICI_FIELD_PRIME"] = str(P)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")

Dual = tuple[int, int]


def dadd(x: Dual, y: Dual) -> Dual:
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def dmul(x: Dual, y: Dual) -> Dual:
    return (x[0] * y[0] % P, (x[0] * y[1] + x[1] * y[0]) % P)


def dinv(x: Dual) -> Dual:
    q = pow(x[0], -1, P)
    return q, -x[1] * q * q % P


def add(row: dict[int, Dual], column: int, value: Dual) -> None:
    value = dadd(row.get(column, (0, 0)), value)
    if value != (0, 0):
        row[column] = value
    else:
        row.pop(column, None)


def scale(x: Dual, n: int) -> Dual:
    return x[0] * n % P, x[1] * n % P


def add_pivot(row: dict[int, Dual], pivots: dict[int, dict[int, Dual]]) -> None:
    while any(value[0] for value in row.values()):
        pivot = max(column for column, value in row.items() if value[0])
        coefficient = row[pivot]
        if pivot not in pivots:
            inverse = dinv(coefficient)
            pivots[pivot] = {column: dmul(value, inverse) for column, value in row.items()}
            return
        existing = pivots[pivot]
        for column, value in existing.items():
            add(row, column, scale(dmul(coefficient, value), -1))


def reduce(row: dict[int, Dual], pivots: dict[int, dict[int, Dual]]) -> dict[int, Dual]:
    row = dict(row)
    while any(value[0] for value in row.values()):
        pivot = max(column for column, value in row.items() if value[0])
        if pivot not in pivots:
            break
        coefficient = row[pivot]
        for column, value in pivots[pivot].items():
            add(row, column, scale(dmul(coefficient, value), -1))
    return row


def presentation_dual(names: tuple[str, ...], gamma: int, ambient: int, cutoff: int):
    k, all_q = base.fiber_data(*SOURCE_POINT)
    qs = [all_q[name] for name in names]
    q_count = len(names)
    low_monomials = base.monomials_at_most(cutoff)
    low_labels = [(0, *levels, m) for levels in product(range(1, 2), repeat=q_count) for m in low_monomials]
    low_set = set(low_labels)
    ordered = list(low_labels)
    for kp in range(3):
        for levels in product(range(1, 3), repeat=q_count):
            ordered.extend(label for m in base.monomials_at_most(ambient + 4)
                           if (label := (kp, *levels, m)) not in low_set)
    columns = {label: i for i, label in enumerate(ordered)}
    pivots: dict[int, dict[int, Dual]] = {}
    kd = [base.derivative(k, axis) for axis in range(2)]
    qd = [[base.derivative(q, axis) for axis in range(2)] for q in qs]

    for kp in range(2):
        for levels in product(range(1, 3), repeat=q_count):
            if any(level == 2 for level in levels):
                continue
            for axis in range(2):
                for exponent in base.monomials_at_most(ambient):
                    row: dict[int, Dual] = {}
                    if exponent[axis]:
                        derived = list(exponent); derived[axis] -= 1
                        add(row, columns[(kp, *levels, tuple(derived))], (exponent[axis] % P, 0))
                    for term, coefficient in kd[axis].items():
                        add(row, columns[(kp + 1, *levels, base.shifted(exponent, term))],
                            ((gamma - kp) * coefficient % P, coefficient % P))
                    for qi, pole in enumerate(levels):
                        raised = list(levels); raised[qi] += 1
                        for term, coefficient in qd[qi][axis].items():
                            add(row, columns[(kp, *raised, base.shifted(exponent, term))],
                                (-pole * coefficient % P, 0))
                    add_pivot(row, pivots)

    for kp in range(2):
        for levels in product(range(1, 3), repeat=q_count):
            for exponent in base.monomials_at_most(ambient - 4):
                row = {columns[(kp, *levels, exponent)]: (1, 0)}
                for term, coefficient in base.multiply_monomial(k, exponent, -1):
                    add(row, columns[(kp + 1, *levels, term)], (coefficient, 0))
                add_pivot(row, pivots)

    for qi, q in enumerate(qs):
        for kp in range(3):
            for levels in product(range(1, 3), repeat=q_count):
                if levels[qi] == 2:
                    continue
                raised = list(levels); raised[qi] += 1
                for exponent in base.monomials_at_most(ambient - 1):
                    row = {columns[(kp, *levels, exponent)]: (1, 0)}
                    for term, coefficient in base.multiply_monomial(q, exponent, -1):
                        add(row, columns[(kp, *raised, term)], (coefficient, 0))
                    add_pivot(row, pivots)
    low_pivots = {pivot: row for pivot, row in pivots.items() if pivot < len(low_labels)}
    free = [i for i in range(len(low_labels)) if i not in low_pivots]
    return low_labels, columns, pivots, free


def rank(vectors: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for source in vectors:
        row = dict(source)
        base.add_pivot(row, pivots)
    return len(pivots)


names = ("g1", "g2", "g3", "g23", "g31")
gamma = -pow(2, -1, P) % P
labels, columns, pivots, free = presentation_dual(names, gamma, 14, 7)
monomials = [(i, j) for i in range(7) for j in range(7 - i)]

# Find the two exact relations using value parts of the dual normal forms.
qcols = []
dual_normals = []
for exponent in monomials:
    normal = reduce({columns[(0, 1, 1, 1, 1, 1, exponent)]: (1, 0)}, pivots)
    dual_normals.append(normal)
    qcols.append({c: normal[c][0] for c in free if c in normal and normal[c][0]})
column_pivots: dict[int, tuple[dict[int, int], dict[int, int]]] = {}
relations = []
for j, source_column in enumerate(qcols):
    column = dict(source_column)
    combination = {j: 1}
    while column:
        pivot = max(column)
        coefficient = column[pivot]
        if pivot not in column_pivots:
            inverse = pow(coefficient, -1, P)
            column_pivots[pivot] = (
                {c: value * inverse % P for c, value in column.items()},
                {c: value * inverse % P for c, value in combination.items()},
            )
            break
        existing_column, existing_combination = column_pivots[pivot]
        for c, value in existing_column.items():
            value = (column.get(c, 0) - coefficient * value) % P
            if value: column[c] = value
            else: column.pop(c, None)
        for c, value in existing_combination.items():
            value = (combination.get(c, 0) - coefficient * value) % P
            if value: combination[c] = value
            else: combination.pop(c, None)
    else:
        relations.append(combination)

# Differentiate reduction at fixed polynomial representatives.
bocksteins = []
for relation in relations:
    normal: dict[int, Dual] = {}
    for j, coefficient in relation.items():
        for c, value in dual_normals[j].items():
            add(normal, c, scale(value, coefficient))
    assert all(normal.get(c, (0, 0))[0] == 0 for c in free)
    bocksteins.append({c: normal[c][1] for c in free if c in normal and normal[c][1]})

# Reuse the collision remainder to identify which relation is root-visible.
x, y, z = SOURCE_POINT
b0 = y + z
C1 = x*x*y+x*x*z+x*y*y+2*x*y*z+2*x*z*z-y**3-y*y*z+y*z*z+z**3
D = C1 * pow(x, -1, P) % P
remainders = []
remainders_g2 = []
C2 = x**3-x*x*y+x*x*z-x*y*y-2*x*y*z-x*z*z-y*y*z-2*y*z*z-z**3
D2 = -C2 * pow(y, -1, P) % P
a0 = x + z
for relation in relations:
    even = odd = 0
    for j, coefficient in relation.items():
        i, degree_b = monomials[j]
        scalar = coefficient * pow(b0, degree_b, P) % P
        if i % 2:
            odd = (odd + scalar * pow(D, (i - 1)//2, P)) % P
        else:
            even = (even + scalar * pow(D, i//2, P)) % P
    remainders.append((even, odd))
    even2 = odd2 = 0
    for j, coefficient in relation.items():
        degree_a, degree_b = monomials[j]
        scalar = coefficient * pow(a0, degree_a, P) % P
        if degree_b % 2:
            odd2 = (odd2 + scalar * pow(D2, (degree_b - 1)//2, P)) % P
        else:
            even2 = (even2 + scalar * pow(D2, degree_b//2, P)) % P
    remainders_g2.append((even2, odd2))

visible = next(i for i, r in enumerate(remainders) if r != (0, 0))
invisible = 1 - visible
checks = {
    "relation_space_dimension_two": len(relations) == 2,
    "bockstein_image_rank_one": rank(bocksteins) == 1,
    "root_visible_relation_has_nonzero_bockstein": bool(bocksteins[visible]),
    "root_invisible_relation_has_zero_bockstein": not bocksteins[invisible],
    "second_conductor_selects_same_relation": remainders_g2[invisible] == (0, 0) and remainders_g2[visible] != (0, 0),
    "bare_second_conductor_reuse_is_not_pure_odd": remainders_g2[visible][0] != 0 and remainders_g2[visible][1] != 0,
}
payload = {
    "schema": "marici.rank26-conductor-gamma-bockstein.v1",
    "prime": P,
    "source_point": list(SOURCE_POINT),
    "gamma_mod_prime": gamma,
    "relation_space_dimension": len(relations),
    "bockstein_image_rank": rank(bocksteins),
    "root_visible_relation_index": visible,
    "root_visible_remainder": list(remainders[visible]),
    "second_conductor_root_visible_remainder": list(remainders_g2[visible]),
    "bockstein_support_sizes": [len(v) for v in bocksteins],
    "root_visible_bockstein_vector": {str(c): value for c, value in sorted(bocksteins[visible].items())},
    "relation_vectors": [{str(c):value for c,value in sorted(vector.items())} for vector in relations],
    "bockstein_vectors": [{str(c):value for c,value in sorted(vector.items())} for vector in bocksteins],
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The gamma-normal derivative maps the two-dimensional exact-relation space onto one canonical line: precisely the first-conductor root-visible odd defect relation maps nontrivially, while the root-invisible relation maps to zero. Bare reuse on the second conductor selects the same relation but gives mixed parity, so occurrence covariance requires the labelled chart transition.",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"] and os.environ.get("MARICI_ALLOW_FAILED_PACKET") != "1":
    raise SystemExit(1)
