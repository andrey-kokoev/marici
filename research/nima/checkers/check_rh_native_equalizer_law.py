"""Exact finite checks for the reciprocal native-equalizer theorem."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
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
        if pivot_row == rows:
            break
    return pivot_row


def weighted_jet_matrix(rates, incidences):
    n = len(rates)
    return [
        [Fraction(incidences[j]) * (-Fraction(rates[j])) ** k for j in range(n)]
        for k in range(n)
    ]


off_seam_records = []
for rates, incidences in [
    ([2], [3]),
    ([2, 3], [1, -2]),
    ([2, 3, 5], [1, -2, 4]),
    ([2, 3, 5, 7], [1, 2, 3, 4]),
]:
    reservoir_rank = rank(weighted_jet_matrix(rates, incidences))
    assert reservoir_rank == len(rates)
    # The reciprocal difference first kills G; the weighted jet then kills c.
    full_constraint_rank = 1 + reservoir_rank
    assert full_constraint_rank == 1 + len(rates)
    off_seam_records.append({
        "label_count": len(rates),
        "equalizer_constraint_rank": full_constraint_rank,
        "state_dimension": 1 + len(rates),
        "trivial_equalizer": True,
    })

# A nonzero one-mode state exists on the seam.
z_seam = Fraction(1, 2)
rate = Fraction(2)
incidence = Fraction(3)
c = Fraction(5)
amplitude = -incidence * c / (z_seam - rate)
assert (z_seam - rate) * amplitude + incidence * c == 0
assert amplitude != 0 and c != 0

# Off-seam fitted reciprocal incidence restores a nonzero common state.
z = Fraction(3, 4)
plus_incidence = Fraction(2)
hostile_minus_incidence = plus_incidence * (1 - z - rate) / (z - rate)
hostile_amplitude = -plus_incidence * c / (z - rate)
assert (z - rate) * hostile_amplitude + plus_incidence * c == 0
assert (1 - z - rate) * hostile_amplitude + hostile_minus_incidence * c == 0
assert hostile_minus_incidence != plus_incidence

payload = {
    "schema": "marici.research.check.v1",
    "claim": "a common-frame reciprocal equalizer is trivial off seam but permits seam states",
    "off_seam_records": off_seam_records,
    "seam_nonzero_state": {
        "tail_amplitude": str(amplitude),
        "reservoir_amplitude": str(c),
    },
    "fitted_frame_hostile": {
        "z": str(z),
        "plus_incidence": str(plus_incidence),
        "minus_incidence": str(hostile_minus_incidence),
        "nonzero_state_admitted": True,
    },
    "verdict": "conditional contraction; common-frame source authority is decisive",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-native-equalizer-law.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
