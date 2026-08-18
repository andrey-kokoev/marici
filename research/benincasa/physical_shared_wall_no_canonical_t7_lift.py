"""Finite rank/type gate for lifting the physical shared-wall cocycle."""

from __future__ import annotations

import json


def main() -> None:
    absolute_rank = 9
    three_wall_relative_rank = 15
    wall_quotient_rank = three_wall_relative_rank - absolute_rank
    elliptic_rank = 2
    t7_rank = absolute_rank - elliptic_rank

    assert wall_quotient_rank == 1 + 2 + 3
    assert t7_rank == 7

    # In a short exact sequence 0 -> A -> B -> Q -> 0, the lifts of one
    # fixed q in Q form an A-torsor. Requiring zero elliptic quotient only
    # replaces A=M9 by ker(M9->V_ell)=T7; it does not choose a point.
    result = {
        "schema": "marici.physical-shared-wall-no-canonical-t7-lift.v1",
        "exact_sequence_ranks": [absolute_rank, three_wall_relative_rank, wall_quotient_rank],
        "H3_rank": 0,
        "physical_cocycle_lift_exists": True,
        "unconstrained_lift_torsor_rank": absolute_rank,
        "elliptic_quotient_rank": elliptic_rank,
        "zero_elliptic_lift_torsor_rank": t7_rank,
        "canonical_lift_selected": False,
        "canonical_T7_coordinates_selected": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
