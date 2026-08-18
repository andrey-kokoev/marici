"""Canonical reduced factors of K_E on the three shared walls."""

from __future__ import annotations

import json
from fractions import Fraction

from physical_k_wall_singularity_audit import (
    gcd_degree, interpolate, k_value, polynomial_gcd, wall_point
)
from physical_bulk_wall_connection_residue import q_values


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


def homogeneous_monomials(degree):
    return [(i, j, degree - i - j) for i in range(degree + 1) for j in range(degree + 1 - i)]


def solve_homogeneous(samples, degree=4):
    monomials = homogeneous_monomials(degree)
    matrix = []
    for (x, y, z), value in samples:
        matrix.append([Fraction(x**i * y**j * z**k) for i, j, k in monomials] + [value])
    row = 0
    pivots = {}
    for column in range(len(monomials)):
        pivot = next(index for index in range(row, len(matrix)) if matrix[index][column])
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][column]
        matrix[row] = [value / scale for value in matrix[row]]
        for index in range(len(matrix)):
            if index == row: continue
            scale = matrix[index][column]
            matrix[index] = [a - scale * b for a, b in zip(matrix[index], matrix[row])]
        pivots[column] = row
        row += 1
    coefficients = {monomials[column]: matrix[index][-1] for column, index in pivots.items()}
    assert all(
        sum(coefficients[m] * x**m[0] * y**m[1] * z**m[2] for m in monomials) == value
        for (x, y, z), value in samples
    )
    return coefficients


def q_value(x, y, z):
    energy = x + y + z
    return -16*x*x*y*y - 8*x*y*energy*energy + 8*(x+y)*energy**3 - 5*energy**4


def proportional(left, right):
    keys = set(left) | set(right)
    pivot = next((key for key in keys if right.get(key, 0)), None)
    if pivot is None: return False
    scale = left.get(pivot, 0) / right[pivot]
    return all(left.get(key, 0) == scale * right.get(key, 0) for key in keys)


def main():
    fibers = []
    points = [
        (x, y, z)
        for x in (1, 2, 3, 5)
        for y in (1, 2, 4, 7)
        for z in (1, 3, 6, 9)
    ]
    discriminant_samples = {wall: [] for wall in ("g1", "g2", "g3")}
    for x, y, z in points:
        generic_energy_letters = all((x+y+z, x+y-z, x-y+z, -x+y+z))
        factors = {}
        for wall in ("g1", "g2", "g3"):
            factor = reduced_factor(wall, x, y, z)
            discriminant = factor[1] ** 2 - 4 * factor[2] * factor[0]
            wall_mark = {"g1": "g1", "g2": "g2", "g3": "g3"}[wall]
            numerator_values = []
            denominator_values = []
            for t in range(5):
                a, b = wall_point(wall, t, x, y, z)
                q = q_values(a, b, x, y, z)
                numerator_values.append(q["g23"] + q["g31"])
                denominator = 1
                for name, value in q.items():
                    if name != wall_mark:
                        denominator *= value
                denominator_values.append(denominator)
            numerator_polynomial = interpolate(numerator_values)
            denominator_polynomial = interpolate(denominator_values)
            factors[wall] = {
                "coefficients_constant_to_quadratic": [str(value) for value in factor],
                "discriminant": str(discriminant),
                "discriminant_nonzero": discriminant != 0,
                "physical_numerator_gcd_degree": gcd_degree(factor, numerator_polynomial),
                "remaining_marked_denominator_gcd_degree": gcd_degree(factor, denominator_polynomial),
            }
            discriminant_samples[wall].append(((x, y, z), discriminant))
        fibers.append({"kinematics": [x, y, z], "generic_energy_letters": generic_energy_letters, "factors": factors})
    assert all(
        row["discriminant_nonzero"]
        for fiber in fibers for row in fiber["factors"].values()
    )
    assert all(
        row["physical_numerator_gcd_degree"] == 0
        and row["remaining_marked_denominator_gcd_degree"] == 0
        for fiber in fibers if fiber["generic_energy_letters"] for row in fiber["factors"].values()
    )
    discriminant_polynomials = {
        wall: solve_homogeneous(samples) for wall, samples in discriminant_samples.items()
    }
    q_polynomial = solve_homogeneous([((x, y, z), Fraction(q_value(x, y, z))) for x, y, z in points])
    q_associates = {
        wall: proportional(polynomial, q_polynomial)
        for wall, polynomial in discriminant_polynomials.items()
    }
    assert not any(q_associates.values())
    print(json.dumps({
        "schema": "marici.physical-shared-wall-reduced-factors.v1",
        "chart": "x*y*z != 0",
        "normalization": {"g1": "leading coefficient x", "g2": "leading coefficient y", "g3": "leading coefficient z"},
        "exact_square_identities_verified": len(fibers) * 3,
        "fibers": fibers,
        "all_reduced_factors_squarefree_on_sweep": True,
        "generic_fibers_with_all_six_physical_tangency_residues_nonzero": sum(
            fiber["generic_energy_letters"] for fiber in fibers
        ),
        "nonzero_residue_scope": "away from signed-energy conductor letters",
        "discriminant_polynomials": {
            wall: {f"x^{i}y^{j}z^{k}": str(value) for (i, j, k), value in polynomial.items() if value}
            for wall, polynomial in discriminant_polynomials.items()
        },
        "Q_associate_to_reduced_discriminant": q_associates,
        "Q_divides_product_of_reduced_discriminants": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
