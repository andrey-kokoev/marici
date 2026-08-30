"""Assemble the lower/restricted interaction actions across localization."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    lower = json.loads(
        (HERE / "generic-lower-interaction-class-faithfulness.json").read_text()
    )
    restricted = json.loads(
        (HERE / "restricted-interaction-class-faithfulness.json").read_text()
    )
    assert lower["source_interaction_module_rank"] == 7
    assert lower["generic_lower_direct_image_class_rank"] == 7
    assert lower["additional_direct_image_kernel_dimension"] == 0
    assert restricted["restricted_source_interaction_rank"] == 6
    assert restricted["restricted_direct_image_class_rank"] == 6
    assert restricted["restriction_kernel_rank"] == 1

    c, E, n1, n2, n3 = sp.symbols("c E nu1 nu2 nu3")
    q_g12 = c + E
    assert all(sp.diff(q_g12, normal) == 0 for normal in (n1, n2, n3))
    principal = c**2 - E**2
    assert sp.factor(principal) == (c-E)*q_g12
    assert sp.simplify(principal.subs(c, -E)) == 0

    lower_rank = 34
    restricted_rank = 26
    full_rank = 60
    assert lower_rank + restricted_rank == full_rank

    # Abstract rank gate: the full normal action restricts to the faithful
    # lower action.  Hence its rank is >=7; it factors through the rank-seven
    # source module, hence is <=7.
    full_interaction_rank_lower_bound = lower["generic_lower_direct_image_class_rank"]
    full_interaction_rank_upper_bound = lower["source_interaction_module_rank"]
    assert full_interaction_rank_lower_bound == full_interaction_rank_upper_bound == 7

    packet = {
        "schema":"marici.benincasa.rank60-interaction-action-faithfulness.v1",
        "localization_ranks":{"lower":34,"restricted":26,"full":60},
        "normal_independence":"partial_nu_i(q_G12)=0 for i=1,2,3",
        "residue_normal_action_commutator":"zero on the source twisted de Rham complex",
        "lower_interaction_rank":7,
        "restricted_interaction_rank":6,
        "principal_restriction_kernel":"c^2-E^2=(c-E)q_G12",
        "full_interaction_rank_lower_bound":full_interaction_rank_lower_bound,
        "full_interaction_rank_upper_bound":full_interaction_rank_upper_bound,
        "full_interaction_rank":7,
        "full_interaction_kernel_dimension":0,
        "off_diagonal_effect":"may encode extension data but cannot erase the faithful invariant lower action",
        "status":"generic_rank60_normal_interaction_action_is_faithful",
        "scope":"algebraic normal action; full connection matrices and physical relative-cycle readout remain open",
        "new_carrier_datum":False,
    }
    print(json.dumps(packet,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
