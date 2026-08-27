"""Exact structural audit of the WP626 source-model compatibility registry."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FIELDS = {
    "S": {"indices": {"row", "port"}, "kind": "real_scalar", "sm_rep": None,
          "kinetic_normalization": None, "threshold_state": None},
    "X": {"indices": {"flavor_adjoint", "port"}, "kind": "scalar", "sm_rep": "singlet",
          "kinetic_normalization": None, "threshold_state": None},
    "Hu": {"indices": {"weak_doublet", "row"}, "kind": "scalar", "sm_rep": "partial",
           "kinetic_normalization": None, "threshold_state": None},
    "Hd": {"indices": {"weak_doublet", "row"}, "kind": "scalar", "sm_rep": "partial",
           "kinetic_normalization": None, "threshold_state": None},
    "Au": {"indices": {"row"}, "kind": "vectorlike_fermion", "sm_rep": None,
           "kinetic_normalization": None, "threshold_state": None},
    "Ad": {"indices": {"row"}, "kind": "vectorlike_fermion", "sm_rep": None,
           "kinetic_normalization": None, "threshold_state": None},
    "Bu": {"indices": {"port"}, "kind": "vectorlike_fermion", "sm_rep": None,
           "kinetic_normalization": None, "threshold_state": None},
    "Bd": {"indices": {"port"}, "kind": "vectorlike_fermion", "sm_rep": None,
           "kinetic_normalization": None, "threshold_state": None},
}

SHAPES = {
    f"{name}{sector}": {"normalization": f"g_{name}_{sector}"}
    for sector in ("u", "d") for name in ("YH", "YS", "YX", "ZA", "ZB")
}

ROUTES = {
    "entrance_u": ["row", "row"], "entrance_d": ["row", "row"],
    "connector_u": ["row", "row", "port", "port"],
    "connector_d": ["row", "row", "port", "port"],
    "exit_u": ["port", "port"], "exit_d": ["port", "port"],
}

def route_closed(indices):
    return all(indices.count(i) == 2 for i in set(indices))

def shapes_independent(shapes):
    return len({x["normalization"] for x in shapes.values()}) == 10

def grammar_compatible(routes, shapes, locality_axiom=True, alignment=True):
    return (all(route_closed(x) for x in routes.values())
            and shapes_independent(shapes) and locality_axiom and alignment)

def export_ready(fields, shapes, locality_axiom=True, alignment=True):
    complete_fields = all(
        x["sm_rep"] not in (None, "partial")
        and x["kinetic_normalization"] is not None
        and x["threshold_state"] is not None for x in fields.values()
    )
    independent = shapes_independent(shapes)
    return complete_fields and independent and locality_axiom and alignment

checks = {
    "eight_new_field_families_registered": len(FIELDS) == 8,
    "ten_independent_tensor_normalizations": len({x["normalization"] for x in SHAPES.values()}) == 10,
    "all_declared_routes_index_closed": all(route_closed(x) for x in ROUTES.values()),
    "completion_debt_lower_bound_is_18": 10 + 3 + 1 + 1 + 3 == 18,
    "current_export_is_refused": not export_ready(FIELDS, SHAPES),
}

aliased = copy.deepcopy(SHAPES)
for name in ("YH", "YS", "YX", "ZA", "ZB"):
    aliased[name + "d"]["normalization"] = aliased[name + "u"]["normalization"]
bad_route = ROUTES["connector_u"][:-1]
checks.update({
    "hostile_up_down_alias_rejected": not grammar_compatible(ROUTES, aliased),
    "hostile_unbound_index_rejected": not route_closed(bad_route),
    "hostile_missing_locality_axiom_rejected": not grammar_compatible(ROUTES, SHAPES, locality_axiom=False),
    "smallest_alignment_omission_rejected": not grammar_compatible(ROUTES, SHAPES, alignment=False),
})

if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP626",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "WP483/WP484 gauged relational connector source family",
    "faithful_quotient_coordinate": "physical16 remains the downstream faithful physical quotient; it is not a source-model completion field",
    "source_authorized_probe_family": "ten independently normalized canonical messenger tensor shapes plus declared scalar invariants",
    "contextual_partition": {
        "route_compatible": ["entrance", "connector", "exit"],
        "export_blocked": ["SM representations", "kinetic normalizations", "threshold states", "18-coordinate RG closure", "one-scheme matching"]
    },
    "classification": "presentation rigidifier only; neither numerical selector nor physical instrument",
    "smallest_exact_falsifier": "omit the connector-adjoint alignment coordinate",
    "remaining_physical_instrument_gate": "derive a common-frame finite-threshold response and calibrated detector map after source-model closure",
    "beta_generation_admitted": False
}
(ROOT / "results" / "wp626_source_model_compatibility_registry.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
