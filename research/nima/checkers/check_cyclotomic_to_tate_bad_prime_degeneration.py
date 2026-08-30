#!/usr/bin/env python3
"""Relate the C3 cyclotomic doublet to its characteristic-three Tate extension."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "cyclotomic-to-tate-bad-prime-degeneration.json"


def rank_mod_p(matrix: list[list[int]], p: int) -> int:
    rows = [[x % p for x in row] for row in matrix]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(inv * x) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                a = rows[i][col]
                rows[i] = [(x - a * y) % p for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def matmul_mod_p(a: list[list[int]], b: list[list[int]], p: int) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) % p for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def main() -> None:
    x = sp.symbols("x")
    R = sp.Matrix([[0, -1], [1, -1]])
    identity = sp.eye(2)
    assert R.charpoly(x).as_expr() == x**2 + x + 1
    assert (R - identity).det() == 3
    assert (R - identity).rank() == 2  # No characteristic-zero fixed vector.

    R3 = [[int(v) % 3 for v in row] for row in R.tolist()]
    J3 = [[(R3[i][j] - (1 if i == j else 0)) % 3 for j in range(2)] for i in range(2)]
    J3_squared = matmul_mod_p(J3, J3, 3)
    assert rank_mod_p(J3, 3) == 1
    assert J3_squared == [[0, 0], [0, 0]]

    # The cyclotomic polynomial acquires a repeated root at one modulo three.
    assert (1**2 + 1 + 1) % 3 == 0
    derivative_at_one = (2 * 1 + 1) % 3
    assert derivative_at_one == 0

    result = {
        "status": "PASS",
        "generic_characteristic_polynomial": "x^2+x+1",
        "generic_eigencharacters": ["zeta_3", "zeta_3^-1"],
        "generic_fixed_rank": 0,
        "det_R_minus_identity": int((R - identity).det()),
        "mod3_characteristic_polynomial": "(x-1)^2",
        "mod3_rotation": R3,
        "mod3_nilpotent_residue": J3,
        "mod3_nilpotent_rank": rank_mod_p(J3, 3),
        "mod3_nilpotent_square": J3_squared,
        "mod3_invariant_rank": 1,
        "direct_D3_map_norm_to_generic_doublet": False,
        "interpretation": (
            "The Tate/norm extension is the characteristic-three collision of "
            "the two conjugate primitive phase eigenlines."
        ),
        "next_gate": "integral linking or Bockstein comparison between the torsion extension and cyclotomic phase doublet",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
