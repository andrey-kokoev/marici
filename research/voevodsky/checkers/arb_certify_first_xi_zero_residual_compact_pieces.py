"""Certify the nonsingular compact pieces of the Evans Hilbert residual."""
import json
from pathlib import Path
from flint import acb, arb, ctx

ctx.dps = 35
LO = arb("14.13472514173469")
HI = arb("14.13472514173470")
T = (LO + HI) / 2 + arb(0, (HI - LO) / 2)
DELTA = arb("0.01")
PI = acb(arb.pi())


def xi_on_critical_parameter(x):
    s = acb(arb("0.5")) + acb(0, 1) * x
    return acb("0.5") * s * (s - 1) * PI ** (-s / 2) * (s / 2).gamma() * s.zeta()


def integrand(x, analytic):
    q = xi_on_critical_parameter(x)
    # q is real on the real integration path. q^2 is its analytic extension;
    # using q*conj(q) here would invalidate complex-box analytic quadrature.
    return q * q * acb(2 * T) / (x * x - acb(T * T))


def integrate(a, b):
    return acb.integral(integrand, a, b, abs_tol=arb("1e-12"), eval_limit=500000)


left = integrate(arb(0), LO - DELTA)
right = integrate(HI + DELTA, arb(50))
total = left + right
# Previously certified absolute allowances.
local_allowance = arb("2.14e-9")
tail_allowance = arb("0.0015")
complete_upper = total.real.upper() + local_allowance + tail_allowance
certified_negative = bool(complete_upper < 0)
out = {
    "schema": "marici.voevodsky.first-xi-zero-evans-residual-compact-pieces.v1",
    "precision_decimal_digits": ctx.dps,
    "zero_bracket": [str(LO), str(HI)],
    "excluded_half_width": str(DELTA),
    "left_compact_integral": str(left),
    "right_compact_integral": str(right),
    "compact_sum": str(total),
    "local_absolute_allowance": str(local_allowance),
    "tail_absolute_allowance": str(tail_allowance),
    "complete_residual_upper": str(complete_upper),
    "complete_residual_strictly_negative": certified_negative,
    "interval_certified": certified_negative,
    "rh_proved": False,
}
path = Path(__file__).parents[1] / "results" / "arb-first-xi-zero-evans-residual-compact-pieces.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
assert certified_negative
