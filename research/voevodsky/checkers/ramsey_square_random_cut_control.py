"""Fixed-size uniform sample control: compare to 315 distinct saturated cliques. Exact minimum via binary search; full-family optimum 9 supplies an upper bound."""
import random,json,collections
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_retention_slice import D,decode
P=D.parent;rows=json.loads(D.read_text());a=decode(next(r['graph6'] for r in rows if (r['l'],r['k'])==(3,9)));ref=next(r for r in json.loads((P/'ramsey_saturated_square_cuts.json').read_text()) if r['k']==9);n=len(a);N=100;seed=390315;rng=random.Random(seed)
def cl(p,q):
 if len(q)==8:yield q;return
 while p.bit_count()>=8-len(q):
  b=p&-p;p^=b;yield from cl(p&~a[b.bit_length()-1],q+[b.bit_length()])
C=list(cl((1<<n)-1,[]));assert len(C)==ref['total']==3360;K=ref['distinct_saturated'];assert K==315
ub=ref['cuts'][2];assert len(ub)==9 and all(any(i-1 in ub for i in q) for q in C);enc={k:CardEnc.atmost(list(range(1,n+1)),k).clauses for k in range(1,9)};mins=[]
for _ in range(N):
 cs=rng.sample(C,K);lo,hi=0,9
 while hi-lo>1:
  k=(lo+hi)//2
  with Solver(name='g4',bootstrap_with=cs+enc[k]) as s:
   if s.solve():hi=k
   else:lo=k
 mins.append(hi)
print(collections.Counter(mins));(P/'ramsey_square_random_cut_control.json').write_text(json.dumps(dict(seed=seed,n_samples=N,cliques_per_sample=K,population=len(C),minima=mins),indent=1)+'\n')
