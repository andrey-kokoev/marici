"""Exploratory core-only demand screen. The two criteria were selected after inspecting the four known exceptions. Include all ties; evaluate on the complete order-11 census, not a blind sample."""
import json,itertools,collections
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;old=json.loads((P/'ramsey_test_coincidence.json').read_text())['rows'];parents=json.loads((P/'ramsey_core_capacity_36.json').read_text());rows=[]
for r in old:
 t=r['vertices'];a=parents[r['parent']]['core'];rows.append(([sum(1<<j for j,v in enumerate(t) if a[u]>>v&1) for u in t],not r['reject']['1234']))
rows += [(r['g'],r['1234'][0]) for r in json.loads((P/'ramsey_distill_unseen.json').read_text())['rows']];out=[]
for a,full in rows:
 Q=[q for q in range(1,2048) if all(not(q>>i&1 and q&v) for i,v in enumerate(a))];S=[s for s in Q if not any(s!=u and s&u==s for u in Q)];T=[q for q in Q if q.bit_count()==4];sel=[]
 for k in (1,2):
  scores={q:(sum(bool(s&q) for s in S),sum(t&q==q for t in T)) for q in Q if q.bit_count()==k};sel.extend(q for q,(h,f) in scores.items() if not any(i<=h and j<=f and (i,j)!=(h,f) for i,j in scores.values()))
 v=lambda j,i:1+11*j+i;cs=[[-v(j,i),-v(j,h)] for j in range(5) for i,h in itertools.combinations(range(11),2) if a[i]>>h&1];
 for q in Q:
  if q.bit_count()<3 and q not in sel:continue
  cs.extend([[v(j,i) for i in range(11) if q>>i&1 for j in js] for js in itertools.combinations(range(5),6-q.bit_count())]);
 with Solver(name='g4',bootstrap_with=cs) as sl:ok=sl.solve()
 assert ok or not full;out.append(dict(selected=sel,available=sum(q.bit_count()<3 for q in Q),pass_screen=ok,pass_full=full))
print(collections.Counter((r['pass_screen'],r['pass_full']) for r in out),sum(len(r['selected']) for r in out),sum(r['available'] for r in out));print([(i,len(out[16+i]['selected'])) for i in [7,8,14,17]]);(P/'ramsey_core_frontier.json').write_text(json.dumps(out,indent=1)+'\n')
