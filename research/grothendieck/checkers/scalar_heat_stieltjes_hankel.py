"""Exact rational audit of the first scalar Stieltjes Hankel identities."""

from fractions import Fraction as F
import json
from pathlib import Path


# Rational positive weights stand for e^(-t lambda)dmu at one fixed time.
atoms = [(F(1, 2), F(1)), (F(1, 3), F(4)), (F(1, 5), F(9))]


def D(k):
    return sum(weight * spectral_value**k for weight, spectral_value in atoms)


moments = [D(k) for k in range(5)]
determinant_0 = moments[0] * moments[2] - moments[1] ** 2
determinant_1 = moments[1] * moments[3] - moments[2] ** 2
pair_formula_0 = sum(
    atoms[i][0] * atoms[j][0] * (atoms[i][1] - atoms[j][1]) ** 2
    for i in range(len(atoms))
    for j in range(i + 1, len(atoms))
)
pair_formula_1 = sum(
    atoms[i][0]
    * atoms[j][0]
    * atoms[i][1]
    * atoms[j][1]
    * (atoms[i][1] - atoms[j][1]) ** 2
    for i in range(len(atoms))
    for j in range(i + 1, len(atoms))
)
assert determinant_0 == pair_formula_0 > 0
assert determinant_1 == pair_formula_1 > 0

variance = moments[2] / moments[0] - (moments[1] / moments[0]) ** 2
effective_energy_derivative = -variance
assert variance == determinant_0 / moments[0] ** 2
assert effective_energy_derivative < 0

hostile = [F(1), F(1), F(1, 2)]
hostile_determinant = hostile[0] * hostile[2] - hostile[1] ** 2
assert all(value > 0 for value in hostile)
assert hostile_determinant < 0

result = {
    "spectral_atom_count": len(atoms),
    "D0_through_D4": [str(value) for value in moments],
    "ordinary_order_one_determinant": str(determinant_0),
    "shifted_order_one_determinant": str(determinant_1),
    "pairwise_variance_formula_verified": True,
    "effective_energy_derivative": str(effective_energy_derivative),
    "hostile_positive_entries": [str(value) for value in hostile],
    "hostile_Hankel_determinant": str(hostile_determinant),
    "entrywise_positivity_is_enough": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "scalar-heat-stieltjes-hankel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
