"""Exact one-parameter audit of the rank-two Kummer vertical excess."""

import json
from fractions import Fraction as F
from pathlib import Path


# Family: a=(1,0,0), b=(0,1,0), c=(1,1,e).
# The first two bisectors fix ell=(1/2,1/2,z). The third and null equations are
#   e(z-e/2)=0,  z^2+1/2=0.
# Their z-resultant is e^2(e^2+2)/4.
def resultant(e):
    return e * e * (e * e + 2) / 4


controls = [F(-3), F(-1), F(0), F(1), F(2), F(5, 3)]
values = [resultant(e) for e in controls]
assert values[2] == 0
assert all(v != 0 for i, v in enumerate(values) if i != 2)

# For e != 0 the linear equation fixes z=e/2, and the null equation becomes
# (e^2+2)/4=0. At e=0 the linear equation disappears and the quadratic has
# two distinct complex roots because its derivative 2z is nonzero there.
for e in controls:
    if e:
        z = e / 2
        assert z * z + F(1, 2) == (e * e + 2) / 4

result = {
    "schema": "marici.cosmology.rank_two_kummer_vertical_excess.v1",
    "family": "a=(1,0,0), b=(0,1,0), c=(1,1,e)",
    "bisector_equation": "e(z-e/2)=0",
    "null_equation": "z^2+1/2=0",
    "resultant": "e^2(e^2+2)/4",
    "gram_vertical_factor": "e^2",
    "nondegenerate_discriminant_factor": "e^2+2",
    "special_fiber_complex_points": 2,
    "generic_fiber_near_e0_points": 0,
    "flat_near_e0": False,
    "passed": True,
}
out = Path(__file__).with_name("results") / "rank-two-kummer-vertical-excess.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
