"""Exact WP134 dimensional-transmutation authority audit."""

from fractions import Fraction as F
import json
from pathlib import Path


# One-loop asymptotically free beta function beta(g)=-b g^3.
b = F(1, 2)
log_mu_0 = F(0)
inverse_g0_sq = F(4)


def log_generated_scale(log_mu, inverse_g_sq):
    return log_mu - inverse_g_sq / (F(2) * b)


log_lambda_0 = log_generated_scale(log_mu_0, inverse_g0_sq)

# Change renormalization presentation by log(mu_1/mu_0)=2 and run the
# coupling on the same trajectory: 1/g_1^2=1/g_0^2+2b log(mu_1/mu_0).
log_mu_1 = F(2)
inverse_g1_sq = inverse_g0_sq + F(2) * b * (log_mu_1 - log_mu_0)
log_lambda_1 = log_generated_scale(log_mu_1, inverse_g1_sq)

# A genuinely different boundary packet: same dimensionless coupling value
# declared at a physical reference scale shifted by three log units.
log_mu_hostile = F(3)
inverse_g_hostile_sq = inverse_g0_sq
log_lambda_hostile = log_generated_scale(log_mu_hostile, inverse_g_hostile_sq)

checks = {
    "asymptotic_freedom_coefficient_positive": b > 0,
    "baseline_generated_log_scale": log_lambda_0 == F(-4),
    "running_inverse_coupling_exact": inverse_g1_sq == F(6),
    "rg_presentation_invariance": log_lambda_1 == log_lambda_0,
    "same_trajectory_boundary_pair_changes_coherently": (log_mu_1, inverse_g1_sq) != (log_mu_0, inverse_g0_sq),
    "hostile_boundary_generated_log_scale": log_lambda_hostile == F(-1),
    "hostile_boundary_changes_physical_scale": log_lambda_hostile - log_lambda_0 == F(3),
    "coupling_boundary_is_required": inverse_g0_sq != 0,
    "scale_boundary_is_required": log_mu_hostile != log_mu_0,
    "rg_invariance_does_not_imply_unique_trajectory": log_lambda_hostile != log_lambda_0,
}

result = {
    "work_package": "WP134",
    "classification": "dimensional transmutation is an RG-invariant conditional scale selector, not a source-free absolute-scale selector",
    "beta_function": "beta(g)=-b*g^3",
    "b": str(b),
    "baseline_boundary": {"log_mu": str(log_mu_0), "inverse_g_squared": str(inverse_g0_sq), "log_Lambda": str(log_lambda_0)},
    "same_trajectory_presentation": {"log_mu": str(log_mu_1), "inverse_g_squared": str(inverse_g1_sq), "log_Lambda": str(log_lambda_1)},
    "hostile_boundary": {"log_mu": str(log_mu_hostile), "inverse_g_squared": str(inverse_g_hostile_sq), "log_Lambda": str(log_lambda_hostile)},
    "hostile_log_scale_residual": str(log_lambda_hostile - log_lambda_0),
    "absolute_scale_selected_without_boundary": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp134_dimensional_transmutation_authority.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
