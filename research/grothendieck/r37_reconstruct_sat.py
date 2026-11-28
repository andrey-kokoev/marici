"""All labelled legal completions of fixed roots and fixed six-blade support."""
from r37_exchange_falsifier import a,n,blades,legal,combinations
from pysat.solvers import Solver

def models(g,B,block=True,positive_only=False):
    V=range(n); X=range(6,n); edges=list(combinations(X,2)); ids={e:i for i,e in enumerate(edges,1)}
    C=[]
    for i,j in edges:
        if g[i]&g[j]&63:C.append([-ids[i,j]])
    for t in combinations(X,3):C.append([-ids[e] for e in combinations(t,2)])
    for t in combinations(X,6):
        L=[ids[e] for e in combinations(t,2)]
        if frozenset(t) in B:C.extend([[-x] for x in L])
        elif not positive_only:C.append(L)
    # An independent exterior set S extends by all roots it misses.
    for k in range(1,8):
        for t in combinations(X,k):
            union=0
            for i in t:union |= g[i]&63
            if k>union.bit_count():C.append([ids[e] for e in combinations(t,2)])
    if block:C.append([-v if g[i]>>j&1 else v for (i,j),v in ids.items()])
    with Solver(name='cadical195',bootstrap_with=C) as s:
        for m in s.enum_models():
            h=g.copy()
            for (i,j),v in ids.items():
                if bool(h[i]>>j&1)!=(m[v-1]>0):h[i]^=1<<j;h[j]^=1<<i
            assert legal(h) and (B<=blades(h) if positive_only else B==blades(h));yield h
if __name__=='__main__':
    B=blades(a);assert len(B)==10 and legal(a)
    print('alternative labelled completions',sum(1 for _ in models(a,B)))
