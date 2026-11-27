"""Endpoint-local interval domains; propagate compatibility, never branch on a mesh."""
from itertools import combinations
from functools import lru_cache

@lru_cache(maxsize=256)
def geometry(B):
    cells=sorted(B,key=sorted);carrier={}
    for i,t in enumerate(cells):
        for k in (2,3,4):
            for f in combinations(t,k):
                s=frozenset(f);carrier[s]=carrier.get(s,0)|(1<<i)
    edges={s:m for s,m in carrier.items() if len(s)==2};domain={}
    for e,m in edges.items():
        ids=[i for i in range(len(cells)) if m>>i&1];adj={i:[j for j in ids if len(cells[i]&cells[j])==3] for i in ids};start=min(ids,key=lambda i:len(adj[i]));order=[start]
        while len(order)<len(ids):order.append(next(j for j in adj[order[-1]] if j not in order))
        cycle=all(len(adj[i])==2 for i in ids);d={0};n=len(ids)
        for i in range(n):
            z=0
            for j in range(n if cycle else n-i):z|=1<<order[(i+j)%n];d.add(z)
        domain[e]=(d,cycle)
    return carrier,edges,domain

@lru_cache(maxsize=256)
def vertex_links(B):
    cells=sorted(B,key=sorted);out={}
    for v in set().union(*cells):
        triangles={1<<i:t-{v} for i,t in enumerate(cells) if v in t};star=sum(triangles);disk=set();sphere=set();z=star
        while z:
            tris=[t for bit,t in triangles.items() if bit&z];edges={frozenset(e) for t in tris for e in combinations(t,2)};vertices=set().union(*tris)
            rim={e for e in edges if sum(e<=t for t in tris)==1};chi=len(vertices)-len(edges)+len(tris)
            # Connected vertex fans within these triangles are already required by
            # the edge domains. Additionally require a connected triangle surface,
            # a single simple boundary cycle (or empty boundary), and disk/sphere Euler count.
            if chi==(1 if rim else 2):
                seen={tris[0]};queue=list(seen)
                while queue:
                    t=queue.pop();fresh={f for f in tris if f not in seen and len(f&t)==2};seen.update(fresh);queue.extend(fresh)
                if len(seen)==len(tris):
                    if not rim:sphere.add(z)
                    else:
                        vs=set().union(*rim);adj={w:set().union(*(e for e in rim if w in e))-{w} for w in vs}
                        if all(len(neighbors)==2 for neighbors in adj.values()):
                            visited={next(iter(vs))};queue=list(visited)
                            while queue:
                                fresh=adj[queue.pop()]-visited;visited.update(fresh);queue.extend(fresh)
                            if visited==vs:disk.add(z)
            z=(z-1)&star
        out[frozenset([v])]=(star,disk,sphere)
    return out

def reject(B,buried,exposed,required,vertices=False):
    c,edges,domains=geometry(B);edges=edges.copy();forced=0
    for t in required|buried:
        if t not in c:return 'missing support'
        forced|=c[t]
    D={}
    for e,m in edges.items():
        source,cycle=domains[e];sel=forced&m;d={z for z in source if z&sel==sel}
        if e in buried and not cycle:return 'open buried star'
        if e in exposed:d={z for z in d if z and (not cycle or z!=m)}
        for s in buried|exposed:
            if len(s)==3 and e<=s:
                h=c.get(s,0);need=2 if s in buried else 1;d={z for z in d if (z&h).bit_count()==need}
        if not d:return 'empty local interval domain'
        D[e]=d
    while True:
        changed=False
        for e,d in D.items():
            for f,q in D.items():
                overlap=edges[e]&edges[f]
                if e==f or not overlap:continue
                possible={z&overlap for z in q};new={z for z in d if z&overlap in possible}
                if not new:return 'incompatible interval domains'
                if new!=d:D[e]=d=new;changed=True
        if not changed:
            if not vertices:return None
            vertices=False
            for v,(star,disk,sphere) in vertex_links(B).items():
                edges[v]=star;values=disk if v in exposed else disk|sphere|{0};sel=forced&star
                D[v]={z for z in values if z&sel==sel}
                if not D[v]:return 'empty vertex domain'
