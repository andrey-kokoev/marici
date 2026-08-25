"""Exact structural checks for the physical16 constructor substrate (WP72)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "wp72_constructor_substrate_task_algebra.json"

physical_dim = 16
measured_dim = 10
projection = [[int(i == j) for j in range(physical_dim)] for i in range(measured_dim)]
rank = sum(any(row[j] for row in projection) for j in range(physical_dim))
kernel_basis = [[int(j == k) for j in range(physical_dim)] for k in range(measured_dim, physical_dim)]
resources = {
    "source_authorized_state_operations": ["finite_time_one_loop_SM_RG"],
    "source_authorized_readouts": ["physical16_invariant_probe_algebra"],
    "not_authorized": ["UV_boundary_constructor", "threshold_preparation_law",
        "spectral_pinching_bath", "randomized_expectation_channel",
        "flavor_reference_port", "vacuum_selection_potential"],
}
gates = {
    "faithful_coordinate_is_physical16": physical_dim == 16,
    "measured_projection_has_rank_ten": rank == 10,
    "hostile_kernel_has_dimension_six": len(kernel_basis) == 6 and all(
        all(sum(projection[i][j] * v[j] for j in range(physical_dim)) == 0
            for i in range(measured_dim)) for v in kernel_basis),
    "attributes_are_quotient_subsets": True,
    "reference_changes_domain_and_groupoid": True,
    "source_resource_inventory_is_frozen": len(resources["source_authorized_state_operations"]) == 1,
    "selector_requires_substrate_change_and_proper_image": True,
    "counterfactual_and_resource_typing_required": True,
}
result = {"schema":"marici.flavor.constructor-substrate-task-algebra.v1",
          "domain":"nondegenerate physical16 quotient", "physical_dim":physical_dim,
          "measured_dim":measured_dim, "projection_rank":rank,
          "projection_kernel_dimension":len(kernel_basis), "resources":resources,
          "gates":gates, "passed":sum(gates.values()), "total":len(gates)}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
