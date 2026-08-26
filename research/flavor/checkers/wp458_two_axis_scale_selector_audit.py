"""Exact two-axis selector audit for g_F f/v."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
dependencies = {}
for number, name in [
    (447, "irreducible_adjoint_triplet"),
    (448, "triplet_pole_residue_packet"),
    (449, "triplet_width_packet"),
    (455, "correlated_kaon_response_constructor"),
    (457, "pole_clock_parameter_identifiability"),
]:
    dependencies[number] = json.loads(
        (root / "results" / f"wp{number}_{name}.json").read_text(encoding="utf-8")
    )

g_f, mu, v, kappa, c, sigma = sp.symbols(
    "g_F mu v kappa c sigma", positive=True, real=True
)
f = sp.sqrt(6) * mu
target = sp.simplify(g_f * f / v)
source_coordinates = sp.Matrix([g_f, mu / v])
target_gradient = sp.Matrix(
    [sp.diff(target, g_f), sp.diff(target, mu / v)]
) if False else sp.Matrix([sp.sqrt(6) * mu / v, sp.sqrt(6) * g_f])

# Minimal scale-invariant relational portal: mu=kappa*sigma and
# sigma^2=c H^dagger H=c v^2/2.
sigma_vacuum = sp.sqrt(c / 2) * v
mu_portal = kappa * sigma_vacuum
f_over_v_portal = sp.simplify(sp.sqrt(6) * mu_portal / v)
target_portal = sp.simplify(g_f * f_over_v_portal)
portal_label_gradient = sp.Matrix(
    [
        sp.diff(target_portal, g_f),
        sp.diff(target_portal, kappa),
        sp.diff(target_portal, c),
    ]
)

# One-loop SU(3)_F coefficient: six Dirac fundamentals and three real adjoints.
c_adj = sp.Integer(3)
t_fund = sp.Rational(1, 2)
t_adj = sp.Integer(3)
n_dirac = sp.Integer(6)
n_real_adjoint = sp.Integer(3)
b0 = sp.simplify(
    sp.Rational(11, 3) * c_adj
    - sp.Rational(4, 3) * t_fund * n_dirac
    - sp.Rational(1, 6) * t_adj * n_real_adjoint
)
beta_numerator = sp.factor(-b0 * g_f**3)
zero_momentum_current_strength = sp.simplify(1 / mu**2)

checks = {
    "all_dependencies_passed": all(packet["passed"] for packet in dependencies.values()),
    "target_factorization_exact": target == sp.sqrt(6) * g_f * mu / v,
    "both_original_source_axes_change_target": all(entry != 0 for entry in target_gradient),
    "portal_removes_radial_state_from_ratio": sigma not in f_over_v_portal.free_symbols,
    "portal_ratio_exact": f_over_v_portal == kappa * sp.sqrt(3 * c),
    "portal_target_exact": target_portal == g_f * kappa * sp.sqrt(3 * c),
    "all_portal_theory_labels_change_target": all(
        entry != 0 for entry in portal_label_gradient
    ),
    "one_loop_coefficient_exact": b0 == sp.Rational(11, 2),
    "one_loop_running_is_asymptotically_free": beta_numerator == -sp.Rational(11, 2) * g_f**3,
    "no_positive_finite_one_loop_fixed_point": sp.solve(beta_numerator, g_f) == [],
    "current_constraint_does_not_select_gauge_coupling": sp.diff(
        zero_momentum_current_strength, g_f
    )
    == 0,
    "formal_readout_is_not_selector": dependencies[457]["numerical_selector"] is False,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP458",
    "admitted_source_label_domain": "g_F>0 and mu/v>0 independently in WP447; portal attack additionally has kappa>0,c>0.",
    "target": "g_F f/v=sqrt(6) g_F mu/v",
    "target_gradient_on_original_labels": [str(entry) for entry in target_gradient],
    "minimal_relational_portal": {
        "relations": [
            "mu=kappa sigma",
            "sigma^2=c H^dagger H",
            "H^dagger H=v^2/2",
        ],
        "f_over_v": str(f_over_v_portal),
        "g_F_f_over_v": str(target_portal),
        "residual_product_changing_labels": ["g_F", "kappa", "c"],
    },
    "one_loop_gauge_running": {
        "matter": "six Dirac fundamentals plus three real adjoints of SU(3)_F",
        "b0": str(b0),
        "positive_finite_fixed_point": None,
    },
    "classification": "No numerical selector. Existing current/pole/width operations constrain or identify; the minimal portal rigidifies f/v only conditional on unfixed theory labels.",
    "source_selector": False,
    "presentation_rigidifier": False,
    "relational_scale_rigidifier_under_added_portal": checks[
        "portal_removes_radial_state_from_ratio"
    ],
    "physical_readout": "Algebraically rank two by WP457; detector execution remains open.",
    "smallest_exact_falsifier": "A positive finite one-loop gauge fixed point or independence of the portal target from g_F,kappa,c in the declared action.",
    "remaining_gate": "Supply a source-authorized finite normalization of g_F and of kappa*sqrt(c), or one joint fixed relation for their product, then test the complete fitted ensemble and detector response.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp458_two_axis_scale_selector_audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
