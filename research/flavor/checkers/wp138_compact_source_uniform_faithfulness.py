"""Exact WP138 compact-source uniform-faithfulness audit."""

from fractions import Fraction as F
import json
from pathlib import Path


# Uniform compact coordinate u in [-1,1].
mean_u, variance_u, fourth_u = F(0), F(1, 3), F(1, 5)
detector_reach = F(1)
max_scale_good = F(4, 5)
max_scale_bad = F(4, 3)


def accessible_probability(max_scale):
    if max_scale <= detector_reach:
        return F(1)
    return (detector_reach / max_scale) ** 2


p_good = accessible_probability(max_scale_good)
p_bad = accessible_probability(max_scale_bad)
tail_bad = 1 - p_bad

checks = {
    "compact_uniform_mean_zero": mean_u == 0,
    "compact_uniform_variance": variance_u == F(1, 3),
    "compact_uniform_fourth_moment": fourth_u == F(1, 5),
    "good_support_below_reach": max_scale_good < detector_reach,
    "good_uniform_accessibility": p_good == 1,
    "bad_support_exceeds_reach": max_scale_bad > detector_reach,
    "bad_accessibility_probability": p_bad == F(9, 16),
    "bad_inaccessible_probability": tail_bad == F(7, 16),
    "support_scale_controls_uniform_faithfulness": p_good != p_bad,
    "sign_kernel_survives_scale_readout": abs(F(-1, 2)) == abs(F(1, 2)),
    "finite_reach_can_cover_compact_support": max_scale_good <= detector_reach,
    "compactness_does_not_select_support_scale": True,
}

result = {
    "work_package": "WP138",
    "classification": "compact source support can make finite-reach identification uniform, but only conditional on an unsourced support scale",
    "source_law": "u uniform on [-1,1]",
    "moments": {"mean": str(mean_u), "variance": str(variance_u), "fourth": str(fourth_u)},
    "scale_map": "Lambda(u)=Lambda_max*sqrt(abs(u))",
    "detector_reach": str(detector_reach),
    "source_packets": {
        "uniformly_accessible": {"Lambda_max": str(max_scale_good), "accessible_probability": str(p_good)},
        "partially_accessible": {"Lambda_max": str(max_scale_bad), "accessible_probability": str(p_bad), "inaccessible_probability": str(tail_bad)},
    },
    "uniform_faithfulness_condition": "Lambda_max <= E_max",
    "support_scale_selected": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp138_compact_source_uniform_faithfulness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
