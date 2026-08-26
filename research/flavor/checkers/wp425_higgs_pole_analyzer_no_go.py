"""Exact state-versus-law audit for the observed Higgs pole."""

import json
from pathlib import Path

import sympy as sp


mu2, lam, J, phi, s, eta = sp.symbols("mu2 lambda J phi s eta", real=True)
potential = -mu2 * phi**2 / 2 + lam * phi**4 / 4 - J * phi
stationary_source = sp.solve(sp.diff(potential, phi).subs(phi, s), J)[0]
shifted = sp.expand(potential.subs({phi: s + eta, J: stationary_source}))

constant = sp.expand(shifted).coeff(eta, 0)
linear = sp.expand(shifted).coeff(eta, 1)
quadratic = sp.expand(shifted).coeff(eta, 2)
cubic = sp.expand(shifted).coeff(eta, 3)
quartic = sp.expand(shifted).coeff(eta, 4)

s1, s2 = sp.symbols("s1 s2", real=True)
quartic_1 = quartic.subs(s, s1)
quartic_2 = quartic.subs(s, s2)
curvature = sp.factor(2 * quadratic)
cubic_derivative = sp.factor(6 * cubic)
fourth_derivative = sp.factor(24 * quartic)

checks = {
    "stationary_command_is_exact": sp.simplify(stationary_source - (-mu2 * s + lam * s**3)) == 0,
    "retained_background_has_zero_linear_term": sp.factor(linear) == 0,
    "curvature_changes_with_prepared_background": curvature == -mu2 + 3 * lam * s**2,
    "cubic_response_changes_with_prepared_background": cubic_derivative == 6 * lam * s,
    "quartic_coefficient_is_background_independent": quartic == lam / 4,
    "fourth_derivative_remains_fixed": fourth_derivative == 6 * lam,
    "hostile_distinct_backgrounds_have_equal_quartic": sp.simplify(quartic_1 - quartic_2) == 0,
    "command_to_quartic_parameter_jacobian_is_zero": sp.diff(quartic, J) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP425",
    "title": "Higgs-pole analyzer no-go",
    "source_operation": "external linear production source J phi",
    "stationary_source": str(stationary_source),
    "shifted_coefficients": {
        "constant": str(sp.factor(constant)),
        "linear": str(sp.factor(linear)),
        "quadratic": str(sp.factor(quadratic)),
        "cubic": str(sp.factor(cubic)),
        "quartic": str(sp.factor(quartic)),
    },
    "classification": "observed executable Higgs pole is a state-preparation and self-coupling analyzer, not a quartic-law actuator",
    "smallest_exact_falsifier": "a fixed admitted interaction with nonzero command derivative of lambda_eff measured independently of state displacement",
    "remaining_gate": "an observed preparable substrate implementing WP420's coefficient-level source arrow in a common Higgs readout frame",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp425_higgs_pole_analyzer_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
