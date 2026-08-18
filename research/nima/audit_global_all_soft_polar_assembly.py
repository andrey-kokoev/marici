#!/usr/bin/env python3
"""Global C3 assembly of the fifteen locally acyclic all-soft polar cubes."""

import json
from pathlib import Path


def main():
    orbit_count = 5
    orbit_size = 3
    point_count = orbit_count * orbit_size
    local_dimensions_one_column = [1, 4, 6, 4, 1]
    local_ranks_one_column = [1, 3, 3, 1]
    column_count = 2

    global_dimensions = [
        point_count * column_count * d for d in local_dimensions_one_column
    ]
    global_ranks = [
        point_count * column_count * r for r in local_ranks_one_column
    ]
    homology = [
        global_dimensions[k]
        - (global_ranks[k] if k < 4 else 0)
        - (global_ranks[k-1] if k > 0 else 0)
        for k in range(5)
    ]
    assert homology == [0, 0, 0, 0, 0]

    degree_characters = [
        [point_count * column_count * d, 0, 0]
        for d in local_dimensions_one_column
    ]
    packet = {
        "free_C3_orbits": orbit_count,
        "orbit_size": orbit_size,
        "all_soft_point_count": point_count,
        "local_columns": ["diagonal C", "anti-diagonal M"],
        "global_complex_dimensions": global_dimensions,
        "global_differential_ranks": global_ranks,
        "global_homology_dimensions": homology,
        "degreewise_C3_characters": degree_characters,
        "cyclic_transport": "conjugates local differentials and preserves exactness",
        "global_algebraic_polar_complex_acyclic": True,
        "physical_selection_inferred": False,
    }
    out = Path(__file__).with_name("global-all-soft-polar-assembly.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
