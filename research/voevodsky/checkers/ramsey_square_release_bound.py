"""Search for a small exact weighted obstruction already at the largest blue cliques. Reweight the dual objective for sparsity; only integer replay determines an exclusion."""
import numpy as np,itertools,json
from scipy.optimize import linprog
from ramsey_retention_slice import D,decode
P=D.parent;out=[]
for r in json.loads((P/'ramsey_square_release_rows.json').read_text()):
 a=decode(r['graph']);k=r['k'];n=len(a);I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count()==k-1];B=np.array([[int(not q&s) for s in S] for q in Q]);lp=linprog(np.ones(len(Q)),A_ub=-B.T,b_ub=-np.ones(len(S)));assert lp.success;y=np.maximum(0,np.rint(lp.x*1e7)).astype('int64');den=int(min(B.T@y));num=int(sum(y));assert den>0;cost=np.ones(len(Q));records=[]
 if num<5*den:
  for j in range(6):
   sl=linprog(cost,A_ub=np.vstack([-B.T,np.ones(len(Q))]),b_ub=[-1]*len(S)+[4.999]);
   if not sl.success:break
   v=np.maximum(0,np.rint(sl.x*1e7)).astype('int64');d=int(min(B.T@v));m=int(sum(v));
   if d>0 and m<5*d:records.append((int(np.count_nonzero(v)),d,m,v))
   cost=1/(1e-5+sl.x)
 if records:
  _,d,m,v=min(records,key=lambda x:x[0]);sparse=dict(den=d,num=m,weights={q:int(w) for q,w in zip(Q,v) if w})
 else:sparse=None
 print(k,len(Q),len(S),num/den,None if not sparse else len(sparse['weights']));out.append(dict(k=k,graph=r['graph'],max_cliques=len(Q),max_supports=len(S),num=num,den=den,weights={q:int(w) for q,w in zip(Q,y) if w},sparse=sparse))
(P/'ramsey_square_release_bound.json').write_text(json.dumps(out)+'\n')
