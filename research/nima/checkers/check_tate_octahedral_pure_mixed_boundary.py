"""Split the octahedral fundamental cycle into pure and mixed faces."""

from collections import Counter
from itertools import product
import json


SIGNED_VERTEX = {
    (2, 1): 0,
    (1, -1): 1,
    (0, 1): 2,
    (2, -1): 3,
    (1, 1): 4,
    (0, -1): 5,
}


def oriented_edge(a, b):
    return (a, b) if a < b else (b, a), (1 if a < b else -1)


def face_boundary(vertices):
    a, b, c = vertices
    result = Counter()
    for (left, right), coefficient in [((b, c), 1), ((a, c), -1), ((a, b), 1)]:
        present, orientation = oriented_edge(left, right)
        result[present] += coefficient * orientation
    return result


def add_scaled(target, source, scale):
    for key, value in source.items():
        target[key] += scale * value


def main():
    pure = Counter()
    mixed = Counter()
    faces = []
    for signs in product((1, -1), repeat=3):
        vertices = tuple(SIGNED_VERTEX[(axis, signs[axis])] for axis in range(3))
        coefficient = signs[0] * signs[1] * signs[2]
        boundary = face_boundary(vertices)
        is_pure = len(set(signs)) == 1
        add_scaled(pure if is_pure else mixed, boundary, coefficient)
        faces.append((signs, vertices, coefficient, is_pure))

    total = pure + mixed
    # Counter addition drops zero/negative entries, so compare explicitly.
    keys = set(pure) | set(mixed)
    assert all(pure[key] + mixed[key] == 0 for key in keys)

    short_edges = {
        tuple(sorted(edge))
        for edge in ((0, 2), (2, 4), (4, 0), (1, 3), (3, 5), (5, 1))
    }
    pure_support = {key for key, value in pure.items() if value != 0}
    mixed_support = {key for key, value in mixed.items() if value != 0}
    assert pure_support == mixed_support == short_edges
    assert all(abs(pure[key]) == abs(mixed[key]) == 1 for key in short_edges)

    print(json.dumps({
        "status": "proved_scoped_octahedral_pure_mixed_relative_boundary",
        "faces": len(faces),
        "pure_faces": sum(face[3] for face in faces),
        "mixed_faces": sum(not face[3] for face in faces),
        "pure_boundary_support": [list(edge) for edge in sorted(pure_support)],
        "mixed_boundary_support": [list(edge) for edge in sorted(mixed_support)],
        "unit_coefficients": True,
        "mixed_boundary_equals_negative_pure_boundary": True,
        "cross_sheet_residue": 0,
        "conclusion": (
            "The six mixed octahedral faces form the canonical relative "
            "carrier filler of the six short-facet defect, while the two "
            "pure faces carry the reflection comparison."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
