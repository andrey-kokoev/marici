"""Exact rational checks of the resummed one-prime Adams adjacency."""

from fractions import Fraction as F


r = F(1, 3)
log_weight = F(5, 2)


def closed(cosine):
    return 2 * log_weight * (r * cosine - r * r) / (
        1 - 2 * r * cosine + r * r
    )


maximum = closed(F(1))
minimum = closed(F(-1))
assert maximum == 2 * log_weight * r / (1 - r)
assert minimum == -2 * log_weight * r / (1 + r)
assert maximum == F(5, 2)
assert minimum == F(-5, 4)

# Partial sums at phase zero monotonically approach the exact maximum.
partials = [2 * log_weight * sum(r**k for k in range(1, n + 1)) for n in range(1, 8)]
assert all(left < right for left, right in zip(partials, partials[1:]))
assert all(value < maximum for value in partials)

result = {
    "radial_contraction": str(r),
    "log_weight_surrogate": str(log_weight),
    "maximum": str(maximum),
    "minimum": str(minimum),
    "extrema_asymmetric": abs(maximum) != abs(minimum),
    "zero_phase_partial_sums_monotone": True,
    "Adams_tower_geometric_resummation_verified": True,
    "global_unsmoothed_prime_adjacency_bounded": False,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "euler-ray-adjacency-resummation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
