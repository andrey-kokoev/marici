from fractions import Fraction
import json
from pathlib import Path


LABELS = (0, 1, 3)
ORDER = 7
AMPLITUDES = (Fraction(1, 1), Fraction(2, 1), Fraction(-1, 1))


def main() -> None:
    carrier = [
        [AMPLITUDES[i] * AMPLITUDES[j] for j in range(len(LABELS))]
        for i in range(len(LABELS))
    ]
    expected = [
        [
            carrier[i][j] if LABELS[i] == LABELS[j] else Fraction(0, 1)
            for j in range(len(LABELS))
        ]
        for i in range(len(LABELS))
    ]

    averaged = []
    for i, left in enumerate(LABELS):
        row = []
        for j, right in enumerate(LABELS):
            frequency = (right - left) % ORDER
            haar_coefficient = 1 if frequency == 0 else 0
            row.append(carrier[i][j] * haar_coefficient)
        averaged.append(row)

    assert averaged == expected
    assert all(averaged[i][j] == 0 for i in range(3) for j in range(3) if i != j)
    assert all(averaged[i][i] == carrier[i][i] for i in range(3))

    averaged_twice = [
        [
            averaged[i][j] if LABELS[i] == LABELS[j] else Fraction(0, 1)
            for j in range(3)
        ]
        for i in range(3)
    ]
    assert averaged_twice == averaged

    result = {
        "schema": "marici.nima.mellin-conditional-expectation.v1",
        "finite_character_order": ORDER,
        "labels": list(LABELS),
        "carrier_rank": 1,
        "conditional_expectation_is_diagonal_projection": True,
        "conditional_expectation_is_idempotent": True,
        "diagonal_is_fixed": True,
        "off_diagonal_character_sectors_are_annihilated": True,
        "conditional_expectation_is_invertible": False,
        "averaged_matrix": [[str(value) for value in row] for row in averaged],
    }
    output = Path(__file__).parents[1] / "results" / "mellin-conditional-expectation.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

