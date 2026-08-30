"""Finite exact audit of the heat-kernel/zero-character adjacency relation."""

from fractions import Fraction as F


# Exact positive surrogates for Gaussian-damped von Mangoldt coefficients.
coefficients = [F(1, 2), F(1, 3), F(1, 7), F(1, 11)]


def multiplier(cosines):
    return 2 * sum(weight * cosine for weight, cosine in zip(coefficients, cosines))


zero_character = multiplier([F(1)] * len(coefficients))
assert zero_character == 2 * sum(coefficients)

# Every character value is bounded by the trivial character.
hostile_cosines = [F(-1), F(1, 2), F(-1, 3), F(3, 4)]
hostile_value = multiplier(hostile_cosines)
assert abs(hostile_value) <= zero_character

# Omitting the universal scalar factor, the negative prime heat value is one
# half of the negative paired-adjacency zero character.
prime_heat_without_prefactor = -sum(coefficients)
assert prime_heat_without_prefactor == -zero_character / 2

result = {
    "coefficient_count": len(coefficients),
    "zero_character": str(zero_character),
    "adjacency_norm": str(zero_character),
    "hostile_nonzero_character": str(hostile_value),
    "prime_heat_is_negative_half_zero_character_before_prefactor": True,
    "absolute_convergence_requires_positive_smoothing_time": True,
    "scalar_zero_character_controls_full_completed_operator": False,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "gaussian-smoothed-prime-adjacency.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
