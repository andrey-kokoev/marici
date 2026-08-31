import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    m, n = len(a), len(a[0]) if a else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r

# Coordinates: (B, L, g, nu, d, c).  c is coherent final-state overlap between
# Flavor amplitude and reference amplitude.  WP1044-WP1047 calibrate nu and d;
# they do not prove c=1.
background = [1, 0, 0, 0, 0, 0]
signal_rate = [1, 1, 2, 0, 0, 0]
flavor_difference = [0, 4, 4, 4, 4, 4]  # D = 4*nu*d*c*L*g
visibility_reference = [0, 0, 0, 1, 0, 0]
epoch_anchor = [0, 0, 0, 0, 1, 0]
cofinality_anchor = [0, 0, 0, 0, 0, 1]

rows_without_cofinality = [background, signal_rate, flavor_difference, visibility_reference, epoch_anchor]
rows_with_cofinality = rows_without_cofinality + [cofinality_anchor]
assert rank(rows_without_cofinality) == 5
assert rank(rows_with_cofinality) == 6

# Collision after all previous instrument repairs when coherent support is unproved.
def observables(B, L, g, nu, d, c):
    return {
        "B": B,
        "S": B + L * g * g,
        "D": Fraction(4) * nu * d * c * L * g,
        "Vref": nu,
        "epoch": d,
    }

packet_partial = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2))
packet_full = (Fraction(0), Fraction(1), Fraction(2), Fraction(1), Fraction(1), Fraction(1))
obs_partial = observables(*packet_partial)
obs_full = observables(*packet_full)
assert obs_partial == obs_full == {"B": 0, "S": 4, "D": 8, "Vref": 1, "epoch": 1}
assert packet_partial[5] != 1 and packet_full[5] == 1

# If cofinality is falsely assumed, partial-overlap data decode as the wrong gain.
def decode_assuming_cofinal(B, S, D, nu, d):
    # Assumes c=1.
    g = Fraction(4) * nu * d * (S - B) / D
    L = D * D / (Fraction(16) * nu * nu * d * d * (S - B))
    return L, g

wrong_L, wrong_g = decode_assuming_cofinal(
    obs_partial["B"], obs_partial["S"], obs_partial["D"], obs_partial["Vref"], obs_partial["epoch"]
)
assert (wrong_L, wrong_g) == (Fraction(1), Fraction(2))
assert (packet_partial[1], packet_partial[2]) == (Fraction(4), Fraction(1))

# With an explicit cofinality/overlap record, reconstruction includes c.
def decode_with_cofinality(B, S, D, nu, d, c):
    g = Fraction(4) * nu * d * c * (S - B) / D
    L = D * D / (Fraction(16) * nu * nu * d * d * c * c * (S - B))
    return L, g

correct_L, correct_g = decode_with_cofinality(
    obs_partial["B"], obs_partial["S"], obs_partial["D"], obs_partial["Vref"], obs_partial["epoch"], packet_partial[5]
)
assert (correct_L, correct_g) == (Fraction(4), Fraction(1))

result = {
    "schema": "marici.flavor.wp1048.v1",
    "status": "PASS",
    "question": "Do WP1044-WP1047 calibrations prove the Flavor amplitude and reference amplitude reach one coherent final state?",
    "coordinates": ["B", "L", "g", "nu", "d", "c"],
    "rank_without_cofinality": 5,
    "rank_with_cofinality_anchor": 6,
    "coherent_overlap": "c multiplies the interference difference D=4*nu*d*c*L*g",
    "exact_collision_without_cofinality": {
        "partial_overlap_packet": {"B": "0", "L": "4", "g": "1", "nu": "1", "d": "1", "c": "1/2", "observables": {k: str(v) for k, v in obs_partial.items()}},
        "full_overlap_packet": {"B": "0", "L": "1", "g": "2", "nu": "1", "d": "1", "c": "1", "observables": {k: str(v) for k, v in obs_full.items()}}
    },
    "false_cofinal_decode": {"assuming_c=1_decodes": {"L": str(wrong_L), "g": str(wrong_g)}, "actual_partial_overlap": {"L": "4", "g": "1"}},
    "decode_with_overlap_record": {"formula_g": "4*nu*d*c*(S-B)/D", "formula_L": "D^2/(16*nu^2*d^2*c^2*(S-B))", "partial_packet_L": str(correct_L), "partial_packet_g": str(correct_g)},
    "classification": "conditional support gate: calibrated visibility and live epoch do not prove coherent final-state overlap; the physical16 process must supply cofinality or measure the overlap",
    "remaining_gate": "derive one shared final-state Hilbert/event cell for the Flavor and reference amplitudes, or add an independent overlap/cofinality monitor with null-retaining loss accounting",
    "claim_boundary": "one-amplitude overlap model; does not handle multi-amplitude phases, continuum final states, or source derivation of the physical16 vertex",
    "disposition": "productive: the instrument branch reaches the physical16-process support gate rather than another scalar calibration row"
}

(ROOT / "results" / "wp1048_coherent_final_state_support_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1048 PASS:", rank(rows_without_cofinality), rank(rows_with_cofinality), wrong_g, correct_g)
