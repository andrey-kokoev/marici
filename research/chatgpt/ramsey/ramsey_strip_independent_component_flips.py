"""Test irreducibility of the matching transition. Independent cycle flips give valid intermediate witnesses, but need not be the prescribed row-swapped endpoint."""
from itertools import product
from collections import Counter
from ramsey_common_frame_components import allms,frame,turn
stats=Counter()
for m in allms:
 if not {(0,16),(7,29)}<=m or frame[m]!=frame[turn(m)]:continue
 d=m^turn(m);adj={}
 for x,y in d:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
 todo=set(adj);cycles=[]
 while todo:
  stack=[min(todo)];S=set()
  while stack:
   x=stack.pop()
   if x in S:continue
   S.add(x);stack.extend(adj[x]-S)
  todo-=S;cycles.append(frozenset(e for e in d if e[0] in S))
 states=[]
 for bits in product((0,1),repeat=len(cycles)):
  n=m
  for c,b in zip(cycles,bits):
   if b:n=n^c
  assert n in allms and frame[n]==frame[m];states.append(n)
  assert n^turn(n)==d
 keep=sum({(0,16),(7,29)}<=n for n in states);stats[len(cycles),len(states),keep]+=1
print('(independent cycle flips, intermediate states, states preserving boundary): starting matchings',dict(stats))
