"""Exact maximal conditional selector with one calibrated physical clock."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
w, s = sp.symbols("w s", positive=True)
a, y, zA, zB, kappa = sp.symbols("a y z_A z_B kappa", positive=True)
alpha_v, Cm, DeltaC = sp.symbols("alpha_v C_m Delta_C", positive=True)
precision_1, precision_2, covariance = sp.symbols("p q r", real=True)

v = sp.sqrt(2*a)*w
Lambda_c = kappa*w
f = sp.sqrt(6)*y*w
MA = zA*w
MB = zB*w
Cn = Cm+DeltaC
portal_contrast = sp.factor(alpha_v*(Cn-Cm))

ratios = sp.Matrix([f/v, MA/v, MB/v, v/Lambda_c, MA/MB])
scaled_ratios = sp.simplify(ratios.subs(w, s*w))
absolute_scales = sp.Matrix([v, Lambda_c, f, MA, MB])
scaled_absolute = sp.simplify(absolute_scales.subs(w, s*w))

R_labelled = sp.eye(2)
R_total = sp.Matrix([[1, 1]])
contrast_direction = sp.Matrix([1, -1])
W = sp.Matrix([[precision_1, covariance], [covariance, precision_2]])
labelled_gram = sp.simplify(R_labelled.T*W*R_labelled)

checks = {
    "one_clock_scales_every_absolute_mass": sp.simplify(scaled_absolute-s*absolute_scales) == sp.zeros(5, 1),
    "all_source_threshold_ratios_are_clock_independent": sp.simplify(scaled_ratios-ratios) == sp.zeros(5, 1),
    "safe_trajectory_argument_is_source_fixed": sp.simplify(v/Lambda_c-sp.sqrt(2*a)/kappa) == 0,
    "representation_order_fixes_positive_contrast_sign": portal_contrast == alpha_v*DeltaC,
    "portal_magnitude_is_independent_of_clock_value": sp.diff(portal_contrast, w) == 0,
    "messenger_threshold_ratio_is_fixed": sp.simplify(MA/MB-zA/zB) == 0,
    "labelled_detector_preserves_contrast": R_labelled*contrast_direction == contrast_direction,
    "unlabelled_total_detector_kills_contrast": R_total*contrast_direction == sp.zeros(1, 1),
    "labelled_information_gram_has_calibrated_determinant": sp.factor(labelled_gram.det()) == precision_1*precision_2-covariance**2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP724",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one calibrated electroweak clock v, a common-singlet mass constructor, and a hypothetical source-fixed dimensionless gauge-Yukawa packet",
    "faithful_coordinate": "ordered portal pair, source-fixed mass ratios, RG point at v/Lambda_c, and two labelled detector responses",
    "candidate_source_principle": "a clock-locked asymptotically safe representation source",
    "required_source_equalities": [
        "representation theory fixes C_n=C_m+Delta_C with Delta_C>0",
        "the interacting fixed point fixes alpha_v and every dimensionless coefficient",
        "the relevant trajectory is locked by Lambda_c=kappa w with source-fixed kappa",
        "the common singlet gives v=sqrt(2a)w and M_i=z_i w",
        "threshold matching uses only the fixed ratios and preserves the contrast",
        "two representation-labelled channels have an independently calibrated positive detector metric",
    ],
    "conditional_prediction": "Delta_portal=alpha_v Delta_C; M_A/v=z_A/sqrt(2a); M_B/v=z_B/sqrt(2a); v/Lambda_c=sqrt(2a)/kappa",
    "classification": "a complete selector architecture conditional on one calibrated clock, not an existing admitted flavor theorem",
    "smallest_exact_falsifiers": [
        "any free dimensionless coefficient among a,kappa,z_A,z_B,alpha_v,Delta_C",
        "a threshold response that changes contrast at fixed source ratios",
        "rank-one unlabelled detector response",
    ],
    "remaining_physical_gate": "construct one anomaly-free matter theory realizing all source equalities and bind its two labelled channels to an actual finite-width calibrated experiment",
}
(ROOT / "results" / "wp724_clock_locked_conditional_selector.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
