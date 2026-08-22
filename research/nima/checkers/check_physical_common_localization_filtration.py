"""Typed face filtration inside one common five-mark presentation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

OUT = Path(__file__).resolve().parents[1] / "results" / "physical_common_localization_filtration.json"
NAMES = ("g1", "g2", "g3", "g23", "g31")
GAMMA, AMBIENT, CUTOFF = 5, 10, 5


def add_scaled(target, vector, scale=1):
    for column, value in vector.items():
        m.add_value(target, column, scale * value)


def main() -> None:
    low, columns, pivots, free = m.presentation(
        NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    label_by_column = {columns[label]: label for label in low}

    def face(level_index):
        span = {}
        for label in low:
            if label[1 + level_index] == 0:
                m.add_pivot(m.quotient_coordinates(label, columns, pivots, free), span)
        return span

    face23 = face(4)  # g31 absent
    face31 = face(3)  # g23 absent
    common_faces = [face(index) for index in range(3)]
    face_sum = {}
    for row in list(face23.values()) + list(face31.values()):
        m.add_pivot(dict(row), face_sum)

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

    def preservation_failures(span):
        failures = [0, 0]
        for row in span.values():
            for axis in range(2):
                failures[axis] += int(bool(m.reduce_row(connection(row, axis), span)))
        return failures

    source = {}
    source_labels = (
        (0, 1, 1, 1, 1, 0, (0, 0)),
        (0, 1, 1, 1, 0, 1, (0, 0)),
    )
    for label in source_labels:
        add_scaled(source, m.quotient_coordinates(label, columns, pivots, free))
    source_derivative_residuals = [
        bool(m.reduce_row(connection(source, axis), face_sum)) for axis in range(2)
    ]
    activation_by_common_face = []
    quotient_representative = None
    representative_origin = None
    for index, common_face in enumerate(common_faces):
        enlarged = {pivot: dict(row) for pivot, row in face_sum.items()}
        for row in common_face.values():
            residual = m.reduce_row(row, face_sum)
            if quotient_representative is None and residual:
                quotient_representative = residual
                representative_origin = NAMES[index]
            m.add_pivot(dict(row), enlarged)
        activation_by_common_face.append(len(enlarged) - len(face_sum))
    labels_by_column = {columns[label]: label for label in low}
    representative_packet = [
        {"label": labels_by_column[column], "coefficient": coefficient}
        for column, coefficient in sorted((quotient_representative or {}).items())
    ]

    packet = {
        "schema": "marici.physical-common-localization-filtration.v1",
        "prime": m.PRIME,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "common_total_dimension": len(free),
        "face_dimensions": [len(face23), len(face31)],
        "face_intersection_dimension": len(face23) + len(face31) - len(face_sum),
        "face_sum_dimension": len(face_sum),
        "top_quotient_dimension": len(free) - len(face_sum),
        "face23_connection_failures": preservation_failures(face23),
        "face31_connection_failures": preservation_failures(face31),
        "face_sum_connection_failures": preservation_failures(face_sum),
        "physical_source_lies_in_face_sum": not bool(m.reduce_row(source, face_sum)),
        "physical_source_derivative_outside_face_sum": source_derivative_residuals,
        "top_line_activation_by_g1_g2_g3_faces": activation_by_common_face,
        "top_line_representative_origin": representative_origin,
        "top_line_representative": representative_packet,
        "top_line_local_form": "da wedge db / (q_g23 q_g31), with the common three marks absent",
        "interpretation": "typed filtration 15<25<26; its quotient is the horizontal two-mark Kato line and is physically unactivated",
    }
    packet["passed"] = (
        packet["common_total_dimension"] == 26
        and packet["face_dimensions"] == [20, 20]
        and packet["face_intersection_dimension"] == 15
        and packet["face_sum_dimension"] == 25
        and packet["top_quotient_dimension"] == 1
        and packet["face23_connection_failures"] == [0, 0]
        and packet["face31_connection_failures"] == [0, 0]
        and packet["face_sum_connection_failures"] == [0, 0]
        and packet["physical_source_lies_in_face_sum"]
        and packet["physical_source_derivative_outside_face_sum"] == [False, False]
        and packet["top_line_activation_by_g1_g2_g3_faces"] == [1, 1, 1]
        and packet["top_line_representative"] == [
            {"label": (0, 0, 0, 0, 1, 1, (0, 0)), "coefficient": 1}
        ]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
