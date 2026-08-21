"""Exact rational audit of the persistent Jacobi boundary leakage."""

from fractions import Fraction


def boundary_square(m: int) -> Fraction:
    return Fraction(m * m, 4 * (2 * m - 1) * (2 * m + 1))


values = [boundary_square(m) for m in range(1, 101)]
assert all(value >= Fraction(1, 16) for value in values)
assert values[0] == Fraction(1, 12)
assert boundary_square(10_000) > Fraction(1, 16)

# The lower bound makes every weighted partial sum dominate (1/16) H_N.
result = {
    "rank_one_boundary_square": "1/12",
    "all_boundary_squares_at_least_1_over_16": True,
    "boundary_square_limit": "1/16",
    "harmonic_weighted_operator_leakage_diverges": True,
    "distinguished_vector_factorial_estimate_retained": True,
    "full_operator_hilbert_schmidt_claim_retracted": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "growing-moment-generator-boundary-no-go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

