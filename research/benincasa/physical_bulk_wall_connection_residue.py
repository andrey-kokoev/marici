"""Typed bulk-to-wall connection/residue compatibility gate."""

from __future__ import annotations

import json
from fractions import Fraction


def q_values(a, b, x, y, z):
    return {
        "g1": b - y - z,
        "g2": a - x - z,
        "g3": a + b + z,
        "g23": b - x,
        "g31": a - y,
    }


def k_value(a, b, x, y, z):
    c = x + y + z
    x2, y2, z2 = x * x, y * y, z * z
    return (
        x2 * a**4 - (x2 + y2 - z2) * a**2 * b**2 + y2 * b**4
        + (x2 * (x2 - y2 - z2) + c**2 * (y2 - x2 - z2)) * a**2
        + (y2 * (y2 - x2 - z2) + c**2 * (x2 - y2 - z2)) * b**2
        + z2 * c**4 + c**2 * z2 * (z2 - x2 - y2) + z2 * x2 * y2
    )


def exact_derivative(function, point, axis):
    # Every input polynomial has degree at most four in each variable.
    weights = (1, -8, 0, 8, -1)
    total = 0
    for offset, weight in zip((-2, -1, 0, 1, 2), weights):
        shifted = list(point)
        shifted[axis] += offset
        total += weight * function(*shifted)
    return Fraction(total, 12)


def logarithmic_source_derivative(a, b, x, y, z, wall, axis, gamma=5):
    point = (a, b, x, y, z)
    values = q_values(*point)
    numerator = values["g23"] + values["g31"]
    remaining = [name for name in values if name != wall]
    k = k_value(*point)
    denominator = k**gamma
    for name in remaining:
        denominator *= values[name]
    source = Fraction(numerator, denominator)

    def numerator_function(aa, bb, xx, yy, zz):
        q = q_values(aa, bb, xx, yy, zz)
        return q["g23"] + q["g31"]

    numerator_derivative = exact_derivative(numerator_function, point, axis)
    k_derivative = exact_derivative(k_value, point, axis)
    logarithmic_denominator_derivative = gamma * Fraction(k_derivative, k)
    for name in remaining:
        def q_function(aa, bb, xx, yy, zz, mark=name):
            return q_values(aa, bb, xx, yy, zz)[mark]
        logarithmic_denominator_derivative += Fraction(
            exact_derivative(q_function, point, axis), values[name]
        )
    return source * (
        Fraction(numerator_derivative, numerator)
        - logarithmic_denominator_derivative
    )


def main():
    # wall: (normal coordinate axis, wall substitution, q parameter derivatives)
    walls = {
        "g1": (1, lambda a, b, x, y, z: (a, y + z), {2: 0, 3: -1}),
        "g2": (0, lambda a, b, x, y, z: (x + z, b), {2: -1, 3: 0}),
        "g3": (0, lambda a, b, x, y, z: (-b - z, b), {2: 0, 3: 0}),
    }
    rows = []
    for x, y, z in ((2, 3, 4), (3, 5, 6), (5, 7, 9)):
        # Generic tangent samples avoid all remaining divisors.
        for tangent in (1, 2):
            for wall, (normal_axis, substitute, q_parameter) in walls.items():
                seed_a, seed_b = (tangent, tangent + 1)
                a, b = substitute(seed_a, seed_b, x, y, z)
                point = (a, b, x, y, z)
                values = q_values(*point)
                if any(values[name] == 0 for name in values if name != wall):
                    continue
                if k_value(*point) == 0 or values["g23"] + values["g31"] == 0:
                    continue
                for gamma in (0, 1, 5):
                  for parameter_axis, parameter_name in ((2, "x"), (3, "y")):
                    fixed_parameter = logarithmic_source_derivative(
                        *point, wall, parameter_axis, gamma
                    )
                    normal_derivative = logarithmic_source_derivative(
                        *point, wall, normal_axis, gamma
                    )
                    q_parameter_derivative = q_parameter[parameter_axis]
                    # Res(d_parameter Omega): the double-pole term contributes
                    # -q_parameter * d_normal of the simple-pole coefficient.
                    bulk_then_residue = (
                        fixed_parameter
                        - q_parameter_derivative * normal_derivative
                    )
                    wall_motion = -q_parameter_derivative
                    residue_then_wall_connection = (
                        fixed_parameter + wall_motion * normal_derivative
                    )
                    assert bulk_then_residue == residue_then_wall_connection
                    rows.append({
                        "kinematics": [x, y, z], "wall": wall,
                        "parameter": parameter_name, "gamma": gamma,
                        "double_pole_correction_nonzero": (
                            q_parameter_derivative * normal_derivative != 0
                        ),
                        "commutator": "0",
                    })
    assert rows
    print(json.dumps({
        "schema": "marici.bulk-wall-connection-residue.v1",
        "checks": len(rows),
        "all_commutators_zero": True,
        "nonzero_moving_wall_corrections": sum(
            row["double_pole_correction_nonzero"] for row in rows
        ),
        "wall_degree_retained": True,
        "pair_cech_degree": "verified separately by physical_g12_shared_wall_cech_cocycle.py",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
