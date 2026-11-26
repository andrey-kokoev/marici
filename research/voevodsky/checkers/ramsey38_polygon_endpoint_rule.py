"""Array-only boundary proposal: triangulate its marked embedding, optionally add a polygon center.
Does not call a tetrahedron completion solver. Only handles simple facial cycles in a connected graph.
"""
from itertools import combinations,product,permutations
from functools import lru_cache
from collections import Counter
from unittest.mock import patch
import ramsey38_root15_pair_obstructions as ob
from ramsey38_rotation_holdout import g

@lru_cache(None)
def triang(c):
    if len(c)<3:return (frozenset(),)
    return tuple(frozenset({frozenset((c[0],c[k],c[-1]))})|a|b for k in range(1,len(c)-1) for a in triang(c[:k+1]) for b in triang(c[k:]))

def center(c,x):
    for n in range(3,len(c)+1):
        for I in combinations(range(len(c)),n):
            gaps=[];fan=[]
            for i,j in zip(I,I[1:]+I[:1]):
                fan.append(frozenset((x,c[i],c[j])));gaps.append(triang((c+c)[i:(j if j>i else j+len(c))+1]))
            for parts in product(*gaps):yield frozenset(fan).union(*parts)

def walks(R):
    fs=[];seen=set()
    for a in R:
        for b in R[a]:
            if (a,b) in seen:continue
            c=[];i,j=a,b
            while (i,j) not in seen:
                seen.add((i,j));c.append(i);n=R[j];i,j=j,n[(n.index(i)+1)%len(n)]
            assert len(c)==len(set(c));fs.append(tuple(c))
    return fs

def shells(R,short,x):
    cs=walks(R)
    for target in ([None] if x is None else [i for i,c in enumerate(cs) if frozenset(c) not in short]):
        opts=[center(c,x) if i==target else triang(c) for i,c in enumerate(cs)]
        for parts in product(*opts):
            bd=frozenset.union(*parts);V=set.union(set(),*bd)
            if len(bd)!=2*len(V)-4 or len(bd)!=sum(map(len,parts)):continue
            if set(Counter(e for t in bd for e in ob.sub(t,2)).values())!={2}:continue
            # Glued polygons of a sphere; duplicate edges inside distinct polygons would have incidence four.
            if not all(any(s<=f for f in bd) for s in short):continue
            yield bd

def rim_ok(bd,tet):
    # For each fixed boundary edge, its two opposite boundary vertices must
    # be the ends of a path that contains all mandatory tetrahedral segments.
    for e in set.union(set(),*(ob.sub(t,2) for t in bd)):
        segments=[t-e for t in tet if e<=t];ends=sorted(set.union(set(),*(t-e for t in bd if e<=t)))
        tips=set.union(set(ends),*segments);u,v=ends
        if not any(all(abs(order.index(a)-order.index(b))==1 for a,b in segments) for mid in permutations(tips-{u,v}) for order in [(u,)+mid+(v,)]):return False
    return True

def predict(graph,root,drop,x=28):
    p=graph[root];rows={v:frozenset(p&n) for v,n in graph.items() if v not in p|{root}};short={r for v,r in rows.items() if v!=drop and len(r)<4};tet={r for r in rows.values() if len(r)==4};kw=dict(P=p,tri=set.union(*(ob.sub(r,3) for r in rows.values())),all_edges=set.union(*(ob.sub(r,2) for r in rows.values())),tet=tet);counts=Counter();out={None:set(),x:set()}
    with patch.multiple(ob,**kw):
        for R,E in ob.rotations(short):
            counts['orders']+=1
            if ob.cut_test(R,E) or ob.fan_test(R,E):continue
            counts['orders_pass']+=1
            for aux in out:
                for bd in shells(R,short,aux):
                    if rim_ok(bd,tet):out[aux].add(bd)
    return counts,out
def compatible(bd,required):
    from ramsey38_root15_link_rotation import link_domains,canon
    cells=required|{t|{0} for t in bd};P=set.union(set(),*cells);D={}
    for v in sorted(P-{0}):
        faces=frozenset(t-{v} for t in cells if v in t);D[v]=link_domains(faces)
        if not D[v]:return False
    # At the outside cone point the boundary is already a triangulated
    # sphere; the rotation is fixed up to reversing every order together.
    def oriented(f):return [(f[i-1],f[i]) for i in range(3)]
    fs=list(bd);order=[tuple(sorted(fs.pop()))];edges=set(oriented(order[0]))
    while fs:
        for i,t in enumerate(fs):
            a=tuple(sorted(t));e=oriented(a)
            if edges.intersection(e):a=a[::-1]
            elif not any((v,u) in edges for u,v in e):continue
            edges.update(oriented(a));order.append(a);fs.pop(i);break
        else:raise ValueError('disconnected boundary')
    R={}
    for v in P-{0}:
        nxt={a[(i+1)%3]:a[(i+2)%3] for a in order for i,w in enumerate(a) if w==v};c=[min(nxt)]
        while nxt[c[-1]]!=c[0]:c.append(nxt[c[-1]])
        assert len(c)==len(nxt);R[v]=tuple(c)
    D[0]=[R]
    def solve(d):
        if not d:return True
        v=min(d,key=lambda w:len(d[w]))
        return any(solve({w:[s for s in opts if w not in r or s[v]==canon(r[w][::-1])] for w,opts in d.items() if w!=v}) for r in d[v])
    return solve(D)

if __name__=='__main__':
    for root,drop in [(7,8),(19,7)]:
        c,out=predict(g,root,drop);print(root,drop,c,'original/aux shells:',len(out[None]),len(out[28]));
        req={frozenset(n&g[root]) for v,n in g.items() if v not in g[root]|{root}}
        accepted=[bd for bd in out[28] if compatible(bd,req)];print('consistent link orders:',len(accepted));
        for bd in accepted:print('aux links',sorted(sorted(t-{28}) for t in bd if 28 in t))
        if root==19:
            # Independent constructive check, AFTER making the boundary proposals.
            from ramsey38_support_ball_completion import shelling
            from ramsey38_compare_support_fillings import boundary
            cells=list(map(frozenset,[(6,8,11,16),(8,11,16,25),(8,11,20,25),(6,8,11,28),(6,8,16,28),(6,11,16,25),(6,11,20,25),(6,11,20,28),(6,16,20,28),(6,16,20,22),(6,20,22,25)]));a=boundary(cells);flip=frozenset((8,16,25,28));
            assert {t for t in a if t<=flip}=={frozenset((8,16,25)),frozenset((8,16,28))} and not any({25,28}<=t for t in cells)
            cells.append(flip);b=boundary(cells);assert set(accepted)=={a,b} and shelling(frozenset(cells)) and all(any(r<=t for t in cells) for r in req)
            assert {v for v,n in g.items() if v not in g[root]|{root} and len(n&g[root])<4 and not any((n&g[root])<=f for f in b)}=={drop}
            print('both proposed boundaries certified; added tetrahedron:', sorted(flip))
