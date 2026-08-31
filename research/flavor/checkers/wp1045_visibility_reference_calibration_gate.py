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

# Coordinates: (B, L, g, nu).  The reference-only fringe row measures nu in a
# channel whose amplitude is independent of the flavor portal.
background = [1, 0, 0, 0]
signal_rate = [1, 1, 2, 0]          # B + L g^2
coherent_difference = [0, 4, 4, 4]  # D = 4 nu L g
visibility_row = [0, 0, 0, 1]
assert rank([background, signal_rate, coherent_difference]) == 3
assert rank([background, signal_rate, coherent_difference, visibility_row]) == 4

# Exact reconstruction with calibrated nu.
def reconstruct(B, S, D, nu):
    # S-B = L*g^2, D = 4*nu*L*g.
    g = Fraction(4) * nu * (S - B) / D
    L = D * D / (Fraction(16) * nu * nu * (S - B))
    return L, g

L_a, g_a = reconstruct(Fraction(0), Fraction(4), Fraction(8), Fraction(1, 2))
L_b, g_b = reconstruct(Fraction(0), Fraction(4), Fraction(8), Fraction(1, 1))
assert (L_a, g_a) == (Fraction(4), Fraction(1))
assert (L_b, g_b) == (Fraction(1), Fraction(2))

# Without the visibility row the two packets collide on B,S,D.
def observables(B, L, g, nu):
    return {
        "B": B,
        "S": B + L * g * g,
        "D": Fraction(4) * nu * L * g,
    }

obs_a = observables(Fraction(0), Fraction(4), Fraction(1), Fraction(1, 2))
obs_b = observables(Fraction(0), Fraction(1), Fraction(2), Fraction(1, 1))
assert obs_a == obs_b == {"B": 0, "S": 4, "D": 8}

# Repeating the same flavor interference contrast is not a calibration row.
bad_visibility_row = coherent_difference[:]
assert rank([background, signal_rate, coherent_difference, bad_visibility_row]) == 3

result = {
    "schema": "marici.flavor.wp1045.v1",
    "status": "PASS",
    "question": "What extra reference row closes WP1044's visibility-gain confounder?",
    "coordinates": ["B", "L", "g", "nu"],
    "rows": {
        "background": background,
        "absolute_signal": signal_rate,
        "coherent_difference": coherent_difference,
        "independent_visibility_reference": visibility_row
    },
    "rank_without_visibility_reference": 3,
    "rank_with_visibility_reference": 4,
    "exact_collision_without_reference": {
        "packet_A": {"B": "0", "L": "4", "g": "1", "nu": "1/2", "observables": {k: str(v) for k, v in obs_a.items()}},
        "packet_B": {"B": "0", "L": "1", "g": "2", "nu": "1", "observables": {k: str(v) for k, v in obs_b.items()}}
    },
    "exact_reconstruction_with_reference": {
        "formula_g": "4*nu*(S-B)/D",
        "formula_L": "D^2/(16*nu^2*(S-B))",
        "packet_A": {"nu": "1/2", "L": str(L_a), "g": str(g_a)},
        "packet_B": {"nu": "1", "L": str(L_b), "g": str(g_b)}
    },
    "bad_reference_falsifier": {
        "row": bad_visibility_row,
        "rank": 3,
        "reason": "a repeated flavor contrast is another portal row, not an independent visibility calibration"
    },
    "classification": "conditional calibration gate: one independent reference-only visibility row closes the local gain-visibility kernel in the one-amplitude model",
    "remaining_gate": "derive a reference channel whose visibility is independent of the flavor portal, shares the same interferometer frame, and has its own background and stability calibration",
    "claim_boundary": "local log-linear rank and exact algebraic reconstruction; does not instantiate a collider, optical, or physical16 source process",
    "disposition": "productive: WP1044's visibility caveat is now a finite row requirement, not an unspecified calibration demand"
}

(ROOT / "results" / "wp1045_visibility_reference_calibration_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1045 PASS:", rank([background, signal_rate, coherent_difference]), rank([background, signal_rate, coherent_difference, visibility_row]), g_a, g_b)
