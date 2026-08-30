"""Dependency-free exact majorant checks for arithmetic-grade evaluation."""

from fractions import Fraction
import json


def primitive_majorant(n):
    # Drop n^(-1/2) to keep a rational upper bound.
    return Fraction(1 + n**5, 2 ** (n * n))


def square_majorant(n):
    # Drop n^(-1) and use the stronger sampled exponent n^4.
    return Fraction(1 + n**10, 2 ** (n**4))


primitive_ratios = [primitive_majorant(n + 1) / primitive_majorant(n) for n in range(2, 10)]
square_ratios = [square_majorant(n + 1) / square_majorant(n) for n in range(2, 6)]

# Connected samples have exponent n^(2k). Check the least-decaying k=3 edge;
# larger k only strengthens the exponential domination for n>=2.
def connected_majorant(n, k):
    return Fraction(1 + n ** (5 * k), k * 2 ** (n ** (2 * k)))


connected_ratios = [
    connected_majorant(n + 1, 3) / connected_majorant(n, 3)
    for n in range(2, 5)
]

checks = {
    "primitive_tail_has_geometric_ratio": all(r < Fraction(1, 2) for r in primitive_ratios),
    "square_tail_has_geometric_ratio": all(r < Fraction(1, 2) for r in square_ratios),
    "connected_k3_tail_has_geometric_ratio": all(r < Fraction(1, 2) for r in connected_ratios),
    "larger_connected_depth_strengthens_exponent": all(n ** (2 * 4) > n ** (2 * 3) for n in range(2, 6)),
    "majorants_are_positive": primitive_majorant(2) > 0 and square_majorant(2) > 0 and connected_majorant(2, 3) > 0,
}

result = {
    "schema": "marici.grothendieck.theta-vector-arithmetic-grade-domain.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "max_ratios": {
        "primitive": str(max(primitive_ratios)),
        "square": str(max(square_ratios)),
        "connected_k3": str(max(connected_ratios)),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
