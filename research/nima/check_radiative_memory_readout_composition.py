#!/usr/bin/env python3
"""Exact first constructor-composition square in the radiative-memory fiber."""

import json
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


def center(samples):
    mean = sum(samples, Fraction(0)) / 3
    return tuple(value - mean for value in samples)


def plane_coordinates(centered):
    x, y, z = centered
    assert x + y + z == 0
    # (x,y,z)=(a,-a+b,-b)
    return x, -z


def plane_invariants(coordinates):
    a, b = coordinates
    return a * a - a * b + b * b, a * b * (a - b)


def direct_centered_invariants(samples):
    x, y, z = center(samples)
    return (x * x + y * y + z * z) / 2, x * y * z


composition_checks = 0
permutation_checks = 0
translation_checks = 0
for raw in product(range(-6, 7), repeat=3):
    samples = tuple(Fraction(value) for value in raw)
    via_composition = plane_invariants(plane_coordinates(center(samples)))
    direct = direct_centered_invariants(samples)
    assert via_composition == direct
    composition_checks += 1

    for perm in permutations(range(3)):
        transported = tuple(samples[i] for i in perm)
        assert direct_centered_invariants(transported) == direct
        permutation_checks += 1

    for shift in (-5, -1, 0, 2, 7):
        shifted = tuple(value + shift for value in samples)
        assert direct_centered_invariants(shifted) == direct
        translation_checks += 1

result = {
    "schema": "marici.nima.radiative_memory_readout_composition.v1",
    "source_object": "three direction-labelled displacement-memory samples",
    "constructor_F": "quotient the constant sample line by centering",
    "constructor_E": "D3 invariant scalarization by q2,q3",
    "composition_identity": "(E o F)^* = F^* o E^*",
    "direct_pullbacks": {
        "q2": "1/2 sum_i (x_i-mean(x))^2",
        "q3": "product_i (x_i-mean(x))",
    },
    "composition_checks": composition_checks,
    "permutation_checks": permutation_checks,
    "constant_mode_translation_checks": translation_checks,
    "passed": True,
}
out = Path(__file__).with_name("results") / "radiative-memory-readout-composition.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

