#!/usr/bin/env python3
"""Typed inventory for the generic rank-nine to rank-twelve relative map."""

import json
from pathlib import Path


def main():
    absolute_rank = 9
    wall_rank = 3
    relative_rank = 12
    assert absolute_rank + wall_rank == relative_rank

    infinity_kernel = 7
    elliptic_quotient = 2
    assert infinity_kernel + elliptic_quotient == absolute_rank

    nullities = {
        "one_wall_degree5": 95,
        "two_wall_degree5": 346,
        "top_six_order_degree5": 664,
    }
    assert all(value > 0 for value in nullities.values())

    packet = {
        "surface_model": "S_E with finite marked wall W=W1 union W2",
        "canonical_absolute_object": "M_q^(9)=H^2(S_E;K)",
        "canonical_relative_object": "M_mark^(12)=H^2(S_E\\W;K)",
        "canonical_sequence": "0 -> M_q^(9) --j*--> M_mark^(12) --Res_W--> H^1(W)(-1) -> 0",
        "ranks": [0, absolute_rank, relative_rank, wall_rank, 0],
        "infinity_sequence": "0 -> T_7 -> M_q^(9) -> V_ell(-1) -> 0",
        "infinity_ranks": [0, infinity_kernel, absolute_rank, elliptic_quotient, 0],
        "source_basis_matrix_status": "not constructed",
        "full_bivariate_rank12_connection_status": "not constructed",
        "existing_packet_exact_lift_nullities": nullities,
        "existing_packets_uniquely_determine_connection": False,
        "required_engine": "source-normalized four-stratum relative de Rham reduction",
        "strata": ["absolute q-only", "wall W1", "wall W2", "same-sheet top intersection"],
        "post_hoc_splitting_allowed": False,
        "Q_search_scope": "off-diagonal elliptic-Tate/marked extension after canonical engine only",
    }
    out = Path(__file__).with_name("marked-relative-source-map-inventory.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
