import json
from pathlib import Path
import sympy as sp


def gf2_rank(matrix):
    rows = [sum((int(matrix[i, j]) & 1) << j for j in range(matrix.cols))
            for i in range(matrix.rows)]
    rank = 0
    for col in range(matrix.cols):
        pivot = next((i for i in range(rank, len(rows))
                      if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def incidence(vertex_count, edges):
    matrix = sp.zeros(len(edges), vertex_count)
    for row, (left, right) in enumerate(edges):
        matrix[row, left] = 1
        matrix[row, right] = 1
    return matrix


def mod2(matrix):
    return matrix.applyfunc(lambda value: int(value) % 2)


def main():
    fixtures = []
    graph_cases = [
        (3, [(0, 1), (1, 2)], 1, "path3"),
        (3, [(0, 1), (1, 2), (2, 0)], 1, "triangle"),
        (5, [(0, 1), (1, 2), (3, 4)], 2, "path3_plus_edge"),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)], 1, "square_chord"),
    ]
    for logical_qubits in range(1, 5):
        coefficient_dim = 2 * logical_qubits
        for vertices, edges, components, name in graph_cases:
            boundary = incidence(vertices, edges)
            delta = sp.kronecker_product(boundary, sp.eye(coefficient_dim))
            expected_rank = (vertices - components) * coefficient_dim
            beta_one = len(edges) - vertices + components
            assert gf2_rank(delta) == expected_rank
            assert delta.cols - gf2_rank(delta) == components * coefficient_dim
            assert delta.rows - gf2_rank(delta) == beta_one * coefficient_dim

            # Anchor one vertex in each component for the declared fixtures.
            anchors = [0] if components == 1 else [0, 3]
            keep_columns = []
            for vertex in range(vertices):
                if vertex not in anchors:
                    keep_columns.extend(range(
                        vertex * coefficient_dim, (vertex + 1) * coefficient_dim))
            anchored = delta[:, keep_columns]
            assert gf2_rank(anchored) == anchored.cols

            fixtures.append({
                "graph": name,
                "logical_qubits": logical_qubits,
                "h0_dimension": components * coefficient_dim,
                "h1_dimension": beta_one * coefficient_dim,
                "anchor_count": components,
            })

    triangle = incidence(3, [(0, 1), (1, 2), (2, 0)])
    cycle = sp.ones(1, 3)
    assert mod2(cycle * triangle) == sp.zeros(1, 3)
    single_edge_fault = sp.Matrix([1, 0, 0])
    assert mod2(cycle * single_edge_fault)[0] == 1

    path = incidence(3, [(0, 1), (1, 2)])
    assert path.rows - gf2_rank(path) == 0

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_finite_cohomological_fault_classification",
        "fixture_count": len(fixtures),
        "h0_dimension_formula": "2kc",
        "h1_dimension_formula": "2k(m-n+c)",
        "minimum_anchor_count": "c",
        "anchor_condition": "one_per_connected_component",
        "spanning_forest_relative_complete": True,
        "spanning_forest_detects_edge_measurement_fault": False,
        "cycle_parity_annihilates_valid_records": True,
        "single_triangle_edge_fault_detected": True,
        "cycles_remove_common_mode": False,
    }
    out = Path(__file__).parents[1] / "results" / "bell-reference-network-cohomology.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
