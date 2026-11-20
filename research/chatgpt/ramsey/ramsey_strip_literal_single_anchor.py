"""Use literal tetrahedral labels as proposed identity anchors, rather than an arbitrary target label. Compare role-preserving one-label constraints, without selecting a desired product order."""
from itertools import combinations
from ramsey_strip_fivefold_phase_anchor import transport_records,P,T
from ramsey_strip_short_long_all_transports import r,comp,order,I
X=list(combinations(range(1,5),2))
for x,label in enumerate(X):
 hits=[]
 for n,o,p in transport_records:
  if p[x]!=x:continue
  tr=lambda d:tuple(sorted(p[i] for i in d));H=tuple([P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]);inv=tuple(H.index(i) for i in I);period=order(comp(r,comp(H,comp(r,inv))));hits.append((n,o,period))
 print('fixed edge',label,'(filling, orientation, comparison product order)',sorted(hits))
