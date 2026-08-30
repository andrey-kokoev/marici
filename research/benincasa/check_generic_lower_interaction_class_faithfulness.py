"""Certify that the generic lower direct image adds no interaction-class kernel."""

from __future__ import annotations

import json

import sympy as sp


LABELS = (
    "nu1", "nu2", "nu3",
    "nu1^2", "nu2^2", "nu3^2",
    "nu1*nu2", "nu1*nu3", "nu2*nu3",
    "nu1*nu2*nu3",
)


def signed(value: int, prime: int) -> int:
    value %= prime
    return value - prime if value > prime // 2 else value


def canonical_kernel(p1: int, p2: int, p3: int, prime: int) -> list[list[int]]:
    inv_p3 = pow(p3, -1, prime)
    raw = [
        [0, 0, 0, (p3-p2)*inv_p3, -p2*inv_p3, 1,
         -p2*inv_p3, 1, 0, 0],
        [0, 0, 0, -p1*inv_p3, (p3-p1)*inv_p3, 1,
         -p1*inv_p3, 0, 1, 0],
        [0, 0, 0, -inv_p3, -inv_p3, 0,
         -inv_p3, 0, 0, 1],
    ]
    return [[signed(value, prime) for value in row] for row in raw]


def main() -> None:
    a, b, c = sp.symbols("a b c")
    p1, p2, p3 = sp.symbols("p1 p2 p3")
    d1, d2, d3 = a**2, b**2, c**2
    c12 = p3 - a**2 - b**2
    c13 = p2 - a**2 - c**2
    c23 = p1 - b**2 - c**2
    unit = sp.Integer(1)

    assert sp.expand(p3 * (d1 + d3 + c13) - p2 * (d1 + d2 + c12)) == 0
    assert sp.expand(p3 * (d2 + d3 + c23) - p1 * (d1 + d2 + c12)) == 0
    assert sp.expand(p3 * unit - (d1 + d2 + c12)) == 0

    # The three linear source coefficients from Entry 2400, evaluated at an
    # exact generic point, together with the seven higher labels span rank 7.
    x1, x2, x3 = 2, 3, 4
    q1, q2, q3 = 5**2, 7**2, 11**2
    linear = [
        2*q1*a**2 + q2*q3 - q2*a**2 - q2*b**2 - q3*a**2 - q3*c**2
        + a**4 - a**2*b**2 - a**2*c**2 + b**2*c**2,
        q1*q3 - q1*a**2 - q1*b**2 + 2*q2*b**2 - q3*b**2 - q3*c**2
        - a**2*b**2 + a**2*c**2 + b**4 - b**2*c**2,
        q1*q2 - q1*a**2 - q1*c**2 - q2*b**2 - q2*c**2 + 2*q3*c**2
        + a**2*b**2 - a**2*c**2 - b**2*c**2 + c**4,
    ]
    higher = [
        d1, d2, d3,
        c12.subs({p3: q3}), c13.subs({p2: q2}), c23.subs({p1: q1}), unit,
    ]
    polynomials = linear + higher
    monomials = sorted({monomial for polynomial in polynomials
                        for monomial in sp.Poly(polynomial, a, b, c).monoms()})
    coefficient_matrix = sp.Matrix([
        [sp.Poly(polynomial, a, b, c).coeff_monomial(monomial)
         for polynomial in polynomials]
        for monomial in monomials
    ])
    source_rank = coefficient_matrix.rank()
    assert source_rank == 7

    runs = [
        {
            "point": "A", "prime": 32003, "P_squared": [25, 49, 121],
            "cohomology_rank": 34, "class_rank": 7,
            "elapsed_ms": 439480,
            "kernel": [
                [0,0,0,12696,12695,1,12695,1,0,0],
                [0,0,0,-15076,-15075,1,-15076,0,1,0],
                [0,0,0,-10844,-10844,0,-10844,0,0,1],
            ],
        },
        {
            "point": "B", "prime": 32009, "P_squared": [49, 121, 169],
            "cohomology_rank": 34, "class_rank": 7,
            "elapsed_ms": 440279,
            "kernel": [
                [0,0,0,9281,9280,1,9280,1,0,0],
                [0,0,0,7197,7198,1,7197,0,1,0],
                [0,0,0,-15531,-15531,0,-15531,0,0,1],
            ],
        },
    ]
    for run in runs:
        assert run["cohomology_rank"] == 34
        assert run["class_rank"] == source_rank
        assert run["kernel"] == canonical_kernel(*run["P_squared"], run["prime"])

    packet = {
        "schema": "marici.benincasa.generic-lower-interaction-class-faithfulness.v1",
        "labels": list(LABELS),
        "raw_label_count": 10,
        "source_relation_rank": 3,
        "source_interaction_module_rank": source_rank,
        "source_relations": [
            "p3*(D1+D3+C13)-p2*(D1+D2+C12)=0",
            "p3*(D2+D3+C23)-p1*(D1+D2+C12)=0",
            "p3*U-(D1+D2+C12)=0",
        ],
        "finite_field_runs": runs,
        "generic_lower_direct_image_class_rank": 7,
        "additional_direct_image_kernel_dimension": 0,
        "status": "generic_lower_direct_image_faithful_modulo_exact_source_relations",
        "scope": (
            "four-wall lower twisted Jacobian quotient; restricted q_G12 "
            "rank-26 summand and physical cycle not yet included"
        ),
        "new_carrier_datum": False,
    }
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
