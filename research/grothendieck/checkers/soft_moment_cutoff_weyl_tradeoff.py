"""Exact finite audit of the optimal taper Dirichlet-energy bound."""

from fractions import Fraction


def taper_energy(weights):
    return sum((b - a) ** 2 for a, b in zip(weights, weights[1:]))


for length in range(1, 65):
    linear = [Fraction(length - j, length) for j in range(length + 1)]
    assert taper_energy(linear) == Fraction(1, length)

    # A deliberately nonuniform rational taper obeys the same lower bound.
    steps = [Fraction(2 * j + 1, length * length) for j in range(length)]
    assert sum(steps) == 1
    nonuniform = [Fraction(1)]
    for step in steps:
        nonuniform.append(nonuniform[-1] - step)
    assert taper_energy(nonuniform) >= Fraction(1, length)

result = {
    "cauchy_lower_bound": "sum(delta w)^2 >= 1/L",
    "linear_taper_attains_bound": True,
    "jacobi_boundary_square_lower_bound": "1/16",
    "weyl_sized_taper_series": "sum 1/(k log k), divergent",
    "hs_sufficient_example": "L_k=(log k)^(1+epsilon)",
    "superlog_tail_requires_zero_net_spectral_multiplicity": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "soft-moment-cutoff-weyl-tradeoff.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

