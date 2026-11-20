"""Verify rooted independent-Hall characterization on all regular catalogue records; report nearest-to-uniform roots without assuming distinct signatures."""
from pathlib import Path
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode

def independent_sets(A,mask,chosen=()):
 yield chosen
 while mask:
  bit=mask&-mask;mask^=bit;i=bit.bit_length()-1
  yield from independent_sets(A,mask&~A[i],chosen+(i,))

source=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());out=[];tested=0
for record in source['regular']:
 A=decode(record['graph6'].encode());profiles=[]
 for v in range(22):
  U=A[v];W=((1<<22)-1)^U^(1<<v);vertices=[i for i in range(22) if W>>i&1];S={i:A[i]&U for i in vertices}
  assert sum(s.bit_count() for s in S.values())==30
  tight=Counter()
  for J in independent_sets(A,W):
   union=0
   for i in J:union|=S[i]
   assert len(J)<=5 and union.bit_count()>=len(J);tested+=1
   if union.bit_count()==len(J):tight[len(J)]+=1
  profiles.append({'root':v,'size_histogram':dict(sorted(Counter(s.bit_count() for s in S.values()).items())),'squared_deviation':sum((s.bit_count()-2)**2 for s in S.values()),'distinct_signatures':len(set(S.values())),'tight_independent_sets':dict(tight)})
 best=min(p['squared_deviation'] for p in profiles);r={'record':record['record'],'minimum_squared_deviation':best,'minimizing_roots':[p for p in profiles if p['squared_deviation']==best]};out.append(r);print('record',record['record'],'minimum deviation',best,'best profiles',[(p['root'],p['size_histogram'],p['distinct_signatures']) for p in r['minimizing_roots']])
Path(__file__).with_suffix('.json').write_text(json.dumps({'independent_sets_checked':tested,'records':out},indent=2)+'\n');print('independent sets checked',tested)
