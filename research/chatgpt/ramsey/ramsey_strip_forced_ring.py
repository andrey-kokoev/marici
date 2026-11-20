"""For every unmatchable representative, exhibit the optional-link graph. For its ring case, contract forced paths and count their lengths per resulting circuit."""
from ramsey_strip_secant_reduction import bad,N,M
from collections import Counter
for A,B,m,w in bad:
 if m:continue
 G={**{i:{15+j for j in N[i]-B} for i in set(range(15))-A},**{15+j:M[j]-A for j in set(range(15))-B}};H={x for x in G if len(G[x])==3};O={x:G[x]&H for x in H}
 def comps(g):
    todo=set(g);out=[]
    while todo:
        v=todo.pop();c={v};q=[v]
        for v in q:
            new=g[v]&todo;todo-=new;c|=new;q.extend(new)
        out.append(c)
    return out
 if len(comps(O))!=1:
    assert sorted((len(c),sorted(len(O[v]) for v in c).count(1)) for c in comps(O))==[(5,2),(7,2)];print(w,'two odd paths, orders 5 and 7');continue
 assert all(len(n)==2 for n in O.values());ring=[min(O)]
 while nexts:=O[ring[-1]]-set(ring):ring.append(min(nexts))
 F={v:{u for u in ns if len(ns)==2 or len(G[u])==2} for v,ns in G.items()};parts=comps(F);print('ring positions and forced path orders:',sorted((sorted(ring.index(v) for v in c if v in H),len(c)) for c in parts));
 for shift in (0,1):
    K={v:n.copy() for v,n in F.items()}
    for i in range(shift,12,2):
        u,v=ring[i],ring[(i+1)%12];K[u].add(v);K[v].add(u)
    order=sorted(sorted(len(p) for p in parts if p<=c) for c in comps(K));assert order==[[4,4],[3,3,4,4]] or sorted(map(sum,order))==[8,14];print('path orders on each circuit:',order)
