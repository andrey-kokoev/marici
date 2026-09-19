"""Bound the removable contribution around the certified critical Xi zero."""
import json
from pathlib import Path
from flint import acb, acb_series, arb, ctx

ctx.dps = 60
T_LO = arb("14.13472514173469")
T_HI = arb("14.13472514173470")
T_MID = (T_LO + T_HI) / 2
DELTA = arb("0.01")
# This interval contains [t-delta,t+delta] for every t in the zero bracket.
t_box = T_MID + arb(0, DELTA + (T_HI - T_LO) / 2)
s = acb_series([acb(arb("0.5"), t_box), acb(0, 1)], 2)
pi = acb(arb.pi())
xi_series = acb("0.5") * s * (s - 1) * pi ** (-s / 2) * (s / 2).gamma() * s.zeta()
derivative_bound = abs(xi_series[1]).upper()
# xi(x)=(x-t) integral_0^1 xi'(t+q(x-t))dq.  Integrating the
# resulting absolute integrand over |x-t|<=delta gives this bound.
local_bound = (
    2 * T_HI / (2 * T_LO - DELTA) * derivative_bound**2 * DELTA**2
)
certified = bool(local_bound < arb("2.14e-9"))
out = {
    "schema": "marici.voevodsky.first-xi-zero-removable-neighborhood-bound.v1",
    "precision_decimal_digits": ctx.dps,
    "zero_bracket": [str(T_LO), str(T_HI)],
    "neighborhood_half_width": str(DELTA),
    "xi_derivative_absolute_upper": str(derivative_bound),
    "absolute_integral_upper": str(local_bound.upper()),
    "accepted_upper": "2.14e-9",
    "interval_certified": certified,
    "identity": "xi(x)=(x-t)*integral_0^1 xi'(t+q(x-t))dq",
    "rh_proved": False,
}
path = Path(__file__).parents[1] / "results" / "arb-first-xi-zero-removable-neighborhood-bound.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
assert certified
