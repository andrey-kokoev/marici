"""Compare maximal rotation cores under every element of the eight-element endpoint/row group, and its stabilizer of the literal directed matching boundary."""
from ramsey_strip_rotation_retained_core import best,cores,image,f
from ramsey_strip_ordered_boundary_dualities import solutions
from ramsey_strip_boundary_binary_search import initial
from ramsey_strip_matching_restart import turn
I=tuple(range(30));G={I};todo=[I]
while todo:
    g=todo.pop()
    for h in solutions:
        q=tuple(h[g[i]] for i in range(30))
        if q not in G:G.add(q);todo.append(q)
a,b=best;stab=[g for g in G if image(initial,g)==initial];print('boundary stabilizer size',len(stab),'candidate exchange maps in stabilizer',sum(image(a,g)==b for g in stab),'in all eight',sum(image(a,g)==b for g in G));print('core A',sorted(cores[a]),'core B',sorted(cores[b]))
for i,m in enumerate(best,1):
    diff=m^turn(m);adj={}
    for x,y in diff:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    unseen=set(adj);lengths=[]
    while unseen:
        stack=[min(unseen)];component=set()
        while stack:
            x=stack.pop()
            if x in component:continue
            component.add(x);stack.extend(adj[x]-component)
        unseen-=component;lengths.append(len(component))
    print('candidate',i,'alternating cycle lengths',sorted(lengths),'distinct links before/after one quarter-turn', [len({tuple(sorted((g[x],g[y]))) for g in [I,tuple(f[i] for i in I)]}) for x,y in sorted(cores[m])])
