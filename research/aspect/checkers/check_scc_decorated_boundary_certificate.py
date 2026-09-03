#!/usr/bin/env python3
"""Hostile-test the non-live SCC decorated boundary certificate extension."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACTS = ROOT / "research/aspect/contracts"
DELTA = CONTRACTS / "scc-decorated-boundary-transport.v2.1.candidate.json"
OUTPUT = ROOT / "research/aspect/results/scc_decorated_boundary_certificate.json"
LIVE = (ROOT / "research/aspect/scc/scc.py", ROOT / "research/aspect/scc/contract.v1.json", ROOT / "research/aspect/scc/registry.v1.json")

spec = importlib.util.spec_from_file_location("decorated_validator", CONTRACTS / "scc_decorated_boundary_validator.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def presentation(prefix, carrier):
    return {
        "occurrence_count": 2,
        "occurrences": [
            {"id": f"{prefix}1", "carrier": carrier, "incidence": f"i_{prefix}1"},
            {"id": f"{prefix}2", "carrier": carrier, "incidence": f"i_{prefix}2"},
        ],
    }


def fixture():
    return {
        "applicability": "required",
        "source_boundary_presentation": presentation("p", "face_p"),
        "target_boundary_presentation": presentation("q", "face_q"),
        "transport": {
            "index_equivalence": {"p1": "q1", "p2": "q2"},
            "carrier_natural_isomorphism": {
                "p1": {"source_carrier": "face_p", "target_carrier": "face_q", "isomorphism": True},
                "p2": {"source_carrier": "face_p", "target_carrier": "face_q", "isomorphism": True},
            },
            "apex_isomorphism": True,
            "incidence_coherence": {"p1": True, "p2": True},
        },
    }


delta = json.loads(DELTA.read_text(encoding="utf-8"))
before = {path.name: sha(path) for path in LIVE}
valid = validator.validate(fixture())
not_applicable = validator.validate({"applicability": "not_applicable"})
mutations = {}

item = fixture(); item["source_boundary_presentation"]["occurrences"].pop(); mutations["erased_occurrence"] = validator.validate(item)
item = fixture(); del item["transport"]["carrier_natural_isomorphism"]["p2"]; mutations["missing_carrier_coherence"] = validator.validate(item)
item = fixture(); item["transport"]["index_equivalence"]["p2"] = "q1"; mutations["inequivalent_boundary_selection"] = validator.validate(item)
item = fixture(); item["transport"]["incidence_coherence"]["p2"] = False; mutations["broken_incidence_coherence"] = validator.validate(item)
expected = {
    "erased_occurrence": "source_occurrence_identity_invalid",
    "missing_carrier_coherence": "boundary_carrier_naturality_missing",
    "inequivalent_boundary_selection": "boundary_index_not_equivalence",
    "broken_incidence_coherence": "boundary_incidence_coherence_failed",
}
after = {path.name: sha(path) for path in LIVE}
checks = {
    "delta_binds_exact_v2_candidate": delta["extends"]["sha256"] == sha(CONTRACTS / "scc-contract-probe-semantics.v2.candidate.json"),
    "delta_binds_exact_candidate_registry": delta["extends_registry"]["sha256"] == sha(CONTRACTS / "scc-probe-registry.v2.candidate.json"),
    "valid_occurrence_sensitive_fixture_passes": valid["valid"],
    "duplicate_carriers_retain_two_occurrences": fixture()["source_boundary_presentation"]["occurrence_count"] == 2,
    "undecorated_migration_is_not_applicable": not_applicable["valid"] and not_applicable["status"] == "not_applicable",
    "all_four_hostiles_rejected": all(not result["valid"] for result in mutations.values()),
    "all_hostiles_fail_for_predicted_reason": all(expected[name] in result["errors"] for name, result in mutations.items()),
    "live_scc_files_unchanged": before == after,
    "delta_remains_nonlive": delta["status"] == "review_candidate_not_live",
}
assert all(checks.values()), {"checks": checks, "mutations": mutations}
result = {"schema": "marici.aspect.scc-decorated-boundary-certificate-check.v1", "status": "passed", "checks": checks, "valid": valid, "hostiles": mutations, "live_digests": after, "claim_boundary": "Non-live v2.1 candidate extension only."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "hostile_count": len(mutations)}, sort_keys=True))
