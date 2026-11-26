"""Batch entailment from 34 alone, no score preprocessing. A single guarded disjunction asks for any failed low demand. Used selectors are blocked by the new positive demand itself. Compare against baseline on identical cores."""
import json,itertools,time,statistics
from pysat.solvers import Solver
from ramsey_retention_slice import D,has
P=D.parent;rows=[z for z in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if (z['n'],z['d'])==(10,5)];out=[]
for z in rows:
 a=z['core'];Q=[q for q in range(1,1024) if not has(a,q,2)];low=[q for q in Q if q.bit_count()<3];v=lambda j,i:1+10*j+i;T=time.perf_counter();base=[[-v(j,i),-v(j,h)] for j in range(5) for i,h in itertools.combinations(range(10),2) if a[i]>>h&1];cla={q:[[v(j,i) for i in range(10) if q>>i&1 for j in js] for js in itertools.combinations(range(5),6-q.bit_count())] for q in Q};hi=base+sum((cla[q] for q in Q if q not in low),[]);build=time.perf_counter()-T
 T=time.perf_counter()
 with Solver(name='g4',bootstrap_with=hi+sum((cla[q] for q in low),[])) as sl:assert sl.solve()==z['full']
 baseline=time.perf_counter()-T;T=time.perf_counter();keep=[];calls=0;guard=51+len(low)
 with Solver(name='g4',bootstrap_with=hi) as sl:
  start_ok=sl.solve();calls+=1
  if start_ok:
   for j,q in enumerate(low):
    for lit in cla[q][0]:sl.add_clause([-(51+j),-lit])
   sl.add_clause([-guard]+list(range(51,guard)))
   while True:
    calls+=1
    if not sl.solve(assumptions=[guard]):break
    pos=set(sl.get_model());ss=[sum(1<<i for i in range(10) if v(j,i) in pos) for j in range(5)];failed=[q for q in low if sum(bool(s&q) for s in ss)<q.bit_count()];assert failed and not set(keep)&set(failed);keep.extend(failed)
    for q in failed:
     for c in cla[q]:sl.add_clause(c)
   calls+=1;assert sl.solve(assumptions=[-guard])==z['full']
  else:assert not z['full']
 out.append(dict(kept=keep,total=len(low),calls=calls,full=z['full'],shared_build=build,batch=time.perf_counter()-T,baseline=baseline))
print('times shared/batch/full',*[sum(r[k] for r in out) for k in ('shared_build','batch','baseline')]);print('calls',sum(r['calls'] for r in out),'kept',sum(len(r['kept']) for r in out if r['full']),'of',sum(r['total'] for r in out if r['full']));(P/'ramsey_batch_reduction.json').write_text(json.dumps(out)+'\n')
