"""Maximum possible common induced order on the (3,7) side before specifying a (4,6) partner. Compute minimum transversal of its blue six-cliques."""
import json,collections
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_retention_slice import CAT,D,decode,check
out=[]
for line in (CAT/'r37_22.g6').read_text().splitlines():
 a=decode(line.strip());n=len(a);p=(1<<n)-1;assert n==22 and check(a,p,3,7)
 def six(v,q):
  if len(q)==6:yield q;return
  while v.bit_count()>=6-len(q):
   b=v&-v;v^=b;i=b.bit_length()-1;yield from six(v&~a[i],q+[i+1])
 cs=list(six(p,[]));
 for k in range(5,23): # R(3,6)=18; at least five deletions necessary
  with Solver(name='g4',bootstrap_with=cs+CardEnc.atmost(list(range(1,n+1)),k).clauses) as s:
   if s.solve():
    removed=[i-1 for i in s.get_model() if 1<=i<=n];q=p^sum(1<<i for i in removed);assert len(removed)==k and check(a,q,3,6);out.append(dict(row=len(out)+1,removed=removed,blue_sixes=len(cs),overlap=n-k));break
print(collections.Counter(r['overlap'] for r in out));(D.parent/'ramsey_sum10_outer_overlap.json').write_text(json.dumps(out,indent=1)+'\n')
