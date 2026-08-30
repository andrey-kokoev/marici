"""Exact collision of primitive-square data with different factor divisors."""

from fractions import Fraction
import json


X = (Fraction(1), Fraction(2), Fraction(3))
Y = (Fraction(17, 7), Fraction(6, 7), Fraction(19, 7))


def power_sum(values, grade):
    return sum((value**grade for value in values), Fraction(0))


def connected_grade(values, grade):
    return Fraction((-1) ** (grade + 1), grade) * power_sum(values, grade)


x_grades = tuple(connected_grade(X, k) for k in range(1, 4))
y_grades = tuple(connected_grade(Y, k) for k in range(1, 4))

checks = {
    "all_factors_positive": all(value > 0 for value in X + Y),
    "primitive_grades_agree": x_grades[0] == y_grades[0] == 6,
    "square_grades_agree": x_grades[1] == y_grades[1] == -7,
    "third_grades_differ": x_grades[2] != y_grades[2],
    "first_third_grade_exact": x_grades[2] == 12,
    "second_third_grade_exact": y_grades[2] == Fraction(3996, 343),
    "factor_multisets_differ": sorted(X) != sorted(Y),
}

result = {
    "schema": "marici.grothendieck.primitive-square-multifactor-collision.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "X": [str(x) for x in X],
        "Y": [str(y) for y in Y],
        "connected_grades_X": [str(x) for x in x_grades],
        "connected_grades_Y": [str(y) for y in y_grades],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
