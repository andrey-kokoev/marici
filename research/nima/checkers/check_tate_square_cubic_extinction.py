#!/usr/bin/env python3
"""Verify lift-independent Tate squaring and cubic extinction in F3[C3]."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-square-cubic-extinction.json"


def mul(a: list[int], b: list[int], p: int = 3) -> list[int]:
    out = [0, 0, 0]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[(i + j) % 3] = (out[(i + j) % 3] + ai * bj) % p
    return out


def add(a: list[int], b: list[int], p: int = 3) -> list[int]:
    return [(x + y) % p for x, y in zip(a, b)]


def scale(c: int, a: list[int], p: int = 3) -> list[int]:
    return [(c * x) % p for x in a]


def main() -> None:
    zero = [0, 0, 0]
    t = [2, 1, 0]
    norm = mul(t, t)
    assert norm == [1, 1, 1]
    assert mul(norm, t) == zero
    assert mul(norm, norm) == zero

    reports = []
    for a in range(3):
        lift = add(t, scale(a, norm))
        square = mul(lift, lift)
        cube_left = mul(square, lift)
        cube_right = mul(lift, square)
        assert square == norm
        assert cube_left == cube_right == zero
        reports.append(
            {
                "lift_parameter": a,
                "lift": lift,
                "square": square,
                "left_cube": cube_left,
                "right_cube": cube_right,
            }
        )

    result = {
        "status": "PASS",
        "lift_reports": reports,
        "operational_table": {
            "T*T": "N",
            "N*T": "0",
            "T*N": "0",
            "N*N": "0",
        },
        "falsifier": "Any proposed associative physical constructor with a nonzero three-Tate composite is rejected.",
        "source_authority_established": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
