#!/usr/bin/env python3
"""Compile two probe-semantic entries into a shadow SCC certificate."""

import hashlib
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parents[3]
DELTA = ROOT / "research/aspect/contracts/scc-probe-semantics-delta.v1.json"
LIVE_CONTRACT = ROOT / "research/aspect/scc/contract.v1.json"
LIVE_REGISTRY = ROOT / "research/aspect/scc/registry.v1.json"
OUTPUT = ROOT / "research/aspect/results/probe_semantics_shadow_scc.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def faces(labels):
    return [list(face) for size in range(len(labels) + 1) for face in combinations(labels, size)]


delta = json.loads(DELTA.read_text(encoding="utf-8"))
required = set(delta["required_sections"])
live_before = {"contract": sha(LIVE_CONTRACT), "registry": sha(LIVE_REGISTRY)}

schur = {
    "cell_id": "schur_two_probe_closed_continuation",
    "configuration_domain": {"labels": ["entry", "exit"], "admissible": faces(["entry", "exit"]), "absent": []},
    "constraint_presheaf": {"category": "exact_rational_additive", "restrictions": "configuration_forgetting", "functoriality": "checked"},
    "interaction_classification": {"kind": "additive_cross_effect", "matching_map": "declared", "residual": "-C*A^-1*B"},
    "optional_additive_specialization": {"authority": "exact_rational_additive", "valuation": "effective_response", "cross_effect": "-C*A^-1*B"},
    "continuation_interface": {"state": "new_and_retained_blocks", "transformer": "Schur_elimination", "record_projection": "effective_new_block", "faithfulness": "bounded_to_fixture"},
    "rewrite_certificate": {"boundary": ["A", "B", "C", "E"], "witness": "Schur_complement_identity", "naturality": "fixture_checked", "invertibility": "A_required_invertible"},
    "authority_and_boundary": {"sources": ["research/aspect/contracts/schur-two-probe-scc-cell.v1.json"], "nonclaims": ["not_live_admission", "not_scc_wide"]},
}

polarizer = {
    "cell_id": "three_polarizer_continuation",
    "configuration_domain": {"labels": ["middle_45", "terminal_90"], "admissible": faces(["middle_45", "terminal_90"]), "absent": []},
    "constraint_presheaf": {"category": "finite_exact_state_transformers", "restrictions": "instrument_forgetting", "functoriality": "checked"},
    "interaction_classification": {"kind": "lawful_composition", "matching_map": "factorized_at_full_state", "residual": "posterior_polarization_state"},
    "optional_additive_specialization": {"authority": None, "valuation": None, "cross_effect": None},
    "continuation_interface": {"state": ["intensity", "polarization_angle"], "transformer": "Malus_update", "record_projection": "intensity", "faithfulness": "not_faithful"},
    "rewrite_certificate": {"boundary": ["incoming_state", "outgoing_state"], "witness": "exact_special_angle_composition", "naturality": "composition_checked", "invertibility": "not_claimed"},
    "authority_and_boundary": {"sources": ["research/kitaev/three-polarizer-interaction-net.md", "research/aspect/results/three_polarizer_probe_semantics.json"], "nonclaims": ["not_general_optics", "not_live_admission"]},
}

entries = [schur, polarizer]
entry_checks = {
    entry["cell_id"]: {
        "all_sections_present": set(entry) - {"cell_id"} == required,
        "configuration_domain_downward_closed": all(
            face in entry["configuration_domain"]["admissible"]
            for config in entry["configuration_domain"]["admissible"]
            for face in faces(config)
        ),
        "interaction_kind_typed": entry["interaction_classification"]["kind"] in {"additive_cross_effect", "lawful_composition", "matching_defect"},
        "nonclaims_present": bool(entry["authority_and_boundary"]["nonclaims"]),
    }
    for entry in entries
}

legacy = {"cell_id": "legacy_cell", "stage": "dynamic_coherence"}
legacy_failures = sorted(required - set(legacy))
checks = {
    "both_shadow_entries_valid": all(all(item.values()) for item in entry_checks.values()),
    "schur_and_polarizer_have_distinct_interaction_kinds": schur["interaction_classification"]["kind"] != polarizer["interaction_classification"]["kind"],
    "polarizer_projection_is_explicitly_nonfaithful": polarizer["continuation_interface"]["faithfulness"] == "not_faithful",
    "legacy_entry_fails_all_probe_sections": set(legacy_failures) == required,
    "delta_remains_unadmitted": delta["status"] == "proposed_not_admitted",
}
assert all(checks.values()), checks
live_after = {"contract": sha(LIVE_CONTRACT), "registry": sha(LIVE_REGISTRY)}
checks["live_scc_files_unchanged"] = live_before == live_after
assert checks["live_scc_files_unchanged"]

result = {
    "schema": "marici.aspect.probe-semantics-shadow-scc.v1",
    "status": "passed",
    "checks": checks,
    "entry_checks": entry_checks,
    "entries": entries,
    "legacy_typed_failures": legacy_failures,
    "live_sha256_before": live_before,
    "live_sha256_after": live_after,
    "claim_boundary": "Shadow compilation only; live SCC contract and registry unchanged."
}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks, "legacy_failure_count": len(legacy_failures)}, sort_keys=True))
