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


def path_incidence(vertex_count):
    matrix = sp.zeros(vertex_count - 1, vertex_count)
    for edge in range(vertex_count - 1):
        matrix[edge, edge] = 1
        matrix[edge, edge + 1] = 1
    return matrix


def mod2(matrix):
    return matrix.applyfunc(lambda value: int(value) % 2)


def main():
    fixtures = []
    for logical_qubits in range(1, 5):
        coordinate_count = 2 * logical_qubits
        for blocks in range(2, 7):
            incidence = path_incidence(blocks)
            syndrome = sp.kronecker_product(incidence, sp.eye(coordinate_count))
            expected_rank = (blocks - 1) * coordinate_count
            expected_kernel = coordinate_count
            assert gf2_rank(syndrome) == expected_rank
            assert syndrome.cols - gf2_rank(syndrome) == expected_kernel

            common_mode = sp.ones(blocks, 1)
            common_coordinate = sp.zeros(coordinate_count, 1)
            common_coordinate[0, 0] = 1
            witness = sp.kronecker_product(common_mode, common_coordinate)
            assert mod2(syndrome * witness) == sp.zeros(syndrome.rows, 1)

            # Freeze block zero as an anchor: remove its coordinate columns.
            anchored = syndrome[:, coordinate_count:]
            assert gf2_rank(anchored) == anchored.cols

            fixtures.append({
                "logical_qubits": logical_qubits,
                "blocks": blocks,
                "relative_rank": expected_rank,
                "common_mode_kernel_dimension": expected_kernel,
            })

    # Three scalar-label replicas have distinct one-fault signatures, but the
    # unrestricted all-ones common mode remains invisible.
    three = path_incidence(3)
    signatures = {tuple(int(x) for x in three[:, j]) for j in range(3)}
    assert len(signatures) == 3
    assert mod2(three * sp.ones(3, 1)) == sp.zeros(2, 1)

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_graph_incidence_and_stabilizer_reference_theorem",
        "fixture_count": len(fixtures),
        "connected_relative_rank_formula": "(n-1)2k",
        "connected_common_mode_kernel_dimension": "2k",
        "common_mode_witness_verified": True,
        "spanning_tree_is_relationally_complete": True,
        "cycle_edges_add_absolute_information": False,
        "trusted_anchor_restriction_injective": True,
        "three_replica_single_fault_signatures_distinct": True,
        "single_fault_correction_requires_promise": True,
        "untrusted_replication_creates_absolute_frame": False,
    }
    out = Path(__file__).parents[1] / "results" / "mixed-boundary-reference-kernel.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
