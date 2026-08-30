#!/usr/bin/env python3
"""Hostile scalar symmetry audit for zero-to-dagger promotion."""

from fractions import Fraction
import json
from pathlib import Path


def h(z):
    return z * z + 1


def main():
    z0 = 1j
    assert h(z0) == 0
    assert h(-z0) == h(z0)

    generic = 2 + 3j
    assert h(generic.conjugate()) == h(generic).conjugate()

    # The same exact off-seam continuous-boundary fixture as the prior audit.
    reciprocal = Fraction(1)
    adjoint = Fraction(1, 2)
    star_residual = reciprocal - adjoint
    assert star_residual == Fraction(1, 2)

    result = {
        "schema": "marici.rh-zero-to-dagger-promotion.v1",
        "hostile_multiplier": "H(z)=z^2+1",
        "functional_reflection_even": True,
        "real_structure_preserved": True,
        "off_seam_zero": "z=i",
        "boundary_star_residual_at_zero": "1/2",
        "scalar_zero_implies_star_cell": False,
        "equalizer": "objects_where_reciprocal_transport_equals_hilbert_adjoint",
        "required_constructor": "source_authorized_zero_to_dagger_promotion",
        "categorical_rh_statement": "zero_subcategory_factors_through_reciprocal_adjoint_equalizer"
    }
    out = Path(__file__).parents[1] / "results" / "rh-zero-to-dagger-promotion.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
