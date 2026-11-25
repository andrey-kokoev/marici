"""Replay the final three-vertex demand contradiction of the degree-three search."""
import json
from collections import Counter
from pathlib import Path
from itertools import product
from ramsey310_matching_sides import F,sets
D=Path(__file__).resolve().parents[1]/'results'
A=json.loads((D/'ramsey310_matching_degree3_types.json').read_text())[0]
E=(13117600,33825944,34097697,34652242,4264289,29492304)
C=list(sets(A,F,7));need=[9-a.bit_count()-sum(s>>v&1 for s in E) for v,a in enumerate(A)]
single=sum(1<<v for v,x in enumerate(need) if x==1)
for x,y,z in product(*zip(E[:3],E[3:])):
    missed=single&~(x|y|z)
    C=[s for s in C if (s&missed).bit_count()<=1]
for k in (6,7):
    for t in sets(A,F,k):
        if 6-k+sum(bool(t&x and t&y) for x,y in zip(E[:3],E[3:]))==0:
            C=[s for s in C if s&t]
U=(11,22,25);m=sum(1<<v for v in U);supply=Counter((s&m).bit_count() for s in C)
assert len(C)==103 and max(supply)==1 and [need[v] for v in U]==[2,2,3]
print('eligible rows',len(C),'intersection counts',dict(supply),'required 7, upper bound 6')
