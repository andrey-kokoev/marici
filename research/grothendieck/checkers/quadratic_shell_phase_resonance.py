"""Finite diagnostic for the quadratic shell resonance lattice."""

import cmath
import math


def sinc(t):
    return 1.0 if t == 0 else math.sin(t) / t


def leading_residual(t, k):
    return (sinc(t) - 1) * cmath.exp(-2j * t * k - 0.5j * t) / k


assert leading_residual(0, 10) == 0
partial = [sum(leading_residual(math.pi, k) for k in range(1, n + 1)) for n in (10, 100, 1000, 10000)]
magnitudes = [abs(x) for x in partial]
assert all(a < b for a, b in zip(magnitudes, magnitudes[1:]))

generic_t = 0.7
generic_partial = sum(leading_residual(generic_t, k) for k in range(1, 100_001))
assert abs(generic_partial) < 1

result = {
    "static_T_zero_leading_residual": "0",
    "relative_factor": "sinc(T)-1",
    "nonzero_resonance_lattice": "T=n*pi",
    "resonant_partial_sum_magnitudes": [round(x, 6) for x in magnitudes],
    "generic_oscillatory_partial_sum_bounded_in_test": True,
    "shell_center_unitary_surrogate_has_aliasing_singularities": True,
    "gamma_resolvent_singularity_claimed": False,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "quadratic-shell-phase-resonance.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
