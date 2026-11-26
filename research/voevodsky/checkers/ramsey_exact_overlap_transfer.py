"""Test remaining chords with exact Gram counts from core side and then both sides. Verify any surviving counterexample directly as two binary matrices."""
import json,itertools,collections
from pysat.card import CardEnc
from pysat.formula import IDPool
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_37_catalogue_free.json').read_text())['certificates'];prior=json.loads((P/'ramsey_attachment_rule_transfer.json').read_text());out=[]
for row in prior:
 if row['status']!='tested':continue
 old=[set(s) for s in row['red_supports']];a=R[row['core_index']]['core'];E=set(itertools.product(*row['mark']));missing=sorted(E-set(map(tuple,row['all'])));C=range(16);J=range(6);pool=IDPool();x={(i,j):pool.id((i,j)) for i in C for j in J};cs=[];rec=dict(core=row['core_index'],remaining=missing);out.append(rec)
 for i in C:cs+=CardEnc.equals([x[i,j] for j in J],len(old[i]),vpool=pool).clauses
 for j in J:cs+=CardEnc.equals([x[i,j] for i in C],5,vpool=pool).clauses
 base=cs.copy();base.extend([[-x[i,j],-x[h,j]] for i,h in itertools.combinations(C,2) if a[i]>>h&1 for j in J]);corecs=[]
 for stage,side,other in [('exact_core',C,J),('exact_neighbor',J,C),('exact_both',J,C)]:
  cs=(corecs if stage=='exact_both' else base).copy();missing=rec['remaining']
  def inds(i,j):return (i,j) if stage=='exact_core' else (j,i)
  for i,h in itertools.combinations(side,2):
   vs=[];k=0
   for j in other:
    u,v=inds(i,j),inds(h,j);l,r=x[u],x[v];y=pool.id();cs.extend([[-y,l],[-y,r],[y,-l,-r]]);vs.append(y);k+=u[1] in old[u[0]] and v[1] in old[v[0]]
   cs+=CardEnc.equals(vs,k,vpool=pool).clauses
  if stage=='exact_core':corecs=cs.copy()
  live=[]
  with Solver(name='g4',bootstrap_with=cs) as sl:
   for e in missing:
    if not sl.solve(assumptions=[x[e]]+[-x[f] for f in E-{e}]):continue
    pos=set(sl.get_model());new=[{j for j in J if x[i,j] in pos} for i in C];assert stage=='exact_neighbor' or all(len(old[i]&old[h])==len(new[i]&new[h]) for i in C for h in C);assert all(sum(j in s for s in new)==5 for j in J);assert all(not(new[i]&new[h]) for i,h in itertools.combinations(C,2) if a[i]>>h&1);assert {f for f in E if f[1] in new[f[0]]}=={e}
    if stage!='exact_core':assert all(sum({j,k}<=s for s in old)==sum({j,k}<=s for s in new) for j in J for k in J)
    live.append(e);rec.setdefault(stage+'_counterexample',dict(edge=e,before=[sorted(s) for s in old],after=[sorted(s) for s in new]))
  rec[stage]=live;missing=live
print([(k,sum(len(r[k]) for r in out),sum(bool(r[k]) for r in out)) for k in ('remaining','exact_core','exact_neighbor','exact_both')]);(P/'ramsey_exact_overlap_transfer.json').write_text(json.dumps(out)+'\n')
