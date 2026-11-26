"""Exact entailment, including nonmaximal supports. Keep size 3,4 and frozen frontier. Try omitting low demands in mask order. An omission is sound only if a violating assignment is UNSAT. Recheck equivalence and irredundancy of reinstatements is NOT claimed."""
import itertools,json,collections,time
from pysat.solvers import Solver
from ramsey_retention_slice import D,has
P=D.parent;rows=[r for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if (r['n'],r['d'])==(10,5)];out=[];start=time.perf_counter()
for r in rows:
 a=r['core'];n=len(a);Q=[q for q in range(1,1<<n) if not has(a,q,2)];S=[q for q in Q if not any(s!=q and s&q==q for s in Q)];T=[q for q in Q if q.bit_count()==4];low=[q for q in Q if q.bit_count()<3];sc={q:(sum(bool(q&s) for s in S),sum(q&t==q for t in T)) for q in low};front=[q for q in low if not any(t.bit_count()==q.bit_count() and sc[t]!=sc[q] and all(i<=j for i,j in zip(sc[t],sc[q])) for t in low)];v=lambda j,i:1+n*j+i;base=[[-v(j,i),-v(j,h)] for j in range(5) for i,h in itertools.combinations(range(n),2) if a[i]>>h&1];
 def add(s,q):
  for J in itertools.combinations(range(5),6-q.bit_count()):s.add_clause([v(j,i) for j in J for i in range(n) if q>>i&1])
 rec=dict(front=len(front),total=len(low),restored=[],omitted=[],front_sat=r['frontier'],full_sat=r['full']);out.append(rec)
 with Solver(name='g4',bootstrap_with=base) as s:
  for q in Q:
   if q in front or q.bit_count()>2:add(s,q)
  assert s.solve()==r['frontier']
  for q in sorted(set(low)-set(front)):
   # Any violating assignment can permute its missing neighbors into these slots.
   assumptions=[-v(j,i) for j in range(6-q.bit_count()) for i in range(n) if q>>i&1]
   if s.solve(assumptions=assumptions):
    rec['restored'].append(q);add(s,q)
   else:rec['omitted'].append(q)
  assert s.solve()==r['full']
print('elapsed',time.perf_counter()-start)
for key,group in itertools.groupby(sorted(out,key=lambda r:(r['front_sat'],r['full_sat'])),key=lambda r:(r['front_sat'],r['full_sat'])):
 z=list(group);print(key,len(z),sum(r['total'] for r in z),sum(r['front'] for r in z),sum(len(r['restored']) for r in z),sum(len(r['omitted']) for r in z));
 if key==(True,False):print(z[0]['restored'])
(P/'ramsey_sound_demand_reduction.json').write_text(json.dumps(out)+'\n')
