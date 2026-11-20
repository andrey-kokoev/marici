"""Compare completed literal-seed strips at 10 and 12 interior visits, without treating a pre-exit prefix as a completed strip. Check if the two spare folded positions can be inserted on a square, preserving every other folded visit, endpoint and switch in order. Test actual witness orbit separately."""
from ramsey_strip_witness_orbits import orbits,edges,r,fill
from ramsey_strip_prism_proof import labels,rep,V,E
from pathlib import Path
import json
from collections import Counter
records=json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text());groups={10:[],12:[]}
for z in records:
 p=z['path'];w=tuple(labels[rep(x)] for x in p[1:-1]);
 if (p[0],p[-1])!=(0,29) or len(w) not in groups:continue
 idx=len(groups[len(w)])+1;types=set();c=p+[r[x] for x in p[-2:0:-1]]
 for extra in fill(set(range(30))-set(c)):
    for parity in (0,1):
        m=extra|{edges(c[i],c[(i+1)%len(c)]) for i in range(parity,len(c),2)};u=frozenset((i,j-15) for i,j in m);types.add(orbits[u])
 assert bool(types)==z['closes'];groups[len(w)].append((idx,w,types))
for i,w,t in groups[12]:
 hits=[]
 for j,v,u in groups[10]:
    for a in range(1,10):
        if w[:a]+w[a+2:]==v:
            arc=w[a-1:a+3];assert tuple(sorted(arc[1:3])) in E and set(arc[1:3])==V-set(v) and tuple(sorted((arc[0],arc[3]))) in E;hits.append((j,arc,u))
 print('12-visit path',i,'witness orbit',t,'shortcuts -> 10-visit strips',hits);assert len(hits)==1 and t==hits[0][2]=={1}
