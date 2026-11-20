"""Exhaust five-frame subcovers and test graph isomorphism after toggling only the pole edge. Return an explicit relabeling if it exists."""
from pathlib import Path
from itertools import combinations
import json
H=Path(__file__).resolve().parents[1];D=H/'results';cat=(H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines();covers=[];V=set(range(22));graphs=[]
for o in json.loads((D/'ramsey_37_reciprocal_catalogue.json').read_text())['records']:
    s=cat[o['record']-1];bits=''.join(f'{ord(c)-63:06b}' for c in s[1:]);E={(i,j) for j in range(22) for i in range(j) if bits[j*(j-1)//2+i]=='1'};r=lambda i,j:tuple(sorted((i,j))) in E
    for f in combinations(o['frames'],5):
        U=set(sum(f,[]));
        if len(U)!=20:continue
        p,q=sorted(V-U);W=[[sum(r(i,j) for i in a for j in b) if a!=b else 0 for b in f] for a in f];covers.append(dict(record=o['record'],frames=f,weights=W,poles=[p,q],pole_neighbors=[[sum(r(i,j) for j in a) for a in f] for i in (p,q)],pole_link=r(p,q)));graphs.append(E|{(p,q)})
def iso(A,B):
    n=lambda E,i:{j for j in V if tuple(sorted((i,j))) in E};a=[n(A,i) for i in range(22)];b=[n(B,i) for i in range(22)]
    def rec(P,f):
        if not P:return f
        i=min(P,key=lambda i:len(P[i]));
        for j in P[i]:
            Q={k:{v for v in t if v!=j and (k in a[i])==(v in b[j])} for k,t in P.items() if k!=i};
            if all(Q.values()):
                hit=rec(Q,f|{i:j});
                if hit:return hit
    return rec({i:{j for j in V if len(a[i])==len(b[j])} for i in V},{})
assert len(covers)==2;mapping=iso(*graphs);print([r['record'] for r in covers],'toggle isomorphism',mapping);(D/'ramsey_37_reciprocal_covers.json').write_text(json.dumps(dict(covers=covers,toggle_isomorphism=mapping),indent=2)+'\n')
