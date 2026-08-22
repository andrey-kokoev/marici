"""Differentiate the physical localization presentation with dual numbers.

This distinguishes the frozen commutator A_c F - F A_a from the invariant
mixed curvature dF + A_c F - F A_a.
"""

from __future__ import annotations

import json
import os
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

NAMES = ("g1", "g2", "g3", "g23", "g31")
P = m.PRIME
GAMMA = (P - 1) // 2
AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "12"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "6"))
AXES = tuple(
    int(axis) for axis in os.environ.get("MARICI_EXTERNAL_AXES", "0,1").split(",")
)
AXIS_SUFFIX = "" if AXES == (0, 1) else "_axes" + "-".join(map(str, AXES))
OUT = Path(__file__).resolve().parents[1] / "results" / (
    f"physical_moving_localization_horizontality_p{P}_a{AMBIENT}_c{CUTOFF}{AXIS_SUFFIX}.json"
)


def add(row, column, value, tangent=0):
    old_value, old_tangent = row.get(column, (0, 0))
    pair = ((old_value + value) % P, (old_tangent + tangent) % P)
    if pair != (0, 0):
        row[column] = pair
    else:
        row.pop(column, None)


def scale_pair(pair, scalar):
    return pair[0] * scalar % P, pair[1] * scalar % P


def add_scaled(target, source, scalar):
    for column, pair in source.items():
        add(target, column, pair[0] * scalar, pair[1] * scalar)


def normalize(row, pivot):
    value, tangent = row[pivot]
    inverse = pow(value, P - 2, P)
    inverse_tangent = -tangent * inverse * inverse % P
    return {
        column: (
            coefficient * inverse % P,
            (derivative * inverse + coefficient * inverse_tangent) % P,
        )
        for column, (coefficient, derivative) in row.items()
    }


def eliminate(row, pivots):
    row = dict(row)
    while any(value for value, _ in row.values()):
        pivot = max(column for column, (value, _) in row.items() if value)
        if pivot not in pivots:
            break
        value, tangent = row[pivot]
        existing = pivots[pivot]
        for column, (coefficient, derivative) in existing.items():
            add(
                row,
                column,
                -value * coefficient,
                -tangent * coefficient - value * derivative,
            )
    return row


def add_pivot(row, pivots, tangent_rows):
    row = eliminate(row, pivots)
    value_columns = [column for column, (value, _) in row.items() if value]
    if value_columns:
        pivot = max(value_columns)
        pivots[pivot] = normalize(row, pivot)
    elif any(tangent for _, tangent in row.values()):
        tangent_rows.append(
            {column: tangent for column, (_, tangent) in row.items() if tangent}
        )


def polynomial_terms(polynomial, tangent_polynomial, exponent, scale):
    terms = set(polynomial) | set(tangent_polynomial)
    for term in terms:
        yield (
            m.shifted(exponent, term),
            scale * polynomial.get(term, 0),
            scale * tangent_polynomial.get(term, 0),
        )


