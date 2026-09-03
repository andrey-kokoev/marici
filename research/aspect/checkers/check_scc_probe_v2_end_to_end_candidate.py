#!/usr/bin/env python3
"""End-to-end non-live v2 dispatch, registry, and semantic-validation test."""

import copy
import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACTS = ROOT / "research/aspect/contracts"
OUTPUT = ROOT / "research/aspect/results/scc_probe_v2_end_to_end_candidate.json"
SOURCE = ROOT / "research/aspect/typed-probe-configuration-category-and-restriction-semantics.md"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dispatch = load_module("dispatch", CONTRACTS / "scc_probe_version_dispatch_adapter.py")
semantic = load_module("semantic", CONTRACTS / "scc_probe_semantic_validators.py")
registry = json.loads((CONTRACTS / "scc-probe-registry.v2.candidate.json").read_text(encoding="utf-8"))


def faces(vertices):
    return [list(face) for size in range(len(vertices) + 1) for face in combinations(vertices, size)]


def fixture(entry_id, kind, faithful, additive):
    vertices = ["p", "q"]
    fs = faces(vertices)
    names = [",".join(face) for face in fs]
    return {
        "entry_id": entry_id,
        "configuration_domain": {"vertices": vertices, "admitted_faces": fs},
        "constraint_presheaf": {"objects": {name: {"type": "finite_constraint"} for name in names}, "restrictions": [{"source": name, "target": name, "map": "identity"} for name in names], "composition_verified": True},
        "matching_map_certificate": {"domain": "matching_family", "codomain": "joint_constraint", "map": "mu", "typed": True},
        "continuation_interface": {"schema": "probe_continuation_interface.v1"},
        "continuation_interface_certificate": {"record_projection_faithful": faithful, "unresolved_multiplicity": [] if faithful else [["plus", "minus"]]},
        "rewrite_certificate": {"schema": "probe_rewrite_certificate.v1"},
        "rewrite_naturality_certificate": {"scope": "local", "squares": [{"name": "local", "commutes": True}]},
        "interaction_classification": {"kind": kind},
        "optional_additive_specialization": {"applicable": additive, "target_authority": additive, "residual": "schur" if additive else None},
        "source_digest": {"path": str(SOURCE.relative_to(ROOT)).replace("\\", "/"), "sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
        "authority_and_boundary": {"nonclaims": ["finite candidate fixture only"]},
    }


def route(entry, version):
    resolved = dispatch.resolve(version)
    presence = dispatch.validate_probe_entry(entry, version)
    if not presence["valid"]:
        return {"admitted": False, "stage": "dispatch", "detail": presence}
    semantic_result = semantic.validate(entry, ROOT)
    return {"admitted": semantic_result["valid"], "stage": "semantic", "detail": semantic_result, "registry_schema": registry["schema"]}


fixtures = [fixture("schur-two-probe", "additive_cross_effect", True, True), fixture("three-polarizer", "continuation_projection", False, False)]
v2_results = [route(item, "v2-candidate") for item in fixtures]
v1_results = [route(item, "v1") for item in fixtures]
hostile = copy.deepcopy(fixtures[0])
hostile["matching_map_certificate"]["typed"] = False
hostile_result = route(hostile, "v2-candidate")
unknown_refused = False
try:
    route(fixtures[0], "unknown")
except dispatch.UnknownSCCVersion:
    unknown_refused = True

candidate = dispatch.resolve("v2-candidate")["contract"]
checks = {
    "registry_names_match_contract": set(registry["checks"]) == set(candidate["probe_registry_checks"]),
    "registry_is_nonlive": registry["status"] == "review_candidate_not_live",
    "both_fixtures_pass_explicit_v2_path": all(item["admitted"] and item["stage"] == "semantic" for item in v2_results),
    "v1_rejects_both_at_dispatch": all(not item["admitted"] and item["stage"] == "dispatch" for item in v1_results),
    "malformed_fixture_fails_semantically": not hostile_result["admitted"] and "matching_map_untyped" in hostile_result["detail"]["errors"],
    "unknown_version_fails_closed": unknown_refused,
    "polarizer_nonfaithfulness_retains_multiplicity": v2_results[1]["admitted"] and fixtures[1]["continuation_interface_certificate"]["unresolved_multiplicity"],
    "candidate_path_never_marks_registry_live": all(not item.get("live", False) for item in dispatch.resolve("v2-candidate")["registry"]["probe_candidate_checks"].values()),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.scc-probe-v2-end-to-end-candidate.v1", "status": "passed", "checks": checks, "v2_results": v2_results, "v1_results": v1_results, "hostile_result": hostile_result, "claim_boundary": "One non-live executable candidate path; no live SCC mutation or admission."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "v2_fixture_count": len(v2_results)}, sort_keys=True))
