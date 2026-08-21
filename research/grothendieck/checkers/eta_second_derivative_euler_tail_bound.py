"""Exact bound for the twice-differentiated eta Euler-transform tail."""
import json
from fractions import Fraction
from pathlib import Path

depth = 120
majorant = Fraction(26, depth) + Fraction(4, depth**2) + Fraction(2, depth**3)
tail_bound = majorant / 2**depth
amplified_budget = tail_bound * 10 * 1_500_000_000_000_000
observed_gap_lower_bound = Fraction(34, 10**21)
assert amplified_budget < observed_gap_lower_bound

result = {
    "s_interval": ["1/2", "3/5"],
    "euler_depth": depth,
    "per_difference_second_derivative_bound": "26/k + 4/k^2 + 2/k^3",
    "eta_second_derivative_tail_bound": str(tail_bound),
    "amplified_eta_second_derivative_budget": str(amplified_budget),
    "observed_gap_lower_bound_used": str(observed_gap_lower_bound),
    "budget_below_observed_gap": amplified_budget < observed_gap_lower_bound,
    "exact_rational_arithmetic": True,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-second-derivative-euler-tail-bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
