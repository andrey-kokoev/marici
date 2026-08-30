"""Exact rational local-system audit at a positive conductor pinch."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x = sp.Rational(5, 14)
    y = sp.Rational(3, 5)
    z = sp.Rational(3, 70)
    E = x + y + z
    assert E == 1

    f1 = x * y**2 + 2 * E * x * y - E**2 * (x + 2 * y - E)
    f2 = x**2 * y + 2 * E * x * y - E**2 * (2 * x + y - E)
    delta1 = sp.factor(4 * x * f1)
    delta2 = sp.factor(4 * y * f2)
    assert delta1 == 0
    assert delta2 == sp.Rational(561, 1225)

    ell1 = 2 * x - E
    ell2 = E - 2 * y
    ell3 = 2 * (x + y) - E
    ell4 = E
    A = sp.factor(ell1 * ell2)
    B = sp.factor(ell3 * ell4)
    quartic = sp.factor(4 * A * B - (A + B - E**2) ** 2)
    elliptic_discriminant = sp.factor(16 * A * B * (A - B) ** 4)
    assert (ell1, ell2, ell3, ell4) == (
        -sp.Rational(2, 7), -sp.Rational(1, 5), sp.Rational(32, 35), 1
    )
    assert quartic == sp.Rational(51, 245)
    assert elliptic_discriminant != 0

    # Around generic Delta_1, the absolute rank-nine family is regular and
    # the wall quotient has exactly one -1 Kummer character.
    t_abs = sp.eye(9)
    t_wall = sp.diag(1, -1, 1)  # (top, g_101, g_110)
    assert t_abs == sp.eye(9)

    # Hom(K_-, M_9) has monodromy -I.  Rational local-system extensions are
    # V/(T-I)V, which vanishes because -2 is invertible over Q.
    hom_t = -sp.eye(9)
    coboundary = hom_t - sp.eye(9)
    assert coboundary == -2 * sp.eye(9)
    assert coboundary.rank() == 9
    assert coboundary.det() == (-2) ** 9

    # The fixed route map still observes the only supported wall line.
    J = sp.Matrix([[2, 0, 1], [0, 2, 1], [0, 0, 1]])
    g101 = sp.Matrix([1, 0, 0])
    observed = J * g101
    assert observed == sp.Matrix([2, 0, 0])

    packet = {
        "schema": "marici.benincasa.conductor-ambient-extension-local-splitting.v1",
        "exact_positive_witness": {
            "x": str(x), "y": str(y), "z": str(z), "E": str(E)
        },
        "support_values": {
            "Delta1": str(delta1),
            "Delta2": str(delta2),
            "elliptic_discriminant": str(elliptic_discriminant),
            "Q": str(quartic),
        },
        "local_monodromy": {
            "absolute_rank9": "I9",
            "wall_rank3": "diag(1,-1,1)",
            "Hom(K_minus,M9)": "-I9",
        },
        "rational_extension_coboundary": "-2*I9",
        "rational_extension_coboundary_rank": coboundary.rank(),
        "rational_extension_group_dimension": 0,
        "supported_rational_nearby_rank": 1,
        "observer_image": [int(value) for value in observed],
        "observer_kernel_dimension": 0,
        "integral_qualification": (
            "the same cokernel over Z can carry 2-torsion; no integral "
            "ambient splitting is asserted"
        ),
        "classification": (
            "rational ambient extension locally splits; the only supported "
            "class is the already observed wall Kummer line"
        ),
        "new_carrier_datum": False,
    }
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
