#!/usr/bin/env python3
"""Aggregate and integrity-check all eight-node analytical cell coverage."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
RESULTS = ROOT / "results"
SOURCES = {
    "semantic_complex": "seven_transition_order_ideal_complex.json",
    "triangle_prototypes": "seven_transition_triangle_prototypes.json",
    "tetrahedron_prototypes": "seven_transition_tetrahedron_prototypes.json",
    "four_syzygies": "seven_transition_four_syzygies.json",
    "schedule_census": "eight_factorial_schedule_coverage.json",
    "geometric_f_vector": "esd7_analytical_cell_coverage.json",
    "asymptotic_face": "asymptotic_face_234_propagation.json",
    "geometric_registry": "esd7_tetrahedron_prototype_registry.json",
}

def load(name):
    path = RESULTS / name
    return path, json.loads(path.read_text())

loaded = {key: load(name) for key, name in SOURCES.items()}
data = {key: pair[1] for key, pair in loaded.items()}

schedule = data["schedule_census"]
coverage = schedule["coverage"]
status_counts = {
    state: sum(row["s"] == state for row in coverage.values())
    for state in ("admissible", "empty")
}
constructors = sorted({row["a"] for row in coverage.values()})
geometry = data["geometric_registry"]

checks = {
    "all_source_artifacts_pass": all(item.get("passed", True) for item in data.values()),
    "eight_factorial_exact": schedule["schedule_count"] == 40320 == len(coverage),
    "schedule_keys_unique": len(set(coverage)) == 40320,
    "schedule_partition_exact": status_counts == {"admissible": 28, "empty": 40292},
    "schedule_constructors_resolve": constructors == [
        "empty_typed_fiber", "residual_augmented_relative_feature_nerve"
    ],
    "semantic_f_vector_exact": data["semantic_complex"]["full_order_complex_f_vector"] == [18,112,353,645,716,478,177,28],
    "triangle_registry_complete": data["triangle_prototypes"]["prototype_count"] == 8,
    "three_transition_registry_complete": data["tetrahedron_prototypes"]["critical_triple_count"] == 12,
    "four_syzygy_registry_complete": data["four_syzygies"]["critical_four_count"] == 11,
    "geometric_f_vector_exact": data["geometric_f_vector"]["f_vector"] == [120,560,784,343],
    "geometric_registry_exact": geometry["tetrahedron_count"] == len(geometry["cells"]) == 343,
    "geometric_ids_unique": len({cell["id"] for cell in geometry["cells"]}) == 343,
    "all_geometric_forms_nonempty": all(cell["analytical_form"] and len(cell["face_prototypes"]) == 4 for cell in geometry["cells"]),
}
assert all(checks.values()), checks

artifacts = {
    key: {
        "path": f"research/voevodsky/results/{path.name}",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    for key, (path, _) in loaded.items()
}
result = {
    "schema": "marici.voevodsky.complete-eight-node-analytical-coverage.v1",
    "claim": "Every one of the 8! unrestricted elementary schedules has a typed analytical disposition.",
    "schedule_coverage": {
        "total": 40320,
        "nonempty_admissible": 28,
        "empty_dependency_obstructed": 40292,
        "constructors": constructors,
    },
    "semantic_cell_coverage": {
        "f_vector": [18,112,353,645,716,478,177,28],
        "triangle_prototypes": 8,
        "critical_three_transition_prototypes": 12,
        "critical_four_transition_syzygies": 11,
        "dimensions_four_through_seven": "unique fillers in the residual-augmented ordinary nerve",
    },
    "geometric_cell_coverage": {
        "complex": "esd_7(Delta^3)",
        "f_vector": [120,560,784,343],
        "tetrahedra_individually_registered": 343,
    },
    "artifacts": artifacts,
    "checks": checks,
    "scope": "typed signed/relative analytical forms at finite regulators",
    "nonclaims": [
        "40292 obstructed schedules are nonempty cells",
        "40320 schedules equal 343 geometric tetrahedra",
        "ordinary positive-Hilbert realization at infinite regulator",
        "external arithmetic, determinant, Evans, or RH consequences",
    ],
    "passed": True,
}
out = RESULTS / "complete_eight_node_analytical_coverage.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
