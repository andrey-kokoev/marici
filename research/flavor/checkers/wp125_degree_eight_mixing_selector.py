"""Exact WP125 degree-eight mixing-selector audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def c_of(x):
    """Tr(Hu R Hd R^T) for Hu=(3,2,1), Hd=(6,4,1), x=sin^2(theta)."""
    return F(27) - F(2) * x


def k_of(x):
    """Frobenius norm squared of the commutator in the 1-2 rotation slice."""
    return F(8) * x * (F(1) - x)


def potential(x, a=F(28), q=F(25)):
    return a * c_of(x) - q * k_of(x)


a, q = F(28), F(25)
x_star = F(1, 2) + a / (F(8) * q)
first_derivative = -F(2) * a - F(8) * q + F(16) * q * x_star
second_derivative = F(16) * q

checks = {
    "selected_x_exact": x_star == F(16, 25),
    "selected_rational_sine": x_star == F(4, 5) ** 2,
    "stationary_exact": first_derivative == 0,
    "strict_local_minimum": second_derivative == F(400) and second_derivative > 0,
    "interior_point": F(0) < x_star < F(1),
    "noncommuting_at_minimum": k_of(x_star) == F(1152, 625) and k_of(x_star) > 0,
    "below_aligned_endpoint": potential(x_star) == F(16852, 25) and potential(x_star) < potential(F(0)),
    "below_swapped_endpoint": potential(x_star) < potential(F(1)),
    "coefficient_ratio_controls_angle": a / q == F(28, 25),
    "remove_degree_eight_restores_endpoint_slope": -F(2) * a != 0,
}

result = {
    "work_package": "WP125",
    "classification": "first conditional interior-mixing selector; numerical angle remains coefficient input",
    "degree_threshold": 8,
    "potential_slice": "V(x)=a(27-2x)-8q*x(1-x)",
    "coefficients": {"a": str(a), "q": str(q), "a_over_q": str(a / q)},
    "selected": {
        "x_equals_sin_squared_theta": str(x_star),
        "commutator_norm_squared": str(k_of(x_star)),
        "potential": str(potential(x_star)),
        "first_derivative": str(first_derivative),
        "second_derivative": str(second_derivative),
    },
    "endpoint_potentials": {"aligned": str(potential(F(0))), "swapped_12": str(potential(F(1)))},
    "reference_port_required": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp125_degree_eight_mixing_selector.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
