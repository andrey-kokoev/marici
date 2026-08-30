import json
from pathlib import Path

import sympy as sp


def scores(t):
    X = sp.diag(-1, 0, 1)
    Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])
    C = X*Y - Y*X
    nx = sp.trace(X.H*X)
    ny = sp.trace(Y.H*Y)
    K = sp.factor(sp.trace(C.H*C)/(nx*ny))
    P = sp.factor(C.det()*sp.conjugate(C.det())/(nx*ny)**3)
    return K, P


Kc, Pc = scores(sp.Rational(1, 22))
Kd, Pd = scores(sp.Rational(1))

assert Kc == sp.Rational(162, 323)
assert Pc == sp.Rational(58564, 969**3)
assert Kd == 1
assert Pd == sp.Rational(1, 108)
assert Kd > Kc and Pd > Pc

# Exact symbolic dominance for every positive Q,R.
Q, R = sp.symbols("Q R", positive=True)
gap = sp.factor(Q*(Kd-Kc) + R*(Pd-Pc))
assert (Kd-Kc) > 0 and (Pd-Pc) > 0

# It also dominates the old full-rank endpoint B componentwise.
Kb, Pb = sp.Rational(2, 9), sp.Rational(2, 27783)
assert Kd > Kb and Pd > Pb

# Deliberate-failure test: the finite-set claim remains true only when D is
# deleted from the competitor set.
def winner(r, points):
    vals = [K + r*P for K, P in points]
    m = max(vals)
    return [idx for idx, value in enumerate(vals) if value == m]

A = (sp.Rational(2), sp.Rational(0))
B = (Kb, Pb)
C = (Kc, Pc)
D = (Kd, Pd)
assert winner(25000, [A, C, B]) == [1]
assert winner(25000, [A, C, B, D]) != [1]

result = {
    "schema": "marici.flavor.wp1006.v1",
    "status": "PASS",
    "candidate_scores": {"K": str(Kc), "P": str(Pc)},
    "dominator_scores": {"K": str(Kd), "P": str(Pd)},
    "positive_energy_advantage": str(gap),
    "dominates_wp978_full_rank_endpoint": True,
    "classification": "WP1005 finite-set witness globally falsified; no preparation instrument",
    "remaining_gate": "complete upper score-hull theorem or independently restricted source domain",
}

out = Path(__file__).parents[1] / "results" / "wp1006_third_configuration_global_dominance_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1006 PASS: a same-family Hermitian point strictly dominates the WP1005 candidate globally")

