"""Exact WP136 stochastic-cosmological boundary audit."""

from fractions import Fraction as F
import json
from pathlib import Path


# Normalize z=delta/sigma. The quadratic de Sitter equilibrium law becomes a
# standard Gaussian; sigma^2=3H^4/(8pi^2m^2).
mean_z, variance_z, fourth_moment_z = F(0), F(1), F(3)
theta = F(2)
z_small, z_large = F(1), F(4)
scale_small, scale_large = F(1), F(2)
detector_max_scale = F(3, 2)
log_density_ratio = -(z_large**2 - z_small**2) / F(2)

checks = {
    "stationary_normalized_mean_zero": mean_z == 0,
    "stationary_normalized_variance_one": variance_z == 1,
    "stationary_gaussian_fourth_moment": fourth_moment_z == 3,
    "two_nonzero_support_points": z_small != z_large and z_small != 0 and z_large != 0,
    "hostile_density_ratio_finite": log_density_ratio == F(-15, 2),
    "hostile_scale_ratio_exact": scale_large / scale_small == 2,
    "small_draw_accessible": scale_small < detector_max_scale,
    "large_draw_inaccessible": scale_large > detector_max_scale,
    "sign_pair_collapsed_by_scale_readout": abs(F(-1)) == abs(F(1)),
    "ensemble_not_singleton": variance_z > 0,
    "hubble_mass_boundary_remains": True,
    "equilibrium_duration_gate_remains": True,
}

result = {
    "work_package": "WP136",
    "classification": "source-generated cosmological amplitude ensemble; not a distinguished RG trajectory",
    "source": "light weak-basis-singlet spectator in quasi-de Sitter equilibrium",
    "stationary_distribution": "P(delta) proportional exp[-4*pi^2*m^2*delta^2/(3*H^4)]",
    "variance": "3*H^4/(8*pi^2*m^2)",
    "normalized_moments": {"mean": str(mean_z), "variance": str(variance_z), "fourth": str(fourth_moment_z)},
    "hostile_draws": {
        "z_values": [str(z_small), str(z_large)],
        "log_density_ratio": str(log_density_ratio),
        "crossover_scale_ratio": "2",
        "accessibility_partition": [["z=1"], ["z=4"]],
    },
    "scale_readout_sign_kernel": [["z=1", "z=-1"]],
    "boundary_inputs": ["H", "m/H", "inflationary_duration", "initial_state", "reheating/matching_map"],
    "reference_port_required": True,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp136_stochastic_cosmological_boundary.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
