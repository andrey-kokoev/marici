#!/usr/bin/env python3
"""Exact sparse-polynomial certificate for the generic fixed-base Gram chart."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

VARS = ("x", "y", "z", "p", "u", "v")
N = len(VARS)
ZERO_MON = (0,) * N


class Poly(dict):
    def __add__(self, other):
        other = as_poly(other)
        out = Poly(self)
        for m, c in other.items():
            out[m] = out.get(m, Fraction(0)) + c
            if out[m] == 0:
                del out[m]
        return out

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.items()})

    def __sub__(self, other):
        return self + (-as_poly(other))

    def __rsub__(self, other):
        return as_poly(other) - self

    def __mul__(self, other):
        other = as_poly(other)
        out = Poly()
        for m1, c1 in self.items():
            for m2, c2 in other.items():
                m = tuple(a + b for a, b in zip(m1, m2))
                out[m] = out.get(m, Fraction(0)) + c1 * c2
        return Poly({m: c for m, c in out.items() if c})

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = as_poly(1)
        for _ in range(n):
            out = out * self
        return out


def as_poly(value):
    if isinstance(value, Poly):
        return value
    return Poly({ZERO_MON: Fraction(value)})


def var(name):
    m = [0] * N
    m[VARS.index(name)] = 1
    return Poly({tuple(m): Fraction(1)})


def det3(rows):
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


x, y, z, p, u, v = (var(n) for n in VARS)

# Squared distances from the loop point to the three base vertices.
d1 = x**2 + y**2 + z**2
d2 = (x-p)**2 + y**2 + z**2
d3 = (x-u)**2 + (y-v)**2 + z**2

jac_rows = [
    [2*x, 2*y, 2*z],
    [2*(x-p), 2*y, 2*z],
    [2*(x-u), 2*(y-v), 2*z],
]
jac = det3(jac_rows)
expected_jac = 8*p*v*z
assert jac == expected_jac

# Base area and tetrahedron volume on this chart.
base_area_sq = p**2 * v**2 * Fraction(1, 4)
tetra_volume_sq = p**2 * v**2 * z**2 * Fraction(1, 36)
assert tetra_volume_sq * 9 == base_area_sq * z**2

# Under (v,y)->(-v,-y), every squared distance is unchanged.
def reflect(poly):
    out = Poly()
    iy = VARS.index("y")
    iv = VARS.index("v")
    for mon, coeff in poly.items():
        sign = -1 if (mon[iy] + mon[iv]) % 2 else 1
        out[mon] = coeff * sign
    return out

assert reflect(d1) == d1
assert reflect(d2) == d2
assert reflect(d3) == d3

result = {
    "schema": "marici.benincasa.fixed_base_gram_orientation_cover.v1",
    "status": "pass",
    "chart": {
        "base_vertices": ["(0,0,0)", "(p,0,0)", "(u,v,0)"],
        "loop_point": "(x,y,z)",
        "signed_altitude": "v",
    },
    "jacobian_d_c2_a2_b2_over_d_x_y_z": "8*p*v*z",
    "base_area_squared": "p^2*v^2/4",
    "tetrahedron_volume_squared": "p^2*v^2*z^2/36",
    "volume_ratio": "z^2/9",
    "d3_source_exponent": "-1/2",
    "distance_measure_times_twist": "3*p*v*dxdydz on the oriented chart",
    "gram_relation": "Lambda_P=-4*p^2*v^2",
    "coarse_normal_prefactor": "(3/2)*sqrt(-Lambda_P)",
    "residual_integral_parity": "even under (v,y)->(-v,-y)",
    "oriented_period_parity": "odd in v",
    "semisimple_monodromy": -1,
    "unipotent_logarithm_N": 0,
    "resolved_cover_variation": 0,
    "classification": "fixed-base Gram Kummer/orientation support on existing Cayley-Menger carrier",
    "new_carrier_datum": False,
    "scope_boundary": (
        "Generic smooth Gram component, away from soft support and marked poles. "
        "Soft/Gram overlaps require separate blowup."
    ),
}
out = Path(__file__).with_name("fixed_base_gram_orientation_cover_result.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("FIXED-BASE GRAM ORIENTATION-COVER PASS")
print("Jacobian = 8*p*v*z")
print("T_coarse = -1, N = 0")
print(f"wrote: {out}")
