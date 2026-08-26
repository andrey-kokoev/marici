"""Exact reach audit for electromagnetic-background Higgs-quartic control."""

import json
from pathlib import Path

import sympy as sp


v = sp.Integer(246)  # GeV
tesla_to_gev2 = sp.Rational(195, 10**18)
b_lab_tesla = sp.Rational(403, 4)  # 100.75 T controlled-waveform record
b_lab = sp.factor(b_lab_tesla * tesla_to_gev2)

e0, c_loop, h = sp.symbols("E0 C_loop h", positive=True, real=True)

# Lorentz invariants for a plane wave with orthogonal equal E and B, and for a
# static magnetic background.  Sign convention is irrelevant to the reach
# bound; only vanishing versus nonvanishing and absolute magnitude are used.
f2_plane_wave = sp.factor(2 * (e0**2 - e0**2))
g_plane_wave = sp.Integer(0)
f2_static_b = 2 * b_lab**2

# Broken-phase charged-threshold form.  Its fourth radial derivative gives the
# induced local quartic coefficient in V = ... + delta_lambda*h^4/4.
delta_v = c_loop * f2_static_b * sp.log((v + h) / v)
fourth_derivative = sp.factor(sp.diff(delta_v, h, 4).subs(h, 0))
delta_lambda = sp.factor(fourth_derivative / 6)

# Unit-coefficient envelope is deliberately far larger than a perturbative SM
# loop coefficient, so failure here is a conservative reach obstruction.
unit_coefficient_bound = sp.factor(abs(delta_lambda.subs(c_loop, 1)))
b_required_tesla = sp.factor(v**2 / (sp.sqrt(2) * tesla_to_gev2))
field_ratio = sp.factor(b_required_tesla / b_lab_tesla)

checks = {
    "single_plane_wave_has_zero_scalar_invariants": f2_plane_wave == 0 and g_plane_wave == 0,
    "static_magnetic_background_has_nonzero_invariant": f2_static_b > 0,
    "threshold_log_generates_a_radial_quartic": fourth_derivative == -6 * c_loop * f2_static_b / v**4,
    "induced_quartic_is_proportional_to_commanded_field_squared": delta_lambda == -c_loop * f2_static_b / v**4,
    "unit_coefficient_lab_shift_is_below_1e_minus_36": unit_coefficient_bound < sp.Rational(1, 10**36),
    "unit_shift_requires_more_than_1e20_tesla": b_required_tesla > 10**20,
    "required_to_laboratory_field_ratio_exceeds_1e18": field_ratio > 10**18,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP422",
    "title": "Electromagnetic Higgs-quartic actuation reach",
    "source_substrate": "controlled classical electromagnetic background",
    "source_derived_effective_form": "C_loop F_mu_nu F^mu_nu log(phi/v)",
    "tesla_to_GeV_squared": str(tesla_to_gev2),
    "laboratory_field_tesla": str(b_lab_tesla),
    "laboratory_field_GeV_squared": str(b_lab),
    "plane_wave_invariants": {"F_squared": str(f2_plane_wave), "F_dual_F": str(g_plane_wave)},
    "static_magnetic_F_squared": str(f2_static_b),
    "induced_quartic": str(delta_lambda),
    "unit_loop_coefficient_absolute_shift_bound": str(unit_coefficient_bound),
    "unit_shift_required_field_tesla": str(b_required_tesla),
    "required_to_laboratory_field_ratio": str(field_ratio),
    "classification": "existing executable source with nonzero formal quartic actuation, but no measurable physical instrument because electroweak reach is absent",
    "smallest_exact_falsifier": "a single plane-wave control has vanishing electromagnetic invariants",
    "remaining_gate": "a common-region Higgs experiment with field above the exact sensitivity threshold or a source-derived enhancement exceeding the conservative reach gap",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp422_em_higgs_quartic_reach.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
