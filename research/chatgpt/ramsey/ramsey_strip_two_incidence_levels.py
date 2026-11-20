"""Distinguish nonbacktracking at an exit duad in the Hall cage from nonbacktracking in the ground-label membership subgraph. Check literal strip arrivals from both rows."""
import json
from pathlib import Path
from itertools import combinations
X=list(combinations(range(1,5),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6]
rows=json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text());seen=set()
for z in rows:
 p=z['path'];
 if (p[0],p[-1])!=(0,29):continue
 a,d,b=p[-3:];u,v=P[d];before,after=T[a-15],T[b-15];assert set(before)&set(after)=={(u,v)}
 flip=lambda x:v if x==u else u if x==v else x
 def transform(t):return tuple(sorted(tuple(sorted(map(flip,k))) for k in t))
 assert transform(before)==before and transform(after)==after
 seen.add((a,d,b))
print('all literal final flags:',sorted(seen));assert {d for _,d,_ in seen}=={4,7}
