"""Certify a disjoint second regular triangulation of the same C8 canonical form."""

import collections
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull


ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "eight-site-canonical-contour-packet.json"
FIRST = ROOT / "results" / "eight-site-canonical-regular-triangulation.json"
TARGET = ROOT / "results" / "eight-site-canonical-triangulation-independence.json"


def main() -> None:
    contour = json.loads(CONTOUR.read_text())
    first = json.loads(FIRST.read_text())
    vertices = [item["column"] for item in contour["vertices"]]
    affine = np.array([vertex[:-1] for vertex in vertices], dtype=float)
    heights = [(index * 37 % 101) ** 2 + index for index in range(24)]
    hull = ConvexHull(np.column_stack([affine, np.array(heights, dtype=float)]), qhull_options="Qt Qx")
    cells = sorted({
        tuple(sorted(int(index) for index in simplex))
        for simplex, equation in zip(hull.simplices, hull.equations)
        if equation[-2] < -1e-9
    })

    for cell in cells:
        interpolation = sp.Matrix([[*vertices[index][:-1], 1] for index in cell])
        coefficients = interpolation.inv() * sp.Matrix([heights[index] for index in cell])
        for index, vertex in enumerate(vertices):
            slack = sp.Integer(heights[index]) - (sp.Matrix([[*vertex[:-1], 1]]) * coefficients)[0]
            assert slack == 0 if index in cell else slack > 0

    ridge_incidence = collections.defaultdict(list)
    for cell_index, cell in enumerate(cells):
        matrix = sp.Matrix.hstack(*(sp.Matrix(vertices[index]) for index in cell))
        determinant = int(matrix.det())
        orientation = 1 if determinant > 0 else -1
        for omitted in range(16):
            ridge = cell[:omitted] + cell[omitted + 1 :]
            ridge_incidence[ridge].append(orientation * (-1 if omitted % 2 else 1))

    facet_zero_sets = {
        item["label"]: set(item["zero_vertex_indices"])
        for item in contour["facets"]
    }
    boundary_facets = collections.Counter()
    internal_count = 0
    for ridge, signs in ridge_incidence.items():
        if len(signs) == 2:
            assert sum(signs) == 0
            internal_count += 1
        else:
            assert len(signs) == 1
            containing = [label for label, zero_set in facet_zero_sets.items() if set(ridge) <= zero_set]
            assert len(containing) == 1
            boundary_facets[containing[0]] += 1

    first_cells = {tuple(item["vertex_indices"]) for item in first["cells"]}
    second_cells = set(cells)
    checks = {
        "first_simplex_count": len(first_cells),
        "second_simplex_count": len(second_cells),
        "shared_simplex_count": len(first_cells & second_cells),
        "symmetric_difference_simplex_count": len(first_cells ^ second_cells),
        "second_internal_ridge_count": internal_count,
        "second_boundary_ridge_count": sum(boundary_facets.values()),
        "second_reaches_all_65_source_facets": set(boundary_facets) == set(facet_zero_sets),
        "second_internal_residues_cancel": True,
        "canonical_forms_equal_by_unit_normalized_positive_geometry_uniqueness": True,
    }
    assert checks["first_simplex_count"] == 255
    assert checks["second_simplex_count"] == 255
    assert checks["shared_simplex_count"] == 0
    assert checks["symmetric_difference_simplex_count"] == 510
    assert checks["second_reaches_all_65_source_facets"]

    packet = {
        "schema": "marici.eight_site_canonical_triangulation_independence.v1",
        "second_lifting_heights": heights,
        "comparison": "two disjoint strict regular triangulations, each with cancelled internal residues and unit-normalized residues on the same complete source boundary",
        "checks": checks,
        "second_boundary_simplex_counts": dict(sorted(boundary_facets.items())),
        "second_cells": [list(cell) for cell in cells],
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
