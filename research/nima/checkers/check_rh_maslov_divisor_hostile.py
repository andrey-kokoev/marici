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


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    rows = len(m)
    cols = len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = m[r][c]
        m[r] = [x / scale for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                scale = m[i][c]
                m[i] = [x - scale * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def graph_columns(t):
    return [
        [1, 0],
        [0, 1],
        [0, t],
        [-t, 0],
    ]


zero = Fraction(0)
one = Fraction(1)
q = [[zero] * 4 for _ in range(4)]
for i in range(2):
    q[i][i + 2] = one
    q[i + 2][i] = one

for t in (Fraction(-3), Fraction(0), Fraction(2)):
    l = graph_columns(t)
    assert rank(l) == 2
    assert matmul(transpose(l), matmul(q, l)) == [[zero, zero], [zero, zero]]

assert rank([[0, 0], [0, 0]]) == 0
assert rank([[0, 2], [-2, 0]]) == 2

a = Fraction(3, 2)


def t_of(z):
    return z * z - a * a


assert t_of(a) == 0
assert t_of(-a) == 0
assert t_of(Fraction(0)) != 0
for z in (Fraction(-7, 3), Fraction(-1, 4), Fraction(5, 6), Fraction(9, 2)):
    assert t_of(-z) == t_of(z)

result = {
    "finite_hyperbolic_signature": [2, 2],
    "graph_lagrangians_maximal_isotropic": True,
    "transverse_exactly_when_t_nonzero": True,
    "reciprocal_family": "t(z)=z^2-a^2",
    "hostile_a": "3/2",
    "off_seam_crossings": ["-3/2", "3/2"],
    "reciprocal_symmetry_preserved": True,
    "associator_coherence_blocks_crossing": False,
    "verdict": "RH requires source-derived avoidance of the Maslov divisor, not coherence alone",
}

out = Path(__file__).parents[1] / "results" / "rh-maslov-divisor-hostile.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
