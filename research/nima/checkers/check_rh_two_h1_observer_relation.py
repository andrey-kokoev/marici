from fractions import Fraction
import json
from pathlib import Path


def h1_norm_squared(rate):
    # B(L)=L exp(-rate L)
    return (1 + rate * rate) / (4 * rate**3)


def h1_cross(rate_left, rate_right):
    total = rate_left + rate_right
    return 2 * (1 + rate_left * rate_right) / total**3


def wronskian_current(rate_left, rate_right):
    total = rate_left + rate_right
    return 2 * (rate_right - rate_left) / total**3


def total_transform_of_derivative_profile(_rate):
    # A=B', B(0)=0, and B(infinity)=0, so integral A=0.
    return Fraction(0)


y = Fraction(1, 3)
rate_plus = 1 + y
rate_minus = 1 - y

assert rate_plus > 0 and rate_minus > 0
assert total_transform_of_derivative_profile(rate_plus) == 0
assert total_transform_of_derivative_profile(rate_minus) == 0
assert h1_norm_squared(rate_plus) > 0
assert h1_norm_squared(rate_minus) > 0
assert h1_cross(rate_plus, rate_minus) > 0

current = wronskian_current(rate_plus, rate_minus)
assert current == -y / 2
assert wronskian_current(rate_minus, rate_plus) == -current
assert wronskian_current(Fraction(1), Fraction(1)) == 0

# The current is nonzero despite simultaneous zero-transform and H1 admission.
assert current != 0

result = {
    "schema": "marici.nima.rh-two-h1-observer-relation.v1",
    "horizontal_displacement": str(y),
    "plus_rate": str(rate_plus),
    "minus_rate": str(rate_minus),
    "plus_transform": "0",
    "minus_transform": "0",
    "plus_h1_norm_squared": str(h1_norm_squared(rate_plus)),
    "minus_h1_norm_squared": str(h1_norm_squared(rate_minus)),
    "cross_h1_pairing": str(h1_cross(rate_plus, rate_minus)),
    "wronskian_relational_current": str(current),
    "sector_exchange_reverses_current": True,
    "seam_current_zero": True,
    "off_seam_zero_states_admitted": True,
    "verdict": (
        "Two sector-local H1 zero observers plus trace-compatible sewing do "
        "not confine zeros. A natural Wronskian relationship detects horizontal "
        "displacement, but an additional theta-source law is required to force "
        "that current to vanish on a joined zero-state."
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-two-h1-observer-relation.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
