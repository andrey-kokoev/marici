"""Exact Vandermonde check for derivative-current mode closure."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def determinant(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        p = a[col][col]
        det *= p
        for j in range(col, n):
            a[col][j] /= p
        for r in range(col + 1, n):
            factor = a[r][col]
            for j in range(col, n):
                a[r][j] -= factor * a[col][j]
    return det


def derivative_coefficient_matrix(rates, coefficients):
    n = len(rates)
    return [
        [coefficients[j] * (-rates[j]) ** k for j in range(n)]
        for k in range(n)
    ]


def vandermonde_formula(rates, coefficients):
    out = Fraction(1)
    for c in coefficients:
        out *= c
    # Rows use powers of -lambda, hence the ordered factors are lambda_i-lambda_j.
    for i in range(len(rates)):
        for j in range(i + 1, len(rates)):
            out *= rates[i] - rates[j]
    return out


packets = [
    ([Fraction(2), Fraction(3)], [Fraction(1), Fraction(5)]),
    ([Fraction(2), Fraction(3), Fraction(5)], [Fraction(1), Fraction(-2), Fraction(4)]),
    ([Fraction(1, 2), Fraction(3, 2), Fraction(7, 2), Fraction(9, 2)],
     [Fraction(3), Fraction(1), Fraction(-1), Fraction(2)]),
]

records = []
for rates, coefficients in packets:
    matrix = derivative_coefficient_matrix(rates, coefficients)
    det = determinant(matrix)
    expected = vandermonde_formula(rates, coefficients)
    assert det == expected
    assert det != 0
    records.append({
        "mode_count": len(rates),
        "determinant": str(det),
        "full_rank": True,
    })

proposed_port_dimension = 3
hostile_rates = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
hostile_coefficients = [Fraction(1)] * 4
hostile_det = determinant(
    derivative_coefficient_matrix(hostile_rates, hostile_coefficients)
)
assert hostile_det != 0

payload = {
    "schema": "marici.research.check.v1",
    "claim": "distinct labelled exponential modes force full derivative-orbit rank",
    "packets": records,
    "proposed_port_dimension": proposed_port_dimension,
    "hostile_mode_count": len(hostile_rates),
    "hostile_determinant": str(hostile_det),
    "dimension_overrun_falsifier_pass": len(hostile_rates) > proposed_port_dimension,
    "verdict": "no cutoff-independent finite derivative-current closure",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-derivative-mode-closure.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
