from __future__ import annotations

import json
from fractions import Fraction


def determinant(size: int, correlation: Fraction) -> Fraction:
    return (1 - correlation) ** (size - 1) * (1 + (size - 1) * correlation)


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    cases = []
    for cutoff in range(2, 13):
        correlation = Fraction(-(2 * cutoff - 1), 2 * cutoff * (cutoff - 1))
        cutoff_collective = 1 + (cutoff - 1) * correlation
        next_collective = 1 + cutoff * correlation
        cutoff_det = determinant(cutoff, correlation)
        next_det = determinant(cutoff + 1, correlation)

        assert cutoff_collective > 0
        assert next_collective < 0
        assert cutoff_det > 0
        assert next_det < 0

        cases.append({
            "cutoff": cutoff,
            "correlation": render(correlation),
            "cutoff_collective_eigenvalue": render(cutoff_collective),
            "next_collective_eigenvalue": render(next_collective),
            "cutoff_determinant": render(cutoff_det),
            "next_determinant": render(next_det),
        })

    result = {
        "schema": "marici.voevodsky.no-fixed-green-positivity-cutoff.v1",
        "status": "fixed_local_cutoff_falsified",
        "verified_cutoffs": [2, 12],
        "general_correlation": "-(2k-1)/(2k(k-1))",
        "cases": cases,
        "repair_gate": "full joint certificate or source-derived uniform positivity theorem",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
