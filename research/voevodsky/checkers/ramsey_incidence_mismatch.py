"""Exact L1 degree mismatch under unrestricted triangle-free red completion and every blue demand on <=4 newcomer labels. Use unary totalizer per vertex, soft threshold clauses charge exactly absolute degree error. Bound each optimum also by SAT at one fewer with the same threshold encoding. No endpoint as input."""
import itertools,json,collections
from pysat.solvers import Solver
from pysat.card import ITotalizer,CardEnc,EncType
from ramsey_incidence_first35 import P

def base(m,order=4):
 edges={(i,j):k+1 for k,(i,j) in enumerate(itertools.combinations(range(26),2)) if not m[i]&m[j]};cs=[[-edges[i,j],-edges[i,k],-edges[j,k]] for i,j,k in itertools.combinations(range(26),3) if (i,j) in edges and (i,k) in edges and (j,k) in edges];small=set()
 for t in range(256):
  if t.bit_count()>order:continue
  for q in itertools.combinations([i for i,s in enumerate(m) if not s&~t],t.bit_count()+1):small.add(tuple(edges[e] for e in itertools.combinations(q,2) if e in edges))
 return edges,cs+list(map(list,small))
def measure(m):
 E,cs=base(m);top=max(E.values());err=[]
 for i,s in enumerate(m):
  xs=[v for e,v in E.items() if i in e];d=8-s.bit_count();
  # ITotalizer thresholds suffice in forward direction. Count deficits as excesses of the negated literals, not as missing positive thresholds.
  for lits,k in ((xs,d),([-x for x in xs],len(xs)-d)):
   assert k>=0
   with ITotalizer(lits=lits,ubound=len(xs),top_id=top) as it:
    cs.extend(it.cnf.clauses);top=it.top_id;err.extend(it.rhs[k:])
 with ITotalizer(lits=err,ubound=20,top_id=top) as it, Solver(name='cadical195',bootstrap_with=cs) as sl:
  sl.append_formula(it.cnf.clauses)
  for k in range(0,20,2): # total signed mismatch even, and abs has same parity
   if sl.solve(assumptions=[-it.rhs[k]]):
    model=set(sl.get_model());red=[e for e,v in E.items() if v in model];delta=[sum(i in e for e in red)-(8-s.bit_count()) for i,s in enumerate(m)];assert sum(map(abs,delta))==k;return dict(l1=k,delta=delta,edges=red)
 raise ValueError('outside search bound')
if __name__=='__main__':
 R=json.loads((P/'ramsey_incidence_orient35.json').read_text());out=[]
 for z in json.loads((P/'ramsey_incidence_pockets.json').read_text()):
  if not z['triangle_plus_all_sat']:continue
  m=R[z['skeleton']]['surv'][z['j']]['m'];a=measure(m);out.append(dict(m=m,skeleton=z['skeleton'],j=z['j'],**a));print(z['skeleton'],z['j'],a['l1'],flush=True)
 (P/'ramsey_incidence_mismatch.json').write_text(json.dumps(out)+'\n')
