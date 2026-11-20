"""Recover the ten-cycle from prescribed ordered row gates by shortest-path search in the cage. No stored strip, closure labels, or completed matching input."""
from itertools import combinations
from collections import deque
X=list(combinations(range(4),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];N=[set() for _ in range(30)]
for i,p in enumerate(P):
 for j,t in enumerate(T,15):
  if p in t:N[i].add(j);N[j].add(i)
perm=(0,2,1,3);e=[X.index(tuple(sorted(perm[v] for v in x))) for x in X];tr=lambda p:tuple(sorted(e[i] for i in p));r=[P.index(tr(p)) for p in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
for a in (16,17):
 for b in (4,7):
    dist={a:0};Q=deque([a])
    while Q:
        v=Q.popleft()
        for w in N[v]-dist.keys():dist[w]=dist[v]+1;Q.append(w)
    def shortest(v):
        if v==a:yield [a];return
        for w in N[v]:
            if dist[w]==dist[v]-1:
                for p in shortest(w):yield p+[v]
    middle,=list(shortest(b));assert len(middle)==4
    p=[0]+middle+[29];assert len(set(p+[r[v] for v in p]))==10;cycle=p+[r[v] for v in p[-2:0:-1]];assert len(cycle)==len(set(cycle))==10
    assert all(y in N[x] for x,y in zip(cycle,cycle[1:]+cycle[:1]))
    print('gates',a,b,'unique shortest half',p)