def presentation_tangent(names, external_axis):
    k, all_q = m.fiber_data(2, 3, 4)
    dk, dall_q = m.parameter_derivative_data(external_axis)
    q = [all_q[name] for name in names]
    dq = [dall_q[name] for name in names]
    q_count = len(names)
    low_monomials = m.monomials_at_most(CUTOFF)
    low_labels = [
        (0, *levels, monomial)
        for levels in product(range(2), repeat=q_count)
        for monomial in low_monomials
    ]
    low_set = set(low_labels)
    ordered_columns = list(low_labels)
    for k_pole in range(3):
        for levels in product(range(3), repeat=q_count):
            ordered_columns.extend(
                label
                for monomial in m.monomials_at_most(AMBIENT + 4)
                if (label := (k_pole, *levels, monomial)) not in low_set
            )
    columns = {label: index for index, label in enumerate(ordered_columns)}
    pivots = {}
    tangent_rows = []
    ka = [m.derivative(k, axis) for axis in range(2)]
    dka = [m.derivative(dk, axis) for axis in range(2)]
    qa = [[m.derivative(poly, axis) for axis in range(2)] for poly in q]
    dqa = [[m.derivative(poly, axis) for axis in range(2)] for poly in dq]

    for k_pole in range(2):
        for levels in product(range(3), repeat=q_count):
            if any(level == 2 for level in levels if level > 0):
                continue
            for fiber_axis in range(2):
                for exponent in m.monomials_at_most(AMBIENT):
                    row = {}
                    if exponent[fiber_axis]:
                        derived = list(exponent)
                        derived[fiber_axis] -= 1
                        add(row, columns[(k_pole, *levels, tuple(derived))], exponent[fiber_axis])
                    for term, value, tangent in polynomial_terms(
                        ka[fiber_axis], dka[fiber_axis], exponent, GAMMA - k_pole
                    ):
                        add(row, columns[(k_pole + 1, *levels, term)], value, tangent)
                    for index, level in enumerate(levels):
                        if not level:
                            continue
                        raised = list(levels)
                        raised[index] += 1
                        for term, value, tangent in polynomial_terms(
                            qa[index][fiber_axis], dqa[index][fiber_axis], exponent, -level
                        ):
                            add(row, columns[(k_pole, *raised, term)], value, tangent)
                    add_pivot(row, pivots, tangent_rows)

    for k_pole in range(2):
        for levels in product(range(3), repeat=q_count):
            for exponent in m.monomials_at_most(AMBIENT - 4):
                row = {columns[(k_pole, *levels, exponent)]: (1, 0)}
                for term, value, tangent in polynomial_terms(k, dk, exponent, -1):
                    add(row, columns[(k_pole + 1, *levels, term)], value, tangent)
                add_pivot(row, pivots, tangent_rows)

    for index, polynomial in enumerate(q):
        for k_pole in range(3):
            for levels in product(range(3), repeat=q_count):
                if levels[index] == 2:
                    continue
                raised = list(levels)
                raised[index] += 1
                for exponent in m.monomials_at_most(AMBIENT - 1):
                    row = {columns[(k_pole, *levels, exponent)]: (1, 0)}
                    for term, value, tangent in polynomial_terms(
                        polynomial, dq[index], exponent, -1
                    ):
                        add(row, columns[(k_pole, *raised, term)], value, tangent)
                    add_pivot(row, pivots, tangent_rows)

    low_pivots = {pivot: row for pivot, row in pivots.items() if pivot < len(low_labels)}
    free = [column for column in range(len(low_labels)) if column not in low_pivots]
    base_value_pivots = {
        pivot: {column: value for column, (value, _) in row.items() if value}
        for pivot, row in pivots.items()
    }
    final_tangent_pivots = {}
    for row in tangent_rows:
        reduced = m.reduce_row(dict(row), base_value_pivots)
        m.add_pivot(reduced, final_tangent_pivots)
    return low_labels, columns, pivots, final_tangent_pivots, free


def quotient(label, columns, pivots, tangent_pivots, free):
    row = eliminate({columns[label]: (1, 0)}, pivots)
    tangent = m.reduce_row(
        {column: derivative for column, (_, derivative) in row.items() if derivative},
        tangent_pivots,
    )
    row = {
        column: (value, tangent.get(column, 0))
        for column, (value, _) in row.items()
        if value or tangent.get(column, 0)
    }
    for column, derivative in tangent.items():
        if column not in row:
            row[column] = (0, derivative)
    return {column: row[column] for column in free if column in row}


def rank(rows):
    pivots = {}
    for source in rows:
        row = {column: value for column, value in source.items() if value % P}
        m.add_pivot(row, pivots)
    return len(pivots)


def pivot_packet(rows):
    pivots = {}
    for source in rows:
        m.add_pivot(dict(source), pivots)
    return [pivots[pivot] for pivot in sorted(pivots, reverse=True)]


