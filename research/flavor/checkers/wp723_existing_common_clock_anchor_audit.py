"""Exact composition audit of the existing common-clock source as RG anchor."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / "results" / name).read_text(encoding="utf-8"))


wp489 = load("wp489_common_source_threshold_constructor.json")
wp537 = load("wp537_fixed_v_selector_fiber.json")
wp543 = load("wp543_existing_source_constraint_kernel.json")
wp722 = load("wp722_autonomous_rg_translation_no_go.json")

s, w, y, a, b, zA, zB = sp.symbols(
    "s w y a b z_A z_B", positive=True
)
scale_squares = sp.Matrix([
    y**2*w**2,
    6*y**2*w**2,
    2*a*w**2,
    b*w**2,
    zA**2*w**2,
    zB**2*w**2,
])
scaled_squares = sp.simplify(scale_squares.subs(w, s*w))
dimensionless_ratios = sp.Matrix([
    scale_squares[1]/scale_squares[2],
    scale_squares[4]/scale_squares[2],
    scale_squares[5]/scale_squares[2],
])
scaled_ratios = sp.simplify(dimensionless_ratios.subs(w, s*w))

J = sp.Matrix([[1, 2, 0, 0], [0, 0, -1, 1], [0, 0, 1, 0]])
tangent = sp.Matrix([2, -1, 0, 0])
target_gradient = sp.Matrix([[-sp.Rational(1, 2), 0, sp.Rational(1, 2), 0]])

checks = {
    "wp489_common_source_constructor_passed": bool(wp489["passed"]),
    "wp537_fixed_v_hostile_pair_passed": bool(wp537["passed"]),
    "wp543_equality_kernel_passed": bool(wp543["passed"]),
    "wp722_translation_theorem_passed": wp722["status"] == "PASS",
    "common_w_dilation_scales_every_mass_square": sp.simplify(scaled_squares-s**2*scale_squares) == sp.zeros(6, 1),
    "common_w_dilation_preserves_dimensionless_ratios": sp.simplify(scaled_ratios-dimensionless_ratios) == sp.zeros(3, 1),
    "fixed_v_source_jacobian_retains_tangent": J*tangent == sp.zeros(3, 1),
    "surviving_tangent_changes_flavor_clock_ratio": (target_gradient*tangent)[0] == -1,
    "hostile_pair_keeps_v_and_changes_ratio": wp537["hostile_pair"][0]["v_squared"] == wp537["hostile_pair"][1]["v_squared"] and wp537["hostile_pair"][0]["ratio"] != wp537["hostile_pair"][1]["ratio"],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP723",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the WP489 common-singlet source, its strict threshold cone, fixed electroweak calibration, and every equality admitted through WP543",
    "faithful_coordinate": "absolute common scale w together with the fixed-v coefficient direction t and the resulting flavor/electroweak clock ratio",
    "source_authorized_operation": "one singlet vacuum propagates a common clock into flavor, Higgs, connector, and messenger masses",
    "contextual_partition": "fixed coefficients leave an absolute w-dilation fiber; fixing v still leaves the t fiber changing the flavor clock ratio",
    "classification": "common-clock parallelizer and conditional relational selector, but not a source-derived absolute anchor or numerical portal selector",
    "smallest_exact_falsifiers": [
        "w -> s w scales every physical mass while preserving all dimensionless source ratios",
        "the fixed-v tangent (2,-1,0,0) preserves every admitted equality but changes log(g_F f/v) by -1",
    ],
    "remaining_gate": "an independently derived equation fixing both the absolute singlet scale and the t coefficient direction before threshold or detector data are used",
    "physical_instrument_gate": "WP674 and WP658 give source-level and ideal calibrated rank architectures, but no actual common-frame experiment supplies the anchor or realizes the full response",
}
(ROOT / "results" / "wp723_existing_common_clock_anchor_audit.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
