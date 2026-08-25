#!/usr/bin/env python3
"""Finite countermodels to the overstrong universal DPC formulation."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


OUT = Path(__file__).parents[1] / "results" / "dpc-universal-law-countermodels.json"
TOL = 1e-12


def main():
    # 1. Chronology is not semantic evidence: identical validated models can
    # differ only in whether they were written before or after seeing a target.
    predictions = {"gate": "T", "phase": "pi/4", "holdout": "echo_sign_reversal"}
    prior_model = {"discovery_order": "source_first", "predictions": predictions}
    posterior_model = {"discovery_order": "target_first", "predictions": predictions}
    chronology_countermodel = prior_model["predictions"] == posterior_model["predictions"]

    # 2. No named resource is necessary when two interchangeable realizations
    # exist, although the non-Clifford resource class is necessary.
    resources = {"direct_T_coupler", "injected_T_state"}
    reachable = lambda rs: "T" if rs & resources else "Clifford_only"
    named_resource_necessity_fails = (
        reachable(resources - {"direct_T_coupler"}) == "T"
        and reachable(resources - {"injected_T_state"}) == "T"
    )
    class_obstruction_survives = reachable(set()) == "Clifford_only"

    # 3. Universality: distinct microscopic Hamiltonians have exactly the same
    # compressed low-energy action.  Q acts only on an irrelevant high-energy
    # level, so lambda is invisible in the effective code sector.
    p = np.diag([1, 1, 0]).astype(complex)
    z_low = np.diag([1, -1, 0]).astype(complex)
    q_high = np.diag([0, 0, 1]).astype(complex)
    compressed = [p @ (z_low + lam * q_high) @ p for lam in (-7, -1, 0, 2, 11)]
    universality_countermodel = bool(
        all(np.max(np.abs(row - compressed[0])) < TOL for row in compressed)
    )

    # 4. Exact projector intertwining is unnecessary under code deformation.
    # U moves the code span {e0,e1} to {e0,e2}; recovery U^dagger returns it.
    u = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    exact_intertwining_fails = bool(np.max(np.abs(u @ p - p @ u @ p)) > 0.5)
    recovered_action = u.conj().T @ u @ p
    recovered_channel_is_exact = bool(np.max(np.abs(recovered_action - p)) < TOL)

    # 5. Source production and certificate derivation are different maps.
    physical_map = {"input": "coupler_and_pulse", "output": "implemented_channel"}
    verification_map = {"input": "validated_noise_model_and_channel", "output": "diamond_bound"}
    certificate_category_is_distinct = physical_map["output"] != verification_map["output"]

    # 6. Ordinary forgetting leaves derived products; counterfactual resource
    # restriction must remove the full descendant closure.
    derivation_edges = {"factory": {"magic_state"}, "magic_state": {"compiled_T"}}
    retained_after_source_forgetting = {"magic_state", "compiled_T"}
    descendant_closure = {"factory", "magic_state", "compiled_T"}
    ordinary_forgetting_does_not_restore_obstruction = "compiled_T" in retained_after_source_forgetting
    counterfactual_closure_removal_restores = not ({"compiled_T"} - descendant_closure)

    # 7. A finite reachability claim is meaningful only with explicit budgets.
    bounded_reachability_contract = {
        "accuracy_epsilon": 1e-6,
        "time_horizon": 1000,
        "gate_budget": 10000,
        "resource_class": "declared_non_clifford_ports",
        "decision": "testable_finite_contract",
    }

    countermodels = {
        "chronological_independence_is_not_semantic": chronology_countermodel,
        "named_resource_necessity_fails_under_substitution": named_resource_necessity_fails,
        "resource_class_obstruction_survives": class_obstruction_survives,
        "microscopic_nonuniqueness_can_be_universality": universality_countermodel,
        "exact_intertwining_not_necessary": exact_intertwining_fails and recovered_channel_is_exact,
        "physical_source_does_not_generate_mathematical_certificate": certificate_category_is_distinct,
        "ordinary_forgetting_does_not_restore_obstruction": ordinary_forgetting_does_not_restore_obstruction,
        "descendant_closed_counterfactual_restriction_restores": counterfactual_closure_removal_restores,
    }
    assert all(countermodels.values())

    result = {
        "schema": "marici.kitaev.dpc-universal-law-countermodels.v1",
        "countermodels": countermodels,
        "code_deformation": {
            "UP_equals_PUP": False,
            "recovery_after_deformation_exact_on_code": recovered_channel_is_exact,
        },
        "universality_family": {
            "microscopic_parameters": [-7, -1, 0, 2, 11],
            "common_compressed_generator": "diag(1,-1) on the low-energy sector",
        },
        "bounded_reachability_contract": bounded_reachability_contract,
        "retracted_universal_requirements": [
            "chronological source priority",
            "necessity of one named resource",
            "microscopic counterfactual uniqueness",
            "certificate co-generation by physical dynamics",
            "exact code-projector intertwining",
            "ordinary forgetting as counterfactual restriction",
            "unbudgeted exact reachability",
        ],
        "surviving_audit_framework": {
            "physical_model": "independently validated, possibly discovered post hoc",
            "generation_claim": "bounded reachability within epsilon, time, and resource budgets",
            "obstruction_claim": "resource-class monotone or bounded no-go",
            "verification_claim": "separate model-to-certificate derivation",
            "fault_tolerance_claim": "recovered-channel bound, allowing code deformation and gauge fixing",
            "restriction_claim": "remove the declared resource class and its derived descendants",
            "universality_claim": "predictions may depend only on the validated effective class",
        },
        "verdict": "The sharpened DPC is false as a universal law. Finite countermodels defeat chronological independence, named-resource necessity, microscopic uniqueness, certificate co-generation, exact intertwining, and ordinary forgetting. What survives is a bounded audit framework relating an independently validated physical model to resource-class constraints and a separate recovered-channel certificate.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
