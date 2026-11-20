"""Audit seed-mark preservation under every rooted short-to-long transport. Output root 0 is not the same object as Hall pole 0. Keep these distinct."""
from itertools import permutations,combinations
from collections import Counter
from ramsey_strip_short_long_all_transports import long,r,P,T,moved,selected,allms,comp,order,I
X=list(combinations(range(4),2));tet={tuple(X.index(tuple(sorted(q[i] for i in e))) for e in X) for q in permutations(range(4))};hist={name:Counter() for name in ('output root only','Hall poles','directed entry','directed exit','both directed flags','tetrahedral columns','stationary edge labels')}
for p in permutations(range(6)):
 tr=lambda d:tuple(sorted(p[x] for x in d));H=tuple([P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]);inv=tuple(H.index(i) for i in I);period=order(comp(r,comp(H,comp(r,inv))))
 flags={'output root only':True,'Hall poles':H[0]==0 and H[29]==29,'directed entry':H[0]==0 and H[16]==16,'directed exit':H[29]==29 and H[7]==7,'both directed flags':all(H[i]==i for i in (0,16,7,29)),'tetrahedral columns':p in tet,'stationary edge labels':p[2]==2 and p[3]==3}
 for n,pair in enumerate(selected,1):
  for j in pair:
   if moved(allms[j],H)!=long:continue
   for name,ok in flags.items():
    if ok:hist[name][n,period]+=1
for name,h in hist.items():print(name,sum(h.values()),dict(sorted(h.items())))
