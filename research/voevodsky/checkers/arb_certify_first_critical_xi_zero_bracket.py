"""Certify a critical-line Xi zero in a short interval by an Arb sign change.

This proves existence only. It does not prove uniqueness in the bracket or that
this is globally the first nontrivial zero.
"""
import json
from pathlib import Path
from flint import acb, arb, ctx

ctx.dps = 80
PI = arb.pi()
LEFT = "14.13472514173469"
RIGHT = "14.13472514173470"


def completed_xi(t_text: str) -> acb:
    s = acb(arb("0.5"), arb(t_text))
    return acb("0.5") * s * (s - 1) * acb(PI) ** (-s / 2) * (s / 2).gamma() * s.zeta()


left_value = completed_xi(LEFT)
right_value = completed_xi(RIGHT)
left_positive = bool(left_value.real > 0)
right_negative = bool(right_value.real < 0)
imaginary_parts_contain_zero = bool(left_value.imag.contains(0) and right_value.imag.contains(0))
certified = left_positive and right_negative and imaginary_parts_contain_zero

out = {
    "schema": "marici.voevodsky.first-critical-xi-zero-bracket.v1",
    "precision_decimal_digits": ctx.dps,
    "interval": [LEFT, RIGHT],
    "width": "1e-14",
    "left_xi": str(left_value),
    "right_xi": str(right_value),
    "left_strictly_positive": left_positive,
    "right_strictly_negative": right_negative,
    "endpoint_imaginary_parts_contain_zero": imaginary_parts_contain_zero,
    "critical_line_xi_is_real": True,
    "zero_exists_by_intermediate_value": certified,
    "uniqueness_in_interval_certified": False,
    "globally_first_zero_certified": False,
    "rh_proved": False,
}
path = Path(__file__).parents[1] / "results" / "arb-certified-first-critical-xi-zero-bracket.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
assert certified
