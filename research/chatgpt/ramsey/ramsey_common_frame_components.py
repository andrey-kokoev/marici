"""Classify the active components for every matching sharing a cyclic frame with its literal row-swapped partner, without prescribing poles or lengths."""
from collections import Counter
from ramsey_strip_intrinsic_fivefold_transport import groups,action,moved,I
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_matching_restart import turn
GS=list(groups);gen=[action(next(p for p in G if p!=I)) for G in GS];frame={}
for m in allms:
 hits=[k for k,g in enumerate(gen) if moved(m,g)==m];assert len(hits)==1;frame[m]=hits[0]
hist=Counter();out=[]
for m in allms:
 n=turn(m)
 if frame[m]!=frame[n]:continue
 adj={}
 for x,y in m^n:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
 todo=set(adj);sizes=[]
 while todo:
  stack=[min(todo)];S=set()
  while stack:
   x=stack.pop()
   if x in S:continue
   S.add(x);stack.extend(adj[x]-S)
  todo-=S;sizes.append(len(S))
 hist[tuple(sorted(sizes)),len(m&n)]+=1;out.append(m)
print('common-frame ordered matchings',len(out),'of',len(allms),'(active cycles, shared flags): counts',dict(hist));print('common cyclic groups',len({frame[m] for m in out}))
