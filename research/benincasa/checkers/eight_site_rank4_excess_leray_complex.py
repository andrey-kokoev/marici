"""Construct the source-derived excess Leray/Koszul complex for all C8 occurrences."""

import collections
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
ATTACHMENTS = ROOT / "results" / "eight-site-rank4-circuit-attachment-graph.json"
UNIVERSAL = ROOT / "results" / "eight-site-rank4-universal-jacobian.json"
TARGET = ROOT / "results" / "eight-site-rank4-excess-leray-complex.json"
N = 8


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    values = [sp.Rational(value) for value in vector]
    denominator = sp.ilcm(*(value.q for value in values))
    integers = [int(value * denominator) for value in values]
    gcd = sp.igcd(*(abs(value) for value in integers if value))
    integers = [value // gcd for value in integers]
    if next(value for value in integers if value) < 0:
        integers = [-value for value in integers]
    return integers


def independent_rows(matrix: sp.Matrix) -> list[int]:
    selected = []
    rank = 0
    for row in range(matrix.rows):
        trial = matrix[selected + [row], :]
        if trial.rank() > rank:
            selected.append(row)
            rank += 1
    return selected


def main() -> None:
    source = json.loads(SOURCE.read_text())
    attachment = json.loads(ATTACHMENTS.read_text())
    universal = json.loads(UNIVERSAL.read_text())
    universal_by_key = {item["canonical_key"]: item for item in universal["classes"]}
    occurrence_component = {
        occurrence_id: component_index
        for component_index, component in enumerate(attachment["components"])
        for occurrence_id in component["occurrence_ids"]
    }
    x_symbols = sp.symbols("X1:9")
    audits = []
    orientation_distribution = collections.Counter()

    for occurrence in source["occurrences"]:
        y_matrix = sp.Matrix(occurrence["y_normal_matrix"])
        x_matrix = sp.Matrix(occurrence["x_coefficient_matrix"])
        full_matrix = x_matrix.row_join(y_matrix)
        kernel_basis = [primitive_integer_vector(vector) for vector in y_matrix.T.nullspace()]
        circuit_basis = sp.Matrix.hstack(*(sp.Matrix(vector) for vector in kernel_basis)).T
        base_matrix = circuit_basis * x_matrix
        assert circuit_basis * y_matrix == sp.zeros(3, 8)
        assert base_matrix.rank() == 3
        assert full_matrix.rank() == 7

        selected_columns = list(full_matrix.rref()[1])
        square_minor = full_matrix[:, selected_columns]
        orientation = int(square_minor.det())
        assert orientation != 0
        orientation_distribution[str(orientation)] += 1

        source_base_match = None
        legacy_record = universal_by_key[occurrence["source_orbit_key"]]
        if set(occurrence["labels"]) == set(legacy_record["labels"]):
            expected = legacy_record["base_relations"]
            expected_matrix = sp.Matrix([
                [int(sp.expand(sp.sympify(expression, locals={str(symbol): symbol for symbol in x_symbols})).coeff(symbol)) for symbol in x_symbols]
                for expression in expected
            ])
            source_base_match = (
                base_matrix.col_join(expected_matrix).rank()
                == base_matrix.rank()
                == expected_matrix.rank()
                == 3
            )

        audits.append({
            "occurrence_id": occurrence["occurrence_id"],
            "source_orbit_key": occurrence["source_orbit_key"],
            "cyclic_shift": occurrence["cyclic_shift"],
            "attachment_component": occurrence_component[occurrence["occurrence_id"]],
            "label_order": occurrence["labels"],
            "full_normal_coordinate_order": [*[f"X{i + 1}" for i in range(N)], *[f"y{i + 1}" for i in range(N)]],
            "full_normal_matrix": [[int(value) for value in row] for row in full_matrix.tolist()],
            "full_normal_rank": full_matrix.rank(),
            "routing_normal_rank": y_matrix.rank(),
            "excess_rank": len(kernel_basis),
            "labelled_circuit_basis": kernel_basis,
            "external_base_relation_matrix": [[int(value) for value in row] for row in base_matrix.tolist()],
            "source_base_rowspace_match": source_base_match,
            "transverse_minor_columns_zero_based": selected_columns,
            "transverse_minor_determinant": orientation,
            "leray_torus": {
                "rank": 7,
                "orientation": "dlog(q_1) wedge ... wedge dlog(q_7) in retained label order",
                "boundary_value": "q_a -> q_a-i*(N_X epsilon_X+N_y epsilon_y)_a",
            },
            "excess_koszul_complex": {
                "ring": "Q[X1,...,X8] localized away from excluded carrier factors",
                "differential": "contraction by the three serialized external base relations",
                "chain_ranks": [1, 3, 3, 1],
                "base_specialization_differential": "zero",
                "associated_grade": "Lambda^bullet(K_circuit)",
            },
        })

    checks = {
        "occurrence_count": len(audits),
        "all_full_normal_ranks_seven": all(item["full_normal_rank"] == 7 for item in audits),
        "all_routing_normal_ranks_four": all(item["routing_normal_rank"] == 4 for item in audits),
        "all_excess_ranks_three": all(item["excess_rank"] == 3 for item in audits),
        "source_representative_base_rowspace_match_count": sum(
            item["source_base_rowspace_match"] is True for item in audits
        ),
        "source_representative_base_rowspace_mismatch_count": sum(
            item["source_base_rowspace_match"] is False for item in audits
        ),
        "attachment_component_occurrence_counts": dict(sorted(collections.Counter(item["attachment_component"] for item in audits).items())),
        "transverse_minor_determinant_distribution": dict(sorted(orientation_distribution.items())),
        "generic_leray_torus_rank": 7,
        "excess_koszul_chain_ranks": [1, 3, 3, 1],
        "associated_grade_total_rank": 8,
    }
    assert checks["occurrence_count"] == 288
    assert checks["all_full_normal_ranks_seven"]
    assert checks["all_routing_normal_ranks_four"]
    assert checks["all_excess_ranks_three"]
    assert checks["source_representative_base_rowspace_match_count"] == 36
    assert checks["source_representative_base_rowspace_mismatch_count"] == 0
    assert checks["attachment_component_occurrence_counts"] == {0: 144, 1: 144}

    packet = {
        "schema": "marici.eight_site_rank4_excess_leray_complex.v1",
        "typing": {
            "generic_object": "rank-seven transverse labelled Leray torus in full (X,y) normal space",
            "specialized_object": "derived pullback to the rank-three external base ideal",
            "excess_object": "four-term Koszul complex with associated grade Lambda^bullet(K_circuit)",
            "physical_status": "source-derived local complex; global fold pairing not yet computed",
        },
        "checks": checks,
        "occurrences": audits,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
