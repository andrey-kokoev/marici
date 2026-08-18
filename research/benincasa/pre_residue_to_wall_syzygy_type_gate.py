"""Type gate between the pre-residue top line and residue-surface syzygies."""

from __future__ import annotations

import json


def main() -> None:
    pre_residue = {
        "variables": 3,
        "poles": ["q_g1", "q_g2", "q_G12"],
        "full_rank": 21,
        "proper_face_rank": 20,
        "proper_top_rank": 1,
    }
    residue_surface = {
        "variables": 2,
        "residue_taken_at": "q_G12",
        "walls": ["q_g1", "q_g2", "q_g3", "q_g23", "q_g31"],
        "shared_wall_relative_rank": 15,
        "absolute_rank": 9,
        "shared_wall_quotient_rank": 6,
        "minimal_log_derivation_rank": 3,
    }
    assert pre_residue["full_rank"] - pre_residue["proper_face_rank"] == 1
    assert residue_surface["shared_wall_relative_rank"] - residue_surface["absolute_rank"] == 6
    assert pre_residue["poles"] != residue_surface["walls"][:3]

    print(
        json.dumps(
            {
                "schema": "marici.pre-residue-to-wall-syzygy-type-gate.v1",
                "pre_residue_complex": pre_residue,
                "residue_surface_complex": residue_surface,
                "direct_identification_of_targets_typed": False,
                "missing_map": "Poincare residue on retained pivot presentations, followed by wall localization",
                "admissible_syzygy_target_rank_before_source_line_restriction": 6,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
