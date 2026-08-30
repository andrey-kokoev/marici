"""Exact rational bound for the differentiated Euler-transform eta tail."""
import json
from fractions import Fraction
from pathlib import Path


depth = 120
# For k>=N and 1/2<=s<=3/5:
# |d/ds Delta^k n^-s|_(n=1) <= 3/k + 1/k^2.
# Sum 2^(-k-1) from k=N onward is 2^-N.
tail_bound = (Fraction(3, depth) + Fraction(1, depth * depth)) / 2**depth

# Carry a deliberately generous factor ten for eta denominators and the
# logarithmic-derivative quotient before applying the prior stencil scale.
nonlinear_safety_factor = 10
boundary_stencil_amplification = 1_500_000_000_000_000
amplified_budget = tail_bound * nonlinear_safety_factor * boundary_stencil_amplification
observed_gap_lower_decimal = Fraction(925, 10**17)  # 9.25e-15, rounded down

assert amplified_budget < observed_gap_lower_decimal

result = {
    "s_interval": ["1/2", "3/5"],
    "euler_depth": depth,
    "per_difference_derivative_bound": "3/k + 1/k^2",
    "differentiated_eta_tail_bound": str(tail_bound),
    "nonlinear_safety_factor": nonlinear_safety_factor,
    "boundary_stencil_amplification": boundary_stencil_amplification,
    "amplified_eta_derivative_budget": str(amplified_budget),
    "observed_gap_lower_bound_used": str(observed_gap_lower_decimal),
    "budget_below_observed_gap": amplified_budget < observed_gap_lower_decimal,
    "exact_rational_arithmetic": True,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-derivative-euler-tail-bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
