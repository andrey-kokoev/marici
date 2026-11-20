"""Inspect same-generator family changes as alternating matching switches. Also determine the full graph of single-cycle moves among the eight C5-invariant matchings."""
from collections import Counter
from itertools import combinations
from ramsey_strip_cyclic_matching_eight_states import signatures,hub,P,G,action,moved

def components(A,B):
 adj={}
 for x,y in A^B:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
 todo=set(adj);parts=[]
 while todo:
  stack=[min(todo)];S=set()
  while stack:
   x=stack.pop()
   if x in S:continue
   S.add(x);stack.extend(adj[x]-S)
  todo-=S;parts.append(S)
 return parts
for a in range(1,5):
 A=signatures[a,];B=signatures[tuple(sorted((a,3*a%5)))];parts=components(A,B);shared=A&B
 print('generator',a,'common flags',len(shared),'alternating component lengths',sorted(map(len,parts)),'shared selected-pair hub counts',Counter(hub in P[i] for i,j in shared))
 assert all(moved(shared,action(p))==shared for p in G)
counts=Counter();degrees=Counter()
for a,b in combinations(signatures,2):
 sizes=tuple(sorted(map(len,components(signatures[a],signatures[b]))));counts[sizes]+=1
 if len(sizes)==1:degrees[a]+=1;degrees[b]+=1
print('all pair differences',dict(counts),'single-cycle neighbor degrees',dict(degrees))
