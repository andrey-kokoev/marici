"""Within a common cyclic frame, selected active flags share a C5 orbit iff they lie on the same alternating component. Prove by exhaustive check on quotient-generated states only."""
from itertools import combinations
from collections import Counter
from ramsey_row_quotient_constructor import frame_records,action,move,R
hist=Counter();tests=0
for G,H,matchings in frame_records:
 for m in matchings:
  mate=move(m,R);diff=m^mate;adj={}
  for x,y in diff:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
  components=[];todo=set(adj)
  while todo:
   stack=[min(todo)];part=set()
   while stack:
    v=stack.pop()
    if v in part:continue
    part.add(v);stack.extend(adj[v]-part)
   todo-=part;components.append(part)
  active=m-mate;orbits={e:frozenset().union(*(move({e},action(g)) for g in G)) for e in active}
  for a,b in combinations(active,2):
   samecomponent=any(a[0] in c and b[0] in c for c in components);assert samecomponent==(b in orbits[a]);tests+=1
  if {(0,16),(7,29)}<=m:hist[(7,29) in orbits[0,16],len(components)]+=1
print('active flag pairs checked',tests,'(boundary same orbit, number of components):',dict(hist))
