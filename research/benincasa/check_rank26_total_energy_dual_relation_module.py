"""Basis-free dual-number audit of the total-energy Laurent relation module."""

from __future__ import annotations

import json
import os
import sys
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))

import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts


POINT = (2, 3, -5)
AMBIENT = int(os.environ.get("MARICI_AMBIENT", "8"))
CUTOFF = 6
GAMMA = charts.GAMMA
NAMES = charts.SOURCE_NAMES


def clean(polynomial):
    return {
        exponent: coefficient % base.PRIME
        for exponent, coefficient in polynomial.items()
        if coefficient % base.PRIME
    }


def polynomial_linear_combination(target, source, scale):
    for exponent, coefficient in source.items():
        value = (target.get(exponent, 0) + scale * coefficient) % base.PRIME
        if value:
            target[exponent] = value
        else:
            target.pop(exponent, None)


def normal_derivative_data():
    # Five-point derivative, exact for the source's degree-four dependence on
    # X3 and hence on E_T with X1,X2 fixed.
    weights = { -2: 1, -1: -8, 1: 8, 2: -1 }
    inv12 = pow(12, base.PRIME - 2, base.PRIME)
    kd, qd = {}, {name: {} for name in NAMES}
    for offset, weight in weights.items():
        point = (POINT[0], POINT[1], POINT[2] + offset)
        k, q = base.fiber_data(*point)
        scale = weight * inv12
        polynomial_linear_combination(kd, k, scale)
        for name in NAMES:
            polynomial_linear_combination(qd[name], q[name], scale)
    return clean(kd), {name: clean(polynomial) for name, polynomial in qd.items()}


def column_packet():
    q_count = len(NAMES)
    low_monomials = base.monomials_at_most(CUTOFF)
    low_labels = [
        (0, *levels, monomial)
        for levels in product(range(1, 2), repeat=q_count)
        for monomial in low_monomials
    ]
    low_set = set(low_labels)
    ambient_monomials = base.monomials_at_most(AMBIENT + 4)
    ordered = list(low_labels)
    for k_pole in range(charts.K_DEPTH + 1):
        for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count):
            ordered.extend(
                label
                for monomial in ambient_monomials
                if (label := (k_pole, *levels, monomial)) not in low_set
            )
    return low_labels, {label: index for index, label in enumerate(ordered)}


def add(row, column, value):
    value = (row.get(column, 0) + value) % base.PRIME
    if value:
        row[column] = value
    else:
        row.pop(column, None)


def relation_pairs(columns):
    k0, all_q0 = base.fiber_data(*POINT)
    k1, all_q1 = normal_derivative_data()
    q0 = [all_q0[name] for name in NAMES]
    q1 = [all_q1[name] for name in NAMES]
    kd0 = [base.derivative(k0, axis) for axis in range(2)]
    kd1 = [base.derivative(k1, axis) for axis in range(2)]
    qd0 = [[base.derivative(poly, axis) for axis in range(2)] for poly in q0]
    qd1 = [[base.derivative(poly, axis) for axis in range(2)] for poly in q1]

    for k_pole in range(charts.K_DEPTH):
        for levels in product(range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)):
            if any(level == charts.Q_DEPTH for level in levels):
                continue
            for axis in range(2):
                for exponent in base.monomials_at_most(AMBIENT):
                    r0, r1 = {}, {}
                    if exponent[axis]:
                        derived = list(exponent)
                        derived[axis] -= 1
                        add(r0, columns[(k_pole, *levels, tuple(derived))], exponent[axis])
                    for term, coefficient in kd0[axis].items():
                        add(
                            r0,
                            columns[(k_pole + 1, *levels, base.shifted(exponent, term))],
                            (GAMMA - k_pole) * coefficient,
                        )
                    for term, coefficient in kd1[axis].items():
                        add(
                            r1,
                            columns[(k_pole + 1, *levels, base.shifted(exponent, term))],
                            (GAMMA - k_pole) * coefficient,
                        )
                    for qi, q_pole in enumerate(levels):
                        raised = list(levels)
                        raised[qi] += 1
                        for term, coefficient in qd0[qi][axis].items():
                            add(
                                r0,
                                columns[(k_pole, *raised, base.shifted(exponent, term))],
                                -q_pole * coefficient,
                            )
                        for term, coefficient in qd1[qi][axis].items():
                            add(
                                r1,
                                columns[(k_pole, *raised, base.shifted(exponent, term))],
                                -q_pole * coefficient,
                            )
                    yield r0, r1

    for k_pole in range(charts.K_DEPTH):
        for levels in product(range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)):
            for exponent in base.monomials_at_most(AMBIENT - 4):
                r0 = {columns[(k_pole, *levels, exponent)]: 1}
                r1 = {}
                for term, coefficient in base.multiply_monomial(k0, exponent, -1):
                    add(r0, columns[(k_pole + 1, *levels, term)], coefficient)
                for term, coefficient in base.multiply_monomial(k1, exponent, -1):
                    add(r1, columns[(k_pole + 1, *levels, term)], coefficient)
                yield r0, r1

    for qi, (qpoly0, qpoly1) in enumerate(zip(q0, q1)):
        for k_pole in range(charts.K_DEPTH + 1):
            for levels in product(range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)):
                if levels[qi] == charts.Q_DEPTH:
                    continue
                raised = list(levels)
                raised[qi] += 1
                for exponent in base.monomials_at_most(AMBIENT - 1):
                    r0 = {columns[(k_pole, *levels, exponent)]: 1}
                    r1 = {}
                    for term, coefficient in base.multiply_monomial(qpoly0, exponent, -1):
                        add(r0, columns[(k_pole, *raised, term)], coefficient)
                    for term, coefficient in base.multiply_monomial(qpoly1, exponent, -1):
                        add(r1, columns[(k_pole, *raised, term)], coefficient)
                    yield r0, r1


