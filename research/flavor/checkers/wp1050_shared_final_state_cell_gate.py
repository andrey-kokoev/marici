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

# Coordinates: (B,L,g,nu,d,c,eta,sigma).  sigma distinguishes same-cell
# overlap (1) from split-cell/reference-only cross-amplitude (0).  The observed
# overlap is M=eta*c; a split-cell reference can present the same monitor record
# but does not satisfy the same-cell science rows D/S.
background = [1, 0, 0, 0, 0, 0, 0, 0]
signal_rate = [1, 1, 2, 0, 0, 0, 0, 0]
flavor_difference = [0, 4, 4, 4, 4, 4, 0, 4]  # D=4*nu*d*c*sigma*L*g
visibility_reference = [0, 0, 0, 1, 0, 0, 0, 0]
epoch_anchor = [0, 0, 0, 0, 1, 0, 0, 0]
overlap_monitor = [0, 0, 0, 0, 0, 1, 1, 0]    # M=eta*c
null_loss_monitor = [0, 0, 0, 0, 0, 0, 1, 0]  # eta
same_cell_certificate = [0, 0, 0, 0, 0, 0, 0, 1]  # sigma

rows_without_same_cell = [background, signal_rate, flavor_difference, visibility_reference, epoch_anchor, overlap_monitor, null_loss_monitor]
rows_with_same_cell = rows_without_same_cell + [same_cell_certificate]
assert rank(rows_without_same_cell) == 7
assert rank(rows_with_same_cell) == 8

# Collision after null accounting if same-cell support is unproved.
def observables(B, L, g, nu, d, c, eta, sigma):
    return {
        "B": B,
        "S": B + L * g * g,
        "D": Fraction(4) * nu * d * c * sigma * L * g,
        "Vref": nu,
        "epoch": d,
        "M": eta * c,
        "eta": eta,
    }

same_cell_half_overlap = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2), Fraction(1))
split_cell_proxy = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2), Fraction(0))
obs_same = observables(*same_cell_half_overlap)
obs_split = observables(*split_cell_proxy)
assert obs_same == {"B": 0, "S": 4, "D": 8, "Vref": 1, "epoch": 1, "M": Fraction(1, 4), "eta": Fraction(1, 2)}
assert obs_split == {"B": 0, "S": 4, "D": 0, "Vref": 1, "epoch": 1, "M": Fraction(1, 4), "eta": Fraction(1, 2)}
assert obs_same["M"] == obs_split["M"] and obs_same["eta"] == obs_split["eta"]
assert obs_same["D"] != obs_split["D"]

# Treating the split-cell monitor record as a same-cell science overlap predicts
# a nonzero Flavor difference. Its actual D=0 rejects that promotion.
def decode_with_c(B, S, D, nu, d, c):
    g = Fraction(4) * nu * d * c * (S - B) / D
    L = D * D / (Fraction(16) * nu * nu * d * d * c * c * (S - B))
    return L, g

decoded_c = obs_split["M"] / obs_split["eta"]
assert decoded_c == Fraction(1, 2)
try:
    decode_with_c(obs_split["B"], obs_split["S"], obs_split["D"], obs_split["Vref"], obs_split["epoch"], decoded_c)
except ZeroDivisionError:
    rejected = True
else:
    rejected = False
assert rejected
assert split_cell_proxy[7] == 0  # not a same-cell Flavor-reference final state

# A same-cell certificate separates the packets before any gain promotion.
def same_cell_ok(packet):
    return packet[7] == 1
assert same_cell_ok(same_cell_half_overlap)
assert not same_cell_ok(split_cell_proxy)

result = {
    "schema": "marici.flavor.wp1050.v1",
    "status": "PASS",
    "question": "Does a null-complete overlap monitor prove the Flavor and reference amplitudes share one physical16 final-state cell?",
    "coordinates": ["B", "L", "g", "nu", "d", "c", "eta", "sigma"],
    "rank_without_same_cell_certificate": 7,
    "rank_with_same_cell_certificate": 8,
    "overlap_monitor_law": "M=eta*c; science D=4*nu*d*c*sigma*L*g",
    "exact_collision_without_same_cell": {
        "same_cell_half_overlap": {"B": "0", "L": "4", "g": "1", "nu": "1", "d": "1", "c": "1/2", "eta": "1/2", "sigma": "1", "observables": {k: str(v) for k, v in obs_same.items()}},
        "split_cell_proxy": {"B": "0", "L": "4", "g": "1", "nu": "1", "d": "1", "c": "1/2", "eta": "1/2", "sigma": "0", "observables": {k: str(v) for k, v in obs_split.items()}}
    },
    "false_same_cell_decode": {"decoded_c": str(decoded_c), "same_cell_D": str(obs_same["D"]), "split_cell_D": str(obs_split["D"]), "rejected": rejected},
    "same_cell_gate": {"same_cell_half_overlap": same_cell_ok(same_cell_half_overlap), "split_cell_proxy": same_cell_ok(split_cell_proxy)},
    "classification": "conditional shared-cell gate: null accounting separates monitor efficiency from overlap but does not prove that the overlap occurs in one physical16 final-state cell",
    "remaining_gate": "construct the actual physical16 shared final-state event cell with typed flavor, reference, cross-amplitude, and null outcomes; reject split-cell cross-amplitude proxies",
    "claim_boundary": "binary same-cell certificate only; does not derive the physical16 vertex, shared-state Hilbert space, or continuum event cell",
    "disposition": "productive: WP1049's null-complete monitor alternative now has an explicit same-cell separation gate"
}

(ROOT / "results" / "wp1050_shared_final_state_cell_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1050 PASS:", rank(rows_without_same_cell), rank(rows_with_same_cell), decoded_c, rejected)
