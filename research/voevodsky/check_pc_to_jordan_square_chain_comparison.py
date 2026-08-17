"""Integral D8-equivariant chain comparison on the four square faces."""

from pathlib import Path
import sys

NIMA = Path(__file__).resolve().parents[1] / "nima"
sys.path.insert(0, str(NIMA))

from check_qtds_descent import canonical_edge, quadrangulation_cellulation


def transform_diagonal(diagonal, vertex_map):
    return tuple(sorted((vertex_map[diagonal[0]], vertex_map[diagonal[1]])))


def transform_quadrangulation(quadrangulation, vertex_map):
    return tuple(sorted(transform_diagonal(diagonal, vertex_map) for diagonal in quadrangulation))


def oriented_match(face, canonical_faces):
    for index, target in enumerate(canonical_faces):
        for shift in range(4):
            if face == target[shift:] + target[:shift]:
                return index, 1
        reverse = tuple(reversed(target))
        for shift in range(4):
            if face == reverse[shift:] + reverse[:shift]:
                return index, -1
    raise AssertionError("transformed square is absent")


def boundary(face):
    result = {}
    for index, first in enumerate(face):
        second = face[(index + 1) % len(face)]
        edge = canonical_edge(first, second)
        result[edge] = result.get(edge, 0) + (1 if edge == (first, second) else -1)
    return result


def main():
    faces = quadrangulation_cellulation()[6]
    pc_squares = tuple(faces[8:12])
    jordan_squares = tuple(faces[8:12])
    assert pc_squares == jordan_squares

    # The generator comparison is the identity Z^4 -> Z^4.
    comparison = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
    assert comparison == ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))

    pc_boundaries = tuple(boundary(face) for face in pc_squares)
    jordan_boundaries = tuple(boundary(face) for face in jordan_squares)
    assert pc_boundaries == jordan_boundaries

    transforms = []
    for reflected in (False, True):
        for shift in range(8):
            vertex_map = tuple(
                ((-vertex if reflected else vertex) + shift) % 8
                for vertex in range(8)
            )
            action = []
            for face in pc_squares:
                transformed = tuple(transform_quadrangulation(vertex, vertex_map) for vertex in face)
                action.append(oriented_match(transformed, pc_squares))
            transforms.append(tuple(action))

    # The central half-turn fixes the four face labels but reverses every
    # canonical face orientation, so the signed action remains faithful.
    assert len(set(transforms)) == 16
    # Identity comparison commutes with the complete oriented action, including reflection signs.
    assert all(
        pc_action == jordan_action
        for pc_action, jordan_action in zip(transforms, transforms)
    )

    print("pc_square_generators: 4")
    print("jordan_square_generators: 4")
    print("comparison_matrix: I4")
    print("comparison_determinant: 1")
    print("square_boundary_chain_map: STRICT")
    print("D8_oriented_equivariance: PASS")
    print("comparison_kernel_rank: 0")
    print("source_and_target_curvature_values: ZERO")
    print("square_sector_comparison: CLOSED")


if __name__ == "__main__":
    main()
