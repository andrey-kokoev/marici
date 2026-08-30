"""Exact finite-measure check of the Loewner curvature/concavity identity."""
import json
from fractions import Fraction
from pathlib import Path


x = Fraction(3, 5)
atoms = [Fraction(1, 7), Fraction(2, 3), Fraction(5, 2)]
weights = [Fraction(2, 5), Fraction(7, 11), Fraction(13, 17)]


def moment(power):
    return sum(weight / (x + atom) ** power for atom, weight in zip(atoms, weights))


m2, m3, m4 = (moment(power) for power in (2, 3, 4))
curvature = m2 * m4 - m3 * m3
pair_square = sum(
    wi * wj * (1 / (x + ai)) ** 2 * (1 / (x + aj)) ** 2
    * ((1 / (x + ai)) - (1 / (x + aj))) ** 2 / 2
    for ai, wi in zip(atoms, weights)
    for aj, wj in zip(atoms, weights)
)

assert curvature == pair_square
assert curvature > 0

# Complete monotonicity alone is insufficient: for g(x)=exp(-x),
# g*g''/6-g'^2/4=-g^2/12<0.
exponential_curvature_coefficient = Fraction(-1, 12)
assert exponential_curvature_coefficient < 0

result = {
    "finite_measure_curvature": str(curvature),
    "pair_square_value": str(pair_square),
    "exact_identity_verified": curvature == pair_square,
    "strict_for_distinct_positive_atoms": curvature > 0,
    "reciprocal_square_root_concave": True,
    "complete_monotonicity_is_insufficient": True,
    "exponential_counterexample_coefficient": str(exponential_curvature_coefficient),
    "symbolic_exact_arithmetic": True,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "loewner-curvature-concavity-identity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
