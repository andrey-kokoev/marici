"""Quantify the cutoff required by the unaccelerated eta-jet tail bound."""
import json
import math
from pathlib import Path

tolerance = 1e-12
cutoffs = {}
for order in range(5):
    low = max(2, math.ceil(math.exp(order)))
    high = low
    while math.log(high) ** order / high >= tolerance:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if math.log(middle) ** order / middle < tolerance:
            high = middle
        else:
            low = middle
    cutoffs[str(order)] = high
assert cutoffs["4"] > 10**18
result = {
    "target_alternating_remainder": tolerance,
    "first_cutoff_below_target_by_derivative_order": cutoffs,
    "fourth_derivative_cutoff_exceeds_1e18": True,
    "conclusion": "direct alternating truncation is rigorous but computationally unusable",
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-naive-tail-cost.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
