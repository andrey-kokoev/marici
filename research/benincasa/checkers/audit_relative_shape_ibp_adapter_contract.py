#!/usr/bin/env python3
"""Acceptance contract for a legal exact relative shape-IBP adapter."""

required = {
    "complete_six_simplex_source",
    "second_shape_jet",
    "pole_powers_through_three",
    "length_powers_through_three",
    "occurrence_labels",
    "proper_face_subcomplex",
    "physical_boundary_homotopy",
    "relative_exact_quotient",
    "native_six_term_mate",
    "full_fiber_constancy",
    "source_cycle_authority",
}

marked_relative_engine = {
    "occurrence_labels",
    "proper_face_subcomplex",
    "physical_boundary_homotopy",
    "relative_exact_quotient",
    "first_base_derivative",
    "special_exceptional_geometry",
}

exponent_weighted_engine = {
    "complete_six_simplex_source",
    "pole_powers_through_three",
    "length_powers_through_three",
    "absolute_polynomial_quotient",
}

marked_missing = required - marked_relative_engine
weighted_missing = required - exponent_weighted_engine

checks = {
    "marked_engine_is_not_yet_shape_jet_complete": "second_shape_jet" in marked_missing,
    "marked_engine_lacks_cubic_insertion_depth": "pole_powers_through_three" in marked_missing,
    "weighted_engine_forgets_occurrence_labels": "occurrence_labels" in weighted_missing,
    "weighted_engine_forgets_boundary_homotopy": "physical_boundary_homotopy" in weighted_missing,
    "neither_existing_engine_is_admissible": bool(marked_missing) and bool(weighted_missing),
    "aspect_gates_are_missing_from_both_engines": {
        "native_six_term_mate", "full_fiber_constancy", "source_cycle_authority"
    } <= marked_missing & weighted_missing,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("marked missing:", sorted(marked_missing))
print("weighted missing:", sorted(weighted_missing))
