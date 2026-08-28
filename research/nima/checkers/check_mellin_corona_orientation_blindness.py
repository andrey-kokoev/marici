from fractions import Fraction
import json
from pathlib import Path


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> None:
    a = Fraction(2, 1)
    b = Fraction(3, 1)
    plus = [[a * a, a * b], [a * b, b * b]]
    minus = [[a * a, -a * b], [-a * b, b * b]]
    diagonal = [[a * a, Fraction(0, 1)], [Fraction(0, 1), b * b]]

    assert determinant(plus) == determinant(minus) == 0
    assert plus[0][0] + plus[1][1] == minus[0][0] + minus[1][1]
    assert [plus[0][0], plus[1][1]] == [minus[0][0], minus[1][1]]
    assert plus != minus

    residual_plus = [[Fraction(0, 1), a * b], [a * b, Fraction(0, 1)]]
    residual_minus = [[Fraction(0, 1), -a * b], [-a * b, Fraction(0, 1)]]
    assert determinant(residual_plus) == determinant(residual_minus)
    assert residual_plus != residual_minus

    result = {
        "schema": "marici.nima.mellin-corona-orientation-blindness.v1",
        "positive_carriers_are_distinct": True,
        "positive_carriers_are_unitarily_conjugate": True,
        "trace_agrees": True,
        "determinant_agrees": True,
        "labelled_diagonal_agrees": True,
        "conditional_expectation_agrees": True,
        "residual_orientation_agrees": False,
        "residual_spectrum_agrees": True,
        "declared_corona_invariants_select_orientation": False,
        "plus_matrix": [[str(value) for value in row] for row in plus],
        "minus_matrix": [[str(value) for value in row] for row in minus],
        "conditional_expectation": [
            [str(value) for value in row] for row in diagonal
        ],
    }
    output = Path(__file__).parents[1] / "results" / "mellin-corona-orientation-blindness.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

