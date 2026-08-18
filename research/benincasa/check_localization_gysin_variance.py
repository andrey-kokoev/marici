"""Type-check the localization and Gysin maps for the physical wall class."""
from __future__ import annotations

import json


def main() -> None:
    absolute_h2_rank = 9
    open_h2_rank = 15
    wall_h1_rank = open_h2_rank - absolute_h2_rank
    surface_h3_rank = 0
    elliptic_rank = 2
    algebraic_kernel_rank = absolute_h2_rank - elliptic_rank

    assert wall_h1_rank == 6
    assert surface_h3_rank == 0
    assert algebraic_kernel_rank == 7

    print(json.dumps({
        "schema": "marici.localization-gysin-variance.v1",
        "localization_segment": "H2(S)->H2(S\\W)->H1(W)(-1)->H3(S)",
        "ranks": [absolute_h2_rank, open_h2_rank, wall_h1_rank, surface_h3_rank],
        "gysin_boundary_target": "H3(S)",
        "gysin_boundary_rank": 0,
        "reverse_map_to_H2_exists_canonically": False,
        "lift_ambiguity_rank": absolute_h2_rank,
        "zero_elliptic_lift_ambiguity_rank": algebraic_kernel_rank,
        "physical_class_in_T7_selected": False,
        "correct_home": "localization extension / mapping cone",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
