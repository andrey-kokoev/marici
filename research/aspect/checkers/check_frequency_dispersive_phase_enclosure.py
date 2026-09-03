#!/usr/bin/env python3
"""Exact band-wide phase, effect, margin, and sampling-gap diagnostics."""

import json
from fractions import Fraction as F
from pathlib import Path


def phase_radius(delta, beta_abs, curvature):
    return beta_abs * delta + curvature * delta * delta / 2


def spike(x):
    return 4 * x * (1 - x)


delta = F(1, 10)
beta = F(1, 10)
kappa = F(1, 5)
radius = phase_radius(delta, beta, kappa)
effect_radius = 2 * radius
nominal_margin = F(1, 20)
residual_margin = nominal_margin - effect_radius

hostile_delta = F(1, 2)
hostile_radius = phase_radius(hostile_delta, beta, kappa)
hostile_effect_radius = 2 * hostile_radius
hostile_residual = nominal_margin - hostile_effect_radius

sample_points = (F(0), F(1))
sample_max = max(abs(spike(point)) for point in sample_points)
midpoint_value = spike(F(1, 2))
lipschitz_constant = F(4)
grid_spacing = F(1)
lipschitz_coverage_bound = sample_max + lipschitz_constant * grid_spacing / 2
checks = {
    "phase_radius_is_exact": radius == F(11, 1000),
    "effect_radius_is_exact": effect_radius == F(11, 500),
    "nominal_margin_survives_band_uncertainty": residual_margin == F(7, 250) and residual_margin > 0,
    "hostile_phase_radius_is_exact": hostile_radius == F(3, 40),
    "hostile_effect_budget_exceeds_margin": hostile_effect_radius == F(3, 20) and hostile_effect_radius > nominal_margin,
    "hostile_certificate_is_rejected": hostile_residual == F(-1, 10),
    "endpoint_samples_miss_interior_spike": sample_max == 0 and midpoint_value == 1,
    "finite_samples_alone_do_not_cover_band": midpoint_value > sample_max,
    "lipschitz_gap_bound_covers_spike": lipschitz_coverage_bound >= midpoint_value,
    "lipschitz_bound_is_not_silently_tightened": lipschitz_coverage_bound == 2,
    "all_band_parameters_are_nonnegative": delta >= 0 and beta >= 0 and kappa >= 0,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.frequency-dispersive-phase-enclosure.v1", "status": "passed", "checks": checks, "phase_radius": str(radius), "effect_radius": str(effect_radius), "residual_margin": str(residual_margin), "hostile_residual": str(hostile_residual), "sample_max": str(sample_max), "interior_spike": str(midpoint_value), "lipschitz_coverage_bound": str(lipschitz_coverage_bound), "claim_boundary": "Compact-band slope/curvature enclosure; material dispersion and discontinuous response remain outside scope."}
output = Path(__file__).parents[1] / "results" / "frequency_dispersive_phase_enclosure.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "phase_radius": str(radius), "residual_margin": str(residual_margin)}, sort_keys=True))
