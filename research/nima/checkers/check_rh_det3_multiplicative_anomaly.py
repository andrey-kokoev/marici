from fractions import Fraction as F
import json
from pathlib import Path


def counterterm(x):
    return -x + x * x / 2


def boundary(x):
    return x - x * x / 2


a = F(1, 2)
b = F(1, 3)
c = a + b + a * b

bulk_anomaly = counterterm(c) - counterterm(a) - counterterm(b)
boundary_anomaly = boundary(c) - boundary(a) - boundary(b)
closed_form = a * b * (a + b + a * b / 2)

assert bulk_anomaly == closed_form == F(11, 72)
assert boundary_anomaly == -bulk_anomaly
assert bulk_anomaly + boundary_anomaly == 0

result = {
    "schema": "marici.rh-det3-multiplicative-anomaly.v1",
    "scalar_fixture": {"a": "1/2", "b": "1/3", "composite": "1"},
    "bulk_log_anomaly": "11/72",
    "boundary_log_anomaly": "-11/72",
    "full_determinant_anomaly": "0",
    "general_commuting_bulk_anomaly": "ab(a+b+ab/2)",
    "direct_sum_anomaly": "0",
    "decisive_typing_gate": "orthogonal_prime_blocks_or_source_derived_mixed_boundary_cell",
}

out = Path(__file__).parents[1] / "results" / "rh-det3-multiplicative-anomaly.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
