#!/usr/bin/env python3
"""Route probe fixtures through the complete non-live SCC v2.1 candidate path."""

import copy
import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parents[3]
CONTRACTS = ROOT / "research/aspect/contracts"
RESULTS = ROOT / "research/aspect/results"
SOURCE = ROOT / "research/aspect/typed-probe-configuration-category-and-restriction-semantics.md"
OUTPUT = RESULTS / "scc_v21_decorated_end_to_end.json"
LIVE = (ROOT / "research/aspect/scc/scc.py", ROOT / "research/aspect/scc/contract.v1.json", ROOT / "research/aspect/scc/registry.v1.json")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


dispatch = load_module("dispatch", CONTRACTS / "scc_probe_version_dispatch_adapter.py")
semantic = load_module("semantic", CONTRACTS / "scc_probe_semantic_validators.py")
decorated = load_module("decorated", CONTRACTS / "scc_decorated_boundary_validator.py")
proof = json.loads((RESULTS / "matching_object_isomorphism_proof.json").read_text(encoding="utf-8"))
delta = json.loads((CONTRACTS / "scc-decorated-boundary-transport.v2.1.candidate.json").read_text(encoding="utf-8"))


def faces(vertices):
    return [list(face) for size in range(len(vertices) + 1) for face in combinations(vertices, size)]


def base_fixture():
    vertices = ["p", "q"]
    fs = faces(vertices)
    names = [",".join(face) for face in fs]
    return {
        "configuration_domain": {"vertices": vertices, "admitted_faces": fs},
        "constraint_presheaf": {"objects": {name: {"type": "finite_constraint"} for name in names}, "restrictions": [{"source": name, "target": name, "map": "identity"} for name in names], "composition_verified": True},
        "interaction_classification": {"kind": "matching_defect"},
        "optional_additive_specialization": {"applicable": False, "target_authority": False, "residual": None},
        "continuation_interface": {"schema": "probe_continuation_interface.v1"},
        "continuation_interface_certificate": {"record_projection_faithful": True, "unresolved_multiplicity": []},
        "rewrite_certificate": {"schema": "probe_rewrite_certificate.v1"},
        "rewrite_naturality_certificate": {"scope": "local", "squares": [{"name": "boundary", "commutes": True}]},
        "matching_map_certificate": {"domain": "matching_family", "codomain": "joint_constraint", "map": "mu", "typed": True},
        "source_digest": {"path": str(SOURCE.relative_to(ROOT)).replace("\\", "/"), "sha256": sha(SOURCE)},
        "authority_and_boundary": {"nonclaims": ["non-live candidate"]},
    }


def boundary_fixture():
    return {
        "applicability": "required",
        "source_boundary_presentation": {"occurrence_count": 2, "occurrences": [{"id": "p1", "carrier": "face", "incidence": "i1"}, {"id": "p2", "carrier": "face", "incidence": "i2"}]},
        "target_boundary_presentation": {"occurrence_count": 2, "occurrences": [{"id": "q1", "carrier": "facePrime", "incidence": "j1"}, {"id": "q2", "carrier": "facePrime", "incidence": "j2"}]},
        "transport": {
            "index_equivalence": {"p1": "q1", "p2": "q2"},
            "carrier_natural_isomorphism": {"p1": {"source_carrier": "face", "target_carrier": "facePrime", "isomorphism": True}, "p2": {"source_carrier": "face", "target_carrier": "facePrime", "isomorphism": True}},
            "apex_isomorphism": True,
            "incidence_coherence": {"p1": True, "p2": True},
        },
    }


def route(base, boundary, version="v2-candidate", proof_status="passed"):
    try:
        dispatch.resolve(version)
    except dispatch.UnknownSCCVersion:
        return {"admitted": False, "stage": "dispatch", "reason": "unknown_version"}
    presence = dispatch.validate_probe_entry(base, version)
    if not presence["valid"]:
        return {"admitted": False, "stage": "dispatch", "detail": presence}
    base_result = semantic.validate(base, ROOT)
    if not base_result["valid"]:
        return {"admitted": False, "stage": "base_semantics", "detail": base_result}
    boundary_result = decorated.validate(boundary)
    if not boundary_result["valid"]:
        return {"admitted": False, "stage": "decorated_boundary", "detail": boundary_result}
    if proof_status != "passed":
        return {"admitted": False, "stage": "matching_proof", "reason": "proof_evidence_not_passed"}
    return {"admitted": True, "stage": "candidate_complete", "boundary_status": boundary_result["status"]}


base = base_fixture()
boundary = boundary_fixture()
before = {path.name: sha(path) for path in LIVE}
valid = route(base, boundary)
undecorated = route(base, {"applicability": "not_applicable"})
v1 = route(base, boundary, "v1")
unknown = route(base, boundary, "unknown")
bad_base = copy.deepcopy(base); bad_base["matching_map_certificate"]["typed"] = False
bad_boundary = copy.deepcopy(boundary); bad_boundary["transport"]["incidence_coherence"]["p2"] = False
hostiles = {
    "untyped_matching_map": route(bad_base, boundary),
    "broken_boundary_coherence": route(base, bad_boundary),
    "missing_matching_proof": route(base, boundary, proof_status="failed"),
}
after = {path.name: sha(path) for path in LIVE}
checks = {
    "decorated_fixture_passes_complete_candidate_path": valid["admitted"] and valid["stage"] == "candidate_complete",
    "undecorated_fixture_migrates_not_applicable": undecorated["admitted"] and undecorated["boundary_status"] == "not_applicable",
    "v1_rejects_probe_entry_at_dispatch": not v1["admitted"] and v1["stage"] == "dispatch",
    "unknown_version_fails_closed": not unknown["admitted"] and unknown["reason"] == "unknown_version",
    "untyped_matching_map_fails_base_stage": hostiles["untyped_matching_map"]["stage"] == "base_semantics",
    "broken_boundary_fails_decorated_stage": hostiles["broken_boundary_coherence"]["stage"] == "decorated_boundary",
    "missing_proof_fails_proof_stage": hostiles["missing_matching_proof"]["stage"] == "matching_proof",
    "proof_evidence_currently_passes": proof["status"] == "passed",
    "delta_remains_nonlive": delta["status"] == "review_candidate_not_live",
    "live_v1_files_unchanged": before == after,
}
assert all(checks.values()), {"checks": checks, "hostiles": hostiles}
result = {"schema": "marici.aspect.scc-v21-decorated-end-to-end.v1", "status": "passed", "checks": checks, "valid": valid, "undecorated": undecorated, "v1": v1, "hostiles": hostiles, "claim_boundary": "Non-live candidate integration only; proof evidence is a typed contract, not Lean verification."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "hostile_count": len(hostiles)}, sort_keys=True))
