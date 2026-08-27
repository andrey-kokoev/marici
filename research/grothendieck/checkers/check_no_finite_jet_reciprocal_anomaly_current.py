from fractions import Fraction
import json


def polynomial_value(coefficients, x):
    return sum(c * x**k for k, c in enumerate(coefficients))


# Interpolation can fake the inverse multiplier on d+1 modes for a degree-d
# polynomial, but the next mode must fail. This exact audit covers d=0..8.
checks = {}
for degree in range(9):
    xs = [Fraction(-2 * (j + 1), 1) for j in range(degree + 1)]
    # Solve the Vandermonde system by exact Gaussian elimination.
    matrix = [[x**k for k in range(degree + 1)] + [1 / x] for x in xs]
    for col in range(degree + 1):
        pivot = next(row for row in range(col, degree + 1) if matrix[row][col])
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [entry / scale for entry in matrix[col]]
        for row in range(degree + 1):
            if row == col:
                continue
            scale = matrix[row][col]
            matrix[row] = [
                a - scale * b for a, b in zip(matrix[row], matrix[col])
            ]
    coefficients = [matrix[row][-1] for row in range(degree + 1)]
    hostile_x = Fraction(-2 * (degree + 2), 1)
    checks[f"degree_{degree}_fails_next_mode"] = (
        hostile_x * polynomial_value(coefficients, hostile_x) != 1
    )

out = {
    "schema": "marici.grothendieck.no-finite-jet-anomaly-current.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "symbolic_reason": "x*P(x)-1 cannot vanish on infinitely many x unless P(x)=1/x, which is not polynomial",
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

