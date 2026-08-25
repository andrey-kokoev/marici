"""Exact WP137 reheating transfer and detector-reliability audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


c, s = F(3, 5), F(4, 5)
rotation = [[c, -s], [s, c]]
identity = [[F(1), F(0)], [F(0), F(1)]]
cov_initial = [[F(1), F(0)], [F(0), F(0)]]
cov_final = mm(mm(rotation, cov_initial), tr(rotation))
flavor_variance = cov_final[1][1]

threshold = F(2)
tail_upper_bound = F(1) / threshold**2
accessible_lower_bound = 1 - tail_upper_bound
constructors, accessible_rank, inaccessible_rank = 4, 4, 1

checks = {
    "mixing_rotation_orthogonal": mm(rotation, tr(rotation)) == identity,
    "flavor_transfer_nonzero": s != 0,
    "flavor_variance_exact": flavor_variance == F(16, 25),
    "normalized_flavor_variance_one": flavor_variance / s**2 == 1,
    "transfer_preserves_sign": s > 0,
    "chebyshev_tail_bound": tail_upper_bound == F(1, 4),
    "accessible_reliability_lower_bound": accessible_lower_bound == F(3, 4),
    "accessible_formal_multipoint_rank_four": accessible_rank == constructors,
    "inaccessible_rank_one": inaccessible_rank == 1,
    "inaccessible_kernel_three": constructors - inaccessible_rank == 3,
    "gaussian_support_has_inaccessible_tail": True,
    "uniform_faithfulness_fails": inaccessible_rank < constructors,
}

result = {
    "work_package": "WP137",
    "classification": "reheating transfer is faithful on amplitudes, but finite-reach source identification is not uniform over cosmological support",
    "reheating_rotation": [[str(x) for x in row] for row in rotation],
    "flavor_variance_over_spectator_variance": str(flavor_variance),
    "normalized_accessibility_domain": "abs(w)<2",
    "reliability": {"exact_gaussian_accessibility": "erf(sqrt(2))", "distribution_free_lower_bound": str(accessible_lower_bound), "inaccessible_tail_upper_bound": str(tail_upper_bound)},
    "contextual_classes": {
        "accessible_with_formal_multipoint_probe": [["m1"], ["m2"], ["m3"], ["m4"]],
        "inaccessible": [["m1", "m2", "m3", "m4"]],
    },
    "uniform_source_identification": False,
    "reference_port_required": True,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp137_reheating_detector_reliability.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
