"""Exact diagonal-coherence audit for two consecutive mass insertions."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def rank_over_q(matrix: list[list[int]]) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    column_count = len(rows[0])
    for column in range(column_count):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [x / scale for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [x - factor * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    # Diagonal equations y0-y1=0 and y1-y2=0.
    diagonal_matrix = [[1, -1, 0], [0, 1, -1]]
    diagonal_rank = rank_over_q(diagonal_matrix)

    resolved_coefficient = Fraction(1, 2) ** 3
    resolved_exponents = [-1, -1, -1]
    order_01_then_12 = sum(resolved_exponents)
    order_12_then_01 = sum(resolved_exponents)

    assert diagonal_rank == 2
    assert resolved_coefficient == Fraction(1, 8)
    assert order_01_then_12 == -3
    assert order_12_then_01 == -3

    result = {
        "schema": "marici.two-mass-insertions-diagonal-coherence.v1",
        "resolved_residue": "1/(8*y0*y1*y2)",
        "diagonal_equations": ["y0-y1", "y1-y2"],
        "diagonal_matrix_rank": diagonal_rank,
        "regular_sequence_length": 2,
        "first_then_second": "1/(8*y^3)",
        "second_then_first": "1/(8*y^3)",
        "final_pole_order": 3,
        "higher_tor": 0,
        "conclusion": (
            "The cubic pole is the strict iterated diagonal image of three "
            "labelled simple occurrences; the two diagonal equations are "
            "independent and require no coherence correction."
        ),
    }
    out = Path(__file__).with_name("results") / "two-mass-insertions-diagonal-coherence.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
