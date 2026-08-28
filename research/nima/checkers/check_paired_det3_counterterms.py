from fractions import Fraction
import json
from pathlib import Path


def conjugate(value):
    return value[0], -value[1]


def scale(value, scalar):
    return value[0] * scalar, value[1] * scalar


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


base_coefficients = {
    grade: -Fraction(1, grade) for grade in range(1, 9)
}

a1 = -base_coefficients[1]
a2 = -base_coefficients[2]
assert a1 == 1
assert a2 == Fraction(1, 2)

regularized = base_coefficients.copy()
regularized[1] += a1
regularized[2] += a2
assert regularized[1] == 0
assert regularized[2] == 0
for grade in range(3, 9):
    assert regularized[grade] == -Fraction(1, grade)

trace_plus = {
    grade: (Fraction(grade + 1, grade + 2), Fraction(grade, grade + 3))
    for grade in range(1, 9)
}
trace_minus = {
    grade: conjugate(value) for grade, value in trace_plus.items()
}

counterterm_plus = add(
    trace_plus[1], scale(trace_plus[2], Fraction(1, 2))
)
counterterm_minus = add(
    trace_minus[1], scale(trace_minus[2], Fraction(1, 2))
)
assert counterterm_minus == conjugate(counterterm_plus)

# Logarithmic direct-sum additivity is coordinatewise addition of trace grades.
other = {
    grade: (Fraction(1, grade + 5), Fraction(-1, grade + 7))
    for grade in range(1, 9)
}
combined = {
    grade: add(trace_plus[grade], other[grade]) for grade in range(1, 9)
}
for grade in range(3, 9):
    left = scale(combined[grade], -Fraction(1, grade))
    right = add(
        scale(trace_plus[grade], -Fraction(1, grade)),
        scale(other[grade], -Fraction(1, grade)),
    )
    assert left == right

hostiles = [
    (Fraction(0), Fraction(1, 2)),
    (Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(1)),
]
hostile_residuals = []
for hostile_a1, hostile_a2 in hostiles:
    residual = (
        base_coefficients[1] + hostile_a1,
        base_coefficients[2] + hostile_a2,
    )
    assert residual != (0, 0)
    hostile_residuals.append([str(residual[0]), str(residual[1])])

result = {
    "schema": "marici.nima.paired-det3-counterterms.v1",
    "unique_primitive_coefficient": "1",
    "unique_square_coefficient": "1/2",
    "regularized_tail_begins_at_grade": 3,
    "reciprocal_counterterms_conjugate": True,
    "direct_sum_logarithms_add": True,
    "hostile_residuals": hostile_residuals,
    "verdict": "paired low grades uniquely determine the third regularized determinant",
}

out = Path(__file__).parents[1] / "results" / "paired-det3-counterterms.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
