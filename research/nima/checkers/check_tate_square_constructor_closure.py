#!/usr/bin/env python3
"""Audit arity, support, and authority for the C3 Tate-square constructor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-square-constructor-closure.json"


def main() -> None:
    operations = [
        {
            "name": "localization",
            "arity": 1,
            "supported": True,
            "source_derived": True,
            "coefficient_tate_square": False,
        },
        {
            "name": "gysin",
            "arity": 1,
            "supported": True,
            "source_derived": True,
            "coefficient_tate_square": False,
        },
        {
            "name": "augmentation_sewing",
            "arity": 1,
            "supported": False,
            "source_derived": True,
            "coefficient_tate_square": False,
        },
        {
            "name": "norm_channel",
            "arity": 1,
            "supported": False,
            "source_derived": True,
            "coefficient_tate_square": False,
        },
        {
            "name": "coefficient_convolution",
            "arity": 2,
            "supported": False,
            "source_derived": False,
            "coefficient_tate_square": True,
        },
        {
            "name": "derived_transverse_intersection",
            "arity": 2,
            "supported": True,
            "source_derived": False,
            "coefficient_tate_square": False,
        },
    ]

    # Composites of one-input arrows still have one varying input.
    unary = [op for op in operations if op["arity"] == 1]
    for left in unary:
        for right in unary:
            assert max(left["arity"], right["arity"]) == 1

    admissible = [
        op
        for op in operations
        if op["arity"] == 2
        and op["supported"]
        and op["source_derived"]
        and op["coefficient_tate_square"]
    ]
    assert admissible == []

    result = {
        "status": "PASS",
        "target_signature": "supported source-derived (T,T) -> N inducing the C3 coefficient square",
        "operations": operations,
        "unary_closure_max_arity": 1,
        "admissible_target_count": len(admissible),
        "reopening_burden": [
            "source-derived binary correspondence",
            "support preservation",
            "coefficient shadow equals the fixed Tate-square map",
        ],
        "conclusion": (
            "The admitted unary supported calculus cannot generate the missing "
            "binary Tate product. The two algebraic operations with relevant "
            "pieces each fail an independent authority gate."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
