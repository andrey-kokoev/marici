"""Exact finite model for the mixed residue normal law."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def determinant_3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def matvec(matrix, vector):
    return [sum(Fraction(x) * y for x, y in zip(row, vector)) for row in matrix]


def rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    rows = len(a)
    cols = len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        value = a[pivot_row][col]
        a[pivot_row] = [x / value for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [a[r][j] - factor * a[pivot_row][j] for j in range(cols)]
        pivot_row += 1
    return pivot_row


def operator(normal):
    normal = Fraction(normal)
    return [
        [Fraction(1), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(-1), Fraction(1)],
        [Fraction(0), Fraction(0), normal],
    ]


records = []
for normal in [Fraction(-3), Fraction(-1, 4), Fraction(1, 4), Fraction(5)]:
    matrix = operator(normal)
    assert determinant_3(matrix) == -normal
    assert rank(matrix) == 3
    errors = [Fraction(2), Fraction(-3), Fraction(5)]
    residue = errors[2] / normal
    state = [errors[0] + residue, -errors[1] + residue, residue]
    assert matvec(matrix, state) == errors
    records.append({
        "normal": str(normal),
        "determinant": str(-normal),
        "full_rank": True,
        "inverse_verified": True,
    })

seam_matrix = operator(0)
assert determinant_3(seam_matrix) == 0
assert rank(seam_matrix) == 2
seam_state = [Fraction(1), Fraction(1), Fraction(1)]
assert matvec(seam_matrix, seam_state) == [Fraction(0)] * 3

# A fitted normal law beta(z)=z-z0 creates an off-seam kernel at z0=3/4.
z0 = Fraction(3, 4)
assert z0 != Fraction(1, 2)
hostile_beta = z0 - z0
hostile_matrix = operator(hostile_beta)
assert rank(hostile_matrix) == 2
assert matvec(hostile_matrix, seam_state) == [Fraction(0)] * 3

payload = {
    "schema": "marici.research.check.v1",
    "claim": "an exact residue classifier needs an independent mixed normal law for off-seam acyclicity",
    "off_seam_records": records,
    "seam_rank": 2,
    "seam_kernel_witness": [str(x) for x in seam_state],
    "fitted_off_seam_hostile": {
        "z0": str(z0),
        "rank": 2,
        "nonzero_kernel": True,
    },
    "verdict": "third presentation must carry source-derived normal dynamics",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-residue-normal-law.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
