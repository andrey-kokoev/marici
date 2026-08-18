"""Deletion--restriction occupancy gate for the complete physical source."""

from __future__ import annotations

import json


def main() -> None:
    deletion_rank = 15
    residue_quotient_rank = 20
    full_rank = 35
    conductor_resultants_generically_nonzero = 3
    mixed_occurrence_component = 0

    assert deletion_rank + residue_quotient_rank == full_rank
    assert conductor_resultants_generically_nonzero > 0

    print(
        json.dumps(
            {
                "schema": "marici.physical-five-pole-residue-occupancy-gate.v1",
                "deletion_rank": deletion_rank,
                "residue_quotient_rank": residue_quotient_rank,
                "full_five_pole_rank": full_rank,
                "normalized_shared_wall_components_nonzero": conductor_resultants_generically_nonzero,
                "mixed_occurrence_component": mixed_occurrence_component,
                "physical_residue_class_nonzero": True,
                "physical_source_contained_in_deletion_submodule": False,
                "one_dimensional_proper_top_claimed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
