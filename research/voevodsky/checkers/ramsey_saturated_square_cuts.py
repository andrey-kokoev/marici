"""Compare exact hitting numbers for blue (k-1)-cliques from saturated alternating squares and for all such cliques. Use precisely the deletion-test representatives."""
from ramsey_retention_slice import D,decode
from itertools import combinations
from pysat.card import CardEnc
from pysat.solvers import Solver
import json
P=D.parent;out=[]
def hit(cs,n):
 clauses=[[i+1 for i in range(n) if m>>i&1] for m in cs]
 for d in range(n+1):
  with Solver(name='g4',bootstrap_with=clauses+CardEnc.atmost(list(range(1,n+1)),d).clauses) as s:
   if s.solve():
    cut=[i-1 for i in s.get_model() if 1<=i<=n];assert len(cut)==d and all(any(m>>i&1 for i in cut) for m in cs);return cut
for r in json.loads(D.read_text()):
 if r['l']!=3:continue
 k=r['k'];g=decode(r['graph6']);n=len(g);sat=set();wedges=0
 for x in range(n):
  for a in range(n):
   if not(g[x]>>a&1):continue
   for b in range(n):
    if b==x or g[x]>>b&1:continue
    c=g[b]&~g[a]&~((1<<a)|(1<<b)|(1<<x))
    if c.bit_count()==k-2:sat.add(c|(1<<a));wedges+=1
 def cl(p,q):
  if q.bit_count()==k-1:yield q;return
  while p.bit_count()>=k-1-q.bit_count():
   b=p&-p;p^=b;yield from cl(p&~g[b.bit_length()-1],q|b)
 allq=set(cl((1<<n)-1,0));assert sat<=allq;other=allq-sat;cuts=[hit(q,n) for q in (sat,other,allq)];out.append(dict(k=k,saturated_wedges=wedges,distinct_saturated=len(sat),total=len(allq),cuts=cuts));print(k,wedges,len(sat),len(allq),list(map(len,cuts)),flush=True)
(P/'ramsey_saturated_square_cuts.json').write_text(json.dumps(out,indent=1)+'\n')
