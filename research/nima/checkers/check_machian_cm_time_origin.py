#!/usr/bin/env python3
"""Exact affine-covariance check for CM-memory retarded-time selection."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def preferred_time(k, p):
    p2 = dot(p, p)
    if p2 == 0:
        raise ZeroDivisionError("zero momentum change does not select a time origin")
    return 2 * dot(k, p) / p2


def shift(k, p, a):
    return tuple(ki - a * pi / 2 for ki, pi in zip(k, p))


samples = [
    ((Fraction(1), Fraction(2), Fraction(3)), (Fraction(2), Fraction(-1), Fraction(4)), Fraction(5, 3)),
    ((Fraction(-3, 2), Fraction(7, 5)), (Fraction(4, 7), Fraction(9, 2)), Fraction(-11, 6)),
    ((Fraction(0), Fraction(5), Fraction(-2)), (Fraction(3), Fraction(0), Fraction(1)), Fraction(13, 9)),
]

rows = []
for k, p, a in samples:
    u = preferred_time(k, p)
    ks = shift(k, p, a)
    us = preferred_time(ks, p)
    residual = shift(k, p, u)
    residual_shifted = shift(ks, p, us)
    assert us == u - a
    assert dot(residual, p) == 0
    assert residual_shifted == residual
    rows.append({
        "u_star": str(u),
        "shift": str(a),
        "u_star_after_shift": str(us),
        "residual": [str(x) for x in residual],
    })

try:
    preferred_time((Fraction(1),), (Fraction(0),))
except ZeroDivisionError:
    zero_flux_unselected = True
else:
    zero_flux_unselected = False

assert zero_flux_unselected

packet = {
    "schema": "marici.machian-cm-time-origin.v1",
    "status": "pass",
    "source_equations": ["Nichols 2018 (2.28)", "Nichols 2018 (2.29)"],
    "claims": {
        "affine_covariance": "u_star(K-a P/2,P)=u_star(K,P)-a",
        "invariant_residual": "K-u_star P/2 is shift invariant and orthogonal to P",
        "support_gate": "Delta P != 0",
        "scope": "conditional retarded-time origin only; no spatial origin, rotation, local inertia, or Einstein dynamics",
    },
    "samples": rows,
}
encoded = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(encoded.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-cm-time-origin.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "samples": len(rows), "output": str(out)}))
