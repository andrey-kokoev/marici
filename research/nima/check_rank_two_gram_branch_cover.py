"""Exact polynomial audit of the rank-two Gram branch cover."""

import json
from fractions import Fraction as F
from pathlib import Path


# Normalize a nondegenerate rank-two span to a=(1,0,0), b=(0,1,0).
# Write c=(x,y,0). The first two bisector equations fix h=(1/2,1/2,0).
def consistency(x, y):
    return x * x + y * y - x - y


def fifth_condition(r, t, s):
    # For s != 0, the fifth bisector fixes
    # z=(p^2-r-t)/(2s). Clearing 4s^2 from z^2+1/2 gives this polynomial.
    p2 = r * r + t * t + s * s
    return (p2 - r - t) ** 2 + 2 * s * s


controls = [
    (F(1), F(1), F(0)),       # square corner: consistent
    (F(1), F(0), F(0)),       # repeated point: consistent boundary control
    (F(2), F(1), F(2)),       # generic inconsistent coplanar point
]
consistency_values = [consistency(x, y) for x, y, _ in controls]
assert consistency_values == [0, 0, 2]

# A transverse rational point is generically off fivefold support.
generic_p = (F(1), F(2), F(3))
generic_fifth = fifth_condition(*generic_p)
assert generic_fifth == 139

# The previously used p=(0,0,s) slice factors as s^2(s^2+2).
for sval in (F(1), F(2), F(3)):
    assert fifth_condition(F(0), F(0), sval) == sval * sval * (sval * sval + 2)

result = {
    "schema": "marici.cosmology.rank_two_gram_branch_cover.v1",
    "rank_consistency_polynomial": "x^2 + y^2 - x - y",
    "consistent_controls": sum(v == 0 for v in consistency_values),
    "inconsistent_controls": sum(v != 0 for v in consistency_values),
    "restricted_fourfold_quadratic": "z^2 + 1/2",
    "generic_complex_sheet_count": 2,
    "fifth_support_polynomial": "(r^2+t^2+s^2-r-t)^2 + 2s^2",
    "generic_fifth_value": str(generic_fifth),
    "passed": True,
}
out = Path(__file__).with_name("results") / "rank-two-gram-branch-cover.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
