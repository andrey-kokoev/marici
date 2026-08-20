"""Integral Gysin kernel for a smooth marked hyperplane in a quartic double solid."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-single-mark-gysin.json"


def dot(x,y): return x[0]*y[0]-sum(a*b for a,b in zip(x[1:],y[1:]))


def det(m):
    a=[[Fraction(x) for x in row] for row in m]; out=Fraction(1)
    for c in range(len(a)):
        p=next(i for i in range(c,len(a)) if a[i][c])
        if p!=c: a[c],a[p]=a[p],a[c]; out=-out
        q=a[c][c]; out*=q
        for j in range(c,len(a)): a[c][j]/=q
        for i in range(c+1,len(a)):
            q=a[i][c]
            for j in range(c,len(a)): a[i][j]-=q*a[c][j]
    return int(out)


# Pic(S)=Z<H,E1,...,E7>, intersection diag(1,-1^7), and -K=3H-sum Ei.
antiK=(3,)+(-1,)*7
roots=[]
for i in range(6):
    v=[0]*8; v[i+1]=1; v[i+2]=-1; roots.append(tuple(v))
roots.append((1,-1,-1,-1,0,0,0,0))
assert dot(antiK,antiK)==2
assert all(dot(r,antiK)==0 for r in roots)
gram=[[dot(a,b) for b in roots] for a in roots]
assert abs(det(gram))==2
gysin_row=[dot(tuple(int(i==j) for i in range(8)),antiK) for j in range(8)]
assert gysin_row==[3,1,1,1,1,1,1,1]

packet={
 "schema":"marici.benincasa.four_site_qg_single_mark_gysin.v1",
 "surface":"degree-two del Pezzo double cover of P2 branched over a smooth quartic",
 "picard_basis":["H"]+[f"E{i}" for i in range(1,8)],
 "intersection_form":"diag(1,-1,-1,-1,-1,-1,-1,-1)",
 "anticanonical_vector":antiK,
 "anticanonical_square":2,
 "gysin_row":gysin_row,
 "gysin_rank":1,
 "gysin_cokernel":0,
 "kernel_rank":7,
 "kernel_basis":roots,
 "kernel_gram":gram,
 "kernel_discriminant":abs(det(gram)),
 "kernel_type":"negative E7 root lattice",
 "complement_b3_extension_ranks":{"quartic_double_solid_middle":20,"primitive_tate_kernel":7,"total":27},
 "qualification":"Smooth-section benchmark; source marked sections through nodes require gluing with Entry 1181 before promotion.",
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"gysin_rank":1,"kernel_rank":7,"kernel_discriminant":2,"type":"E7"}))
