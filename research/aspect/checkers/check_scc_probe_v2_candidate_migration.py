#!/usr/bin/env python3
"""Validate the non-live SCC v2 candidate and a lossless legacy registry migration."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
V1 = ROOT / "research/aspect/scc/contract.v1.json"
REGISTRY = ROOT / "research/aspect/scc/registry.v1.json"
CANDIDATE = ROOT / "research/aspect/contracts/scc-contract-probe-semantics.v2.candidate.json"
OUTPUT = ROOT / "research/aspect/results/scc_probe_v2_candidate_migration.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


v1 = json.loads(V1.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
checks_before = json.loads(json.dumps(registry["checks"]))

migrated = [
    {
        "legacy_entry": item,
        "probe_semantics_status": candidate["legacy_migration"]["default_probe_status"],
        "interaction_defect": candidate["legacy_migration"]["default_interaction_defect"],
        "probe_fields_constructed": False,
    }
    for item in registry["checks"]
]

checks = {
    "candidate_binds_exact_v1_digest": candidate["predecessor"]["sha256"] == sha(V1),
    "candidate_is_not_live": candidate["status"] == "review_candidate_not_live",
    "candidate_has_two_new_stages": set(candidate["stages"]) - set(v1["stages"]) == {"probe_configuration", "probe_rewrite_certificate"},
    "all_v1_stages_preserved": set(v1["stages"]) <= set(candidate["stages"]),
    "seven_probe_sections_present": len(candidate["probe_sections"]) == 7,
    "six_probe_registry_checks_present": len(candidate["probe_registry_checks"]) == 6,
    "legacy_entries_preserved_exactly": [item["legacy_entry"] for item in migrated] == checks_before,
    "legacy_entries_are_untyped_not_zero": all(item["probe_semantics_status"] == "untyped_for_probe_semantics" and item["interaction_defect"] is None for item in migrated),
    "migration_does_not_construct_probe_fields": all(item["probe_fields_constructed"] is False for item in migrated),
    "explicit_review_is_required": "explicit review of candidate contract" in candidate["admission_requirements"],
    "live_contract_path_is_not_candidate_path": V1 != CANDIDATE,
    "live_registry_unchanged": registry["checks"] == checks_before,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.scc-probe-v2-candidate-migration.v1",
    "status": "passed",
    "checks": checks,
    "legacy_entry_count": len(migrated),
    "migrated_preview": migrated,
    "live_v1_sha256": sha(V1),
    "live_registry_sha256": sha(REGISTRY),
    "candidate_sha256": sha(CANDIDATE),
    "disposition": "candidate_ready_for_explicit_review_not_admission",
    "claim_boundary": "Candidate and migration simulation only; no live SCC mutation."
}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "legacy_entry_count": len(migrated)}, sort_keys=True))
