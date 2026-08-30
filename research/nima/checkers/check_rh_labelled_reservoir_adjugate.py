"""Exact polynomial adjugate checks for the labelled tail reservoir."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


ZERO = (Fraction(0),)
ONE = (Fraction(1),)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    n = max(len(a), len(b))
    return trim(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(n)
    )


def neg(a):
    return trim(-x for x in a)


def mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def minor(matrix, row, col):
    return [
        [entry for j, entry in enumerate(line) if j != col]
        for i, line in enumerate(matrix) if i != row
    ]


def det(matrix):
    n = len(matrix)
    if n == 0:
        return ONE
    if n == 1:
        return matrix[0][0]
    total = ZERO
    for j, entry in enumerate(matrix[0]):
        term = mul(entry, det(minor(matrix, 0, j)))
        total = add(total, term if j % 2 == 0 else neg(term))
    return total


def adjugate(matrix):
    n = len(matrix)
    return [
        [
            det(minor(matrix, j, i)) if (i + j) % 2 == 0
            else neg(det(minor(matrix, j, i)))
            for j in range(n)
        ]
        for i in range(n)
    ]


def matmul(a, b):
    return [
        [
            sum_poly(mul(a[i][k], b[k][j]) for k in range(len(b)))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def sum_poly(items):
    out = ZERO
    for item in items:
        out = add(out, item)
    return out


def linear(constant):
    return (Fraction(constant), Fraction(1))


def labelled_operator(z, rates, incidences):
    n = len(rates) + 1
    matrix = [[ZERO for _ in range(n)] for _ in range(n)]
    matrix[0][0] = linear(z)
    for j, incidence in enumerate(incidences, start=1):
        matrix[0][j] = (Fraction(incidence),)
    for j, rate in enumerate(rates, start=1):
        matrix[j][j] = linear(rate)
    return matrix


def scalar_identity(size, scalar):
    return [
        [scalar if i == j else ZERO for j in range(size)]
        for i in range(size)
    ]


records = []
for rates, incidences in [
    ([2], [1]),
    ([2, 3], [1, -2]),
    ([2, 3, 5], [1, -2, 4]),
]:
    matrix = labelled_operator(Fraction(3, 2), rates, incidences)
    delta = det(matrix)
    adj = adjugate(matrix)
    expected = scalar_identity(len(matrix), delta)
    assert matmul(adj, matrix) == expected
    assert matmul(matrix, adj) == expected
    assert len(delta) - 1 == len(rates) + 1
    records.append({
        "label_count": len(rates),
        "matrix_size": len(matrix),
        "characteristic_order": len(delta) - 1,
        "left_identity": True,
        "right_identity": True,
    })

payload = {
    "schema": "marici.research.check.v1",
    "claim": "label resolution repairs the adjugate but yields a growing characteristic differential factor",
    "records": records,
    "verdict": "compositional closure without Cartan contraction",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-labelled-reservoir-adjugate.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
