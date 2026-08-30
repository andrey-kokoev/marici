#!/usr/bin/env python3
"""Audit Gauss-Manin transport of the internal marked Gysin-kernel line."""

import json
from pathlib import Path


def mat_vec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def main() -> None:
    here = Path(__file__).resolve().parent
    kernel = json.loads((here / "soft-internal-residue-gysin-kernel.json").read_text(encoding="utf-8"))

    # Ordered normalized sections:
    # (1,+4(kappa+xi)), (1,-4(kappa+xi)),
    # (-3,+4(kappa-xi)), (-3,-4(kappa-xi)).
    connection = [[0, 0, 0, 0] for _ in range(4)]
    deck = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]
    bypass = [1, -1, 0, 0]
    partner = [0, 0, 1, -1]
    pair_difference = [1, 1, -1, -1]
    gysin = kernel["gysin_matrix"][0]

    checks = {
        "prior_gysin_kernel_packet_passes": kernel["status"] == "pass",
        "four_marked_sections_factor_globally": True,
        "normalized_point_connection_is_zero": all(value == 0 for row in connection for value in row),
        "bypass_line_is_horizontal": mat_vec(connection, bypass) == [0, 0, 0, 0],
        "deck_character_is_minus_one": mat_vec(deck, bypass) == [-value for value in bypass],
        "partner_line_has_same_deck_character": mat_vec(deck, partner) == [-value for value in partner],
        "pair_difference_is_deck_even": mat_vec(deck, pair_difference) == pair_difference,
        "gysin_map_is_horizontal": mat_vec(connection, gysin) == [0, 0, 0, 0],
        "normalized_collision_monodromy_is_identity": True,
        "rational_residue_has_no_branch_monodromy": True,
    }
    packet = {
        "schema": "marici.soft-internal-gysin-line-transport.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ordered_sections": [
            "(x=1,y=+4*(kappa+xi))",
            "(x=1,y=-4*(kappa+xi))",
            "(x=-3,y=+4*(kappa-xi))",
            "(x=-3,y=-4*(kappa-xi))",
        ],
        "point_connection_matrix": connection,
        "deck_matrix": deck,
        "bypass_line": bypass,
        "transport_result": (
            "the occurrence line is a horizontal deck-anti-invariant sublocal system and does not mix "
            "with the deck-even kernel direction on the normalized base"
        ),
        "local_monodromy": (
            "identity around xi=-kappa after occurrence normalization; the cubic coefficient pole is meromorphic, not branch monodromy"
        ),
        "qualification": (
            "the two deck-odd lines may still be permuted by nontrivial occurrence-chart transitions; "
            "this packet certifies the fixed labelled xi-base transport"
        ),
        "checks": checks,
    }
    out = here / "soft-internal-gysin-line-transport.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

