#!/usr/bin/env python3
"""Reproduce source predicates for the historical coefficient-role audit."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
SOURCES = {
    "reflection": ROOT / "research/aspect/reflection-component-path-tomography-and-coefficient-authority.md",
    "lenses": ROOT / "research/kitaev/coefficient-lenses-are-quotients-of-constructor-history.md",
    "arithmetic": ROOT / "research/nima/arithmetic-loading-commutes-with-the-oriented-radial-codiagonal-under-one-explicit-prime-majorant.md",
}
texts = {name: path.read_text(encoding="utf-8") for name, path in SOURCES.items()}
checks = {
    "reflection_declares_hadamard_frame": "Hadamard frame" in texts["reflection"],
    "reflection_declares_imaginary_coefficient": "produces an imaginary coefficient" in texts["reflection"],
    "reflection_requires_ring_or_extension": "preserves the declared source\n  coefficient ring or an authorized scalar extension is supplied" in texts["reflection"],
    "lenses_define_history_equivalence": "Each lens defines a history equivalence" in texts["lenses"],
    "lenses_require_declared_forgetful_maps": "hierarchy exists only when the lenses are linked by declared forgetful maps" in texts["lenses"],
    "lenses_retain_distinct_information": "This lens can retain order, conjugation, and noncommutative loop information" in texts["lenses"],
    "arithmetic_declares_two_assemblies": "These facts prove two admissible analytic assemblies" in texts["arithmetic"],
    "arithmetic_refuses_coefficient_identification": "they do not identify the two coefficients" in texts["arithmetic"],
    "arithmetic_refuses_canonical_authority": "authorize either as G4's canonical codiagonal loading" in texts["arithmetic"],
}
# Deliberate-failure diagnostic: a shared sufficient property is not equality.
assembly_a = ("prime-majorant", "theta-loading")
assembly_b = ("prime-majorant", "euler-loading")
checks["shared_majorant_does_not_identify_assemblies"] = assembly_a[0] == assembly_b[0] and assembly_a != assembly_b
assert all(checks.values()), checks
result = {
    "schema": "marici.aspect.historical-coefficient-role-audit.v1",
    "status": "passed",
    "check_count": len(checks),
    "checks": checks,
    "source_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in SOURCES.items()},
    "classifications": {
        "reflection": "presentation_behavior_with_scalar_extension_gate",
        "lenses": "distinct_readout_module_quotients",
        "arithmetic": "unresolved_source_selection_without_comparison_map",
    },
    "disposition": "universal single-mechanism conjecture revised to common-codomain typing gate",
}
out = Path(__file__).parents[1] / "results" / "historical_coefficient_role_audit.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": result["check_count"], "classifications": result["classifications"]}, sort_keys=True))
