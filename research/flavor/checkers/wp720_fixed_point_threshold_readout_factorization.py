"""Exact fixed-point, threshold, and detector factorization gates."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
p_n, p_m = sp.symbols("p_n_star p_m_star", real=True)
r1, r2 = sp.symbols("rho_1 rho_2", real=True)
a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22", real=True)
p_star = sp.Matrix([p_n, p_m])
rho = sp.Matrix([r1, r2])
A = sp.Matrix([[a11, a12], [a21, a22]])
d = sp.Matrix([[1, -1]])
p_low = p_star + A*rho
contrast_low = sp.expand((d*p_low)[0])
contrast_threshold_jacobian = sp.simplify(d*A)

rho_a = sp.Matrix([0, 0])
rho_b = sp.Matrix([1, 0])
A_hostile = sp.diag(1, 0)
hostile_delta = sp.simplify(
    d*((p_star+A_hostile*rho_b)-(p_star+A_hostile*rho_a))
)

A_common = sp.Matrix([[1, 2], [1, 2]])
common_mode_contrast_response = sp.simplify(d*A_common)
R_total = sp.Matrix([[1, 1]])
R_labelled = sp.eye(2)
total_kernel_witness = sp.Matrix([1, -1])

checks = {
    "threshold_contrast_response_is_dA": sp.simplify(sp.Matrix([[sp.diff(contrast_low, r1), sp.diff(contrast_low, r2)]])-d*A) == sp.zeros(1, 2),
    "generic_threshold_survival_requires_dA_zero_or_fixed_rho": contrast_threshold_jacobian == sp.Matrix([[a11-a21, a12-a22]]),
    "same_fixed_point_hostile_thresholds_change_contrast": hostile_delta == sp.Matrix([[1]]),
    "common_threshold_mode_preserves_contrast": common_mode_contrast_response == sp.zeros(1, 2),
    "unlabelled_total_readout_kills_contrast": R_total*total_kernel_witness == sp.zeros(1, 1),
    "labelled_readout_preserves_contrast": R_labelled*total_kernel_witness == total_kernel_witness,
    "labelled_readout_has_rank_two": R_labelled.rank() == 2,
    "unlabelled_readout_has_rank_one": R_total.rank() == 1,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP720",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "an isolated source fixed portal p_star, two relevant threshold coordinates rho, affine matching p_low=p_star+A rho, and linear detector response",
    "faithful_coordinate": "the ordered low-energy portal pair (g_n,g_m), with contrast covector d=(1,-1)",
    "pipeline": "isolated fixed point -> relevant deformation -> threshold matching -> detector response",
    "first_nonfaithful_arrow": "threshold matching unless d A=0 or the source uniquely fixes rho",
    "smallest_exact_falsifier": "one threshold coordinate shifts only g_n: identical p_star with rho=(0,0) and rho=(1,0) gives contrast difference one",
    "threshold_survival_gate": "d A=0 for contrast protection, or a source-normalized unique relevant trajectory with fixed dimensionless threshold ratios",
    "instrument_gate": "an unlabelled total response R=(1,1) kills the contrast direction; two labelled channels R=I preserve it",
    "classification": "an interacting fixed point is a source selector only before thresholds; low-energy selection requires trajectory rigidity and an incidence-preserving instrument",
}
(ROOT / "results" / "wp720_fixed_point_threshold_readout_factorization.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
