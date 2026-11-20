"""Classify the twelve assignments under all eight port-square symmetries, allowing boundary frames to move. Compare invariant alternating cycle lengths and residual symmetry."""
from collections import Counter
from ramsey_strip_common_core_residual_graph import solutions
from ramsey_strip_maxcore_symmetry import G,image
from ramsey_strip_matching_restart import turn
pool={image(m,g) for m in solutions for g in G};unseen=set(pool);hist=Counter();records=[]
while unseen:
    m=min(unseen,key=lambda m:sorted(m));orb={image(m,g) for g in G};unseen-=orb
    adj={}
    for x,y in m^turn(m):adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    todo=set(adj);sizes=[]
    while todo:
        stack=[min(todo)];part=set()
        while stack:
            x=stack.pop()
            if x in part:continue
            part.add(x);stack.extend(adj[x]-part)
        todo-=part;sizes.append(len(part))
    sizes=tuple(sorted(sizes));record=(sizes,len(orb),len(orb&solutions));hist[record]+=1;records.append(record)
print('total moving-frame assignments',len(pool),'unframed orbits',len(records));print('(cycle sizes, orbit size, representatives at literal boundary): orbit count',dict(sorted(hist.items())));assert sum(k[2]*n for k,n in hist.items())==12
