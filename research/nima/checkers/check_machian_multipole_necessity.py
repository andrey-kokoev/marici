#!/usr/bin/env python3
"""Exact Newtonian multipole necessity test for the Machian-gravity lane."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def add_vec(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, v):
    return tuple(c * x for x in v)


def outer(a, b):
    return tuple(tuple(a[i] * b[j] for j in range(3)) for i in range(3))


def quadrupole(points):
    # Q_ij = sum m (3 r_i r_j - |r|^2 delta_ij)
    q = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    for mass, r in points:
        r2 = sum(x * x for x in r)
        rr = outer(r, r)
        for i in range(3):
            for j in range(3):
                q[i][j] += mass * (3 * rr[i][j] - (r2 if i == j else 0))
    return tuple(tuple(row) for row in q)


def invariants(points):
    mass = sum((m for m, _ in points), Fraction(0))
    dipole = (Fraction(0), Fraction(0), Fraction(0))
    for m, r in points:
        dipole = add_vec(dipole, scale(m, r))
    # Static point configurations have zero total angular momentum.
    angular_momentum = (Fraction(0), Fraction(0), Fraction(0))
    return mass, dipole, angular_momentum


def antipodal_pair(axis, radius, pair_mass):
    r = [Fraction(0), Fraction(0), Fraction(0)]
    r[axis] = Fraction(radius)
    r = tuple(r)
    return [(pair_mass / 2, r), (pair_mass / 2, tuple(-x for x in r))]


# Same monopole, dipole and angular momentum; different quadrupole/tidal data.
a = antipodal_pair(0, 1, Fraction(1))
b = antipodal_pair(1, 1, Fraction(1))
assert invariants(a) == invariants(b)
qa, qb = quadrupole(a), quadrupole(b)
assert qa != qb
assert sum(qa[i][i] for i in range(3)) == 0
assert sum(qb[i][i] for i in range(3)) == 0

# A generic global anisotropy has a simple quadrupole spectrum and hence
# selects three unoriented principal axes (up to signs and ordering).
triaxial = (
    antipodal_pair(0, 1, Fraction(1, 6))
    + antipodal_pair(1, 2, Fraction(1, 3))
    + antipodal_pair(2, 3, Fraction(1, 2))
)
qt = quadrupole(triaxial)
assert all(qt[i][j] == 0 for i in range(3) for j in range(3) if i != j)
eigenvalues = tuple(qt[i][i] for i in range(3))
assert len(set(eigenvalues)) == 3

packet = {
    "schema": "marici.machian-multipole-necessity.v1",
    "status": "pass",
    "claims": {
        "finite_charge_no_go": "equal mass, center of mass and angular momentum do not determine the local tidal tensor",
        "multipole_selector": "a simple-spectrum quadrupole conditionally selects three unoriented principal axes",
        "scope": "exact Newtonian-limit proxy; not a derivation of GR localization or inertia",
    },
    "configuration_a": {
        "invariants": [[str(x) for x in item] if isinstance(item, tuple) else str(item) for item in invariants(a)],
        "quadrupole": [[str(x) for x in row] for row in qa],
    },
    "configuration_b": {
        "invariants": [[str(x) for x in item] if isinstance(item, tuple) else str(item) for item in invariants(b)],
        "quadrupole": [[str(x) for x in row] for row in qb],
    },
    "triaxial_selector": {
        "quadrupole": [[str(x) for x in row] for row in qt],
        "distinct_eigenvalues": [str(x) for x in eigenvalues],
    },
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-multipole-necessity.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))
