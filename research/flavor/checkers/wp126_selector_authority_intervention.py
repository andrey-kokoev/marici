"""Exact WP126 causal-authority intervention audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def selected_x(a, q):
    return F(1, 2) + a / (F(8) * q)


a, q = F(28), F(25)
x = selected_x(a, q)
dx_da = F(1, 8) / q
dx_dq = -a / (F(8) * q * q)
delta_a = selected_x(a + 1, q) - x
delta_common_scale = selected_x(2 * a, 2 * q) - x
delta_ratio_preserving = selected_x(3 * a, 3 * q) - x

checks = {
    "baseline_selector": x == F(16, 25),
    "a_intervention_response": delta_a == F(1, 200),
    "exact_dx_da": dx_da == F(1, 200),
    "exact_dx_dq": dx_dq == F(-7, 1250),
    "ratio_euler_identity": a * dx_da + q * dx_dq == 0,
    "common_scale_is_gauge_for_angle": delta_common_scale == 0,
    "second_ratio_preserving_control": delta_ratio_preserving == 0,
    "interior_stability_domain": q > 0 and -4 * q < a < 4 * q,
    "positive_slice_hessian": 16 * q == F(400),
    "inert_angle_falsifies_ratio_changing_source_response": delta_a != 0,
}

result = {
    "work_package": "WP126",
    "classification": "conditional causal selector grant with missing UV constructor and instrument",
    "grant_chain": ["UV_constructor", "EFT_matching_to_a_q", "degree_eight_potential", "vacuum_selector_x_star", "physical16_readout"],
    "selected_x": str(x),
    "source_intervention_response": {
        "dx_da": str(dx_da), "dx_dq": str(dx_dq),
        "finite_delta_a_plus_one": str(delta_a),
        "common_scale_delta": str(delta_common_scale),
        "euler_ratio_identity": str(a * dx_da + q * dx_dq),
    },
    "contextual_partition": "coefficient rays (a,q) modulo common positive scaling at fixed spectra",
    "reference_port_required": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp126_selector_authority_intervention.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
