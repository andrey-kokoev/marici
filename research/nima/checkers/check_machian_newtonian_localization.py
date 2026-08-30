#!/usr/bin/env python3
"""Exact Newtonian source-to-local tidal localization map."""

from fractions import Fraction
from math import isqrt
import hashlib
import json
from pathlib import Path


def source_jet_at_origin(points):
    """Return Phi, grad Phi, Hess Phi for Phi=-sum m/|x-r|, G=1.

    Coordinates are chosen so every source radius is rational.
    """
    phi = Fraction(0)
    grad = [Fraction(0) for _ in range(3)]
    hess = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    for mass, r in points:
        r2 = sum(v * v for v in r)
        assert r2.denominator == 1
        radius = Fraction(isqrt(r2.numerator))
        assert radius * radius == r2
        phi -= mass / radius
        for i in range(3):
            grad[i] -= mass * r[i] / radius**3
            for j in range(3):
                numerator = 3 * r[i] * r[j] - (r2 if i == j else 0)
                hess[i][j] -= mass * numerator / radius**5
    return phi, tuple(grad), tuple(tuple(row) for row in hess)


def add_affine_to_jet(jet, constant, linear):
    phi, grad, hess = jet
    return phi + constant, tuple(grad[i] + linear[i] for i in range(3)), hess


sources_a = [
    (Fraction(2), (Fraction(3), Fraction(0), Fraction(0))),
    (Fraction(1), (Fraction(0), Fraction(4), Fraction(0))),
]
sources_b = sources_a + [
    (Fraction(3, 2), (Fraction(0), Fraction(0), Fraction(5))),
]

jet_a = source_jet_at_origin(sources_a)
jet_b = source_jet_at_origin(sources_b)

# Both source configurations have the same empty local density germ at the
# origin, yet the remote added source changes local curvature.
assert jet_a[2] != jet_b[2]
assert sum(jet_a[2][i][i] for i in range(3)) == 0
assert sum(jet_b[2][i][i] for i in range(3)) == 0

# Equivalence-principle quotient: constant and uniform-gradient additions
# alter Phi and acceleration but leave tidal curvature unchanged.
affine = add_affine_to_jet(
    jet_b,
    Fraction(17, 3),
    (Fraction(-2), Fraction(5, 7), Fraction(11, 4)),
)
assert affine[0] != jet_b[0]
assert affine[1] != jet_b[1]
assert affine[2] == jet_b[2]

packet = {
    "schema": "marici.machian-newtonian-localization.v1",
    "status": "pass",
    "map": "rho_global -> J^2 Phi|_U -> J^2 Phi/J^1_affine = tidal Hessian",
    "claims": {
        "remote_sensitivity": "remote source change with unchanged empty local density germ changes the local tidal tensor",
        "equivalence_principle_quotient": "constant and uniform-gradient potential jets are removed; Hessian is invariant",
        "vacuum_constraint": "trace Hessian=0 at the source-free observation point",
        "scope": "Newtonian weak-field localization only; no nonlinear Einstein or inertial-mass derivation",
    },
    "jet_a": {
        "potential": str(jet_a[0]),
        "gradient": [str(v) for v in jet_a[1]],
        "hessian": [[str(v) for v in row] for row in jet_a[2]],
    },
    "jet_b": {
        "potential": str(jet_b[0]),
        "gradient": [str(v) for v in jet_b[1]],
        "hessian": [[str(v) for v in row] for row in jet_b[2]],
    },
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-newtonian-localization.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))
