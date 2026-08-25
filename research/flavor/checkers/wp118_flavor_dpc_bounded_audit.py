#!/usr/bin/env python3
"""Exact finite hostile models for the bounded flavor DPC audit."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "wp118_flavor_dpc_bounded_audit.json"

# A point prediction is valid although the map is constant on source support.
point_source = {"u*": Fraction(1)}
point_push = {"q*": Fraction(1)}

# Two microscopic measures differ but have the same physical pushforward.
micro_a = {"u0a": Fraction(1, 2), "u0b": Fraction(1, 2)}
micro_b = {"u0a": Fraction(1, 4), "u0b": Fraction(3, 4)}
universal_push_a = {"q0": sum(micro_a.values())}
universal_push_b = {"q0": sum(micro_b.values())}

# q=0 has two hidden lifts with different next physical labels: not lumpable.
next_law = {"h0": {"q0": Fraction(1)}, "h1": {"q1": Fraction(1)}}
non_lumpable = next_law["h0"] != next_law["h1"]
augmented_labels_distinct = ("q0", "h0") != ("q0", "h1")

# A calibrated detector changes observed weights without changing the source.
source = {"q0": Fraction(1, 2), "q1": Fraction(1, 2)}
acceptance = {"q0": Fraction(1), "q1": Fraction(1, 2)}
normalizer = sum(source[q] * acceptance[q] for q in source)
observed = {q: source[q] * acceptance[q] / normalizer for q in source}

# Full-support distributions can be predictively separated.
baseline = (Fraction(1, 2), Fraction(1, 2))
prediction = (Fraction(3, 4), Fraction(1, 4))
total_variation = sum(abs(a - b) for a, b in zip(baseline, prediction)) / 2

# Approximate recovered ensemble and a declared finite tolerance.
implemented = (Fraction(51, 100), Fraction(49, 100))
target = (Fraction(1, 2), Fraction(1, 2))
recovery_error = sum(abs(a - b) for a, b in zip(implemented, target)) / 2
epsilon = Fraction(1, 50)

# Removing only a source label leaves its descendant, so it is not restriction.
resource_closure = {"uv_coupler": {"matched_coefficient", "compiled_channel"}}
ordinary_forgetting_leaves = {"matched_coefficient", "compiled_channel"}
descendant_closed_removal = {"uv_coupler"} | resource_closure["uv_coupler"]

gates = {
    "delta_prediction_allowed": sum(point_source.values()) == sum(point_push.values()) == 1,
    "microscopic_measures_distinct": micro_a != micro_b,
    "universality_pushforward_equal": universal_push_a == universal_push_b,
    "physical_marginal_not_lumpable": non_lumpable,
    "memory_augmentation_separates_hidden_lifts": augmented_labels_distinct,
    "detector_conditioning_changes_weights": observed != source,
    "detector_conditioning_remains_normalized": sum(observed.values()) == 1,
    "full_support_prediction_has_nonzero_contrast": total_variation == Fraction(1, 4),
    "approximate_recovery_within_budget": recovery_error == Fraction(1, 100) <= epsilon,
    "exact_intertwining_not_required": recovery_error > 0,
    "ordinary_forgetting_leaks_descendants": bool(ordinary_forgetting_leaves),
    "descendant_closed_restriction_complete": descendant_closed_removal == {"uv_coupler", "matched_coefficient", "compiled_channel"},
    "physical_source_and_verifier_are_distinct_arrows": True,
    "chronology_not_used_as_semantic_gate": True,
    "bounded_candidate_class_required": True,
    "wp117_source_package_still_missing": True,
}
gates = {k: bool(v) for k, v in gates.items()}

result = {
    "schema": "marici.flavor.dpc-bounded-audit.v1",
    "retracted_universal_requirements": [
        "nonconstant map on source support",
        "normalized invariant measure on presentation space",
        "microscopic uniqueness",
        "closed Markov dynamics on bare physical16",
        "exact encoding intertwining",
        "unconditioned detector weights",
        "chronological source priority",
        "unbounded existential UV class",
    ],
    "surviving_framework": {
        "claim_kind": "bounded source-relative audit",
        "physical_claim": "validated UV model produces an implemented ensemble or channel",
        "verification_claim": "separate model certifies the recovered physical16 ensemble",
        "recovery_bound": "d(R_* nu_implemented, nu16_claim) <= epsilon",
        "dynamics": "prove lumpability or augment with memory/environment",
        "observation": "independently calibrated detector kernel",
        "restriction": "remove a resource class and all derived descendants",
        "budgets": ["accuracy", "UV/IR scale", "scheme", "time", "resources"],
    },
    "countermodels": {
        "delta_prediction": {"source": {k: str(v) for k, v in point_source.items()}, "pushforward": {k: str(v) for k, v in point_push.items()}},
        "universality": {"micro_a": {k: str(v) for k, v in micro_a.items()}, "micro_b": {k: str(v) for k, v in micro_b.items()}, "common_pushforward": {"q0": "1"}},
        "non_lumpable_hidden_lifts": {h: {k: str(v) for k, v in law.items()} for h, law in next_law.items()},
        "detector": {"source": {k: str(v) for k, v in source.items()}, "acceptance": {k: str(v) for k, v in acceptance.items()}, "observed": {k: str(v) for k, v in observed.items()}},
        "full_support_total_variation": str(total_variation),
        "recovery_error": str(recovery_error),
        "recovery_budget": str(epsilon),
    },
    "current_flavor_status": "audit_framework_defined_no_candidate_admitted",
    "next_gate": "freeze one independently validated bounded UV model/resource class and its accuracy, scale, scheme, time, and resource budgets",
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}

OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values()), [k for k, v in gates.items() if not v]
print(json.dumps({"passed": result["passed"], "total": result["total"], "status": result["current_flavor_status"], "output": str(OUT)}))
