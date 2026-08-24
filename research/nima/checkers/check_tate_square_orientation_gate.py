#!/usr/bin/env python3
"""Audit the exchange-character gate for a supported Tate-square product."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-square-orientation-gate.json"


def main() -> None:
    tate_character = -1
    coefficient_domain_character = tate_character * tate_character
    norm_character = 1
    assert coefficient_domain_character == norm_character == 1

    branches = []
    for normal_degree_parity in (0, 1):
        intersection_exchange = (-1) ** normal_degree_parity
        plain_norm_equivariant = intersection_exchange == norm_character
        orientation_twisted_norm_character = norm_character * intersection_exchange
        twisted_equivariant = intersection_exchange == orientation_twisted_norm_character
        branches.append(
            {
                "normal_degree_parity": normal_degree_parity,
                "intersection_exchange_character": intersection_exchange,
                "plain_norm_equivariant": plain_norm_equivariant,
                "orientation_twisted_norm_character": orientation_twisted_norm_character,
                "orientation_twisted_target_equivariant": twisted_equivariant,
            }
        )

    assert branches[0]["plain_norm_equivariant"] is True
    assert branches[1]["plain_norm_equivariant"] is False
    assert branches[1]["orientation_twisted_target_equivariant"] is True

    result = {
        "status": "PASS",
        "coefficient_T_tensor_T_character": coefficient_domain_character,
        "coefficient_norm_character": norm_character,
        "branches": branches,
        "required_unresolved_source_datum": "binary physical Gysin parity and Thom/orientation line",
        "conclusion": (
            "An even Gysin realization may land in the plain norm line. An odd "
            "real/Koszul realization must retain an orientation twist; choosing "
            "its trivialization yields only a framed product."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
