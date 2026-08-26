"""Exact source-authority audit for the scale-free flavor-ratio selector."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp435 = load("wp435_dynamical_flavon_messenger_completion.json")
wp465 = load("wp465_messenger_fixed_point_threshold_gate.json")
wp467 = load("wp467_common_dilaton_clock_portal.json")
wp476 = load("wp476_common_domain_vector_widths.json")

g, y, a, c = sp.symbols("g_F y a c", positive=True)
target = sp.sqrt(3) * g * y / sp.sqrt(a)
selected_target = sp.simplify(target.subs(a, c * g**2 * y**2))

# Both members remain in WP467's positive coefficient domain and share its
# fields, symmetries, and sum-of-squares structure.
hostile_one = sp.simplify(selected_target)
hostile_four = sp.simplify(selected_target.subs(c, 4 * c))

v = sp.Rational(12311, 50000)
m1 = sp.Integer(5)
benchmark_target = sp.simplify(sp.sqrt(6) * m1 / v)
required_c = sp.simplify(3 / benchmark_target**2)

beta_a, beta_g, beta_y = sp.symbols("beta_a beta_g beta_y", real=True)
beta_c_over_c = sp.simplify(beta_a / a - 2 * beta_g / g - 2 * beta_y / y)

checks = {
    "wp435_dependency_passed": wp435["passed"],
    "wp465_threshold_gate_failed_as_recorded": wp465["threshold_compatibility"] == "failed",
    "wp467_scale_kernel_is_repaired": wp467["scale_kernel_repaired"],
    "wp467_numerical_selector_is_not_admitted": not wp467["numerical_selector_admitted"],
    "wp476_dependency_passed": wp476["passed"],
    "normal_form_selects_scale_free_target": selected_target == sp.sqrt(3) / sp.sqrt(c),
    "normal_form_removes_g_and_y": not selected_target.has(g, y),
    "positive_hostile_pair_changes_target_by_two": sp.simplify(hostile_one / hostile_four) == 2,
    "benchmark_coefficient_is_exact": required_c == sp.Rational(151560721, 125000000000),
    "benchmark_coefficient_reproduces_readout": sp.simplify(selected_target.subs(c, required_c) - benchmark_target) == 0,
    "rg_invariance_requires_three_beta_functions": beta_c_over_c.has(beta_a, beta_g, beta_y),
    "gauge_beta_alone_cannot_make_beta_c_zero": sp.simplify(beta_c_over_c.subs({beta_a: 0, beta_y: 0})) == -2 * beta_g / g,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP477",
    "target": "sqrt(3)*g_F*y/sqrt(a)",
    "minimal_scale_free_selector_coordinate": "c=a/(g_F^2*y^2)",
    "selector_normal_form": {
        "source_relation": "a=c*g_F^2*y^2",
        "selected_target": str(selected_target),
        "classification": "A source-fixed c would numerically select g_F*f/v without fixing the common scale.",
    },
    "conditional_five_TeV_readout": {
        "target_exact": str(benchmark_target),
        "target_numeric": float(sp.N(benchmark_target, 16)),
        "required_c_exact": str(required_c),
        "required_c_numeric": float(sp.N(required_c, 16)),
        "authority": "derived from the frozen pole and measured electroweak clock; it may test but cannot define a source law",
    },
    "hostile_source_pair": {
        "coefficients": ["c", "4*c"],
        "targets": [str(hostile_one), str(hostile_four)],
        "same_admitted_structure": "positive WP467 common-clock sum of squares with the same fields and symmetries",
    },
    "rg_descent_gate": {
        "beta_c_over_c": str(beta_c_over_c),
        "required_condition": "beta_a/a=2*beta_g/g+2*beta_y/y on the complete coupled trajectory",
        "current_authority": "WP465 supplies only a gauge-subsystem root and proves it is lost after messenger decoupling; beta_a and beta_y plus threshold matching are absent",
    },
    "authority_audit": {
        "common_clock_geometry": "selects a ratio conditional on independent positive g_F, y, and a",
        "messenger_grammar": "adds independent masses and Yukawa couplings but no equation fixing c",
        "gauge_fixed_point": "does not survive the messenger threshold and does not constrain a or y",
        "kaon_and_pole_records": "constrain or read out c after the fact; they are physical probes, not source constructors",
    },
    "classification": "Exact selector normal form found, but no admitted source operation fixes its coefficient; current five-TeV value remains a readout, not a selection.",
    "selector_architecture": bool(selected_target == sp.sqrt(3) / sp.sqrt(c)),
    "numerical_selector_admitted": False,
    "rigidifier": False,
    "reference_port_required": False,
    "smallest_exact_falsifier": "The positive actions with c and 4c obey the same admitted source grammar but predict targets differing by a factor of two.",
    "remaining_gate": "Derive c independently from a complete coupled gauge-messenger-scalar action and prove beta_c=0 with threshold matching before comparing its prediction with the pole/current instruments.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp477_ratio_selector_normal_form.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
