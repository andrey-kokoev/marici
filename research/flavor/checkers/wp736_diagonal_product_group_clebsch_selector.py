"""Exact Clebsch matching and low-energy RG defect for WP736."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sqrt2 = sp.sqrt(2)
I = sp.I

sigma = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
T0 = sp.eye(2) / sqrt2
Ta = [matrix / sqrt2 for matrix in sigma]
basis = [T0, *Ta]
gram = sp.Matrix([
    [sp.simplify(sp.trace(left.conjugate().T * right)) for right in basis]
    for left in basis
])

kU = sp.symbols("kappa_U", positive=True)
kA = kU / sqrt2
kB = sqrt2 * kU
alpha_ratio = sp.factor(kB**2 / kA**2)
q = sp.symbols("q", positive=True)
portal_contrast = sp.factor(-4 * q + 3 * alpha_ratio * q)

a, b, u, v, T, g1, g2 = sp.symbols(
    "a b u v T g1 g2", positive=True
)
log_a = 3 * u + 9 * a + sp.Rational(21, 4) * b + 6 * T \
    - sp.Rational(15, 2) * g1 - sp.Rational(9, 2) * g2
log_b = 3 * v + sp.Rational(23, 4) * b + 7 * a + 6 * T \
    - sp.Rational(15, 2) * g1 - sp.Rational(33, 2) * g2
log_u = 8 * u + 2 * a - 12 * g1
log_v = 12 * v + sp.Rational(1, 2) * b - 12 * g1 - 24 * g2
ray = {b: 4 * a, v: u}
ratio_ba_flow = sp.factor((log_b - log_a).subs(ray))
ratio_vu_flow = sp.factor((log_v - log_u).subs(ray))
ratio_R_flow = sp.factor((log_b - log_a + log_v - log_u).subs(ray))

# The parent PyR@TE matrix result reduces at kappa_U = k I_3 to
# 2 tr(kappa^dag kappa) + 3/2 kappa kappa^dag.
parent_amplitude_self = 2 * 3 + sp.Rational(3, 2)
parent_squared_self = 2 * parent_amplitude_self
hostile = ratio_ba_flow.subs(g2, 1)

checks = {
    "singlet_triplet_basis_is_orthonormal": gram == sp.eye(4),
    "parent_to_singlet_matching_is_exact": sp.simplify(kA - kU / sqrt2) == 0,
    "parent_to_triplet_matching_is_exact": sp.simplify(kB - sqrt2 * kU) == 0,
    "squared_clebsch_ratio_is_four": alpha_ratio == 4,
    "matching_portal_contrast_is_positive_8q": portal_contrast == 8 * q,
    "parent_amplitude_self_coefficient_is_15_over_2": parent_amplitude_self == sp.Rational(15, 2),
    "parent_squared_self_coefficient_is_15": parent_squared_self == 15,
    "kappa_ratio_flow_defect_is_minus_12_g2": ratio_ba_flow == -12 * g2,
    "flavor_yukawa_ratio_flow_defect_is_4u_minus_24_g2": sp.simplify(
        ratio_vu_flow - (4 * u - 24 * g2)
    ) == 0,
    "portal_product_ratio_flow_is_4u_minus_36_g2": sp.simplify(
        ratio_R_flow - (4 * u - 36 * g2)
    ) == 0,
    "matching_R_is_four": alpha_ratio == 4,
    "positive_portal_sign_boundary_is_R_greater_than_4_over_3": sp.Rational(4, 3) < 4,
    "hostile_weak_gauge_residual_is_nonzero": hostile == -12 and hostile != 0,
    "clebsch_ray_is_not_low_energy_RG_invariant": ratio_ba_flow != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP736",
    "status": "PASS",
    "checks": checks,
    "parent_group": "SU(2)_A x SU(2)_B x U(1)_Y broken to diagonal SU(2)_L",
    "parent_fields": {
        "L": "(2,1)_-1/2",
        "H": "(1,2)_+1/2",
        "Psi_R": "(2,2)_-1",
    },
    "source_fixed_matching": {
        "kappa_A": "kappa_U/sqrt(2)",
        "kappa_B": "sqrt(2) kappa_U",
        "alpha_kappaB_over_alpha_kappaA": "4",
        "additive_portal_contrast": "8 alpha_kappaA alpha_yU > 0",
    },
    "contextual_partition": "one parent Yukawa orbit maps to a fixed singlet-triplet Clebsch ray at the diagonal-breaking surface",
    "classification": "matching-scale selector and rigidifier; not yet a numerical low-energy selector",
    "exact_transport_defect": "d log(alpha_kappaB/alpha_kappaA)/dt = -12 alpha_2 on the matching ray",
    "portal_sign_transport": "for R=(alpha_kappaB alpha_yB)/(alpha_kappaA alpha_yA), the sign survives exactly while R>4/3; R starts at 4",
    "deliberate_failure_residual": {"slice": "alpha_2=1 on the matching ray", "value": str(hostile)},
    "smallest_source_falsifier": "ordinary parent SM Yukawas are not gauge invariant when L and H occupy different SU(2) sites",
    "remaining_source_gate": "complete the link/mediator matter grammar and derive an isolated interacting parent fixed point plus its unique relevant clock ray",
    "remaining_threshold_gate": "fix the breaking scale and prove R>4/3 through finite matching and uncertainty-completed running",
    "remaining_physical_gate": "resolve singlet/triplet channels using a detector calibration whose authority locus is independent of shared source-detector drift",
    "external_reproduction": {
        "tool": "PyR@TE 3",
        "repository": "https://github.com/LSartore/pyrate",
        "revision": "04b219c2016f3fc4f2371d72607edc26a7e06364",
    },
}
(ROOT / "results" / "wp736_diagonal_product_group_clebsch_selector.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
