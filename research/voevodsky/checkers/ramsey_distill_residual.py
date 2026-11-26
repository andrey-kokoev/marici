"""Minimum extra individual demands on top of all 34 constraints. Enumerate maximal-support multisets and use exact DP over <=18 surviving multisets."""
import json,itertools,collections
import numpy as np
from ramsey_retention_slice import D
P=D.parent;rows=json.loads((P/'ramsey_distill_unseen.json').read_text())['rows'];out=[]
for i,r in enumerate(rows):
 if not(r['34'][0] and not r['1234'][0]):continue
 a=r['g'];Q=[q for q in range(1,2048) if not any(q>>j&1 and q&v for j,v in enumerate(a))];S=[q for q in Q if not any(s!=q and s&q==q for s in Q)];M=np.array(list(itertools.combinations_with_replacement(S,5)));M=M[np.logical_and.reduce([((M&q)!=0).sum(axis=1)>=q.bit_count() for q in Q if q.bit_count()>=3])];F=(1<<len(M))-1;kill={q:sum(1<<j for j,x in enumerate(((M&q)!=0).sum(axis=1)) if x<q.bit_count()) for q in Q if q.bit_count()<=2};record={}
 for mode in ['1','2','12']:
  dp={0:[]};keys=[q for q,k in kill.items() if k and str(q.bit_count()) in mode];
  for q in keys:
   for bits,sel in list(dp.items()):
    b=bits|kill[q];
    if b not in dp or len(dp[b])>len(sel)+1:dp[b]=sel+[q]
  best=dp.get(F);record[mode]=dict(survivors=len(M)-max(dp,key=int.bit_count).bit_count(),minimum=None if best is None else len(best),example=best,universal=[q for q in keys if kill[q]==F]);
 out.append(dict(row=i,partial=len(M),tests=record));print(i,len(M),record)
(P/'ramsey_distill_residual.json').write_text(json.dumps(out,indent=1)+'\n')
