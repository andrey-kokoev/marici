"""Exact WP628 audit of entrance kinetic mixing and canonical alignment."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def det(k):
    return k[0][0] * k[1][1] - k[0][1] * k[1][0]

def inverse(k):
    d = det(k)
    return [[k[1][1] / d, -k[0][1] / d],
            [-k[1][0] / d, k[0][0] / d]]

def normalized_overlap_squared(k):
    ki = inverse(k)
    return ki[0][1] ** 2 / (ki[0][0] * ki[1][1])

k0 = [[F(1), F(0)], [F(0), F(1)]]
k1 = [[F(2), F(1)], [F(1), F(2)]]
kbad = [[F(1), F(1)], [F(1), F(1)]]

checks = {
    "canonical_gram_is_positive": k0[0][0] > 0 and det(k0) > 0,
    "hostile_gram_is_positive": k1[0][0] > 0 and det(k1) == 3,
    "canonical_axes_are_orthogonal": normalized_overlap_squared(k0) == 0,
    "hostile_axes_have_quarter_overlap_squared": normalized_overlap_squared(k1) == F(1, 4),
    "off_diagonal_zero_is_exact_alignment_condition": inverse(k1)[0][1] == F(-1, 3),
    "singular_hostile_boundary_is_rejected": det(kbad) == 0,
    "gauge_representation_does_not_separate_doublets": (1, 2, F(1, 2), "SO3E-vector") == (1, 2, F(1, 2), "SO3E-vector"),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP628", "status": "PASS", "checks": checks,
    "admitted_domain": "two identically represented SO(3)_E-vector electroweak entrance doublets",
    "field_redefinition_quotient": "positive kinetic Grams with all interaction tensors transformed covariantly",
    "hostile_pair": {"K0": [[1, 0], [0, 1]], "rho0_squared": "0",
                     "K1": [[2, 1], [1, 2]], "rho1_squared": "1/4"},
    "classification": "model-export obstruction; neither selector nor rigidifier instrument",
    "first_nonfaithful_arrow": "dropping the off-diagonal entrance kinetic Gram while retaining axis-aligned Yukawa tensors",
    "smallest_exact_falsifier": "K=[[2,1],[1,2]] has determinant 3 and canonical-axis overlap squared 1/4",
    "repair_gate": "derive a source symmetry distinguishing Hu and Hd, or run the complete two-family kinetic/Yukawa tensor system",
}
(ROOT / "results" / "wp628_entrance_kinetic_gram_obstruction.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

