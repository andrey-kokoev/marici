"""Construct the all-crossing residual matching using only distances from the active cycle. Check all residual completions, not just the three symmetry-selected pairs."""
from collections import deque,Counter
from ramsey_strip_accumulated_pair import ms
from ramsey_strip_forced_local_propagation import adj
from ramsey_strip_matching_restart import turn
active={v for e in ms[0]^ms[1] for v in e};dist={v:0 for v in active};Q=deque(active)
while Q:
 x=Q.popleft()
 for y in adj[x]-dist.keys():dist[y]=dist[x]+1;Q.append(y)
remaining=set(adj)-active;cross={v:{w for w in adj[v]&remaining if dist[v]!=dist[w]} for v in remaining};print('layer populations',Counter(dist[v] for v in remaining),'cross-degree histogram',Counter(map(len,cross.values())))
used=set();matching=set();rounds=[]
while remaining:
 options={v:cross[v]&remaining for v in remaining};forced={tuple(sorted((v,next(iter(ns))))) for v,ns in options.items() if len(ns)==1}
 if not forced:break
 assert len({v for e in forced for v in e})==2*len(forced);rounds.append(sorted(forced));matching|=forced;remaining-={v for e in forced for v in e}
assert not remaining and turn(matching)==matching
print('local forced rounds',rounds,'total matching links',len(matching))
# Every non-crossing matching would require explicitly admitting within-layer edges.
print('all-crossing completion forced without choosing a residual flag',True)
