#!/usr/bin/env python3
"""Check the contracted-edge normal pushforward in the local two-pole model."""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OUTPUT = REPO / "research/nima/results/polygon-contraction-normal-pushforward.json"


def main() -> None:
    # Exact partial-fraction numerator identity:
    # 1/(A+y)-1/(B+y) = (B-A)/((A+y)(B+y)).
    exact_samples = []
    for a in range(1, 8):
        for b in range(1, 8):
            if a == b:
                continue
            for y in range(0, 8):
                lhs = Fraction(1, a + y) - Fraction(1, b + y)
                rhs = Fraction(b - a, (a + y) * (b + y))
                assert lhs == rhs
                exact_samples.append((a, b, y))

    getcontext().prec = 60
    one = Decimal(1)

    def pushforward(a: int, b: int) -> Decimal:
        if a == b:
            return one / Decimal(a)
        da, db = Decimal(a), Decimal(b)
        return (db / da).ln() / (db - da)

    # Symmetry and non-proportionality to the merged rational pole.
    values = []
    for a, b in ((1, 1), (1, 2), (1, 3), (2, 5), (3, 7)):
        value = pushforward(a, b)
        swapped = pushforward(b, a)
        assert abs(value - swapped) < Decimal("1e-55")
        target = one / Decimal(a + b)
        values.append(
            {
                "A": a,
                "B": b,
                "normal_pushforward": str(value),
                "merged_pole": str(target),
                "ratio": str(value / target),
            }
        )
    assert values[0]["ratio"] != values[1]["ratio"]

    result = {
        "schema": "marici.nima.polygon_contraction.normal_pushforward.v1",
        "local_model": {
            "q1": "A+y",
            "qn": "B+y",
            "merged_wall_on_y0": "q=A+B",
        },
        "ordinary_residue_at_y0": 0,
        "ordinary_restriction_at_y0": "1/(A*B)",
        "normal_pushforward": "log(B/A)/(B-A)",
        "diagonal_limit": "1/A",
        "target_merged_pole": "1/(A+B)",
        "partial_fraction_exact_sample_count": len(exact_samples),
        "pushforward_is_exchange_symmetric": True,
        "pushforward_is_constant_multiple_of_merged_pole": False,
        "interpretation": (
            "Normal integration retains the relative endpoint ratio and cannot "
            "supply either a one-sided occurrence selection or a universal 1/2 counit."
        ),
        "samples": values,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(json.dumps({"sha256": digest, **{k: result[k] for k in (
        "ordinary_residue_at_y0",
        "normal_pushforward",
        "pushforward_is_constant_multiple_of_merged_pole",
    )}}, sort_keys=True))


if __name__ == "__main__":
    main()
