"""Exact descent test for the two-mode zero-frequency multi-Rees lens."""
import json
from fractions import Fraction as Q
from pathlib import Path


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def tr(a): return [list(x) for x in zip(*a)]
def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def eq(a,b): return all(a[i][j]==b[i][j] for i in range(len(a)) for j in range(len(a[0])))


Z=Q(0); O=Q(1)
# Mode-major ordering (q1,p1,q2,p2). Passive mode rotation with cos=3/5,sin=4/5.
c=Q(3,5); s=Q(4,5)
S=[[c,Z,s,Z],[Z,c,Z,s],[-s,Z,c,Z],[Z,-s,Z,c]]
I=[[O if i==j else Z for j in range(4)] for i in range(4)]
assert eq(mm(S,tr(S)),I)

B1=[[Q(1,2),Z,Z,Z],[Z,Z,Z,Z],[Z,Z,Z,Z],[Z,Z,Z,Z]]
B2=[[Z,Z,Z,Z],[Z,Z,Z,Z],[Z,Z,Q(1,2),Z],[Z,Z,Z,Z]]
B1p=mm(mm(S,B1),tr(S)); B2p=mm(mm(S,B2),tr(S))
Bsum=add(B1,B2); Bsump=add(B1p,B2p)
assert eq(Bsump,Bsum)  # the q-plane coefficient is invariant under passive mixing
assert not eq(B1p,B1) and not eq(B2p,B2)

# At the coincident source h0=diag(0,1,0,1), the same passive mixing is a
# stabilizer, so h0 cannot distinguish the two decompositions.
h0=[[Z,Z,Z,Z],[Z,O,Z,Z],[Z,Z,Z,Z],[Z,Z,Z,O]]
assert eq(mm(mm(S,h0),tr(S)),h0)

packet={
 "schema":"marici.two-mode-gaussian-rees-descent.v1",
 "rotation":{"cos":"3/5","sin":"4/5"},
 "coincident_source_is_fixed":True,
 "individual_lines_are_fixed":False,
 "combined_boundary_coefficient_is_fixed":True,
 "B1_prime":[[str(x) for x in row] for row in B1p],
 "B2_prime":[[str(x) for x in row] for row in B2p],
 "Bsum":[[str(x) for x in row] for row in Bsum],
 "classification":"multi-Rees boundary coefficients glue as a rank-two associated bundle; splitting into two lines is chart/frame data at coincident degeneracy",
 "conclusion":"The occurrence-resolved lines transform covariantly away from coincidence but do not descend individually through the enlarged source stabilizer. Their combined rank-two q-plane coefficient is canonical. No new Carrier incidence is required; coefficient descent remembers the stabilizer representation.",
}
out=Path(__file__).parent/'results'/'two-mode-gaussian-rees-descent.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
