"""Scope gate separating the rank-21 subpacket from the physical five-pole source."""

from __future__ import annotations

import json


def main() -> None:
    three_pole = {
        "denominators": ["q_g1", "q_g2", "q_G12"],
        "rank": 21,
        "proper_top_rank": 1,
        "tested_source_column": "1/(q_g1*q_g2*q_G12)",
    }
    physical = {
        "family_23": ["q_g1", "q_g2", "q_g3", "q_G12", "q_g23"],
        "family_31": ["q_g1", "q_g2", "q_g3", "q_G12", "q_g31"],
        "rank_each": 35,
        "source_occurrence_factor": "1/q_g23 + 1/q_g31",
    }
    assert len(three_pole["denominators"]) == 3
    assert len(physical["family_23"]) == len(physical["family_31"]) == 5
    assert set(three_pole["denominators"]) < set(physical["family_23"])

    print(
        json.dumps(
            {
                "schema": "marici.physical-source-scope-correction.v1",
                "three_pole_subpacket": three_pole,
                "complete_physical_source": physical,
                "entry_653_proves_subpacket_top_occupancy": True,
                "entry_653_proves_complete_physical_source_occupancy": False,
                "required_next_complex": "retained-pivot five-pole rank-35 complex",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
