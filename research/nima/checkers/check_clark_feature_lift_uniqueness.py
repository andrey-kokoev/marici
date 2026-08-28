import json
from fractions import Fraction
from pathlib import Path


SHEET_MAP = [
    [1, 0, 0, -1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, -1, 0],
]


def rank(matrix):
    work = [[Fraction(value, 1) for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            scale = work[row][column]
            if scale:
                work[row] = [
                    work[row][index] - scale * work[pivot_row][index]
                    for index in range(column_count)
                ]
        pivot_row += 1
    return pivot_row


def multiply(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def main() -> None:
    assert rank(SHEET_MAP) == 4

    feature_map = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    state_observation = multiply(SHEET_MAP, feature_map)
    assert rank(feature_map) == 4
    assert rank(state_observation) == 4
    hidden_state = [0, 0, 0, 0, 1]
    assert all(
        sum(row[index] * hidden_state[index] for index in range(5)) == 0
        for row in state_observation
    )

    result = {
        "schema": "marici.nima.clark-feature-lift-uniqueness.v1",
        "feature_dimension": 4,
        "sheet_map_rank": rank(SHEET_MAP),
        "feature_level_invisible_dimension": 0,
        "extended_state_dimension": 5,
        "extended_state_observation_rank": rank(state_observation),
        "state_level_invisible_dimension": 1,
        "complete_sheets_select_unique_feature_lift": True,
        "complete_sheets_select_unique_state_lift": False,
        "remaining_gate": "state_feature_injectivity_and_uniform_observability",
    }
    output = Path(__file__).parents[1] / "results" / "clark-feature-lift-uniqueness.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

