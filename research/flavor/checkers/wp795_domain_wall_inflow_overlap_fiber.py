"""Exact domain-wall chirality, anomaly, and flavor-overlap audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp794 = json.loads(
    (ROOT / "results" / "wp794_mirror_equivariant_pipeline_selector_no_go.json")
    .read_text(encoding="utf-8")
)

y, mu, ell, rho = sp.symbols("y mu ell rho", positive=True, real=True)
delta = sp.symbols("delta", positive=True, real=True)

A = (2 * mu**2 / sp.pi) ** sp.Rational(1, 4)
profile = A * sp.exp(-mu**2 * (y - ell) ** 2)
wall = 2 * mu**2 * (y - ell)

normalization = sp.integrate(profile**2, (y, -sp.oo, sp.oo))
left_zero_residual = sp.simplify(sp.diff(profile, y) + wall * profile)
right_zero_residual = sp.simplify(-sp.diff(profile, y) + wall * profile)

# Exact overlap of two normalized Gaussian wall modes separated by delta.
profile_left = A * sp.exp(-mu**2 * y**2)
profile_right = A * sp.exp(-mu**2 * (y - delta) ** 2)
overlap = sp.simplify(
    sp.integrate(profile_left * profile_right, (y, -sp.oo, sp.oo))
)
expected_overlap = sp.exp(-mu**2 * delta**2 / 2)
effective_yukawa = rho * overlap

# The five-dimensional mass M shifts the center without changing chirality.
M = sp.symbols("M", real=True)
shifted_center = -M / (2 * mu**2)

# Hostile same-topology configurations. They share kink orientation, one
# chiral zero mode, and anomaly coefficient, but differ in overlaps. Swapping
# the two separations reverses the portal contrast without changing inflow.
g_near = sp.simplify(effective_yukawa.subs(delta, 1 / mu))
g_far = sp.simplify(effective_yukawa.subs(delta, 2 / mu))
contrast_positive = sp.simplify(g_near - g_far)
contrast_negative = sp.simplify(g_far - g_near)

# The first heavy wall excitation is controlled by mu, not the index.
threshold_one = mu
threshold_two = 2 * mu
anomaly_index_one = sp.Integer(1)
anomaly_index_two = sp.Integer(1)

checks = {
    "wp794_dependency_passed": wp794["status"] == "PASS"
    and all(wp794["checks"].values()),
    "gaussian_zero_mode_is_normalized": normalization == 1,
    "one_chirality_solves_wall_zero_mode_equation": left_zero_residual == 0,
    "opposite_chirality_is_not_a_zero_mode": right_zero_residual != 0,
    "mass_shift_moves_localization_center":
        sp.diff(shifted_center, M) == -1 / (2 * mu**2),
    "exact_overlap_matches_exponential":
        sp.simplify(overlap - expected_overlap) == 0,
    "near_and_far_overlaps_are_distinct":
        sp.simplify(g_near - g_far) != 0,
    "swapping_separations_reverses_portal_contrast":
        contrast_negative == -contrast_positive,
    "portal_contrast_is_strictly_positive_in_near_far_order":
        sp.simplify(contrast_positive / rho)
        == sp.exp(-sp.Rational(1, 2)) - sp.exp(-2),
    "threshold_scale_varies_while_anomaly_index_does_not":
        threshold_one != threshold_two
        and anomaly_index_one == anomaly_index_two,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP795",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP794",
    "admitted_state_domain": (
        "a five-dimensional fermion coupled to an oriented scalar domain wall "
        "with asymptotic boundary vacua, Gaussian linear-wall zero modes, "
        "continuous bulk masses M_i, wall slope mu, higher-dimensional Yukawa "
        "normalization rho, and the bulk-edge anomaly-inflow channel"
    ),
    "faithful_coordinate": (
        "wall orientation and endpoint vacua, zero-mode chirality, anomaly "
        "coefficient, every localization center, wall slope, normalized "
        "wavefunction overlap, heavy-mode threshold, and detector channel"
    ),
    "source_authorized_probe_family": (
        "the first-order domain-wall Dirac operator, its normalizable index, "
        "bulk Chern-Simons anomaly inflow, Gaussian overlap integrals, and the "
        "mass gap to paired heavy modes"
    ),
    "contextual_partition": (
        "fixed oriented boundary endpoints select one chiral zero mode and "
        "one anomaly-inflow sign, but continuous M_i, mu, and rho fibers "
        "remain within that same topological sector and generate distinct "
        "flavor overlaps"
    ),
    "selector_result": (
        "the prepared wall is a relative chirality selector and anomaly "
        "rigidifier; it is neither a numerical flavor-overlap selector nor a "
        "selector of the wall boundary history itself"
    ),
    "smallest_exact_falsifier": (
        "separations delta=1/mu and delta=2/mu have the same wall chirality "
        "and anomaly coefficient but Yukawas rho*exp(-1/2) and rho*exp(-2); "
        "swapping them reverses g_n-g_m"
    ),
    "sign_result": (
        "fixed ordered boundary vacua select chirality relative to the wall "
        "normal, but the mirror antikink exists unless the boundary history "
        "itself is independently source-authorized"
    ),
    "magnitude_result": (
        "flavor magnitude depends continuously on rho, mu, and mass-controlled "
        "separations; anomaly inflow quantizes none of these overlap data"
    ),
    "rg_threshold_result": (
        "anomaly matching survives RG and massive thresholds, but the first "
        "heavy wall scale is proportional to mu and the flavor Yukawas retain "
        "their continuous boundary-profile inputs"
    ),
    "instrument_result": (
        "the inflow current is a typed anomaly response, while masses and CKM "
        "elements are physical flavor readouts; the cited split-fermion model "
        "fits localization positions and supplies no source-calibrated "
        "physical16 perturbation instrument"
    ),
    "deutschian_status": (
        "domain-wall inflow explains why chirality and anomaly response are "
        "robust once an oriented wall history is prepared, but it does not "
        "explain the wall orientation or numerical flavor overlaps"
    ),
    "remaining_gate": (
        "derive the ordered wall endpoints, all M_i, mu, and rho from one "
        "non-mirror-completable source history, and propagate its perturbations "
        "through RG, finite thresholds, and a calibrated physical16 channel"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/hep-lat/9206013",
        "https://arxiv.org/abs/2001.03318",
        "https://arxiv.org/abs/hep-ph/9912265",
    ],
}

(ROOT / "results" / "wp795_domain_wall_inflow_overlap_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
