from fractions import Fraction
import json
from pathlib import Path


def partial_sums(increments):
    values = [Fraction(0)]
    for increment in increments:
        values.append(values[-1] + increment)
    return values


count = 24
summable = partial_sums([Fraction(1, 2**n) for n in range(1, count + 1)])
oscillatory = partial_sums([Fraction(1 if n % 2 else -1) for n in range(1, count + 1)])
unbounded = partial_sums([Fraction(1) for _ in range(count)])

assert summable[-1] == 1 - Fraction(1, 2**count)
assert set(oscillatory) == {Fraction(0), Fraction(1)}
assert unbounded[-1] == count

# The summable tower has a source-compatible boundary value 1, and its
# remainder tends geometrically to zero.
summable_remainder = [value - 1 for value in summable]
assert abs(summable_remainder[-1]) == Fraction(1, 2**count)

# Bounded oscillation is not Cauchy: adjacent late values remain distance 1.
assert all(abs(oscillatory[n + 1] - oscillatory[n]) == 1 for n in range(count))

result = {
    "schema": "marici.rh.anomaly-boundary-carriers.v1",
    "summable": {
        "product": True,
        "bounded": True,
        "convergent": True,
        "boundary_value": 1,
    },
    "bounded_oscillatory": {
        "product": True,
        "bounded": True,
        "convergent": False,
        "late_adjacent_distance": 1,
    },
    "unbounded": {
        "product": True,
        "bounded": False,
        "convergent": False,
        "cutoff_value": count,
    },
    "verdict": "finite exactness requires a source-authorized boundary realization before completion is meaningful",
}

out = Path(__file__).parents[1] / "results" / "rh-anomaly-boundary-carriers.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
