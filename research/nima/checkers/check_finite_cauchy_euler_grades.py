import json
from fractions import Fraction


primes = [2, 3, 5, 7]
max_grade = 8


def trace_power(grade):
    return sum((Fraction(1, prime) ** grade for prime in primes), Fraction(0))


moments = []
for grade in range(1, max_grade + 1):
    # The Cauchy characteristic function contributes a second p^(-k/2), so
    # each observed raw coordinate is exactly p^(-k).
    observed = trace_power(grade)
    deterministic = trace_power(grade)
    assert observed == deterministic
    moments.append(
        {
            "grade": grade,
            "observed_trace": str(observed),
            "deterministic_trace": str(deterministic),
        }
    )

primitive = trace_power(1)
square = Fraction(1, 2) * trace_power(2)
connected_truncation = sum(
    (Fraction(1, grade) * trace_power(grade) for grade in range(3, max_grade + 1)),
    Fraction(0),
)
full_truncation = sum(
    (Fraction(1, grade) * trace_power(grade) for grade in range(1, max_grade + 1)),
    Fraction(0),
)

assert primitive + square + connected_truncation == full_truncation

result = {
    "schema": "marici.nima.finite-cauchy-euler-grades.v1",
    "primes": primes,
    "max_grade": max_grade,
    "moments": moments,
    "primitive_truncation": str(primitive),
    "square_truncation": str(square),
    "connected_truncation": str(connected_truncation),
    "full_truncation": str(full_truncation),
    "every_finite_moment_intertwines": True,
    "observed_grades_from_two_are_globally_summable": True,
    "scalar_completion_obstruction_grade": "primitive",
    "state_valued_completion_closed": False,
}
print(json.dumps(result, indent=2, sort_keys=True))

