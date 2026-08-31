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

# Coordinates: (B,L,g,nu,d,c,eta).  c is final-state overlap and eta is the
# cofinality monitor collection efficiency.  H=eta*c is not a null-complete
# overlap record without eta.
background = [1, 0, 0, 0, 0, 0, 0]
signal_rate = [1, 1, 2, 0, 0, 0, 0]
flavor_difference = [0, 4, 4, 4, 4, 4, 0]  # D=4*nu*d*c*L*g
visibility_reference = [0, 0, 0, 1, 0, 0, 0]
epoch_anchor = [0, 0, 0, 0, 1, 0, 0]
overlap_monitor = [0, 0, 0, 0, 0, 1, 1]    # H=eta*c
null_loss_monitor = [0, 0, 0, 0, 0, 0, 1]  # eta, or equivalently retained null accounting

rows_without_null = [background, signal_rate, flavor_difference, visibility_reference, epoch_anchor, overlap_monitor]
rows_with_null = rows_without_null + [null_loss_monitor]
assert rank(rows_without_null) == 6
assert rank(rows_with_null) == 7

# Collision when the overlap monitor is not null-complete.
def observables(B, L, g, nu, d, c, eta):
    return {
        "B": B,
        "S": B + L * g * g,
        "D": Fraction(4) * nu * d * c * L * g,
        "Vref": nu,
        "epoch": d,
        "H": eta * c,
    }

partial_support = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1))
full_support_lossy_monitor = (Fraction(0), Fraction(1), Fraction(2), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2))
obs_partial = observables(*partial_support)
obs_full_lossy = observables(*full_support_lossy_monitor)
assert obs_partial == obs_full_lossy == {"B": 0, "S": 4, "D": 8, "Vref": 1, "epoch": 1, "H": Fraction(1, 2)}

# If H is decoded as c by assuming eta=1, the full-support lossy-monitor packet
# is assigned the wrong gain.
def decode_with_c(B, S, D, nu, d, c):
    g = Fraction(4) * nu * d * c * (S - B) / D
    L = D * D / (Fraction(16) * nu * nu * d * d * c * c * (S - B))
    return L, g

wrong_L, wrong_g = decode_with_c(obs_full_lossy["B"], obs_full_lossy["S"], obs_full_lossy["D"], obs_full_lossy["Vref"], obs_full_lossy["epoch"], obs_full_lossy["H"])
assert (wrong_L, wrong_g) == (Fraction(4), Fraction(1))
assert (full_support_lossy_monitor[1], full_support_lossy_monitor[2]) == (Fraction(1), Fraction(2))

# Null-retaining eta reconstructs c=H/eta and recovers the full-support packet.
def decode_with_null(B, S, D, nu, d, H, eta):
    c = H / eta
    L, g = decode_with_c(B, S, D, nu, d, c)
    return c, L, g

c_rec, L_rec, g_rec = decode_with_null(obs_full_lossy["B"], obs_full_lossy["S"], obs_full_lossy["D"], obs_full_lossy["Vref"], obs_full_lossy["epoch"], obs_full_lossy["H"], full_support_lossy_monitor[6])
assert (c_rec, L_rec, g_rec) == (Fraction(1), Fraction(1), Fraction(2))

result = {
    "schema": "marici.flavor.wp1049.v1",
    "status": "PASS",
    "question": "Does an overlap monitor certify physical16 cofinality without null-retaining loss accounting?",
    "coordinates": ["B", "L", "g", "nu", "d", "c", "eta"],
    "rank_without_null_loss_monitor": 6,
    "rank_with_null_loss_monitor": 7,
    "overlap_monitor_law": "H=eta*c",
    "exact_collision_without_null": {
        "partial_support": {"B": "0", "L": "4", "g": "1", "nu": "1", "d": "1", "c": "1/2", "eta": "1", "observables": {k: str(v) for k, v in obs_partial.items()}},
        "full_support_lossy_monitor": {"B": "0", "L": "1", "g": "2", "nu": "1", "d": "1", "c": "1", "eta": "1/2", "observables": {k: str(v) for k, v in obs_full_lossy.items()}}
    },
    "false_decode_assuming_eta_1": {"decoded_L": str(wrong_L), "decoded_g": str(wrong_g), "actual_L": "1", "actual_g": "2"},
    "null_retaining_decode": {"formula_c": "H/eta", "formula_g": "4*nu*d*(H/eta)*(S-B)/D", "c": str(c_rec), "L": str(L_rec), "g": str(g_rec)},
    "classification": "conditional null-accounting gate: an overlap monitor measures cofinality only after monitor loss/null events are retained or independently calibrated",
    "remaining_gate": "construct a physical16 cofinality monitor with null-complete outcome space, efficiency calibration, and proof that its null channel is not another Flavor-gain path",
    "claim_boundary": "one-amplitude multiplicative monitor-loss model; does not prove coherent final-state existence or handle continuum/multi-channel overlap",
    "disposition": "productive: WP1048's overlap-monitor alternative now has a minimal null-retaining calibration requirement"
}

(ROOT / "results" / "wp1049_overlap_monitor_null_accounting_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1049 PASS:", rank(rows_without_null), rank(rows_with_null), wrong_g, g_rec)
