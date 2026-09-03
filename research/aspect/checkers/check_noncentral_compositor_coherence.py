#!/usr/bin/env python3
"""Finite crossed-system checks for G=C2 and attachment automorphisms S3."""

import itertools
import json
from pathlib import Path

PERMS = tuple(itertools.permutations(range(3)))
ID = (0, 1, 2)
G = (0, 1)


def mul(p, q): return tuple(p[q[i]] for i in range(3))
def inv(p): return tuple(p.index(i) for i in range(3))
def inner(a, x): return mul(mul(a, x), inv(a))
def equal_maps(left, right): return all(left(x) == right(x) for x in PERMS)

def valid_crossed(alpha, c):
    compatibility = all(equal_maps(lambda x, g=g, h=h: alpha[g](alpha[h](x)), lambda x, g=g, h=h: inner(c[g, h], alpha[(g + h) % 2](x))) for g in G for h in G)
    cocycle = all(mul(c[g, h], c[(g + h) % 2, k]) == mul(alpha[g](c[h, k]), c[g, (h + k) % 2]) for g in G for h in G for k in G)
    normalized = equal_maps(alpha[0], lambda x: x) and all(c[0, g] == ID and c[g, 0] == ID for g in G)
    return compatibility, cocycle, normalized


def gauge(alpha, c, b):
    alpha_new = {g: (lambda x, g=g: inner(b[g], alpha[g](x))) for g in G}
    c_new = {(g, h): mul(mul(mul(b[g], alpha[g](b[h])), c[g, h]), inv(b[(g + h) % 2])) for g in G for h in G}
    return alpha_new, c_new

alpha_strict = {g: (lambda x: x) for g in G}
c_strict = {(g, h): ID for g in G for h in G}
transposition = (1, 0, 2)
c_false = dict(c_strict)
c_false[1, 1] = transposition
false_compatibility, false_cocycle, false_normalized = valid_crossed(alpha_strict, c_false)

cycle = (1, 2, 0)
b = {0: ID, 1: cycle}
alpha_gauged, c_gauged = gauge(alpha_strict, c_strict, b)
gauged_valid = valid_crossed(alpha_gauged, c_gauged)
b_inverse = {g: inv(b[g]) for g in G}
alpha_returned, c_returned = gauge(alpha_gauged, c_gauged, b_inverse)
returned_valid = valid_crossed(alpha_returned, c_returned)

checks = {
    "strict_system_is_valid": all(valid_crossed(alpha_strict, c_strict)),
    "cocycle_only_false_fixture_is_normalized": false_normalized,
    "cocycle_only_false_fixture_passes_associativity": false_cocycle,
    "cocycle_only_false_fixture_fails_action_compatibility": not false_compatibility,
    "gauged_system_satisfies_both_equations": all(gauged_valid),
    "gauge_produces_nonidentity_compositor": c_gauged[1, 1] != ID,
    "gauge_produces_nontrivial_inner_action": any(alpha_gauged[1](x) != x for x in PERMS),
    "inverse_gauge_returns_identity_compositor": all(value == ID for value in c_returned.values()),
    "inverse_gauge_returns_trivial_action": all(equal_maps(alpha_returned[g], lambda x: x) for g in G),
    "returned_system_remains_valid": all(returned_valid),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.noncentral-compositor-coherence.v1", "status": "passed", "checks": checks, "false_fixture": {"compatibility": false_compatibility, "cocycle": false_cocycle}, "gauged_c_11": c_gauged[1, 1], "claim_boundary": "One-object finite fixture G=C2, A=S3; general attachment groupoids remain outside scope."}
output = Path(__file__).parents[1] / "results" / "noncentral_compositor_coherence.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "gauged_c_11": c_gauged[1, 1]}, sort_keys=True))
