from fractions import Fraction
import json
from pathlib import Path


def A(v):
    return v[0] - v[1]


def current_jump(v):
    return v[1] ** 2 - v[0] ** 2


omega = (Fraction(1), Fraction(1))
h_good = (Fraction(-3, 2), Fraction(-1, 2))
h_bad = (Fraction(0), Fraction(1))
shifted_good = tuple(x + y for x, y in zip(omega, h_good))
shifted_bad = tuple(x + y for x, y in zip(omega, h_bad))

checks = {
    "gaussian_homogeneous": A(omega) == 0,
    "good_affine_anomaly": A(h_good) == -1,
    "good_endpoint_sewing": current_jump(shifted_good) == 0,
    "good_positive_energy": sum(x * x for x in shifted_good) > 0,
    "bad_affine_anomaly": A(h_bad) == -1,
    "deliberate_failure_nonzero_jump": current_jump(shifted_bad) != 0,
}
assert all(checks.values())

result = {
    "schema": "marici.affine-shift-observer-witness.v1",
    "status": "passed",
    "arithmetic": "exact_rational",
    "omega": [str(x) for x in omega],
    "h_good": [str(x) for x in h_good],
    "shifted_good": [str(x) for x in shifted_good],
    "good_current_jump": str(current_jump(shifted_good)),
    "good_energy": str(sum(x * x for x in shifted_good)),
    "h_bad": [str(x) for x in h_bad],
    "shifted_bad": [str(x) for x in shifted_bad],
    "deliberate_failure_current_jump": str(current_jump(shifted_bad)),
    "checks": checks,
    "scope": "finite algebraic consistency only; no source derivation or completed-limit claim",
}
out = Path(__file__).parents[1] / "results" / "affine-shift-observer-witness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}))
