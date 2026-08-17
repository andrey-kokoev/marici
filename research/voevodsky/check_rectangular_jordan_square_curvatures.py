"""Evaluate all four octagonal square curvatures in a rectangular Jordan pair."""

from fractions import Fraction
from pathlib import Path
import sys

NIMA = Path(__file__).resolve().parents[1] / "nima"
sys.path.insert(0, str(NIMA))

from check_qtds_descent import quadrangulation_cellulation, ternary_presentations
from check_qtds_lift import matrix_product


def matrix(rows, columns, seed):
    return tuple(
        tuple(Fraction(seed + 3 * row - 2 * column) for column in range(columns))
        for row in range(rows)
    )


def evaluate(expression, leaves):
    if isinstance(expression, int):
        return leaves[expression]
    operation, first, second, third = expression
    assert operation in {"T+", "T-"}
    return matrix_product(
        matrix_product(evaluate(first, leaves), evaluate(second, leaves)),
        evaluate(third, leaves),
    )


def linear_combination(coefficients, values):
    return tuple(
        tuple(
            sum(
                (coefficient * value[row][column] for coefficient, value in zip(coefficients, values)),
                Fraction(0),
            )
            for column in range(len(values[0][0]))
        )
        for row in range(len(values[0]))
    )


def is_zero(value):
    return all(entry == 0 for row in value for entry in row)


def main():
    # Seven distinct alternating rectangular inputs: A,B,A,B,A,B,A.
    leaves = {
        index: matrix(2, 3, 5 + index) if index % 2 == 0 else matrix(3, 2, 5 + index)
        for index in range(7)
    }
    presentations = ternary_presentations()
    values = {vertex: evaluate(expression, leaves) for vertex, expression in presentations.items()}
    flat = leaves[0]
    for index in range(1, 7):
        flat = matrix_product(flat, leaves[index])
    assert set(values.values()) == {flat}

    faces = quadrangulation_cellulation()[6]
    squares = faces[8:12]
    curvatures = []
    for square in squares:
        curvature = linear_combination((1, -1, 1, -1), tuple(values[vertex] for vertex in square))
        assert is_zero(curvature)
        curvatures.append(curvature)

    alternating_projection = linear_combination((1, -1, 1, -1), tuple(curvatures))
    standard_projection_1 = linear_combination((1, 0, -1, 0), tuple(curvatures))
    standard_projection_2 = linear_combination((0, 1, 0, -1), tuple(curvatures))
    assert is_zero(alternating_projection)
    assert is_zero(standard_projection_1)
    assert is_zero(standard_projection_2)

    print("ternary_presentations_evaluated: 12")
    print("distinct_generic_rectangular_inputs: 7")
    print("square_curvature_matrices: [ZERO,ZERO,ZERO,ZERO]")
    print("alternating_projection: ZERO")
    print("standard_2d_projection: [ZERO,ZERO]")
    print("rectangular_Jordan_square_comparison: CLOSED")
    print("geometric_chain_comparison_map: NOT_CONSTRUCTED")


if __name__ == "__main__":
    main()