def main():
    a0, ac, ap, af = m.presentation((), GAMMA, AMBIENT, CUTOFF, minimum_q_level=0)
    c0, cc, cp, cf = m.presentation(NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0)
    al = {column: label for label, column in ac.items()}
    cl = {column: label for label, column in cc.items()}

    def cq(vector):
        reduced = m.reduce_row(vector, cp)
        return {column: reduced[column] for column in cf if column in reduced}

    images = {}
    for column in af:
        k_pole, monomial = al[column]
        images[column] = cq({cc[(k_pole, 0, 0, 0, 0, 0, monomial)]: 1})

    # Carry source lifts through row reduction to obtain the intrinsic kernel
    # of the frozen localization map.
    image_pivots = {}
    lift_pivots = {}
    kernel = []
    for source_column in af:
        row = dict(images[source_column])
        lift = {source_column: 1}
        while row and max(row) in image_pivots:
            pivot = max(row)
            coefficient = row[pivot]
            for target, value in image_pivots[pivot].items():
                m.add_value(row, target, -coefficient * value)
            for target, value in lift_pivots[pivot].items():
                m.add_value(lift, target, -coefficient * value)
        if row:
            pivot = max(row)
            inverse = pow(row[pivot], P - 2, P)
            image_pivots[pivot] = {
                target: value * inverse % P for target, value in row.items()
            }
            lift_pivots[pivot] = {
                target: value * inverse % P for target, value in lift.items()
            }
        else:
            kernel.append(lift)

    packets = []
    all_residuals = []
    for axis in AXES:
        a_low, a_columns, a_pivots, a_tangent_pivots, a_free = presentation_tangent((), axis)
        c_low, c_columns, c_pivots, c_tangent_pivots, c_free = presentation_tangent(NAMES, axis)
        a_label = {column: label for label, column in a_columns.items()}

        derivatives = []
        values_match = True
        for column in a_free:
            k_pole, monomial = a_label[column]
            embedded = (k_pole, 0, 0, 0, 0, 0, monomial)
            coordinates = quotient(
                embedded, c_columns, c_pivots, c_tangent_pivots, c_free
            )
            value_coordinates = {
                target: pair[0] for target, pair in coordinates.items() if pair[0]
            }
            if value_coordinates != images[column]:
                values_match = False
            derivatives.append({target: pair[1] for target, pair in coordinates.items() if pair[1]})

        # Independently reproduce the frozen commutator using the established
        # checker machinery and test whether dF cancels it.
        def conn(vector, labels, names, columns, pivots, free):
            result = {}
            for column, coefficient in vector.items():
                for target, value in m.connection_image(labels[column], names, GAMMA, axis, columns).items():
                    m.add_value(result, target, coefficient * value)
            reduced = m.reduce_row(result, pivots)
            return {column: reduced[column] for column in free if column in reduced}

        residuals = []
        commutators = []
        for index, source_column in enumerate(af):
            commutator = conn(images[source_column], cl, NAMES, cc, cp, cf)
            source_connection = conn({source_column: 1}, al, (), ac, ap, af)
            mapped = {}
            for source, coefficient in source_connection.items():
                for target, value in images[source].items():
                    m.add_value(mapped, target, coefficient * value)
            for target, value in mapped.items():
                m.add_value(commutator, target, -value)
            residual = dict(commutator)
            for target, value in derivatives[index].items():
                m.add_value(residual, target, value)
            commutators.append(commutator)
            residuals.append(residual)

        all_residuals.extend(residuals)
        kernel_residuals = []
        for relation in kernel:
            residual = {}
            for source_column, coefficient in relation.items():
                for target, value in residuals[af.index(source_column)].items():
                    m.add_value(residual, target, coefficient * value)
            kernel_residuals.append(residual)
        parity_ranks = {}
        for parity in ((0, 0), (0, 1), (1, 0), (1, 1)):
            selected = [
                residual
                for source_column, residual in zip(af, residuals)
                if tuple(power % 2 for power in al[source_column][-1]) == parity
            ]
            parity_ranks[str(parity)] = rank(selected)

        packets.append(
            {
                "axis": axis,
                "absolute_dimension": len(a_free),
                "common_dimension": len(c_free),
                "dual_free_bases_match": a_free == af and c_free == cf,
                "dual_value_channel_matches_frozen_map": values_match,
                "absolute_tangent_relation_rank": len(a_tangent_pivots),
                "common_tangent_relation_rank": len(c_tangent_pivots),
                "moving_derivative_rank": rank(derivatives),
                "frozen_commutator_rank": rank(commutators),
                "mixed_curvature_rank": rank(residuals),
                "mixed_curvature_parity_ranks": parity_ranks,
                "mixed_curvature_kernel_restriction_rank": rank(kernel_residuals),
                "mixed_curvature_rows": residuals,
                "mixed_curvature_image_basis": pivot_packet(residuals),
                "mixed_curvature_kernel_rows": kernel_residuals,
            }
        )

    packet = {
        "schema": "marici.physical-moving-localization-horizontality.v1",
        "prime": P,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "external_axes": list(AXES),
        "localization_kernel_dimension": len(kernel),
        "axes": packets,
        "combined_mixed_curvature_rank": rank(all_residuals),
    }
    packet["theta_vanishes"] = packet["combined_mixed_curvature_rank"] == 0
    packet["higher_coherence_obstruction_detected"] = (
        not packet["theta_vanishes"]
        and all(item["mixed_curvature_rank"] > 0 for item in packets)
    )
    packet["passed"] = all(
        item["dual_free_bases_match"]
        and item["dual_value_channel_matches_frozen_map"]
        and item["absolute_tangent_relation_rank"] == 0
        and item["common_tangent_relation_rank"] == 0
        for item in packets
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
