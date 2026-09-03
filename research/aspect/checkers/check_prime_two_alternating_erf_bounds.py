"""Exact-rational certificates for the prime-two normal-CDF bounds."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path


def q(text: str) -> F:
    return F(text)


def alternating_sum(x: F, terms: int) -> F:
    return sum(((-1) ** n) * x ** (2 * n + 1) / (factorial(n) * (2 * n + 1)) for n in range(terms))


def erf_interval(x_lo: F, x_hi: F, lower_terms: int = 10, upper_terms: int = 11):
    # Ten terms (n=0,...,9) give the lower sum; eleven give the upper sum.
    series_lo = alternating_sum(x_lo, lower_terms)
    series_hi = alternating_sum(x_hi, upper_terms)
    pref_lo = F(2, 1) / q("1.77246")
    pref_hi = F(2, 1) / q("1.77245")
    return pref_lo * series_lo, pref_hi * series_hi


def phi_interval(z_lo: F, z_hi: F, lower_terms: int = 10, upper_terms: int = 11):
    sqrt2_lo, sqrt2_hi = q("1.41421"), q("1.41422")
    erf_lo, erf_hi = erf_interval(z_lo / sqrt2_hi, z_hi / sqrt2_lo, lower_terms, upper_terms)
    return (1 + erf_lo) / 2, (1 + erf_hi) / 2


def q_interval(z_lo: F, z_hi: F, lower_terms: int = 10, upper_terms: int = 11):
    phi_lo, phi_hi = phi_interval(z_lo, z_hi, lower_terms, upper_terms)
    return 1 - phi_hi, 1 - phi_lo


def shown(interval):
    return [str(interval[0]), str(interval[1])]


pi_lo, pi_hi = q("3.14159"), q("3.14160")
log2_lo, log2_hi = q("0.693147"), q("0.693148")
sqrt2_lo, sqrt2_hi = q("1.41421"), q("1.41422")
sqrt3_lo, sqrt3_hi = q("1.73205"), q("1.73206")
sqrtpi_lo, sqrtpi_hi = q("1.77245"), q("1.77246")
u_lo, u_hi = q("1.22856"), q("1.22859")

input_checks = {
    "pi_encloses_square_root_bounds": sqrtpi_lo ** 2 < pi_lo and sqrtpi_hi ** 2 > pi_hi,
    "sqrt2_bounds_square_outward": sqrt2_lo ** 2 < 2 < sqrt2_hi ** 2,
    "sqrt3_bounds_square_outward": sqrt3_lo ** 2 < 3 < sqrt3_hi ** 2,
    "u_product_enclosed": sqrtpi_lo * log2_lo > u_lo and sqrtpi_hi * log2_hi < u_hi,
}

arguments = {
    "u": (u_lo, u_hi),
    "three_u_over_two": (F(3, 2) * u_lo, F(3, 2) * u_hi),
    "u_over_two_sqrt3": (u_lo / (2 * sqrt3_hi), u_hi / (2 * sqrt3_lo)),
    "sqrt3_u": (sqrt3_lo * u_lo, sqrt3_hi * u_hi),
}

intervals = {
    "Phi_u": phi_interval(*arguments["u"]),
    "Phi_three_u_over_two": phi_interval(*arguments["three_u_over_two"]),
    "Q_u_over_two_sqrt3": q_interval(*arguments["u_over_two_sqrt3"]),
    "Q_sqrt3_u": q_interval(*arguments["sqrt3_u"]),
}

target_checks = {
    "0.8903_lt_Phi_u_lt_0.8905": q("0.8903") < intervals["Phi_u"][0] < intervals["Phi_u"][1] < q("0.8905"),
    "0.9672_lt_Phi_3u2_lt_0.9675": q("0.9672") < intervals["Phi_three_u_over_two"][0] < intervals["Phi_three_u_over_two"][1] < q("0.9675"),
    "0.3613_lt_Q_small_lt_0.3616": q("0.3613") < intervals["Q_u_over_two_sqrt3"][0] < intervals["Q_u_over_two_sqrt3"][1] < q("0.3616"),
    "0.0165_lt_Q_large_lt_0.0169": q("0.0165") < intervals["Q_sqrt3_u"][0] < intervals["Q_sqrt3_u"][1] < q("0.0169"),
}

# Hostile control: two/three terms are valid but too wide to certify every coarse target.
coarse = phi_interval(*arguments["three_u_over_two"], lower_terms=2, upper_terms=3)
hostile_residual = coarse[1] - coarse[0]
hostile_check = hostile_residual > q("0.0005")

checks = {**input_checks, **target_checks, "deliberate_short_series_is_too_wide": hostile_check}
result = {
    "status": "pass" if all(checks.values()) else "fail",
    "arithmetic": "fractions.Fraction only; no floating-point evaluation",
    "checks": checks,
    "argument_intervals": {name: shown(value) for name, value in arguments.items()},
    "certified_intervals": {name: shown(value) for name, value in intervals.items()},
    "hostile_short_series_width": str(hostile_residual),
}
output = Path("research/aspect/results/prime_two_alternating_erf_bounds.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
