"""Conservative error budget for certifying the central concavity scan."""
import json
from decimal import Decimal, localcontext
from pathlib import Path


with localcontext() as context:
    context.prec = 90
    D = Decimal
    eta_depth = 120
    eta_value_remainder = D(2) ** (-eta_depth)
    # Eight retained Bernoulli terms end at B_16; B_18 is first omitted.
    b18 = D(43867) / D(798)
    digamma_recurrence_target = 100
    digamma_remainder = b18 / (D(18) * D(digamma_recurrence_target) ** 18)
    smallest_t = D("1e-8")
    finite_difference_step = smallest_t * D("1e-3")
    central_prefactor_scale = 1 / smallest_t.sqrt()
    stencil_amplification = D(18) / (D(12) * finite_difference_step)
    total_amplification = central_prefactor_scale * stencil_amplification
    eta_value_slope_budget = eta_value_remainder * total_amplification
    digamma_slope_budget = digamma_remainder * total_amplification / 2
    observed_minimum_gap = D("3.4e-20")

result = {
    "eta_depth": eta_depth,
    "eta_value_euler_remainder_bound": str(eta_value_remainder),
    "digamma_first_omitted_term_bound": str(digamma_remainder),
    "digamma_recurrence_target": digamma_recurrence_target,
    "pessimistic_boundary_slope_amplification": str(total_amplification),
    "eta_value_amplified_budget": str(eta_value_slope_budget),
    "digamma_independent_value_amplified_budget": str(digamma_slope_budget),
    "observed_minimum_chord_gap": str(observed_minimum_gap),
    "eta_value_budget_below_observed_gap": eta_value_slope_budget < observed_minimum_gap,
    "digamma_independent_value_budget_below_observed_gap": digamma_slope_budget < observed_minimum_gap,
    "remaining_uncertified_terms": [
        "outward-rounded propagation through the complete nonlinear expression",
        "rigorous finite-difference truncation bound",
    ],
    "certification_complete": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "central-concavity-certification-error-budget.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
