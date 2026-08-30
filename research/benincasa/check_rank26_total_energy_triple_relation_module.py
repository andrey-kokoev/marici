"""Third-order Rees audit of the total-energy Laurent relation module."""

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


POINT = tuple(
    int(value)
    for value in os.environ.get("MARICI_POINT", "2,3,-5").split(",")
)
assert len(POINT) == 3 and sum(POINT) == 0
OFFSETS = (-3, -2, -1, 0, 1, 2, 3)
CHECK_OFFSET = 4
AMBIENT = int(os.environ.get("MARICI_AMBIENT", "8"))
CUTOFF = 6
NAMES = charts.SOURCE_NAMES


def add(row, column, value):
    value = (row.get(column, 0) + value) % base.PRIME
    if value:
        row[column] = value
    else:
        row.pop(column, None)


def column_packet():
    low_monomials = base.monomials_at_most(CUTOFF)
    low_labels = [
        (0, *levels, monomial)
        for levels in product(range(1, 2), repeat=len(NAMES))
        for monomial in low_monomials
    ]
    low_set = set(low_labels)
    ambient_monomials = base.monomials_at_most(AMBIENT + 4)
    ordered = list(low_labels)
    for k_pole in range(charts.K_DEPTH + 1):
        for levels in product(
            range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)
        ):
            ordered.extend(
                label
                for monomial in ambient_monomials
                if (label := (k_pole, *levels, monomial)) not in low_set
            )
    return low_labels, {label: index for index, label in enumerate(ordered)}


def raw_relations(point, columns):
    k, all_q = base.fiber_data(*point)
    q = [all_q[name] for name in NAMES]
    kd = [base.derivative(k, axis) for axis in range(2)]
    qd = [[base.derivative(poly, axis) for axis in range(2)] for poly in q]

    for k_pole in range(charts.K_DEPTH):
        for levels in product(
            range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)
        ):
            if any(level == charts.Q_DEPTH for level in levels):
                continue
            for axis in range(2):
                for exponent in base.monomials_at_most(AMBIENT):
                    row = {}
                    if exponent[axis]:
                        derived = list(exponent)
                        derived[axis] -= 1
                        add(
                            row,
                            columns[(k_pole, *levels, tuple(derived))],
                            exponent[axis],
                        )
                    for term, coefficient in kd[axis].items():
                        add(
                            row,
                            columns[(
                                k_pole + 1,
                                *levels,
                                base.shifted(exponent, term),
                            )],
                            (charts.GAMMA - k_pole) * coefficient,
                        )
                    for qi, q_pole in enumerate(levels):
                        raised = list(levels)
                        raised[qi] += 1
                        for term, coefficient in qd[qi][axis].items():
                            add(
                                row,
                                columns[(
                                    k_pole,
                                    *raised,
                                    base.shifted(exponent, term),
                                )],
                                -q_pole * coefficient,
                            )
                    yield row

    for k_pole in range(charts.K_DEPTH):
        for levels in product(
            range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)
        ):
            for exponent in base.monomials_at_most(AMBIENT - 4):
                row = {columns[(k_pole, *levels, exponent)]: 1}
                for term, coefficient in base.multiply_monomial(k, exponent, -1):
                    add(row, columns[(k_pole + 1, *levels, term)], coefficient)
                yield row

    for qi, qpoly in enumerate(q):
        for k_pole in range(charts.K_DEPTH + 1):
            for levels in product(
                range(1, charts.Q_DEPTH + 1), repeat=len(NAMES)
            ):
                if levels[qi] == charts.Q_DEPTH:
                    continue
                raised = list(levels)
                raised[qi] += 1
                for exponent in base.monomials_at_most(AMBIENT - 1):
                    row = {columns[(k_pole, *levels, exponent)]: 1}
                    for term, coefficient in base.multiply_monomial(
                        qpoly, exponent, -1
                    ):
                        add(row, columns[(k_pole, *raised, term)], coefficient)
                    yield row


def combine(rows, weights):
    result = {}
    for row, weight in zip(rows, weights):
        for column, value in row.items():
            add(result, column, weight * value)
    return result


def polynomial_multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] = (
                result[i + j] + left_value * right_value
            ) % base.PRIME
    return result


def interpolation_weights(coefficient_degree):
    """Coefficient-of-E weights for exact degree-six interpolation."""
    weights = []
    for offset in OFFSETS:
        numerator = [1]
        denominator = 1
        for other in OFFSETS:
            if other == offset:
                continue
            numerator = polynomial_multiply(
                numerator, [(-other) % base.PRIME, 1]
            )
            denominator = denominator * (offset - other) % base.PRIME
        weights.append(
            numerator[coefficient_degree]
            * pow(denominator, base.PRIME - 2, base.PRIME)
            % base.PRIME
        )
    return weights


