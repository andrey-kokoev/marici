import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1064's retained vector-ratio event-cell rows.
S = Fraction(1,5)
D = Fraction(2,5)
M = Fraction(1,4)
N = Fraction(1,2)
B = Fraction(0)
alpha = beta = sigma = nu = d = Fraction(1)

# Typed reconstruction from WP1051/WP1064.
eta = N / beta
c = M / eta
g = 4 * nu * d * c * (S - B) / D
L = D**2 / (16 * nu**2 * d**2 * c**2 * (S - B))
assert eta == Fraction(1,2)
assert c == Fraction(1,2)
assert g == Fraction(1)
assert L == Fraction(1,5)

# Hostile target gain from WP1075 changes both retained rows.
g_target = Fraction(3,2)
S_target = L * g_target**2
D_target = 4 * nu * d * c * sigma * L * g_target
assert S_target == Fraction(9,20)
assert D_target == Fraction(3,5)
assert (S_target, D_target) != (S, D)

# A pure-rate laundering pair reproduces S but not coherent D.
g_launder = Fraction(1,2)
L_launder = Fraction(4,5)
assert L_launder * g_launder**2 == S
D_launder = 4 * c * L_launder * g_launder
assert D_launder == Fraction(4,5)
assert D_launder != D

result = {
    "schema": "marici.flavor.wp1140.v1",
    "status": "PASS",
    "question": "Does carrying the vector-KK row through the gain chain uniquely fix its event-cell parameters?",
    "dpc": {
        "conjecture": "The source-derived vector-KK row can be carried through the common event-cell gain chain.",
        "rivals": [
            "unique vector event-cell",
            "WP1075 target gain",
            "pure-rate laundering",
            "no common gain chain"
        ],
        "risky_consequences": [
            "eta=c=1/2 from monitor rows",
            "g=1 and L=1/5 from coherent rows",
            "rejection of g=3/2 on the same cell",
            "rejection of same-S laundering"
        ],
        "falsification_attempt": "The chain passes only as a conditional event cell: reconstruction is unique with g=1, while target gain 3/2 changes S and D.",
        "residual": "A physical16 production packet may source a different event cell or derive the target gain.",
        "disposition": "accept a unique conditional vector carrier but reject it as source-derived gain authority"
    },
    "retained_rows": {"S": str(S), "D": str(D), "M": str(M), "N": str(N)},
    "reconstruction": {"eta": str(eta), "c": str(c), "g": str(g), "L": str(L)},
    "target_gain_hostile": {"g": str(g_target), "S": str(S_target), "D": str(D_target)},
    "pure_rate_laundering_hostile": {"g": str(g_launder), "L": str(L_launder), "D": str(D_launder)},
    "classification": "conditional vector-ratio gain-chain carrier with unique reconstruction, not source gain authority",
    "remaining_gate": "test whether the vector event-cell gain is compatible with the source reweighting gain",
    "hostile_gate": "do not treat exact row carriage or g=1 reconstruction as source-derived physical16 gain",
    "claim_boundary": "the vector ratio is source-derived; the event-cell atoms and gain remain conditional",
    "disposition": "vector-KK gain-chain leaf resolved; gain-authority branch remains open",
}

(ROOT / "results" / "wp1140_vector_kk_gain_chain_uniqueness.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1140 PASS:", g, L, S_target, D_target)
