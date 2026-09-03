#!/usr/bin/env python3
"""Hostile-test SCC boundary-index constructor discrimination."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACTS = ROOT / "research/aspect/contracts"
DELTA = CONTRACTS / "scc-boundary-index-kind.v2.3.candidate.json"
OUTPUT = ROOT / "research/aspect/results/scc_boundary_index_kind.json"
LIVE = (ROOT / "research/aspect/scc/scc.py", ROOT / "research/aspect/scc/contract.v1.json", ROOT / "research/aspect/scc/registry.v1.json")
spec = importlib.util.spec_from_file_location("index_kind", CONTRACTS / "scc_boundary_index_kind_validator.py")
validator = importlib.util.module_from_spec(spec); spec.loader.exec_module(validator)


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def internal_fixture():
    flip = {0: 1, 1: 0}
    return {
        "index_kind": "internal_groupoid_diagram",
        "objects": ["p1", "p2"],
        "object_values": {"p1": [0, 1], "p2": [0, 1]},
        "internal_morphisms": [{"name": "u", "source": "p1", "target": "p2"}, {"name": "u_inv", "source": "p2", "target": "p1"}],
        "diagram_maps": {"u": flip, "u_inv": flip},
        "matching_limit": [[0, 1], [1, 0]],
        "constructor_inferred_from_cardinality": False,
    }


def discrete_fixture():
    return {"index_kind": "discrete_occurrences_with_external_action", "objects": ["p1", "p2"], "object_values": {"p1": [0, 1], "p2": [0, 1]}, "internal_morphisms": [], "matching_cardinality": 4, "constructor_inferred_from_cardinality": False}


delta = json.loads(DELTA.read_text(encoding="utf-8"))
before = {p.name: sha(p) for p in LIVE}
internal = validator.validate(internal_fixture())
discrete = validator.validate(discrete_fixture())
authorized_orbit = validator.validate({"index_kind": "authorized_orbit_quotient", "source_action_reference": "S2-on-M", "orbit_projection": "q", "source_derived_quotient_authority": "source:exchange", "constructor_inferred_from_cardinality": False})

hostiles = {}
item = internal_fixture(); del item["diagram_maps"]["u_inv"]; hostiles["missing_internal_map"] = validator.validate(item)
item = internal_fixture(); item["matching_limit"] = [[0, 0], [1, 1]]; hostiles["wrong_internal_limit"] = validator.validate(item)
item = discrete_fixture(); item["internal_morphisms"] = [{"name": "u"}]; hostiles["discrete_with_internal_morphism"] = validator.validate(item)
item = {"index_kind": "authorized_orbit_quotient", "source_action_reference": "S2-on-M", "orbit_projection": "q", "source_derived_quotient_authority": None, "constructor_inferred_from_cardinality": False}; hostiles["orbit_without_authority"] = validator.validate(item)
item = internal_fixture(); item["constructor_inferred_from_cardinality"] = True; hostiles["cardinality_inference"] = validator.validate(item)
expected = {"missing_internal_map": "internal_groupoid_diagram_map_missing", "wrong_internal_limit": "internal_matching_limit_not_compatibility_solution", "discrete_with_internal_morphism": "discrete_index_has_internal_morphisms", "orbit_without_authority": "orbit_quotient_authority_missing", "cardinality_inference": "constructor_identity_inferred_from_cardinality"}
after = {p.name: sha(p) for p in LIVE}
checks = {
    "delta_binds_exact_v22_candidate": delta["extends"]["sha256"] == sha(CONTRACTS / "scc-boundary-equivariance.v2.2.candidate.json"),
    "internal_flip_groupoid_passes": internal["valid"] and internal["status"] == "internal_groupoid",
    "discrete_occurrence_index_passes": discrete["valid"] and discrete["status"] == "discrete_external",
    "authorized_orbit_is_separate_kind": authorized_orbit["valid"] and authorized_orbit["status"] == "authorized_orbit_quotient",
    "all_five_hostiles_rejected": all(not result["valid"] for result in hostiles.values()),
    "all_hostiles_fail_for_predicted_reason": all(expected[name] in result["errors"] for name, result in hostiles.items()),
    "delta_remains_nonlive": delta["status"] == "review_candidate_not_live",
    "live_scc_v1_unchanged": before == after,
}
assert all(checks.values()), {"checks": checks, "hostiles": hostiles}
result = {"schema": "marici.aspect.scc-boundary-index-kind-check.v1", "status": "passed", "checks": checks, "valid_kinds": {"internal": internal, "discrete": discrete, "orbit": authorized_orbit}, "hostiles": hostiles, "claim_boundary": "Two-object finite groupoid validator only."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "hostile_count": len(hostiles)}, sort_keys=True))
