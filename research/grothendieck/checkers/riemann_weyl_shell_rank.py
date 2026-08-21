"""Numerical asymptotic diagnostic for the forced shell-rank scales."""

import math


def minimal_rank_scale(k: float) -> float:
    return math.log(math.log(k)) / math.log(math.log(math.log(k)))


def weyl_rank_scale(k: float) -> float:
    return math.log(k / (2 * math.pi)) / (2 * math.pi)


samples = [1e12, 1e24, 1e48, 1e96]
ratios = [weyl_rank_scale(k) / minimal_rank_scale(k) for k in samples]
assert all(a < b for a, b in zip(ratios, ratios[1:]))

result = {
    "weyl_rank": "(1/(2*pi))*log(k/(2*pi))",
    "minimal_hs_rank": "c*log(log(k))/log(log(log(k)))",
    "weyl_over_minimal_ratio_increases": True,
    "sample_ratios": [round(x, 6) for x in ratios],
    "necessary_not_sufficient": True,
    "conclusion": "sublogarithmic rank cannot reproduce Riemann-von Mangoldt zero density",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "riemann-weyl-shell-rank.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

