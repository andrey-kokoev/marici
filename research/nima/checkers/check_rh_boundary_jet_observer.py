"""Exact rank and null-vector checks for the reservoir boundary jet."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def rref(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivots = []
    row = 0
    for col in range(cols):
        pivot = next((r for r in range(row, rows) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        value = a[row][col]
        a[row] = [x / value for x in a[row]]
        for r in range(rows):
            if r != row and a[r][col] != 0:
                factor = a[r][col]
                a[r] = [a[r][j] - factor * a[row][j] for j in range(cols)]
        pivots.append(col)
        row += 1
        if row == rows:
            break
    return a, pivots


def null_vector(matrix):
    reduced, pivots = rref(matrix)
    cols = len(matrix[0])
    free = next(col for col in range(cols) if col not in pivots)
    vector = [Fraction(0) for _ in range(cols)]
    vector[free] = Fraction(1)
    for row, pivot in reversed(list(enumerate(pivots))):
        vector[pivot] = -sum(
            reduced[row][j] * vector[j] for j in range(pivot + 1, cols)
        )
    return vector


def matvec(matrix, vector):
    return [sum(Fraction(x) * y for x, y in zip(row, vector)) for row in matrix]


def jet_matrix(rates, jet_count):
    return [
        [(-Fraction(rate)) ** k for rate in rates]
        for k in range(jet_count)
    ]


records = []
for mode_count in range(1, 6):
    rates = [2, 3, 5, 7, 11][:mode_count]
    full = jet_matrix(rates, mode_count)
    _, full_pivots = rref(full)
    assert len(full_pivots) == mode_count
    record = {
        "mode_count": mode_count,
        "full_jet_rank": len(full_pivots),
        "faithful": True,
    }
    if mode_count > 1:
        short = jet_matrix(rates, mode_count - 1)
        witness = null_vector(short)
        assert any(witness)
        assert matvec(short, witness) == [Fraction(0)] * (mode_count - 1)
        record["short_jet_rank"] = len(rref(short)[1])
        record["short_jet_null_witness"] = [str(x) for x in witness]
    records.append(record)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "N distinct source modes require N endpoint jet coordinates for faithful kernel observation",
    "records": records,
    "verdict": "scalar seam observation is not cutoff-stable",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-boundary-jet-observer.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
