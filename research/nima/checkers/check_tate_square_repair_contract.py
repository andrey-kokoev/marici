#!/usr/bin/env python3
"""Check that the C3 Tate-square residue fixes the observable repair contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-square-repair-contract.json"


def mul(a: list[int], b: list[int], p: int = 3) -> list[int]:
    out = [0, 0, 0]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[(i + j) % 3] = (out[(i + j) % 3] + ai * bj) % p
    return out


def main() -> None:
    # t=g-1 and n=1+g+g^2 in F_3[C_3].
    t = [2, 1, 0]
    norm = [1, 1, 1]
    square = mul(t, t)
    assert square == norm

    scalar_maps = {c: [(c * x) % 3 for x in norm] for c in range(3)}
    nonzero = [c for c in range(3) if c != 0]
    normalized = [c for c in nonzero if scalar_maps[c] == square]
    assert normalized == [1]

    result = {
        "status": "PASS",
        "missing_cell_type": "lax-monoidal supported-realization comparator",
        "repair_contract": {
            "arity": 2,
            "support": "S_x intersect S_y",
            "coefficient_shadow": "t tensor t maps to norm",
            "required_coherence": ["naturality", "associativity", "deck equivariance"],
        },
        "rank_one_scalar_candidates_over_F3": list(scalar_maps),
        "nonzero_candidates": nonzero,
        "normalized_candidate": normalized[0],
        "existence_established": False,
        "conclusion": (
            "The residue uniquely fixes the observable coefficient behavior of "
            "any repair, but does not establish a source-level implementation."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
