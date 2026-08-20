"""Integral A1^4 embedding and orthogonal complement inside the E7 Gysin lattice."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-a1four-e7-embedding.json"


def dot(x,y): return x[0]*y[0]-sum(a*b for a,b in zip(x[1:],y[1:]))
def det3(m): return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])

# E7 simple roots in Pic=<H,E1,...,E7>.
alpha=[]
for i in range(6):
    v=[0]*8; v[i+1]=1; v[i+2]=-1; alpha.append(tuple(v))
alpha.append((1,-1,-1,-1,0,0,0,0))
G=[[dot(a,b) for b in alpha] for a in alpha]

# Four orthogonal roots corresponding to the four resolved conic intersections.
a1four=[
 (0,1,-1,0,0,0,0,0),
 (0,0,0,1,-1,0,0,0),
 (0,0,0,0,0,1,-1,0),
 (1,-1,-1,0,0,0,0,-1),
]
assert [[dot(a,b) for b in a1four] for a in a1four]==[[-2,0,0,0],[0,-2,0,0],[0,0,-2,0],[0,0,0,-2]]

# Coordinates in the alpha basis, as derived directly from the displayed roots.
embed_cols=[
 [1,0,0,0,0,0,0],
 [0,0,1,0,0,0,0],
 [0,0,0,0,1,0,0],
 [0,0,1,1,1,1,1],
]
# Primitive iff gcd of maximal minors is one.
minor_values=[]
for rows in itertools.combinations(range(7),4):
    m=[[embed_cols[c][r] for c in range(4)] for r in rows]
    # Bareiss-style recursive determinant at size four.
    val=sum(((-1)**j)*m[0][j]*det3([[m[i][k] for k in range(4) if k!=j] for i in range(1,4)]) for j in range(4))
    minor_values.append(val)
g=0
for x in minor_values:g=math.gcd(g,abs(x))
assert g==1

# Integral basis of the orthogonal complement in alpha coordinates.
complement_basis=[
 [0,0,1,2,1,0,0],
 [1,2,1,-1,0,1,1],
 [0,0,-1,-1,0,1,-1],
]
def pair_coords(x,y): return sum(x[i]*G[i][j]*y[j] for i in range(7) for j in range(7))
complement_gram=[[pair_coords(a,b) for b in complement_basis] for a in complement_basis]
assert abs(det3(complement_gram))==8

# A unimodular basis change inside the complement exhibits A1^3.
orthogonal_roots=[]
for c in [(1,1,-1),(1,1,0),(2,1,0)]:
    orthogonal_roots.append([sum(c[k]*complement_basis[k][i] for k in range(3)) for i in range(7)])
orthogonal_gram=[[pair_coords(a,b) for b in orthogonal_roots] for a in orthogonal_roots]
assert orthogonal_gram==[[-2,0,0],[0,-2,0],[0,0,-2]]

packet={
 "schema":"marici.benincasa.four_site_qg_a1four_e7_embedding.v1",
 "exceptional_root_gram":[[-2,0,0,0],[0,-2,0,0],[0,0,-2,0],[0,0,0,-2]],
 "embedding_columns_in_E7_simple_basis":embed_cols,
 "gcd_maximal_minors":g,
 "embedding_primitive":True,
 "quotient_torsion":[],
 "orthogonal_complement_basis":complement_basis,
 "orthogonal_complement_gram":complement_gram,
 "orthogonal_root_basis":orthogonal_roots,
 "orthogonal_root_gram":orthogonal_gram,
 "orthogonal_complement_type":"A1^3",
 "orthogonal_discriminant":8,
 "direct_sum_index_in_E7":8,
 "four_node_intersection_cohomology_kernel_rank":3,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"primitive":True,"quotient_torsion":0,"complement":"A1^3","rank":3,"gluing_index":8}))
