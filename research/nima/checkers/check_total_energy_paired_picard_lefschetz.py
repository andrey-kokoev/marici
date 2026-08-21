#!/usr/bin/env python3
"""Exact local audit of the paired total-energy Picard--Lefschetz nodes."""

import hashlib
import json
from pathlib import Path

import sympy as sp


def main():
    x, y, e, t = sp.symbols("x y E t", nonzero=True)
    z = e - x - y
    h = x**2 + y**2 - z**2
    f = sp.expand(x**2 * t**4 - h * t**2 + y**2)
    p = x * t**2 + y

    assert sp.factor(f.subs(e, 0)) == p**2
    deformation = sp.factor(sp.diff(f, e).subs(e, 0))
    assert deformation == -2 * t**2 * (x + y)

    # On either node t^2=-y/x, the first E-jet is nonzero on the generic
    # locus x*y*(x+y) != 0.
    node_jet = sp.factor(deformation.subs(t**2, -y / x))
    assert node_jet == 2 * y * (x + y) / x

    # P has two simple roots away from x*y=0; t -> -t exchanges them.
    p_t = sp.diff(p, t)
    simple_root_test = sp.factor(p_t**2).subs(t**2, -y / x)
    assert sp.factor(simple_root_test) == -4 * x * y
    assert sp.expand(p.subs(t, -t) - p) == 0

    result = {
        "schema": "marici.nima.total_energy_paired_picard_lefschetz.v1",
        "generic_locus": "x*y*(x+y)!=0",
        "identities": {
            "E0_boundary": "F(t)|E=0=(x*t^2+y)^2",
            "node_equation": "x*t^2+y=0",
            "node_count": 2,
            "node_exchange": "t -> -t",
            "first_E_jet": "2*y*(x+y)/x at either node",
            "root_derivative_square": "-4*x*y",
        },
        "established_local_conclusion": "two exchanged ordinary nodes with primitive first-order E smoothing",
        "picard_lefschetz_consequence": "the width-two elliptic monodromy is locally compatible with two equal Dehn-twist contributions",
        "not_established": [
            "the integral ambient vanishing-root class",
            "its coordinates along (e6,v_alg)",
            "the physical Cayley-Menger contour normalization",
        ],
        "next_falsifier": "compute the two ambient thimble classes in the integral degree-two del Pezzo Picard lattice and compare them modulo 2",
    }

    out = Path(__file__).parents[1] / "results" / "total-energy-paired-picard-lefschetz.json"
    payload = out.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
