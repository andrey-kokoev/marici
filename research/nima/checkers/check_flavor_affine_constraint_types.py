from fractions import Fraction
import json
from pathlib import Path


q0 = (Fraction(3), Fraction(2), Fraction(0))


def lift(sign, shift):
    return tuple(sign * charge + shift for charge in q0)


def linear(coefficients, charges):
    return sum(a * q for a, q in zip(coefficients, charges))


# Translation-sensitive origin observer: total charge equals five.
origin_coefficients = (Fraction(1), Fraction(1), Fraction(1))
origin_target = Fraction(5)
origin_solutions = {}
for sign in (-1, 1):
    coefficient_sum = sum(origin_coefficients)
    signed_base = linear(origin_coefficients, tuple(sign * q for q in q0))
    shift = (origin_target - signed_base) / coefficient_sum
    origin_solutions[sign] = shift
    assert linear(origin_coefficients, lift(sign, shift)) == origin_target

assert origin_solutions[1] == 0
assert origin_solutions[-1] == Fraction(10, 3)

# Charge-lattice typing removes the reflected rational lift, but this is an
# extra assumption rather than a consequence of the sum equation.
integer_origin_solutions = {
    sign: shift
    for sign, shift in origin_solutions.items()
    if shift.denominator == 1
}
assert integer_origin_solutions == {1: Fraction(0)}

# Translation-invariant orientation observer: q1-q2 equals one.
orientation_coefficients = (Fraction(1), Fraction(-1), Fraction(0))
orientation_target = Fraction(1)
assert sum(orientation_coefficients) == 0
assert linear(orientation_coefficients, lift(1, Fraction(17, 5))) == orientation_target
assert linear(orientation_coefficients, lift(-1, Fraction(17, 5))) == -orientation_target

# Combining the two observer types fixes sign and shift without relying on
# lattice integrality.
combined_solutions = tuple(
    (sign, shift)
    for sign, shift in origin_solutions.items()
    if linear(orientation_coefficients, lift(sign, shift)) == orientation_target
)
assert combined_solutions == ((1, Fraction(0)),)

result = {
    "schema": "marici.nima.flavor-affine-constraint-types.v1",
    "origin_observer_coefficient_sum": str(sum(origin_coefficients)),
    "rational_origin_solutions": {
        str(sign): str(shift) for sign, shift in sorted(origin_solutions.items())
    },
    "integer_lattice_origin_solutions": {
        str(sign): str(shift) for sign, shift in sorted(integer_origin_solutions.items())
    },
    "orientation_observer_coefficient_sum": str(sum(orientation_coefficients)),
    "orientation_observer_translation_invariant": True,
    "combined_rational_solutions": [
        {"sign": sign, "shift": str(shift)} for sign, shift in combined_solutions
    ],
    "verdict": (
        "Origin and orientation are different affine observability directions. "
        "One translation-sensitive equation fixes a shift on each reflected "
        "sheet; one translation-invariant signed equation fixes the sheet. "
        "Their combination fixes the rational lift. Integer uniqueness from "
        "the first equation alone additionally assumes charge quantization."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-affine-constraint-types.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
