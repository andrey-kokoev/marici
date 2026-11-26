"""LP upper bound for whole edit interval: use all (not only maximal) independent supports of size >=5 in lower, every immutable blue 5..7 in upper, degree budgets at vertices. A 34-vertex (3,9) has min degree >=6 since its non-neighbors form a (3,8) on at most 27. Any optimal panel member has at least five core neighbors. Certify exclusions by integer rounding and exhaustive pricing. Probe all 62 seeds first with one example per edge count for controls."""
import json,collections,sys
import numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_minimal.json').read_text());d=int(sys.argv[2]) if len(sys.argv)>2 else 7;path=P/f'ramsey_gain26_minimal_dual{d}.json';out=json.loads(path.read_text()) if path.exists() else [];done={z['idx'] for z in out}
for idx,r in enumerate(R):
 if idx in done:continue
 a=r['adj'];u=[v for v in a];I=[0]
 for i,v in enumerate(a):
  I.extend([s|1<<i for s in I if not s&v]);
  for j in range(i):
   if not v&a[j] and not v>>j&1:u[i]|=1<<j;u[j]|=1<<i
 S=np.array([s for s in I if s.bit_count()>=d-2]);Q=[q for q in I if q.bit_count()>=5 and all(not q>>i&1 or not q&v for i,v in enumerate(u))];B=np.array([(S&q)==0 for q in Q]+[(S>>i&1)>0 for i in range(26)],dtype=np.int32);caps=np.array([8-q.bit_count() for q in Q]+[8-v.bit_count() for v in a]);res=linprog(-np.ones(len(S)),A_ub=B,b_ub=caps,method='highs');assert res.success;y=np.maximum(0,np.rint(-1e6*res.ineqlin.marginals)).astype('int64');den=int(min(y@B));num=int(y@caps);z=dict(idx=idx,lp=-res.fun,num=num,den=den,excludes=bool(den and num<d*den));
 if z['excludes']:z['dual']=[[('miss',Q[j]) if j<len(Q) else ('degree',int(j)-len(Q)),int(y[j])] for j in np.nonzero(y)[0]]
 out.append(z);path.write_text(json.dumps(out)+'\n');
 if len(out)>=int(sys.argv[1]):break
print('tested',len(out),'excluded',sum(r['excludes'] for r in out),'range',min(r['lp'] for r in out),max(r['lp'] for r in out))
