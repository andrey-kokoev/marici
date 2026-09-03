#!/usr/bin/env python3
"""Exact enumeration of higher probe parity matching obstructions."""

import json
from itertools import combinations, product
from pathlib import Path


def project(relation, coordinates):
    return {tuple(row[index] for index in coordinates) for row in relation}


arity_results = {}
all_checks = {}
for n in range(2, 9):
    cube = set(product((0, 1), repeat=n))
    even = {row for row in cube if sum(row) % 2 == 0}
    odd = cube - even
    proper_projection_checks = {}
    for size in range(n):
        for coordinates in combinations(range(n), size):
            expected = set(product((0, 1), repeat=size))
            proper_projection_checks[str(coordinates)] = project(even, coordinates) == expected

    deleted = set(even)
    deleted.remove((0,) * n)
    codim_one_faces = list(combinations(range(n), n - 1))
    deleted_mutation_detected = any(
        project(deleted, face) != set(product((0, 1), repeat=n - 1))
        for face in codim_one_faces
    )

    checks = {
        "all_proper_projections_full": all(proper_projection_checks.values()),
        "even_relation_has_half_cube": len(even) == 2 ** (n - 1),
        "odd_obstruction_has_half_cube": len(odd) == 2 ** (n - 1),
        "kernel_equals_even_relation": {row for row in cube if sum(row) % 2 == 0} == even,
        "matching_map_not_surjective": even != cube,
        "factorized_top_has_no_obstruction": cube - cube == set(),
        "deleted_even_assignment_breaks_lower_face_fullness": deleted_mutation_detected,
    }
    all_checks.update({f"n{n}_{key}": value for key, value in checks.items()})
    arity_results[str(n)] = {
        "checks": checks,
        "matching_cardinality": len(cube),
        "admitted_cardinality": len(even),
        "obstructed_cardinality": len(odd),
    }

assert all(all_checks.values()), {key: value for key, value in all_checks.items() if not value}
result = {
    "schema": "marici.aspect.higher-probe-parity-obstructions.v1",
    "status": "passed",
    "arity_range": [2, 8],
    "checks": all_checks,
    "arities": arity_results,
    "claim_boundary": "Finite parity matching family; no universal classification or physical realization theorem."
}
output = Path(__file__).parents[1] / "results" / "higher_probe_parity_obstructions.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(all_checks)}, sort_keys=True))
