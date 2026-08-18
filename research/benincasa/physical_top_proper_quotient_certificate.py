"""Certificate for the proper three-pole quotient and the literal top form."""

from __future__ import annotations

import argparse
import json

from physical_single_q_twisted_derham_calibration import Q_POLYNOMIALS
from physical_top_twisted_derham_calibration import PRIME, add_pivot
from physical_two_q_twisted_derham_calibration import filtered_presentation


def normal_form(row, pivots):
    work = dict(row)
    remainder = {}
    while work:
        column = max(work)
        coefficient = work[column]
        if column in pivots:
            for other_column, value in pivots[column].items():
                updated = (work.get(other_column, 0) - coefficient * value) % PRIME
                if updated:
                    work[other_column] = updated
                else:
                    work.pop(other_column, None)
        else:
            remainder[column] = coefficient
            del work[column]
    return remainder


def span_rank(rows):
    pivots = {}
    for row in rows:
        add_pivot(dict(row), pivots)
    return len(pivots)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k-depth", type=int, default=2)
    parser.add_argument("--q-depth", type=int, default=2)
    parser.add_argument("--ambient", type=int, default=9)
    parser.add_argument("--cutoff", type=int, default=5)
    parser.add_argument("--gamma", type=int, default=5)
    arguments = parser.parse_args()

    names = ("g1", "g2", "G12")
    labels, columns, low_labels, relation_pivots = filtered_presentation(
        tuple(Q_POLYNOMIALS[name] for name in names),
        arguments.k_depth,
        arguments.q_depth,
        arguments.ambient,
        arguments.cutoff,
        arguments.gamma % PRIME,
    )
    del labels
    low_normal_forms = [
        normal_form({columns[label]: 1}, relation_pivots) for label in low_labels
    ]
    inherited = [
        row
        for label, row in zip(low_labels, low_normal_forms)
        if 0 in label[1:4]
    ]
    omega_label = (0, 1, 1, 1, (0, 0, 0))
    omega = normal_form({columns[omega_label]: 1}, relation_pivots)
    total_rank = span_rank(low_normal_forms)
    inherited_rank = span_rank(inherited)
    omega_augmented_rank = span_rank([*inherited, omega])
    result = {
        "schema": "marici.benincasa.physical_top_proper_quotient_certificate.v1",
        "prime": PRIME,
        "kinematics": [2, 3, 4],
        "denominators": names,
        "gamma": arguments.gamma,
        "k_depth": arguments.k_depth,
        "q_depth_each": arguments.q_depth,
        "ambient_degree": arguments.ambient,
        "cutoff_degree": arguments.cutoff,
        "top_rank": total_rank,
        "proper_face_span_rank": inherited_rank,
        "proper_top_quotient_rank": total_rank - inherited_rank,
        "literal_omega_111_normal_form_nonzero": bool(omega),
        "face_span_plus_literal_omega_rank": omega_augmented_rank,
        "literal_omega_111_generates_proper_quotient": (
            omega_augmented_rank == total_rank == inherited_rank + 1
        ),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
