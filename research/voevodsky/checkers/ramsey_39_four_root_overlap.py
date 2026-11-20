"""Classify the 35-circle crossover by common plus-neighbor counts, independently of cyclic order. Check necessity and sufficiency against direct core sizes."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';E=json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges'];V=set(range(35));N=[set() for _ in V]
for a,b in E:N[a].add(b);N[b].add(a)
def core(q):return V-set(q)-set.union(*(N[i] for i in q))
def sig(q):return Counter(len(N[a]&N[b]) for a,b in combinations(q,2))
tr=Counter();qu=Counter();samples={};conf=Counter()
for q in combinations(range(35),3):
    if any(b in N[a] for a,b in combinations(q,2)):continue
    c=core(q);ov=sorted(sig(q).elements());z=len(set.intersection(*(N[i] for i in q)));assert len(c)==8+sum(ov)-z
    if len(c)==16:
        ports=[v for v in sorted(c) if len(N[v]&c)==2];tr[str((tuple(ov),z,len(ports)))]+=1;assert ports
for q in combinations(range(35),4):
    if any(b in N[a] for a,b in combinations(q,2)):continue
    high=[e for e in combinations(q,2) if len(set.intersection(*(N[i] for i in e)))==4];degrees=sorted(sum(i in e for e in high) for i in q);shape='C4' if degrees==[2,2,2,2] else 'P4' if degrees==[1,1,2,2] else 'other';pred=shape!='other' and set(sig(q))=={2,4};truth=len(core(q))==13;conf[str((pred,truth))]+=1
    if truth:
        qu[shape]+=1;samples.setdefault(shape,dict(roots=q,high_edges=high));assert all(len(core(t))==16 for t in combinations(q,3))
out=dict(triple_profile=tr,successful_shapes=qu,examples=samples,pair_only_confusion=conf);print(out);(D/'ramsey_39_four_root_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
