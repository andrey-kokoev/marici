"""Exact physical-incidence and route-faithfulness audit for conductor collisions."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, y = sp.symbols("x y", positive=True)
    # Homogeneity permits E=1.  The third positive energy is z=1-x-y.
    f1 = sp.expand(x * y**2 + 2 * x * y - (x + 2 * y - 1))
    f2 = sp.expand(x**2 * y + 2 * x * y - (2 * x + y - 1))

    x_on_d1 = sp.factor(sp.solve(f1, x)[0])
    y_on_d2 = sp.factor(sp.solve(f2, y)[0])
    z_on_d1 = sp.factor(1 - y - x_on_d1)
    z_on_d2 = sp.factor(1 - x - y_on_d2)
    golden_endpoint = (sp.sqrt(5) - 1) / 2

    assert x_on_d1 == (2 * y - 1) / (y**2 + 2 * y - 1)
    assert y_on_d2 == (2 * x - 1) / (x**2 + 2 * x - 1)
    assert z_on_d1 == -y * (y**2 + y - 1) / (y**2 + 2 * y - 1)
    assert z_on_d2 == -x * (x**2 + x - 1) / (x**2 + 2 * x - 1)

    # On (1/2, (sqrt(5)-1)/2), numerator and denominator of the
    # displayed x/y parametrizations are positive, while z is positive.
    assert sp.simplify(golden_endpoint**2 + golden_endpoint - 1) == 0
    witness_y = sp.Rational(3, 5)
    witness_x = sp.simplify(x_on_d1.subs(y, witness_y))
    witness_z = sp.simplify(z_on_d1.subs(y, witness_y))
    assert (witness_x, witness_y, witness_z) == (
        sp.Rational(5, 14), sp.Rational(3, 5), sp.Rational(3, 70)
    )
    assert sp.simplify(f1.subs({x: witness_x, y: witness_y})) == 0

    # The double roots of the normalized wall quadratics are interior to
    # the source-oriented occurrence interval (-1,1).
    r1 = -y
    r2 = x
    assert -1 < float(r1.subs(y, witness_y)) < 0
    assert 0 < float(r2.subs(x, witness_y)) < 1

    # Simultaneous collisions cannot occur in x>0,y>0,x+y<1.
    difference = sp.factor(f1 - f2)
    assert sp.simplify(difference + (x - y) * (x * y - 1)) == 0
    diagonal = sp.factor(f1.subs(y, x))
    assert diagonal == x**3 + 2 * x**2 - 3 * x + 1
    diagonal_derivative = sp.diff(diagonal, x)
    assert sp.simplify(diagonal.subs(x, sp.Rational(1, 2))) == sp.Rational(1, 8)
    # h' is negative on [0,1/2], so h >= h(1/2) > 0 there.
    assert sp.simplify(diagonal_derivative.subs(x, sp.Rational(1, 2))) < 0

    # Entry 308's fixed Leray/occurrence map.  Each collision line maps to
    # a distinct nonzero route before scalar aggregation.
    J = sp.Matrix([[2, 0, 1], [0, 2, 1], [0, 0, 1]])
    route1 = J * sp.Matrix([1, 0, 0])
    route2 = J * sp.Matrix([0, 1, 0])
    assert route1 == sp.Matrix([2, 0, 0])
    assert route2 == sp.Matrix([0, 2, 0])
    assert sp.Matrix.hstack(route1, route2).rank() == 2

    packet = {
        "schema": "marici.benincasa.physical-conductor-collision-routes.v1",
        "normalization": "E=1 by homogeneous scaling",
        "delta1_equation": str(f1),
        "delta2_equation": str(f2),
        "delta1_physical_parametrization": {
            "parameter": "1/2 < y < (sqrt(5)-1)/2",
            "x": str(x_on_d1),
            "z": str(z_on_d1),
            "collision_coordinate": "r=-y in (-1,0)",
        },
        "delta2_physical_parametrization": {
            "parameter": "1/2 < x < (sqrt(5)-1)/2",
            "y": str(y_on_d2),
            "z": str(z_on_d2),
            "collision_coordinate": "r=x in (0,1)",
        },
        "exact_delta1_witness": {
            "x": str(witness_x), "y": str(witness_y), "z": str(witness_z)
        },
        "simultaneous_collision_difference": str(difference),
        "simultaneous_positive_physical_collision": False,
        "local_coefficient_lines": {
            "delta1": {"monodromy": -1, "nilpotent_rank": 0},
            "delta2": {"monodromy": -1, "nilpotent_rank": 0},
        },
        "leray_matrix": [[int(value) for value in row] for row in J.tolist()],
        "route_images": {
            "delta1": [int(value) for value in route1],
            "delta2": [int(value) for value in route2],
        },
        "route_packet_rank": 2,
        "route_resolved_kernel_dimension": 0,
        "classification": "existing conductor/Landau support with two separately faithful Kummer routes",
        "new_carrier_datum": False,
        "scope": (
            "homogeneous scalar rank-three conductor quotient; no finite-q "
            "tensor vertex or polarization completion"
        ),
    }
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