def main() -> None:
    low_labels, columns = column_packet()
    width = len(columns)
    special_pivots = {}
    dual_pivots = {}
    relation_count = 0
    normal_nonzero_count = 0
    for r0, r1 in relation_pairs(columns):
        relation_count += 1
        normal_nonzero_count += bool(r1)
        base.add_pivot(dict(r0), special_pivots)
        e_row = {width + column: value for column, value in r0.items()}
        base.add_pivot(e_row, dual_pivots)
        full_row = dict(r0)
        for column, value in r1.items():
            add(full_row, width + column, value)
        base.add_pivot(full_row, dual_pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = AMBIENT, CUTOFF
    try:
        reference = charts.presentation(base.fiber_data, POINT, NAMES)
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    assert len(reference["columns"]) == width
    assert len(reference["pivots"]) == len(special_pivots)

    special_rank = len(special_pivots)
    dual_rank = len(dual_pivots)
    bockstein_rank = dual_rank - 2 * special_rank
    special_cokernel = width - special_rank
    dual_cokernel = 2 * width - dual_rank
    inferred_torsion = 2 * special_cokernel - dual_cokernel
    inferred_free = special_cokernel - inferred_torsion
    assert bockstein_rank == inferred_torsion
    assert bockstein_rank >= 0

    payload = {
        "schema": "marici.benincasa.rank26-total-energy-dual-relation-module.v1",
        "field": base.PRIME,
        "point": list(POINT),
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": CUTOFF,
        "column_count": width,
        "low_column_count": len(low_labels),
        "raw_relation_count": relation_count,
        "normal_nonzero_relation_count": normal_nonzero_count,
        "special_relation_rank": special_rank,
        "dual_relation_rank": dual_rank,
        "bockstein_rank": bockstein_rank,
        "special_cokernel_dimension": special_cokernel,
        "dual_cokernel_dimension_over_field": dual_cokernel,
        "inferred_dual_number_decomposition": {
            "free_rank": inferred_free,
            "ET_torsion_rank": inferred_torsion,
        },
        "reference_presentation_rank_match": True,
        "status": "basis_free_total_energy_first_normal_module_computed",
        "scope": (
            "complete finite-cutoff Laurent relation module over F_p[E_T]/(E_T^2); "
            "not yet the rank-26 cyclic source submodule or an unbounded nearby-cycle theorem"
        ),
    }
    output = Path(__file__).with_name(
        f"rank26-total-energy-dual-relation-module-a{AMBIENT}-p{base.PRIME}.json"
    )
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
