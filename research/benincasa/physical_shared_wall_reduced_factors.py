"""Canonical reduced factors of K_E on the three shared walls."""

from __future__ import annotations

import json
from fractions import Fraction

from physical_k_wall_singularity_audit import interpolate, k_value, wall_point


def multiply(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def reduced_factor(wall, x, y, z):
    restricted = interpolate([
        k_value(*wall_point(wall, t, x, y, z), x, y, z) for t in range(5)
    ])
    leading = {"g1": Fraction(x), "g2": Fraction(y), "g3": Fraction(z)}[wall]
    if wall in ("g1", "g2"):
        factor = [restricted[2] / (2 * leading), Fraction(0), leading]
    else:
        linear = restricted[3] / (2 * leading)
        constant = (restricted[2] - linear * linear) / (2 * leading)
        factor = [constant, linear, leading]
    assert multiply(factor, factor) == restricted
    return factor


def main():
    fibers = []
    points = [
        (x, y, z)
        for x in (2, 3, 5)
        for y in (4, 7)
        for z in (6, 9)
    ]
    for x, y, z in points:
        factors = {}
        for wall in ("g1", "g2", "g3"):
            factor = reduced_factor(wall, x, y, z)
            discriminant = factor[1] ** 2 - 4 * factor[2] * factor[0]
            factors[wall] = {
                "coefficients_constant_to_quadratic": [str(value) for value in factor],
                "discriminant": str(discriminant),
                "discriminant_nonzero": discriminant != 0,
            }
        fibers.append({"kinematics": [x, y, z], "factors": factors})
    assert all(
        row["discriminant_nonzero"]
        for fiber in fibers for row in fiber["factors"].values()
    )
    print(json.dumps({
        "schema": "marici.physical-shared-wall-reduced-factors.v1",
        "chart": "x*y*z != 0",
        "normalization": {"g1": "leading coefficient x", "g2": "leading coefficient y", "g3": "leading coefficient z"},
        "exact_square_identities_verified": len(fibers) * 3,
        "fibers": fibers,
        "all_reduced_factors_squarefree_on_sweep": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
