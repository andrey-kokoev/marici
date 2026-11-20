"""Separate actual boundary data from common-frame, pole-connection and single-active-component requirements. Every counted matching is already a valid witness by the general theorem."""
from collections import Counter
from ramsey_common_frame_components import allms,frame,turn
H=Counter();examples={}
for m in allms:
 if not {(0,16),(7,29)}<=m:continue
 adj={}
 for x,y in m^turn(m):adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
 todo=set(adj);parts=[]
 while todo:
  stack=[min(todo)];S=set()
  while stack:
   x=stack.pop()
   if x in S:continue
   S.add(x);stack.extend(adj[x]-S)
  todo-=S;parts.append(S)
 same=frame[m]==frame[turn(m)];one=len(parts)==1;joined=any({0,29}<=S for S in parts);H[same,one,joined]+=1;examples.setdefault((same,one),tuple(sorted(map(len,parts))))
print('(common frame, single component, poles joined): counts',dict(sorted(H.items())));print('examples by common-frame/single-component',examples)
assert sum(H.values())==36 and sum(n for (same,one,joined),n in H.items() if same and one)==1
