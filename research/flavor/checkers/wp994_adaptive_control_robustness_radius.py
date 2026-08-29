"""WP994: exact robust radii of the WP993 adaptive section."""

import json
from fractions import Fraction as F
from pathlib import Path


def region(label, Q, R):
    if label == "commuting":
        return Q < 0 and R < -3087 * Q
    if label == "rank_two":
        return Q > 0 and R < 24696 * Q
    if label == "full_rank":
        return R > -3087 * Q and R > 24696 * Q
    raise ValueError(label)


targets = {
    "commuting": (F(-1), F(0)),
    "rank_two": (F(1), F(0)),
    "full_rank": (F(0), F(1)),
}
radii = {
    "commuting": F(3087, 3088),
    "rank_two": F(24696, 24697),
    "full_rank": F(1, 24697),
}
boundary_hostiles = {
    "commuting": (radii["commuting"], radii["commuting"]),
    "rank_two": (-radii["rank_two"], radii["rank_two"]),
    "full_rank": (radii["full_rank"], -radii["full_rank"]),
}

interior_checks = {}
boundary_failures = {}
for label, radius in radii.items():
    Q0, R0 = targets[label]
    r = radius / 2
    corners = ((-r, -r), (-r, r), (r, -r), (r, r))
    interior_checks[label] = all(region(label, Q0 + dQ, R0 + dR) for dQ, dR in corners)
    dQ, dR = boundary_hostiles[label]
    boundary_failures[label] = not region(label, Q0 + dQ, R0 + dR)

checks = {
    "all_half_radius_error_boxes_are_admitted": all(interior_checks.values()),
    "all_declared_boundary_hostiles_fail_strict_selection": all(boundary_failures.values()),
    "full_rank_is_unique_bottleneck": radii["full_rank"] < radii["commuting"] < radii["rank_two"],
    "joint_uniform_radius": min(radii.values()) == F(1, 24697),
}

result = {
    "schema": "marici.flavor.wp994-adaptive-control-robustness-radius.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "linfinity_radii": {key: str(value) for key, value in radii.items()},
    "joint_radius": str(min(radii.values())),
    "bottleneck": "full_rank",
    "boundary_hostiles": {
        key: [str(pair[0]), str(pair[1])] for key, pair in boundary_hostiles.items()
    },
    "classification": "formal robust feedback margin; neither source selector nor calibrated apparatus",
    "smallest_exact_falsifier": "the full-rank error corner dQ=1/24697, dR=-1/24697 reaches the rank-two/full-rank boundary exactly",
    "remaining_gate": "independently calibrated joint error bound strictly below 1/24697 in invariant control units, including measurement, feedback, actuation, and common-mode covariance",
}

out = Path(__file__).parents[1] / "results" / "wp994_adaptive_control_robustness_radius.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
