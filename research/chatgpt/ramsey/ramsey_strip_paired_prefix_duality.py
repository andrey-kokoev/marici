"""Identify the endpoint exchange from one or two matched visits at opposite ends. No closure or square used as input."""
from collections import Counter
import json
from pathlib import Path
from ramsey_strip_ordered_boundary_dualities import solutions,s,t,r
out=Counter()
for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()):
    p=z['path']
    if (p[0],p[-1])!=(s,t):continue
    candidates=list(solutions)
    for i in (1,2,3):
        candidates=[f for f in candidates if f[p[i]]==p[-1-i]]
        if i==1:assert len(candidates)==2
        if i==2:
            f,=candidates;order=2 if f[f[p[1]]]==p[1] else 4
            assert all(f[f[x]]==(x if order==2 else r[x]) for x in range(30))
    out[order,bool(candidates),z['closes']]+=1
print('(order, third paired visit matches, closes)',out)
