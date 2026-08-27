"""Exact checks for the finite cutoff-natural reciprocal equalizer cube."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def matvec(matrix, vector):
    return [sum(Fraction(x) * y for x, y in zip(row, vector)) for row in matrix]


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


def sector_matrix(z, rates, incidences, reciprocal=False):
    n = len(rates)
    matrix = [[Fraction(0) for _ in range(2 * n)] for _ in range(n)]
    for j, (rate, incidence) in enumerate(zip(rates, incidences)):
        matrix[j][2 * j] = (1 - z - rate) if reciprocal else (z - rate)
        matrix[j][2 * j + 1] = incidence
    return matrix


def stack(a, b):
    return [*a, *b]


def pad_state(state, new_mode_count):
    return [*state, *([Fraction(0), Fraction(0)] * new_mode_count)]


def jet_matrix(rates, jet_count):
    return [[(-Fraction(rate)) ** k for rate in rates] for k in range(jet_count)]


rates_all = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
incidences_all = [Fraction(1), Fraction(-2), Fraction(4), Fraction(3)]
z = Fraction(3, 4)
z_seam = Fraction(1, 2)
records = []

for n in range(1, 4):
    rates_x = rates_all[:n]
    rates_y = rates_all[: n + 1]
    incidences_x = incidences_all[:n]
    incidences_y = incidences_all[: n + 1]
    state_x = [Fraction(k + 1) for k in range(2 * n)]
    state_y = pad_state(state_x, 1)

    plus_x = sector_matrix(z, rates_x, incidences_x)
    plus_y = sector_matrix(z, rates_y, incidences_y)
    minus_x = sector_matrix(z, rates_x, incidences_x, reciprocal=True)
    minus_y = sector_matrix(z, rates_y, incidences_y, reciprocal=True)
    assert matvec(plus_y, state_y)[:n] == matvec(plus_x, state_x)
    assert matvec(minus_y, state_y)[:n] == matvec(minus_x, state_x)

    equalizer_off = stack(plus_x, minus_x)
    assert rank(equalizer_off) == 2 * n
    equalizer_seam = stack(
        sector_matrix(z_seam, rates_x, incidences_x),
        sector_matrix(z_seam, rates_x, incidences_x, reciprocal=True),
    )
    assert rank(equalizer_seam) == n

    reservoir_x = state_x[1::2]
    reservoir_y = state_y[1::2]
    jet_x = matvec(jet_matrix(rates_x, n), reservoir_x)
    jet_y = matvec(jet_matrix(rates_y, n + 1), reservoir_y)
    assert jet_y[:n] == jet_x

    records.append({
        "small_cutoff": n,
        "large_cutoff": n + 1,
        "direct_natural": True,
        "reciprocal_natural": True,
        "off_seam_equalizer_rank": 2 * n,
        "seam_equalizer_rank": n,
        "jet_natural": True,
    })

# Changing an old incidence breaks cutoff naturality.
rates_x = rates_all[:2]
incidences_x = incidences_all[:2]
drifted_incidences = [Fraction(9), incidences_all[1], incidences_all[2]]
state_x = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
state_y = pad_state(state_x, 1)
old_output = matvec(sector_matrix(z, rates_x, incidences_x), state_x)
drifted_output = matvec(
    sector_matrix(z, rates_all[:3], drifted_incidences), state_y
)[:2]
assert old_output != drifted_output

payload = {
    "schema": "marici.research.check.v1",
    "claim": "the native finite equalizer, sector dynamics, and boundary jets form a cutoff-natural coherence cube",
    "records": records,
    "incidence_drift_breaks_naturality": True,
    "verdict": "finite cube closed; completion comparison remains open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-finite-equalizer-coherence-cube.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
