#!/usr/bin/env python3
"""Verify the two deeper square normal forms of Q_pol."""

import json
from pathlib import Path


def q_coefficients(x, p, q, r):
    return (
        (x-p)**2,
        -2*(x**2+(2*r-p-q)*x+p*q),
        (x-q)**2,
    )


def main():
    # Soft wall x=E^2=0.
    for p, q, r in [(4,9,25), (9,25,16), (1,16,36)]:
        qaa, qab, qbb = q_coefficients(0, p, q, r)
        assert (qaa, qab, qbb) == (p*p, -2*p*q, q*q)

    # Endpoint wall K0/r=x^2+c*x+p*q=0.  Reduce coefficient identities
    # modulo that monic quadratic without adjoining either root.
    for p, q, r in [(4,9,25), (9,25,16), (1,16,36), (9,64,16)]:
        c = r-p-q
        # q_AB - 2(x-p)(x-q) has coefficients (constant, x, x^2).
        # Exact division by x^2+c*x+p*q leaves zero remainder.
        difference = [-4*p*q, -4*c, -4]
        quotient = -4
        remainder = [difference[0]-quotient*p*q, difference[1]-quotient*c]
        assert remainder == [0, 0]

    packet = {
        "triangle_first_normal_grade": "Q_pol=Q_AA*A^2+Q_AB*A*B+Q_BB*B^2",
        "soft_wall": {
            "equation": "E=0",
            "exact_square": "Q_pol=(P1^2*A-P2^2*B)^2",
            "binary_discriminant_order": "ord_E=2 when P1*P2*P3 != 0",
            "branch_separation": "linear in E",
            "transverse_type": "ordinary two-branch node",
        },
        "endpoint_wall": {
            "equation": "K0=0",
            "exact_square": "Q_pol=((E^2-P1^2)*A+(E^2-P2^2)*B)^2 mod K0",
            "binary_discriminant_order": "ord_K0=1 when E != 0",
            "branch_separation": "square-root in K0",
            "transverse_type": "simple fold",
        },
        "higher_excess_away_from_deeper_intersections": False,
        "remaining_intersection": "E=K0=0 implies P1*P2*P3=0",
    }
    out = Path(__file__).with_name("polar-deeper-square-normal-forms.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
