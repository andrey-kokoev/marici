"""Look for a boundary cycle filled by marked triangles away from a crossing edge."""
from itertools import combinations,permutations
from unittest.mock import patch
from ramsey38_rotation_holdout import g
import ramsey38_root15_pair_obstructions as ob
p=g[19];rows={v:frozenset(n&p) for v,n in g.items() if v not in p|{19}};short={r for v,r in rows.items() if len(r)<4 and v!=7};tris=set.union(*(ob.sub(s,3) for s in rows.values()));edges=set.union(*(ob.sub(s,2) for s in rows.values()));edge_list=sorted(edges,key=sorted)
def mask(s):return sum(1<<edge_list.index(e) for e in s)
def span(tgt,avoid):
    base={};faces=sorted((f for f in tris if not f&avoid),key=sorted)
    for i,f in enumerate(faces):
        h=mask(ob.sub(f,2));w=1<<i
        while h and h.bit_length() in base:
            a,b=base[h.bit_length()];h^=a;w^=b
        if h:base[h.bit_length()]=(h,w)
    h=tgt;w=0
    while h and h.bit_length() in base:
        a,b=base[h.bit_length()];h^=a;w^=b
    if not h:return [sorted(f) for i,f in enumerate(faces) if w>>i&1]

def obstruction(R,E):
    for n in range(3,len(p)-1):
        for c in permutations(p,n):
            if c[0]!=min(c) or c[1]>c[-1]:continue
            rim={frozenset((v,c[i-1])) for i,v in enumerate(c)}
            if not rim<=E:continue
            sides=[set(),set()]
            for i,v in enumerate(c):
                ns=R[v];j=ns.index(c[i-1]);o=ns[j+1:]+ns[:j];k=o.index(c[(i+1)%n]);sides[0].update(set(o[:k])-set(c));sides[1].update(set(o[k+1:])-set(c))
            for a in sides[0]:
                for b in sides[1]:
                    for k in range(len(p)-n-1):
                        for mid in permutations(p-set(c)-{a,b},k):
                            path=(a,)+mid+(b,)
                            if all(frozenset(pair) in edges for pair in zip(path,path[1:])):
                                cert=span(mask(rim),set(path))
                                if cert:return c,path,cert
if __name__=='__main__':
    with patch.object(ob,'P',p):
        for R,E in ob.rotations(short):print(obstruction(R,E))
