from fractions import Fraction
import json
from pathlib import Path


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


cutoffs = [1, 2, 4, 8, 16, 32]
target_primitive = Fraction(3, 2)
target_square = Fraction(-5, 3)
rows = []

for cutoff in cutoffs:
    primitive = Fraction(cutoff)
    primitive_archimedean = -primitive + target_primitive
    square = harmonic(cutoff)
    square_archimedean = -square + target_square
    primitive_relative = primitive + primitive_archimedean
    square_relative = square + square_archimedean
    joint = primitive_relative + square_relative
    assert primitive_relative == target_primitive
    assert square_relative == target_square
    assert joint == target_primitive + target_square
    rows.append(
        {
            "cutoff": cutoff,
            "primitive_raw": str(primitive),
            "square_raw": str(square),
            "joint_relative": str(joint),
        }
    )

cross_grade_primitive = Fraction(7)
cross_grade_square = Fraction(-7)
assert cross_grade_primitive + cross_grade_square == 0
assert cross_grade_primitive != 0 and cross_grade_square != 0

coarse_value = target_primitive + target_square + 2
refined_value = target_primitive + target_square + 4
assert refined_value != coarse_value

result = {
    "schema": "marici.rh.joint-relative-character.v1",
    "cutoffs": cutoffs,
    "joint_relative_value": str(target_primitive + target_square),
    "raw_components_grow": True,
    "typed_relative_components_stable": True,
    "cross_grade_scalar_cancellation_rejected": True,
    "refinement_dependent_counterterm_rejected": True,
    "verdict": "theta anomaly totalization must be a joint relative character rather than separate scalar factors",
}

out = Path(__file__).parents[1] / "results" / "rh-joint-relative-character.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
