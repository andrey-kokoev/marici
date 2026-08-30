from fractions import Fraction
import json
from pathlib import Path


def cycle_sum(edges):
    return tuple(sum((edge[i] for edge in edges), Fraction(0)) for i in range(2))


def transitions(potentials):
    return [
        tuple(potentials[(i + 1) % len(potentials)][d] - potentials[i][d] for d in range(2))
        for i in range(len(potentials))
    ]


good_potentials = [
    (Fraction(0), Fraction(0)),
    (Fraction(2), Fraction(-1)),
    (Fraction(5), Fraction(3)),
]
good_edges = transitions(good_potentials)
assert cycle_sum(good_edges) == (0, 0)

hostile_degree_one = [(Fraction(1), Fraction(0)), (Fraction(1), Fraction(0)), (Fraction(-1), Fraction(0))]
hostile_degree_two = [(Fraction(0), Fraction(2)), (Fraction(0), Fraction(-3)), (Fraction(0), Fraction(2))]
assert cycle_sum(hostile_degree_one) == (1, 0)
assert cycle_sum(hostile_degree_two) == (0, 1)

# Reciprocal-looking cancellation on one paired edge does not kill a third
# completion edge.
reciprocal_pair_plus_completion = [
    (Fraction(3), Fraction(-2)),
    (Fraction(-3), Fraction(2)),
    (Fraction(1), Fraction(1)),
]
assert cycle_sum(reciprocal_pair_plus_completion) == (1, 1)

result = {
    "schema": "marici.rh.anomaly-frame-descent.v1",
    "good_cycle_sum": list(map(int, cycle_sum(good_edges))),
    "hostile_degree_one_cycle_sum": list(map(int, cycle_sum(hostile_degree_one))),
    "hostile_degree_two_cycle_sum": list(map(int, cycle_sum(hostile_degree_two))),
    "reciprocal_pair_completion_cycle_sum": list(map(int, cycle_sum(reciprocal_pair_plus_completion))),
    "verdict": "global scalar frame requires two source-typed anomaly cocycles to be coboundaries",
}

out = Path(__file__).parents[1] / "results" / "rh-anomaly-frame-descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
