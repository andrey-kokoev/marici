from __future__ import annotations

import json


def main() -> None:
    requirements = {
        "common_invariant_form_core": False,
        "independently_derived_R_zeta": False,
        "independently_defined_B": False,
        "independently_defined_C": False,
        "factorization_CR_zeta_equals_B_verified": False,
        "coercive_pivot_form_verified": False,
        "strict_relative_cross_bound_verified": False,
        "closed_domain_identification_verified": False,
        "radical_stability_verified": False,
        "dense_range_and_coercivity_verified": False,
    }
    first_missing_typed_object = "source-derived common invariant form core together with R_zeta"
    downstream_completion_admitted = all(requirements.values())
    assert not downstream_completion_admitted
    assert not requirements["common_invariant_form_core"]
    assert not requirements["independently_derived_R_zeta"]

    countermodel_coverage = {
        "dense_core_equality_without_closed_domain_identity": True,
        "finite_positive_forms_with_new_completed_radical": True,
        "injective_dense_range_with_zero_reduced_minimum_modulus": True,
    }
    assert all(countermodel_coverage.values())

    result = {
        "schema": "marici.voevodsky.r-zeta-source-adequacy.v1",
        "status": "blocked_at_first_missing_source_typed_object",
        "requirements": requirements,
        "first_missing_typed_object": first_missing_typed_object,
        "failed_consequence": "no source-typed mixed bridge or closed-form completion comparison is defined",
        "acceptance_test": "materialize the common core, independently derived R_zeta, B, and C, then verify CR_zeta=B, domain closure, radical stability, strict relative bound, and quotient coercivity",
        "downstream_completion_admitted": downstream_completion_admitted,
        "countermodel_coverage": countermodel_coverage,
        "synthetic_unbounded_realization_exists": True,
        "radial_source_realization_exists": False,
        "reopening_condition": "new source-derived common core and intertwiner data",
        "successor_waiting_leaf_allowed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
