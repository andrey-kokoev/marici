#!/usr/bin/env python3
"""Exact one-pole dispersion derivative, pole-exclusion, and margin checks."""

import json
from fractions import Fraction as F
from pathlib import Path


def fprime(omega, resonance):
    return (resonance**2 + omega**2) / (resonance**2 - omega**2)**2


def fsecond(omega, resonance):
    return 2 * omega * (3 * resonance**2 + omega**2) / (resonance**2 - omega**2)**3


def pole_free(resonance_low, band_low, band_high):
    return not (band_low <= resonance_low <= band_high) and resonance_low > band_high


L_MAX = F(1, 90)
N_MAX = F(8, 5)
A_MAX = F(1, 8)
OMEGA_MIN = F(2)
BAND_LOW, CENTER, BAND_HIGH = F(2, 5), F(1, 2), F(3, 5)
DELTA = F(1, 10)

slope_bound = L_MAX * (N_MAX + A_MAX * fprime(CENTER, OMEGA_MIN))
curvature_bound = L_MAX * A_MAX * fsecond(BAND_HIGH, OMEGA_MIN)
phase_radius = slope_bound * DELTA + curvature_bound * DELTA**2 / 2
effect_radius = 2 * phase_radius
nominal_margin = F(1, 20)
residual_margin = nominal_margin - effect_radius
pole_gap = OMEGA_MIN - BAND_HIGH

# Endpoint monotonicity checks for the positive source box.
frequency_curvature_order = fsecond(BAND_LOW, OMEGA_MIN) < fsecond(BAND_HIGH, OMEGA_MIN)
resonance_order = fprime(CENTER, F(5, 2)) < fprime(CENTER, OMEGA_MIN) and fsecond(BAND_HIGH, F(5, 2)) < fsecond(BAND_HIGH, OMEGA_MIN)
hostile_resonance = F(1, 2)
checks = {
    "admitted_band_is_pole_free": pole_free(OMEGA_MIN, BAND_LOW, BAND_HIGH),
    "pole_gap_is_exact": pole_gap == F(7, 5),
    "slope_bound_is_positive": slope_bound > 0,
    "curvature_bound_is_positive": curvature_bound > 0,
    "curvature_increases_across_positive_band": frequency_curvature_order,
    "derivative_bounds_decrease_with_resonance": resonance_order,
    "phase_radius_is_positive": phase_radius > 0,
    "effect_radius_fits_nominal_margin": effect_radius < nominal_margin,
    "continuous_mode_residual_is_positive": residual_margin > 0,
    "hostile_resonance_intersects_band": BAND_LOW <= hostile_resonance <= BAND_HIGH,
    "hostile_parameter_box_is_rejected_before_derivatives": not pole_free(hostile_resonance, BAND_LOW, BAND_HIGH),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.source-material-dispersion-bounds.v1", "status": "passed", "checks": checks, "slope_bound": str(slope_bound), "curvature_bound": str(curvature_bound), "phase_radius": str(phase_radius), "effect_radius": str(effect_radius), "residual_margin": str(residual_margin), "pole_gap": str(pole_gap), "claim_boundary": "One-pole rational source-model prototype; not fitted material evidence."}
output = Path(__file__).parents[1] / "results" / "source_material_dispersion_bounds.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "phase_radius": str(phase_radius), "residual_margin": str(residual_margin)}, sort_keys=True))
