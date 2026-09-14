#!/usr/bin/env python3
"""Two labelled Picard classes with identical universal cusp invariants."""
import json
from math import gcd
from pathlib import Path

R = Path(__file__).resolve().parents[3]
# Coordinates H,E1,...,E7; intersection diag(1,-1,...,-1).
K = [-3] + [1] * 7
d1 = [3, -3] + [-1] * 6
d2 = [3, -1, -3] + [-1] * 5

def pair(a, b):
    return a[0] * b[0] - sum(x*y for x, y in zip(a[1:], b[1:]))

def primitive(v):
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    return g == 1

minusK = [-x for x in K]
ell = [0, 1, -1] + [0] * 5
checks = {
    "distinct": d1 != d2,
    "both_square_minus_six": pair(d1, d1) == pair(d2, d2) == -6,
    "both_K_orthogonal": pair(K, d1) == pair(K, d2) == 0,
    "both_primitive": primitive(d1) and primitive(d2),
    "same_minus_K_mod_two": all((d1[i]-minusK[i]) % 2 == 0 and (d2[i]-minusK[i]) % 2 == 0 for i in range(8)),
    "detector_distinguishes": pair(ell, d1) == 2 and pair(ell, d2) == -2,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.universal-cusp-invariant-nonuniqueness.v1",
    "passed": True,
    "candidate_columns": {"d_E1": d1, "d_E2": d2},
    "common_invariants": {"square": -6, "K_pairing": 0, "primitive": True, "mod_two": "-K"},
    "distinguishing_functional": "intersection with E1-E2",
    "detector_values": [2, -2],
    "consequence": "universal cusp invariants do not select the labelled Picard-Lefschetz column or orientation",
    "required_output_of_missing_lift": "explicit oriented Picard column for each based braid word",
    "checks": checks,
}
p = R / "research/voevodsky/results/universal_cusp_invariant_nonuniqueness.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "same_universal_invariants": True, "detector_values": [2, -2]}))
