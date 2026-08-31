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

# Local logarithmic/amplitude variables at B=0, L=1, g=1, shape=1,
# calibrated reference amplitude and visibility. Coordinates: (B, L, g).
background = [1, 0, 0]                 # B
signal_rate = [1, 1, 2]                # B + L g^2
interference_difference = [0, 4, 4]    # S+ - S- = 4 L g
pure_rate_rows = [background, signal_rate]
coherent_rows = [background, signal_rate, interference_difference]
assert rank(pure_rate_rows) == 2
assert rank(coherent_rows) == 3

# If visibility is not calibrated, coordinates are (B,L,g,nu).  The same
# three rows cannot separate gain from visibility.
background_u = [1, 0, 0, 0]
signal_rate_u = [1, 1, 2, 0]
interference_difference_u = [0, 4, 4, 4]
assert rank([background_u, signal_rate_u, interference_difference_u]) == 3

# Exact nonlinear reconstruction on the calibrated coherent domain.
def reconstruct(B, S, D):
    # S = B + L*g^2, D = 4*L*g.  For D != 0 and S>B, g = 4(S-B)/D.
    g = Fraction(4) * (S - B) / D
    L = D * D / (Fraction(16) * (S - B))
    return L, g

L1, g1 = reconstruct(Fraction(0), Fraction(1), Fraction(4))
L2, g2 = reconstruct(Fraction(0), Fraction(4), Fraction(8))
assert (L1, g1) == (Fraction(1), Fraction(1))
assert (L2, g2) == (Fraction(1), Fraction(2))

# Pure rates retain the calibration-laundering hostile.
# (g,L)=(1,4) and (2,1) both give L*g^2=4.
assert Fraction(4) * Fraction(1) ** 2 == Fraction(1) * Fraction(2) ** 2
# Interference separates them when the same coherent reference is calibrated.
assert Fraction(4) * Fraction(4) * Fraction(1) != Fraction(4) * Fraction(1) * Fraction(2)

result = {
    "schema": "marici.flavor.wp1044.v1",
    "status": "PASS",
    "question": "What is the smallest coherent instrument that can attack the WP1042 physical16 gain fiber?",
    "model": "background cell B, absolute signal rate B+L*g^2, and phase-flipped coherent difference S+-S-=4*L*g with calibrated reference amplitude, shape, and visibility",
    "local_rank": {
        "coordinates": ["B", "L", "g"],
        "pure_rate_rows": pure_rate_rows,
        "pure_rate_rank": rank(pure_rate_rows),
        "coherent_rows": coherent_rows,
        "coherent_rank": rank(coherent_rows)
    },
    "exact_reconstruction": {
        "formula_g": "4*(S-B)/D",
        "formula_L": "D^2/(16*(S-B))",
        "witness_g1": {"B": "0", "S": "1", "D": "4", "L": str(L1), "g": str(g1)},
        "witness_g2": {"B": "0", "S": "4", "D": "8", "L": str(L2), "g": str(g2)}
    },
    "hostiles": {
        "pure_rate_laundering": "(g,L)=(1,4) and (2,1) have the same L*g^2=4",
        "coherent_difference_separates": "4*L*g gives 16 versus 8 on that hostile pair",
        "uncalibrated_visibility_rank": rank([background_u, signal_rate_u, interference_difference_u]),
        "uncalibrated_visibility_coordinates": ["B", "L", "g", "nu"]
    },
    "classification": "conditional instrument gate: coherent phase-flipped difference plus background and absolute signal rows identifies signed gain locally after visibility/reference calibration; it does not derive the source value of g",
    "remaining_gate": "construct a physical16 process with one coherent final state, calibrated reference amplitude and visibility, retained plus/minus ports, background model, and source provenance for using this gain in the Flavor Interaction Net",
    "claim_boundary": "factorized one-amplitude model at nonzero signal and nonzero coherent difference; finite-width, multiple amplitudes, detector adaptation, and physical16 source typing remain outside this checker",
    "disposition": "productive: WP1042's gain fiber has a minimal conditional acquisition target, but no current Flavor source or experiment instantiates it"
}

(ROOT / "results" / "wp1044_coherent_rate_interference_gain_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1044 PASS:", rank(pure_rate_rows), rank(coherent_rows), g1, g2)
