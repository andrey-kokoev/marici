"""Test two extra structures absent from the bare G-set count: reversal and overlapping-pair updates on transitions staying in the depth-three layer. If state s=(a,b) goes to t=(b,c), its right endpoint must equal t's left. Test forced identifications, not a chosen bijection."""
from collections import defaultdict,Counter
from itertools import product
from functools import reduce
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';a=json.loads((D/'ramsey_triangle_transport_memory.json').read_text())['full'];T=a['transition'];run=lambda w:reduce(lambda s,m:T[s][m],w,a['initial']);lower={run(w) for k in range(3) for w in product(range(8),repeat=k)};H=defaultdict(list)
for w in product(range(8),repeat=3):
    s=run(w)
    if s not in lower:H[s].append(w)
r={s:{run(w[::-1]) for w in ws} for s,ws in H.items()};assert all(len(rs)==1 for rs in r.values());r={s:next(iter(rs)) for s,rs in r.items()};assert all(r[r[s]]==s for s in H)
parent={}
def root(x):
    parent.setdefault(x,x)
    if parent[x]!=x:parent[x]=root(parent[x])
    return parent[x]
edges=0
for s in H:
    for t in T[s]:
        if t in H:parent[root(('R',s))]=root(('L',t));edges+=1
comp=defaultdict(lambda:{'L':[],'R':[]})
for side in 'LR':
    for s in H:comp[root((side,s))][side].append(s)
maxR=max(len(c['R']) for c in comp.values());maxL=max(len(c['L']) for c in comp.values());largest=max(comp.values(),key=lambda c:max(map(len,c.values())));capacity=3+8-1
out=dict(states=len(H),representative_counts=Counter(map(len,H.values())),history_reversal_fixed=sum(s==t for s,t in r.items()),pair_reversal_fixed=24,within_layer_transition_occurrences=edges,max_forced_left=maxL,max_forced_right=maxR,endpoint_capacity=capacity,largest_component=largest);print({k:v for k,v in out.items() if k!='largest_component'});(D/'ramsey_triangle_240_dynamics.json').write_text(json.dumps(out,indent=2)+'\n')
