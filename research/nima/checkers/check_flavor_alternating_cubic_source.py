from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


def parity(perm):
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def determinant_port(u, v, w):
    return sum(
        Fraction(parity(perm)) * u[perm[0]] * v[perm[1]] * w[perm[2]]
        for perm in permutations(range(3))
    )


def transform(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


e1 = (Fraction(1), Fraction(0), Fraction(0))
e2 = (Fraction(0), Fraction(1), Fraction(0))
e3 = (Fraction(0), Fraction(0), Fraction(1))
x = (Fraction(2), Fraction(-3), Fraction(5))
y = (Fraction(7), Fraction(1), Fraction(-2))

assert determinant_port(x, x, x) == 0
assert determinant_port(x, y, y) == 0
assert determinant_port(x, x, y) == 0
assert determinant_port(e1, e2, e3) == 1
assert determinant_port(e2, e1, e3) == -1

cycle = (
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
)
reflection = (
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 1),
)

frame = (e1, e2, e3)
cycled_frame = tuple(transform(cycle, vector) for vector in frame)
reflected_frame = tuple(transform(reflection, vector) for vector in frame)
assert determinant_port(*cycled_frame) == 1
assert determinant_port(*reflected_frame) == -1

# On the orthonormal-frame locus, a real source coefficient epsilon selects
# one of the two orientations by the energy -epsilon det.
epsilon = Fraction(1, 5)
positive_orientation_energy = -epsilon * determinant_port(*frame)
negative_orientation_energy = -epsilon * determinant_port(*reflected_frame)
assert positive_orientation_energy < negative_orientation_energy

result = {
    "schema": "marici.nima.flavor-alternating-cubic-source.v1",
    "one_commuting_triplet_cubic": str(determinant_port(x, x, x)),
    "two_triplets_with_repetition_cubic": str(determinant_port(x, y, y)),
    "three_typed_basis_triplets_cubic": str(determinant_port(e1, e2, e3)),
    "cyclic_transform_preserves_carrier": True,
    "reflection_flips_carrier": True,
    "real_positive_coefficient_selects_positive_orientation_on_frame_locus": True,
    "minimum_independent_vector_ports": 3,
    "verdict": (
        "The alternating Flavor carrier vanishes for one commuting triplet or "
        "two triplets with repetition. Its first nonzero realization requires "
        "three independently typed vector ports, or three source-distinct jets."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-alternating-cubic-source.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
