"""Finite exact audit of path-diagonal flags for mass-insertion chains."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


def rank_over_q(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [x / scale for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def path_matrix(insertions: int) -> list[list[int]]:
    matrix = []
    for i in range(insertions):
        row = [0] * (insertions + 1)
        row[i] = 1
        row[i + 1] = -1
        matrix.append(row)
    return matrix


def main() -> None:
    full_rank_checks = 0
    subset_flag_checks = 0
    records = []
    for r in range(1, 33):
        matrix = path_matrix(r)
        rank = rank_over_q(matrix)
        assert rank == r
        full_rank_checks += 1
        coefficient = Fraction(1, 2) ** (r + 1)
        records.append({
            "white_sites": r,
            "edge_occurrences": r + 1,
            "diagonal_rank": rank,
            "pole_order": r + 1,
            "coefficient": f"1/{coefficient.denominator}",
        })

        # Exhaust every partial diagonal flag through nine white sites.
        if r <= 9:
            for size in range(r + 1):
                for chosen in itertools.combinations(range(r), size):
                    submatrix = [matrix[i] for i in chosen]
                    assert rank_over_q(submatrix) == size
                    subset_flag_checks += 1

    result = {
        "schema": "marici.all-mass-insertion-path-diagonals.v1",
        "full_rank_checks": full_rank_checks,
        "exhaustive_partial_flag_checks_through_r=9": subset_flag_checks,
        "all_pass": True,
        "records": records,
        "theorem": (
            "For r white sites, the path-incidence diagonal matrix has rank r; "
            "r+1 labelled simple factors specialize to 1/(2y)^(r+1), and "
            "every partial diagonal flag remains independent."
        ),
    }
    out = Path(__file__).with_name("results") / "all-mass-insertion-path-diagonals.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "records"}, indent=2))


if __name__ == "__main__":
    main()
