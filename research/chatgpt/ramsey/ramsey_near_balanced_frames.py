"""Census nearest balanced roots and canonical six-point trace multisets."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import json
from ramsey_hall_center_conjecture import decode

D=Path(__file__).parent
maps=[[sum(1<<p[i] for i in range(6) if m>>i&1) for m in range(64)] for p in permutations(range(6))]
frames={};results=[]
for row in json.loads((D/'ramsey_hall_center_conjecture.json').read_text())['regular']:
    A=decode(row['graph6'].encode());roots=[]
    for r in range(22):
        points=[i for i in range(22) if A[r]>>i&1];assert len(points)==6
        T=[sum(1<<j for j,u in enumerate(points) if A[v]>>u&1) for v in range(22) if v!=r and v not in points]
        sizes=sorted(t.bit_count() for t in T);distance=sum(abs(k-2) for k in sizes)
        roots.append((r,T,sizes,distance))
    d=min(x[-1] for x in roots);selected=[]
    for r,T,sizes,dist in roots:
        if dist!=d:continue
        key=min(tuple(sorted(p[t] for t in T)) for p in maps);idx=frames.setdefault(key,len(frames));selected.append({'root':r,'sizes':sizes,'frame':idx})
    results.append({'source':row['record'],'profile_counts':dict(Counter(str(x[2]) for x in roots)),'distance':d,'nearest':selected});print(row['record'],d,Counter(x['frame'] for x in selected))
(D/'ramsey_near_balanced_frames.json').write_text(json.dumps({'frame_masks':list(frames),'records':results},indent=2)+'\n')
