#!/usr/bin/env python3
"""Check dependency closure and claim boundaries of the Lean handoff contract."""

import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACT = ROOT / "research/aspect/contracts/finite-probe-semantics-lean-handoff.v1.json"
OUTPUT = ROOT / "research/aspect/results/finite_probe_lean_handoff.json"
data = json.loads(CONTRACT.read_text(encoding="utf-8"))
definitions = {item["id"] for item in data["definitions"]}
theorems = {item["id"] for item in data["theorems"]}
available = definitions | theorems
order = data["implementation_order"]
position = {item: index for index, item in enumerate(order)}

checks = {
    "all_requirements_resolve": all(set(item["requires"]) <= available for item in data["theorems"]),
    "dependency_order_is_topological": all(position[requirement] < position[item["id"]] for item in data["theorems"] for requirement in item["requires"]),
    "face_system_encodes_downward_closure": "downward closure" in next(item for item in data["definitions"] if item["id"] == "FaceSystem")["laws"],
    "presheaf_has_both_functor_laws": set(next(item for item in data["definitions"] if item["id"] == "ConstraintPresheaf")["laws"]) == {"restriction identity", "restriction composition"},
    "rewrite_requires_natural_isomorphism": "natural isomorphism of constraint presheaves" in next(item for item in data["definitions"] if item["id"] == "ProbeRewrite")["data"],
    "fiber_theorem_depends_on_conjugacy": next(item for item in data["theorems"] if item["id"] == "rewrite_fiber_equiv")["requires"] == ["rewrite_matching_conjugacy"],
    "additive_structure_is_not_implicit": any("no additive structure" in item for item in data["explicit_assumptions"]),
    "global_confluence_promotion_forbidden": any("global rewrite confluence" in item for item in data["forbidden_promotions"]),
    "physical_time_promotion_forbidden": any("physical time" in item for item in data["forbidden_promotions"]),
    "acceptance_requires_no_sorry": "no sorry declarations" in data["acceptance"],
    "owner_boundary_is_explicit": data["owner_required"] == "marici.Buzzard" and data["status"] == "frozen_statement_handoff_not_formalized",
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.finite-probe-lean-handoff-check.v1", "status": "passed", "checks": checks, "definition_count": len(definitions), "theorem_count": len(theorems), "claim_boundary": "Checks statement contract only; no Lean theorem has been compiled."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "definition_count": len(definitions), "theorem_count": len(theorems)}, sort_keys=True))
