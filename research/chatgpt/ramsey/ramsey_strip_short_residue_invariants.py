"""Intrinsic residual descriptors relative to the active alternating cycle; no coordinate order or entry-port orientation. Count residual edge distance layers and cycles in residual unions with quarter-turn images."""
from collections import Counter,deque
from ramsey_strip_unbiased_three_constraints import selected,allms,ms
from ramsey_strip_forced_local_propagation import adj
from ramsey_strip_rotating_boundary import f,image
from ramsey_strip_matching_restart import turn
for a,b in selected:
    m,n=allms[a],allms[b];shared=m&n;active={v for e in m^n for v in e};dist={v:0 for v in active};Q=deque(active)
    while Q:
        x=Q.popleft()
        for y in adj[x]-dist.keys():dist[y]=dist[x]+1;Q.append(y)
    layers=Counter(tuple(sorted((dist[x],dist[y]))) for x,y in shared)
    d=shared^image(shared,f);N={}
    for x,y in d:N.setdefault(x,set()).add(y);N.setdefault(y,set()).add(x)
    todo=set(N);components=[]
    while todo:
        stack=[min(todo)];part=set()
        while stack:
            x=stack.pop()
            if x in part:continue
            part.add(x);stack.extend(N[x]-part)
        todo-=part;components.append((len(part),sum(len(N[x]) for x in part)//2,tuple(sorted(Counter(len(N[x]) for x in part).items()))))
    print('accumulated target',set(ms)=={m,n},'distance layers',dict(layers),'quarter-turn residual difference components',sorted(components))
