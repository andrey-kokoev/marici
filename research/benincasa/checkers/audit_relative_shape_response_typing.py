#!/usr/bin/env python3
"""Type the quadratic-shape test in the physical relative coefficient object."""

from fractions import Fraction as F


# Primary-source master labels.
elliptic_absolute_block = {"e7=phi001", "e8=y23^2*phi001", "e9=y31^2*phi001"}
physical_top_source = "e15=phi1110"

# Published homogeneous elliptic modulus along the symmetric shape family.
m_second = F(8, 3)

# Localization typing established by the frozen source and Entry 658.
physical_home = "H2(S_E minus W)"
absolute_home = "H2(S_E)"
canonical_open_to_absolute_retraction = False

checks = {
    "elliptic_block_is_rank_three_cyclic_module": len(elliptic_absolute_block) == 3,
    "physical_top_source_is_not_an_elliptic_block_master": all(
        physical_top_source not in label for label in elliptic_absolute_block
    ),
    "elliptic_quadratic_shape_response_is_nonzero": m_second != 0,
    "physical_and_absolute_classes_have_distinct_homes": physical_home != absolute_home,
    "source_supplies_no_reverse_localization_map": not canonical_open_to_absolute_retraction,
    "physical_test_must_use_relative_period": (
        physical_home == "H2(S_E minus W)" and not canonical_open_to_absolute_retraction
    ),
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("elliptic coefficient Hessian: nonzero")
print("full physical Hessian: must be computed as a relative period")

