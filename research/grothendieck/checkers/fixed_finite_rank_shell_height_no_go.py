"""Exact checks for the fixed finite-rank logarithmic-shell no-go."""

from fractions import Fraction
from math import comb, factorial


def leading_residual_coefficient(m: int) -> Fraction:
    monic_norm = Fraction(1, (2 * m + 1) * comb(2 * m, m) ** 2)
    return monic_norm / factorial(m) ** 2


expected = {
    1: Fraction(1, 12),
    2: Fraction(1, 720),
    3: Fraction(1, 100800),
    4: Fraction(1, 25401600),
}
assert {m: leading_residual_coefficient(m) for m in expected} == expected

result = {
    "rank_one_T2_coefficient_is_1_over_12": True,
    "rank_two_T4_coefficient_is_1_over_720": True,
    "rank_three_T6_coefficient_is_1_over_100800": True,
    "rank_four_T8_coefficient_is_1_over_25401600": True,
    "finite_rank_height_orbit_no_go": True,
    "reason": "Distinct exponentials are linearly independent; a rank-m fiber contains exact height vectors at at most m distinct heights.",
    "summability_gate": "sum_k delta_(V_k)(T)/k must converge locally uniformly in T",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "fixed-finite-rank-shell-height-no-go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

