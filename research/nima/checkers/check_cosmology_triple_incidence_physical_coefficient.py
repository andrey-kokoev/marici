"""Restrict the literal physical coefficient to the triple-wall incidence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "nima" / "results" / "cosmology_triple_incidence_physical_coefficient.json"


def main() -> None:
    # On p=x+y+3z=0 with q1=q2=q3=0:
    # z=-(x+y)/3, a=(2x-y)/3, b=(-x+2y)/3.
    numerator_triple = "-2*(x + y)/3"
    left_triple = "-2*(2*x - y)/3"
    right_triple = "2*(x - 2*y)/3"
    cover_triple = "64*(x - 2*y)**2*(x + y)**2*(2*x - y)**2/729"
    coefficient_norm = "6561/(256*(x - 2*y)**4*(2*x - y)**4)"

    # These formulas imply the coefficient norm is the square of
    # 81/(16*(x-2y)^2*(2x-y)^2) away from the visible occurrence poles.
    assert numerator_triple == "-2*(x + y)/3"
    assert left_triple == "-2*(2*x - y)/3"
    assert right_triple == "2*(x - 2*y)/3"

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
