"""23-vertex upper-bound replay conditional on stored (3,6) catalogues; no (3,7) endpoint used. Support columns for 6-regular case must have size five. Check all remaining catalogued cores."""
import gzip,json,itertools,collections
from pysat.solvers import Solver
from ramsey_retention_slice import D,CAT,decode,check,has
P=D.parent;A=[decode(s.strip()) for s in gzip.open(CAT.parent/'r36_16.g6.gz','rt')];B=[decode(s.strip()) for s in (CAT/'r36_17.g6').read_text().splitlines()];e=lambda g:sum(v.bit_count() for v in g)//2
assert all(check(g,2**len(g)-1,3,6) for g in A+B);print(len(A),min(map(e,A)),min(map(e,B)),flush=True);remaining=[g for g in A if e(g)==33];stats=collections.Counter();out=[]
for g in remaining:
 Q=[sum(1<<i for i in u) for k in range(1,6) for u in itertools.combinations(range(16),k) if all(not(g[i]>>j&1) for i,j in itertools.combinations(u,2))];S=[q for q in Q if q.bit_count()==5];# rejection via exact row margins and blue clique hitting inequalities
 from ortools.sat.python import cp_model
 m=cp_model.CpModel();x=[m.new_int_var(0,6,str(j)) for j in S];m.add(sum(x)==6)
 for i in range(16):m.add(sum(v for v,s in zip(x,S) if s>>i&1)==6-g[i].bit_count())
 for q in Q:m.add(sum(v for v,s in zip(x,S) if q&s)>=q.bit_count())
 sol=cp_model.CpSolver();sol.parameters.num_search_workers=1;st=sol.solve(m);assert st==cp_model.INFEASIBLE;stats['infeasible']+=1;out.append(dict(core=g,support_count=len(S)))
print(stats,flush=True)
# 22-vertex construction: 17-core and four blue neighbors of the root.
for a in B:
 n=17;v=lambda j,i:1+n*j+i;cs=[[-v(j,i),-v(j,h)] for j in range(4) for i,h in itertools.combinations(range(n),2) if a[i]>>h&1];
 for q in range(1,1<<n):
  k=q.bit_count()
  if not 3<=k<=5 or has(a,q,2):continue
  cs.extend([[v(j,i) for i in range(n) if q>>i&1 for j in J] for J in itertools.combinations(range(4),7-k)])
 with Solver(name='g4',bootstrap_with=cs) as sl:
  if not sl.solve():continue
  pos=set(sl.get_model());g=a.copy()+[0]*5
  for j in range(4):
   for i in list(range(n))+[21]:
    if i==21 or v(j,i) in pos:g[n+j]|=1<<i;g[i]|=1<<(n+j)
  assert check(g,2**22-1,3,7);break
else:raise ValueError('no lower witness')
(P/'ramsey_37_edge_average.json').write_text(json.dumps(dict(hist16=dict(collections.Counter(map(e,A))),hist17=dict(collections.Counter(map(e,B))),remaining=out,witness=g))+'\n')
