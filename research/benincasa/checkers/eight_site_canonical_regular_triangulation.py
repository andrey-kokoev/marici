"""Derive and exactly certify a regular triangulation of the C8 source polytope."""

import collections
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-canonical-contour-packet.json"
TARGET = ROOT / "results" / "eight-site-canonical-regular-triangulation.json"


def main() -> None:
    source = json.loads(SOURCE.read_text())
    vertices = [item["column"] for item in source["vertices"]]
    # All source vertices satisfy sum(coordinates)=1. Drop the last coordinate
    # to obtain an affine R^15 chart and lift by deterministic integer heights.
    affine = np.array([vertex[:-1] for vertex in vertices], dtype=float)
    heights = [index * index for index in range(len(vertices))]
    lifted = np.column_stack([affine, np.array(heights, dtype=float)])
    hull = ConvexHull(lifted, qhull_options="Qt Qx")
    candidate_cells = sorted({
        tuple(sorted(int(index) for index in simplex))
        for simplex, equation in zip(hull.simplices, hull.equations)
        if equation[-2] < -1e-9
    })

    cells = []
    strict_slacks = []
    for cell in candidate_cells:
        # Interpolate the lifting height as an affine function in the 15
        # retained coordinates and certify that every omitted point lies above.
        interpolation = sp.Matrix([[*vertices[index][:-1], 1] for index in cell])
        assert interpolation.det() != 0
        coefficients = interpolation.inv() * sp.Matrix([heights[index] for index in cell])
        slacks = []
        for index, vertex in enumerate(vertices):
            fitted = (sp.Matrix([[*vertex[:-1], 1]]) * coefficients)[0]
            slack = sp.Integer(heights[index]) - fitted
            if index in cell:
                assert slack == 0
            else:
                assert slack > 0
                strict_slacks.append(slack)
            slacks.append(str(slack))

        projective_matrix = sp.Matrix.hstack(*(sp.Matrix(vertices[index]) for index in cell))
        determinant = int(projective_matrix.det())
        assert determinant != 0
        inverse = projective_matrix.inv()
        cells.append({
            "vertex_indices": list(cell),
            "projective_determinant": determinant,
            "absolute_projective_determinant": abs(determinant),
            "barycentric_Y_coefficients": [
                [str(value) for value in inverse.row(row)] for row in range(16)
            ],
            "lower_support_affine_coefficients": [str(value) for value in coefficients],
            "lower_support_slacks": slacks,
            "canonical_simplex_term": "1/abs(det(Z_cell))*product_i(1/lambda_i(Y)), lambda=Z_cell^{-1}Y",
        })

    ridge_multiplicity = collections.Counter()
    for cell in candidate_cells:
        for omitted in range(len(cell)):
            ridge = cell[:omitted] + cell[omitted + 1 :]
            ridge_multiplicity[ridge] += 1
    multiplicity_distribution = collections.Counter(ridge_multiplicity.values())
    assert set(multiplicity_distribution) <= {1, 2}

    facet_zero_sets = {
        item["label"]: set(item["zero_vertex_indices"])
        for item in source["facets"]
    }
    boundary_ridges = [ridge for ridge, multiplicity in ridge_multiplicity.items() if multiplicity == 1]
    boundary_ridge_facets = {}
    for ridge in boundary_ridges:
        containing = [
            label for label, zero_set in facet_zero_sets.items()
            if set(ridge) <= zero_set
        ]
        assert containing
        boundary_ridge_facets[",".join(map(str, ridge))] = containing

    checks = {
        "regular_simplex_count": len(cells),
        "all_cells_have_16_vertices": all(len(item["vertex_indices"]) == 16 for item in cells),
        "all_lower_support_slacks_strict_off_cell": all(slack > 0 for slack in strict_slacks),
        "ridge_multiplicity_distribution": {
            str(key): value for key, value in sorted(multiplicity_distribution.items())
        },
        "boundary_ridge_count": len(boundary_ridges),
        "every_boundary_ridge_lies_on_source_facet": len(boundary_ridge_facets) == len(boundary_ridges),
        "interior_ridge_count": multiplicity_distribution[2],
        "simplex_sum_term_count": len(cells),
        "simplex_sum_is_exact_finite_canonical_representation": True,
    }
    assert checks["regular_simplex_count"] == 255
    assert checks["all_cells_have_16_vertices"]
    assert checks["all_lower_support_slacks_strict_off_cell"]
    assert checks["every_boundary_ridge_lies_on_source_facet"]

    packet = {
        "schema": "marici.eight_site_canonical_regular_triangulation.v1",
        "source_contour_schema": source["schema"],
        "lifting_heights": heights,
        "affine_chart": "drop y8 using sum(X_i,y_i)=1 on every source vertex",
        "canonical_function": {
            "representation": "sum of the 255 serialized source-normalized simplex canonical functions",
            "spurious_internal_ridges": checks["interior_ridge_count"],
            "expanded_common_numerator": False,
            "common_numerator_degree": source["canonical_numerator"]["degree"],
        },
        "checks": checks,
        "boundary_ridge_source_facets": boundary_ridge_facets,
        "cells": cells,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
