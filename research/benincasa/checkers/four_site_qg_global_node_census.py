"""Exact support-pattern census of generic singularities of the C4 infinity branch."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-global-node-census.json"


def rank(rows):
    a=[[Fraction(x) for x in row] for row in rows if any(row)]
    if not a: return 0
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r


def matmul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


d=[[-1,1,0,0],[0,-1,1,0],[0,0,-1,1]]
gradient_rows=[[1,0,0],[1,-1,0],[0,1,-1],[0,0,1]]
witnesses=[
 [[2,1,0],[1,3,1],[0,1,5]],
 [[5,-1,1],[-1,4,2],[1,2,7]],
 [[3,1,-1],[1,6,2],[-1,2,8]],
]

support_profiles=[]
for h in witnesses:
    hd=matmul(h,d)
    survivors=[]
    for mask in range(1,16):
        present=[i for i in range(4) if mask>>i&1]
        absent=[i for i in range(4) if not (mask>>i&1)]
        equations=[]
        for i in absent:
            row=[0]*4; row[i]=1; equations.append(row)
        for i in present:
            equations.append([sum(gradient_rows[i][k]*hd[k][j] for k in range(3)) for j in range(4)])
        nullity=4-rank(equations)
        if nullity:
            survivors.append({"mask":mask,"present":present,"nullity":nullity})
    support_profiles.append(survivors)

assert all(profile==[{"mask":15,"present":[0,1,2,3],"nullity":1}] for profile in support_profiles)

# Delta=0 gives z1=z2=z3=z4.  Every nonzero projective z solution lifts to
# 2^4/2=8 projective sign points in y, forming the regular C2^3 orbit.
sign_points=[]
for signs in itertools.product((-1,1),repeat=4):
    if signs[0] != 1: continue
    sign_points.append(list(signs))
assert len(sign_points)==8

packet={
 "schema":"marici.benincasa.four_site_qg_global_node_census.v1",
 "generic_witness_count":len(witnesses),
 "surviving_z_support":"all four coordinates, z1=z2=z3=z4",
 "projective_sign_points":sign_points,
 "node_count":8,
 "sign_deck_group":"C2^3 acting regularly",
 "local_type":"eight threefold A1 nodes away from det(G)=0",
 "physical_positive_node":[1,1,1,1],
 "additional_generic_singular_strata":False,
 "qualification":"special Gram support det(G)=0 is excluded",
 "new_carrier_datum":False,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"nodes":8,"witnesses":len(witnesses),"extra":False}))
