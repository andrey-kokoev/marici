"""Compare symbolic witness lists by path capacity before expanding any six-blade."""
from ga_seam_local_clauses import maximal_cliques,minimal,demands,S,graph,fl,mask,check,combinations
from functools import lru_cache
sites=511
@lru_cache(None)
def cap(m):
    if not m:return 0
    lo=m&-m
    return 1+cap(m&~(lo|lo<<1))

def solve(s,c):
    a=graph(9,s,c);adj={i:{j for j in range(5) if i!=j and not(a[9+i]>>(9+j)&1)} for i in range(5)}
    groups=[]
    for p in range(32):
        if any(a[9+i]&(p<<9) for i in range(5) if p>>i&1):continue
        A=sites
        for i in range(5):
            if p>>i&1:A&=~a[9+i]
        groups.append((p,A))
    def feasible(ban,k):return [(p,A&~ban,k-p.bit_count()) for p,A in groups if not ban&(p<<9) and 0<=k-p.bit_count()<=cap(A&~ban)]
    families={}
    for g,f in enumerate(fl):
        if 0<g<9 and feasible(f|a[g-1]|a[g],5):continue
        ports={i for i in range(5) if not f&a[9+i]}
        for p,_,_ in feasible(f,6):
            for t in maximal_cliques({i for i in ports if not p>>i&1},adj):
                ban=f|(mask(t)<<9);families[ban]=feasible(ban,6)
    # The list for ban X is contained in that for Y iff no X-witness can use a Y vertex.
    def sub(X,Y):
        for p,A,k in families[X]:
            if (p<<9)&Y:return False
            for i in range(9):
                v=1<<i
                if k and v&A&Y and 1+cap(A&~(v|v<<1|v>>1))>=k:return False
        return True
    kept=[]
    for x in families:
        if any(sub(y,x) for y in kept):continue
        kept=[y for y in kept if not sub(x,y)]+[x]
    F=set()
    for x in kept:
        W=set()
        for p,A,k in families[x]:
            for t in combinations([i for i in range(9) if A>>i&1],k):
                m=mask(t)
                if not m&(m<<1):W.add(m|(p<<9))
        F.add(frozenset(W))
    return F
if __name__=='__main__':
    count=0
    for c in range(1024):
        if not check(graph(9,S,c),16383,3,7):continue
        F=solve(S,c);assert F==minimal(set(demands(S,c).values()));count+=1
        if c==192:print('clauses',sorted(map(sorted,F)),'unique blades materialized',len(set.union(set(),*F)))
    print('parents matched',count)
