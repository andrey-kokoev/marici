#!/usr/bin/env python3
"""Exact local tidal-frame stabilizer census for the Machian lane."""

from fractions import Fraction
from itertools import permutations, product
import hashlib
import json
from pathlib import Path


def parity(p):
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def signed_permutation(perm, signs):
    return tuple(tuple(Fraction(signs[i] if perm[i] == j else 0)
                       for j in range(3)) for i in range(3))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def mul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(3)), Fraction(0))
                       for j in range(3)) for i in range(3))


def diag(values):
    return tuple(tuple(Fraction(values[i] if i == j else 0) for j in range(3))
                 for i in range(3))


def stabilizer_signed_permutations(eigenvalues):
    e = diag(eigenvalues)
    keep = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            determinant = parity(perm) * signs[0] * signs[1] * signs[2]
            if determinant != 1:
                continue
            r = signed_permutation(perm, signs)
            if mul(mul(r, e), transpose(r)) == e:
                keep.append((perm, signs))
    return keep


def lie_stabilizer_dimension(eigenvalues):
    # For antisymmetric Omega, [Omega,E]_ij=(lambda_j-lambda_i)Omega_ij.
    return sum(eigenvalues[i] == eigenvalues[j]
               for i in range(3) for j in range(i + 1, 3))


generic = (Fraction(-3), Fraction(1), Fraction(2))
axial = (Fraction(2), Fraction(-1), Fraction(-1))
flat = (Fraction(0), Fraction(0), Fraction(0))

generic_discrete = stabilizer_signed_permutations(generic)
axial_discrete = stabilizer_signed_permutations(axial)

assert sum(generic) == sum(axial) == 0
assert lie_stabilizer_dimension(generic) == 0
assert len(generic_discrete) == 4  # orientation-preserving sign flips
assert lie_stabilizer_dimension(axial) == 1
assert len(axial_discrete) == 8
assert lie_stabilizer_dimension(flat) == 3

packet = {
    "schema": "marici.machian-local-tidal-frame.v1",
    "status": "pass",
    "claims": {
        "generic_local_selection": "a simple-spectrum local tidal tensor fixes a spatial eigenframe up to four orientation-preserving sign flips and has no continuous SO(3) stabilizer",
        "axial_residual": "a double eigenvalue retains one continuous rotation",
        "flat_residual": "zero tidal curvature retains the full three-dimensional rotation algebra",
        "interpretation": "a separate exterior frame map is unnecessary on generic local-curvature strata and underdetermined on symmetric strata unless an operational relational readout is added",
        "scope": "spatial triad along an already chosen observer/worldline; not a full Lorentz Cartan-frame theorem",
    },
    "generic": {"eigenvalues": [str(x) for x in generic], "discrete_stabilizer_size": len(generic_discrete), "lie_stabilizer_dimension": 0},
    "axial": {"eigenvalues": [str(x) for x in axial], "discrete_stabilizer_size": len(axial_discrete), "lie_stabilizer_dimension": 1},
    "flat": {"eigenvalues": [str(x) for x in flat], "lie_stabilizer_dimension": 3},
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-local-tidal-frame.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))
