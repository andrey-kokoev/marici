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

# Coordinates: (B, L, g, nu_f, nu_r).  WP1045's visibility row measures a
# reference visibility.  It calibrates the flavor visibility only if a common
# frame/source transport identifies nu_f with nu_r.
background = [1, 0, 0, 0, 0]
signal_rate = [1, 1, 2, 0, 0]
flavor_difference = [0, 4, 4, 4, 0]  # D = 4 nu_f L g
reference_visibility = [0, 0, 0, 0, 1]
common_frame_constraint = [0, 0, 0, 1, -1]

rows_without_frame = [background, signal_rate, flavor_difference, reference_visibility]
rows_with_frame = rows_without_frame + [common_frame_constraint]
assert rank(rows_without_frame) == 4
assert rank(rows_with_frame) == 5

# Exact collision when the reference visibility is not tied to the flavor arm.
def observables(B, L, g, nu_f, nu_r):
    return {
        "B": B,
        "S": B + L * g * g,
        "D": Fraction(4) * nu_f * L * g,
        "Vref": nu_r,
    }

packet_a = (Fraction(0), Fraction(4), Fraction(1), Fraction(1, 2), Fraction(1))
packet_b = (Fraction(0), Fraction(1), Fraction(2), Fraction(1), Fraction(1))
obs_a = observables(*packet_a)
obs_b = observables(*packet_b)
assert obs_a == obs_b == {"B": 0, "S": 4, "D": 8, "Vref": 1}
assert packet_a[3] != packet_a[4]
assert packet_b[3] == packet_b[4]

# With the common-frame constraint, packet_a is rejected and packet_b remains.
def common_frame_ok(packet):
    return packet[3] == packet[4]
assert not common_frame_ok(packet_a)
assert common_frame_ok(packet_b)

# If common-frame transport is granted, reconstruction uses nu_r as nu_f.
def reconstruct(B, S, D, nu_r):
    g = Fraction(4) * nu_r * (S - B) / D
    L = D * D / (Fraction(16) * nu_r * nu_r * (S - B))
    return L, g

L_b, g_b = reconstruct(obs_b["B"], obs_b["S"], obs_b["D"], obs_b["Vref"])
assert (L_b, g_b) == (Fraction(1), Fraction(2))

result = {
    "schema": "marici.flavor.wp1046.v1",
    "status": "PASS",
    "question": "Does a reference-only visibility measurement calibrate the Flavor interference arm without common-frame transport?",
    "coordinates": ["B", "L", "g", "nu_f", "nu_r"],
    "rows_without_common_frame": rows_without_frame,
    "rank_without_common_frame": 4,
    "common_frame_constraint": common_frame_constraint,
    "rank_with_common_frame_constraint": 5,
    "exact_collision_without_frame": {
        "packet_A": {"B": "0", "L": "4", "g": "1", "nu_f": "1/2", "nu_r": "1", "observables": {k: str(v) for k, v in obs_a.items()}},
        "packet_B": {"B": "0", "L": "1", "g": "2", "nu_f": "1", "nu_r": "1", "observables": {k: str(v) for k, v in obs_b.items()}}
    },
    "common_frame_rejection": "packet_A is rejected by nu_f=nu_r; packet_B satisfies it",
    "reconstruction_when_granted": {"formula_g": "4*nu_r*(S-B)/D", "formula_L": "D^2/(16*nu_r^2*(S-B))", "packet_B_L": str(L_b), "packet_B_g": str(g_b)},
    "classification": "conditional transport gate: a reference row calibrates Flavor visibility only after a source or apparatus law identifies the reference and flavor visibilities in one frame",
    "remaining_gate": "derive common-frame visibility transport, including stability under drift and finite-width detector response, for the actual physical16 process",
    "claim_boundary": "local algebraic one-amplitude visibility model; does not prove existence of the reference channel or its independence from the Flavor portal",
    "disposition": "productive: WP1045's reference-independence caveat is sharpened to a common-frame equality/transport obligation"
}

(ROOT / "results" / "wp1046_common_frame_visibility_transport_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1046 PASS:", rank(rows_without_frame), rank(rows_with_frame), g_b)
