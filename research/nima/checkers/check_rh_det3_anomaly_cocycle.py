from fractions import Fraction as F
import json
from pathlib import Path


def compose(a, b):
    return a + b + a * b


def counterterm(x):
    return -x + x * x / 2


def anomaly(a, b):
    return counterterm(compose(a, b)) - counterterm(a) - counterterm(b)


a, b, d = F(1, 2), F(1, 3), F(1, 4)
ab, bd = compose(a, b), compose(b, d)
left = anomaly(a, b) + anomaly(ab, d)
right = anomaly(b, d) + anomaly(a, bd)

assert compose(ab, d) == compose(a, bd)
assert left == right

result = {
    "schema": "marici.rh-det3-anomaly-cocycle.v1",
    "fixture": {"a": "1/2", "b": "1/3", "d": "1/4"},
    "alpha_a_b": str(anomaly(a, b)),
    "alpha_ab_d": str(anomaly(ab, d)),
    "alpha_b_d": str(anomaly(b, d)),
    "alpha_a_bd": str(anomaly(a, bd)),
    "left_total": str(left),
    "right_total": str(right),
    "cocycle_residual": "0",
    "classification": "exact_2_cocycle_generated_by_low_order_counterterm",
}

out = Path(__file__).parents[1] / "results" / "rh-det3-anomaly-cocycle.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
