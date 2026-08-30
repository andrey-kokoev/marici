import json
from pathlib import Path

# Exact resultant from Entry 1769:
# Res_v(4P6,D)=16*u^4*(u-1)^2*c(u), c=1-8u+12u^2-4u^3.
# At u=1, both u and c are units, so the local intersection multiplicity is 2.
c_at_one = 1 - 8 + 12 - 4
assert c_at_one == 1
intersection_multiplicity = 2

# Both branches are smooth at x=u-1=z=v-1=0; their linear terms are 8x and -4x.
linear_p = (8, 0)
linear_d = (-4, 0)
assert linear_p[0] != 0 and linear_d[0] != 0
assert linear_p[0]*linear_d[1] - linear_p[1]*linear_d[0] == 0

# Two smooth branches with contact order two form an A3 tacnode.
# For x^2+y^4, the total-link Alexander polynomial is
# Delta(t)=(t-1)*(t^2+1), of degree mu=3.
def delta(t):
    return (t - 1)*(t*t + 1)

assert delta(-1) == -4

packet = {
    "schema": "marici.p6_d_tacnode_kummer.v1",
    "center": {"u": 1, "v": 1, "support": ["X2=0", "X3=0"]},
    "branch_linear_terms": {"4P6": "8*x", "D": "-4*x"},
    "intersection_multiplicity": intersection_multiplicity,
    "union_formal_type": "A3 tacnode: Y^2-X^4",
    "milnor_number": 3,
    "relative_hom_character": {"P6_meridian": -1, "D_meridian": -1},
    "total_character": -1,
    "alexander_polynomial": "(t-1)*(t^2+1)",
    "alexander_at_character": -4,
    "twisted_link_cohomology_dimensions": [0, 0, 0],
    "supported_relative_sign_rank": 0,
}
Path("research/benincasa/results/p6-d-tacnode-kummer.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
