from fractions import Fraction
import json
from pathlib import Path


q0 = (Fraction(3), Fraction(2), Fraction(0))


def lift(sign, shift):
    return tuple(sign * charge + shift for charge in q0)


def mean(charges):
    return sum(charges) / len(charges)


def centered_moment(charges, degree):
    center = mean(charges)
    return sum((charge - center) ** degree for charge in charges)


positive = lift(1, Fraction(0))
translated = lift(1, Fraction(17, 5))
reflected = lift(-1, Fraction(0))
reflected_translated = lift(-1, Fraction(17, 5))

m1 = centered_moment(positive, 1)
m2 = centered_moment(positive, 2)
m3 = centered_moment(positive, 3)

assert m1 == 0
assert m2 == Fraction(14, 3)
assert m3 == Fraction(-20, 9)

assert centered_moment(translated, 2) == m2
assert centered_moment(translated, 3) == m3
assert centered_moment(reflected, 2) == m2
assert centered_moment(reflected, 3) == -m3
assert centered_moment(reflected_translated, 3) == -m3

# Mean and signed cubic jointly recover the affine lift when the distance
# geometry has already fixed the base configuration q0.
target_mean = mean(positive)
target_cubic = m3
candidate_signs = (-1, 1)
solutions = []
for sign in candidate_signs:
    base_mean = mean(lift(sign, Fraction(0)))
    shift = target_mean - base_mean
    candidate = lift(sign, shift)
    if centered_moment(candidate, 3) == target_cubic:
        solutions.append((sign, shift, candidate))
assert solutions == [(1, Fraction(0), positive)]

result = {
    "schema": "marici.nima.flavor-centered-charge-moments.v1",
    "centered_linear_moment": str(m1),
    "centered_quadratic_moment": str(m2),
    "centered_cubic_moment": str(m3),
    "quadratic_translation_invariant": True,
    "quadratic_reflection_even": True,
    "cubic_translation_invariant": True,
    "cubic_reflection_odd": True,
    "mean_plus_signed_cubic_unique_lifts": len(solutions),
    "verdict": (
        "For the three-charge affine family, the centered linear moment "
        "vanishes and the centered quadratic is reflection-even. The centered "
        "cubic is the first translation-free signed moment; together with the "
        "mean it reconstructs the affine lift fixed by the hierarchy geometry."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-centered-charge-moments.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
