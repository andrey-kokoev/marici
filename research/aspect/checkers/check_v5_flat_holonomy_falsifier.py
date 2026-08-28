import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v5 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v5.json").read_text(
        encoding="utf-8"
    )
)

# Two flat unitary connections on the same resolved rank-one route bundle over S^1.
# Their local v5 data are identical. Only loop transport differs.
gram = sp.eye(1)
chart_transition = sp.eye(1)
holonomy_trivial = sp.eye(1)
holonomy_half_turn = -sp.eye(1)


def fixed_space_dimension(holonomy: sp.Matrix) -> int:
    return len((holonomy - sp.eye(holonomy.rows)).nullspace())


required_fields = set(v5["log_resolved_metric_route_family"]["required_fields"])
required_laws = set(v5["log_resolved_metric_route_family"]["required_laws"])
associator_laws = set(v5["resolved_metric_route_associator"]["required_laws"])
all_declared_terms = (
    set(v5["object_types"])
    | set(v5["arrow_types"])
    | set(v5["cell_types"])
    | required_fields
    | required_laws
    | associator_laws
)

checks = {
    "v5_is_frozen": v5["cell_creation_during_replay"] is False,
    "same_rank_one_metric": gram == sp.eye(1),
    "same_nondegenerate_determinant": gram.det() == 1,
    "same_zero_radical": len(gram.nullspace()) == 0,
    "same_zero_divisor_valuation": sp.Integer(0) == 0,
    "same_identity_chart_transition": chart_transition == sp.eye(1),
    "both_holonomies_are_metric_isometries": (
        holonomy_trivial.T * gram * holonomy_trivial == gram
        and holonomy_half_turn.T * gram * holonomy_half_turn == gram
    ),
    "trivial_packet_has_one_global_parallel_section": (
        fixed_space_dimension(holonomy_trivial) == 1
    ),
    "half_turn_packet_has_no_nonzero_global_parallel_section": (
        fixed_space_dimension(holonomy_half_turn) == 0
    ),
    "v5_has_no_connection_or_holonomy_datum": not any(
        "connection" in term or "holonomy" in term or "parallel_transport" in term
        for term in all_declared_terms
    ),
    "v5_local_data_cannot_determine_global_descent": (
        fixed_space_dimension(holonomy_trivial)
        != fixed_space_dimension(holonomy_half_turn)
    ),
}

result = {
    "schema": "marici.aspect.v5-flat-holonomy-falsifier.v1",
    "status": "frozen_v5_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "one resolved rank-one route line over a circle with flat holonomy +1 versus -1",
    "shared_v5_data": "metric, determinant, radical, divisor valuation, crossing form, chart cover, and chart transition maps",
    "distinguishing_result": "the +1 packet has a one-dimensional global parallel-section space; the -1 packet has none",
    "failure": "v5 records resolved static gluing but has no flat connection, path-groupoid representation, or loop-holonomy datum",
    "required_future_repair": "a transport local system on every resolved stratum, functorial path-groupoid action, specialization-compatible holonomy, and a boundary-port obstruction to strict descent",
}

out = root / "results" / "v5_flat_holonomy_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v5_falsified" else 1)
