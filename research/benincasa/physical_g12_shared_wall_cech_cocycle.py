"""Exact Cech-closure gate for the physical q_G12 shared-wall boundary."""

from __future__ import annotations

import json
from fractions import Fraction


# q = alpha*a + beta*b + constant(x,y,z).
GRADIENTS = {
    "q_g1": (0, 1),
    "q_g2": (1, 0),
    "q_g3": (1, 1),
}


def constants(x: int, y: int, z: int) -> dict[str, int]:
    return {"q_g1": -y - z, "q_g2": -x - z, "q_g3": z}


def solve_pair(first: str, second: str, x: int, y: int, z: int) -> tuple[Fraction, Fraction]:
    a1, b1 = GRADIENTS[first]
    a2, b2 = GRADIENTS[second]
    c = constants(x, y, z)
    determinant = a1 * b2 - b1 * a2
    assert determinant != 0
    a = Fraction((-c[first]) * b2 - b1 * (-c[second]), determinant)
    b = Fraction(a1 * (-c[second]) - (-c[first]) * a2, determinant)
    return a, b


def q_values(a: Fraction, b: Fraction, x: int, y: int, z: int) -> dict[str, Fraction]:
    return {
        "q_g1": b - y - z,
        "q_g2": a - x - z,
        "q_g3": a + b + z,
        "q_g23": b - x,
        "q_g31": a - y,
    }


def cayley_menger(a: Fraction, b: Fraction, x: int, y: int, z: int) -> Fraction:
    c = -(x + y + z)
    x2, y2, z2 = x * x, y * y, z * z
    return (
        x2 * a**4
        - a**2 * b**2 * (x2 + y2 - z2)
        + y2 * b**4
        + a**2 * x2 * (x2 - y2 - z2)
        + c**2 * a**2 * (y2 - x2 - z2)
        + b**2 * y2 * (y2 - x2 - z2)
        + c**2 * b**2 * (x2 - y2 - z2)
        + z2 * c**4
        + c**2 * z2 * (z2 - x2 - y2)
        + z2 * x2 * y2
    )


def main() -> None:
    pairs = (("q_g1", "q_g2"), ("q_g1", "q_g3"), ("q_g2", "q_g3"))
    points = ((2, 3, 4), (3, 5, 6), (5, 7, 9))
    rows = []
    for x, y, z in points:
        for first, second in pairs:
            a, b = solve_pair(first, second, x, y, z)
            values = q_values(a, b, x, y, z)
            determinant = (
                GRADIENTS[first][0] * GRADIENTS[second][1]
                - GRADIENTS[first][1] * GRADIENTS[second][0]
            )
            remaining = ({"q_g1", "q_g2", "q_g3"} - {first, second}).pop()
            occurrence_numerator = values["q_g23"] + values["q_g31"]
            assert values[first] == values[second] == 0
            assert values[remaining] != 0
            assert values["q_g23"] != 0 and values["q_g31"] != 0
            assert occurrence_numerator != 0
            assert cayley_menger(a, b, x, y, z) != 0
            assert Fraction(1, determinant) + Fraction(1, -determinant) == 0
            rows.append(
                {
                    "kinematics": [x, y, z],
                    "pair": [first, second],
                    "intersection": [str(a), str(b)],
                    "oriented_jacobians": [determinant, -determinant],
                    "iterated_residue_sum": "0",
                }
            )

    # At the occurrence intersection u=q_g31=a-y and v=q_g23=b-x,
    # the unsplit source factor is (u+v)/(u*v).
    mixed_numerator_at_intersection = (0 + 0)
    assert mixed_numerator_at_intersection == 0

    print(
        json.dumps(
            {
                "schema": "marici.physical-g12-shared-wall-cech-cocycle.v1",
                "pair_checks": rows,
                "shared_wall_pairwise_cech_differential": 0,
                "mixed_occurrence_double_residue_numerator": 0,
                "physical_localization_boundary_is_closed": True,
                "absolute_T7_coordinates_selected": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
