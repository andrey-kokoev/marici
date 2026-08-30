"""Exact fixed-law constructor for conditional Higgs-quartic actuation."""

import json
from pathlib import Path

import sympy as sp


lam, g, scale, s, s0, s1, s2 = sp.symbols(
    "lambda g Lambda s s0 s1 s2", real=True
)
v0, w_h, w_j = sp.symbols("v0 w_H w_J", positive=True, real=True)

lambda_eff = lam + g * s / scale
actuation = sp.diff(lambda_eff, s)
setting_separation = sp.factor(lambda_eff.subs(s, s2) - lambda_eff.subs(s, s1))

# Combine the WP412 quadratic source with the prepared substrate state.  The
# theory coefficients g and Lambda remain fixed; only the substrate state s is
# commanded.
response = sp.Matrix(
    [
        [1, 3 * v0**2 * actuation],
        [v0, v0**3 * actuation],
    ]
)
wedge = sp.factor(response.det())
gram_det = sp.factor((response.T * sp.diag(w_h, w_j) * response).det())

# Exact null limits required of a physical EFT constructor.
zero_coupling_limit = sp.simplify(actuation.subs(g, 0))
equal_setting_limit = sp.simplify(setting_separation.subs(s2, s1))
decoupling_limit = sp.limit(actuation, scale, sp.oo)

checks = {
    "fixed_law_state_actuation_is_nonzero_conditionally": actuation == g / scale,
    "two_prepared_states_separate_effective_quartics": sp.simplify(
        setting_separation - g * (s2 - s1) / scale
    ) == 0,
    "wp416_response_wedge_is_inherited": wedge == -2 * g * v0**3 / scale,
    "positive_weighted_gram_has_expected_form": gram_det == 4 * g**2 * v0**6 * w_h * w_j / scale**2,
    "zero_coupling_kills_actuation": zero_coupling_limit == 0,
    "identical_source_settings_kill_displacement": equal_setting_limit == 0,
    "heavy_scale_decouples_actuator": decoupling_limit == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP420",
    "title": "Fixed-law Higgs-quartic constructor",
    "fixed_interaction": "-(g/Lambda) S (H-dagger-H)^2",
    "commanded_attribute": "prepared homogeneous source state s=<S>",
    "effective_quartic": str(lambda_eff),
    "command_to_quartic_transfer": str(actuation),
    "two_setting_separation": str(setting_separation),
    "quadratic_plus_source_state_response": [[str(x) for x in row] for row in response.tolist()],
    "response_wedge": str(wedge),
    "weighted_gram_determinant": str(gram_det),
    "classification": "well-typed fixed-law constructor conditional on an observed preparable singlet substrate",
    "smallest_exact_falsifiers": [
        "g = 0",
        "s2 = s1",
        "Lambda tends to infinity",
    ],
    "remaining_physical_gate": "observe S and g, prepare at least two calibrated long-lived s states, and measure quartic-sensitive records without refitting",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp420_fixed_law_quartic_constructor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
