#!/usr/bin/env python3
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
contract_path = ROOT / "research/aspect/contracts/realization-fiber-coherence.v1.json"
result_path = ROOT / "research/aspect/results/realization_fiber_coherence.json"
c = json.loads(contract_path.read_text(encoding="utf-8"))

required_slots = {
    "named_constructor_actions", "observers", "viewing_forms", "authority",
    "completion_topology", "instrument_backaction"
}

def first_failure(x):
    tower = x["base_tower"]
    hostile = x["same_profile_hostile"]
    gates = [
        ("tower_counts", len(tower["rungs"]) == 8 and len(tower["adjacent_reconcilers"]) == 7
         and tower["interval_cell_count"] == 8 * 9 // 2
         and tower["left_right_face_map_count"] == 2 * (36 - 8)
         and tower["theta_tate_overlay_count"] == 36),
        ("classifier_separation", "do not imply" in x["classifier_relation"]["not_equivalence"]
         and hostile["conclusion"].startswith("no invertible")),
        ("comparison_slot_completeness", set(x["realization_fiber"]["comparison_slots"]) == required_slots),
        ("named_action_intertwiner", hostile["left_character"] != hostile["right_character"]),
        ("observer_intertwiner", hostile["observer"] == "identity"),
        ("viewing_form_isometry", hostile["viewing_gramian"] == "identity"),
        ("authority_compatibility", "authority contexts" in " ".join(x["realization_fiber"]["verified_morphism_laws"])),
        ("completion_compatibility", "completion topology" in " ".join(x["realization_fiber"]["verified_morphism_laws"])),
        ("instrument_backaction_compatibility", "instrument transitions" in " ".join(x["realization_fiber"]["verified_morphism_laws"])),
        ("higher_coherence_support", all(s["status"] == "unsupported_formal_only" for s in x["realization_fiber"]["higher_coherence_slots"]))
    ]
    return next((name for name, ok in gates if not ok), None), dict(gates)

first, checks = first_failure(c)
deleted = copy.deepcopy(c)
deleted["realization_fiber"]["comparison_slots"].remove("named_constructor_actions")
mutated = copy.deepcopy(c)
mutated["classifier_relation"]["not_equivalence"] = "equal SCC profiles imply constructor equivalence"
mutated["same_profile_hostile"]["conclusion"] = "equivalent"

# For T=[[a,b],[c,d]], T(-I)=diag(1,-1)T forces a=b=0, hence rank(T)<=1.
intertwiner_linear_residual = {"a_coefficient": -2, "b_coefficient": -2, "forced_zero_entries": ["a", "b"], "maximum_rank": 1}

out = {
    "schema": "marici.aspect.realization-fiber-coherence-check.v1",
    "contract": str(contract_path.relative_to(ROOT)).replace("\\", "/"),
    "checks": checks,
    "exact_intertwiner_obstruction": intertwiner_linear_residual,
    "baseline_first_failure": first,
    "deletion_first_failure": first_failure(deleted)[0],
    "mutation_first_failure": first_failure(mutated)[0],
    "passed": (all(checks.values()) and first is None
               and first_failure(deleted)[0] == "comparison_slot_completeness"
               and first_failure(mutated)[0] == "classifier_separation"),
    "claim": "finite schema binding and hostile obstruction only; higher fiber coherence remains formal and unsupported"
}
result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
