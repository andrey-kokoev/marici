"""Recover the unchecked visit from radius-three neighborhoods, not from a census of alternative returns. Compare checking 4 versus 7. Endpoints 0,29 are the literal seed poles."""
import json
from pathlib import Path
from collections import deque
from ramsey_strip_prism_proof import P,T,labels,rep,r
N=[set() for _ in r]
for i,d in enumerate(P):
    for j,m in enumerate(T,15):
        if d in m:N[i].add(j);N[j].add(i)
rows=[z for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(0,29)]
def sphere(start,allowed):
    q=deque([start]);d={start:0}
    while q:
        v=q.popleft()
        if d[v]==3:continue
        for w in (N[v]&allowed)-d.keys():d[w]=d[v]+1;q.append(w)
    return {x for x,h in d.items() if h==3}
def midpoints(p,k):
    q=[r[v] for v in p];b=q[1 if k==7 else 10];forbid=set(p)|set(q[k+1:11] if k==7 else q[1:k]);available=set(range(30))-forbid
    return sphere(q[k],available)&sphere(b,available)
for j,z in enumerate(rows,1):
    p=z['path'];toward=labels[rep(p[3])][0].upper()==labels[rep(p[10])][0].upper();k=7 if toward else 4;m=midpoints(p,k);assert m=={r[p[11-k]]};print(j,'check',k,'candidates at unchecked midpoint',sorted(m),'other ordering candidates',len(midpoints(p,11-k)))
assert len(rows)==10
