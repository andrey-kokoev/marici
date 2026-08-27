from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "research/nima/fixtures/semantic-pullback-prospective-observability.json"
RESULT = ROOT / "research/nima/results/semantic-pullback-prospective-observability.json"
FROZEN_SHA256 = "862e4e3486009184cbc4828eed4031573b259ce8e86340b69ee03f94a7c946f7"


def matrix_product(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    assert left and right and len(left[0]) == len(right)
    return [
        [sum((row[k] * right[k][j] for k in range(len(right))), Fraction(0)) for j in range(len(right[0]))]
        for row in left
    ]


def matrix_power(matrix: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    size = len(matrix)
    result = [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]
    base = matrix
    for _ in range(exponent):
        result = matrix_product(result, base)
    return result


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    work = [row[:] for row in matrix]
    if not work:
        return work, []
    rows = len(work)
    cols = len(work[0])
    pivot_cols: list[int] = []
    pivot_row = 0
    for col in range(cols):
        candidate = next((row for row in range(pivot_row, rows) if work[row][col]), None)
        if candidate is None:
            continue
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        pivot = work[pivot_row][col]
        work[pivot_row] = [value / pivot for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [
                    work[row][j] - factor * work[pivot_row][j]
                    for j in range(cols)
                ]
        pivot_cols.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return work, pivot_cols


def nullspace(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(matrix)
    cols = len(matrix[0])
    free_cols = [col for col in range(cols) if col not in pivots]
    basis: list[list[Fraction]] = []
    for free_col in free_cols:
        vector = [Fraction(0) for _ in range(cols)]
        vector[free_col] = Fraction(1)
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -reduced[row][free_col]
        basis.append(vector)
    return basis


def row_times_vector(row: list[Fraction], vector: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(row, vector)), Fraction(0))


def encode_fraction(value: Fraction) -> int | str:
    return value.numerator if value.denominator == 1 else str(value)


def encode_matrix(matrix: list[list[Fraction]]) -> list[list[int | str]]:
    return [[encode_fraction(value) for value in row] for row in matrix]


def main() -> None:
    fixture_bytes = FIXTURE.read_bytes()
    fixture_sha256 = hashlib.sha256(fixture_bytes).hexdigest()
    assert fixture_sha256 == FROZEN_SHA256
    fixture = json.loads(fixture_bytes)

    constructor = fixture["constructor"]
    transport = [[Fraction(value) for value in row] for row in constructor["transport"]]
    observer = [[Fraction(value) for value in row] for row in constructor["observer"]]
    times = constructor["admitted_record_times"]
    extension_time = constructor["candidate_extension_time"]

    pulled_effects = [matrix_product(observer, matrix_power(transport, time))[0] for time in times]
    admitted_rref, admitted_pivots = rref(pulled_effects)
    residual_basis = nullspace(pulled_effects)

    candidate_row = matrix_product(observer, matrix_power(transport, extension_time))[0]
    extended_rows = pulled_effects + [candidate_row]
    _, extended_pivots = rref(extended_rows)

    hostile = [Fraction(value) for value in fixture["falsifier"]["state"]]
    hostile_trace = [row_times_vector(row, hostile) for row in extended_rows]

    predicted = fixture["prediction"]
    predicted_basis = [[Fraction(value) for value in row] for row in predicted["residual_state_basis"]]
    assert len(admitted_pivots) == predicted["admitted_observability_rank"]
    assert residual_basis == predicted_basis
    assert len(extended_pivots) == constructor["state_dimension"]
    assert predicted["minimal_added_record_count"] == 1
    assert hostile_trace[:-1] == [Fraction(0), Fraction(0), Fraction(0)]
    assert hostile_trace[-1] == Fraction(1)

    # Independent hostile audit: search the complete {-1,0,1}^4 cube for
    # nonzero states invisible at admitted times, then require time 3 to
    # separate every such state. This does not use the preregistered basis.
    invisible_states: list[list[Fraction]] = []
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            for c in (-1, 0, 1):
                for d in (-1, 0, 1):
                    vector = [Fraction(a), Fraction(b), Fraction(c), Fraction(d)]
                    if vector == [Fraction(0)] * 4:
                        continue
                    if all(row_times_vector(row, vector) == 0 for row in pulled_effects):
                        invisible_states.append(vector)
    assert invisible_states == [
        [Fraction(0), Fraction(0), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]
    assert all(row_times_vector(candidate_row, vector) != 0 for vector in invisible_states)

    result = {
        "schema": "marici.semantic_pullback_prospective_observability.v1",
        "status": "pass",
        "preregistration": {
            "path": str(FIXTURE.relative_to(ROOT)).replace("\\", "/"),
            "sha256": fixture_sha256,
            "graph_event": "ev-000000006383-53b6e708-5423-4bd5-81f8-d18873d082a4",
        },
        "semantic_pullback": {
            "rule": "C maps backward to C T^k",
            "admitted_times": times,
            "pulled_effects": encode_matrix(pulled_effects),
            "rref": encode_matrix(admitted_rref),
            "rank": len(admitted_pivots),
            "residual_basis": encode_matrix(residual_basis),
        },
        "extension": {
            "time": extension_time,
            "pulled_effect": encode_matrix([candidate_row])[0],
            "extended_rank": len(extended_pivots),
            "minimal_added_record_count": 1,
        },
        "forward_hostile": {
            "preregistered_state": encode_matrix([hostile])[0],
            "record_trace_times_0_to_3": [encode_fraction(value) for value in hostile_trace],
            "independent_cube_invisible_states": encode_matrix(invisible_states),
            "candidate_separates_all_cube_hostiles": True,
        },
        "prediction_match": {
            "rank": True,
            "residual_direction": True,
            "minimal_extension": True,
            "hostile_trace": True,
        },
        "claim_boundary": (
            "Exact finite rational observability fixture. This validates semantic "
            "pullback on one new constructor, not a universal explanation theorem."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
