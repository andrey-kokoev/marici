import json
import math


alpha = 0.49
legal_rate = 0.5
hostile_rate = 0.25
samples = [0, 10, 20, 40]


def weighted_value(rate, x):
    return math.exp((alpha - rate) * abs(x))


legal = [weighted_value(legal_rate, x) for x in samples]
hostile = [weighted_value(hostile_rate, x) for x in samples]

assert all(x <= 1.0 for x in legal)
assert all(hostile[i + 1] > hostile[i] for i in range(len(hostile) - 1))
assert hostile[-1] > 1000.0

# Pointwise products add rates and therefore preserve the legal threshold.
product_rate = legal_rate + legal_rate
product = [weighted_value(product_rate, x) for x in samples]
assert all(x <= 1.0 for x in product)

result = {
    "schema": "marici.nima.half-offset-residual-gap.v1",
    "alpha": alpha,
    "legal_rate": legal_rate,
    "hostile_rate": hostile_rate,
    "legal_weighted_samples_bounded": True,
    "hostile_weighted_samples_strictly_grow": True,
    "hostile_last_sample": hostile[-1],
    "product_preserves_threshold": True,
    "unweighted_completion_sufficient": False,
}
print(json.dumps(result, indent=2, sort_keys=True))

