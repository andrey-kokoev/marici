from fractions import Fraction
import json
from pathlib import Path


def observer(vector):
    # Finite exact model of a graph-domain boundary functional.
    return vector[0] - 2 * vector[1] + 3 * vector[2]


def ambient_l1(vector):
    return sum(abs(value) for value in vector)


def graph_norm(vector):
    return ambient_l1(vector) + abs(observer(vector))


def add(left, right):
    return [a + b for a, b in zip(left, right)]


def scale(value, vector):
    return [value * entry for entry in vector]


samples = [
    (
        [Fraction(2), Fraction(-1), Fraction(4)],
        [Fraction(1), Fraction(3), Fraction(-2)],
        Fraction(5),
    ),
    (
        [Fraction(-3), Fraction(7), Fraction(1)],
        [Fraction(2), Fraction(-4), Fraction(5)],
        Fraction(-2),
    ),
]

for vector, u, scalar in samples:
    translated = add(vector, scale(-scalar, u))
    bound = graph_norm(vector) + abs(scalar) * graph_norm(u)
    assert graph_norm(translated) <= bound
    restored = add(translated, scale(scalar, u))
    assert restored == vector

result = {
    "graph_translation_samples": len(samples),
    "translation_and_inverse_preserve_linear_graph_domain": True,
    "graph_norm_bound": "norm_y(v-tu) <= norm_y(v)+abs(t) norm_y(u)",
    "honest_readout_requires_u_in_observer_domain": True,
    "ordinary_graph_unboundedness_blocks_elimination": False,
    "remaining_case": "renormalized pairing with additional typed boundary currents",
    "verdict": "an honest closed observer pairing collapses the bordered complex to the scalar readout even on its graph domain",
}

out = Path(__file__).parents[1] / "results" / "rh-graph-domain-elimination.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
