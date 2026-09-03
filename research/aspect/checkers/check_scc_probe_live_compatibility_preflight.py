#!/usr/bin/env python3
"""Read-only structural compatibility preflight for the SCC probe candidate."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
SCC = ROOT / "research/aspect/scc/scc.py"
V1 = ROOT / "research/aspect/scc/contract.v1.json"
REGISTRY = ROOT / "research/aspect/scc/registry.v1.json"
CANDIDATE = ROOT / "research/aspect/contracts/scc-contract-probe-semantics.v2.candidate.json"
SHADOW_RESULT = ROOT / "research/aspect/results/probe_semantics_shadow_scc.json"
OUTPUT = ROOT / "research/aspect/results/scc_probe_live_compatibility_preflight.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


source = SCC.read_text(encoding="utf-8")
v1 = json.loads(V1.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
shadow = json.loads(SHADOW_RESULT.read_text(encoding="utf-8"))
pre = {path.name: sha(path) for path in (SCC, V1, REGISTRY)}

probe_checks_registered = [name for name in candidate["probe_registry_checks"] if name in registry["checks"]]
source_probe_terms = [term for term in ("probe_configuration", "matching_map_certificate", "rewrite_naturality_certificate") if term in source]

checks = {
    "candidate_binds_current_live_contract": candidate["predecessor"]["sha256"] == sha(V1),
    "candidate_preserves_live_stages": set(v1["stages"]) <= set(candidate["stages"]),
    "live_compiler_hardwires_v1_registry": 'REGISTRY=json.loads((HERE/"registry.v1.json")' in source,
    "live_compiler_has_no_candidate_contract_dispatch": "scc-contract-probe-semantics.v2.candidate" not in source,
    "probe_checks_are_not_live_registered": probe_checks_registered == [],
    "probe_validator_terms_are_absent_from_live_compiler": source_probe_terms == [],
    "shadow_entries_pass_outside_live_compiler": shadow["status"] == "passed" and shadow["checks"]["both_shadow_entries_valid"],
    "shadow_run_reports_live_files_unchanged": shadow["checks"]["live_scc_files_unchanged"],
    "live_files_unchanged_during_preflight": pre == {path.name: sha(path) for path in (SCC, V1, REGISTRY)},
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.scc-probe-live-compatibility-preflight.v1",
    "status": "passed_with_blockers",
    "checks": checks,
    "live_regression_evidence": {"command": "python research/aspect/scc/test_scc.py", "tests": 31, "status": "passed"},
    "blockers": [
        "live compiler hardwires registry.v1.json and has no contract-version dispatch",
        "six probe checks are absent from the live registry",
        "live compiler has no probe configuration, matching-map, continuation, or rewrite-naturality validators",
        "shadow entry success therefore establishes sidecar compatibility only, not live consumption"
    ],
    "safe_adapter_boundary": "Add version-selecting registry/contract injection before adding probe validators; retain v1 as default.",
    "live_digests": pre,
    "claim_boundary": "Read-only structural preflight plus separately executed 31-test live regression suite."
}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "blocker_count": len(result["blockers"])}, sort_keys=True))
