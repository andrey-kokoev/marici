import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "results" / "t7_residual_uv_counterterm.json"

# Coordinates are (e1,e2,e3,e4,e5,e6,v_alg).  The e1 coefficient is positive
# and nonzero.  Generically v_alg also has a Lambda^4 e8/e9-tail coefficient,
# denoted kappa.  Its exact normalization is frame and kinematics dependent.
kappa = 1
leading_uv_grade = (1, 0, 0, 0, 0, 0, kappa)
residual_e1_detector = (1, 0, 0, 0, 0, 0, 0)


def pair(a, b):
    return sum(x * y for x, y in zip(a, b, strict=True))


pairing = pair(residual_e1_detector, leading_uv_grade)
result = {
    "checker": "t7_residual_uv_counterterm",
    "basis": ["e1", "e2", "e3", "e4", "e5", "e6", "v_alg"],
    "leading_cutoff_grade": "Lambda^4",
    "leading_uv_counterterm_direction": leading_uv_grade,
    "v_alg_coefficient_status": "generic nonzero marker; exact scalar is frame and kinematics dependent",
    "residual_e1_detector": residual_e1_detector,
    "pairing": pairing,
    "residual_quotient_annihilates_uv_counterterms": pairing == 0,
    "canonical_unrenormalized_rank_test_possible": False,
}

assert pairing == 1
assert not result["residual_quotient_annihilates_uv_counterterms"]
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
