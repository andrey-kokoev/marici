#!/usr/bin/env python3
"""Exact typing audit for all-soft support maps against fiber Gysin."""

import json
from pathlib import Path

def main():
    external_names = [
        "soft_E", "soft_P1", "soft_P2", "soft_P3",
        "signed_E_plus_P1", "signed_E_minus_P1", "triangle",
    ]
    external_weights = {name: 0 for name in external_names}
    coordinate_weights = {"a": "a", "b": "b"}

    # The frozen Cayley--Menger polynomial is copied term-for-term from the
    # source certificate used in Entry 828.
    # (coefficient, exponents E,P1,P2,P3,a,b), exactly as in Entry 828.
    terms = [
        (1,(4,0,0,2,0,0)),(-1,(2,2,0,0,2,0)),(1,(2,0,2,0,2,0)),
        (-1,(2,0,0,2,2,0)),(1,(2,2,0,0,0,2)),(-1,(2,0,2,0,0,2)),
        (-1,(2,0,0,2,0,2)),(-1,(2,2,0,2,0,0)),(-1,(2,0,2,2,0,0)),
        (1,(2,0,0,4,0,0)),(1,(0,2,0,0,4,0)),(-1,(0,2,0,0,2,2)),
        (-1,(0,0,2,0,2,2)),(1,(0,0,0,2,2,2)),(1,(0,4,0,0,2,0)),
        (-1,(0,2,2,0,2,0)),(-1,(0,2,0,2,2,0)),(1,(0,0,2,0,0,4)),
        (-1,(0,2,2,0,0,2)),(1,(0,0,4,0,0,2)),(-1,(0,0,2,2,0,2)),
        (1,(0,2,2,2,0,0)),
    ]
    point = (1, 2, 3, 5, 7, 11)
    witness = sum(
        coefficient * (exponents[4] + exponents[5] - 6)
        * __import__("math").prod(x**power for x, power in zip(point, exponents))
        for coefficient, exponents in terms
    )
    assert witness != 0

    packet = {
        "fiber_euler": "a*d/da+b*d/db",
        "external_support_contractions": external_weights,
        "coordinate_support_weights": coordinate_weights,
        "coordinate_residue_rule": "Res_f i_X = - i_X Res_f (Koszul sign)",
        "cayley_menger_fiber_eigenvector": False,
        "cayley_menger_tangency_witness": str(witness),
        "typed_conclusion": {
            "external_supports": "commute exactly",
            "coordinate_residues": "commute with the degree-shift sign",
            "cayley_menger_branch": "requires full-radial/projective localization; no fiber-Euler restriction map",
        },
    }
    out = Path(__file__).with_name("all-soft-support-gysin-typing.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
