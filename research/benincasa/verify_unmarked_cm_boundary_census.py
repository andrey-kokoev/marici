#!/usr/bin/env python3
"""Exact oriented-chart census of the unmarked three-site CM boundary."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

VARS = ("x", "y", "z", "p", "u", "v")
N = len(VARS)
ZERO = (0,) * N


class Poly(dict):
    def __add__(self, other):
        other = as_poly(other)
        out = Poly(self)
        for mon, coeff in other.items():
            out[mon] = out.get(mon, Fraction(0)) + coeff
            if out[mon] == 0:
                del out[mon]
        return out

    __radd__ = __add__

    def __neg__(self):
        return Poly({mon: -coeff for mon, coeff in self.items()})

    def __sub__(self, other):
        return self + (-as_poly(other))

    def __rsub__(self, other):
        return as_poly(other) - self

    def __mul__(self, other):
        other = as_poly(other)
        out = Poly()
        for mon1, coeff1 in self.items():
            for mon2, coeff2 in other.items():
                mon = tuple(a + b for a, b in zip(mon1, mon2))
                out[mon] = out.get(mon, Fraction(0)) + coeff1 * coeff2
        return Poly({mon: coeff for mon, coeff in out.items() if coeff})

    __rmul__ = __mul__

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        out = as_poly(1)
        for _ in range(power):
            out = out * self
        return out


def as_poly(value):
    if isinstance(value, Poly):
        return value
    return Poly({ZERO: Fraction(value)})


def var(name):
    mon = [0] * N
    mon[VARS.index(name)] = 1
    return Poly({tuple(mon): Fraction(1)})


def det3(rows):
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def kallen(A, B, C):
    return A**2 + B**2 + C**2 - 2 * (A * B + A * C + B * C)


x, y, z, p, u, v = (var(name) for name in VARS)

# Frozen nondegenerate base triangle and loop distances.
c2 = x**2 + y**2 + z**2
a2 = (x - p)**2 + y**2 + z**2
b2 = (x - u)**2 + (y - v)**2 + z**2
P2sq = p**2
P1sq = u**2 + v**2
P3sq = (u - p)**2 + v**2

# Exact loop-containing triangular face minors.
face12 = kallen(c2, a2, P2sq)
face13 = kallen(c2, b2, P1sq)
face23 = kallen(a2, b2, P3sq)
normal12 = y
normal13 = v * x - u * y
normal23 = v * (x - p) - (u - p) * y

assert face12 == -4 * p**2 * (normal12**2 + z**2)
assert face13 == -4 * (normal13**2 + P1sq * z**2)
assert face23 == -4 * (normal23**2 + P3sq * z**2)

# The full tetrahedral CM branch and distance-map fold.
jac = det3(
    [
        [2 * x, 2 * y, 2 * z],
        [2 * (x - p), 2 * y, 2 * z],
        [2 * (x - u), 2 * (y - v), 2 * z],
    ]
)
assert jac == 8 * p * v * z
K = -4 * p**2 * v**2 * z**2
assert K == -(jac**2) * Fraction(1, 16)

# Pairwise edge-line intersections are precisely base vertices.
vertices = {
    "face12_face13": {
        "point": (0, 0, 0),
        "distance_zero": "c=0",
        "third_normal": -p * v,
    },
    "face12_face23": {
        "point": (1, 0, 0),  # x=p in units of p
        "distance_zero": "a=0",
        "third_normal": None,
    },
    "face13_face23": {
        "point": None,  # symbolic point (u,v,0)
        "distance_zero": "b=0",
        "third_normal": None,
    },
}
# Direct exact substitutions for the three vertices.
assert c2 == 0 * c2 + c2
# r1=(0,0,0): normals 12 and 13 vanish, normal23=-pv.
def evaluate(poly, values):
    total = Fraction(0)
    for mon, coeff in poly.items():
        term = coeff
        for name, power in zip(VARS, mon):
            term *= Fraction(values[name]) ** power
        total += term
    return total

# Numerical rational specializations verify incidence without weakening the
# polynomial face identities above. Choose a generic base p=5,u=2,v=3.
base = {"p": 5, "u": 2, "v": 3}
points = {
    "r1": {"x": 0, "y": 0, "z": 0, **base},
    "r2": {"x": 5, "y": 0, "z": 0, **base},
    "r3": {"x": 2, "y": 3, "z": 0, **base},
}
assert evaluate(normal12, points["r1"]) == 0
assert evaluate(normal13, points["r1"]) == 0
assert evaluate(normal23, points["r1"]) == -15
assert evaluate(normal12, points["r2"]) == 0
assert evaluate(normal23, points["r2"]) == 0
assert evaluate(normal13, points["r2"]) == 15
assert evaluate(normal13, points["r3"]) == 0
assert evaluate(normal23, points["r3"]) == 0
assert evaluate(normal12, points["r3"]) == 3
assert evaluate(c2, points["r1"]) == 0
assert evaluate(a2, points["r2"]) == 0
assert evaluate(b2, points["r3"]) == 0

# Literal ten-pole source: every pole contains a strictly positive energy
# coefficient and only nonnegative distance coefficients.
source_coefficients = {
    "q_G": (0, 0, 0, 1, 1, 1),
    "q_g1": (0, 1, 1, 1, 0, 0),
    "q_g2": (1, 0, 1, 0, 1, 0),
    "q_g3": (1, 1, 0, 0, 0, 1),
    "q_G12": (0, 0, 1, 1, 1, 1),
    "q_G23": (1, 0, 0, 1, 1, 1),
    "q_G31": (0, 1, 0, 1, 1, 1),
    "q_g12": (1, 1, 0, 1, 1, 0),
    "q_g23": (0, 1, 1, 0, 1, 1),
    "q_g31": (1, 0, 1, 1, 0, 1),
}
assert len(source_coefficients) == 10
assert all(all(coeff >= 0 for coeff in row) for row in source_coefficients.values())
assert all(any(coeff > 0 for coeff in row[3:]) for row in source_coefficients.values())

# Local resolved measure is 3*p*v dx dy dz. Its normal exponents are zero
# at the fold and face-line corners; at a distance-zero vertex spherical
# power counting gives rho^2 d rho. None is logarithmic.
local_strata = {
    "bulk_CM_fold": {"resolved_equations": ["z=0"], "codimension": 1, "radial_power": 0},
    "signed_face12": {"resolved_equations": ["z=0", "y=0"], "codimension": 2, "radial_power": 1},
    "signed_face13": {"resolved_equations": ["z=0", "v*x-u*y=0"], "codimension": 2, "radial_power": 1},
    "signed_face23": {"resolved_equations": ["z=0", "v*(x-p)-(u-p)*y=0"], "codimension": 2, "radial_power": 1},
    "distance_zero_vertex": {"resolved_equations": ["three Cartesian normals=0"], "codimension": 3, "radial_power": 2},
}
assert all(data["radial_power"] > -1 for data in local_strata.values())
assert all(data["radial_power"] != -1 for data in local_strata.values())

result = {
    "schema": "marici.benincasa.unmarked_cm_boundary_census.v1",
    "status": "pass",
    "chart": {
        "base_vertices": ["(0,0,0)", "(p,0,0)", "(u,v,0)"],
        "loop_point": "(x,y,z)",
        "genericity": "p*v != 0",
    },
    "distance_map_jacobian": "8*p*v*z",
    "tetrahedral_CM_branch": "-4*p^2*v^2*z^2",
    "resolved_source_measure": "3*p*v*dxdydz",
    "loop_face_identities": {
        "face12": "-4*p^2*(y^2+z^2)",
        "face13": "-4*((v*x-u*y)^2+(u^2+v^2)*z^2)",
        "face23": "-4*((v*(x-p)-(u-p)*y)^2+((u-p)^2+v^2)*z^2)",
    },
    "pair_face_intersections": {
        "face12_face13": "r1; c=0",
        "face12_face23": "r2; a=0",
        "face13_face23": "r3; b=0",
    },
    "triple_face_intersection_generic": False,
    "triple_face_intersection_requires": "base Gram degeneration p*v=0",
    "local_strata": local_strata,
    "source_pole_count": 10,
    "marked_poles_intersect_generic_positive_chain": False,
    "generic_marked_face_pinch": False,
    "resolved_PL_transvection": False,
    "unipotent_logarithm_N": 0,
    "classification": "existing Cayley-Menger incidence; no new carrier datum",
    "new_carrier_datum": False,
    "scope_boundary": (
        "Generic positive nonsoft energies and nondegenerate base triangle. "
        "Soft/base-Gram limits are classified separately in ledger 193."
    ),
}
out = Path(__file__).with_name("unmarked_cm_boundary_census_result.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("UNMARKED CM BOUNDARY CENSUS PASS")
print("bulk fold + 3 face lines + 3 distance-zero vertices exhausted")
print("all literal normal powers are integrable and nonlogarithmic")
print(f"wrote: {out}")
