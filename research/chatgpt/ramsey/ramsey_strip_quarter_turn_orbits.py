"""Follow an endpoint square root on oriented literal-seed routes without prematurely identifying a route with its reflected copy. Track boundary row phase and residual closure."""
import json
from pathlib import Path
from ramsey_strip_ordered_boundary_dualities import solutions,r,s,t,entry,exit
rows=[z for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(s,t)]
swap=lambda p:tuple(r[v] for v in p)
lookup={}
for i,z in enumerate(rows,1):
    p=tuple(z['path']);lookup[p]=(i,0,z['closes']);lookup[swap(p)]=(i,1,z['closes'])
assert len(lookup)==20
roots=[f for f in solutions if all(f[f[v]]==r[v] for v in range(30))];f,g=roots;assert all(g[f[v]]==v for v in range(30));step=lambda p:tuple(f[v] for v in reversed(p))
phase=lambda p:entry.index(p[1])^exit.index(p[-2]);seen=set()
for p in lookup:
    if p in seen:continue
    cycle=[p]
    for _ in range(3):cycle.append(step(cycle[-1]))
    assert step(cycle[-1])==p and cycle[2]==swap(p) and len(set(cycle))==4;assert [phase(q) for q in cycle]==[phase(p),1-phase(p)]*2
    assert len({lookup[q][2] for q in cycle})==1;seen.update(cycle);print('cycle (strip, row copy)',[lookup[q][:2] for q in cycle],'ports',[(q[1],q[-2]) for q in cycle],'closes',lookup[p][2]);
assert seen==lookup.keys()
