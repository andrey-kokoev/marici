"""Exact parameter-authority census for mediator-to-clock relations."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp134 = json.loads((root / "results" / "wp134_dimensional_transmutation_authority.json").read_text(encoding="utf-8"))
wp135 = json.loads((root / "results" / "wp135_uv_fixed_point_scale_authority.json").read_text(encoding="utf-8"))

kappa, g_f, c_r, f_over_v = sp.symbols("kappa g_F C_R f_over_v", positive=True, real=True)
mu0_over_v, b, g0 = sp.symbols("mu0_over_v b g_0", positive=True, real=True)

scale_invariant_ratio = sp.sqrt(kappa)
gauge_higgs_ratio = g_f * sp.sqrt(c_r) * f_over_v
transmutation_ratio = mu0_over_v * sp.exp(-1 / (2 * b * g0**2))

candidate_free_inputs = {
    "classical_scale_invariance": sorted(str(x) for x in scale_invariant_ratio.free_symbols),
    "gauge_higgsing": sorted(str(x) for x in gauge_higgs_ratio.free_symbols),
    "dimensional_transmutation": sorted(str(x) for x in transmutation_ratio.free_symbols),
    "uv_fixed_point": ["relevant_amplitude"],
}

checks = {
    "scale_invariance_leaves_portal_coupling": scale_invariant_ratio.free_symbols == {kappa},
    "scale_invariant_ratio_changes_with_portal_coupling": sp.diff(scale_invariant_ratio, kappa) != 0,
    "gauge_higgsing_leaves_coupling_and_scale_ratio": {g_f, f_over_v}.issubset(gauge_higgs_ratio.free_symbols),
    "discrete_representation_factor_does_not_remove_continuous_inputs": sp.diff(gauge_higgs_ratio, g_f) != 0 and sp.diff(gauge_higgs_ratio, f_over_v) != 0,
    "transmutation_leaves_boundary_inputs": {mu0_over_v, g0}.issubset(transmutation_ratio.free_symbols),
    "wp134_dependency_passed_and_scale_not_absolute": wp134["all_pass"] and not wp134["absolute_scale_selected_without_boundary"],
    "wp135_dependency_passed_and_amplitude_not_fixed": wp135["all_pass"] and not wp135["absolute_scale_selected_by_fixed_point_alone"],
    "no_candidate_is_parameter_free": all(len(inputs) > 0 for inputs in candidate_free_inputs.values()),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP432",
    "title": "Mediator-clock relation census",
    "candidate_relations": {
        "classical_scale_invariance": str(scale_invariant_ratio),
        "gauge_higgsing": str(gauge_higgs_ratio),
        "dimensional_transmutation": str(transmutation_ratio),
        "uv_fixed_point": "crossover scale depends on relevant amplitude",
    },
    "remaining_free_inputs": candidate_free_inputs,
    "classification": "all current mechanisms provide conditional formulas but none derives a parameter-free mediator-to-clock ratio",
    "closest_progressive_route": "independently observed flavor gauge coupling and breaking order parameter matched to the WP128 adjoints",
    "smallest_exact_falsifier": "one admitted relation for M/v containing only independently measured source-channel quantities and discrete representation data",
    "remaining_gate": "source and instrument authority for every continuous input before threshold prediction",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp432_mediator_clock_relation_census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
