import itertools
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


def mixed_distance(vertex_count, edges, anchor=0):
    unanchored = [v for v in range(vertex_count) if v != anchor]
    best = None
    for size in range(1, len(unanchored) + 1):
        for subset_tuple in itertools.combinations(unanchored, size):
            subset = set(subset_tuple)
            cut = sum((left in subset) != (right in subset)
                      for left, right in edges)
            weight = size + cut
            best = weight if best is None else min(best, weight)
    return best


def main():
    fixtures = []
    for vertices in range(3, 7):
        path_edges = [(i, i + 1) for i in range(vertices - 1)]
        cycle_edges = path_edges + [(vertices - 1, 0)]
        complete_edges = [(i, j) for i in range(vertices)
                          for j in range(i + 1, vertices)]
        cases = [
            ("path", path_edges, 2),
            ("cycle", cycle_edges, 3),
            ("complete", complete_edges, vertices),
        ]
        for name, edges, expected_distance in cases:
            boundary = incidence(vertices, edges)
            anchored = boundary[:, 1:]
            joint = anchored.row_join(sp.eye(len(edges)))
            assert gf2_rank(anchored) == vertices - 1
            assert gf2_rank(joint) == len(edges)
            assert joint.cols - gf2_rank(joint) == vertices - 1
            distance = mixed_distance(vertices, edges)
            assert distance == expected_distance
            fixtures.append({
                "graph": f"{name}_{vertices}",
                "mixed_distance": distance,
                "corrects_one_arbitrary_joint_fault": 2 < distance,
            })

    # Exact leaf ambiguity on the anchored three-vertex path.
    path = incidence(3, [(0, 1), (1, 2)])
    anchored = path[:, 1:]
    leaf_vertex = sp.Matrix([0, 1])
    induced_edge = anchored * leaf_vertex
    assert induced_edge == sp.Matrix([0, 1])

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_finite_joint_fault_code_theorem",
        "fixture_count": len(fixtures),
        "joint_kernel_dimension_connected_one_anchor": "n-1 per Pauli coordinate",
        "ambiguity_distance_formula": "min_nonempty_S(|S|+|boundary S|)",
        "anchored_tree_distance": 2,
        "anchored_cycle_distance": 3,
        "anchored_complete_graph_distance": "n",
        "tree_corrects_one_arbitrary_joint_fault": False,
        "cycle_corrects_one_arbitrary_joint_fault": True,
        "leaf_vertex_edge_fault_ambiguity_verified": True,
        "decoder_cost_model_required_beyond_unique_radius": True,
    }
    out = Path(__file__).parents[1] / "results" / "bell-reference-joint-fault-distance.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
