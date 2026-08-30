from fractions import Fraction
import json
from pathlib import Path


def identity():
    return [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(value, a):
    return [[value * x for x in row] for row in a]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def product(*matrices):
    out = identity()
    for matrix in matrices:
        out = matmul(out, matrix)
    return out


def elementary(i, j):
    out = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    out[i][j] = Fraction(1)
    return out


def unipotent(generator, value):
    return add(identity(), scale(value, generator))


e21 = elementary(1, 0)
e12 = elementary(0, 1)
e13 = elementary(0, 2)
e23 = elementary(1, 2)

r = [
    [Fraction(0), Fraction(-1), Fraction(0)],
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
]
r_inverse = [
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(-1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
]

assert product(r, e21, r_inverse) == scale(Fraction(-1), e12)
assert matmul(e21, e13) == e23
assert matmul(e13, e21) == scale(Fraction(0), e23)

for a in [Fraction(2), Fraction(-3), Fraction(5, 2)]:
    derived_x1 = product(r, unipotent(e21, -a), r_inverse)
    assert derived_x1 == unipotent(e12, a)

commutator_samples = [
    (Fraction(2), Fraction(3)),
    (Fraction(-4), Fraction(5, 2)),
    (Fraction(7, 3), Fraction(-2, 5)),
]

for a, b in commutator_samples:
    derived_x2 = product(
        unipotent(e21, a),
        unipotent(e13, b),
        unipotent(e21, -a),
        unipotent(e13, -b),
    )
    assert derived_x2 == unipotent(e23, a * b)

braid_samples = [
    (Fraction(2), Fraction(3), Fraction(5)),
    (Fraction(-2), Fraction(7), Fraction(5)),
    (Fraction(3, 2), Fraction(-4, 3), Fraction(5, 4)),
]

for a, b, c in braid_samples:
    assert a + c != 0
    left = product(
        unipotent(e12, a),
        unipotent(e23, b),
        unipotent(e12, c),
    )
    right = product(
        unipotent(e23, b * c / (a + c)),
        unipotent(e12, a + c),
        unipotent(e23, a * b / (a + c)),
    )
    assert left == right

result = {
    "first_root_source_word": "Fourier conjugate of inverse jet shear",
    "second_root_source_word": "group commutator of jet shear and forward wall extension",
    "derived_first_root": "E12",
    "derived_second_root": "E23",
    "commutator_samples": len(commutator_samples),
    "braid_samples": len(braid_samples),
    "dual_wall_required_for_positive_borel": False,
    "dual_wall_required_for_full_sl3": True,
    "finite_source_braid_generated": True,
    "analytic_common_domain_verified": False,
    "verdict": "the finite A2 braid is source-generated; its rigged-domain lift is the remaining coherencer",
}

out = Path(__file__).parents[1] / "results" / "rh-positive-a2-source-generation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
