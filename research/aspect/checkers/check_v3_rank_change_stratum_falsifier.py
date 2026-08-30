import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v3 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v3.json").read_text(encoding="utf-8"))

t = sp.symbols("t", real=True)
G = sp.diag(1, t)
F = sp.eye(2)
G_zero = G.subs(t, 0)
radical = G_zero.nullspace()
determinant = sp.factor(G.det())

checks = {
    "v3_is_frozen": v3["cell_creation_during_replay"] is False,
    "family_is_metric_isometry_everywhere_as_bilinear_identity": sp.simplify(F.T * G * F - G) == sp.zeros(2),
    "generic_rank_is_two": G.subs(t, 1).rank() == 2 and G.subs(t, -1).rank() == 2,
    "central_rank_drops_to_one": G_zero.rank() == 1,
    "central_radical_is_one_dimensional": len(radical) == 1 and radical[0] == sp.Matrix([0, 1]),
    "determinant_crosses_simply": determinant == t and sp.diff(determinant, t).subs(t, 0) == 1,
    "signature_changes_across_stratum": G.subs(t, 1).is_positive_definite is True and G.subs(t, -1).det() < 0,
    "v3_forbids_singular_gram_object": "gram_is_nondegenerate_hermitian" in v3["labelled_metric_route_space"]["laws"],
    "v3_lacks_degenerate_route_object": "degenerate_metric_route_space" not in v3["object_types"],
    "v3_lacks_specialization_arrow": "metric_specialization" not in v3["arrow_types"],
    "v3_lacks_radical_quotient_cell": "radical_quotient_gluing" not in v3["cell_types"],
}

result = {
    "schema": "marici.aspect.v3-rank-change-stratum-falsifier.v1",
    "status": "frozen_v3_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "hostile": "G(t)=diag(1,t), F(t)=I across the rank-drop stratum t=0",
    "failure": "v3 demands a separate singular stratum but provides no object, specialization arrow, radical quotient, or gluing cell for it",
    "required_future_repair": "stratified metric route spaces with radical, quotient metric, specialization, normal jet, and gluing laws",
}

out = root / "results" / "v3_rank_change_stratum_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v3_falsified" else 1)
