from fractions import Fraction
import json
from pathlib import Path


def identity(n):
    return [
        [Fraction(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]


def multiply(left, right):
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def power(matrix, exponent):
    result = identity(len(matrix))
    for _ in range(exponent):
        result = multiply(result, matrix)
    return result


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def shift(n):
    return [
        [Fraction(1 if j == i + 1 else 0) for j in range(n)]
        for i in range(n)
    ]


def dot(row, column):
    return sum((a * b for a, b in zip(row, column)), Fraction(0))


def matvec(matrix, vector):
    return [
        sum((a * b for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


def coupled(a, b, c, q):
    n = len(a)
    return [
        a[i] + [b[i]]
        for i in range(n)
    ] + [c + [q]]


records = []
for n in range(2, 9):
    a = shift(n)
    q = Fraction(2, 5)

    # Nonzero incidence and return maps with no directed return path.
    b_safe = [Fraction(1)] + [Fraction(0) for _ in range(n - 1)]
    c_safe = [Fraction(0) for _ in range(n - 1)] + [Fraction(1)]

    safe_moments = []
    current = b_safe
    for _ in range(n):
        safe_moments.append(dot(c_safe, current))
        current = matvec(a, current)
    assert all(moment == 0 for moment in safe_moments)

    safe = coupled(a, b_safe, c_safe, q)
    for grade in range(1, 2 * n + 3):
        assert trace(power(safe, grade)) == q ** grade

    # Terminal incidence followed by shift transport and initial return closes
    # one extra cycle of length n+1.
    b_bad = [Fraction(0) for _ in range(n - 1)] + [Fraction(1)]
    c_bad = [Fraction(1)] + [Fraction(0) for _ in range(n - 1)]

    bad_moments = []
    current = b_bad
    for _ in range(n):
        bad_moments.append(dot(c_bad, current))
        current = matvec(a, current)
    assert bad_moments[:-1] == [0 for _ in range(n - 1)]
    assert bad_moments[-1] == 1

    bad = coupled(a, b_bad, c_bad, q)
    for grade in range(1, n + 1):
        assert trace(power(bad, grade)) == q ** grade
    assert trace(power(bad, n + 1)) != q ** (n + 1)

    records.append(
        {
            "boundary_dimension": n,
            "safe_mixed_moments_all_zero": True,
            "hostile_first_nonzero_moment": n - 1,
            "hostile_first_contaminated_trace_grade": n + 1,
        }
    )

result = {
    "schema": "marici.nima.determinant-preserving-attachment.v1",
    "records": records,
    "nonzero_couplings_can_preserve_primitive_determinant": True,
    "bidirectional_coupling_automatically_preserves_grammar": False,
    "verdict": "preservation is equivalent to vanishing mixed return moments",
}

out = Path(__file__).parents[1] / "results" / "determinant-preserving-attachment.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
