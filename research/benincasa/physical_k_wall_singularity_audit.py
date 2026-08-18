"""Exact singularity audit for K_E restricted to the five marked walls."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations

from physical_bulk_wall_connection_residue import k_value


WALLS = {
    "g1": ((0, 1), lambda x, y, z: -y - z),
    "g2": ((1, 0), lambda x, y, z: -x - z),
    "g3": ((1, 1), lambda x, y, z: z),
    "g23": ((0, 1), lambda x, y, z: -x),
    "g31": ((1, 0), lambda x, y, z: -y),
}


def wall_point(name, t, x, y, z):
    if name == "g1": return t, y + z
    if name == "g2": return x + z, t
    if name == "g3": return t, -t - z
    if name == "g23": return t, x
    if name == "g31": return y, t
    raise KeyError(name)


def interpolate(values):
    matrix = [[Fraction(i**j) for j in range(5)] + [Fraction(values[i])] for i in range(5)]
    for column in range(5):
        pivot = next(row for row in range(column, 5) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [value / scale for value in matrix[column]]
        for row in range(5):
            if row == column: continue
            scale = matrix[row][column]
            matrix[row] = [a - scale * b for a, b in zip(matrix[row], matrix[column])]
    return trim([matrix[i][-1] for i in range(5)])


def trim(polynomial):
    polynomial = list(polynomial)
    while polynomial and polynomial[-1] == 0: polynomial.pop()
    return polynomial


def derivative(polynomial):
    return trim([i * polynomial[i] for i in range(1, len(polynomial))])


def remainder(left, right):
    left = trim(left)
    while len(left) >= len(right) and left:
        scale = left[-1] / right[-1]
        shift = len(left) - len(right)
        for i, coefficient in enumerate(right): left[i + shift] -= scale * coefficient
        left = trim(left)
    return left


def gcd_degree(left, right):
    while right:
        left, right = right, remainder(left, right)
    return len(left) - 1


def solve_pair(first, second, x, y, z):
    (aa, ab), ac = WALLS[first]
    (ba, bb), bc = WALLS[second]
    determinant = aa * bb - ab * ba
    if not determinant: return None
    c1, c2 = ac(x, y, z), bc(x, y, z)
    return Fraction(ab * c2 - bb * c1, determinant), Fraction(ba * c1 - aa * c2, determinant)


def main():
    fibers = []
    for x, y, z in ((2, 3, 4), (3, 5, 7), (5, 7, 9)):
        restrictions = {}
        for wall in WALLS:
            values = [k_value(*wall_point(wall, t, x, y, z), x, y, z) for t in range(5)]
            polynomial = interpolate(values)
            restrictions[wall] = {
                "degree": len(polynomial) - 1,
                "gcd_with_derivative_degree": gcd_degree(polynomial, derivative(polynomial)),
            }
        collisions = []
        parallel = []
        for first, second in combinations(WALLS, 2):
            point = solve_pair(first, second, x, y, z)
            if point is None:
                parallel.append([first, second])
            else:
                collisions.append({
                    "pair": [first, second],
                    "K_E_zero": k_value(*point, x, y, z) == 0,
                })
        fibers.append({
            "kinematics": [x, y, z], "restrictions": restrictions,
            "finite_pair_collisions": collisions, "parallel_pairs": parallel,
        })
    expected_gcd_degrees = {"g1": 2, "g2": 2, "g3": 2, "g23": 0, "g31": 0}
    assert all(
        row["gcd_with_derivative_degree"] == expected_gcd_degrees[wall]
        for fiber in fibers for wall, row in fiber["restrictions"].items()
    )
    assert not any(
        row["K_E_zero"] for fiber in fibers for row in fiber["finite_pair_collisions"]
    )
    print(json.dumps({
        "schema": "marici.physical-k-wall-singularity-audit.v1",
        "fibers": fibers,
        "restriction_gcd_degree_pattern": expected_gcd_degrees,
        "shared_wall_restrictions_squarefree": False,
        "occurrence_wall_restrictions_squarefree": True,
        "finite_marked_pair_K_collisions": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
