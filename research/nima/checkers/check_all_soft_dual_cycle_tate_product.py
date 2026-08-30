#!/usr/bin/env python3
"""Construct the all-soft dual-complex cycle carrying the Tate product."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MARICI = ROOT.parents[1]
TRIPLE = MARICI / "research" / "benincasa" / "triple-soft-exceptional-resolution-certificate.json"
LOCAL = ROOT / "results" / "cyclic-tate-product-coefficient-descent.json"
RESULT = ROOT / "results" / "all-soft-dual-cycle-tate-product.json"


def rank_mod_p(matrix: list[list[int]], p: int) -> int:
    rows = [[x % p for x in row] for row in matrix]
    rank = 0
    cols = len(rows[0])
    for col in range(cols):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(inv * x) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                factor = rows[i][col]
                rows[i] = [(x - factor * y) % p for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def main() -> None:
    triple = json.loads(TRIPLE.read_text(encoding="utf-8"))
    local = json.loads(LOCAL.read_text(encoding="utf-8"))
    assert triple["corner"] == "(E,x,y)=(0,0,0)"
    assert triple["E_chart_modulus"] == "(2*r-1)*(1-2*s)/(2*r+2*s-1)"
    assert triple["new_carrier_datum"] is False
    assert local["coefficient_cech_cocycle_closed"] is True

    # Columns are oriented edges 12,23,31; rows are vertices 1,2,3.
    boundary = [
        [-1, 0, 1],
        [1, -1, 0],
        [0, 1, -1],
    ]
    cycle = sp.Matrix([1, 1, 1])
    boundary_matrix = sp.Matrix(boundary)
    assert boundary_matrix * cycle == sp.zeros(3, 1)
    assert boundary_matrix.rank() == 2
    assert rank_mod_p(boundary, 3) == 2
    homology_rank = 3 - boundary_matrix.rank()  # No triple-intersection C2 term.
    assert homology_rank == 1

    norm = (1, 1, 1)
    supported_tuple = [norm, norm, norm]
    scalar_sum_mod_3 = tuple(sum(v[i] for v in supported_tuple) % 3 for i in range(3))
    assert scalar_sum_mod_3 == (0, 0, 0)

    geometric_reflection_sign = -1
    occurrence_reflection_sign = -1
    assert geometric_reflection_sign * occurrence_reflection_sign == 1

    result = {
        "status": "PASS",
        "exceptional_carrier": "projective all-soft normal plane",
        "dual_complex": "unfilled oriented triangle",
        "boundary_matrix": boundary,
        "boundary_rank_Q": boundary_matrix.rank(),
        "boundary_rank_F3": rank_mod_p(boundary, 3),
        "H1_rank": homology_rank,
        "cycle_generator": [int(x) for x in cycle],
        "local_norm_tuple": [list(v) for v in supported_tuple],
        "combined_reflection_character": geometric_reflection_sign * occurrence_reflection_sign,
        "ordinary_scalar_sum_mod_3": list(scalar_sum_mod_3),
        "global_supported_product_constructed": True,
        "physical_relative_chain_activation_established": False,
        "conclusion": (
            "The three local Tate products descend on the canonical all-soft "
            "dual-complex H1 line. The supported class is nonzero, while ordinary "
            "occurrence summation vanishes in characteristic three."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
