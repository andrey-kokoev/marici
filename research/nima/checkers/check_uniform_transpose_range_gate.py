from fractions import Fraction
import json
from pathlib import Path


def least_norm_cost_squared(diagonal, target):
    solution = [Fraction(target[i], diagonal[i]) for i in range(len(diagonal))]
    return sum(value * value for value in solution), solution


stable = []
hostile = []
for n in range(1, 13):
    target = [Fraction(0) for _ in range(n)]
    target[-1] = Fraction(1)

    stable_cost, stable_solution = least_norm_cost_squared(
        [Fraction(1) for _ in range(n)], target
    )
    hostile_cost, hostile_solution = least_norm_cost_squared(
        [Fraction(1) for _ in range(n - 1)] + [Fraction(1, n)], target
    )

    assert stable_cost == 1
    assert hostile_cost == n * n
    assert stable_solution[-1] == 1
    assert hostile_solution[-1] == n
    stable.append(stable_cost)
    hostile.append(hostile_cost)

assert hostile == [n * n for n in range(1, 13)]

result = {
    "schema": "marici.nima.uniform-transpose-range-gate.v1",
    "cutoffs": list(range(1, 13)),
    "stable_minimum_cost_squared": [int(value) for value in stable],
    "hostile_minimum_cost_squared": [int(value) for value in hostile],
    "finite_solvability": True,
    "hostile_uniform_bound": False,
    "verdict": "boundary provenance requires uniformly bounded transpose interpolation",
}

out = Path(__file__).parents[1] / "results" / "uniform-transpose-range-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

