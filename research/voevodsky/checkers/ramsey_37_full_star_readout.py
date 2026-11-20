"""Exact row-Krylov closure under full red adjacency, with a rotation-average control. No floating point eigenvalue decisions."""
from pathlib import Path
from fractions import Fraction as Q
import json
H=Path(__file__).resolve().parents[1];D=H/'results';w=json.loads((D/'ramsey_37_dual_stars.json').read_text());E=set(map(tuple,w['red_edges']));N=[{j for j in range(22) if tuple(sorted((i,j))) in E} for i in range(22)];orb=[[0],[6]]+w['rows'];M=set(orb[3]+orb[4]);F=[[[5*int(i in s)-2*int(i in M) for i in range(22)] for s in f] for f in w['stars']]
def act(v,middle=False):return [sum(v[j] for j in n if not middle or j in M) if not middle or i in M else 0 for i,n in enumerate(N)]
def basis(V):
    B={}
    for v in V:
        v=list(map(Q,v))
        for j in sorted(B):
            t=v[j];v=[a-t*b for a,b in zip(v,B[j])]
        if any(v):
            j=next(i for i,a in enumerate(v) if a);B[j]=[a/v[j] for a in v]
    return list(B.values())
def closure(V,middle=False):
    B=basis(V);r=[len(B)]
    while True:
        C=basis(B+[act(v,middle) for v in B]);r.append(len(C))
        if len(C)==len(B):return r,C
        B=C
profiles={}
for middle in (True,False):
 for label,f in [('P',F[0]),('Q',F[1]),('PQ',sum(F,[]))]:
    h,b=closure(f,middle);profiles[str((middle,label))]=h
    if not middle and label=='PQ':assert len(b)==16 and all(sum(v[i] for i in o)==0 for v in b for o in orb)
quot=[[len(N[o[0]]&set(t)) for t in orb] for o in orb];assert all([len(N[i]&set(t)) for t in orb]==row for o,row in zip(orb,quot) for i in o)
out=dict(rank_profiles=profiles,orbit_order=['P','Q','A','B','C','D'],invisible_mode_update=quot);print(out);(D/'ramsey_37_full_star_readout.json').write_text(json.dumps(out,indent=2)+'\n')
