#!/usr/bin/env python3
"""Enumerate filtered algebra gauges invisible to the C3 Tate repair syndrome."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-repair-gauge-torsor.json"
P = 3


def mul(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    # Coordinates in 1,t,t^2 with t^3=0.
    x0, x1, x2 = x
    y0, y1, y2 = y
    return (
        x0 * y0 % P,
        (x0 * y1 + x1 * y0) % P,
        (x0 * y2 + x1 * y1 + x2 * y0) % P,
    )


def phi(x: tuple[int, int, int], a: int, b: int) -> tuple[int, int, int]:
    # Substitute t -> a*t+b*t^2.
    x0, x1, x2 = x
    return (x0 % P, x1 * a % P, (x1 * b + x2 * a * a) % P)


def main() -> None:
    elements = [(x0, x1, x2) for x0 in range(P) for x1 in range(P) for x2 in range(P)]
    t = (0, 1, 0)
    norm = (0, 0, 1)
    zero = (0, 0, 0)
    gauges = []

    for a in (1, 2):
        for b in range(P):
            images = {phi(x, a, b) for x in elements}
            assert len(images) == len(elements)
            for x in elements:
                for y in elements:
                    assert phi(mul(x, y), a, b) == mul(phi(x, a, b), phi(y, a, b))
            image_t = phi(t, a, b)
            assert mul(image_t, image_t) == norm
            assert mul(mul(image_t, image_t), image_t) == zero
            assert phi(norm, a, b) == norm
            gauges.append({"a": a, "b": b, "image_of_t": list(image_t)})

    assert len(gauges) == 6
    result = {
        "status": "PASS",
        "filtered_augmentation_preserving_automorphism_count": len(gauges),
        "automorphisms": gauges,
        "invariants_shared_by_all": [
            "augmentation",
            "augmentation filtration",
            "associated Tate grade",
            "norm line",
            "T*T=N",
            "cubic extinction",
            "associativity",
        ],
        "canonical_decoder_exists_from_current_invariants": False,
        "conclusion": (
            "The coherence syndrome determines a repair class only modulo a "
            "six-element filtered algebra automorphism torsor."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
