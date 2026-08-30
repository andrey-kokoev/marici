#!/usr/bin/env python3
"""Exact Poincare-orbit reduction for the Machian-gravity pilot."""

from fractions import Fraction
from itertools import permutations
import hashlib
import json
from pathlib import Path

ETA = (-1, 1, 1, 1)


def dot(x, y):
    return sum((ETA[i] * x[i] * y[i] for i in range(4)), Fraction(0))


def lower(x):
    return tuple(ETA[i] * x[i] for i in range(4))


def wedge(a, p):
    return tuple(tuple(a[mu] * p[nu] - a[nu] * p[mu] for nu in range(4)) for mu in range(4))


def add_matrix(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(4)) for i in range(4))


def centroid(j, p):
    p2 = dot(p, p)
    if p2 == 0:
        raise ZeroDivisionError("null total momentum has no massive centroid projector")
    pl = lower(p)
    return tuple(sum((j[mu][nu] * pl[nu] for nu in range(4)), Fraction(0)) / p2 for mu in range(4))


def transverse(a, p):
    return tuple(a[mu] - p[mu] * dot(a, p) / dot(p, p) for mu in range(4))


def parity(seq):
    inversions = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
    return -1 if inversions % 2 else 1


EPS = {perm: Fraction(parity(perm)) for perm in permutations(range(4))}


def pauli_lubanski(j, p):
    pl = lower(p)
    jl = tuple(tuple(ETA[r] * ETA[s] * j[r][s] for s in range(4)) for r in range(4))
    return tuple(
        sum((EPS.get((mu, nu, rho, sig), 0) * pl[nu] * jl[rho][sig] / 2
             for nu in range(4) for rho in range(4) for sig in range(4)), Fraction(0))
        for mu in range(4)
    )


samples = [
    {
        "p": (Fraction(5), Fraction(1), Fraction(1), Fraction(0)),
        "a": (Fraction(2), Fraction(-1), Fraction(3), Fraction(1, 2)),
        "j": (
            (0, Fraction(2), Fraction(-1), Fraction(3)),
            (Fraction(-2), 0, Fraction(4), Fraction(1)),
            (Fraction(1), Fraction(-4), 0, Fraction(-2)),
            (Fraction(-3), Fraction(-1), Fraction(2), 0),
        ),
    },
    {
        "p": (Fraction(7), Fraction(2), Fraction(-1), Fraction(1)),
        "a": (Fraction(-3, 2), Fraction(5, 3), Fraction(2), Fraction(-4)),
        "j": (
            (0, Fraction(-1), Fraction(5), Fraction(2)),
            (Fraction(1), 0, Fraction(-3), Fraction(4)),
            (Fraction(-5), Fraction(3), 0, Fraction(1)),
            (Fraction(-2), Fraction(-4), Fraction(-1), 0),
        ),
    },
]

rows = []
for sample in samples:
    p, a, j = sample["p"], sample["a"], sample["j"]
    x = centroid(j, p)
    jp = add_matrix(j, wedge(a, p))
    xp = centroid(jp, p)
    aperp = transverse(a, p)
    assert xp == tuple(x[i] + aperp[i] for i in range(4))
    assert dot(x, p) == 0
    assert dot(aperp, p) == 0
    assert pauli_lubanski(jp, p) == pauli_lubanski(j, p)
    rows.append({
        "p_squared": str(dot(p, p)),
        "centroid": [str(v) for v in x],
        "translation_transverse": [str(v) for v in aperp],
        "pauli_lubanski": [str(v) for v in pauli_lubanski(j, p)],
    })

try:
    centroid(
        ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)),
        (Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
    )
except ZeroDivisionError:
    null_gate = True
else:
    null_gate = False
assert null_gate

packet = {
    "schema": "marici.machian-poincare-frame-reduction.v1",
    "status": "pass",
    "claims": {
        "centroid_covariance": "X(J+a wedge P,P)=X(J,P)+a-P(a dot P)/P^2",
        "centroid_orthogonality": "X dot P=0",
        "translation_invariant_spin": "W(J+a wedge P,P)=W(J,P)",
        "support_gate": "P^2 != 0",
        "scope": "kinematic Poincare-orbit reduction; not a derivation of inertia or Einstein dynamics",
    },
    "samples": rows,
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-poincare-frame-reduction.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "samples": len(rows), "output": str(out)}))
