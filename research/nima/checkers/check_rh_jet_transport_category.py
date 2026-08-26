#!/usr/bin/env python3
"""Exact functorial laws for multiplicative first-jet seam transports."""

import json
from fractions import Fraction
from pathlib import Path


def compose_jet(left, right):
    """Jet of the product: (g,g') * (h,h')."""
    g, dg = left
    h, dh = right
    return g * h, dg * h + g * dh


def matrix(jet):
    g, dg = jet
    return ((g, 0), (dg, g))


def multiply(left, right):
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def determinant(value):
    return value[0][0] * value[1][1] - value[0][1] * value[1][0]


g = (Fraction(2), Fraction(3))
h = (Fraction(5), Fraction(7))
k = (Fraction(11), Fraction(13))

assert compose_jet(compose_jet(g, h), k) == compose_jet(g, compose_jet(h, k))
assert matrix(compose_jet(g, h)) == multiply(matrix(g), matrix(h))
assert determinant(matrix(g)) == g[0] ** 2
assert determinant(matrix(compose_jet(g, h))) == determinant(matrix(g)) * determinant(matrix(h))

logarithmic_shear_g = g[1] / g[0]
logarithmic_shear_h = h[1] / h[0]
logarithmic_shear_product = compose_jet(g, h)[1] / compose_jet(g, h)[0]
assert logarithmic_shear_product == logarithmic_shear_g + logarithmic_shear_h

result = {
    "jet_composition_associative": True,
    "jet_matrix_is_functorial": True,
    "determinant_character_is_square": True,
    "determinant_character_is_multiplicative": True,
    "normalized_logarithmic_shear_is_additive": True,
    "sample_logarithmic_shears": [
        str(logarithmic_shear_g),
        str(logarithmic_shear_h),
        str(logarithmic_shear_product),
    ],
    "verdict": (
        "source multipliers act through a first-jet transport category; the square "
        "character carries determinant coherence and the normalized shear carries "
        "the additive logarithmic derivative"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-jet-transport-category.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
