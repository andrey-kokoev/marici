"""Restrict the literal physical coefficient to the triple-wall incidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "benincasa"))
import check_physical_residue_at_weighted_tangencies as source  # noqa: E402

OUT = ROOT / "nima" / "results" / "cosmology_triple_incidence_physical_coefficient.json"


def main() -> None:
    a, b, x, y, z = source.a, source.b, source.x, source.y, source.z
    z0 = -(x + y) / 3
    triple = {a: x + z0, b: y + z0, z: z0}
    occurrence_left = b - x
    occurrence_right = a - y
    numerator = occurrence_left + occurrence_right

    numerator_triple = sp.factor(numerator.subs(triple, simultaneous=True))
    left_triple = sp.factor(occurrence_left.subs(triple, simultaneous=True))
    right_triple = sp.factor(occurrence_right.subs(triple, simultaneous=True))
    cover_triple = sp.factor(source.K.subs(triple, simultaneous=True))
    coefficient_norm = sp.factor(
        numerator_triple**2
        / (cover_triple * left_triple**2 * right_triple**2)
    )
    rational_coefficient_square_root = sp.factor(
        sp.Rational(81, 16) / ((x - 2 * y) ** 2 * (2 * x - y) ** 2)
    )

    assert sp.factor(numerator_triple + sp.Rational(2, 3) * (x + y)) == 0
    assert sp.factor(left_triple + sp.Rational(2, 3) * (2 * x - y)) == 0
    assert sp.factor(right_triple - sp.Rational(2, 3) * (x - 2 * y)) == 0
    expected_cover = (
        sp.Rational(64, 729)
        * (x - 2 * y) ** 2
        * (x + y) ** 2
        * (2 * x - y) ** 2
    )
    assert sp.factor(cover_triple - expected_cover) == 0
    assert sp.factor(coefficient_norm - rational_coefficient_square_root**2) == 0

    packet = {
        "schema": "marici.cosmology-triple-incidence-physical-coefficient.v1",
        "triple_incidence_parameter": "p=x+y+3*z",
        "physical_numerator_restriction": str(numerator_triple),
        "occurrence_left_restriction": str(left_triple),
        "occurrence_right_restriction": str(right_triple),
        "cayley_menger_restriction": str(cover_triple),
        "coefficient_norm": str(coefficient_norm),
        "coefficient_norm_is_rational_square": True,
        "algebraic_coefficient_generically_nonzero": True,
        "restricted_cover_generically_split_over_function_field": True,
        "coefficient_deck_character": "odd",
        "invariant_mu2_trace_activation_inferred": False,
        "physical_chain_activation_inferred": False,
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
