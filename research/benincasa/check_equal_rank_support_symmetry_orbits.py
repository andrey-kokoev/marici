#!/usr/bin/env python3
"""Test whether the equal-rank support divisors are source-symmetry equivalent."""

import json
from itertools import permutations, product
from math import gcd
from pathlib import Path


VERTEX = (1, 1, 3)
COMPLEMENTARY = (1, 1, 0)


def primitive(vector):
    divisor = 0
    for value in vector:
        divisor = gcd(divisor, abs(value))
    reduced = tuple(value // divisor for value in vector)
    first = next(value for value in reduced if value)
    return tuple(-value for value in reduced) if first < 0 else reduced


def signed_permutation_orbit(vector):
    orbit = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            transformed = tuple(signs[i] * vector[permutation[i]] for i in range(3))
            orbit.add(primitive(transformed))
    return orbit


def coordinate_axes_contained(vector):
    # Axis i is contained in L=0 exactly when its coefficient vanishes.
    return [index for index, coefficient in enumerate(vector) if coefficient == 0]


def main():
    orbit_vertex = signed_permutation_orbit(VERTEX)
    orbit_complementary = signed_permutation_orbit(COMPLEMENTARY)
    axes_vertex = coordinate_axes_contained(VERTEX)
    axes_complementary = coordinate_axes_contained(COMPLEMENTARY)
    checks = {
        "orbits_are_disjoint": orbit_vertex.isdisjoint(orbit_complementary),
        "zero_pattern_is_signed_permutation_invariant": all(0 not in vector for vector in orbit_vertex) and all(vector.count(0) == 1 for vector in orbit_complementary),
        "vertex_support_contains_no_coordinate_axis": axes_vertex == [],
        "complementary_support_contains_one_coordinate_axis": axes_complementary == [2],
        "both_miss_strict_positive_chamber": sum(VERTEX) > 0 and sum(COMPLEMENTARY) > 0,
    }
    result = {
        "schema": "marici.equal-rank-support-symmetry-orbits.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "admissible_test_group": "signed permutations of the three homogeneous site-energy labels, modulo nonzero scalar units",
        "vertex_support": {
            "primitive_coefficients": list(VERTEX),
            "orbit_size": len(orbit_vertex),
            "coordinate_axes_contained": axes_vertex,
        },
        "complementary_support": {
            "primitive_coefficients": list(COMPLEMENTARY),
            "orbit_size": len(orbit_complementary),
            "coordinate_axes_contained": axes_complementary,
        },
        "invariant_discriminator": "number of zero site-energy coefficients, equivalently number of coordinate axes contained in the support divisor",
        "checks": checks,
    }
    output = Path(__file__).with_name("equal-rank-support-symmetry-orbits.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
