#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
contract_path = ROOT / "research/aspect/contracts/category-lattice.v1.json"
result_path = ROOT / "research/aspect/results/category_lattice.json"
c = json.loads(contract_path.read_text(encoding="utf-8"))

axes = c["gate_axes"]
scales = c["assembly_scale"]
expected_axes = {"carrier", "action", "observation", "estimate"}
required_cells = {
    "composition_square", "restriction_naturality_square",
    "affine_cocycle_triangle", "associator_pentagon",
    "mixed_action_observation_square", "completion_limit_cone"
}
required_obstructions = {
    "action_kernel", "observer_kernel", "reference_holonomy",
    "affine_cocycle_residual", "associator_residual",
    "nonuniform_margin", "missing_source_authority"
}

checks = {
    "four_axes": set(axes) == expected_axes,
    "three_gate_values_each": all(len(v) == 3 and len(set(v)) == 3 for v in axes.values()),
    "five_scales": scales == ["local", "packet", "finite_system", "pro_system", "completion"],
    "partial_join_typed": "undefined" in c["join"] and "source-authorized" in c["join"],
    "affine_two_coordinate_observer": c["observer"]["increment_coordinates"] == [
        "primitive_fluctuation", "square_compensator"
    ],
    "coherence_cells_complete": required_cells <= set(c["coherence_cells"]),
    "obstructions_complete": required_obstructions <= set(c["obstruction_labels"]),
    "finite_does_not_imply_completion": "does not promote" in c["propagation"]["upward"],
    "axes_do_not_imply_each_other": "does not imply" in c["propagation"]["sideways"],
    "action_precedes_observation": (
        c["active_theta_placement"]["action"].startswith("incomplete_")
        and c["active_theta_placement"]["observation"] == "blocked_until_action_splitting"
    ),
    "domain_authority_remains_open": len(c["scc_coverage"]["still_requires_domain_packets"]) == 6
}

out = {
    "schema": "marici.aspect.category-lattice-check.v1",
    "contract": str(contract_path.relative_to(ROOT)).replace("\\", "/"),
    "finite_cell_count": len(scales) * math.prod(len(v) for v in axes.values()),
    "checks": checks,
    "passed": all(checks.values()),
    "claim": "schema coherence only; no domain packet or physical apparatus is certified"
}
result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
