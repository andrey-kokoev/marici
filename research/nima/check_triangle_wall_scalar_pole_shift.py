"""Exact obstruction to a scalar Cayley--Menger pole-shift chain map.

The labelled source presentation has de Rham coefficient ``gamma-k`` and
principal relation ``e_k-K e_{k+1}``.  A diagonal shift
``e_k -> a_k e_{k+1}`` must satisfy both displayed constraints below.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def audit(gamma: int, levels: list[int]) -> dict[str, object]:
    records = []
    for k in levels:
        # Normalize a_k=1.  De Rham and principal coherence then demand two
        # independently derived values of a_{k+1}.
        de_rham_ratio = Fraction(gamma - k - 1, gamma - k)
        principal_ratio = Fraction(1, 1)
        records.append(
            {
                "k": k,
                "de_rham_required_ratio": [
                    de_rham_ratio.numerator,
                    de_rham_ratio.denominator,
                ],
                "principal_required_ratio": [1, 1],
                "nonzero_scalar_shift_exists": de_rham_ratio == principal_ratio,
            }
        )
    return {
        "schema": "marici.triangle-wall-scalar-pole-shift.v1",
        "gamma": gamma,
        "constraints": {
            "de_rham": "a_(k+1)*(gamma-k)=a_k*(gamma-k-1)",
            "principal": "a_(k+1)=a_k",
        },
        "levels": records,
        "nonzero_scalar_shift_exists_at_all_tested_levels": all(
            record["nonzero_scalar_shift_exists"] for record in records
        ),
        "conclusion": (
            "A nonzero diagonal pole shift cannot intertwine de Rham reduction "
            "and principal coherence at the tested source levels."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gamma", type=int, default=5)
    parser.add_argument("--levels", type=int, nargs="+", default=[2, 3])
    parser.add_argument("--output")
    args = parser.parse_args()
    if any(args.gamma == k for k in args.levels):
        raise ValueError("gamma-k must be nonzero at every tested level")
    result = audit(args.gamma, args.levels)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        from pathlib import Path

        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
