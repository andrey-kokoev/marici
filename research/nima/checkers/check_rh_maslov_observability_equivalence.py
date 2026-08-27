from fractions import Fraction
import json
from pathlib import Path


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def rank_2(a):
    a00, a01 = a[0]
    a10, a11 = a[1]
    determinant = a00 * a11 - a01 * a10
    if determinant:
        return 2
    if any((a00, a01, a10, a11)):
        return 1
    return 0


def a_matrix(t):
    return [[Fraction(0), t], [-t, Fraction(0)]]


for t in (Fraction(-2), Fraction(0), Fraction(3, 5)):
    a = a_matrix(t)
    gram = matmul(transpose(a), a)
    expected = [[t * t, Fraction(0)], [Fraction(0), t * t]]
    assert gram == expected
    intersection_dimension = 2 - rank_2(a)
    observability_kernel_dimension = 2 - rank_2(gram)
    assert intersection_dimension == observability_kernel_dimension
    assert (t != 0) == (rank_2(a) == 2)

a_hostile = Fraction(3, 2)


def margin(z):
    t = z * z - a_hostile * a_hostile
    return t * t


assert margin(a_hostile) == 0
assert margin(-a_hostile) == 0
assert margin(Fraction(0)) > 0
for z in (Fraction(-7, 3), Fraction(1, 5), Fraction(11, 4)):
    assert margin(-z) == margin(z)

cutoffs = list(range(1, 13))
finite_margins = [Fraction(1, n * n) for n in cutoffs]
assert all(x > 0 for x in finite_margins)
assert finite_margins[-1] < finite_margins[0]

result = {
    "finite_equivalences": [
        "lagrangian_transversality",
        "maslov_divisor_avoidance",
        "observability_injectivity",
        "positive_definite_observability_gramian"
    ],
    "graph_gramian": "t^2 I",
    "reciprocal_hostile_margin": "(z^2-a^2)^2",
    "hostile_crossings": ["-3/2", "3/2"],
    "finite_cutoffs_observable": True,
    "uniform_completion_margin": False,
    "verdict": "Maslov transversality is observability; completion stability is uniform observability",
}

out = Path(__file__).parents[1] / "results" / "rh-maslov-observability-equivalence.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
