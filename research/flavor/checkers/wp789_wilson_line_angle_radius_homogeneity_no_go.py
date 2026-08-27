"""Exact Wilson-line selection versus radius-clock audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp788 = json.loads(
    (ROOT / "results" / "wp788_5d_susy_prepotential_coulomb_modulus_no_go.json")
    .read_text(encoding="utf-8")
)

R, theta, phi, C = sp.symbols("R theta phi C", positive=True, real=True)
F = sp.Function("F")

V_general = C * F(theta) / R**4
d_theta = sp.diff(V_general, theta)
d_R = sp.diff(V_general, R)
h_theta_theta = sp.diff(V_general, theta, 2)
h_theta_R = sp.diff(V_general, theta, R)
h_R_R = sp.diff(V_general, R, 2)

# Maximally favorable oriented periodic selector.
U = 1 - sp.cos(theta - phi)
V_favorable = C * U / R**4
stationary_subs = {theta: phi}
fav_gradient = (
    sp.simplify(sp.diff(V_favorable, theta).subs(stationary_subs)),
    sp.simplify(sp.diff(V_favorable, R).subs(stationary_subs)),
)
fav_hessian = sp.simplify(sp.hessian(V_favorable, (theta, R)).subs(stationary_subs))

# The full one-scale stationary conditions F=F'=0 force a null radius row.
stationary_hessian = sp.Matrix(
    [
        [h_theta_theta, h_theta_R],
        [h_theta_R, h_R_R],
    ]
).subs({F(theta): 0, sp.diff(F(theta), theta): 0})

# Minimal second-homogeneity repair.
A, B, f, g = sp.symbols("A B f g", nonzero=True, real=True)
V_two = A * f / R**4 + B * g / R**6
dR_two = sp.factor(sp.diff(V_two, R))
R_squared_solution = sp.simplify(-3 * B * g / (2 * A * f))
two_scale_hessian_on_shell = sp.simplify(
    sp.diff(V_two, R, 2).subs(B * g, -sp.Rational(2, 3) * A * f * R**2)
)

# Fixed Wilson angle does not fix the absolute Kaluza-Klein threshold.
q = sp.symbols("q", nonzero=True, real=True)
threshold = sp.Abs(q * phi) / R
radius_hostile_ratio = sp.simplify(threshold.subs(R, 2 * R) / threshold)

checks = {
    "wp788_dependency_passed": wp788["status"] == "PASS"
    and all(wp788["checks"].values()),
    "one_scale_angle_derivative": d_theta
    == C * sp.diff(F(theta), theta) / R**4,
    "one_scale_radius_derivative": d_R == -4 * C * F(theta) / R**5,
    "joint_stationarity_requires_zero_shape_value": sp.solve(
        sp.Eq(d_R, 0), F(theta)
    )
    == [0],
    "favorable_oriented_angle_is_jointly_stationary": fav_gradient == (0, 0),
    "favorable_angle_has_positive_curvature": fav_hessian[0, 0] == C / R**4,
    "favorable_radius_is_exactly_flat": fav_hessian[1, 1] == 0
    and fav_hessian.det() == 0,
    "general_one_scale_stationary_hessian_has_null_radius_row":
        stationary_hessian[0, 1] == 0
        and stationary_hessian[1, 0] == 0
        and stationary_hessian[1, 1] == 0,
    "two_scale_radius_solution_depends_on_coefficient_ratio": R_squared_solution
    == -3 * B * g / (2 * A * f),
    "two_scale_radial_hessian_requires_signed_balance":
        two_scale_hessian_on_shell == -8 * A * f / R**6,
    "doubling_free_radius_halves_absolute_threshold": radius_hostile_ratio
    == sp.Rational(1, 2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP789",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP788",
    "admitted_state_domain": (
        "a dimensionless Wilson angle theta, positive radius R, a general "
        "single-scale four-dimensional Casimir potential C*F(theta)/R^4, a "
        "maximally favorable oriented periodic shape, and the minimal added "
        "R^-6 homogeneity"
    ),
    "faithful_coordinate": (
        "Wilson angle, compactification radius, full two-variable gradient and "
        "Hessian, and absolute charge-labelled Kaluza-Klein threshold"
    ),
    "source_authorized_probe_family": (
        "the one-scale Casimir/Hosotani effective potential and its exact "
        "angle/radius derivatives; the oriented phase phi is treated as a "
        "favorable conditional source input, not as already derived"
    ),
    "contextual_partition": (
        "the favorable periodic shape selects theta=phi modulo its period, but "
        "every positive radius is contextually equivalent at the joint minimum"
    ),
    "selector_result": (
        "one-scale Hosotani dynamics is a dimensionless angle selector and "
        "rigidifier, but cannot be a strict joint angle-radius selector"
    ),
    "smallest_exact_falsifier": (
        "(theta,R)=(phi,R0) and (phi,2*R0) have the same one-scale minimum and "
        "angle curvature, while every absolute threshold is halved"
    ),
    "two_scale_result": (
        "adding an R^-6 contribution can stabilize the radius only at "
        "R^2=-3*B*g/(2*A*f), so the clock is transferred to an independently "
        "derived signed coefficient ratio"
    ),
    "rg_result": (
        "positive Wilson-angle curvature supplies a local angular basin, but "
        "the joint Hessian has a radius zero mode and therefore no complete RG "
        "or vacuum basin"
    ),
    "threshold_result": (
        "charge and Wilson-angle ratios can survive compactification, while "
        "absolute thresholds remain proportional to 1/R"
    ),
    "instrument_result": (
        "relative spectral lines can read charge ratios, but absolute detector "
        "calibration and signed orientation require the unstabilized radius and "
        "an additional interference channel"
    ),
    "deutschian_status": (
        "radiative compactification can make a dimensionless angle hard to "
        "vary, but a single homogeneous source cannot explain its own clock"
    ),
    "remaining_gate": (
        "derive two distinct radius scalings and their signed coefficient ratio "
        "from the same chiral source packet, then prove the resulting joint "
        "minimum survives thresholds and maps to a calibrated signed readout"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/hep-ph/0401183",
        "https://arxiv.org/abs/1009.5353",
    ],
}
(ROOT / "results" / "wp789_wilson_line_angle_radius_homogeneity_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
