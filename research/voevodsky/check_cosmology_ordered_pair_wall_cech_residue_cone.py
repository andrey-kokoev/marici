"""Ordered pair-wall Cech residue cone for the triple-incidence denominator gate.

Repeat iteration 3 constructs the smallest source-derived Cech face module whose
oriented 2-simplex boundary carries the opposite residue vector required by the
previous pair-face obstruction.  This is only a residue-level relative cone, not
a full logarithmic primitive or physical period.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_ordered_pair_wall_cech_residue_cone.json"


def load(name: str) -> dict:
    return json.loads((VOEVODSKY_RESULTS / name).read_text(encoding="utf-8"))


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    col_count = len(rows[0])
    for col in range(col_count):
        pivot = next((r for r in range(rank, row_count) if rows[r][col] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(value * inv) % prime for value in rows[rank]]
        for r in range(row_count):
            if r == rank:
                continue
            factor = rows[r][col] % prime
            if factor:
                rows[r] = [(a - factor * b) % prime for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    pair_residue = load("cosmology_pair_face_residue_vector.json")
    assert pair_residue["passed"] is True
    assert pair_residue["residue_vector"] == [1, -1, 1]
    assert pair_residue["pair_faces_order"] == ["q1_q2", "q1_q3", "q2_q3"]

    vertices = ["q1", "q2", "q3"]
    edges = ["q1_q2", "q1_q3", "q2_q3"]
    face = "sigma123=[q1,q2,q3]"

    # Edge boundary rows are vertices q1,q2,q3; columns are edges
    # [q1,q2], [q1,q3], [q2,q3], oriented from lower index to higher index.
    d_edge_to_vertex = [
        [-1, -1, 0],
        [1, 0, -1],
        [0, 1, 1],
    ]
    # Boundary of [q1,q2,q3] is [q2,q3]-[q1,q3]+[q1,q2].
    d_face_to_edge = [[1], [-1], [1]]
    assert matmul(d_edge_to_vertex, d_face_to_edge) == [[0], [0], [0]]

    residue_vector = pair_residue["residue_vector"]
    canceling_face_orientation = [-value for value in d_face_to_edge[0] + d_face_to_edge[1] + d_face_to_edge[2]]
    # Above concatenation keeps the declared edge order.
    assert canceling_face_orientation == [-1, 1, -1]
    assert [residue_vector[i] + canceling_face_orientation[i] for i in range(3)] == [0, 0, 0]

    witnesses = {}
    for prime in (101, 103):
        d2_rank = rank_mod_prime(d_face_to_edge, prime)
        d1_rank = rank_mod_prime(d_edge_to_vertex, prime)
        composite_rank = rank_mod_prime(matmul(d_edge_to_vertex, d_face_to_edge), prime)
        assert (d2_rank, d1_rank, composite_rank) == (1, 2, 0)
        witnesses[str(prime)] = {
            "rank_face_to_edge": d2_rank,
            "rank_edge_to_vertex": d1_rank,
            "rank_composite": composite_rank,
            "residue_plus_canceling_boundary": [0, 0, 0],
        }

    result = {
        "schema": "marici.voevodsky.cosmology-ordered-pair-wall-cech-residue-cone.v1",
        "status": "minimal_ordered_cech_face_cancels_residue_vector_at_residue_level",
        "rechecked_input": "research/voevodsky/results/cosmology_pair_face_residue_vector.json",
        "vertices": vertices,
        "edges_order": edges,
        "face": face,
        "edge_to_vertex_matrix_rows_vertices_cols_edges": d_edge_to_vertex,
        "face_to_edge_matrix_rows_edges_cols_face": d_face_to_edge,
        "d_squared_zero": True,
        "residue_vector": residue_vector,
        "canceling_orientation": "-sigma123",
        "canceling_boundary_vector": canceling_face_orientation,
        "residue_canceled": True,
        "finite_field_witnesses": witnesses,
        "source_derivation": "oriented Cech nerve of the ordered wall cover (q1,q2,q3); no circuit quotient is imposed",
        "not_yet_constructed": [
            "chain map from this residue cone to the full logarithmic denominator complex",
            "one-form primitive H_p^log",
            "resolved/Rees exceptional generator compatibility",
            "Cayley-Menger face cone compatibility",
            "global contour or physical-period readout",
        ],
        "ambient_division_by_p": False,
        "tautological_circuit_quotient_used": False,
        "ideal_dual_evaluation_applied": False,
        "conclusion": "The exact opposite residue vector is not mysterious: it is the boundary of the oppositely oriented ordered Cech 2-simplex. This supplies a minimal residue-level relative cone with d^2=0. The remaining blocker is a source-derived chain map from this Cech residue cone into the full logarithmic denominator or resolved/Rees carrier; without that map, the denominator primitive itself remains unconstructed.",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
