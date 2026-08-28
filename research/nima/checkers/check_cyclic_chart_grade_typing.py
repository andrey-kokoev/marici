from fractions import Fraction
import json
from pathlib import Path


def cyclic_grade(diagonal, grade):
    return sum(value ** grade for value in diagonal) / grade


left = [Fraction(1), Fraction(1)]
right = [Fraction(0), Fraction(2)]

assert cyclic_grade(left, 1) == cyclic_grade(right, 1) == 2
assert cyclic_grade(left, 2) == 1
assert cyclic_grade(right, 2) == 2

direct_sum_checks = []
for grade in range(1, 9):
    a = [Fraction(1, 2), Fraction(2, 3)]
    b = [Fraction(3, 5), Fraction(5, 7), Fraction(7, 11)]
    combined = cyclic_grade(a + b, grade)
    separated = cyclic_grade(a, grade) + cyclic_grade(b, grade)
    assert combined == separated
    direct_sum_checks.append(grade)

# Formal coefficients of -log(1-x), truncated at grade six.
determinant_coefficients = [Fraction(1, grade) for grade in range(1, 7)]
duplicated = determinant_coefficients[:]
duplicated[0] += Fraction(1)
duplicated[1] += Fraction(1, 2)
assert determinant_coefficients[:2] == [Fraction(1), Fraction(1, 2)]
assert duplicated[:2] == [Fraction(2), Fraction(1)]

result = {
    "schema": "marici.nima.cyclic-chart-grade-typing.v1",
    "equal_primitive_trace": 2,
    "left_square_grade": 1,
    "right_square_grade": 2,
    "square_descends_from_primitive_scalar": False,
    "direct_sum_additivity_verified_through_grade": max(direct_sum_checks),
    "determinant_first_two_coefficients": ["1", "1/2"],
    "double_counted_first_two_coefficients": ["2", "1"],
    "verdict": "primitive and square are distinct cyclic chart grades, not additive seam rows",
}

out = Path(__file__).parents[1] / "results" / "cyclic-chart-grade-typing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
