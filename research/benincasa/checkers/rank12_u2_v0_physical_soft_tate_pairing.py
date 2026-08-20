#!/usr/bin/env python3
"""Physical soft-normal pullback of the second-center nodal Tate line."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/benincasa/results/rank12-u2-v0-physical-soft-tate-pairing.json"
eta, B, alpha, gamma = sp.symbols("eta B alpha gamma")

# Source projective chart with X1 fixed, and the canonical normal slice to
# the physical soft divisor X2=0: hold X1=X3=1 and vary X2=eta.
X1 = sp.Integer(1)
X2 = eta
X3 = sp.Integer(1)
u = sp.cancel((X1 + X2 + X3) / X1)
v = sp.cancel((X1 + X2 - X3) / X1)
p = sp.expand(u - 2)
q = sp.expand(v)
s = sp.cancel(q / p)

assert p == eta
assert q == eta
assert s == 1

# Entry 1100's normalized node is XY=p*U with
# U|_{p=0,T=0}=-16*s*(B-1).  The irrelevant nonzero unit -16 does not alter
# the vanishing-cycle multiplicity or orientation line.
t_reduced = sp.expand(p * s * (B - 1))
assert sp.simplify(t_reduced - eta * (B - 1)) == 0
normal_derivative = sp.diff(t_reduced, eta).subs(eta, 0)
assert normal_derivative == B - 1

# Audit a general first-order tangential lift.  It belongs to a different
# iterated corner exactly when its q-normal coefficient vanishes.
X1g = 1 + alpha * eta
X2g = eta
X3g = 1 + gamma * eta
ug = sp.cancel((X1g + X2g + X3g) / X1g)
vg = sp.cancel((X1g + X2g - X3g) / X1g)
pg_lead = sp.diff(ug - 2, eta).subs(eta, 0)
qg_lead = sp.diff(vg, eta).subs(eta, 0)
assert sp.simplify(pg_lead - (1 + gamma - alpha)) == 0
assert sp.simplify(qg_lead - (1 + alpha - gamma)) == 0

result = {
    "schema": "marici.benincasa.rank12_u2_v0_physical_soft_tate_pairing.v1",
    "status": "passed",
    "center": {"X1": "1", "X2": "0", "X3": "1", "u": "2", "v": "0"},
    "physical_normal_slice": {"X1": "1", "X2": "eta", "X3": "1", "eta": "eta>0"},
    "rees_pullback": {"p": str(p), "q": str(q), "s": str(s)},
    "node_smoothing_up_to_source_unit": str(t_reduced),
    "normal_derivative": str(normal_derivative),
    "genericity_locus": "B-1 != 0",
    "soft_normal_valuation": 1,
    "gysin_coefficient": 1,
    "coefficient_object": "rank-one anti-invariant Tate vanishing-cycle line",
    "deck_character": -1,
    "pairing": "nonzero up to the frozen global orientation sign",
    "general_tangential_lift": {
        "X1": "1+alpha*eta",
        "X2": "eta",
        "X3": "1+gamma*eta",
        "p_leading_coefficient": str(pg_lead),
        "q_leading_coefficient": str(qg_lead),
        "deeper_corner_condition": "1+alpha-gamma=0"
    },
    "scope": "Canonical soft specialization means X2->0 at fixed X1,X3. Tangentially moving lifts have varying normalization and the locus 1+alpha-gamma=0 belongs to the separately labelled q=0 corner.",
    "conclusion": "The physical X2-soft nearby-cycle map activates the second-center nodal Tate line with multiplicity one on the generic conductor locus.",
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
