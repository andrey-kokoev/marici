"""WP996: Chebyshev-optimal targets under a frozen l-infinity control budget."""

import json
from fractions import Fraction as F
from pathlib import Path


def margins(label, Q, R):
    if label == "commuting":
        return (-Q, -(R + 3087 * Q) / 3088)
    if label == "rank_two":
        return (Q, (24696 * Q - R) / 24697)
    if label == "full_rank":
        return ((R + 3087 * Q) / 3088, (R - 24696 * Q) / 24697)
    raise ValueError(label)


def radius(label, Q, R):
    return min(margins(label, Q, R))


def targets(B):
    return {
        "commuting": (-B, -B),
        "rank_two": (B, -B),
        "full_rank": (-F(7, 49401) * B, B),
    }


budgets = (F(1), F(7), F(101))
rows = {}
for B in budgets:
    t = targets(B)
    rows[str(B)] = {
        label: {
            "target": [str(Q), str(R)],
            "margins": [str(x) for x in margins(label, Q, R)],
            "radius": str(radius(label, Q, R)),
        }
        for label, (Q, R) in t.items()
    }

D = 152500887
alpha = F(76261248, D)
beta = F(76239639, D)
old_full_radius = radius("full_rank", F(0), F(1))
optimal_full_radius = radius("full_rank", -F(7, 49401), F(1))

checks = {
    "weights_positive_and_sum_one": alpha > 0 and beta > 0 and alpha + beta == 1,
    "weighted_full_rank_bound_cancels_Q": (
        alpha * F(3087, 3088) - beta * F(24696, 24697) == 0
    ),
    "weighted_full_rank_bound_is_R_over_5489": (
        alpha * F(1, 3088) + beta * F(1, 24697) == F(1, 5489)
    ),
    "commuting_optimum_is_B": all(
        radius("commuting", *targets(B)["commuting"]) == B for B in budgets
    ),
    "rank_two_optimum_is_B": all(
        radius("rank_two", *targets(B)["rank_two"]) == B for B in budgets
    ),
    "full_rank_optimum_is_B_over_5489": all(
        radius("full_rank", *targets(B)["full_rank"]) == B / 5489 for B in budgets
    ),
    "deliberate_unit_ray_target_is_suboptimal": old_full_radius < optimal_full_radius,
}

result = {
    "schema": "marici.flavor.wp996-bounded-control-chebyshev-optimum.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "optimal_targets": {
        "commuting": ["-B", "-B"],
        "rank_two": ["B", "-B"],
        "full_rank": ["-7B/49401", "B"],
    },
    "per_label_optimal_radii": {
        "commuting": "B",
        "rank_two": "B",
        "full_rank": "B/5489",
    },
    "joint_optimal_radius": "B/5489",
    "old_unit_ray_radius": str(old_full_radius),
    "improvement_factor_over_wp994_ray": str(optimal_full_radius / old_full_radius),
    "sample_rows": rows,
    "classification": "conditional Chebyshev-optimal formal controller under an assumed l-infinity control budget",
    "smallest_exact_falsifier": "the WP994 full-rank ray target (0,B) is suboptimal by the exact factor 24697/5489",
    "remaining_gate": "a source-derived physical control norm and bound B, with calibrated closed-loop error in the dual invariant units",
}

out = Path(__file__).parents[1] / "results" / "wp996_bounded_control_chebyshev_optimum.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
