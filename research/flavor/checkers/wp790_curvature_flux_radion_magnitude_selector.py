"""Exact curvature-flux radion and portal-magnitude audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp789 = json.loads(
    (ROOT / "results" / "wp789_wilson_line_angle_radius_homogeneity_no_go.json")
    .read_text(encoding="utf-8")
)

R = sp.symbols("R", positive=True)
A, B, n = sp.symbols("A B n", positive=True)
sigma = sp.symbols("sigma", real=True)
C = sp.symbols("C", real=True)

V = -B / R**4 + A * n**2 / R**6
dV = sp.factor(sp.diff(V, R))
R2_star = sp.simplify(3 * A * n**2 / (2 * B))

# Use the on-shell relation A*n^2=(2/3)B*R^2.
hessian_on_shell = sp.simplify(
    sp.diff(V, R, 2).subs(A * n**2, sp.Rational(2, 3) * B * R**2)
)
energy_on_shell = sp.simplify(
    V.subs(A * n**2, sp.Rational(2, 3) * B * R**2)
)

R_star = sp.sqrt(R2_star)
signed_threshold = sp.simplify(sigma * n / R_star)
threshold_magnitude = sp.simplify(n / R_star)

# Add the 6D cosmological contribution C/R^2 and solve simultaneous
# stationarity plus zero four-dimensional vacuum energy.
x = sp.symbols("x", positive=True)
V_uplift_x = C / x - B / x**2 + A * n**2 / x**3
zero_eq = sp.factor(V_uplift_x * x**3)
stationary_eq = sp.factor(
    sp.diff(C / R**2 - B / R**4 + A * n**2 / R**6, R)
    * (-R**7 / 2)
).subs(R**2, x)
minkowski_solution = {
    x: sp.simplify(2 * A * n**2 / B),
    C: sp.simplify(B**2 / (4 * A * n**2)),
}
minkowski_zero = sp.simplify(zero_eq.subs(minkowski_solution))
minkowski_stationary = sp.simplify(stationary_eq.subs(minkowski_solution))

checks = {
    "wp789_dependency_passed": wp789["status"] == "PASS"
    and all(wp789["checks"].values()),
    "curvature_flux_stationary_equation": sp.simplify(
        dV - 2 * (2 * B * R**2 - 3 * A * n**2) / R**7
    )
    == 0,
    "finite_radius_is_fixed": R2_star == 3 * A * n**2 / (2 * B),
    "radion_hessian_is_strictly_positive": hessian_on_shell == 8 * B / R**6,
    "unlifted_vacuum_is_ads": energy_on_shell == -B / (3 * R**4),
    "signed_threshold_magnitude_is_flux_integer_independent":
        threshold_magnitude == sp.sqrt(6) * sp.sqrt(B) / (3 * sp.sqrt(A)),
    "orientation_bit_survives_radion_selection": signed_threshold
    == sp.sqrt(6) * sp.sqrt(B) * sigma / (3 * sp.sqrt(A)),
    "minkowski_completion_solves_zero_energy": minkowski_zero == 0,
    "minkowski_completion_solves_stationarity": minkowski_stationary == 0,
    "minkowski_uplift_coefficient_depends_on_flux_and_ratio":
        minkowski_solution[C] == B**2 / (4 * A * n**2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP790",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP789",
    "admitted_state_domain": (
        "a six-dimensional Einstein-frame radius R, positive curvature and "
        "Maxwell-flux coefficients B and A, positive flux magnitude n, an "
        "independent orientation bit sigma, and an optional cosmological "
        "coefficient C"
    ),
    "faithful_coordinate": (
        "signed flux sigma*n, Einstein-frame radius, full radion Hessian, "
        "signed threshold sigma*n/R, and four-dimensional vacuum energy"
    ),
    "source_authorized_probe_family": (
        "the classical curvature term -B/R^4 and quantized flux energy "
        "A*n^2/R^6; gauge-gravity relations fixing A/B are not assumed"
    ),
    "contextual_partition": (
        "curvature-flux balance identifies all flux orientations at fixed "
        "magnitude, while fixing one radius and one absolute threshold magnitude"
    ),
    "selector_result": (
        "the balance is a strict radion selector and conditional portal-"
        "magnitude selector, but it is exactly blind to the flux orientation"
    ),
    "smallest_exact_falsifier": (
        "sigma=+1 and sigma=-1 have identical radius, Hessian, energy, and "
        "threshold magnitude, but opposite signed portal readouts"
    ),
    "magnitude_result": (
        "R_*^2=3*A*n^2/(2*B) and |n|/R_*=sqrt(2*B/(3*A)); the flux integer "
        "cancels, but numerical authority remains in the gauge-gravity ratio B/A"
    ),
    "vacuum_result": (
        "without uplift the strict minimum is AdS; a Minkowski completion "
        "requires C=B^2/(4*A*n^2), an additional coefficient relation"
    ),
    "rg_result": (
        "the positive radion Hessian supplies a local classical vacuum basin, "
        "not a computed quantum RG basin for A/B or the portal"
    ),
    "threshold_result": (
        "the absolute Kaluza-Klein/flux threshold is fixed conditional on A/B "
        "and is independent of flux magnitude, but quantum and localized "
        "threshold corrections remain uncomputed"
    ),
    "instrument_result": (
        "mass spectroscopy can read the fixed magnitude; a parity- or chirality-"
        "sensitive labelled channel is still required to read sigma"
    ),
    "deutschian_status": (
        "curvature-flux competition explains why a finite clock and magnitude "
        "exist, but not the orientation or the gauge-gravity coefficient ratio"
    ),
    "remaining_gate": (
        "derive A/B and the flux orientation from one non-mirror-completable "
        "gauge-gravity source, then compute quantum RG stability, localized "
        "matching, and a calibrated signed instrument"
    ),
    "primary_source": "https://arxiv.org/abs/2312.03184",
}
(ROOT / "results" / "wp790_curvature_flux_radion_magnitude_selector.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
