import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v4 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v4.json").read_text(encoding="utf-8"))

x, y, t, a, b = sp.symbols("x y t a b", real=True)
G = sp.diag(x, y)
G_origin = G.subs({x: 0, y: 0})
B_direction = a * sp.diff(G, x) + b * sp.diff(G, y)

path_linear = G.subs({x: t, y: t})
path_tangent = G.subs({x: t, y: t**2})
path_axis = G.subs({x: t, y: 0})

fields = set(v4["stratified_metric_route_family"]["singular_stratum_required_fields"])
objects = set(v4["object_types"])
arrows = set(v4["arrow_types"])
cells = set(v4["cell_types"])

checks = {
    "v4_is_frozen": v4["cell_creation_during_replay"] is False,
    "origin_radical_has_dimension_two": len(G_origin.nullspace()) == 2,
    "generic_normal_direction_crossing_rank_two": B_direction.subs({a: 1, b: 1}).rank() == 2,
    "x_axis_direction_crossing_rank_one": B_direction.subs({a: 1, b: 0}).rank() == 1,
    "y_axis_direction_crossing_rank_one": B_direction.subs({a: 0, b: 1}).rank() == 1,
    "linear_path_has_two_first_order_grades": [sp.diff(path_linear[i, i], t).subs(t, 0) for i in range(2)] == [1, 1],
    "tangent_path_has_first_and_second_order_grades": sp.diff(path_tangent[0, 0], t).subs(t, 0) == 1 and (sp.diff(path_tangent[1, 1], t, 2).subs(t, 0) / 2) == 1,
    "path_determinant_orders_differ": sp.factor(path_linear.det()) == t**2 and sp.factor(path_tangent.det()) == t**3,
    "axis_path_never_recovers_full_rank": path_axis.rank() == 1,
    "normal_cone_field_exists_but_no_resolution_object": "normal_parameter_or_normal_cone" in fields and "projectivized_normal_direction_stratum" not in objects,
    "v4_lacks_blowup_arrow": "normal_blowup" not in arrows,
    "v4_lacks_direction_change_gluing": "directional_filtration_gluing" not in cells,
}

result = {
    "schema": "marici.aspect.v4-direction-dependent-specialization-falsifier.v1",
    "status": "frozen_v4_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "hostile": "G(x,y)=diag(x,y) at the crossing of the two determinant divisors",
    "failure": "the radical filtration depends on normal direction and path order, but v4 has no resolved normal-direction strata or gluing",
    "required_future_repair": "projectivized normal cone or blowup, direction-indexed filtrations, and gluing across exceptional-direction strata",
}

out = root / "results" / "v4_direction_dependent_specialization_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v4_falsified" else 1)
