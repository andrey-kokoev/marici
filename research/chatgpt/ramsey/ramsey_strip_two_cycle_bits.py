"""Factor the four completions of a maximal retained core into two alternating-cycle bits and measure quarter-turn action."""
from itertools import product
from ramsey_strip_rotation_retained_core import best,cores,image,f,allms
from ramsey_strip_matching_restart import turn
for k,m in enumerate(best,1):
    core=cores[m];d=m^turn(m);adj={}
    for x,y in d:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    todo=set(adj);parts=[]
    while todo:
        stack=[min(todo)];vertices=set()
        while stack:
            x=stack.pop()
            if x in vertices:continue
            vertices.add(x);stack.extend(adj[x]-vertices)
        todo-=vertices;parts.append(frozenset(e for e in d if e[0] in vertices))
    assert len(parts)==2 and all(len(p)==10 for p in parts)
    opts=[(p&m,p&turn(m)) for p in parts];states={bits:core|opts[0][bits[0]]|opts[1][bits[1]] for bits in product((0,1),repeat=2)};reverse={v:b for b,v in states.items()}
    assert set(states.values())=={n for n in allms if core<=n}
    perm=[parts.index(image(p,f)) for p in parts];assert perm==[1,0]
    moves={bits:reverse[image(n,f)] for bits,n in states.items()};assert all(reverse[turn(n)]==tuple(1-x for x in b) for b,n in states.items())
    print('core',k,'quarter-turn exchanges components',perm,'bit action',moves)
