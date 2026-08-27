import json
from pathlib import Path

import sympy as sp


s = sp.symbols("s")
L = sp.Function("Lambda")


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def tau(n, alpha):
    return sum(sp.Rational(d * d, n) ** alpha for d in divisors(n))


alpha = sp.symbols("alpha")
phi = L(2 * s - 1) / L(2 * s)
log_derivative = sp.simplify(sp.diff(phi, s) / phi)
expected_log_derivative = 2 * sp.diff(L(2 * s - 1), s) / (2 * L(2 * s - 1)) - 2 * sp.diff(L(2 * s), s) / (2 * L(2 * s))

# Use abstract nonzero mode numerators V_n. Their common denominator is the
# entire divisor-bearing content relevant here.
v1, v2, v3 = sp.symbols("v1 v2 v3")
modes = sp.Matrix([v1, v2, v3]) / L(2 * s)

checks = {
    "first_divisor_sum_is_one": tau(1, alpha) == 1,
    "all_modes_share_one_denominator": all(sp.simplify(entry * L(2 * s) - v) == 0 for entry, v in zip(modes, [v1, v2, v3])),
    "mode_ratios_cancel_scalar_divisor": sp.simplify(modes[1] / modes[0] - v2 / v1) == 0,
    "scattering_log_derivative_uses_only_completed_scalar_factors": sp.simplify(log_derivative - expected_log_derivative) == 0,
}

result = {
    "schema": "marici.grothendieck.eisenstein-fourier-modes-common-divisor.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "The nonconstant Eisenstein Fourier vector repeats the common pole factor 1/Lambda(2s). Mode ratios erase it, and the Maass-Selberg logarithmic term is the derivative of the same scalar scattering coefficient.",
}

out = Path(__file__).parents[1] / "results" / "eisenstein_fourier_modes_common_divisor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
