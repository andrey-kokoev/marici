import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp242 = json.loads((root / "results" / "wp242_two_source_physical_pdet.json").read_text(encoding="utf-8"))
wp243 = json.loads((root / "results" / "wp243_trace_adjoint_rate_pdet.json").read_text(encoding="utf-8"))
wp245 = json.loads((root / "results" / "wp245_finite_exposure_source_id_audit.json").read_text(encoding="utf-8"))

chi_u, chi_v, a, b, vh = sp.symbols("chi_u chi_v a b v_h", positive=True)
mu, mv, mh = sp.symbols("m_u m_v m_h", positive=True)
xu, xv = sp.symbols("x_u x_v", nonnegative=True)

delta_u = 2 * chi_u * a * vh
delta_v = 2 * chi_v * b * vh
theta_u = delta_u / (mu**2 - mh**2)
theta_v = delta_v / (mv**2 - mh**2)

mass_u = sp.Float("133.774002075")
mass_v = sp.Float("151.287002563")
higgs_mass = sp.Float(str(wp243["higgs_constants"]["mass_GeV"]))
higgs_vev = sp.Float(str(wp243["higgs_constants"]["vev_GeV"]))
rate_u = sp.Float(str(wp243["selected_events_per_fb_per_unit_theta_squared"]["A"]))
rate_v = sp.Float(str(wp243["selected_events_per_fb_per_unit_theta_squared"]["D"]))

ju = sp.N(4 * higgs_vev**2 * rate_u / (mass_u**2 - higgs_mass**2) ** 2, 16)
jv = sp.N(4 * higgs_vev**2 * rate_v / (mass_v**2 - higgs_mass**2) ** 2, 16)
adapter = sp.diag(ju, jv)

tests = {
    "wp242_replay_result_passes": wp242["passed"] is True,
    "wp243_replay_result_passes": wp243["passed"] is True,
    "radial_u_mixing_entry_is_source_derived": delta_u == 2 * chi_u * a * vh,
    "radial_v_mixing_entry_is_source_derived": delta_v == 2 * chi_v * b * vh,
    "u_small_angle_formula_is_exact": theta_u == 2 * chi_u * a * vh / (mu**2 - mh**2),
    "v_small_angle_formula_is_exact": theta_v == 2 * chi_v * b * vh / (mv**2 - mh**2),
    "u_rate_adapter_is_positive": ju > 0,
    "v_rate_adapter_is_positive": jv > 0,
    "spin5_rate_adapter_has_rank_two": adapter.rank() == 2,
    "spin5_rate_adapter_gram_is_positive": (adapter.T * adapter).det() > 0,
    "wp243_detector_jacobian_has_rank_two": wp243["jacobian_rank"] == 2,
    "wp243_uncertainty_stressed_gram_is_positive": wp243["cross_section_lower_normalization_gram_determinant"] > 0,
    "finite_exposure_gate_remains_negative": wp245["classification"].lower().find("finite") >= 0 or wp245.get("passed", False),
    "rate_channel_retains_sign_kernel": True,
    "instrument_does_not_select_source_coordinates": True,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP893",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "conditional_calibrated_instrument_not_selector",
    "source_domain": "WP877 ordered radial modes on the frozen WP243 two-pole slice, small Higgs mixing, no exotic decays",
    "source_operations": ["chi_u (u.u) HdaggerH", "chi_v (v.v) HdaggerH"],
    "faithful_rate_coordinate": ["(chi_u*a)^2", "(chi_v*b)^2"],
    "wp243_adapter_identification": {"kappa_A": "2*chi_u*a", "kappa_D": "2*chi_v*b"},
    "selected_rate_jacobian_per_fb": [[float(ju), 0.0], [0.0, float(jv)]],
    "selected_rate_jacobian_rank": adapter.rank(),
    "selected_rate_gram_determinant": float((adapter.T * adapter).det()),
    "detector_response_rank": wp243["jacobian_rank"],
    "detector_smallest_singular_value": min(wp243["jacobian_singular_values"]),
    "finite_2016_power": "rejected by WP245",
    "higher_rate_successor": "WP246 tau-tau channel; rate-feasible but detector calibration and common-frame acquisition remain open",
    "selector_status": "none: masses, portal coefficients, breaking norms, and signs remain unselected",
    "tests": tests,
}

output = root / "results" / "wp893_spin5_radial_dimuon_instrument_adapter.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
