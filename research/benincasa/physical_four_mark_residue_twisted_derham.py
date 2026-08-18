"""Literal two-variable product-pole reducer for the four-mark G12 residue."""

from __future__ import annotations

import argparse
import json
from itertools import product


PRIME = 32003
Monomial = tuple[int, int]
Polynomial = dict[Monomial, int]


def add_value(row: dict[int, int], column: int, value: int) -> None:
    value = (row.get(column, 0) + value) % PRIME
    if value:
        row[column] = value
    else:
        row.pop(column, None)


def add_pivot(row: dict[int, int], pivots: dict[int, dict[int, int]]) -> None:
    while row:
        pivot = max(row)
        coefficient = row[pivot]
        if pivot not in pivots:
            inverse = pow(coefficient, PRIME - 2, PRIME)
            pivots[pivot] = {column: value * inverse % PRIME for column, value in row.items()}
            return
        existing = pivots[pivot]
        for column, value in existing.items():
            add_value(row, column, -coefficient * value)


def monomials_at_most(degree: int) -> list[Monomial]:
    return [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)]


def shifted(left: Monomial, right: Monomial) -> Monomial:
    return left[0] + right[0], left[1] + right[1]


def derivative(polynomial: Polynomial, axis: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[axis]
        if not power:
            continue
        next_exponent = list(exponent)
        next_exponent[axis] -= 1
        result[tuple(next_exponent)] = coefficient * power % PRIME
    return result


def multiply_monomial(polynomial: Polynomial, exponent: Monomial, scale: int = 1):
    return [(shifted(exponent, term), scale * coefficient % PRIME) for term, coefficient in polynomial.items()]


def fiber_data(x: int, y: int, z: int) -> tuple[Polynomial, dict[str, Polynomial]]:
    energy = x + y + z
    x2, y2, z2, c2 = x * x, y * y, z * z, energy * energy
    k: Polynomial = {
        (4, 0): x2,
        (2, 2): -(x2 + y2 - z2),
        (0, 4): y2,
        (2, 0): x2 * (x2 - y2 - z2) + c2 * (y2 - x2 - z2),
        (0, 2): y2 * (y2 - x2 - z2) + c2 * (x2 - y2 - z2),
        (0, 0): z2 * c2 * c2 + c2 * z2 * (z2 - x2 - y2) + z2 * x2 * y2,
    }
    k = {exponent: coefficient % PRIME for exponent, coefficient in k.items() if coefficient % PRIME}
    q = {
        "g1": {(0, 1): 1, (0, 0): -y - z},
        "g2": {(1, 0): 1, (0, 0): -x - z},
        "g3": {(1, 0): 1, (0, 1): 1, (0, 0): z},
        "g23": {(0, 1): 1, (0, 0): -x},
        "g31": {(1, 0): 1, (0, 0): -y},
    }
    return k, {name: {e: c % PRIME for e, c in poly.items()} for name, poly in q.items()}


def reduce_row(row: dict[int, int], pivots: dict[int, dict[int, int]]) -> dict[int, int]:
    row = dict(row)
    while row:
        pivot = max(row)
        if pivot not in pivots:
            break
        coefficient = row[pivot]
        for column, value in pivots[pivot].items():
            add_value(row, column, -coefficient * value)
    return row


def presentation(
    names: tuple[str, ...], gamma: int, ambient: int, cutoff: int, minimum_q_level: int = 0
):
    k, all_q = fiber_data(2, 3, 4)
    q_polynomials = [all_q[name] for name in names]
    q_count = len(names)
    k_depth = q_depth = 2
    column_degree = ambient + 4
    low_monomials = monomials_at_most(cutoff)
    low_labels = [
        (0, *levels, monomial)
        for levels in product(range(minimum_q_level, 2), repeat=q_count)
        for monomial in low_monomials
    ]
    low_set = set(low_labels)
    ambient_monomials = monomials_at_most(column_degree)
    ordered_columns = list(low_labels)
    for k_pole in range(k_depth + 1):
        for levels in product(range(minimum_q_level, q_depth + 1), repeat=q_count):
            ordered_columns.extend(
                label for monomial in ambient_monomials
                if (label := (k_pole, *levels, monomial)) not in low_set
            )
    columns = {label: index for index, label in enumerate(ordered_columns)}
    pivots: dict[int, dict[int, int]] = {}
    k_derivatives = [derivative(k, axis) for axis in range(2)]
    q_derivatives = [[derivative(q, axis) for axis in range(2)] for q in q_polynomials]

    for k_pole in range(k_depth):
        for levels in product(range(minimum_q_level, q_depth + 1), repeat=q_count):
            if any(level == q_depth for level in levels if level > 0):
                continue
            for axis in range(2):
                for exponent in monomials_at_most(ambient):
                    row: dict[int, int] = {}
                    if exponent[axis]:
                        derived = list(exponent)
                        derived[axis] -= 1
                        add_value(row, columns[(k_pole, *levels, tuple(derived))], exponent[axis])
                    for term, coefficient in k_derivatives[axis].items():
                        add_value(row, columns[(k_pole + 1, *levels, shifted(exponent, term))], (gamma - k_pole) * coefficient)
                    for q_index, q_pole in enumerate(levels):
                        if not q_pole:
                            continue
                        raised = list(levels)
                        raised[q_index] += 1
                        for term, coefficient in q_derivatives[q_index][axis].items():
                            add_value(row, columns[(k_pole, *raised, shifted(exponent, term))], -q_pole * coefficient)
                    add_pivot(row, pivots)

    for k_pole in range(k_depth):
        for levels in product(range(minimum_q_level, q_depth + 1), repeat=q_count):
            for exponent in monomials_at_most(ambient - 4):
                row = {columns[(k_pole, *levels, exponent)]: 1}
                for term, coefficient in multiply_monomial(k, exponent, -1):
                    add_value(row, columns[(k_pole + 1, *levels, term)], coefficient)
                add_pivot(row, pivots)

    for q_index, q_polynomial in enumerate(q_polynomials):
        for k_pole in range(k_depth + 1):
            for levels in product(range(minimum_q_level, q_depth + 1), repeat=q_count):
                if levels[q_index] == q_depth:
                    continue
                raised = list(levels)
                raised[q_index] += 1
                for exponent in monomials_at_most(ambient - 1):
                    row = {columns[(k_pole, *levels, exponent)]: 1}
                    for term, coefficient in multiply_monomial(q_polynomial, exponent, -1):
                        add_value(row, columns[(k_pole, *raised, term)], coefficient)
                    add_pivot(row, pivots)

    low_pivots = {pivot: row for pivot, row in pivots.items() if pivot < len(low_labels)}
    free_low = [column for column in range(len(low_labels)) if column not in low_pivots]
    return low_labels, columns, low_pivots, free_low


def quotient_coordinates(
    label, columns: dict, low_pivots: dict[int, dict[int, int]], free_low: list[int]
) -> dict[int, int]:
    reduced = reduce_row({columns[label]: 1}, low_pivots)
    return {column: reduced[column] for column in free_low if column in reduced}


def filtered_census(names: tuple[str, ...], gamma: int, ambient: int, cutoff: int) -> dict:
    low_labels, columns, low_pivots, free_low = presentation(names, gamma, ambient, cutoff)
    source_label = (0, *([1] * len(names)), (0, 0))
    source = quotient_coordinates(source_label, columns, low_pivots, free_low)

    face_pivots: dict[int, dict[int, int]] = {}
    for label in low_labels:
        if any(level == 0 for level in label[1:-1]):
            add_pivot(quotient_coordinates(label, columns, low_pivots, free_low), face_pivots)
    source_mod_faces = reduce_row(source, face_pivots)
    return {
        "dimension": len(free_low),
        "source_nonzero": bool(source),
        "proper_face_rank": len(face_pivots),
        "source_beyond_proper_faces": bool(source_mod_faces),
        "source_quotient_support": len(source),
        "source_mod_faces_support": len(source_mod_faces),
    }


def relative_top_census(names: tuple[str, ...], gamma: int, ambient: int, cutoff: int) -> dict:
    low_labels, columns, low_pivots, free_low = presentation(
        names, gamma, ambient, cutoff, minimum_q_level=1
    )
    source_label = (0, *([1] * len(names)), (0, 0))
    source = quotient_coordinates(source_label, columns, low_pivots, free_low)
    return {
        "relative_top_dimension": len(free_low),
        "relative_source_nonzero": bool(source),
        "relative_source_support": len(source),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--partner", choices=("g23", "g31"), default="g23")
    parser.add_argument("--gamma", type=int, default=5)
    parser.add_argument("--ambient", type=int, default=8)
    parser.add_argument("--cutoff", type=int, default=5)
    args = parser.parse_args()
    names = ("g1", "g2", "g3", args.partner)
    census = filtered_census(names, args.gamma % PRIME, args.ambient, args.cutoff)
    relative = relative_top_census(names, args.gamma % PRIME, args.ambient, args.cutoff)
    print(json.dumps({
        "schema": "marici.physical-four-mark-residue-twisted-derham.v1",
        "prime": PRIME, "kinematics": [2, 3, 4], "marks": names,
        "gamma": args.gamma, "ambient_degree": args.ambient,
        "cutoff_degree": args.cutoff, **census, **relative,
        "expected_dimension": 20, "calibration_passed": census["dimension"] == 20,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
