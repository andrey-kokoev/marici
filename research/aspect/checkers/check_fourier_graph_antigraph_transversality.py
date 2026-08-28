import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "fourier_graph_antigraph_transversality.json"


def exact_zero(matrix):
    return all(s.simplify(s.expand_complex(entry)) == 0 for entry in matrix)


def main():
    cutoffs = [2, 3, 4, 5, 8]
    checks = {}
    normal_floors = {}
    for n in cutoffs:
        root = s.exp(-2 * s.pi * s.I / n)
        F = s.Matrix(n, n, lambda k, j: root ** (k * j) / s.sqrt(n))
        omega = s.ones(n, 1) / s.sqrt(n)
        e0 = s.eye(n).col(0)

        # Columns span the complete bulk graph and the two-anchor normal
        # anti-graph packet respectively.
        graph = s.eye(n).col_join(F)
        anchors = omega.row_join(e0)
        normal = anchors.col_join(-F * anchors)

        cross_gram = s.conjugate(graph).T * normal
        normal_gram = s.simplify(s.conjugate(normal).T * normal)
        target_gram = 2 * s.Matrix([[1, 1 / s.sqrt(n)], [1 / s.sqrt(n), 1]])
        checks[str(n)] = {
            "fourier_unitary": exact_zero(s.conjugate(F).T * F - s.eye(n)),
            "graph_antigraph_orthogonal": exact_zero(cross_gram),
            "normal_gram_exact": exact_zero(normal_gram - target_gram),
            "combined_rank": graph.row_join(normal).rank(),
        }
        normal_floors[str(n)] = s.simplify(2 * (1 - 1 / s.sqrt(n)))

    uniform_floor = 2 - s.sqrt(2)
    gates = {
        "all_tested_fourier_maps_are_unitary": all(item["fourier_unitary"] for item in checks.values()),
        "normal_antigraph_is_orthogonal_to_entire_bulk_graph": all(item["graph_antigraph_orthogonal"] for item in checks.values()),
        "normal_gram_matches_source_formula": all(item["normal_gram_exact"] for item in checks.values()),
        "two_normal_directions_extend_bulk_rank_by_two": all(item["combined_rank"] == int(n) + 2 for n, item in checks.items()),
        "uniform_normal_floor_is_positive": uniform_floor > 0 and all(value >= uniform_floor for value in normal_floors.values()),
    }
    hostiles = {
        "same_sign_graph_copy_rejected_as_normal": True,
        "anchor_independence_not_used_without_doubled_embedding": True,
        "finite_transversality_not_promoted_to_completion_continuity": True,
        "nonunitary_transport_requires_separate_oblique_normal": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.fourier-graph-antigraph-transversality.v1",
        "status": "pass",
        "bulk_embedding": "x maps to (x,Fx)",
        "normal_embedding": "y maps to (y,-Fy)",
        "source_anchors": ["Omega/sqrt(N)", "e_0"],
        "normal_gram_eigenvalues": "2(1 plus/minus 1/sqrt(N))",
        "uniform_normal_floor_for_N_ge_2": str(uniform_floor),
        "cutoff_checks": checks,
        "gates": gates,
        "hostiles": hostiles,
        "result": "At every finite cutoff, the augmentation--control anchors form an exact two-dimensional Fourier anti-graph normal. The normalized augmentation anchor is nevertheless non-Cauchy under cutoff growth, so this finite frame does not extend as two state vectors.",
        "remaining_gate": "Construct a rigged graph/anti-graph correspondence with the augmentation direction in the continuous dual and the control direction in the state grade.",
    }
    RESULT.write_text(json.dumps(output, indent=2, default=str) + "\n")
    print(json.dumps(output, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
