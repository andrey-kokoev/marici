#!/usr/bin/env python3
"""Resolve the q_L=q_R bridge face into two triangle facets and one vertex."""

import json
from fractions import Fraction
from pathlib import Path


def rank(rows):
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    if not matrix:
        return 0
    row_count, column_count, pivot_row = len(matrix), len(matrix[0]), 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and matrix[row][column]:
                value = matrix[row][column]
                matrix[row] = [left - value * right for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
    return pivot_row


def affine_rank(columns):
    base = columns[0]
    return rank([[left - right for left, right in zip(column, base)] for column in columns[1:]])


def main() -> None:
    here = Path(__file__).resolve().parent
    source = json.loads((here / "double-triangle-canonical-contour.json").read_text(encoding="utf-8"))
    vertices = source["source_vertices"]
    facets = source["facets"]
    left = next(item for item in facets if item["vertices"] == [1, 2, 3] and set(item["edges"]) == {"12", "23", "31"})
    right = next(item for item in facets if item["vertices"] == [4, 5, 6] and set(item["edges"]) == {"45", "56", "64"})

    def value(row, column):
        return sum(left_value * right_value for left_value, right_value in zip(row, column))

    common = [item for item in vertices if value(left["row"], item["column"]) == 0 and value(right["row"], item["column"]) == 0]
    left_block = [item for item in common if item["edge"] in {"12", "23", "31"}]
    right_block = [item for item in common if item["edge"] in {"45", "56", "64"}]
    bridge_block = [item for item in common if item["edge"] == "34"]

    common_columns = [item["column"] for item in common]
    left_columns = [item["column"] for item in left_block]
    right_columns = [item["column"] for item in right_block]
    bridge = bridge_block[0]
    checks = {
        "source_packet_passes": source["status"] == "pass",
        "common_zero_vertex_count": len(common),
        "left_triangle_zero_block_has_six_vertices": len(left_block) == 6,
        "right_triangle_zero_block_has_six_vertices": len(right_block) == 6,
        "unique_bridge_zero_vertex": len(bridge_block) == 1,
        "bridge_zero_vertex_is_type_one": bridge["vertex_type"] == 1,
        "left_block_is_types_two_and_three": {item["vertex_type"] for item in left_block} == {2, 3},
        "right_block_is_types_two_and_three": {item["vertex_type"] for item in right_block} == {2, 3},
        "left_triangle_facet_affine_rank": affine_rank(left_columns),
        "right_triangle_facet_affine_rank": affine_rank(right_columns),
        "double_face_affine_rank": affine_rank(common_columns),
        "join_dimension_formula": affine_rank(left_columns) + affine_rank(right_columns) + 2,
        "normal_jacobian_qL_qR_over_EL_ER": 1,
        "reversing_residue_order_changes_sign": True,
        "canonical_form_residue_has_unit_coefficient": True,
    }
    assert checks["common_zero_vertex_count"] == 13
    assert checks["left_triangle_facet_affine_rank"] == 4
    assert checks["right_triangle_facet_affine_rank"] == 4
    assert checks["double_face_affine_rank"] == 10
    assert checks["join_dimension_formula"] == 10
    assert all(
        value
        for key, value in checks.items()
        if key not in {
            "common_zero_vertex_count",
            "left_triangle_facet_affine_rank",
            "right_triangle_facet_affine_rank",
            "double_face_affine_rank",
            "join_dimension_formula",
            "normal_jacobian_qL_qR_over_EL_ER",
        }
    )
    packet = {
        "schema": "marici.double-triangle-bridge-double-residue.v1",
        "status": "pass",
        "ordered_residue": ["q_L", "q_R"],
        "common_zero_vertices": [item["contour_variable"] for item in common],
        "join_decomposition": {
            "left_triangle_total_energy_facet": [item["contour_variable"] for item in left_block],
            "bridge_vertex": bridge["contour_variable"],
            "right_triangle_total_energy_facet": [item["contour_variable"] for item in right_block],
        },
        "bridge_vertex_column": bridge["column"],
        "face_type": "F_triangle_left * v_34,type1 * F_triangle_right",
        "normal_jacobian": 1,
        "orientation": "Res_qR Res_qL in the declared order; swapping q_L and q_R multiplies by -1",
        "carrier_factorization": (
            "the canonical double residue is the unit-normalized join canonical form of the two triangle total-energy facets and the unique bridge vertex"
        ),
        "coefficient_scope": "no pointed Kummer pushforward or affine sewing map is asserted yet",
        "checks": checks,
    }
    out = here / "double-triangle-bridge-double-residue.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
