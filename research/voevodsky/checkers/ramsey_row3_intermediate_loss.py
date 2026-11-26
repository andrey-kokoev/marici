"""Measure the best induced intermediate for each stored representative of a maximum endpoint. A deletion set must hit every blue (k-1)-clique. Certify attainability and test next smaller cut unless excluded by the known order."""
from ramsey_retention_slice import D,decode,check
from pysat.card import CardEnc
from pysat.solvers import Solver
import json
M={3:5,4:8,5:13,6:17,7:22,8:27,9:35};out=[]
for r in json.loads(D.read_text()):
 if r['l']!=3:continue
 k=r['k'];g=decode(r['graph6']);n=len(g);P=(1<<n)-1
 def cl(p,q):
  if len(q)==k-1:yield q;return
  while p.bit_count()>=k-1-len(q):
   b=p&-p;p^=b;i=b.bit_length()-1;yield from cl(p&~g[i],q+[i+1])
 clauses=list(cl(P,[]));delta=n-M[k-1]
 for d in range(delta,n):
  with Solver(name='g4',bootstrap_with=clauses+CardEnc.atmost(list(range(1,n+1)),d).clauses) as s:
   if not s.solve():continue
   cut=[i-1 for i in s.get_model() if 1<=i<=n];assert len(cut)==d and check(g,P^sum(1<<i for i in cut),3,k-1);break
 out.append(dict(k=k,n=n,gain=delta,min_cut=d,loss=d-delta,excess_over_half=delta-(k+1)//2,blue_cliques=len(clauses),cut=cut));print(k,delta,d,d-delta,flush=True)
(D.parent/'ramsey_row3_intermediate_loss.json').write_text(json.dumps(out,indent=1)+'\n')
