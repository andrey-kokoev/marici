"""Identify the reflection mismatch with the two short-facet triangles."""

from collections import Counter
import json


def edge(a, b):
    return tuple(sorted((a, b)))


def source_reflection(i):
    return (1 - i) % 6


def literal_reflection(i):
    return (5 - i) % 6


def main():
    oriented = [
        (source_reflection(i), literal_reflection(i))
        for i in range(6)
    ]
    mismatch_edges = {edge(a, b) for a, b in oriented}
    literal_sheetwise_edges = {
        edge(0, 2), edge(2, 4), edge(4, 0),
        edge(1, 3), edge(3, 5), edge(5, 1),
    }
    assert mismatch_edges == literal_sheetwise_edges
    assert len(mismatch_edges) == 6

    boundary = Counter()
    for a, b in oriented:
        boundary[a] -= 1
        boundary[b] += 1
    assert all(value == 0 for value in boundary.values())

    even_cycle = [(0, 4), (4, 2), (2, 0)]
    odd_cycle = [(1, 5), (5, 3), (3, 1)]
    assert set(map(lambda value: edge(*value), even_cycle + odd_cycle)) == mismatch_edges

    # These are exactly the boundaries of the two pure-sheet octahedral
    # faces; the remaining six mixed faces supply coherence with cross-sheet
    # dP6 edges.
    print(json.dumps({
        "status": "proved_scoped_reflection_mismatch_is_short_facet_boundary",
        "oriented_mismatch_edges": oriented,
        "distinct_edges": len(mismatch_edges),
        "equals_literal_short_facet_edges": True,
        "boundary_zero": True,
        "components": {
            "even_sheet_triangle": even_cycle,
            "odd_sheet_triangle": odd_cycle,
        },
        "pure_sheet_octahedral_faces": 2,
        "remaining_mixed_coherence_faces": 6,
        "conclusion": (
            "The strict reflection comparison is not a scalar conjugacy. "
            "Its carrier boundary is canonically the two pure-sheet "
            "short-facet triangles."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
