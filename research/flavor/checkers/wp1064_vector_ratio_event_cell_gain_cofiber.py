import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1052's common-source atom cell.
alpha = beta = sigma = nu = d = Fraction(1)
c = eta = Fraction(1, 2)
B = Fraction(0)
g = Fraction(1)

# WP1062's source-derived first vector-KK threshold shape.
L_vector = Fraction(1, 5)
S = B + alpha * L_vector * g * g
D = 4 * nu * d * c * sigma * L_vector * g
M = eta * c * beta
N = eta * beta
assert (S, D, M, N) == (Fraction(1, 5), Fraction(2, 5), Fraction(1, 4), Fraction(1, 2))

# Typed WP1051 reconstruction recovers the vector shape and gain exactly.
eta_rec = N / beta
c_rec = M / eta_rec
g_rec = 4 * nu * d * c_rec * (S - B) / D
L_rec = D * D / (16 * nu * nu * d * d * c_rec * c_rec * (S - B))
assert (eta_rec, c_rec, g_rec, L_rec) == (eta, c, g, L_vector)

# Exact hostile: retaining WP1042's ratio-one shape changes the retained rows.
L_unit = Fraction(1, 2)
S_unit = B + alpha * L_unit * g * g
D_unit = 4 * nu * d * c * sigma * L_unit * g
assert (S_unit, D_unit) == (Fraction(1, 2), Fraction(1))
assert S_unit - S == Fraction(3, 10)
assert D_unit - D == Fraction(3, 5)

# Coherent-row laundering check: another (L,g) with the same rate does not
# preserve the vector coherent difference.
g_launder = Fraction(1, 2)
L_launder = (S - B) / (g_launder * g_launder)
D_launder = 4 * nu * d * c * sigma * L_launder * g_launder
assert L_launder == Fraction(4, 5)
assert D_launder == Fraction(4, 5)
assert D_launder != D

result = {
    "schema": "marici.flavor.wp1064.v1",
    "status": "PASS",
    "question": "Can the WP1052 physical16 atom cell carry WP1062's source-derived vector threshold ratio?",
    "atom_cell": {
        "alpha": str(alpha), "beta": str(beta), "c": str(c), "eta": str(eta), "sigma": str(sigma),
        "nu": str(nu), "d": str(d), "B": str(B), "g": str(g),
    },
    "vector_ratio_cell": {
        "threshold_ratio": "4",
        "L": str(L_vector),
        "S": str(S), "D": str(D), "M": str(M), "N": str(N),
        "reconstruction": {
            "eta": str(eta_rec), "c": str(c_rec), "g": str(g_rec), "L": str(L_rec),
        },
    },
    "unit_ratio_hostile": {
        "threshold_ratio": "1",
        "L": str(L_unit), "S": str(S_unit), "D": str(D_unit),
        "row_gaps": {"S": str(S_unit - S), "D": str(D_unit - D)},
    },
    "laundering_hostile": {
        "same_rate_L": str(L_launder), "g": str(g_launder), "D": str(D_launder),
        "separated_by_coherent_row": True,
    },
    "classification": "conditional vector-ratio event-cell constructor: the common-source atom cell carries the source-derived ratio-4 threshold shape and reconstructs (L,g)=(1/5,1), but physical16 channel realization and atom-weight dynamics remain open",
    "remaining_gate": "realize the vector and/or soft momentum ports in actual physical16 production/decay channels and derive the atom weights, labels, and gain g from one source",
    "claim_boundary": "uses WP1052's conditional atom cell and WP1062's vector ratio; it does not prove that physical16 has these atoms or that g=1",
    "disposition": "productive: the gain chain now has an exact vector-ratio branch, so the missing soft channel is no longer the only coherent readout route",
}

(ROOT / "results" / "wp1064_vector_ratio_event_cell_gain_cofiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1064 PASS:", L_vector, S, D, g_rec, L_rec)
