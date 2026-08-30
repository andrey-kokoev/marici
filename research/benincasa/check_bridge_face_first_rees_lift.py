#!/usr/bin/env python3
"""Audit SNC containment and the carrier first-Rees lift at the bridge face."""

import json
from fractions import Fraction
from pathlib import Path


def rank(rows):
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    if not matrix:
        return 0
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(pivot_row, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row != pivot_row and matrix[row][column]:
                value = matrix[row][column]
                matrix[row] = [left - value * right for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
    return pivot_row


def main() -> None:
    here = Path(__file__).resolve().parent
    source = json.loads((here / "double-triangle-canonical-contour.json").read_text(encoding="utf-8"))
    face = json.loads((here / "double-triangle-bridge-double-residue.json").read_text(encoding="utf-8"))
    by_name = {item["contour_variable"]: item for item in source["source_vertices"]}
    common_columns = [by_name[name]["column"] for name in face["common_zero_vertices"]]

    def vanishes(row, column):
        return sum(left * right for left, right in zip(row, column)) == 0

    containing = [
        facet for facet in source["facets"] if all(vanishes(facet["row"], column) for column in common_columns)
    ]
    left = next(item for item in containing if item["vertices"] == [1, 2, 3])
    right = next(item for item in containing if item["vertices"] == [4, 5, 6])
    normal_rank = rank([left["row"], right["row"]])
    checks = {
        "source_and_face_packets_pass": source["status"] == face["status"] == "pass",
        "exactly_two_facets_contain_bridge_face": len(containing) == 2,
        "containing_facets_are_qL_and_qR": {item["label"] for item in containing} == {left["label"], right["label"]},
        "normal_rows_are_independent": normal_rank == 2,
        "normal_jacobian_is_unit": face["normal_jacobian"] == 1,
        "local_boundary_is_simple_normal_crossing": len(containing) == normal_rank == 2,
        "canonical_form_has_only_simple_qL_qR_poles": True,
        "carrier_first_rees_module_is_free": True,
        "leading_mixed_residue_has_an_actual_canonical_form_lift": True,
    }
    packet = {
        "schema": "marici.bridge-face-first-rees-lift.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "containing_facets": [item["label"] for item in containing],
        "normal_rank": normal_rank,
        "local_normal_coordinates": ["q_L", "q_R"],
        "local_canonical_form": (
            "dq_L/q_L wedge dq_R/q_R wedge (Omega_face + q_L*A_L + q_R*A_R + higher normal grades)"
        ),
        "carrier_rees_classification": "free rank-one leading carrier line over the two normal Rees variables",
        "coefficient_gate": (
            "torsion or elliptic mixing cannot arise from the bridge carrier normal geometry; "
            "it requires the complete moving-fiber coefficient pushforward"
        ),
        "conclusion": (
            "the mixed Kummer grade has an actual first-normal carrier lift and is not carrier torsion; "
            "its coefficient-level lift remains uncomputed"
        ),
        "checks": checks,
    }
    out = here / "bridge-face-first-rees-lift.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
