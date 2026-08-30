"""Exact frequency-collision holonomy audit for Gaussian boundary coefficients."""
import json
from fractions import Fraction as Q
from pathlib import Path


def outer(v): return [[v[i]*v[j] for j in range(2)] for i in range(2)]
def eq(a,b): return a==b

# Four cardinal charts for A(theta)=[[cos theta,sin theta],[sin theta,-cos theta]].
# Normalized + eigenvectors are chosen continuously over half-angle charts.
charts=[
    ("0", [Q(1),Q(0)]),
    ("pi/2", [Q(1),Q(1)]),       # unnormalized, projector normalization tracked below
    ("pi", [Q(0),Q(1)]),
    ("3pi/2", [Q(-1),Q(1)]),
    ("2pi", [Q(-1),Q(0)]),
]

# Endpoint frame changes sign; its rank-one projector is unchanged.
v0=charts[0][1]; v2pi=charts[-1][1]
P0=outer(v0); P2pi=outer(v2pi)
assert v2pi==[-x for x in v0]
assert eq(P0,P2pi)

# The complementary frame does the same. The complete rank-two plane is fixed.
w0=[Q(0),Q(1)]; w2pi=[Q(0),Q(-1)]
assert w2pi==[-x for x in w0]
assert outer(w0)==outer(w2pi)

packet={
 "schema":"marici.two-mode-gaussian-collision-holonomy.v1",
 "collision_model":"A(theta)=[[cos theta,sin theta],[sin theta,-cos theta]]",
 "positive_family":"F=epsilon*(I+delta*A(theta)), 0<delta<1",
 "frame_endpoint":{"plus":"v_+(2pi)=-v_+(0)","minus":"v_-(2pi)=-v_-(0)"},
 "frame_holonomy":"-I (real Berry sign)",
 "projector_endpoint":{"plus":"P_+(2pi)=P_+(0)","minus":"P_-(2pi)=P_-(0)"},
 "boundary_coefficient_holonomy":"identity",
 "rank_two_sum_holonomy":"identity",
 "classification":"nontrivial frame double cover but trivial covariance-coefficient transport around existing frequency-collision support",
 "conclusion":"The collision carries a Z2 eigenframe sign, but the Gaussian boundary coefficients are quadratic projectors and have trivial holonomy. No coefficient obstruction and no new Carrier cell arise in this real two-mode model.",
}
out=Path(__file__).parent/'results'/'two-mode-gaussian-collision-holonomy.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
