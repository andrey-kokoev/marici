"""Exact real-support census for the rank-two Kummer vertical excess."""

import json
from pathlib import Path


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def radius_numerator(a, b):
    aa, bb, ab = dot(a, a), dot(b, b), dot(a, b)
    det_h = aa * bb - ab * ab
    # d^T adj(H)d for d=(aa,bb).
    value = bb * aa * aa - 2 * ab * aa * bb + aa * bb * bb
    return det_h, value


tested = 0
minimum_r = None
for ax in range(-3, 4):
    for ay in range(-3, 4):
        if (ax, ay) == (0, 0):
            continue
        for bx in range(-3, 4):
            for by in range(-3, 4):
                if (bx, by) == (0, 0) or ax * by - ay * bx == 0:
                    continue
                a = (ax, ay)
                b = (bx, by)
                det_h, r = radius_numerator(a, b)
                assert det_h > 0
                assert r > 0
                tested += 1
                minimum_r = r if minimum_r is None else min(minimum_r, r)

assert tested > 0
result = {
    "schema": "marici.cosmology.rank_two_vertical_excess_real_support.v1",
    "independent_integer_plane_bases_tested": tested,
    "minimum_positive_R": minimum_r,
    "real_solutions_to_w2_plus_R": 0,
    "literal_euclidean_activation": False,
    "analytic_continuation_required": True,
    "passed": True,
}
out = Path(__file__).with_name("results") / "rank-two-vertical-excess-real-support.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
