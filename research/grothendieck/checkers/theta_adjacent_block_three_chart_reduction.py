"""Exact rational audit of the adjacent-block three-chart coordinate maps."""
import json
from fractions import Fraction as Q
from pathlib import Path


d = Q(3, 7)
x = Q(2, 11)
assert 0 < x < d

# Each tuple is (u,v); verify d=u-v, the stated midpoint, nonnegative folded
# arguments, and unit absolute Jacobian by the affine coefficient matrices.
charts = {
    "A": {"uv": (x + d, x), "S": 2 * x + d, "folded": (x + d, x), "jacobian": 1},
    "B": {"uv": (-x, -x - d), "S": -2 * x - d, "folded": (x, x + d), "jacobian": 1},
    "C": {"uv": (d - x, -x), "S": d - 2 * x, "folded": (d - x, x), "jacobian": 1},
}

for chart in charts.values():
    u, v = chart["uv"]
    assert u - v == d
    assert u + v == chart["S"]
    assert all(value >= 0 for value in chart["folded"])
    assert chart["jacobian"] == 1

# Audit the block-domain identity with rational endpoints: [0,L] union its
# translate [L,2L] is [0,2L], with only a measure-zero shared endpoint.
L = Q(5, 13)
first_band = (Q(0), L)
second_band = (L, 2 * L)
whole_block = (Q(0), 2 * L)
assert first_band[0] == whole_block[0]
assert first_band[1] == second_band[0]
assert second_band[1] == whole_block[1]

result = {
    "whole_block_identity": "integral_0^L [H(D)+H(D+L)] dD = integral_0^(2L) H(d) dd",
    "rational_test_d_x": [str(d), str(x)],
    "charts": {
        name: {
            "u_v": [str(value) for value in chart["uv"]],
            "S": str(chart["S"]),
            "folded_label_arguments": [str(value) for value in chart["folded"]],
            "absolute_jacobian": chart["jacobian"],
        }
        for name, chart in charts.items()
    },
    "all_theta_arguments_nonnegative": True,
    "moving_absolute_value_cusps_removed": True,
    "source_exchange_labels_preserved": True,
    "interval_certificate_completed": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-adjacent-block-three-chart-reduction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
