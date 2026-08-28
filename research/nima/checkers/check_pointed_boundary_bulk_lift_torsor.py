import json
from pathlib import Path


TRACE = [[1, 0]]
LIFT_PLUS = [[1, 0], [0, 1]]
LIFT_MINUS = [[1, 0], [0, -1]]


def multiply(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def main() -> None:
    assert multiply(TRACE, LIFT_PLUS) == TRACE
    assert multiply(TRACE, LIFT_MINUS) == TRACE
    assert LIFT_PLUS != LIFT_MINUS

    identity = [[1, 0], [0, 1]]
    assert multiply(transpose(LIFT_PLUS), LIFT_PLUS) == identity
    assert multiply(transpose(LIFT_MINUS), LIFT_MINUS) == identity

    residual = [
        [
            LIFT_PLUS[i][j] - LIFT_MINUS[i][j]
            for j in range(2)
        ]
        for i in range(2)
    ]
    assert residual != [[0, 0], [0, 0]]
    assert multiply(TRACE, residual) == [[0, 0]]

    result = {
        "schema": "marici.nima.pointed-boundary-bulk-lift-torsor.v1",
        "boundary_trace_agrees": True,
        "both_lifts_are_orthogonal": True,
        "bulk_lifts_are_distinct": True,
        "difference_is_boundary_invisible": True,
        "pointed_boundary_selects_unique_bulk_lift": False,
        "minimum_bulk_kernel_dimension": 1,
        "residual": residual,
    }
    output = Path(__file__).parents[1] / "results" / "pointed-boundary-bulk-lift-torsor.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

