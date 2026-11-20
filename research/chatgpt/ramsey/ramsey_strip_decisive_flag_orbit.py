"""Classify the five decisive flags intrinsically via the unique C5 action: star versus finite duad, and whether the hub's partner is the finite midpoint modulo five."""
from collections import Counter
from ramsey_strip_intrinsic_fivefold_transport import records,long,action,moved,P,T,I
for n,o,m,G,candidates,correct in records:
 hub,=[x for x in I if all(p[x]==x for p in G)];g=min(p for p in G if p!=I);cycle=[min(set(I)-{hub})]
 for _ in range(4):cycle.append(g[cycle[-1]])
 coord={x:i for i,x in enumerate(cycle)};hist=Counter();decisive=set()
 for e in m:
    d,j=e;pair=P[d];kind='hub in selected pair'
    if hub not in pair:
        block,=[p for p in T[j-15] if hub in p];z,=set(block)-{hub};x,y=pair;kind='hub partner is midpoint' if (coord[x]+coord[y]-2*coord[z])%5==0 else 'hub partner not midpoint'
    count=sum(moved({e},action(p))<=long for p in candidates);hist[kind,count]+=1
    if count==1:decisive.add(e)
 assert len(decisive)==5 and all(moved(decisive,action(p))==decisive for p in G)
 print('source',n,o,'flag classes and surviving transports',dict(hist))
