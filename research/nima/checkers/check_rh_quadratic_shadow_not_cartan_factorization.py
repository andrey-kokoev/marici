import json
from fractions import Fraction
from pathlib import Path


# One-dimensional quadratic identity H=aN.
samples = []
for a in (Fraction(-2), Fraction(-1, 3), Fraction(1, 4), Fraction(3)):
    for x in (Fraction(-2), Fraction(0), Fraction(1, 2), Fraction(5)):
        left = a * x * x
        right = a * x * x
        assert left == right
    samples.append({"a": str(a), "quadratic_identity_holds": True})

# A scalar nilpotent operator d obeys d^2=0 only when d=0 over Q; likewise Q.
# Their anticommutator is then zero and cannot equal nonzero a.
scalar_nilpotent_d = Fraction(0)
scalar_nilpotent_q = Fraction(0)
scalar_anticommutator = 2 * scalar_nilpotent_d * scalar_nilpotent_q
assert scalar_anticommutator == 0


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def add(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(2)) for i in range(2))


a = Fraction(3, 2)
d = ((Fraction(0), a), (Fraction(0), Fraction(0)))
q = ((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)))
graded_anticommutator = add(matmul(d, q), matmul(q, d))
expected = ((a, Fraction(0)), (Fraction(0), a))
assert graded_anticommutator == expected

result = {
    "one_dimensional_quadratic_samples": samples,
    "one_dimensional_nilpotent_factorization_exists_for_nonzero_a": False,
    "minimal_graded_enlargement": "1|1",
    "graded_anticommutator_example": [[str(entry) for entry in row] for row in graded_anticommutator],
    "quadratic_identity_authorizes_graded_enlargement": False,
    "required_next_object": "source-derived graded differential and contraction on the polarized Green module",
    "verdict": "normal-divisible quadratic energy is only the shadow of, not evidence for, a Cartan factorization",
}

output = Path(__file__).parents[1] / "results" / "rh-quadratic-shadow-not-cartan-factorization.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

