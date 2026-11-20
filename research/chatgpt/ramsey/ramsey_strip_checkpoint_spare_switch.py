"""Construct the false checkpoint return from the *unused midpoint*, without an alternative-path search. Independently compare its missing midpoint to all radius-three corridor candidates at all four endpoint pairs."""
from collections import Counter
from ramsey_strip_checkpoint_corridor_proof import N,r,rep,labels,midpoints
from ramsey_strip_prism_proof import V,E
from pathlib import Path
import json
rows=json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text());hist=Counter()
for row in rows:
 p=row['path'];q=[r[v] for v in p];fold=[labels[rep(x)] for x in q[1:-1]];rem=V-set(fold);assert len(rem)==2;ok=tuple(sorted(rem)) in E;assert ok==row['closes'];extras={k:midpoints(p,k)-{q[11-k]} for k in (4,7)};false=[]
 for U in (v for v in rem if v.isupper()):
    ix=[i for i,v in enumerate(fold,1) if v[0]==U.lower()];
    if len(ix)!=2:continue
    i,j=ix;assert j-i==4
    def unused_copy(x):
        v,=[n for n in N[x] if labels.get(rep(n))==U];return v
    a,b=map(unused_copy,(q[i],q[j]));assert a==r[b];f,=[v for v in N[a]&N[b] if r[v]==v];h=q[:i+1]+[a,f,b]+q[j:];assert len(h)==len(set(h))==12 and set(h[1:-1]).isdisjoint(p[1:-1]);assert all(y in N[x] for x,y in zip(h,h[1:]));held,=[k for k in (4,7) if h[k]==q[k]];false.append((held,h[11-held]));assert h[1]==q[1] and h[10]==q[10]
 assert {(k,v) for k,vs in extras.items() for v in vs}==set(false);assert len(false)==int(not ok);hist[ok,tuple(sorted('mid' if x.isupper() else 'corner' for x in rem)),len(false)]+=1
print('closure, remaining positions, constructed checkpoint ambiguities:',hist)
