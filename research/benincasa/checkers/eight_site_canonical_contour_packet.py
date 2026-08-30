"""Freeze the complete source-normalized C8 canonical contour presentation."""

import itertools
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "eight-site-canonical-contour-packet.json"
N = 8


def region_label(sites: set[int]) -> str:
    return "g_" + "".join(str(site + 1) for site in sorted(sites))


def main() -> None:
    coordinate_order = [*[f"X{site + 1}" for site in range(N)], *[f"y{edge + 1}" for edge in range(N)]]
    vertices = []
    for edge in range(N):
        right_site = (edge + 1) % N
        for vertex_type, (left, right, edge_value) in enumerate(
            [(1, 1, -1), (1, -1, 1), (-1, 1, 1)], start=1
        ):
            column = [0] * (2 * N)
            column[edge] = left
            column[right_site] = right
            column[N + edge] = edge_value
            vertices.append({
                "contour_variable": f"c_{edge + 1}_{vertex_type}",
                "edge": edge + 1,
                "vertex_type": vertex_type,
                "column": column,
                "regulator": f"epsilon_{edge + 1}_{vertex_type}",
                "regulator_condition": "strictly_positive",
            })

    facets = []
    for length in range(1, N):
        for start in range(N):
            sites = {(start + offset) % N for offset in range(length)}
            row = [0] * (2 * N)
            for site in sites:
                row[site] = 1
            for edge in range(N):
                if (edge in sites) != ((edge + 1) % N in sites):
                    row[N + edge] = 1
            facets.append({"label": region_label(sites), "kind": "connected_region", "row": row})
    for edge in range(N):
        row = [1] * N + [0] * N
        row[N + edge] = 2
        facets.append({
            "label": f"G_minus_e{edge + 1}{(edge + 1) % N + 1}",
            "kind": "spanning_connected_subgraph",
            "row": row,
        })
    facets.append({"label": "G", "kind": "total_energy", "row": [1] * N + [0] * N})
    facets.sort(key=lambda item: item["label"])

    vertex_matrix = sp.Matrix.hstack(*(sp.Matrix(item["column"]) for item in vertices))
    pivot_columns = list(vertex_matrix.rref()[1])
    assert len(pivot_columns) == 16
    localization_columns = pivot_columns[:16]
    localization_matrix = vertex_matrix[:, localization_columns]
    localization_determinant = int(localization_matrix.det())
    unfixed_columns = [index for index in range(24) if index not in localization_columns]
    unfixed_matrix = vertex_matrix[:, unfixed_columns]
    inverse = localization_matrix.inv()
    localized_y_coefficients = inverse
    localized_unfixed_coefficients = -inverse * unfixed_matrix
    localized_denominators = []
    for row_index, column_index in enumerate(localization_columns):
        localized_denominators.append({
            "contour_variable": vertices[column_index]["contour_variable"],
            "Y_coefficients": [str(value) for value in localized_y_coefficients.row(row_index)],
            "unfixed_coefficients": [str(value) for value in localized_unfixed_coefficients.row(row_index)],
            "constant_term": "0",
            "imaginary_shift": f"-i*{vertices[column_index]['regulator']}",
        })

    for facet in facets:
        values = [
            sum(left * right for left, right in zip(facet["row"], vertex["column"]))
            for vertex in vertices
        ]
        assert min(values) >= 0
        facet["vertex_pairings"] = values
        facet["zero_vertex_indices"] = [index for index, value in enumerate(values) if value == 0]

    denominator_degree = len(facets)
    projective_dimension = 15
    numerator_degree = denominator_degree - (projective_dimension + 1)
    checks = {
        "coordinate_count": len(coordinate_order),
        "vertex_count": len(vertices),
        "vertex_rank": vertex_matrix.rank(),
        "facet_count": len(facets),
        "connected_region_facet_count": sum(item["kind"] == "connected_region" for item in facets),
        "spanning_facet_count": sum(item["kind"] == "spanning_connected_subgraph" for item in facets),
        "total_energy_facet_count": sum(item["kind"] == "total_energy" for item in facets),
        "localization_basis_size": len(localization_columns),
        "localization_determinant": localization_determinant,
        "unfixed_contour_dimension": len(unfixed_columns),
        "canonical_denominator_degree": denominator_degree,
        "canonical_numerator_degree": numerator_degree,
        "all_facet_vertex_pairings_nonnegative": all(
            min(item["vertex_pairings"]) >= 0 for item in facets
        ),
    }
    assert checks == {
        "coordinate_count": 16,
        "vertex_count": 24,
        "vertex_rank": 16,
        "facet_count": 65,
        "connected_region_facet_count": 56,
        "spanning_facet_count": 8,
        "total_energy_facet_count": 1,
        "localization_basis_size": 16,
        "localization_determinant": localization_determinant,
        "unfixed_contour_dimension": 8,
        "canonical_denominator_degree": 65,
        "canonical_numerator_degree": 49,
        "all_facet_vertex_pairings_nonnegative": True,
    }
    assert localization_determinant != 0

    packet = {
        "schema": "marici.eight_site_canonical_contour_packet.v1",
        "primary_source": {
            "paper": "arXiv:2305.19686v2",
            "equations": ["3.8", "3.9", "3.10", "3.11", "4.1", "4.2", "4.3"],
        },
        "ambient_orientation": coordinate_order,
        "contour_orientation": [item["contour_variable"] for item in vertices],
        "vertices": vertices,
        "facets": facets,
        "normalization": {
            "exact": "1/(15!*(2*pi*i)^8)",
            "factorial": math.factorial(15),
            "remaining_contour_power": 8,
        },
        "localization_basis": {
            "column_indices_zero_based": localization_columns,
            "contour_variables": [vertices[index]["contour_variable"] for index in localization_columns],
            "jacobian_determinant": localization_determinant,
            "absolute_jacobian": abs(localization_determinant),
            "unfixed_column_indices_zero_based": unfixed_columns,
            "unfixed_contour_variables": [vertices[index]["contour_variable"] for index in unfixed_columns],
            "localized_denominators": localized_denominators,
            "localized_integrand": "|det(Z_basis)|^-1 * product(dc_u/(c_u-i*epsilon_u)) * product(1/(c_hat(Y,c_u)-i*epsilon_hat))",
        },
        "canonical_numerator": {
            "status": "exact_implicit_pushforward_definition",
            "degree": numerator_degree,
            "definition": "N_C8(Y)=(product over the 65 source facet forms q_f(Y))*Omega_C8(Y), where Omega_C8 is the oriented 24-variable contour pushforward fixed by this packet",
            "expanded_polynomial_claimed": False,
            "uniqueness_basis": "unique unit-normalized canonical form with logarithmic poles only on the 65 frozen facets",
        },
        "checks": checks,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
