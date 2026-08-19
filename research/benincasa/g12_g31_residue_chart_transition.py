"""Exact labelled G12 -> G31 residue-chart transition over F_32003.

This checker imports the frozen product-pole reducer, constructs the reflected
G31 chart independently from the source denominator formulas, and verifies
that the signed Poincare-residue map descends through every retained pivot.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import physical_four_mark_residue_twisted_derham as base

PRIME = base.PRIME
SOURCE_POINT = (2, 3, 4)
TARGET_POINT = (2, 4, 3)
SOURCE_NAMES = ("g1", "g2", "g3", "g23", "g31")
TARGET_NAMES = ("g1", "g3", "g2", "g23", "g12")
GAMMA = 5
AMBIENT = 10
CUTOFF = 5
K_DEPTH = 2
Q_DEPTH = 2


def clean(poly):
    return {e: c % PRIME for e, c in poly.items() if c % PRIME}


def swap_exponents(poly):
    return clean({(j, i): c for (i, j), c in poly.items()})


def g31_fiber_data(x, y, z):
    """G31 residue b=-E in retained coordinates (c,a)=(y12,y23)."""
    # The Cayley--Menger polynomial follows from the source permutation
    # sigma_23: (x,y,z;c,a,b) -> (x,z,y;b,a,c).
    source_k, _ = base.fiber_data(x, z, y)
    k = swap_exponents(source_k)
    q = {
        "g1": {(1, 0): 1, (0, 0): -y - z},
        "g3": {(0, 1): 1, (0, 0): -x - y},
        "g2": {(1, 0): 1, (0, 1): 1, (0, 0): y},
        "g23": {(1, 0): 1, (0, 0): -x},
        "g12": {(0, 1): 1, (0, 0): -z},
    }
    return k, {name: clean(poly) for name, poly in q.items()}


def presentation(fiber, point, names):
    k, all_q = fiber(*point)
    q_polynomials = [all_q[name] for name in names]
    q_count = len(names)
    k_depth, q_depth = K_DEPTH, Q_DEPTH
    column_degree = AMBIENT + 4
    low_monomials = base.monomials_at_most(CUTOFF)
    low_labels = [
        (0, *levels, monomial)
        for levels in product(range(1, 2), repeat=q_count)
        for monomial in low_monomials
    ]
    low_set = set(low_labels)
    ambient_monomials = base.monomials_at_most(column_degree)
    ordered_columns = list(low_labels)
    for k_pole in range(k_depth + 1):
        for levels in product(range(1, q_depth + 1), repeat=q_count):
            ordered_columns.extend(
                label
                for monomial in ambient_monomials
                if (label := (k_pole, *levels, monomial)) not in low_set
            )
    columns = {label: index for index, label in enumerate(ordered_columns)}
    pivots = {}
    kd = [base.derivative(k, axis) for axis in range(2)]
    qd = [[base.derivative(q, axis) for axis in range(2)] for q in q_polynomials]

    for k_pole in range(k_depth):
        for levels in product(range(1, q_depth + 1), repeat=q_count):
            if any(level == q_depth for level in levels):
                continue
            for axis in range(2):
                for exponent in base.monomials_at_most(AMBIENT):
                    row = {}
                    if exponent[axis]:
                        derived = list(exponent)
                        derived[axis] -= 1
                        base.add_value(
                            row,
                            columns[(k_pole, *levels, tuple(derived))],
                            exponent[axis],
                        )
                    for term, coefficient in kd[axis].items():
                        base.add_value(
                            row,
                            columns[(k_pole + 1, *levels, base.shifted(exponent, term))],
                            (GAMMA - k_pole) * coefficient,
                        )
                    for qi, q_pole in enumerate(levels):
                        raised = list(levels)
                        raised[qi] += 1
                        for term, coefficient in qd[qi][axis].items():
                            base.add_value(
                                row,
                                columns[(k_pole, *raised, base.shifted(exponent, term))],
                                -q_pole * coefficient,
                            )
                    base.add_pivot(row, pivots)

    for k_pole in range(k_depth):
        for levels in product(range(1, q_depth + 1), repeat=q_count):
            for exponent in base.monomials_at_most(AMBIENT - 4):
                row = {columns[(k_pole, *levels, exponent)]: 1}
                for term, coefficient in base.multiply_monomial(k, exponent, -1):
                    base.add_value(row, columns[(k_pole + 1, *levels, term)], coefficient)
                base.add_pivot(row, pivots)

    for qi, qpoly in enumerate(q_polynomials):
        for k_pole in range(k_depth + 1):
            for levels in product(range(1, q_depth + 1), repeat=q_count):
                if levels[qi] == q_depth:
                    continue
                raised = list(levels)
                raised[qi] += 1
                for exponent in base.monomials_at_most(AMBIENT - 1):
                    row = {columns[(k_pole, *levels, exponent)]: 1}
                    for term, coefficient in base.multiply_monomial(qpoly, exponent, -1):
                        base.add_value(row, columns[(k_pole, *raised, term)], coefficient)
                    base.add_pivot(row, pivots)

    low_pivots = {p: r for p, r in pivots.items() if p < len(low_labels)}
    free_low = [c for c in range(len(low_labels)) if c not in low_pivots]
    return {
        "k": k,
        "q": all_q,
        "low_labels": low_labels,
        "ordered_columns": ordered_columns,
        "columns": columns,
        "pivots": pivots,
        "free_low": free_low,
    }


def map_label(label):
    k_pole, *rest = label
    exponent = rest.pop()
    return (k_pole, *rest, (exponent[1], exponent[0]))


def map_row(row, source, target, sign=1):
    out = {}
    for column, coefficient in row.items():
        label = source["ordered_columns"][column]
        base.add_value(out, target["columns"][map_label(label)], sign * coefficient)
    return out


def quotient_vector(label, pres, sign=1):
    reduced = base.reduce_row({pres["columns"][label]: sign % PRIME}, pres["pivots"])
    return {c: reduced[c] for c in pres["free_low"] if c in reduced}


def matrix_rank(rows):
    pivots = {}
    for row in rows:
        base.add_pivot(dict(row), pivots)
    return len(pivots)


def compose(forward_rows, reverse_rows, target_free, source_free):
    target_pos = {c: i for i, c in enumerate(target_free)}
    source_pos = {c: i for i, c in enumerate(source_free)}
    failures = 0
    for i, frow in enumerate(forward_rows):
        composed = {}
        for target_column, coeff in frow.items():
            rrow = reverse_rows[target_pos[target_column]]
            for source_column, value in rrow.items():
                base.add_value(composed, source_pos[source_column], coeff * value)
        expected = {i: 1}
        if composed != expected:
            failures += 1
    return failures


def main():
    source = presentation(base.fiber_data, SOURCE_POINT, SOURCE_NAMES)
    target = presentation(g31_fiber_data, TARGET_POINT, TARGET_NAMES)

    # Raw polynomial transport under (a,b)->(c',a')=(b,a).
    source_k_mapped = swap_exponents(source["k"])
    k_match = source_k_mapped == target["k"]
    q_matches = {}
    for sname, tname in zip(SOURCE_NAMES, TARGET_NAMES):
        q_matches[f"{sname}->{tname}"] = swap_exponents(source["q"][sname]) == target["q"][tname]

    # Every source retained relation must map into the target exact image.
    relation_failures = 0
    for row in source["pivots"].values():
        mapped = map_row(row, source, target)
        if base.reduce_row(mapped, target["pivots"]):
            relation_failures += 1

    # Poincare residue convention Omega=dq_G wedge Res:
    # Res_G12=da^db; Res_G31=dc^da; sigma^*(dc^da)=db^da=-da^db.
    orientation_sign = -1
    forward = []
    for source_column in source["free_low"]:
        label = source["ordered_columns"][source_column]
        forward.append(quotient_vector(map_label(label), target, orientation_sign))
    reverse = []
    for target_column in target["free_low"]:
        label = target["ordered_columns"][target_column]
        reverse.append(quotient_vector(map_label(label), source, orientation_sign))

    forward_rank = matrix_rank(forward)
    reverse_rank = matrix_rank(reverse)
    inverse_failures = compose(
        forward, reverse, target["free_low"], source["free_low"]
    )

    source_num = dict(source["q"]["g23"])
    for e, c in source["q"]["g31"].items():
        source_num[e] = (source_num.get(e, 0) + c) % PRIME
    target_num = dict(target["q"]["g23"])
    for e, c in target["q"]["g12"].items():
        target_num[e] = (target_num.get(e, 0) + c) % PRIME
    numerator_match = swap_exponents(clean(source_num)) == clean(target_num)

    result = {
        "schema": "marici.g12-g31-residue-chart-transition.v1",
        "field": PRIME,
        "source": {
            "chart": "q_G12=0",
            "point": SOURCE_POINT,
            "retained_coordinates": ["a=y23", "b=y31"],
            "residue_orientation": "da wedge db",
            "marks": SOURCE_NAMES,
            "quotient_rank": len(source["free_low"]),
            "retained_pivots": len(source["pivots"]),
        },
        "target": {
            "chart": "q_G31=0",
            "point": TARGET_POINT,
            "retained_coordinates": ["c=y12", "a=y23"],
            "residue_orientation": "dc wedge da",
            "marks": TARGET_NAMES,
            "quotient_rank": len(target["free_low"]),
            "retained_pivots": len(target["pivots"]),
        },
        "transition": {
            "site_permutation": "sigma_23",
            "external_parameters": "(X1,X2,X3)->(X1,X3,X2)",
            "fiber_coordinates": "(a,b)->(c',a')=(b,a)",
            "mark_map": dict(zip(SOURCE_NAMES, TARGET_NAMES)),
            "poincare_residue_convention": "Omega=dq_G wedge Res, Omega=dc wedge da wedge db",
            "orientation_pullback": "sigma_23^*(dc' wedge da')=db wedge da=-da wedge db",
            "orientation_sign": orientation_sign,
        },
        "checks": {
            "cayley_menger_polynomial_match": k_match,
            "marked_denominator_matches": q_matches,
            "physical_numerator_g23_plus_partner_match": numerator_match,
            "source_relation_count": len(source["pivots"]),
            "mapped_relation_failures": relation_failures,
            "transport_rank": forward_rank,
            "reverse_transport_rank": reverse_rank,
            "roundtrip_failures": inverse_failures,
            "passed": (
                k_match
                and all(q_matches.values())
                and numerator_match
                and relation_failures == 0
                and forward_rank == len(source["free_low"])
                and reverse_rank == len(target["free_low"])
                and inverse_failures == 0
            ),
        },
        "transport": {
            "basis_convention": "retained free-low columns in reducer order",
            "entry_count": sum(len(row) for row in forward),
            "rows": [
                {
                    "source_free_column": source["free_low"][i],
                    "target_coefficients": {
                        str(column): coefficient for column, coefficient in sorted(row.items())
                    },
                }
                for i, row in enumerate(forward)
            ],
        },
    }
    output = Path(__file__).with_name("g12-g31-residue-chart-transition.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("schema", "checks")}, sort_keys=True))


if __name__ == "__main__":
    main()
