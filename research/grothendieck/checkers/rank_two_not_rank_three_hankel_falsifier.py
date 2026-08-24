"""Exact falsifier: adjacent rank-two Hankel positivity is not rank three."""

from fractions import Fraction as Q
import json
from pathlib import Path


q = [Q(1), Q(1), Q(2), Q(5), Q(51, 4)]


def det2(a, b, c):
    return a * c - b * b


def det3(m):
    return (
        m[0] * (m[2] * m[4] - m[3] * m[3])
        - m[1] * (m[1] * m[4] - m[2] * m[3])
        + m[2] * (m[1] * m[3] - m[2] * m[2])
    )


adjacent = [det2(q[k], q[k + 1], q[k + 2]) for k in range(3)]
result = {
    "factorially_normalized_jet_q": [str(value) for value in q],
    "adjacent_rank_two_hankel_minors": [str(value) for value in adjacent],
    "all_adjacent_rank_two_minors_strictly_positive": all(v > 0 for v in adjacent),
    "rank_three_hankel_determinant": str(det3(q)),
    "rank_three_strictly_negative": det3(q) < 0,
    "logical_conclusion": (
        "rank-two Hankel/Schwarzian positivity does not imply the first "
        "rank-three moment condition"
    ),
    "rh_proved_or_disproved": False,
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "rank-two-not-rank-three-hankel-falsifier.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