def evaluation_weights(value):
    weights = []
    for offset in OFFSETS:
        numerator = 1
        denominator = 1
        for other in OFFSETS:
            if other == offset:
                continue
            numerator = numerator * (value - other) % base.PRIME
            denominator = denominator * (offset - other) % base.PRIME
        weights.append(
            numerator * pow(denominator, base.PRIME - 2, base.PRIME)
            % base.PRIME
        )
    return weights


def shifted_row(coefficients, width, shift):
    return {
        shift * width + column: value
        for column, value in coefficients.items()
    }


def assemble(coefficients, width):
    row = {}
    for grade, coefficient_row in enumerate(coefficients):
        for column, value in coefficient_row.items():
            add(row, grade * width + column, value)
    return row


def main() -> None:
    low_labels, columns = column_packet()
    width = len(columns)
    points = [
        (POINT[0], POINT[1], POINT[2] + offset) for offset in OFFSETS
    ]
    generators = [raw_relations(point, columns) for point in points]
    check_generator = raw_relations(
        (POINT[0], POINT[1], POINT[2] + CHECK_OFFSET), columns
    )
    first_weights = interpolation_weights(1)
    second_weights = interpolation_weights(2)
    check_weights = evaluation_weights(CHECK_OFFSET)

    special_pivots = {}
    dual_pivots = {}
    triple_pivots = {}
    relation_count = 0
    degree_bound_checks = 0
    for all_rows in zip(*generators, check_generator, strict=True):
        relation_count += 1
        sampled_rows = all_rows[:-1]
        check_row = all_rows[-1]
        predicted_check = combine(sampled_rows, check_weights)
        assert combine((predicted_check, check_row), (1, -1)) == {}
        degree_bound_checks += 1
        r0 = dict(sampled_rows[OFFSETS.index(0)])
        r1 = combine(sampled_rows, first_weights)
        r2 = combine(sampled_rows, second_weights)
        base.add_pivot(dict(r0), special_pivots)

        base.add_pivot(shifted_row(r0, width, 1), dual_pivots)
        base.add_pivot(assemble((r0, r1), width), dual_pivots)

        base.add_pivot(shifted_row(r0, width, 2), triple_pivots)
        base.add_pivot(assemble(({}, r0, r1), width), triple_pivots)
        base.add_pivot(assemble((r0, r1, r2), width), triple_pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = AMBIENT, CUTOFF
    try:
        special_reference = charts.presentation(base.fiber_data, POINT, NAMES)
        generic_reference = charts.presentation(
            base.fiber_data, (POINT[0], POINT[1], POINT[2] + 1), NAMES
        )
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    assert len(special_reference["pivots"]) == len(special_pivots)

    special_dimension = width - len(special_pivots)
    generic_dimension = width - len(generic_reference["pivots"])
    dual_dimension = 2 * width - len(dual_pivots)
    triple_dimension = 3 * width - len(triple_pivots)
    support_excess = special_dimension - generic_dimension
    length_one = 2 * special_dimension - dual_dimension
    length_two = 2 * dual_dimension - special_dimension - triple_dimension
    length_at_least_three = support_excess - length_one - length_two
    assert min(
        support_excess, length_one, length_two, length_at_least_three
    ) >= 0

    payload = {
        "schema": "marici.benincasa.rank26-total-energy-triple-relation-module.v1",
        "field": base.PRIME,
        "point": list(POINT),
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": CUTOFF,
        "column_count": width,
        "low_column_count": len(low_labels),
        "raw_relation_count": relation_count,
        "normal_interpolation_offsets": list(OFFSETS),
        "degree_bound_check_offset": CHECK_OFFSET,
        "degree_bound_checks_passed": degree_bound_checks,
        "special_relation_rank": len(special_pivots),
        "generic_relation_rank": len(generic_reference["pivots"]),
        "dual_relation_rank": len(dual_pivots),
        "triple_relation_rank": len(triple_pivots),
        "generic_cokernel_dimension": generic_dimension,
        "special_cokernel_dimension": special_dimension,
        "dual_cokernel_dimension": dual_dimension,
        "triple_cokernel_dimension": triple_dimension,
        "support_excess": support_excess,
        "elementary_length_census": {
            "length_1": length_one,
            "length_2": length_two,
            "length_at_least_3": length_at_least_three,
        },
        "reference_presentation_rank_match": True,
        "status": "basis_free_total_energy_second_normal_lengths_computed",
        "scope": (
            "complete finite-cutoff Laurent relation module over "
            "F_p[E_T]/(E_T^3); no rank-26 cyclic-submodule identification "
            "or unbounded nearby-cycle theorem"
        ),
    }
    output = Path(__file__).with_name(
        f"rank26-total-energy-triple-relation-module-a{AMBIENT}-p{base.PRIME}.json"
    )
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
