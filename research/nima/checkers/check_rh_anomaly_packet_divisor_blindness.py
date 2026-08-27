from fractions import Fraction as F
import json
from pathlib import Path


def compose(a, b):
    return a + b + a * b


def counterterm(x):
    return -x + x * x / 2


def anomaly(a, b):
    return counterterm(compose(a, b)) - counterterm(a) - counterterm(b)


a, b = F(1, 2), F(1, 3)
packet_anomaly = anomaly(a, b)

# Endpoint sections are represented by coefficient tuples in ascending order.
baseline = (F(1),)
hostile = (F(1), F(0), F(-1))  # 1-z^2

def evaluate(poly, z):
    return sum(coef * z**i for i, coef in enumerate(poly))


assert packet_anomaly == F(11, 72)
assert evaluate(hostile, F(1)) == 0
assert evaluate(hostile, F(-1)) == 0
assert all(evaluate(hostile, z) == evaluate(hostile, -z) for z in (F(0), F(1, 2), F(2)))
assert all(evaluate(baseline, z) != 0 for z in (F(-1), F(0), F(1)))

result = {
    "schema": "marici.rh-anomaly-packet-divisor-blindness.v1",
    "shared_det3_anomaly": "11/72",
    "baseline_endpoint": "1",
    "hostile_endpoint": "1-z^2",
    "hostile_preserves_reflection_symmetry": True,
    "hostile_off_seam_zeros": ["-1", "1"],
    "anomaly_packet_distinguishes_endpoints": False,
    "missing_constructor": "source_derived_boundary_normal_form_to_endpoint_section_map",
}

out = Path(__file__).parents[1] / "results" / "rh-anomaly-packet-divisor-blindness.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
