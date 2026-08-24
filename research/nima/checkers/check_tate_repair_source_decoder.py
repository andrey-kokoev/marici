#!/usr/bin/env python3
"""Test how source occurrence orientation reduces the C3 repair gauge torsor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-repair-source-decoder.json"
P = 3


def phi(x: tuple[int, int, int], a: int, b: int) -> tuple[int, int, int]:
    x0, x1, x2 = x
    return (x0 % P, x1 * a % P, (x1 * b + x2 * a * a) % P)


def main() -> None:
    # Coordinates are in 1,t,t^2.  g=1+t and g^-1=g^2=1+2t+t^2.
    g = (1, 1, 0)
    g_inverse = (1, 2, 1)
    gauges = [(a, b) for a in (1, 2) for b in range(P)]

    oriented = [(a, b) for a, b in gauges if phi(g, a, b) == g]
    unoriented = [
        (a, b)
        for a, b in gauges
        if phi(g, a, b) in {g, g_inverse}
    ]
    assert oriented == [(1, 0)]
    assert unoriented == [(1, 0), (2, 1)]

    result = {
        "status": "PASS",
        "filtered_algebra_gauges": len(gauges),
        "unoriented_cyclic_gauges": [list(x) for x in unoriented],
        "oriented_labelled_gauges": [list(x) for x in oriented],
        "counts": {
            "filtration_only": len(gauges),
            "unoriented_cyclic_source": len(unoriented),
            "oriented_labelled_source": len(oriented),
        },
        "constructor_existence_established": False,
        "conclusion": (
            "The oriented source occurrence generator canonically decodes the "
            "filtered representative, but does not construct the missing product."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
