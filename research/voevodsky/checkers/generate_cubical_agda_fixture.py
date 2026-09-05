#!/usr/bin/env python3
"""Validate structured cubical data and generate positive and hostile Agda modules."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VOE = ROOT / "research" / "voevodsky"
PATHS = {
    "signature": VOE / "cyclic-residue-feedback-signature.json",
    "common": VOE / "cyclic-common-interface.json",
    "overlay": VOE / "contracts" / "theta-rh-cubical-scc-overlay.v1.json",
    "native": VOE / "contracts" / "native-cubical-fixture.v1.json",
}
OUTPUT = VOE / "agda" / "generated" / "RHGeneratedFixture.agda"
BAD_OUTPUT = VOE / "agda" / "negative" / "BadGeneratedMatrix.agda"
RESULT = VOE / "results" / "cubical_agda_fixture_generation.json"


class ContractError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_legacy(signature: dict, common: dict, overlay: dict) -> None:
    require(signature.get("schema") == "marici.voevodsky.cyclic-residue-feedback-signature.v1", "wrong signature schema")
    require(common.get("schema") == "marici.voevodsky.cyclic-common-interface.v1", "wrong common-interface schema")
    require(signature.get("orientation") == "counterclockwise successor i -> i+1 mod 3", "wrong cyclic orientation")
    require(set(signature.get("vertices", {})) == {"A", "B", "C"}, "vertices must be exactly A, B, C")
    require(signature.get("cycle_cell", {}).get("status", "").startswith("materialized_as_lax_filler"), "cycle status contradicts fixture realization")
    require(common.get("completion", {}).get("preserve_epsilon") is True, "completion does not preserve epsilon")
    adapter = overlay.get("cubical_adapter", {})
    require(adapter.get("projection") == {"vertices": "level0", "edge_cells": "level1", "Omega_ABC": "level2", "residual_feedback": "child_tower"}, "SCC projection mismatch")
    require(adapter.get("promotion_policy") == "residual re-entry cannot modify parent without cubical_residual_parent_promotion", "promotion policy mismatch")
    require(adapter.get("cubical_type_theory_implementation") is True, "native implementation not declared")
    require(adapter.get("source_global_naturality") is False, "generator cannot certify source-global naturality")
    require(adapter.get("canonical_scc_contract_mutated") is False, "canonical SCC mutation asserted")


def validate_native(native: dict) -> None:
    require(native.get("schema") == "marici.voevodsky.native-cubical-fixture.v1", "wrong native schema")
    require(native.get("coefficient_ring") == "Z", "only integer fixture coefficients are admitted")
    vertices = native.get("vertices", [])
    require([v.get("id") for v in vertices] == ["A", "B", "C"], "native vertices must be ordered A, B, C")
    require(native.get("successor") == {"A": "B", "B": "C", "C": "A"}, "native successor is not the directed three-cycle")
    maps: dict[str, tuple[str, str]] = {}
    for vertex in vertices:
        for label, field in ((f"G_{vertex['id']}", "generator"), (f"C_{vertex['id']}", "coherencer")):
            arrow = vertex[field]
            maps[label] = (arrow["source"], arrow["target"])
    transports = native.get("residue_transports", [])
    require([t.get("id") for t in transports] == ["T_A", "T_B", "T_C"], "transport order mismatch")
    for transport in transports:
        maps[transport["id"]] = (transport["source"], transport["target"])
    for transition in native.get("transitions", []):
        maps[transition["id"]] = (transition["source"], transition["target"])
    edges = native.get("edge_cells", [])
    require([e.get("id") for e in edges] == ["alpha_A", "alpha_B", "alpha_C"], "edge-cell order mismatch")
    for edge in edges:
        path = edge.get("source_path", [])
        require(len(path) == 3 and all(name in maps for name in path), f"{edge.get('id')} has unknown path maps")
        arrows = [maps[name] for name in path]
        require(arrows[0][1] == arrows[1][0] and arrows[1][1] == arrows[2][0], f"{edge['id']} source path is not composable")
        require(edge.get("target") in maps, f"{edge['id']} target map is absent")
        require((arrows[0][0], arrows[-1][1]) == maps[edge["target"]], f"{edge['id']} boundaries are not parallel")
    omega = native.get("omega", {})
    require(omega.get("oriented_faces") == ["alpha_A", "alpha_B", "alpha_C"], "Omega face orientation mismatch")
    require(omega.get("filler_status") == "fixture_inhabited_unique_mod_vertex_adjustment", "Omega filler status mismatch")
    complex_ = native.get("chain_complex", {})
    d1, d2 = complex_.get("d1_matrix"), complex_.get("d2_matrix")
    require(isinstance(d1, list) and len(d1) == 3 and all(isinstance(r, list) and len(r) == 3 for r in d1), "d1 must be 3 by 3")
    require(isinstance(d2, list) and len(d2) == 1 and len(d2[0]) == 3, "d2 must be 1 by 3")
    require(all(isinstance(c, int) and c in (-1, 0, 1) for row in d1 + d2 for c in row), "matrix coefficients must be -1, 0, or 1")
    require(complex_.get("c1_basis") == ["A", "B", "C"], "c1 basis mismatch")
    require(complex_.get("c2_basis") == ["alpha_A", "alpha_B", "alpha_C"], "c2 basis mismatch")
    require(complex_.get("c3_basis") == ["Omega_ABC"], "c3 basis mismatch")
    require(native.get("completion", {}).get("preserves_injection") is True, "completion preservation absent")
    reentry = native.get("residual_reentry", {})
    require(reentry.get("source") == "child_tower" and reentry.get("target") == "parent_tower", "residual tower typing mismatch")
    require(reentry.get("authority_constructor") is None, "fixture silently contains promotion authority")
    require(reentry.get("required_constructor") == "cubical_residual_parent_promotion", "wrong promotion constructor")


def term(coefficient: int, variable: str) -> str | None:
    return {1: variable, -1: f"(- {variable})", 0: None}[coefficient]


def linear(row: list[int], variables: list[str]) -> str:
    terms = [term(c, v) for c, v in zip(row, variables)]
    return " + ".join(t for t in terms if t is not None) or "0"


def render(native: dict, hashes: dict[str, str], module: str) -> str:
    d1 = native["chain_complex"]["d1_matrix"]
    d2 = native["chain_complex"]["d2_matrix"][0]
    r1 = [linear(row, ["a v", "b v", "c v"]) for row in d1]
    r2 = linear(d2, ["x v", "y v", "z v"])
    return f'''{{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}}
module {module} where

-- Generated from structured contracts. Do not edit.
-- native contract sha256: {hashes["native"]}
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
open import RHNativeFixture using (integerAdapter; integerCompletion; fixture-completion-preserved)
open import CompletionPreservation

record Generatedℤ³ : Type where
  constructor triple
  field a b c : ℤ
open Generatedℤ³

generated∂₁ : Generatedℤ³ → Generatedℤ³
generated∂₁ v = triple ({r1[0]}) ({r1[1]}) ({r1[2]})

x y z : Generatedℤ³ → ℤ
x = a
y = b
z = c

generated∂₂ : Generatedℤ³ → ℤ
generated∂₂ v = {r2}

generated-chain : (v : Generatedℤ³) → generated∂₂ (generated∂₁ v) ≡ 0
generated-chain v = solve! ℤCommRing

generated-cycle : ℤ → ℤ → Generatedℤ³
generated-cycle p q = triple p q (- (p + q))

generated-preimage : ℤ → ℤ → Generatedℤ³
generated-preimage p q = triple 0 p (p + q)

generated-exact-a : (p q : ℤ) → a (generated∂₁ (generated-preimage p q)) ≡ p
generated-exact-a p q = solve! ℤCommRing

generated-exact-b : (p q : ℤ) → b (generated∂₁ (generated-preimage p q)) ≡ q
generated-exact-b p q = solve! ℤCommRing

generated-exact-c : (p q : ℤ) → c (generated∂₁ (generated-preimage p q)) ≡ - (p + q)
generated-exact-c p q = solve! ℤCommRing

generated-exact : (p q : ℤ) → generated∂₁ (generated-preimage p q) ≡ generated-cycle p q
generated-exact p q i = triple (generated-exact-a p q i) (generated-exact-b p q i) (generated-exact-c p q i)

generated-completion-preserved :
  (n : ℤ) → map integerAdapter (inject integerCompletion n) ≡ inject integerCompletion n
generated-completion-preserved = fixture-completion-preserved
'''


def rejected_cases(signature: dict, common: dict, overlay: dict, native: dict) -> list[dict]:
    cases = []

    def reject(name: str, mutate) -> None:
        s, c, o, n = map(copy.deepcopy, (signature, common, overlay, native))
        mutate(s, c, o, n)
        try:
            validate_legacy(s, c, o)
            validate_native(n)
        except ContractError as error:
            cases.append({"id": name, "rejected": True, "residual": str(error)})
        else:
            raise AssertionError(f"hostile semantic fixture admitted: {name}")

    reject("clockwise_orientation", lambda s, c, o, n: n.__setitem__("successor", {"A": "C", "C": "B", "B": "A"}))
    reject("nonparallel_alpha_A", lambda s, c, o, n: n["edge_cells"][0].__setitem__("target", "Phi_B"))
    reject("reversed_T_A", lambda s, c, o, n: n["residue_transports"][0].update(source="P_B", target="R_A"))
    reject("completion_not_preserved", lambda s, c, o, n: n["completion"].__setitem__("preserves_injection", False))
    reject("promotion_authority_inserted", lambda s, c, o, n: n["residual_reentry"].__setitem__("authority_constructor", "fabricated"))
    reject("source_global_naturality_promoted", lambda s, c, o, n: o["cubical_adapter"].__setitem__("source_global_naturality", True))
    return cases


def main() -> None:
    data = {name: load(path) for name, path in PATHS.items()}
    validate_legacy(data["signature"], data["common"], data["overlay"])
    validate_native(data["native"])
    hashes = {name: digest(path) for name, path in PATHS.items()}
    tests = rejected_cases(data["signature"], data["common"], data["overlay"], data["native"])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(data["native"], hashes, "RHGeneratedFixture"), encoding="utf-8")
    malformed = copy.deepcopy(data["native"])
    malformed["chain_complex"]["d1_matrix"][0][0] = 1
    BAD_OUTPUT.write_text(render(malformed, hashes, "BadGeneratedMatrix"), encoding="utf-8")
    result = {
        "schema": "marici.voevodsky.cubical-agda-fixture-generation.v2",
        "passed": True,
        "inputs": {str(path.relative_to(ROOT)).replace("\\", "/"): digest(path) for path in PATHS.values()},
        "generated": str(OUTPUT.relative_to(ROOT)).replace("\\", "/"),
        "generated_sha256": digest(OUTPUT),
        "semantic_hostile_tests": tests,
        "semantic_hostile_rejected": len(tests),
        "generated_matrix_hostile": str(BAD_OUTPUT.relative_to(ROOT)).replace("\\", "/"),
        "positive_agda_typecheck": "pending separate governed execution",
        "negative_agda_typecheck": "pending separate governed execution",
        "source_global_naturality": False,
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "generated", "semantic_hostile_rejected": len(tests)}))


if __name__ == "__main__":
    main()
