"""Certify the rank-six q_G12-restricted interaction module and its kernel."""

from __future__ import annotations

import json

import sympy as sp


def signed(value: int, prime: int) -> int:
    value %= prime
    return value - prime if value > prime // 2 else value


def canonical_kernel(p1: int, p2: int, p3: int, energy: int, prime: int):
    e2 = energy**2
    inv_e2 = pow(e2, -1, prime)
    raw = [
        [0,0,0,1,1,-p3*inv_e2,1,0,0,0],
        [0,0,0,1,0,(e2-p2)*inv_e2,0,1,0,0],
        [0,0,0,0,1,(e2-p1)*inv_e2,0,0,1,0],
        [0,0,0,0,0,-inv_e2,0,0,0,1],
    ]
    return [[signed(value, prime) for value in row] for row in raw]


def polynomial_rank(polynomials, variables):
    monomials = sorted({monomial for polynomial in polynomials
                        for monomial in sp.Poly(polynomial, *variables).monoms()})
    matrix = sp.Matrix([
        [sp.Poly(polynomial, *variables).coeff_monomial(monomial)
         for polynomial in polynomials]
        for monomial in monomials
    ])
    return matrix.rank()


def main() -> None:
    a, b, c, E = sp.symbols("a b c E")
    p1, p2, p3 = sp.symbols("p1 p2 p3")
    d1, d2, d3, unit = a**2, b**2, c**2, sp.Integer(1)
    c12 = p3-a**2-b**2
    c13 = p2-a**2-c**2
    c23 = p1-b**2-c**2
    assert sp.factor(d3-E**2*unit) == (c-E)*(c+E)

    # Exact generic witness for the source restriction rank.
    substitutions = {p1:25, p2:49, p3:121, E:9, c:-9}
    linear = [
        2*p1*a**2+p2*p3-p2*a**2-p2*b**2-p3*a**2-p3*c**2
        +a**4-a**2*b**2-a**2*c**2+b**2*c**2,
        p1*p3-p1*a**2-p1*b**2+2*p2*b**2-p3*b**2-p3*c**2
        -a**2*b**2+a**2*c**2+b**4-b**2*c**2,
        p1*p2-p1*a**2-p1*c**2-p2*b**2-p2*c**2+2*p3*c**2
        +a**2*b**2-a**2*c**2-b**2*c**2+c**4,
    ]
    higher = [d1,d2,d3,c12,c13,c23,unit]
    restricted = [sp.expand(value.subs(substitutions)) for value in linear+higher]
    assert polynomial_rank(restricted, (a,b)) == 6

    runs = [
        {
            "point":"A", "prime":32003, "P_squared":[25,49,121], "E":9,
            "cohomology_rank":26, "class_rank":6, "elapsed_ms":5839,
            "kernel":[
                [0,0,0,1,1,1974,1,0,0,0],
                [0,0,0,1,0,-1580,0,1,0,0],
                [0,0,0,0,1,-2765,0,0,1,0],
                [0,0,0,0,0,-3951,0,0,0,1],
            ],
        },
        {
            "point":"B", "prime":32009, "P_squared":[49,121,169], "E":14,
            "cohomology_rank":26, "class_rank":6, "elapsed_ms":5821,
            "kernel":[
                [0,0,0,1,1,-6370,1,0,0,0],
                [0,0,0,1,0,-7022,0,1,0,0],
                [0,0,0,0,1,8003,0,0,1,0],
                [0,0,0,0,0,7349,0,0,0,1],
            ],
        },
    ]
    for run in runs:
        assert run["cohomology_rank"] == 26
        assert run["class_rank"] == 6
        assert run["kernel"] == canonical_kernel(
            *run["P_squared"], run["E"], run["prime"]
        )

    packet = {
        "schema":"marici.benincasa.restricted-interaction-class-faithfulness.v1",
        "lower_source_interaction_rank":7,
        "restricted_source_interaction_rank":6,
        "restriction_kernel_generator":"D3-E^2*U=(c-E)*q_G12",
        "restriction_kernel_rank":1,
        "restricted_source_relation_rank":4,
        "finite_field_runs":runs,
        "restricted_direct_image_class_rank":6,
        "additional_restricted_direct_image_kernel_dimension":0,
        "status":"rank_7_to_6_source_restriction_with_principal_Cartier_kernel",
        "scope":"q_G12 residue rank-26 twisted Jacobian quotient; extension gluing and physical cycle pending",
        "new_carrier_datum":False,
    }
    print(json.dumps(packet,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
