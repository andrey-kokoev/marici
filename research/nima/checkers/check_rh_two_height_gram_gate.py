from fractions import Fraction
import json
from pathlib import Path


def determinant_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


good = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
]
bad = [
    [Fraction(1), Fraction(2)],
    [Fraction(2), Fraction(1)],
]

assert [good[0][0], good[1][1]] == [bad[0][0], bad[1][1]]
assert all(value > 0 for value in [good[0][0], good[1][1]])
assert all(value > 0 for value in [bad[0][0], bad[1][1]])
assert determinant_2(good) > 0
assert determinant_2(bad) < 0

# Exact collapsing family: every finite Gramian is positive, but no uniform
# lower bound survives.
collapsing_determinants = []
for cutoff in range(1, 9):
    epsilon = Fraction(1, cutoff)
    gram = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), epsilon * epsilon],
    ]
    determinant = determinant_2(gram)
    assert determinant > 0
    collapsing_determinants.append(str(determinant))

result = {
    "good_diagonal": ["1", "1"],
    "bad_diagonal": ["1", "1"],
    "good_determinant": str(determinant_2(good)),
    "bad_determinant": str(determinant_2(bad)),
    "positive_one_height_energy_implies_positive_two_height_kernel": False,
    "collapsing_positive_determinants": collapsing_determinants,
    "finite_kernel_positivity_implies_uniform_completion_strictness": False,
    "required_test": "typed mixed-height lurking-isometry residual",
    "verdict": "the Clark diagonal energy cannot authorize a conservative colligation before mixed-height polarization is verified",
}

out = Path(__file__).parents[1] / "results" / "rh-two-height-gram-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
