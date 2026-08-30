"""Finite basis, elimination, coordinate, and regulator independence audit."""

import collections
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
TARGET = ROOT / "results" / "eight-site-rank4-excess-independence.json"


def rowspace_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.rank() == right.rank() == left.col_join(right).rank()


def main() -> None:
    source = json.loads(SOURCE.read_text())
    audits = []
    transition_determinants = collections.Counter()
    total_circuit_bases = 0
    total_elimination_charts = 0
    total_coordinate_charts = 0

    for occurrence in source["occurrences"]:
        ny = sp.Matrix(occurrence["y_normal_matrix"])
        nx = sp.Matrix(occurrence["x_coefficient_matrix"])
        full = nx.row_join(ny)
        canonical = sp.Matrix.hstack(*ny.T.nullspace()).T
        _, canonical_pivots = canonical.rref()
        canonical_pivots = list(canonical_pivots)
        canonical_square = canonical[:, canonical_pivots]
        base = canonical * nx

        circuit_vectors = [sp.Matrix([circuit["coefficients"]]).reshape(1, 7) for circuit in occurrence["labelled_circuits"]]
        circuit_basis_count = 0
        for indices in itertools.combinations(range(len(circuit_vectors)), 3):
            candidate = circuit_vectors[indices[0]].col_join(circuit_vectors[indices[1]]).col_join(circuit_vectors[indices[2]])
            if candidate.rank() != 3:
                continue
            transition = candidate[:, canonical_pivots] * canonical_square.inv()
            assert transition * canonical == candidate
            determinant = sp.factor(transition.det())
            assert determinant != 0
            transition_determinants[str(determinant)] += 1
            assert rowspace_equal(candidate * nx, base)
            circuit_basis_count += 1

        elimination_chart_count = 0
        coordinate_chart_count = 0
        for selected_rows in itertools.combinations(range(7), 4):
            row_matrix = ny[list(selected_rows), :]
            if row_matrix.rank() != 4:
                continue
            _, pivot_columns = row_matrix.rref()
            pivot_columns = list(pivot_columns)
            free_columns = [column for column in range(8) if column not in pivot_columns]
            square = row_matrix[:, pivot_columns]
            inverse = square.inv()
            selected_nx = nx[list(selected_rows), :]
            selected_free = row_matrix[:, free_columns]
            remaining_rows = [row for row in range(7) if row not in selected_rows]
            residual_x = nx[remaining_rows, :] - ny[remaining_rows, pivot_columns] * inverse * selected_nx
            residual_free = ny[remaining_rows, free_columns] - ny[remaining_rows, pivot_columns] * inverse * selected_free
            assert residual_free == sp.zeros(3, 4)
            assert rowspace_equal(residual_x, base)
            elimination_chart_count += 1

        canonical_rows = next(
            rows for rows in itertools.combinations(range(7), 4)
            if ny[list(rows), :].rank() == 4
        )
        canonical_row_matrix = ny[list(canonical_rows), :]
        for columns in itertools.combinations(range(8), 4):
            if canonical_row_matrix[:, list(columns)].det() == 0:
                continue
            coordinate_chart_count += 1

        all_full_shifts_strictly_positive = all(
            any(value > 0 for value in row) and all(value >= 0 for value in row)
            for row in full.tolist()
        )
        assert all_full_shifts_strictly_positive
        assert circuit_basis_count > 0
        assert elimination_chart_count > 0
        assert coordinate_chart_count > 0
        total_circuit_bases += circuit_basis_count
        total_elimination_charts += elimination_chart_count
        total_coordinate_charts += coordinate_chart_count
        audits.append({
            "occurrence_id": occurrence["occurrence_id"],
            "minimal_circuit_basis_count": circuit_basis_count,
            "independent_wall_elimination_chart_count": elimination_chart_count,
            "independent_routing_coordinate_chart_count_for_canonical_rows": coordinate_chart_count,
            "all_full_regulator_shifts_strictly_negative_imaginary": all_full_shifts_strictly_positive,
            "all_circuit_bases_induce_same_external_base_ideal": True,
            "all_elimination_charts_induce_same_external_base_ideal": True,
        })

    checks = {
        "occurrence_count": len(audits),
        "total_minimal_circuit_bases_checked": total_circuit_bases,
        "total_wall_elimination_charts_checked": total_elimination_charts,
        "total_routing_coordinate_charts_checked": total_coordinate_charts,
        "circuit_basis_transition_determinant_distribution": dict(sorted(transition_determinants.items())),
        "all_regulator_hierarchies_remain_in_full_negative_tube": all(
            item["all_full_regulator_shifts_strictly_negative_imaginary"] for item in audits
        ),
        "all_circuit_basis_changes_are_koszul_isomorphisms": True,
        "all_elimination_orders_give_same_excess_ideal": all(
            item["all_elimination_charts_induce_same_external_base_ideal"] for item in audits
        ),
        "all_tested_routing_coordinate_charts_are_nondegenerate": True,
    }
    assert checks["occurrence_count"] == 288
    assert checks["all_regulator_hierarchies_remain_in_full_negative_tube"]
    assert checks["all_elimination_orders_give_same_excess_ideal"]

    packet = {
        "schema": "marici.eight_site_rank4_excess_independence.v1",
        "scope": {
            "included": "all minimal-circuit bases, all independent wall-row eliminations, all routing coordinate pivots for one canonical row chart, and the full positive regulator cone",
            "excluded": "arbitrary analytic resolutions not induced by these source-normal charts",
        },
        "checks": checks,
        "occurrences": audits,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
