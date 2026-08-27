#!/usr/bin/env python3
"""Exact scalar-block hostile for Schur--Evans zero-to-dagger promotion."""

from fractions import Fraction
import json
from pathlib import Path


def schur(a, b, c):
    return c - b * b / a


def main():
    a = Fraction(2)
    b = Fraction(3)
    z0 = Fraction(0)
    evans_at_zero = z0

    source_c_at_zero = Fraction(5)
    source_schur = schur(a, b, source_c_at_zero)
    assert evans_at_zero == 0
    assert source_schur == Fraction(1, 2) != 0

    fitted_c_at_zero = b * b / a
    fitted_schur = schur(a, b, fitted_c_at_zero)
    assert fitted_schur == evans_at_zero == 0

    # Functional comparison: C(z)=b^2/a+z gives S(z)=z, but this formula is
    # acceptable only if C is independently source-derived.
    samples = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(3)]
    for z in samples:
        assert schur(a, b, b * b / a + z) == z
        assert schur(a, b, Fraction(5) + z) == z + Fraction(1, 2)

    result = {
        "schema": "marici.rh-schur-evans-promotion.v1",
        "forward_block": {"A": "2", "B": "3"},
        "endpoint_evans_zero": "F(0)=0",
        "independent_source_scalar_fixture": "C(z)=5+z",
        "source_schur_fixture": "S(z)=z+1/2",
        "zero_divisor_mismatch_at_z0": True,
        "fitted_scalar_block": "C(z)=9/2+z",
        "fitted_schur": "S(z)=z",
        "fitted_agreement_has_no_authority": True,
        "surviving_constructor": "source_derived_reciprocal_colligation_with_schur_evans_comparison_cell",
        "acceptance_gates": ["adjoint_return_channel", "independent_scalar_block", "nowhere_zero_unit", "cutoff_naturality", "completion_stability"]
    }
    out = Path(__file__).parents[1] / "results" / "rh-schur-evans-promotion.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
