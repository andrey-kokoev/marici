"""Audit every rooted six-label transport, not a single arbitrary graph isomorphism, from the short-cycle alternatives to the fixed longest matching."""
from itertools import permutations
from collections import Counter
from ramsey_strip_short_long_root_transport import long,short,r,P,T,moved
from ramsey_strip_unbiased_three_constraints import selected,allms
I=tuple(range(30));comp=lambda a,b:tuple(a[x] for x in b)
def order(g):
 h=g;k=1
 while h!=I:h=comp(g,h);k+=1
 return k
hist=Counter();axes=set();source_counts=Counter()
for p in permutations(range(6)):
 tr=lambda d:tuple(sorted(p[x] for x in d));H=tuple([P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]);inv=tuple(H.index(i) for i in I)
 for n,(a,b) in enumerate(selected,1):
  for m in (allms[a],allms[b]):
   if moved(m,H)!=long:continue
   rp=comp(H,comp(r,inv));third=comp(r,comp(rp,r));hist[n,order(comp(r,rp)),len(long&moved(long,third))]+=1;axes.add(rp);source_counts[n]+=1
print('short-filling source, product order, shared links for third conjugate: transport counts',dict(sorted(hist.items())));print('source transport totals',dict(source_counts),'distinct transported row involutions',len(axes));print('distinct comparison axes by product order',dict(Counter(order(comp(r,a)) for a in axes)))
