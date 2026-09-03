#!/usr/bin/env python3
"""Hostile tests for non-live SCC probe semantic validators."""

import copy
import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parents[3]
MODULE = ROOT / "research/aspect/contracts/scc_probe_semantic_validators.py"
OUTPUT = ROOT / "research/aspect/results/scc_probe_semantic_validators.json"
SOURCE = ROOT / "research/aspect/typed-probe-configuration-category-and-restriction-semantics.md"
spec = importlib.util.spec_from_file_location("probe_validators", MODULE)
validators = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validators)


def faces(vertices):
    return [list(face) for size in range(len(vertices) + 1) for face in combinations(vertices, size)]


def fixture(kind, faithful, additive):
    vertices = ["p", "q"]
    names = [",".join(face) for face in faces(vertices)]
    return {
        "configuration_domain": {"vertices": vertices, "admitted_faces": faces(vertices)},
        "constraint_presheaf": {
            "objects": {name: {"type": "finite_constraint"} for name in names},
            "restrictions": [{"source": name, "target": name, "map": "identity"} for name in names],
            "composition_verified": True,
        },
        "matching_map_certificate": {"domain": "matching_family", "codomain": "joint_constraint", "map": "mu_pq", "typed": True},
        "continuation_interface_certificate": {
            "record_projection_faithful": faithful,
            "unresolved_multiplicity": [] if faithful else [["plus", "minus"]],
        },
        "rewrite_naturality_certificate": {"scope": "local", "squares": [{"name": "restriction_square", "commutes": True}]},
        "interaction_classification": {"kind": kind},
        "optional_additive_specialization": {"applicable": additive, "target_authority": additive, "residual": "schur" if additive else None},
        "source_digest": {"path": str(SOURCE.relative_to(ROOT)).replace("\\", "/"), "sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest()},
        "authority_and_boundary": {"nonclaims": ["no SCC-wide soundness theorem"]},
    }


schur = fixture("additive_cross_effect", True, True)
polarizer = fixture("continuation_projection", False, False)
valid = [validators.validate(item, ROOT) for item in (schur, polarizer)]

hostiles = {}
mutations = {
    "missing_face": lambda x: x["configuration_domain"]["admitted_faces"].remove(["p"]),
    "bad_identity": lambda x: x["constraint_presheaf"]["restrictions"][0].update(map="not_identity"),
    "untyped_matching": lambda x: x["matching_map_certificate"].update(typed=False),
    "erased_multiplicity": lambda x: x["continuation_interface_certificate"].update(unresolved_multiplicity=[]),
    "noncommuting_rewrite": lambda x: x["rewrite_naturality_certificate"]["squares"][0].update(commutes=False),
    "bad_digest": lambda x: x["source_digest"].update(sha256="0" * 64),
    "additive_without_authority": lambda x: x["optional_additive_specialization"].update(target_authority=False),
}
expected = {
    "missing_face": "configuration_not_downward_closed",
    "bad_identity": "restriction_identity_missing",
    "untyped_matching": "matching_map_untyped",
    "erased_multiplicity": "nonfaithful_projection_without_multiplicity",
    "noncommuting_rewrite": "rewrite_naturality_unverified",
    "bad_digest": "source_digest_mismatch",
    "additive_without_authority": "additive_specialization_untyped",
}
for name, mutate in mutations.items():
    item = copy.deepcopy(polarizer if name == "erased_multiplicity" else schur)
    mutate(item)
    hostiles[name] = validators.validate(item, ROOT)

checks = {
    "schur_fixture_valid": valid[0]["valid"],
    "polarizer_fixture_valid_with_declared_multiplicity": valid[1]["valid"],
    "all_hostiles_rejected": all(not result["valid"] for result in hostiles.values()),
    "all_hostiles_fail_for_predicted_reason": all(expected[name] in result["errors"] for name, result in hostiles.items()),
    "hostile_reasons_are_distinct": len(set(expected.values())) == len(expected),
    "nonfaithfulness_is_not_itself_invalid": valid[1]["valid"],
}
assert all(checks.values()), {"checks": checks, "hostiles": hostiles}
result = {"schema": "marici.aspect.scc-probe-semantic-validators.v1", "status": "passed", "checks": checks, "valid_fixtures": valid, "hostiles": hostiles, "claim_boundary": "Finite certificate validator prototype; not live SCC admission."}
OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "valid_fixture_count": len(valid), "hostile_count": len(hostiles), "check_count": len(checks)}, sort_keys=True))
