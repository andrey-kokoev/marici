#!/usr/bin/env python3
"""Check exchange-sign cancellation in the completed double-soft Leray block."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-square-leray-parity-completion.json"


def koszul_swap_sign(left_degree: int, right_degree: int) -> int:
    return -1 if (left_degree * right_degree) % 2 else 1


def main() -> None:
    normal_swap = koszul_swap_sign(1, 1)
    link_circle_swap = koszul_swap_sign(1, 1)
    factored_total = normal_swap * link_circle_swap
    thom_block_swap = koszul_swap_sign(2, 2)

    assert normal_swap == -1
    assert link_circle_swap == -1
    assert factored_total == thom_block_swap == 1

    result = {
        "status": "PASS",
        "real_normal_exchange_sign": normal_swap,
        "leray_circle_exchange_sign": link_circle_swap,
        "factored_complete_exchange_sign": factored_total,
        "degree_two_thom_block_exchange_sign": thom_block_swap,
        "coefficient_norm_character": 1,
        "parity_compatible": factored_total == 1,
        "double_soft_leray_torus_constructed": False,
        "next_object": "source-normalized double-soft Leray torus and its norm comparison",
        "conclusion": (
            "Retaining both real-normal and Leray-link orientations cancels the "
            "odd exchange signs and makes an unframed even Tate-square comparison "
            "parity-legal."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
