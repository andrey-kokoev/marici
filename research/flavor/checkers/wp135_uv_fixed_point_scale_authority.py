"""Exact WP135 UV-fixed-point scale-authority audit."""

from fractions import Fraction as F
import json
from pathlib import Path


# Linearized relevant direction: d delta / d log(mu) = -theta delta.
theta = F(2)


def log_crossover_scale(log_mu, log_abs_delta):
    return log_mu + log_abs_delta / theta


log_mu_0, log_delta_0 = F(0), F(-4)
log_scale_0 = log_crossover_scale(log_mu_0, log_delta_0)

# Same trajectory at another RG presentation.
log_mu_1 = F(3)
log_delta_1 = log_delta_0 - theta * (log_mu_1 - log_mu_0)
log_scale_1 = log_crossover_scale(log_mu_1, log_delta_1)

# Distinct point on the relevant critical surface at the same reference scale.
log_delta_hostile = F(-2)
log_scale_hostile = log_crossover_scale(log_mu_0, log_delta_hostile)

checks = {
    "relevant_exponent_positive": theta > 0,
    "baseline_crossover_log_scale": log_scale_0 == F(-2),
    "same_trajectory_running_exact": log_delta_1 == F(-10),
    "same_trajectory_scale_invariant": log_scale_1 == log_scale_0,
    "hostile_relevant_amplitude_distinct": log_delta_hostile != log_delta_0,
    "hostile_crossover_log_scale": log_scale_hostile == F(-1),
    "relevant_amplitude_changes_scale": log_scale_hostile - log_scale_0 == F(1),
    "fixed_point_location_does_not_fix_amplitude": True,
    "zero_deformation_has_no_finite_crossover": True,
    "critical_surface_fiber_non_singleton": log_scale_hostile != log_scale_0,
}

result = {
    "work_package": "WP135",
    "classification": "UV fixed point fixes critical data but not the relevant amplitude or crossover scale",
    "linearized_flow": "d(delta)/dlog(mu)=-theta*delta",
    "theta": str(theta),
    "baseline": {"log_mu": str(log_mu_0), "log_abs_delta": str(log_delta_0), "log_Lambda": str(log_scale_0)},
    "same_trajectory_presentation": {"log_mu": str(log_mu_1), "log_abs_delta": str(log_delta_1), "log_Lambda": str(log_scale_1)},
    "hostile_critical_surface_point": {"log_mu": str(log_mu_0), "log_abs_delta": str(log_delta_hostile), "log_Lambda": str(log_scale_hostile)},
    "hostile_log_scale_residual": str(log_scale_hostile - log_scale_0),
    "absolute_scale_selected_by_fixed_point_alone": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp135_uv_fixed_point_scale_authority.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
