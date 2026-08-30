#!/usr/bin/env python3
"""Exact metric/Cut invariance test for Marici entanglement entropy."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))),
                           Fraction(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def det2(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def reduced_invariants(amplitude):
    gram = mul(amplitude, transpose(amplitude))
    norm = trace(gram)
    rho = scale(Fraction(1, 1) / norm, gram)
    return trace(rho), det2(rho), rho


a = (
    (Fraction(2), Fraction(-1)),
    (Fraction(3), Fraction(4)),
)
rot_l = (
    (Fraction(3, 5), Fraction(-4, 5)),
    (Fraction(4, 5), Fraction(3, 5)),
)
rot_r = (
    (Fraction(5, 13), Fraction(-12, 13)),
    (Fraction(12, 13), Fraction(5, 13)),
)
reflection = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(-1)),
)

base = reduced_invariants(a)
transformed = reduced_invariants(mul(mul(rot_l, a), transpose(rot_r)))
reflected = reduced_invariants(mul(reflection, a))
rescaled = reduced_invariants(scale(Fraction(-7, 3), a))

# In dimension two, trace and determinant determine the unordered spectrum.
assert base[:2] == transformed[:2]
assert base[:2] == reflected[:2]
assert base[:2] == rescaled[:2]
assert base[0] == 1

# Bell diagonal specialization recovers the Schmidt weights r^2/(r^2+s^2).
r, s = Fraction(3), Fraction(4)
bell = ((r, 0), (0, s))
_, bell_det, bell_rho = reduced_invariants(bell)
assert bell_rho == ((Fraction(9, 25), 0), (0, Fraction(16, 25)))
assert bell_det == Fraction(144, 625)

packet = {
    "schema": "marici.shannon-metric-cut-invariance.v1",
    "status": "pass",
    "claims": {
        "basis_invariance": "the reduced-state spectrum is invariant under independent rational orthogonal changes of wing bases",
        "orientation_invariance": "a transverse orientation reversal preserves the spectrum",
        "projective_invariance": "overall nonzero amplitude rescaling preserves the spectrum",
        "minimal_data": "a Cut bipartition plus positive wing metrics suffices for canonical Schmidt probabilities; analyzer choices and Hodge orientation are unnecessary",
        "remaining_gate": "physical Cut and its compatibility with the source-derived positive metric must still be established",
    },
    "generic_trace": str(base[0]),
    "generic_determinant": str(base[1]),
    "bell_weights": ["9/25", "16/25"],
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "shannon-metric-cut-invariance.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))
