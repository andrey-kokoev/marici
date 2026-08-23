"""Exact algebra audit of the central-fiber adjacent-band transport failure."""
import json
from fractions import Fraction as Q
from pathlib import Path


# After cancellation of alpha*sin(bD)>0 on S=0, domination requires
# transported_density/base_density <= D/(D+L).
L = Q(3, 2)
positive_density_ratio_lower = Q(1, 100)

# Continuity makes the actual theta density ratio exceed some fixed positive
# lower bound near D=0. This rational witness audits the universal asymptotic
# contradiction once such a lower bound is fixed.
D = Q(1, 1000)
required_ratio_upper = D / (D + L)
assert required_ratio_upper < positive_density_ratio_lower

# The kernel magnitudes on the S=0 fiber differ by the exact factor below;
# the common positive alpha*sin(bD) cancels.
base_kernel_factor = D
transported_negative_kernel_factor = D + L
assert transported_negative_kernel_factor > base_kernel_factor > 0

result = {
    "canonical_transport": "(S,D) -> (S,D+pi/b)",
    "jacobian": "1",
    "orientation_preserving": True,
    "theta_labels_preserved": True,
    "tested_faithful_fiber": "S=0 with ordered label pair (n,m) retained",
    "required_density_ratio": "D/(D+L)",
    "required_ratio_tends_to_zero": True,
    "actual_labelled_theta_ratio_limit": "phi_n(L/2) phi_m(L/2) / (phi_n(0) phi_m(0)) > 0",
    "rational_L_and_D": [str(L), str(D)],
    "rational_required_ratio_upper": str(required_ratio_upper),
    "positive_continuity_lower_bound_test": str(positive_density_ratio_lower),
    "pointwise_adjacent_shift_falsified": True,
    "integrated_expectation_falsified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-adjacent-band-transport-first-falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
