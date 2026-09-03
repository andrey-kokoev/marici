#!/usr/bin/env python3
"""Hostile-test the non-live SCC boundary-equivariance certificate."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACTS = ROOT / "research/aspect/contracts"
DELTA = CONTRACTS / "scc-boundary-equivariance.v2.2.candidate.json"
OUTPUT = ROOT / "research/aspect/results/scc_boundary_equivariance_certificate.json"
LIVE = (ROOT / "research/aspect/scc/scc.py", ROOT / "research/aspect/scc/contract.v1.json", ROOT / "research/aspect/scc/registry.v1.json")
spec = importlib.util.spec_from_file_location("equivariance", CONTRACTS / "scc_boundary_equivariance_validator.py")
validator = importlib.util.module_from_spec(spec); spec.loader.exec_module(validator)


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def fixture():
    points = ["00", "01", "10", "11"]
    swap = {"00": "00", "01": "10", "10": "01", "11": "11"}
    identity = {point: point for point in points}
    multiplication = {"id": {"id": "id", "s": "s"}, "s": {"id": "s", "s": "id"}}
    return {
        "applicability": "required",
        "source_automorphism_group": {"elements": ["id", "s"], "identity": "id", "multiplication": multiplication},
        "target_automorphism_group": {"elements": ["id", "t"], "identity": "id", "multiplication": {"id": {"id": "id", "t": "t"}, "t": {"id": "t", "t": "id"}}},
        "group_isomorphism": {"id": "id", "s": "t"},
        "source_matching_points": points,
        "target_matching_points": points,
        "source_matching_action": {"id": identity, "s": swap},
        "target_matching_action": {"id": identity, "t": swap},
        "matching_object_map": identity,
        "orbit_only": False,
        "source_derived_quotient_authority": None,
    }


delta = json.loads(DELTA.read_text(encoding="utf-8"))
before = {p.name: sha(p) for p in LIVE}
valid = validator.validate(fixture())
not_applicable = validator.validate({"applicability": "not_applicable"})

hostiles = {}
item = fixture(); item["group_isomorphism"]["s"] = "id"; hostiles["nonbijective_group_map"] = validator.validate(item)
item = fixture(); item["matching_object_map"] = {"00": "01", "01": "00", "10": "10", "11": "11"}; hostiles["broken_equivariance"] = validator.validate(item)
item = fixture(); item["orbit_only"] = True; item["matching_object_map"] = {}; hostiles["orbit_only_without_authority"] = validator.validate(item)
item = fixture(); item["source_matching_action"]["s"]["01"] = "01"; hostiles["action_not_permutation"] = validator.validate(item)
expected = {
    "nonbijective_group_map": "automorphism_group_map_not_bijective",
    "broken_equivariance": "matching_object_equivariance_failed",
    "orbit_only_without_authority": "orbit_quotient_authority_missing",
    "action_not_permutation": "source_matching_action_not_permutation",
}
authorized = fixture(); authorized["orbit_only"] = True; authorized["matching_object_map"] = {}; authorized["source_derived_quotient_authority"] = "source:declared-occurrence-exchange"; authorized_result = validator.validate(authorized)
after = {p.name: sha(p) for p in LIVE}
checks = {
    "delta_binds_exact_v21_candidate": delta["extends"]["sha256"] == sha(CONTRACTS / "scc-decorated-boundary-transport.v2.1.candidate.json"),
    "valid_equivariant_rewrite_passes": valid["valid"] and valid["status"] == "reversible_equivariant",
    "trivial_action_migration_is_not_applicable": not_applicable["valid"] and not_applicable["status"] == "not_applicable",
    "all_four_hostiles_rejected": all(not result["valid"] for result in hostiles.values()),
    "all_hostiles_fail_for_predicted_reason": all(expected[name] in result["errors"] for name, result in hostiles.items()),
    "authorized_orbit_quotient_is_typed_separately": authorized_result["valid"] and authorized_result["status"] == "authorized_orbit_quotient",
    "authorized_orbit_quotient_is_not_reversible_status": authorized_result["status"] != "reversible_equivariant",
    "delta_remains_nonlive": delta["status"] == "review_candidate_not_live",
    "live_scc_v1_unchanged": before == after,
}
assert all(checks.values()), {"checks": checks, "hostiles": hostiles}
result = {"schema": "marici.aspect.scc-boundary-equivariance-certificate-check.v1", "status": "passed", "checks": checks, "valid": valid, "hostiles": hostiles, "authorized_quotient": authorized_result, "claim_boundary": "Non-live finite-action candidate validator only."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "hostile_count": len(hostiles)}, sort_keys=True))
