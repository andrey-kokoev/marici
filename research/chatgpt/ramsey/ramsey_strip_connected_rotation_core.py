"""Reimpose actual alternating connectivity of poles 0,29, beyond the two matching boundary flags. Classify component types and maximal rotation cores."""
from collections import Counter
from ramsey_strip_rotation_retained_core import leaves,cores,target,image,f
from ramsey_strip_matching_restart import turn
hist=Counter();connected=[]
for m in leaves:
    d=m^turn(m);adj={}
    for x,y in d:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    todo=set(adj);parts=[]
    while todo:
        stack=[min(todo)];part=set()
        while stack:
            v=stack.pop()
            if v in part:continue
            part.add(v);stack.extend(adj[v]-part)
        todo-=part;parts.append(part)
    yes=any({0,29}<=p for p in parts);hist[yes,tuple(sorted(map(len,parts))),len(cores[m])]+=1
    if yes:connected.append(m)
print('connected, cycle sizes, retained-core size: count',dict(sorted(hist.items())))
mx=max(len(cores[m]) for m in connected);winners=[m for m in connected if len(cores[m])==mx];print('connected',len(connected),'maximum core',mx,'winners',len(winners),'target included',target in winners,'distinct best cores',[sorted(c) for c in set(cores[m] for m in winners)])
