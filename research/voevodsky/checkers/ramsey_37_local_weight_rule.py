"""Construct a normalized cover from disjointness degrees, then repair deficits by simultaneous equal splits and trim excess. Rational final checker. No stored LP weights used."""
import json,itertools,numpy as np
from fractions import Fraction as F
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_37_edge_average.json').read_text())['remaining'];out=[]
for r in R:
 a=r['core'];Q=[sum(1<<i for i in t) for t in itertools.combinations(range(16),5) if all(not(a[i]>>j&1) for i,j in itertools.combinations(t,2))];B=np.array([[int(not(s&q)) for q in Q] for s in Q]);deg=B.sum(axis=1);assert min(deg)>0
 # Feasible local cover: each target bids 1/degree to every neighbor; use maximum received bid. Compress by re-splitting each target's unit proportionally to its present neighboring weights.
 w=np.ones(len(Q));history=[];done=False
 for it in range(101):
  load=B@w;w=w*np.max(B/load[:,None],axis=0);history.append(float(sum(w)))
  if sum(w)<5.99999:
   u=np.ceil(w*10**8).astype('int64');assert min(B@u)>=10**8 and sum(u)<6*10**8;done=True;break
 direct=done
 if True:
  # Multiplicative weights for normalized max-min coverage. Pay the least covered targets more; pick a best support column each round. Use integral counts as the actual certificate.
  counts=np.zeros(len(Q),dtype=int);cover=np.zeros(len(Q),dtype=int)
  for j in range(1,10001):
   price=np.exp(-0.1*(cover-cover.min()));scores=B@price;best=int(scores.argmax());counts[best]+=1;cover+=B[:,best]
   if 6*min(cover)>j:break
  if 6*min(cover)>j:u=counts;den=int(min(cover));done=True
  else:den=1;u=counts
 assert (B@u).min()==den and 6*den>sum(u)
 out.append(dict(local=direct,local_bound=history[-1],rounds=j,success=bool(done),numerators=u.tolist(),denominator=den));
print('local',sum(r['local'] for r in out),'all',sum(r['success'] for r in out),'max rounds',max(r['rounds'] for r in out),'worst verified bound',max(F(sum(r['numerators']),r['denominator']) for r in out if r['success']));(P/'ramsey_37_local_weight_rule.json').write_text(json.dumps(out)+'\n')
