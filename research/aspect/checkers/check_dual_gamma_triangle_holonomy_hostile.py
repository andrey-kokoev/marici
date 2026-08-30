import json
from pathlib import Path


root = Path(__file__).parents[1]
marici = root.parents[1]
records = [
    json.loads((marici / "research" / "benincasa" / "results" / name).read_text(encoding="utf-8"))
    for name in (
        "rank26-gamma-bockstein-transition-naturality.json",
        "rank26-gamma-bockstein-transition-naturality-p32003.json",
    )
]


def transport_beta(beta: int, edge_unit: int) -> int:
    return edge_unit * beta


def triangle(edge_units: tuple[int, int, int], beta0: int = 1) -> tuple[list[int], int]:
    values = [beta0]
    for unit in edge_units:
        values.append(transport_beta(values[-1], unit))
    return values, values[-1] - beta0


closed_units = (-1, -1, 1)
hostile_units = (-1, 1, 1)
closed_values, closed_residual = triangle(closed_units)
hostile_values, hostile_residual = triangle(hostile_units)

checks = {
    "existing_edge_passes_at_two_primes": all(record["passed"] for record in records),
    "existing_edge_has_fixed_orientation_sign": all(record["orientation_sign"] == -1 for record in records),
    "existing_edge_intertwines_all_gamma_generators": all(record["gamma_derivative_transport_failures"] == 0 for record in records),
    "closed_triangle_has_zero_holonomy_residual": closed_residual == 0,
    "hostile_edges_are_each_nonzero_isomorphisms": all(unit in (-1, 1) for unit in hostile_units),
    "hostile_local_naturality_can_be_propagated_edgewise": hostile_values == [1, -1, -1, -1],
    "hostile_triangle_has_nontrivial_holonomy": hostile_residual == -2,
    "edgewise_naturality_does_not_imply_cycle_closure": closed_residual != hostile_residual,
}

result = {
    "schema": "marici.aspect.dual-gamma-triangle-holonomy-hostile.v1",
    "status": "hostile_constructed" if all(checks.values()) else "checker_failure",
    "checks": checks,
    "closed_control": {"edge_units": closed_units, "transported_beta_values": closed_values, "cycle_residual": closed_residual},
    "hostile": {"edge_units": hostile_units, "transported_beta_values": hostile_values, "cycle_residual": hostile_residual},
    "conclusion": "three invertible edgewise-natural Bockstein transports need not close; the product of signed edge units is the next scalar holonomy obstruction",
    "decisive_source_test": "construct all three dual-gamma edges independently and verify that their signed composite is the identity on both the rank-26 quotient and the common Bockstein line",
}

out = root / "results" / "dual_gamma_triangle_holonomy_hostile.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "hostile_constructed" else 1)
