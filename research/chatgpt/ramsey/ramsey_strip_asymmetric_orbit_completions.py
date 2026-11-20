"""Hold the asymmetric orbit, not an arbitrarily chosen family bit. Count all Hall completions, C5-preserving completions, and possible new cyclic frames."""
from collections import Counter
from ramsey_strip_cyclic_matching_eight_states import signatures,P,T,hub,c
from ramsey_strip_intrinsic_fivefold_transport import groups,action,moved
from ramsey_strip_minimal_shared_constraints import allms
for a in range(1,5):
 m=signatures[a,];obs=set()
 for d,j in m:
  x,y=P[d]
  if hub in (x,y):continue
  block,=[p for p in T[j-15] if hub in p];z,=set(block)-{hub}
  if (c[x]+c[y]-2*c[z])%5:obs.add((d,j))
 assert len(obs)==5
 cyclic=[key for key,M in signatures.items() if obs<=M];allhits=[M for M in allms if obs<=M];framecounts=Counter()
 for M in allhits:
  k=sum(all(moved(M,action(g))==M for g in G) for G in groups);framecounts[k]+=1
 print('retained arrow step',a,'same-frame completions',sorted(cyclic),'all perfect completions',len(allhits),'number of C5 frames per completion',dict(framecounts))
 assert set(cyclic)=={(a,),tuple(sorted((a,2*a%5))),tuple(sorted((a,3*a%5)))}
