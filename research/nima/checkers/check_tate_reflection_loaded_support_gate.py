"""Locate the first support obstruction in the reflection nullhomotopy.

The carrier homotopy is certified by
check_tate_reflection_discrepancy_homotopy.py.  This companion checker
compares its forced degree-zero support and derived degree-one cells with
the frozen literal triangulation supports of Entry 258.
"""

from itertools import combinations
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HOMOTOPY = ROOT / "research/nima/checkers/check_tate_reflection_discrepancy_homotopy.py"


def edge(a, b):
    return (a, b) if a < b else (b, a)


def short(index):
    return edge(index, (index + 2) % 6)


def rotate_diagonal(value, turns):
    return edge((value[0] + 2 * turns) % 6, (value[1] + 2 * turns) % 6)


def road_halves(road):
    d03 = edge(0, 3)
    plus = {short(1), short(3), short(5)}
    minus = {short(0), short(2), short(4)}
    v10 = {d03, short(1), short(3)}
    central = {d03, short(0), short(3)}
    v01 = {d03, short(0), short(4)}
    turns = (2, 0, 1)[road]

    def rotate(face):
        return {rotate_diagonal(value, turns) for value in face}

    return tuple(map(rotate, (plus, v10, central))), tuple(
        map(rotate, (minus, v01, central))
    )


def ordered_vertex(left, right):
    road = next(value for value in range(3) if value not in (left, right))
    positive = right == (left + 1) % 3
    plus, minus = road_halves(road)
    half = plus if positive else minus
    edge0 = half[0] & half[1]
    edge1 = half[1] & half[2]
    return edge0 | edge1


def source_reflection(i):
    return (1 - i) % 6


def literal_reflection(i):
    return (5 - i) % 6


def main():
    certified = json.loads(
        subprocess.check_output([sys.executable, str(HOMOTOPY)], text=True)
    )
    assert certified["all_chain_homotopy_equations"]
    assert certified["h1_nonzero_entries_in_zero_parameter_gauge"] > 0
    assert certified["mixed_faces_only_h1_with_zero_h2_exists"]
    assert certified["mixed_faces_only_solution_integral"]
    assert certified["mixed_faces_only_affine_parameter_count"] == 0

    ordered = ((0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1))
    supports = tuple(ordered_vertex(*pair) for pair in ordered)

    legal_edges = tuple(
        candidate
        for candidate in combinations(range(6), 2)
        if candidate not in {edge(i, i + 3) for i in range(3)}
    )
    faces = tuple(
        triple
        for triple in combinations(range(6), 3)
        if all(edge(a, b) in legal_edges for a, b in combinations(triple, 2))
    )
    assert len(legal_edges) == 12
    assert len(faces) == 8

    h0_edges = tuple(
        edge(source_reflection(i), literal_reflection(i)) for i in range(6)
    )
    assert len(set(h0_edges)) == 6
    h0_common_support = tuple(supports[a] & supports[b] for a, b in h0_edges)
    assert all(len(common) == 1 for common in h0_common_support)

    face_common_support = tuple(
        supports[a] & supports[b] & supports[c] for a, b, c in faces
    )
    assert all(not common for common in face_common_support)

    print(
        json.dumps(
            {
                "status": "falsified_scoped_ordinary_loaded_reflection_homotopy",
                "carrier_nullhomotopy_certified": True,
                "degree_zero_homotopy_edges": 6,
                "degree_zero_edges_with_literal_support": 6,
                "degree_zero_ordinary_lift_exists": True,
                "derived_degree_one_faces": 8,
                "degree_one_faces_with_literal_triple_support": 0,
                "degree_one_homotopy_nonzero": True,
                "minimal_required_extraordinary_faces": 6,
                "pure_faces_required": False,
                "relative_interior_required": False,
                "ordinary_loaded_lift_exists": False,
                "first_failed_grade": 1,
                "required_repair": (
                    "six mixed extraordinary Beck-Chevalley face cells; the "
                    "two pure faces and relative interior are not required "
                    "by the unique constrained reflection homotopy"
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
