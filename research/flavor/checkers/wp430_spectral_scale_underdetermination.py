"""Exact scale-orbit obstruction for frequency-resolved threshold packets."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp131 = json.loads((root / "results" / "wp131_sm_portal_accessibility.json").read_text(encoding="utf-8"))
wp429 = json.loads((root / "results" / "wp429_threshold_preregistration_completeness.json").read_text(encoding="utf-8"))

m = sp.Integer(1)
gamma = sp.Rational(1, 10)
residue = sp.Integer(1)
scale = sp.Integer(10)
omega = sp.Integer(1)


def response(freq, mass, width, pole_residue):
    return sp.factor(pole_residue / (mass**2 - freq**2 - sp.I * mass * width))


scaled_m = scale * m
scaled_gamma = scale * gamma
scaled_residue = scale**2 * residue

low_coefficient = sp.factor(residue / m**2)
scaled_low_coefficient = sp.factor(scaled_residue / scaled_m**2)
width_ratio = sp.factor(gamma / m)
scaled_width_ratio = sp.factor(scaled_gamma / scaled_m)
fixed_frequency_response = response(omega, m, gamma, residue)
scaled_fixed_frequency_response = response(omega, scaled_m, scaled_gamma, scaled_residue)

wp131_benchmark = wp131["benchmark"]
wp131_scaled = wp131["scale_hostile_pair"]

checks = {
    "generic_dilation_preserves_low_energy_coefficient": scaled_low_coefficient == low_coefficient,
    "generic_dilation_preserves_dimensionless_width": scaled_width_ratio == width_ratio,
    "generic_dilation_moves_pole_location": scaled_m != m,
    "generic_dilation_changes_absolute_width_and_residue": scaled_gamma != gamma and scaled_residue != residue,
    "fixed_frequency_response_changes_on_scale_orbit": sp.simplify(scaled_fixed_frequency_response - fixed_frequency_response) != 0,
    "wp131_dependency_passed": wp131["all_pass"],
    "wp131_preserves_low_packet_while_moving_thresholds": wp131["checks"]["low_yukawa_preserved_by_scale_dilation"] and wp131["checks"]["threshold_spectrum_changes_under_same_low_packet"],
    "wp131_accessibility_changes_exactly": wp131_benchmark["accessible_poles"] == 2 and wp131_scaled["scaled_accessible_poles"] == 0,
    "wp429_missing_spectral_arrow_is_confirmed": wp429["passed"] and len(wp429["missing_from_wp428"]) == 5,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP430",
    "title": "Spectral-scale underdetermination",
    "hostile_scale": str(scale),
    "baseline": {"mass": str(m), "width": str(gamma), "residue": str(residue)},
    "dilated": {"mass": str(scaled_m), "width": str(scaled_gamma), "residue": str(scaled_residue)},
    "common_low_energy_coefficient": str(low_coefficient),
    "common_dimensionless_width": str(width_ratio),
    "baseline_response_at_fixed_frequency": str(fixed_frequency_response),
    "dilated_response_at_fixed_frequency": str(scaled_fixed_frequency_response),
    "classification": "the admitted low-energy packet leaves an exact scale orbit of inequivalent frequency spectra",
    "smallest_exact_falsifier": "a source-derived absolute mediator mass or equivalent dimensionful invariant normalized to an admitted physical clock",
    "remaining_gate": "break the scale orbit independently, then freeze widths, residues, continuum density, normalization, and uncertainties before WP428 convolution",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp430_spectral_scale_underdetermination.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
