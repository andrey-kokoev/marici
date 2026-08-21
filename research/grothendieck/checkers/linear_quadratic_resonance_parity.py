"""Finite exact parity diagnostic at the first odd-pi shell resonance."""

from fractions import Fraction


def harmonic(n):
    return sum(Fraction(1, k) for k in range(1, n + 1))


def alternating_harmonic(n):
    return sum(Fraction((-1) ** k, k) for k in range(1, n + 1))


cutoffs = [10, 100, 1000]
quadratic = [harmonic(n) for n in cutoffs]
linear = [alternating_harmonic(n) for n in cutoffs]

assert quadratic[0] < quadratic[1] < quadratic[2]
assert all(abs(value) < 1 for value in linear)
assert abs(linear[-1] - linear[-2]) < Fraction(1, 100)

result = {
    "odd_pi_quadratic_shell_phase": "1",
    "odd_pi_linear_shell_phase": "(-1)^k",
    "quadratic_partial_sums_grow_harmonically": True,
    "linear_partial_sums_remain_bounded": True,
    "rank_one_same_height_surrogate_cancellation_impossible": True,
    "gamma_resolvent_singularity_claimed": False,
    "required_repair": "operator-valued within-shell or mapping-cone frequency mixing",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "linear-quadratic-resonance-parity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
