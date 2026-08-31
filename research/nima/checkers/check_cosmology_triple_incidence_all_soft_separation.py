"""Separate the all-soft Z/3 character from the triple-incidence nearby line.

The triple-incidence line is a sheet-odd logarithmic nearby line at p=0.  The
existing all-soft packet is a flat order-three relative differential character.
This checker verifies that the current all-soft specialization data do not
supply the missing physical twisted pairing or mu2 descent for the nearby line.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_triple_incidence_all_soft_separation.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    activation = load("cosmology_triple_incidence_activation_obstruction.json")
    flat = load("all-soft-flat-z3-character.json")
    character = load("all-soft-relative-differential-character.json")
    no_go = load("half-twist-torsion-coupling-rank-no-go.json")

    assert activation["nearby_line_constructed"] is True
    assert activation["deck_descent_gate"]["coefficient_deck_character"] == "odd"
    assert activation["deck_descent_gate"]["invariant_mu2_trace_activation_inferred"] is False
    assert activation["literal_generic_physical_period_supported_on_nearby_line"] is False
    assert flat["relative_H2_mod3_generator_evaluation"] == 1
    assert flat["Cayley_Menger_relative_chain_coupling_constructed"] is False
    assert character["order"] == 3
    assert character["curvature"] == 0
    assert character["de_rham_rank_contribution"] == 0
    assert character["physical_evaluation"] == "source_underdetermined"
    assert no_go["torsion_order"] == 3
    assert no_go["checks"]["three_torsion_scalar_extension_is_zero"] is True

    order_mismatch = {
        "nearby_line_descent_type": "mu2_sheet_odd",
        "all_soft_character_order": 3,
        "canonical_hom_from_order3_to_mu2_supplied": False,
    }
    packet = {
        "schema": "marici.cosmology-triple-incidence-all-soft-separation.v1",
        "nearby_line": "triple-incidence universal logarithmic rank-one line",
        "all_soft_candidate": "flat relative Z/3 differential character",
        "nearby_line_constructed": True,
        "all_soft_character_constructed": True,
        "all_soft_is_separated_specialization": True,
        "order_and_descent": order_mismatch,
        "support_comparison": {
            "generic_positive_chain_activates_nearby_line": False,
            "all_soft_origin_is_boundary_specialization_not_generic_chamber": True,
        },
        "pairing_comparison": {
            "all_soft_physical_evaluation": character["physical_evaluation"],
            "Cayley_Menger_relative_chain_coupling_constructed": False,
            "nearby_line_physical_twisted_pairing_constructed": False,
        },
        "rank_comparison": {
            "all_soft_de_rham_rank_contribution": 0,
            "order_three_scalar_repairs_rank_defect": False,
        },
        "conclusion": (
            "the existing all-soft Z/3 differential character is a separated "
            "torsion readout and does not activate the sheet-odd triple-incidence "
            "nearby line as a physical period"
        ),
        "next_gate": (
            "derive a new source map from the all-soft relative character to the "
            "mu2-odd nearby coefficient, or keep the two sectors disjoint"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
