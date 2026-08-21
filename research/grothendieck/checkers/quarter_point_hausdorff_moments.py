"""Exact rational audit of the quarter-point compact moment transformation."""

from fractions import Fraction as F
import json
from pathlib import Path


x0 = F(1, 4)
# Positive squared spectral values and residues.
spectral_atoms = [(F(2), F(3, 4)), (F(1), F(15, 4)), (F(3), F(35, 4))]

# Push dnu to dmu=u*dnu, where u=1/(x0+lambda).
hausdorff_atoms = []
for residue, spectral_value in spectral_atoms:
    u = 1 / (x0 + spectral_value)
    weight = u * residue
    hausdorff_atoms.append((weight, u))
    assert 0 < u <= 4


def A(k):
    return sum(weight * u**k for weight, u in hausdorff_atoms)


moments = [A(k) for k in range(6)]


def two_by_two_determinant(entries):
    return entries[0] * entries[2] - entries[1] ** 2


ordinary_det = two_by_two_determinant(moments[0:3])
lower_localizer = [moments[k + 1] for k in range(3)]
upper_localizer = [4 * moments[k] - moments[k + 1] for k in range(3)]
lower_det = two_by_two_determinant(lower_localizer)
upper_det = two_by_two_determinant(upper_localizer)
assert ordinary_det > 0
assert lower_det > 0
assert upper_det > 0

# Direct resolvent derivatives agree with the transformed compact moments.
direct = [
    sum(residue / (x0 + spectral_value) ** (k + 1) for residue, spectral_value in spectral_atoms)
    for k in range(6)
]
assert moments == direct

result = {
    "quarter_point": str(x0),
    "compact_support_bound": "4",
    "hausdorff_atoms": [[str(weight), str(u)] for weight, u in hausdorff_atoms],
    "A0_through_A5": [str(value) for value in moments],
    "ordinary_order_one_determinant": str(ordinary_det),
    "lower_localizer_determinant": str(lower_det),
    "upper_localizer_determinant": str(upper_det),
    "all_three_order_one_tests_positive": True,
    "direct_resolvent_jet_matches_compact_moments": True,
    "compact_moment_problem_determinate": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "quarter-point-hausdorff-moments.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
