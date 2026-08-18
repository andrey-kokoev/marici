"""Type gate for reconstructing the rank-35 physical connection from its blocks."""

from __future__ import annotations

import json


def main() -> None:
    deletion_rank = 15
    residue_rank = 20
    total_rank = 35
    source_residue_columns_known = 1
    off_diagonal_scalar_entries = deletion_rank * residue_rank

    assert deletion_rank + residue_rank == total_rank
    assert source_residue_columns_known < residue_rank

    print(
        json.dumps(
            {
                "schema": "marici.physical-rank35-extension-type-gate.v1",
                "exact_sequence_ranks": [deletion_rank, total_rank, residue_rank],
                "fiber_sequence_splits_noncanonically": True,
                "connection_sequence_splitting_established": False,
                "source_Poincare_residue_column_known": True,
                "source_columns_known": source_residue_columns_known,
                "off_diagonal_connection_block_shape": [deletion_rank, residue_rank],
                "off_diagonal_scalar_entry_count_before_constraints": off_diagonal_scalar_entries,
                "rank_data_plus_source_column_determine_connection": False,
                "missing_datum": "horizontal extension class / off-diagonal Gauss-Manin block modulo triangular gauge",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
