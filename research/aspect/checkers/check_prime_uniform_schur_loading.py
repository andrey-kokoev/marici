"""Exact-rational assembly of the prime-uniform theta-mass Schur margin."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path


def q(s: str) -> F:
    return F(s)


def log3_interval(terms: int = 12):
    # log(3)=2*atanh(1/2)=2*sum_{n>=0}(1/2)^(2n+1)/(2n+1).
    lo = 2 * sum(F(1, 2) ** (2*n + 1) / (2*n + 1) for n in range(terms))
    # Bound every omitted denominator below by 2N+1 and sum the geometric tail.
    tail = 2 * (F(1, 2) ** (2*terms + 1)) / (2*terms + 1) / (1 - F(1, 4))
    return lo, lo + tail


def alternating_sum(x: F, terms: int) -> F:
    return sum(((-1) ** n) * x ** (2*n + 1) / (factorial(n) * (2*n + 1)) for n in range(terms))


sqrtpi_lo, sqrtpi_hi = q("1.77245"), q("1.77246")
pi_lo, pi_hi = q("3.14159"), q("3.14160")
log3_lo, log3_hi = log3_interval()
x_lo = sqrtpi_lo * log3_lo / 2
x_hi = sqrtpi_hi * log3_hi / 2

# Ten terms are a lower alternating sum; 2/sqrt(pi) is bounded below by 2/1.77246.
A3_lower = F(2, 1) / sqrtpi_hi * alternating_sum(x_lo, 10)
T3_upper = 1 - A3_lower
p_ge_3_lhs_upper = T3_upper ** 2 + T3_upper
# xi(1/2)<1/2 implies 8(1-M)^2>2; use A(log 3)>4/5.
p_ge_3_rhs_lower = 2 * q("0.8") ** 3
p_ge_3_margin_lower = p_ge_3_rhs_lower - (q("0.2") ** 2 + q("0.2"))

# Prime-two consequences of the independently certified five normal bounds.
a2_lower = q("0.6")
d2_upper = 2*q("0.078")*(q("0.362")+q("0.017")) + 2*q("0.033")*(q("0.5")+q("0.017"))
p2_rhs_lower = 2 * a2_lower  # again from xi(1/2)<1/2
p2_margin_lower = p2_rhs_lower - d2_upper

hostile_target = q("0.9")
hostile_residual = hostile_target - A3_lower
checks = {
    "sqrtpi_bounds_are_outward": sqrtpi_lo**2 < pi_lo and sqrtpi_hi**2 > pi_hi,
    "log3_series_interval_is_ordered": log3_lo < log3_hi,
    "erf_argument_below_one": 0 < x_lo < x_hi < 1,
    "A_log3_strictly_above_four_fifths": A3_lower > q("0.8"),
    "p_ge_3_envelope_margin_above_0.784": p_ge_3_lhs_upper < q("0.24") and p_ge_3_margin_lower == q("0.784"),
    "prime_two_d_squared_below_point_one": d2_upper == q("0.093246") < q("0.1"),
    "prime_two_mass_margin_above_1.1": p2_margin_lower > q("1.1"),
    "deliberate_A_log3_above_point_nine_is_not_certified": hostile_residual > 0,
}
result = {
    "status": "pass" if all(checks.values()) else "fail",
    "arithmetic": "fractions.Fraction only; no floating-point evaluation",
    "assumption": "source theta proof xi(1/2)<1/2",
    "checks": checks,
    "log3_interval": [str(log3_lo), str(log3_hi)],
    "A_log3_lower": str(A3_lower),
    "p_ge_3_lhs_upper_from_computed_A": str(p_ge_3_lhs_upper),
    "p_ge_3_uniform_margin_lower": str(p_ge_3_margin_lower),
    "prime_two_d_squared_upper": str(d2_upper),
    "prime_two_uniform_margin_lower": str(p2_margin_lower),
    "hostile_point_nine_residual": str(hostile_residual),
    "claim_boundary": "analytic theta-mass Schur inequality only; constructor identifications remain separate",
}
out = Path("research/aspect/results/prime_uniform_schur_loading.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
