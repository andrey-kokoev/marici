"""Exact rational audit of the endpoint's ordinary and shifted Gram signs."""

from fractions import Fraction as F
import json
from pathlib import Path


# Replace exp(t0/4), exp(s/4), exp(u/4) by positive rational factors; only the
# rank-one factorization and generator sign are under audit.
base = F(3, 2)
increments = [F(1), F(5, 4), F(7, 4)]
ordinary = [[base * left * right for right in increments] for left in increments]
shifted = [[-F(1, 4) * value for value in row] for row in ordinary]

assert all(ordinary[i][i] > 0 for i in range(len(increments)))
assert all(shifted[i][i] < 0 for i in range(len(increments)))

# Every 2-by-2 ordinary minor vanishes because the kernel has rank one.
ordinary_minors = []
for i in range(len(increments)):
    for j in range(i + 1, len(increments)):
        minor = ordinary[i][i] * ordinary[j][j] - ordinary[i][j] ** 2
        ordinary_minors.append(minor)
assert all(minor == 0 for minor in ordinary_minors)

result = {
    "endpoint_spectral_value": "-1/4",
    "ordinary_diagonal": [str(ordinary[i][i]) for i in range(len(increments))],
    "ordinary_two_by_two_minors": [str(value) for value in ordinary_minors],
    "ordinary_kernel_positive_semidefinite": True,
    "ordinary_kernel_rank": 1,
    "shifted_diagonal": [str(shifted[i][i]) for i in range(len(increments))],
    "shifted_kernel_positive_semidefinite": False,
    "shifted_kernel_detects_negative_support": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "endpoint-negative-energy-shifted-kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
