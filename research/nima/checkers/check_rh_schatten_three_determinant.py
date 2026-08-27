from fractions import Fraction as F
import json
from pathlib import Path


def log_coefficient(k):
    return F((-1) ** (k + 1), k)


regularized = {k: log_coefficient(k) for k in range(1, 7)}
regularized[1] -= 1
regularized[2] += F(1, 2)

assert regularized[1] == 0
assert regularized[2] == 0
assert regularized[3] == F(1, 3)

# Eight-term even alternating partial sum is a rigorous lower bound for log(2).
log2_lower = sum((F(1, k) if k % 2 else -F(1, k)) for k in range(1, 9))
assert log2_lower > F(5, 8)

result = {
    "schema": "marici.rh-schatten-three-determinant.v1",
    "regularized_log_coefficients": {str(k): str(v) for k, v in regularized.items()},
    "first_surviving_order": 3,
    "removed_cumulants": [1, 2],
    "repeated_safe_mode_hostile": {
        "eigenvalue": "-1/2",
        "per_mode_factor": "exp(5/8)/2 < 1",
        "proof": f"log(2) > {log2_lower} > 5/8",
        "failure": "unbounded_S3_mass_collapses_regularized_determinant",
    },
    "single_mode_hostile": {
        "eigenvalue": "-1+1/N",
        "failure": "bounded_S3_mass_but_inverse_gap_collapses",
    },
    "required_boundary_packet": ["order_1_current", "order_2_current"],
}

out = Path(__file__).parents[1] / "results" / "rh-schatten-three-determinant.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
