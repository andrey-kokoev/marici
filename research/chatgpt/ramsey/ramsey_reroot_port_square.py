"""Minimal (3,3) failure of descent for the complete fixed-root port language.
Roles 0=root, 1=new root, 2,3=old ports; 4=fresh. Verify minimality in the
same-core, same-role, blue-related-root model, with identical labelled border.
"""
from itertools import combinations

def ok(n,E):return all(0<sum(e in E for e in combinations(t,2))<3 for t in combinations(range(n),3))
def extend(n,E,S):return E|{(v,n) for v in S}
def states(n):
    pairs=list(combinations(range(n),2))
    for m in range(1<<len(pairs)):
        E={e for j,e in enumerate(pairs) if m>>j&1}
        if (0,1) not in E and ok(n,E):yield E

def subsets(H):return [set(s) for j in range(len(H)+1) for s in combinations(H,j)]
def key(n,E):
    P={i for i in range(1,n) if (0,i) in E};H=set(range(1,n))-P
    def lang(n,E,p):
        if p==2:return frozenset()
        return frozenset((tuple(sorted(T)),lang(n+1,B,p+1)) for T in subsets(H) if ok(n+1,B:=extend(n,E,T|{0})))
    return (tuple(sorted(P)),frozenset(e for e in E if set(e)<=H),lang(n,E,len(P)))
if __name__=='__main__':
    for n in range(2,5):
        bad=0
        for A,B in combinations(states(n),2):
            if key(n,A)!=key(n,B):continue
            for S in subsets(range(n)):
                if 1 not in S or 0 in S:continue
                if ok(n+1,extend(n,A,S))!=ok(n+1,extend(n,B,S)):bad+=1;break
        print(n,'distinguishable pairs after old-view identification:',bad);assert bool(bad)==(n==4)
    A={(0,2),(0,3),(1,2)};B=A|{(1,3)};S={1,3}
    assert key(4,A)==key(4,B) and ok(5,extend(4,A,S)) and not ok(5,extend(4,B,S))
