"""Exact fixed-electroweak hostile fiber in the WP489 common-source cone."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp489 = load("wp489_common_source_threshold_constructor.json")
wp536 = load("wp536_selector_width_common_source_gate.json")

F, V, R, sigma = sp.symbols("F V R sigma", real=True)
fields = (F, V, R, sigma)
rho = eta = lambda_s = kappa = sp.Integer(100)
y = g_f2 = sp.Integer(1)
b = sp.Integer(32)
g_p2 = sp.Rational(1, 68)


def witness(t):
    t = sp.Rational(t)
    a = t**2
    w = 1 / t
    potential = sp.expand(
        rho * (F**2 - 6 * y**2 * sigma**2) ** 2
        + eta * (V**2 / 2 - a * sigma**2) ** 2
        + lambda_s / 3 * (R**2 - 3 * b * sigma**2) ** 2
        + kappa * (sigma**2 - w**2) ** 2
    )
    vacuum = {
        F: sp.sqrt(6) * y * w,
        V: sp.sqrt(2 * a) * w,
        R: sp.sqrt(3 * b) * w,
        sigma: w,
    }
    gradient = sp.Matrix([sp.diff(potential, q) for q in fields]).subs(vacuum)
    hessian = sp.hessian(potential, fields).subs(vacuum)

    mu2 = y**2 * w**2
    v2 = 2 * a * w**2
    s2 = b * w**2
    triplet_a = g_f2 * mu2
    triplet_d = g_p2 * (4 * mu2 + 2 * s2)
    mixing2 = 4 * g_f2 * g_p2 * mu2**2
    disc = sp.factor((triplet_a - triplet_d) ** 2 + 4 * mixing2)
    vectors = [
        sp.simplify((triplet_a + triplet_d - sp.sqrt(disc)) / 2),
        3 * g_f2 * mu2,
        sp.simplify((triplet_a + triplet_d + sp.sqrt(disc)) / 2),
    ]
    max_vector2 = max(vectors)
    shift = max_vector2 / 4
    shifted = hessian - shift * sp.eye(4)
    minors = [sp.factor(shifted[:n, :n].det()) for n in range(1, 5)]

    messenger2 = w**2
    flavon_min2 = 16 * rho * w**2
    connector_min2 = 8 * lambda_s * s2
    tau2 = min(messenger2, flavon_min2, connector_min2)
    vector_pair_margins = [sp.simplify(4 * x - z) for x in vectors for z in vectors]
    threshold_margins = [sp.simplify(4 * tau2 - z) for z in vectors]
    ratio = sp.simplify(sp.sqrt(6 * g_f2 * y**2 * w**2 / v2))

    return {
        "t": str(t),
        "a": str(a),
        "w": str(w),
        "v_squared": str(v2),
        "ratio": str(ratio),
        "gradient": [str(x) for x in gradient],
        "radial_shift": str(shift),
        "shifted_leading_minors": [str(x) for x in minors],
        "vector_mass_squares": [str(x) for x in vectors],
        "minimum_nonquark_mass_squared": str(tau2),
        "stationary": gradient == sp.zeros(4, 1),
        "radial_above_half_vector_threshold": all(x > 0 for x in minors),
        "vector_pair_closed": all(x > 0 for x in vector_pair_margins),
        "nonquark_pairs_closed": all(x > 0 for x in threshold_margins),
    }


left = witness(1)
right = witness(2)

checks = {
    "wp489_dependency_passed": bool(wp489["passed"]),
    "wp536_dependency_passed": bool(wp536["passed"]),
    "both_points_are_stationary": left["stationary"] and right["stationary"],
    "both_radial_blocks_close_vector_decays": left["radial_above_half_vector_threshold"] and right["radial_above_half_vector_threshold"],
    "both_vector_pair_domains_are_closed": left["vector_pair_closed"] and right["vector_pair_closed"],
    "both_nonquark_pair_domains_are_closed": left["nonquark_pairs_closed"] and right["nonquark_pairs_closed"],
    "electroweak_norm_is_fixed": sp.sympify(left["v_squared"]) == sp.sympify(right["v_squared"]) == 2,
    "clock_ratio_changes_by_exact_factor_two": sp.simplify(sp.sympify(left["ratio"]) / sp.sympify(right["ratio"])) == 2,
    "source_coefficients_differ_only_along_declared_a_w_fiber": left["a"] != right["a"] and left["w"] != right["w"],
}
checks = {name: bool(value) for name, value in checks.items()}

for point in (left, right):
    for key in ("stationary", "radial_above_half_vector_threshold", "vector_pair_closed", "nonquark_pairs_closed"):
        point[key] = bool(point[key])

result = {
    "work_package": "WP537",
    "domain": "The WP489 positive common-source action with fixed y=g_F^2=1, b=32, g_P^2=1/68, z_A=z_B=1 and positive quartics 100, restricted to a=t^2 and w=1/t.",
    "family": {
        "parameter": "t>0",
        "a": "t^2",
        "w": "1/t",
        "v_squared": "2",
        "g_F_f_over_v": "sqrt(3)/t",
    },
    "hostile_pair": [left, right],
    "theorem": "The admitted common-source grammar contains two exact stationary, positive, width-closed points with the same electroweak norm and different physical clock ratios. It therefore supplies conditional relational selection for fixed coefficients but no numerical selector of g_F f/v.",
    "classification": "Relational selector and presentation rigidifier for fixed source labels; neither a numerical selector nor a calibrated physical instrument across the coefficient fiber.",
    "smallest_exact_falsifier": "t=1 and t=2 have v^2=2 but ratios sqrt(3) and sqrt(3)/2 while satisfying the same declared stability and tree-level width-closure tests.",
    "remaining_gate": "Derive an equation fixing t from independently declared coefficient dynamics, then recompute the selected vacuum, poles, residues, widths and WP535 instrument response.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp537_fixed_v_selector_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
