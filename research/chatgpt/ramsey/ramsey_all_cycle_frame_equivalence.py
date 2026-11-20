"""Test frame compatibility versus cross-layer completion on every ten-cycle and every type-preserving reflection through opposite vertices. No literal poles or rows selected."""
from collections import Counter,deque
from ramsey_all_ten_cycle_layers import cycles,N
from ramsey_strip_intrinsic_fivefold_transport import groups,action,moved,I
from ramsey_strip_minimal_shared_constraints import allms
GS=list(groups);gen=[action(next(p for p in G if p!=I)) for G in GS];frame={}
for m in allms:
 hits=[k for k,g in enumerate(gen) if moved(m,g)==m];assert len(hits)==1;frame[m]=hits[0]
stats=Counter();config=Counter()
for C in cycles:
 S=set(C);M=[next(iter(N[x]-S)) for x in C];D=[next(iter(N[x]-S-set(M))) for x in M];active={tuple(sorted((x,y))) for x,y in zip(C,C[1:]+C[:1])};chosen={tuple(sorted((C[i],C[(i+1)%10]))) for i in range(0,10,2)};candidates=[m for m in allms if chosen<=m];cross={tuple(sorted((x,y))) for x,y in zip(M,D)}
 for k in range(5):
  r={L[i]:L[(2*k-i)%10] for L in (C,M,D) for i in range(10)};hits=[]
  for m in candidates:
   mate=moved(m,r)
   if m^mate!=active:continue
   same=frame[m]==frame[mate];allcross=m-active==cross;stats[same,allcross]+=1;hits.append((same,allcross));assert same==allcross
  config[len(hits),sum(same for same,_ in hits)]+=1
print('all configurations (row-invariant fillings, same-frame fillings)',dict(config));print('(same cyclic frame, cross-layer filling)',dict(stats));assert sum(config.values())==360
