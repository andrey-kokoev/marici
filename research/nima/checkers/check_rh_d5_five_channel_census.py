#!/usr/bin/env python3
"""Exact invariant census for the provisional five-channel D5 completion."""

import itertools
import json
from pathlib import Path

import sympy as sp


def exponent_tuples(total_degree, length=5):
    for exponents in itertools.product(range(total_degree + 1), repeat=length):
        if sum(exponents) == total_degree:
            yield exponents


def rotation_weight(exponents):
    z1, w1, z2, w2, _singlet = exponents
    return (z1 - w1 + 2 * (z2 - w2)) % 5


def reflect(exponents):
    z1, w1, z2, w2, singlet = exponents
    return (w1, z1, w2, z2, singlet)


def invariant_orbits(total_degree):
    weight_zero = {
        exponents
        for exponents in exponent_tuples(total_degree)
        if rotation_weight(exponents) == 0
    }
    orbits = []
    unseen = set(weight_zero)
    while unseen:
        representative = min(unseen)
        orbit = {representative, reflect(representative)}
        assert orbit <= weight_zero
        orbits.append(sorted(orbit))
        unseen -= orbit
    return sorted(orbits)


dimensions = {degree: len(invariant_orbits(degree)) for degree in range(7)}
assert dimensions == {0: 1, 1: 1, 2: 3, 3: 5, 4: 10, 5: 16, 6: 26}

# The only bidegree-(2,2) weight-zero monomial is the radial product.
bidegree_22 = []
for exponents in itertools.product(range(3), repeat=4):
    if (
        exponents[0] + exponents[1] == 2
        and exponents[2] + exponents[3] == 2
        and rotation_weight(exponents + (0,)) == 0
    ):
        bidegree_22.append(exponents)
assert bidegree_22 == [(1, 1, 1, 1)]

# Degree two has no mixed doublet invariant.
degree_two = invariant_orbits(2)
expected_degree_two = [
    [(0, 0, 0, 0, 2)],
    [(0, 0, 1, 1, 0)],
    [(1, 1, 0, 0, 0)],
]
assert degree_two == expected_degree_two

# Degree three contains two mixed cubics in addition to singlet-dressed norms.
degree_three = invariant_orbits(3)
mixed_cubic_orbits = [
    orbit
    for orbit in degree_three
    if any((e[0] + e[1]) > 0 and (e[2] + e[3]) > 0 for e in orbit)
    and all(e[4] == 0 for e in orbit)
]
assert {tuple(orbit) for orbit in mixed_cubic_orbits} == {
    ((0, 2, 1, 0, 0), (2, 0, 0, 1, 0)),
    ((0, 1, 0, 2, 0), (1, 0, 2, 0, 0)),
}

a, b, c, d = sp.symbols("a b c d", real=True)
z1 = a + sp.I * b
z2 = c + sp.I * d
cubic_112 = sp.expand(sp.re(z1**2 * sp.conjugate(z2)))
cubic_122 = sp.expand(sp.re(z1 * z2**2))
assert cubic_112 == a**2 * c + 2 * a * b * d - b**2 * c
assert cubic_122 == a * c**2 - a * d**2 - 2 * b * c * d

tail_scalar_zero = {a: 0, b: 1, c: 1, d: 1}
tail_zero_values = [
    sp.simplify(cubic_112.subs(tail_scalar_zero)),
    sp.simplify(cubic_122.subs(tail_scalar_zero)),
]
assert tail_zero_values == [-1, -2]

both_even_zero = {a: 0, b: 1, c: 0, d: 1}
assert cubic_112.subs(both_even_zero) == 0
assert cubic_122.subs(both_even_zero) == 0

result = {
    "representation": "1 + V1 + V2",
    "reflection_cycle_type": "(12)(34)(5)",
    "invariant_dimensions_by_degree": dimensions,
    "quadratic_basis": ["L^2", "|z1|^2", "|z2|^2"],
    "mixed_quadratic_invariant": False,
    "mixed_bidegree_22_basis": ["|z1|^2 |z2|^2"],
    "mixed_cubic_basis": ["Re(z1^2 conjugate(z2))", "Re(z1 z2^2)"],
    "mixed_cubic_real_forms": [str(cubic_112), str(cubic_122)],
    "tail_scalar_zero_hostile_values": [str(value) for value in tail_zero_values],
    "both_even_channels_zero_kills_mixed_cubics": True,
    "source_order_five_rotation_constructed": False,
    "verdict": (
        "the provisional D5 completion has exact quadratic complementarity but admits "
        "two mixed cubic invariants; one scalar zero does not annihilate them"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-d5-five-channel-census.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
