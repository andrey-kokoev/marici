"""Based holonomy from spanning-tree transport at row-fixed partition 29. Compare actual row swap on its eight opposite partitions, not an arbitrary cube reflection."""
from collections import deque,Counter
from itertools import combinations
from ramsey_strip_cube_holonomy import trans,compose,I,charts,bits,T,order
base=14;paths={base:[base]};Q=deque([base])
while Q:
 a=Q.popleft()
 for b in range(15):
  if (a,b) in trans and b not in paths:paths[b]=paths[a]+[b];Q.append(b)
def transport(path):
 h=I
 for a,b in zip(path,path[1:]):h=compose(trans[a,b],h)
 return h
inv=lambda h:tuple(h.index(i) for i in I)
gens=[]
for a,b in trans:
 h=compose(inv(transport(paths[b])),compose(trans[a,b],transport(paths[a])));gens.append(h)
G={I};todo=[I]
while todo:
 h=todo.pop()
 for g in gens:
  q=compose(g,h)
  if q not in G:G.add(q);todo.append(q)
X=list(combinations(range(4),2));p=(0,2,1,3);e=[X.index(tuple(sorted(p[i] for i in x))) for x in X];tr=lambda t:frozenset(tuple(sorted(e[i] for i in d)) for d in t);assert tr(T[base])==T[base]
R=list(I)
for j,b in charts[base].items():R[bits.index(b)]=bits.index(charts[base][T.index(tr(T[j]))])
R=tuple(R);roots=[g for g in G if compose(g,g)==R];print('based holonomy group size',len(G),'element orders',Counter(map(order,G)));print('actual row swap on cube',R,'fixed cube vertices',sum(R[i]==i for i in I),'in group',R in G,'square roots in group',len(roots));print('row swap square roots',roots)
