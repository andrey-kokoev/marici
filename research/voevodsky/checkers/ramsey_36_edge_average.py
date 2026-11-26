"""Recover the (3,6) maximum from (3,5) cores only. Uses known R(3,5)=14. Census inputs: exhaustive canonical-augmentation 12-cores and maximum 13-core catalogue. Exact fractional dual for last case; constructive lower bound."""
from itertools import combinations,combinations_with_replacement
from fractions import Fraction as F
from scipy.optimize import linprog
import json,numpy as np
from ramsey_retention_slice import D,CAT,decode,check
P=D.parent;R=[r['core'] for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==12 and r['d']==5];T=[decode(s) for s in (CAT/'r35_13.g6').read_text().splitlines()];edges=lambda a:sum(s.bit_count() for s in a)//2;assert len(R)==12 and min(map(edges,R))==20 and min(map(edges,T))==26;last=[a for a in R if edges(a)==20];assert len(last)==1;a=last[0];Q=[q for q in range(1,4096) if all(not(q>>i&1 and q&v) for i,v in enumerate(a))];S=[s for s in Q if not any(t!=s and t&s==s for t in Q)];A=np.array([[int(bool(q&s)) for s in S] for q in Q]);rhs=np.array([q.bit_count() for q in Q]);lp=linprog(np.ones(len(S)),A_ub=-A,b_ub=-rhs);y=[F(-float(x)).limit_denominator() for x in lp.ineqlin.marginals];lb=sum(w*int(b) for w,b in zip(y,rhs));assert all(w>=0 for w in y) and all(sum(y[i] for i in range(len(Q)) if A[i,j])<=1 for j in range(len(S)));print('last fractional bound',lb,flush=True)
# Check the 13-vertex minimum without assuming completeness of the separate 13-catalogue.
from ramsey_retention_slice import has
edge13={edges(h)+s.bit_count() for h in R for s in range(4096) if not has(h,s,2) and not has([~u for u in h],4095^s,4)};assert edge13=={26}
# A 5-regular endpoint further requires every support to have order four, and demands exact coverage per core vertex.
from pysat.solvers import Solver
from pysat.card import CardEnc
def grow(a,d):
 n=len(a);Q=[q for q in range(1,1<<n) if all(not(q>>i&1 and q&v) for i,v in enumerate(a))];cs=[[-(1+n*j+i),-(1+n*j+h)] for j in range(d) for i,h in combinations(range(n),2) if a[i]>>h&1];
 for q in Q:
  cs.extend([[1+n*j+i for j in J for i in range(n) if q>>i&1] for J in combinations(range(d),6-q.bit_count())]);
 with Solver(name='g4',bootstrap_with=cs) as s:
  if not s.solve():return None
  m=set(s.get_model());g=a.copy()+[0]*(d+1)
  for j in range(d):
   for i in list(range(n))+[n+d]:
    if i==n+d or 1+n*j+i in m:g[n+j]|=1<<i;g[i]|=1<<(n+j)
  assert check(g,(1<<len(g))-1,3,6);return g
assert lb>5 or grow(a,5) is None;w=next(w for h in R if (w:=grow(h,4)) is not None);print('constructed',len(w));(P/'ramsey_36_edge_average.json').write_text(json.dumps(dict(core12_edge_counts=sorted(map(edges,R)),core13_edge_counts=list(map(edges,T)),last=a,dual_bound=str(lb),weights={q:str(v) for q,v in zip(Q,y) if v},witness=w),indent=1)+'\n')
