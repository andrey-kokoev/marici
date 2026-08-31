"""Activation gate for the triple-incidence logarithmic nearby line.

This checker does not deny the algebraic nearby line.  It separates it from a
literal positive-energy physical readout.  The current source data give two
independent obstructions:

1. support: p=X1+X2+3X3 has no strict-positive chamber zero;
2. descent: the restricted coefficient is sheet-odd, so an invariant mu2 trace
   is not supplied by the split function-field coefficient alone.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "cosmology_triple_incidence_activation_obstruction.json"


def read_result(name: str) -> dict:
    return json.loads((ROOT / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    log = read_result("cosmology_triple_incidence_logarithmic_identity.json")
    coeff = read_result("cosmology_triple_incidence_physical_coefficient.json")
    chamber = read_result("cosmology_triple_incidence_positive_chamber_gate.json")

    assert log["universal_logarithmic_nearby_line_constructed"] is True
    assert log["physical_twisted_coefficient_pairing_constructed"] is False
    assert coeff["coefficient_norm_is_rational_square"] is True
    assert coeff["coefficient_deck_character"] == "odd"
    assert coeff["invariant_mu2_trace_activation_inferred"] is False
    assert coeff["physical_chain_activation_inferred"] is False
    assert chamber["strict_positive_chamber_intersection"] is False
    assert chamber["literal_positive_chain_activation"] is False
    assert chamber["analytic_continuation_activation_inferred"] is False

    literal_activation = (
        log["physical_twisted_coefficient_pairing_constructed"]
        and coeff["invariant_mu2_trace_activation_inferred"]
        and chamber["literal_positive_chain_activation"]
    )
    analytic_activation = chamber["analytic_continuation_activation_inferred"]

    packet = {
        "schema": "marici.cosmology-triple-incidence-activation-obstruction.v1",
        "nearby_line": "universal logarithmic rank-one vanishing quotient",
        "nearby_line_constructed": True,
        "support_gate": {
            "incidence_parameter": chamber["incidence_parameter"],
            "strict_positive_chamber_intersection": False,
            "closed_nonnegative_chamber_intersection": chamber[
                "closed_nonnegative_chamber_intersection"
            ],
            "literal_positive_chain_activation": False,
        },
        "deck_descent_gate": {
            "restricted_cover_split": coeff[
                "restricted_cover_generically_split_over_function_field"
            ],
            "coefficient_deck_character": coeff["coefficient_deck_character"],
            "invariant_mu2_trace_activation_inferred": False,
        },
        "pairing_gate": {
            "physical_twisted_coefficient_pairing_constructed": False,
            "physical_chain_activation_inferred": False,
            "analytic_continuation_activation_inferred": False,
        },
        "literal_generic_physical_period_supported_on_nearby_line": literal_activation,
        "analytic_continuation_period_supported_on_nearby_line": analytic_activation,
        "conclusion": (
            "the algebraic nearby line is real, but the current source does not "
            "activate it as a literal generic positive-energy cosmological readout"
        ),
        "next_gate": (
            "derive analytic-continuation authority or an all-soft specialization "
            "before pairing the odd nearby line with a physical chain"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
