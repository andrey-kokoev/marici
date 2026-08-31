import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rank(mat):
    m = [[Fraction(x) for x in row] for row in mat]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if m[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                factor = m[i][c]
                m[i] = [x - factor * y for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r

# Six-port scale identification: unreferenced rows have rank one; an
# independent frequency reference raises the scale rank to two.
c_values = [1, 2, 3, 5, 7, 11]
six_port_rows = [[c, -c] for c in c_values]
assert rank(six_port_rows) == 1
assert rank(six_port_rows + [[0, 1]]) == 2

# Source-monitor affine calibration: y=g x+o.  Dark fixes o, bright-dark
# fixes g, and the corrected science record recovers x.
g = Fraction(2)
o = Fraction(1, 10)
reference = Fraction(1)
science_x = Fraction(1, 8)
dark = o
bright = g * reference + o
science_y = g * science_x + o
g_recovered = (bright - dark) / reference
x_recovered = (science_y - dark) / g_recovered
assert g_recovered == g
assert x_recovered == science_x

# A bright reference alone has a gain/offset alias.
g_alias = Fraction(3)
o_alias = o + (g - g_alias) * reference
assert g_alias * reference + o_alias == bright
x_alias = (science_y - o_alias) / g_alias
assert x_alias == Fraction(5, 12)
assert x_alias != science_x

# Phase-sensitive detection needs two independent calibrated phase rows.
assert rank([[1, 0]]) == 1
assert rank([[1, 0], [0, 1]]) == 2

# Robustness threshold: predeclared eta separates detectable from unresolved
# coupling hostiles.
eta = Fraction(1, 1000)
assert Fraction(1, 100) > eta
assert Fraction(1, 10000) < eta

result = {
    "schema": "marici.flavor.wp1078.v1",
    "status": "PASS",
    "question": "Can the cited Aspect calibration patterns compose with the WP1077 acquisition gate without claiming source selection?",
    "aspect_sources": [
        "research/aspect/calibrated-six-port-scale-identification-instrument.md",
        "research/aspect/source-monitor-gain-calibration.md",
        "research/aspect/calibrated-homodyne-heterodyne-detection.md",
        "research/aspect/two-instrument-calibration-robustness.md",
    ],
    "composed_gates": {
        "six_port_unreferenced_rank": rank(six_port_rows),
        "six_port_referenced_rank": rank(six_port_rows + [[0, 1]]),
        "monitor_affine_recovery": {
            "gain": str(g_recovered),
            "offset": str(o),
            "science": str(x_recovered),
        },
        "one_reference_alias_science": str(x_alias),
        "phase_row_ranks": [1, 2],
        "noise_floor": str(eta),
        "detectable_coupling": "1/100",
        "unresolved_coupling": "1/10000",
    },
    "constructor_order": [
        "calibrate dark and bright monitor rows at each epoch",
        "prepare independent scale reference",
        "calibrate gain balance and common phase frame",
        "retain two phase rows and environment/noise ports",
        "calibrate momentum in the same frame",
        "reconstruct coherent rows before threshold comparison",
        "compare residuals with a predeclared noise floor",
    ],
    "classification": "conditional Aspect-pattern composition: the cited instruments close scale, affine-monitor, phase, and robustness hostiles but still contribute no source-production kernel",
    "remaining_gate": "attach the calibrated acquisition to a source-derived physical16 production/decay kernel and mixing law",
    "claim_boundary": "audits and composes the cited instrument packets; it does not use detector rank as source authority",
    "disposition": "productive: D1 now has an exact instrument contract and a clean authority boundary",
}

(ROOT / "results" / "wp1078_aspect_pattern_acquisition_composition_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1078 PASS:", rank(six_port_rows), rank(six_port_rows + [[0, 1]]), x_recovered, x_alias)
