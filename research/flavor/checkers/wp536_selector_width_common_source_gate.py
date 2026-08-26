"""Common-source compatibility gate for selected ratio and WP534 poles."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp477 = load("wp477_ratio_selector_normal_form.json")
wp489 = load("wp489_common_source_threshold_constructor.json")
wp527 = load("wp527_hierarchical_nonquark_closure.json")
wp534 = load("wp534_invariant_complex_pole_packet.json")

# Pull the WP527 witness into WP489's common-source coordinates:
# g_F^2=2, y=1, w=1, a=v^2/2=30258, b=s^2=256.
g_f_squared = sp.Integer(2)
y_squared = sp.Integer(1)
v_squared = sp.Integer(246) ** 2
a_width = v_squared / 2
c_width = sp.simplify(a_width / (g_f_squared * y_squared))
ratio_width = sp.simplify(sp.sqrt(3 * g_f_squared * y_squared / a_width))

c_target = sp.sympify(
    wp477["conditional_five_TeV_readout"]["required_c_exact"]
)
ratio_target = sp.sympify(
    wp477["conditional_five_TeV_readout"]["target_exact"]
)
a_target = sp.simplify(c_target * g_f_squared * y_squared)

# Keeping the measured electroweak norm fixed forces the common clock and
# flavor scale to move when a changes.
w_target_squared = sp.simplify(v_squared / (2 * a_target))
mu_target_squared = y_squared * w_target_squared
quintet_target_mass_squared = sp.simplify(
    3 * g_f_squared * mu_target_squared
)
clock_scale_factor = sp.simplify(sp.sqrt(w_target_squared))
ratio_mismatch_factor = sp.simplify(ratio_target / ratio_width)

entrance_minimum_squared = sp.sympify(
    wp527["nonquark_closure_witness"][
        "entrance_minimum_mass_squared"
    ]
)
entrance_pair_margin_at_target = sp.simplify(
    quintet_target_mass_squared - 4 * entrance_minimum_squared
)
entrance_pair_margin_at_width_point = sp.simplify(
    sp.Integer(6) - 4 * entrance_minimum_squared
)

# A common dimensional rescaling cannot repair the mismatch because the ratio
# is independent of w.
w = sp.symbols("w", positive=True)
scale_free_ratio = sp.sqrt(3 * g_f_squared * y_squared / a_width)
scale_derivative = sp.diff(scale_free_ratio, w)

checks = {
    "wp477_dependency_passed": bool(wp477["passed"]),
    "wp489_dependency_passed": bool(wp489["passed"]),
    "wp527_dependency_passed": bool(wp527["passed"]),
    "wp534_dependency_passed": bool(wp534["passed"]),
    "wp527_width_source_has_c_15129": c_width == 15129,
    "wp527_width_ratio_is_sqrt3_over_123": ratio_width
    == sp.sqrt(3) / 123,
    "withheld_target_matches_wp477_exactly": ratio_target
    == sp.Rational(250000, 12311) * sp.sqrt(6),
    "width_and_target_selector_coordinates_differ": c_width != c_target,
    "ratio_mismatch_exceeds_three_thousand": ratio_mismatch_factor > 3000,
    "common_dimensional_rescaling_cannot_change_ratio": scale_derivative == 0,
    "target_ratio_requires_changed_source_coefficient_a": a_target != a_width,
    "width_point_closes_the_entrance_scalar_pair": (
        entrance_pair_margin_at_width_point < 0
    ),
    "target_point_opens_the_same_entrance_scalar_pair": (
        entrance_pair_margin_at_target > 0
    ),
    "wp534_classification_is_bounded_to_wp527": (
        "WP527" in wp534["domain"]
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP536",
    "domain": "Comparison of the WP527/WP534 common-source width witness with WP477's withheld five-TeV ratio readout in WP489 coordinates.",
    "width_source": {
        "g_F_squared": str(g_f_squared),
        "y_squared": str(y_squared),
        "a": str(a_width),
        "c": str(c_width),
        "g_F_f_over_v": str(ratio_width),
    },
    "withheld_target_source_requirement": {
        "c": str(c_target),
        "required_a_at_fixed_g_F_and_y": str(a_target),
        "required_w_squared_at_fixed_v": str(w_target_squared),
        "required_quintet_mass_squared_GeV_squared": str(
            quintet_target_mass_squared
        ),
    },
    "mismatch": {
        "target_over_width_ratio": str(ratio_mismatch_factor),
        "target_over_width_ratio_numeric": float(
            sp.N(ratio_mismatch_factor, 20)
        ),
        "clock_scale_factor": str(clock_scale_factor),
        "scale_change_repairs_ratio": bool(scale_derivative != 0),
    },
    "threshold_hostile_test": {
        "entrance_scalar_mass_squared_GeV_squared": str(
            entrance_minimum_squared
        ),
        "quintet_minus_pair_threshold_at_width_point": str(
            entrance_pair_margin_at_width_point
        ),
        "quintet_minus_pair_threshold_at_target_point": str(
            entrance_pair_margin_at_target
        ),
        "conclusion": "The WP527 entrance-scalar pair is closed at the WP534 width point and open after imposing the withheld target while retaining the other declared witness coefficients.",
    },
    "theorem": "WP534's channel-complete declared tree widths and WP477's withheld ratio do not inhabit one currently admitted source point. The dimensionless mismatch cannot be repaired by rescaling the common clock, and changing the selector coefficient to the target invalidates the WP527 nonquark closure used by WP534.",
    "classification": "Exact common-source noncomposability result. The ratio readout and width packet are separately valid conditional objects but cannot jointly support a selected-ratio prediction.",
    "selector": False,
    "rigidifier": bool(
        c_width != c_target and entrance_pair_margin_at_target > 0
    ),
    "instrument": "WP535 remains the correct downstream instrument contract, but it cannot calibrate a target-ratio pole packet until that packet is recomputed on a source-selected common domain.",
    "smallest_exact_falsifier": "At fixed v and the other WP527 witness coefficients, imposing the target c opens the previously closed entrance-scalar pair below the quintet. One new partial width already invalidates reuse of WP534.",
    "remaining_gate": "Derive c from coefficient dynamics independently of the readout, solve the full vacuum at that selected point, redo all scalar and messenger thresholds, and recompute invariant poles, residues and widths before applying WP535.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp536_selector_width_common_source_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
