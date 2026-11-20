"""Test f(p[i])=r(p[11-i]) as an ordered half-path extension. Distinguish matching both boundary ports from matching every visit."""
import json
from pathlib import Path
from collections import Counter
from ramsey_strip_ordered_boundary_dualities import solutions,r,s,t,entry,exit
cases=Counter()
for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()):
    p=z['path']
    if (p[0],p[-1],p[1],p[-2])!=(s,t,entry[0],exit[1]):continue
    q=[r[v] for v in reversed(p)];f,=[f for f in solutions if f[p[1]]==q[1] and f[p[-2]]==q[-2]]
    assert all(f[f[i]]==i for i in range(30));cases[all(f[x]==y for x,y in zip(p,q)),z['closes']]+=1
print('(full reflected leg extension, closes):',cases);assert sum(cases.values())==5
