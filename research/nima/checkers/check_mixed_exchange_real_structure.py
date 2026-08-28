import json
from fractions import Fraction
from pathlib import Path


def mul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def conj(z):
    return (z[0], -z[1])


def norm2(z):
    return mul(z, conj(z))[0]


def k(c, z):
    return mul(c, conj(z))


unit_samples = [
    (Fraction(1), Fraction(0)),
    (Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(1)),
    (Fraction(3, 5), Fraction(4, 5)),
]

fixed_vectors = []
for c in unit_samples:
    trial = (Fraction(0), Fraction(1)) if c == (Fraction(-1), Fraction(0)) else (
        Fraction(1) + c[0], c[1]
    )
    assert trial != (0, 0)
    assert k(c, trial) == trial
    assert k(c, k(c, trial)) == trial
    fixed_vectors.append(trial)

hostile_c = (Fraction(2), Fraction(0))
hostile_z = (Fraction(3), Fraction(1))
assert k(hostile_c, k(hostile_c, hostile_z)) == (
    4 * hostile_z[0], 4 * hostile_z[1]
)
assert norm2(hostile_c) == 4

# A nonzero fixed vector would force equal norms on z and c conjugate(z),
# hence norm2(c)=1. The hostile coefficient violates that necessary condition.
assert norm2(hostile_c) != 1

result = {
    "schema": "marici.mixed-exchange-real-structure.v1",
    "coherence_scalar": "norm_squared_of_c",
    "real_structure_condition": "norm_squared_of_c_equals_one",
    "unit_fixed_vectors": [
        [str(a), str(b)] for a, b in fixed_vectors
    ],
    "hostile": {
        "c": ["2", "0"],
        "square_scalar": 4,
        "nonzero_fixed_vector_possible": False,
    },
    "verdict": "two invertible exchanges need a trivial mixed square before they define a Real line",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "mixed-exchange-real-structure.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
