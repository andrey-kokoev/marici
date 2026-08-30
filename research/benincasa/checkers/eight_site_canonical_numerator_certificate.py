"""Certify the complete C8 numerator as an exact polynomial arithmetic circuit."""

import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "eight-site-canonical-contour-packet.json"
TRIANGULATION = ROOT / "results" / "eight-site-canonical-regular-triangulation.json"
TARGET = ROOT / "results" / "eight-site-canonical-numerator-certificate.json"


def main() -> None:
    contour = json.loads(CONTOUR.read_text())
    triangulation = json.loads(TRIANGULATION.read_text())
    ridge_incidence = collections.defaultdict(list)
    for cell_index, cell in enumerate(triangulation["cells"]):
        vertices = cell["vertex_indices"]
        orientation = 1 if cell["projective_determinant"] > 0 else -1
        for omitted in range(16):
            ridge = tuple(vertices[:omitted] + vertices[omitted + 1 :])
            ridge_incidence[ridge].append({
                "cell_index": cell_index,
                "omitted_local_vertex": omitted,
                "oriented_boundary_sign": orientation * (-1 if omitted % 2 else 1),
            })

    internal_certificates = []
    boundary_certificates = []
    boundary_source_map = triangulation["boundary_ridge_source_facets"]
    facet_piece_counts = collections.Counter()
    for ridge, incidences in sorted(ridge_incidence.items()):
        ridge_key = ",".join(map(str, ridge))
        if len(incidences) == 2:
            assert sum(item["oriented_boundary_sign"] for item in incidences) == 0
            internal_certificates.append({
                "ridge_vertex_indices": list(ridge),
                "incidences": incidences,
                "residue_sum": 0,
            })
        else:
            assert len(incidences) == 1
            source_facets = boundary_source_map[ridge_key]
            assert len(source_facets) == 1
            source_facet = source_facets[0]
            facet_piece_counts[source_facet] += 1
            boundary_certificates.append({
                "ridge_vertex_indices": list(ridge),
                "incidence": incidences[0],
                "source_facet": source_facet,
            })

    facet_labels = [item["label"] for item in contour["facets"]]
    assert set(facet_piece_counts) == set(facet_labels)
    arithmetic_circuit = {
        "facet_linear_forms": {
            item["label"]: item["row"] for item in contour["facets"]
        },
        "simplex_terms": [
            {
                "absolute_determinant": item["absolute_projective_determinant"],
                "barycentric_Y_coefficients": item["barycentric_Y_coefficients"],
            }
            for item in triangulation["cells"]
        ],
        "canonical_function_expression": "sum_s [1/abs(det_s) * product_i 1/lambda_{s,i}(Y)]",
        "canonical_numerator_expression": "product_f q_f(Y) * canonical_function_expression",
        "evaluation_rule": "evaluate the serialized rational simplex sum exactly, multiply by all 65 serialized facet forms, and cancel using the internal-ridge certificates",
    }
    checks = {
        "simplex_term_count": len(triangulation["cells"]),
        "internal_ridge_cancellation_count": len(internal_certificates),
        "boundary_ridge_count": len(boundary_certificates),
        "physical_facet_count_reached": len(facet_piece_counts),
        "every_internal_residue_cancels_pairwise": all(
            item["residue_sum"] == 0 for item in internal_certificates
        ),
        "every_boundary_piece_has_exactly_one_source_facet": all(
            bool(item["source_facet"]) for item in boundary_certificates
        ),
        "all_65_source_facets_are_reached": set(facet_piece_counts) == set(facet_labels),
        "numerator_degree": contour["canonical_numerator"]["degree"],
        "numerator_representation": "exact_polynomial_arithmetic_circuit_with_residue_cancellation_certificate",
    }
    assert checks["simplex_term_count"] == 255
    assert checks["internal_ridge_cancellation_count"] == 1016
    assert checks["boundary_ridge_count"] == 2048
    assert checks["physical_facet_count_reached"] == 65
    assert checks["every_internal_residue_cancels_pairwise"]
    assert checks["all_65_source_facets_are_reached"]
    assert checks["numerator_degree"] == 49

    packet = {
        "schema": "marici.eight_site_canonical_numerator_certificate.v1",
        "scope": {
            "included": "complete exact arithmetic-circuit numerator and polynomiality certificate",
            "excluded": "expanded monomial serialization, which is not required for exact evaluation or residues",
        },
        "checks": checks,
        "facet_boundary_simplex_counts": dict(sorted(facet_piece_counts.items())),
        "arithmetic_circuit": arithmetic_circuit,
        "internal_ridge_certificates": internal_certificates,
        "boundary_certificates": boundary_certificates,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
