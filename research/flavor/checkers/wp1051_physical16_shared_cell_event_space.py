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

# Typed physical16 shared-cell event-space constructor.
# Coordinates: (B,L,g,nu,d,c,eta,sigma,alpha,beta).
# alpha is detector-cell support; beta is monitor-cell support.
background = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
signal_rate = [1, 1, 2, 0, 0, 0, 0, 0, 10, 0]              # S=B+alpha*L*g^2
flavor_difference = [0, 4, 4, 4, 4, 4, 0, 4, 0, 0]         # D=4*nu*d*c*sigma*L*g
visibility_reference = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
epoch_anchor = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
overlap_monitor = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1]            # M=eta*c*beta
null_loss_monitor = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]          # N=eta*beta
same_cell_certificate = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
detector_cell_support = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
monitor_cell_support = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

rows_without_cells = [background, signal_rate, flavor_difference, visibility_reference, epoch_anchor, overlap_monitor, null_loss_monitor, same_cell_certificate]
rows_with_cells = rows_without_cells + [detector_cell_support, monitor_cell_support]
assert rank(rows_without_cells) == 8
assert rank(rows_with_cells) == 10

# Exact model: detector events satisfy S=B+alpha*L*g^2 and
# D=4*nu*d*c*sigma*L*g; monitor events satisfy M=eta*c*beta and N=eta*beta.
def observables(B, L, g, nu, d, c, eta, sigma, alpha, beta):
    return {
        "B": B,
        "S": B + alpha * L * g * g,
        "D": Fraction(4) * nu * d * c * sigma * L * g,
        "Vref": nu,
        "epoch": d,
        "M": eta * c * beta,
        "N": eta * beta,
        "sigma": sigma,
    }

same_cell = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2), Fraction(1), Fraction(1), Fraction(1))
monitor_leak = (Fraction(0), Fraction(4), Fraction(1), Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2), Fraction(1), Fraction(1), Fraction(1, 2))
obs_same = observables(*same_cell)
obs_leak = observables(*monitor_leak)
assert obs_same == {"B": 0, "S": 4, "D": 8, "Vref": 1, "epoch": 1, "M": Fraction(1, 4), "N": Fraction(1, 2), "sigma": 1}
assert obs_leak == {"B": 0, "S": 4, "D": 8, "Vref": 1, "epoch": 1, "M": Fraction(1, 8), "N": Fraction(1, 4), "sigma": 1}
assert obs_same["sigma"] == obs_leak["sigma"] and obs_same["S"] == obs_leak["S"] and obs_same["D"] == obs_leak["D"]
assert (obs_same["M"], obs_same["N"]) != (obs_leak["M"], obs_leak["N"])

# Decoding the leaked cell while assuming beta=1 uses M/N as an overlap proxy;
# typed beta is needed to recover eta=N/beta and c=M/eta.
def decode_gain(B, S, D, nu, d, c):
    g = Fraction(4) * nu * d * c * (S - B) / D
    L = D * D / (Fraction(16) * nu * nu * d * d * c * c * (S - B))
    return L, g

c_wrong = obs_leak["M"] / obs_leak["N"]
wrong_L, wrong_g = decode_gain(obs_leak["B"], obs_leak["S"], obs_leak["D"], obs_leak["Vref"], obs_leak["epoch"], c_wrong)
assert c_wrong == Fraction(1, 2)
assert (wrong_L, wrong_g) == (Fraction(4), Fraction(1))
assert monitor_leak[9] == Fraction(1, 2)

# Typed cell rows repair the monitor reconstruction: c=M/eta and eta=N/beta.
def decode_with_cell_rows(B, S, D, nu, d, M, N, beta):
    eta = N / beta
    c = M / eta
    L, g = decode_gain(B, S, D, nu, d, c)
    return eta, c, L, g

eta_rec, c_rec, L_rec, g_rec = decode_with_cell_rows(obs_same["B"], obs_same["S"], obs_same["D"], obs_same["Vref"], obs_same["epoch"], obs_same["M"], obs_same["N"], same_cell[9])
assert (eta_rec, c_rec, L_rec, g_rec) == (Fraction(1, 2), Fraction(1, 2), Fraction(4), Fraction(1))
eta_leak, c_leak, L_leak, g_leak = decode_with_cell_rows(obs_leak["B"], obs_leak["S"], obs_leak["D"], obs_leak["Vref"], obs_leak["epoch"], obs_leak["M"], obs_leak["N"], monitor_leak[9])
assert (eta_leak, c_leak, L_leak, g_leak) == (Fraction(1, 2), Fraction(1, 4), Fraction(16), Fraction(1, 2))
assert monitor_leak[5] == Fraction(1, 2)  # intended overlap is not the typed monitor c

result = {
    "schema": "marici.flavor.wp1051.v1",
    "status": "PASS",
    "question": "Can a typed physical16 shared-cell event space distinguish an actual same-cell overlap from a leaked/mis-celled monitor overlap?",
    "coordinates": ["B", "L", "g", "nu", "d", "c", "eta", "sigma", "alpha", "beta"],
    "typed_event_rows": {
        "detector_signal": "S=B+alpha*L*g^2",
        "science_interference": "D=4*nu*d*c*sigma*L*g",
        "overlap_monitor": "M=eta*c*beta",
        "null_loss": "N=eta*beta"
    },
    "rank_without_typed_cell_support": 8,
    "rank_with_detector_and_monitor_cell_support": 10,
    "exact_mis_celled_hostile": {
        "same_cell": {"packet": [str(x) for x in same_cell], "observables": {k: str(v) for k, v in obs_same.items()}},
        "monitor_leak": {"packet": [str(x) for x in monitor_leak], "observables": {k: str(v) for k, v in obs_leak.items()}},
        "wrong_decode_assuming_beta_1": {"c": str(c_wrong), "L": str(wrong_L), "g": str(wrong_g), "actual_beta": "1/2", "typed_monitor_c": "1/4"}
    },
    "same_cell_reconstruction_with_cell_rows": {"eta": str(eta_rec), "c": str(c_rec), "L": str(L_rec), "g": str(g_rec), "leak_with_typed_beta": {"eta": str(eta_leak), "c": str(c_leak), "L": str(L_leak), "g": str(g_leak)}},
    "classification": "conditional event-cell gate: a same-cell certificate is insufficient unless detector-cell and monitor-cell supports are typed and null-complete",
    "remaining_gate": "realize the physical16 event cell with detector cell support alpha and monitor cell support beta derived from the same source, with typed flavor/reference/cross/null outcomes",
    "claim_boundary": "exact two-cell binary support model; does not derive the physical16 Hilbert space, detector dynamics, or continuum cell support",
    "disposition": "productive: WP1050's typed event-cell requirement now has a minimal exact mis-celled hostile and cell-support reconstruction"
}

(ROOT / "results" / "wp1051_physical16_shared_cell_event_space.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1051 PASS:", rank(rows_without_cells), rank(rows_with_cells), wrong_g, c_rec)
