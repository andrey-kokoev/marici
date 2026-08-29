"""WP995: robustness radius scales with unfrozen target normalization."""

import json
from fractions import Fraction as F
from pathlib import Path


def radii(L):
    return {
        "commuting": F(3087, 3088) * L,
        "rank_two": F(24696, 24697) * L,
        "full_rank": F(1, 24697) * L,
    }


scales = (F(1), F(2), F(17), F(24698))
families = {str(L): {k: str(v) for k, v in radii(L).items()} for L in scales}
joint = {L: min(radii(L).values()) for L in scales}

checks = {
    "all_radii_scale_linearly": all(
        radii(L)[key] == L * radii(F(1))[key]
        for L in scales
        for key in radii(L)
    ),
    "full_rank_remains_bottleneck": all(
        min(radii(L), key=radii(L).get) == "full_rank" for L in scales
    ),
    "joint_radius_is_L_over_24697": all(joint[L] == L * F(1, 24697) for L in scales),
    "deliberate_fixed_radius_claim_fails_at_L2": joint[F(2)] != joint[F(1)],
    "no_finite_upper_radius_without_scale_bound": joint[F(24698)] > F(1),
}

result = {
    "schema": "marici.flavor.wp995-robustness-normalization-no-go.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "scale_family": families,
    "joint_radius_law": "L/24697",
    "classification": "WP994 margin is target-normalization relative, not an intrinsic apparatus threshold",
    "smallest_exact_falsifier": "L=2 doubles the joint radius from 1/24697 to 2/24697 while preserving every region relation",
    "remaining_gate": "a source-derived actuator normalization or cost/support constraint fixing the admissible target scale L",
}

out = Path(__file__).parents[1] / "results" / "wp995_robustness_normalization_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
