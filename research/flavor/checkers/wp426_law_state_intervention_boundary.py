"""Exact bounded-grammar audit of law labels versus state interventions."""

import json
from pathlib import Path

import sympy as sp


phi = sp.symbols("phi", real=True)
lam, mu2, a1, a3 = sp.symbols("lambda mu2 a1 a3", real=True)
u0, u1, u2, u3, u4 = sp.symbols("u0 u1 u2 u3 u4", real=True)
g, S, scale, c = sp.symbols("g S Lambda c", nonzero=True, real=True)
sfun = sp.Function("s")

base = lam * phi**4 / 4 - mu2 * phi**2 / 2 + a3 * phi**3 + a1 * phi
state_sourced = sp.expand(base + u0 + u1 * phi + u2 * phi**2 + u3 * phi**3)
quartic_coefficient = state_sourced.coeff(phi, 4)
state_jacobian = sp.Matrix([quartic_coefficient]).jacobian([u0, u1, u2, u3])

law_labelled = sp.expand(state_sourced + u4 * phi**4)
law_label_derivative = sp.diff(law_labelled.coeff(phi, 4), u4)

extended = sp.expand(base + g * S * phi**4 / (4 * scale))
extended_quartic = sp.factor(4 * extended.coeff(phi, 4))
lambda_effective = extended_quartic.subs(S, sfun(c))
command_derivative = sp.diff(lambda_effective, c)

checks = {
    "subquartic_source_grammar_preserves_quartic_coefficient": quartic_coefficient == lam / 4,
    "all_state_source_to_quartic_derivatives_vanish": state_jacobian == sp.zeros(1, 4),
    "explicit_degree_four_label_has_nonzero_derivative": law_label_derivative == 1,
    "added_scalar_port_changes_effective_quartic": sp.simplify(extended_quartic - (lam + g * S / scale)) == 0,
    "prepared_port_command_derivative_factors_through_preparation": command_derivative == g * sp.diff(sfun(c), c) / scale,
    "zero_coupling_decouples_added_port": sp.simplify(extended_quartic.subs(g, 0) - lam) == 0,
    "constant_port_preparation_has_zero_command_derivative": command_derivative.subs(sp.diff(sfun(c), c), 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP426",
    "title": "Law-state intervention boundary",
    "admitted_fixed_SM_source_grammar": "sum from k=0 to 3 of u_k phi^k",
    "quartic_coefficient": str(quartic_coefficient),
    "state_source_jacobian": str(state_jacobian),
    "counterfactual_degree_four_label_derivative": str(law_label_derivative),
    "enlarged_domain_effective_quartic": str(extended_quartic),
    "enlarged_domain_command_derivative": str(command_derivative),
    "classification": "fixed-SM state controls do not actuate the quartic; nonzero actuation requires a theory label or an explicitly enlarged dynamical port",
    "smallest_exact_falsifier": "an admitted operation inside the stated subquartic source grammar with nonzero degree-four coefficient derivative",
    "programme_disposition": "close direct SM quartic actuation negative and return selector search to fixed-law physical16 dynamics",
    "remaining_gate": "a fixed-law source action or observed enlarged-domain constructor that descends to physical16 and selects a proper subfamily",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp426_law_state_intervention_boundary.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
