"""Exact WP592 isolated fixed-ray criterion for the common-clock CP ratio."""

import json
from pathlib import Path

import sympy as sp

x, r, g2 = sp.symbols("x r g2", positive=True, real=True)
A, B, C, D = sp.symbols("A B C D", positive=True, real=True)

# x=y^2/g^2 and r=chi/y^2. The gauge coupling is evaluated at a nonzero
# fixed point, so g2 is constant in this reduced ray calculation.
beta_x = 2 * x * g2 * (A * x - B)
beta_r = r * g2 * (C * r * x - D * x - 2 * (A * x - B))

x_star = B / A
r_star = D / C
fixed_subs = {x: x_star, r: r_star}
jacobian = sp.Matrix([beta_x, beta_r]).jacobian([x, r])
fixed_jacobian = sp.simplify(jacobian.subs(fixed_subs))
fixed_determinant = sp.factor(fixed_jacobian.det())

# The fixed-line hostile removes the r-dependent beta coefficient.
fixed_line_beta_r = sp.simplify(beta_r.subs({C: 0, D: 0, x: x_star}))

checks = {
    "x_fixed_ray_is_exact": sp.simplify(beta_x.subs(fixed_subs)) == 0,
    "r_fixed_ray_is_exact": sp.simplify(beta_r.subs(fixed_subs)) == 0,
    "selected_ratio_is_D_over_C": r_star == D / C,
    "overall_gauge_magnitude_cancels_from_ratio": g2 not in r_star.free_symbols,
    "fixed_ray_jacobian_is_full_rank": fixed_determinant
    == 2 * B**2 * D * g2**2 / A,
    "fixed_ray_determinant_is_positive": bool(
        sp.StrictGreaterThan(fixed_determinant, 0)
    ),
    "fixed_line_hostile_leaves_r_free": fixed_line_beta_r == 0,
    "coefficient_hostile_changes_prediction": r_star.subs({C: 1, D: 1}) == 1
    and r_star.subs({C: 1, D: 2}) == 2,
}

if not all(checks.values()):
    raise SystemExit(f"WP592 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP592",
    "status": "PASS",
    "checks": checks,
    "reduced_coordinates": "x=y^2/g^2 and r=chi/y^2",
    "beta_system": {
        "beta_x": sp.sstr(beta_x),
        "beta_r": sp.sstr(beta_r),
    },
    "isolated_fixed_ray": {
        "x_star": sp.sstr(x_star),
        "r_star": sp.sstr(r_star),
        "jacobian": [
            [sp.sstr(value) for value in fixed_jacobian.row(i)]
            for i in range(fixed_jacobian.rows)
        ],
        "determinant": sp.sstr(fixed_determinant),
    },
    "hard_to_vary_content": "once A,B,C,D are derived from frozen field content and scheme, changing r_star requires changing the beta-function law",
    "remaining_variability": "choosing C or D after inspecting flavor data merely moves the fit into beta-function coefficients",
    "classification": "exact acceptance architecture for a hard-to-vary CP/flavor-clock ratio; not yet a realized flavor source",
    "smallest_exact_falsifier": "C=D=0 gives a fixed line in r and destroys isolation; C=1,D=1 versus C=1,D=2 changes r_star from one to two",
    "experiment_after_realization": "joint calibrated measurement of s^2/f^2 must equal D/(6*C) and survive threshold and detector transport",
    "full_flavor_gate": "derive the complete anomaly-free beta system and enough isolated ray relations to constrain the remaining physical16 moduli",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp592_cp_clock_fixed_ray_criterion.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
