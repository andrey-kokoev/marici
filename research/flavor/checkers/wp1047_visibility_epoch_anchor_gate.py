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

# Coordinates: (B, L, g, nu_r, d).  The drift d transports reference visibility
# into the Flavor arm: nu_f=d*nu_r.  A stale common-frame claim silently sets d=1.
background = [1, 0, 0, 0, 0]
signal_rate = [1, 1, 2, 0, 0]
flavor_difference = [0, 4, 4, 4, 4]  # D = 4*d*nu_r*L*g
reference_visibility = [0, 0, 0, 1, 0]
epoch_anchor = [0, 0, 0, 0, 1]       # live external anchor for d

rows_without_anchor = [background, signal_rate, flavor_difference, reference_visibility]
rows_with_anchor = rows_without_anchor + [epoch_anchor]
assert rank(rows_without_anchor) == 4
assert rank(rows_with_anchor) == 5

# Collision when the reference has an unobserved drift from the Flavor arm.
def observables(B, L, g, nu_r, d):
    return {
        "B": B,
        "S": B + L * g * g,
        "D": Fraction(4) * d * nu_r * L * g,
        "Vref": nu_r,
    }

packet_stale = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1, 2))
packet_live = (Fraction(0), Fraction(1), Fraction(2), Fraction(1), Fraction(1))
obs_stale = observables(*packet_stale)
obs_live = observables(*packet_live)
assert obs_stale == obs_live == {"B": 0, "S": 4, "D": 8, "Vref": 1}
assert packet_stale[4] != 1 and packet_live[4] == 1

# A live epoch anchor rejects stale drift before gain decoding.
def epoch_ok(packet):
    return packet[4] == 1
assert not epoch_ok(packet_stale)
assert epoch_ok(packet_live)

# Decoding while assuming d=1 gives a wrong gain on the stale packet.
def decode_assuming_live(B, S, D, nu_r):
    g = Fraction(4) * nu_r * (S - B) / D
    L = D * D / (Fraction(16) * nu_r * nu_r * (S - B))
    return L, g

wrong_L, wrong_g = decode_assuming_live(obs_stale["B"], obs_stale["S"], obs_stale["D"], obs_stale["Vref"])
assert (wrong_L, wrong_g) == (Fraction(1), Fraction(2))
assert (packet_stale[1], packet_stale[2]) == (Fraction(4), Fraction(1))

# Correct decoding with the anchored drift recovers the stale packet values.
def decode_with_anchor(B, S, D, nu_r, d):
    # S-B=L*g^2, D=4*d*nu_r*L*g.
    g = Fraction(4) * d * nu_r * (S - B) / D
    L = D * D / (Fraction(16) * d * d * nu_r * nu_r * (S - B))
    return L, g

correct_L, correct_g = decode_with_anchor(obs_stale["B"], obs_stale["S"], obs_stale["D"], obs_stale["Vref"], packet_stale[4])
assert (correct_L, correct_g) == (Fraction(4), Fraction(1))

result = {
    "schema": "marici.flavor.wp1047.v1",
    "status": "PASS",
    "question": "Does a common-frame visibility transport law remain valid without a live epoch or external drift anchor?",
    "coordinates": ["B", "L", "g", "nu_r", "d"],
    "rows_without_anchor": rows_without_anchor,
    "rank_without_anchor": 4,
    "rows_with_epoch_anchor": rows_with_anchor,
    "rank_with_epoch_anchor": 5,
    "exact_stale_collision": {
        "stale_packet": {"B": "0", "L": "4", "g": "1", "nu_r": "1", "d": "1/2", "observables": {k: str(v) for k, v in obs_stale.items()}},
        "live_packet": {"B": "0", "L": "1", "g": "2", "nu_r": "1", "d": "1", "observables": {k: str(v) for k, v in obs_live.items()}}
    },
    "stale_decode_error": {
        "assuming_d=1_decodes": {"L": str(wrong_L), "g": str(wrong_g)},
        "actual_stale": {"L": "4", "g": "1"}
    },
    "anchored_decode": {"formula_g": "4*d*nu_r*(S-B)/D", "formula_L": "D^2/(16*d^2*nu_r^2*(S-B))", "stale_packet_L": str(correct_L), "stale_packet_g": str(correct_g)},
    "classification": "conditional epoch gate: common-frame visibility transport must be live-anchored; stale transport gives a confidently wrong gain",
    "remaining_gate": "derive a live epoch interlock or external drift anchor for the actual physical16 interferometer and reject records whose transport token is stale",
    "claim_boundary": "one-amplitude multiplicative drift model; stochastic drift, finite-width lines, and physical source realization remain outside this checker",
    "disposition": "productive: WP1046's common-frame obligation now has an exact stale-frame falsifier and one-row anchor repair"
}

(ROOT / "results" / "wp1047_visibility_epoch_anchor_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1047 PASS:", rank(rows_without_anchor), rank(rows_with_anchor), wrong_g, correct_g)
