#!/usr/bin/env python3
"""Type-check the arrow chains in the matching-object isomorphism proof contract."""

import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACT = ROOT / "research/aspect/contracts/matching-object-isomorphism-proof.v1.json"
OUTPUT = ROOT / "research/aspect/results/matching_object_isomorphism_proof.json"
data = json.loads(CONTRACT.read_text(encoding="utf-8"))
arrows = {name: tuple(types) for name, types in data["arrows"].items()}


def chain_type(chain):
    source, target = arrows[chain[0]]
    for name in chain[1:]:
        next_source, next_target = arrows[name]
        if target != next_source:
            raise ValueError(f"ill-typed composition {chain}: {target} != {next_source}")
        target = next_target
    return source, target


def equation_typed(sides):
    return chain_type(sides[0]) == chain_type(sides[1])


equation_checks = {name: equation_typed(sides) for name, sides in data["equations"].items()}
projected_left = data["equations"]["conjugacy_after_projection"][0]
projected_right = data["equations"]["conjugacy_after_projection"][1]
conjugacy_left = data["equations"]["matching_map_conjugacy"][0]
conjugacy_right = data["equations"]["matching_map_conjugacy"][1]
checks = {
    "all_equations_are_well_typed": all(equation_checks.values()),
    "projected_conjugacy_has_common_target": chain_type(projected_left) == chain_type(projected_right) == ("F_sigma", "G_Etau"),
    "unprojected_conjugacy_has_common_target": chain_type(conjugacy_left) == chain_type(conjugacy_right) == ("F_sigma", "M_G"),
    "projected_equation_is_projection_of_conjugacy": projected_left == conjugacy_left + ["pi_G_Etau"] and projected_right == conjugacy_right + ["pi_G_Etau"],
    "limit_comparison_defining_equation_present": "limit_comparison_projection" in data["equations"],
    "naturality_equation_present": "presheaf_naturality" in data["equations"],
    "joint_monicity_rule_present": any("jointly monic" in rule for rule in data["proof_rules"]),
    "inverse_construction_present": any("quasi-inverse" in rule for rule in data["proof_rules"]),
    "proper_face_transport_is_explicit": any("punctured lower" in assumption for assumption in data["assumptions"]),
    "no_additive_assumption": not any("additive" in assumption.lower() for assumption in data["assumptions"]),
    "physical_time_is_disclaimed": "physical time interpretation" in data["nonclaims"],
}
assert all(checks.values()), {"checks": checks, "equations": equation_checks}
result = {"schema": "marici.aspect.matching-object-isomorphism-proof-check.v1", "status": "passed", "checks": checks, "equation_checks": equation_checks, "supported_strength": "typed categorical proof contract conditional on declared limit and transport assumptions", "formalization_status": "not machine-checked in Lean"}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "equation_count": len(equation_checks)}, sort_keys=True))
