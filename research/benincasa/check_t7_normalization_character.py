"""Determine the surface-normalization character of the Gysin kernel."""
from __future__ import annotations

import json

import sympy as sp

import derive_nine_master_residue_connection as source


def main() -> None:
    a, b, k1 = sp.symbols("a b K1")
    masters = source.build_masters(a, b, k1)
    powers = {
        master.name: (-1 if master.pole == "simple" else -3)
        for master in masters
    }
    characters = {name: (-1 if power % 2 else 1) for name, power in powers.items()}

    assert len(masters) == 9
    assert set(characters.values()) == {-1}

    master_rank = 9
    elliptic_rank = 2
    kernel_rank = master_rank - elliptic_rank
    assert kernel_rank == 7

    print(json.dumps({
        "schema": "marici.t7-normalization-character.v1",
        "master_w_powers": powers,
        "master_characters": characters,
        "nine_master_minus_rank": master_rank,
        "nine_master_plus_rank": 0,
        "gysin_kernel_minus_rank": kernel_rank,
        "gysin_kernel_plus_rank": 0,
        "compatible_target_multiplicity": kernel_rank,
        "character_selects_unique_line": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
