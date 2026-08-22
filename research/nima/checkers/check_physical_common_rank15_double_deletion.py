"""Identify the rank-15 common sector inside one five-mark presentation."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

NAMES = ("g1", "g2", "g3", "g23", "g31")
GAMMA = int(os.environ.get("MARICI_TWIST_GAMMA", "5")) % m.PRIME
AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "10"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "5"))
RESULT_NAME = (
    "physical_common_rank15_half_twist_filtration.json"
    if GAMMA == (m.PRIME - 1) // 2
    else "physical_common_rank15_double_deletion.json"
)
OUT = Path(__file__).resolve().parents[1] / "results" / RESULT_NAME


def add_scaled(target, vector, scale=1):
    for column, value in vector.items():
        m.add_value(target, column, scale * value)


def main() -> None:
    low, columns, pivots, free = m.presentation(
        NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    label_by_column = {columns[label]: label for label in low}

    def labelled_span(predicate):
        span = {}
        for label in low:
            if predicate(label):
                m.add_pivot(m.quotient_coordinates(label, columns, pivots, free), span)
        return span

    face23 = labelled_span(lambda label: label[5] == 0)  # g31 absent
    face31 = labelled_span(lambda label: label[4] == 0)  # g23 absent
    double_face = labelled_span(lambda label: label[4] == 0 and label[5] == 0)

    face_sum = {}
    for row in list(face23.values()) + list(face31.values()):
        m.add_pivot(dict(row), face_sum)
    intersection_dimension = len(face23) + len(face31) - len(face_sum)

    def outside(candidate, container):
        return sum(bool(m.reduce_row(row, container)) for row in candidate.values())

    def connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(
                image,
                m.connection_image(label_by_column[column], NAMES, GAMMA, axis, columns),
                coefficient,
            )
        reduced = m.reduce_row(image, pivots)
        return {column: reduced[column] for column in free if column in reduced}

    connection_failures = [
        sum(bool(m.reduce_row(connection(row, axis), double_face)) for row in double_face.values())
        for axis in range(2)
    ]

    marked_deletion_dimensions = []
    marked_deletions = []
    marked_deletion_sum = {}
    for marked_index in range(1, 4):
        subface = labelled_span(
            lambda label, marked_index=marked_index:
            label[4] == 0 and label[5] == 0 and label[marked_index] == 0
        )
        marked_deletion_dimensions.append(len(subface))
        marked_deletions.append(subface)
        for row in subface.values():
            m.add_pivot(dict(row), marked_deletion_sum)

    marked_pair_sum_dimensions = []
    marked_pair_intersection_dimensions = []
    one_mark_faces = []
    for left, right in ((0, 1), (0, 2), (1, 2)):
        pair_sum = {}
        for row in list(marked_deletions[left].values()) + list(marked_deletions[right].values()):
            m.add_pivot(dict(row), pair_sum)
        marked_pair_sum_dimensions.append(len(pair_sum))
        marked_pair_intersection_dimensions.append(
            len(marked_deletions[left]) + len(marked_deletions[right]) - len(pair_sum)
        )
        absent = {left + 1, right + 1}
        one_mark_faces.append(
            labelled_span(
                lambda label, absent=absent:
                label[4] == 0 and label[5] == 0
                and all(label[index] == 0 for index in absent)
            )
        )
    triple_deletion = labelled_span(
        lambda label: all(label[index] == 0 for index in range(1, 6))
    )
    marked_deletion_connection_failures = [preservation for preservation in (
        [
            sum(bool(m.reduce_row(connection(row, axis), subface)) for row in subface.values())
            for axis in range(2)
        ]
        for subface in marked_deletions
    )]
    one_mark_connection_failures = [
        [
            sum(bool(m.reduce_row(connection(row, axis), subface)) for row in subface.values())
            for axis in range(2)
        ]
        for subface in one_mark_faces
    ]
    triple_deletion_connection_failures = [
        sum(bool(m.reduce_row(connection(row, axis), triple_deletion)) for row in triple_deletion.values())
        for axis in range(2)
    ]

    packet = {
        "schema": "marici.physical-common-rank15-double-deletion.v1",
        "prime": m.PRIME,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "twist_gamma_mod_prime": GAMMA,
        "face_dimensions": [len(face23), len(face31)],
        "face_intersection_dimension": intersection_dimension,
        "double_deletion_dimension": len(double_face),
        "double_deletion_outside_face23": outside(double_face, face23),
        "double_deletion_outside_face31": outside(double_face, face31),
        "double_deletion_connection_failures": connection_failures,
        "marked_deletion_dimensions_inside_double_face": marked_deletion_dimensions,
        "marked_deletion_connection_failures": marked_deletion_connection_failures,
        "marked_pair_sum_dimensions_inside_double_face": marked_pair_sum_dimensions,
        "marked_pair_intersection_dimensions_inside_double_face": marked_pair_intersection_dimensions,
        "triple_deletion_dimension_inside_double_face": len(triple_deletion),
        "one_mark_connection_failures": one_mark_connection_failures,
        "triple_deletion_connection_failures": triple_deletion_connection_failures,
        "marked_deletion_sum_dimension_inside_double_face": len(marked_deletion_sum),
    }
    packet["double_deletion_equals_face_intersection"] = (
        packet["double_deletion_dimension"] == intersection_dimension
        and packet["double_deletion_outside_face23"] == 0
        and packet["double_deletion_outside_face31"] == 0
    )
    packet["passed"] = (
        packet["face_dimensions"] == [20, 20]
        and packet["face_intersection_dimension"] == 15
        and packet["double_deletion_equals_face_intersection"]
        and packet["double_deletion_connection_failures"] == [0, 0]
        and packet["marked_deletion_connection_failures"] == [[0, 0]] * 3
        and packet["one_mark_connection_failures"] == [[0, 0]] * 3
        and packet["triple_deletion_connection_failures"] == [0, 0]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
