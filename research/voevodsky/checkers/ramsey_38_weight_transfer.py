"""At order 28, a degree-seven root has a 20-vertex core. Test the previous missed-clique inequality on the stored 44-edge stratum only. Optimize using all maximal supports; replay exact rational upper and lower certificates."""
import itertools,json
import numpy as np
from fractions import Fraction as F
from scipy.optimize import linprog
from ramsey_retention_slice import CAT,D,check
out=[]
for s in (CAT.parent/'ramsey_37_20_44_cores.txt').read_text().split():
 m=int(s,16);a=[0]*20
 for j in range(20):
  for i in range(j):
   if m>>(j*(j-1)//2+i)&1:a[j]|=1<<i;a[i]|=1<<j
 assert check(a,2**20-1,3,7) and m.bit_count()==44;I=[0]
 for j,v in enumerate(a):I += [q|1<<j for q in I if not q&v]
 S=[q for q in I if not any(q!=t and q&t==q for t in I)];Q=[q for q in I if q.bit_count()==6];B=np.array([[int(not q&t) for t in S] for q in Q]);res=linprog(-np.ones(len(S)),A_ub=B,b_ub=np.ones(len(Q)));assert res.success
 x=[F(int(w),10**7) for w in np.floor(np.maximum(res.x,0)*10**7)];y=[F(int(w),10**7) for w in np.ceil(np.maximum(-res.ineqlin.marginals,0)*10**7)];scale=max(F(1),max(sum(v for v,b in zip(x,row) if b) for row in B));x=[v/scale for v in x];scale=min(sum(v for v,b in zip(y,col) if b) for col in B.T);y=[v/scale for v in y];assert min(x+y)>=0 and all(sum(v for v,b in zip(x,row) if b)<=1 for row in B) and all(sum(v for v,b in zip(y,col) if b)>=1 for col in B.T);out.append(dict(core=s,bound=str(sum(y)),lower=str(sum(x)),weights={q:str(v) for q,v in zip(Q,y) if v},support_masses={q:str(v) for q,v in zip(S,x) if v}));print(out[-1]['bound'],flush=True)
(D.parent/'ramsey_38_weight_transfer.json').write_text(json.dumps(out)+'\n')
