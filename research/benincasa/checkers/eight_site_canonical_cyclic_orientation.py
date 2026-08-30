"""Freeze the labelled C8 cyclic action and its orientation characters."""

import collections
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "eight-site-canonical-contour-packet.json"
TRIANGULATION = ROOT / "results" / "eight-site-canonical-regular-triangulation.json"
TARGET = ROOT / "results" / "eight-site-canonical-cyclic-orientation.json"


def permutation_sign(permutation: list[int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def rotate_vertex(index: int, shift: int = 1) -> int:
    edge, vertex_type = divmod(index, 3)
    return ((edge + shift) % 8) * 3 + vertex_type


def rotate_coordinate(index: int, shift: int = 1) -> int:
    block, position = divmod(index, 8)
    return block * 8 + (position + shift) % 8


def main() -> None:
    contour = json.loads(CONTOUR.read_text())
    triangulation = json.loads(TRIANGULATION.read_text())
    vertex_permutation = [rotate_vertex(index) for index in range(24)]
    coordinate_permutation = [rotate_coordinate(index) for index in range(16)]
    contour_sign = permutation_sign(vertex_permutation)
    ambient_sign = permutation_sign(coordinate_permutation)

    vertices = [item["column"] for item in contour["vertices"]]
    rotated_cell_records = []
    determinant_ratio_distribution = collections.Counter()
    for cell in triangulation["cells"]:
        original = cell["vertex_indices"]
        transported_order = [rotate_vertex(index) for index in original]
        lexical_order = sorted(transported_order)
        sorting_permutation = [transported_order.index(index) for index in lexical_order]
        sorting_sign = permutation_sign(sorting_permutation)
        matrix = sp.Matrix.hstack(*(sp.Matrix(vertices[index]) for index in lexical_order))
        rotated_determinant = int(matrix.det())
        ratio = sp.Rational(rotated_determinant, cell["projective_determinant"])
        assert ratio in (-1, 1)
        assert int(ratio) == sorting_sign * ambient_sign
        determinant_ratio_distribution[str(int(ratio))] += 1
        rotated_cell_records.append({
            "source_vertex_indices": original,
            "transported_vertex_order": transported_order,
            "lexical_vertex_order": lexical_order,
            "lexical_sorting_sign": sorting_sign,
            "source_determinant": cell["projective_determinant"],
            "rotated_lexical_determinant": rotated_determinant,
            "determinant_ratio": str(ratio),
        })

    checks = {
        "ambient_coordinate_permutation_sign": ambient_sign,
        "contour_variable_permutation_sign": contour_sign,
        "integration_cycle_orientation_transport_sign": contour_sign,
        "contour_form_times_cycle_sign": contour_sign * contour_sign,
        "projective_measure_sign": ambient_sign,
        "canonical_scalar_cyclic_character": ambient_sign * contour_sign * contour_sign,
        "rotated_cell_count": len(rotated_cell_records),
        "determinant_ratio_distribution_after_lexical_sort": dict(sorted(determinant_ratio_distribution.items())),
        "all_rotated_cells_nondegenerate": all(item["rotated_lexical_determinant"] != 0 for item in rotated_cell_records),
    }
    assert checks["ambient_coordinate_permutation_sign"] == 1
    assert checks["contour_variable_permutation_sign"] == -1
    assert checks["contour_form_times_cycle_sign"] == 1
    assert checks["canonical_scalar_cyclic_character"] == 1
    assert checks["rotated_cell_count"] == 255
    assert checks["all_rotated_cells_nondegenerate"]

    packet = {
        "schema": "marici.eight_site_canonical_cyclic_orientation.v1",
        "vertex_permutation_one_step_zero_based": vertex_permutation,
        "coordinate_permutation_one_step_zero_based": coordinate_permutation,
        "orientation_convention": {
            "ambient": contour["ambient_orientation"],
            "contour": contour["contour_orientation"],
            "rule": "transport in source order; lexical reserialization contributes the displayed sorting sign",
        },
        "checks": checks,
        "rotated_cells": rotated_cell_records,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
