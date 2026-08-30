"""Deck and cyclic characters of the second-grade endpoint-node packet."""

from __future__ import annotations

import json


def main():
    local_node_count = 4
    cyclic_occurrences = 3
    assembled_rank = local_node_count * cyclic_occurrences

    # A threefold A1 Milnor fiber has vanishing sphere S^3.  The cover deck
    # w -> -w reflects one coordinate of S^3, hence has degree -1.
    vanishing_sphere_dimension = 3
    reflected_coordinates = 1
    deck_degree = -1 if reflected_coordinates % 2 else 1
    assert deck_degree == -1

    # Four local labels, each forming a free C3 orbit.
    character = {
        "identity": assembled_rank,
        "rho": 0,
        "rho2": 0,
        "deck": deck_degree * assembled_rank,
        "deck_rho": 0,
        "deck_rho2": 0,
    }
    assert character == {
        "identity": 12,
        "rho": 0,
        "rho2": 0,
        "deck": -12,
        "deck_rho": 0,
        "deck_rho2": 0,
    }

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-node-deck-character.v1",
        "local_A1_complex_dimension": 3,
        "vanishing_sphere": f"S^{vanishing_sphere_dimension}",
        "square_root_deck_action": "reflection of one vanishing-sphere coordinate",
        "local_deck_character": deck_degree,
        "local_physical_node_rank": local_node_count,
        "cyclic_occurrence_count": cyclic_occurrences,
        "assembled_rank_before_relations": assembled_rank,
        "C3_times_mu2_character": character,
        "required_physical_operation": (
            "source-normalized anti-trace of the positive-sheet relative hemisphere"
        ),
        "ordinary_sheet_trace_on_anti_invariant_node_line": 0,
        "status": "second_grade_node_packet_is_mu2_anti_invariant_and_C3_regular",
        "scope": (
            "standard local A1 topology and source occurrence labels; "
            "the anti-trace normalization, Picard--Lefschetz comparison signs, "
            "and global node relations remain uncomputed"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
