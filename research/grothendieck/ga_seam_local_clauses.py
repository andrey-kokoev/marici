"""Generate deciding witness lists from maximal independent port sets, without a move sweep."""
from ga_seam_v5 import graph,mask,fl,S,combinations,check
from ga_seam_residual import demands

def minimal(F):return {w for w in F if not any(v<w for v in F)}
def maximal_cliques(P,adj):
    def rec(R,P,X):
        if not P and not X:yield R
        for v in list(P):
            yield from rec(R|{v},P&adj[v],X&adj[v]);P=P-{v};X=X|{v}
    yield from rec(set(),P,set())

def local(s,c):
    a=graph(9,s,c);blue={k:[mask(t) for t in combinations(range(14),k) if all(not(a[i]>>j&1) for i,j in combinations(t,2))] for k in (5,6)};adj={i:{j for j in range(5) if i!=j and not(a[9+i]>>(9+j)&1)} for i in range(5)};Q={};base={};seen=set()
    for gap,f in enumerate(fl):
        if 0<gap<9 and any(not b&(f|a[gap-1]|a[gap]) for b in blue[5]):continue
        W={b for b in blue[6] if not b&f};P={i for i in range(5) if not a[9+i]&f};base[gap]=W
        for b in W:
            for t in maximal_cliques({i for i in P if not b>>(9+i)&1},adj):
                p=mask(t);seen.add((gap,p));Q[gap,p]=frozenset(z for z in W if not (z>>9)&p)
    return Q,base
if __name__=='__main__':
    parents=0;checked=0
    for c in range(1024):
        if not check(graph(9,S,c),16383,3,7):continue
        Q,base=local(S,c);F=minimal(set(Q.values()));assert F==minimal(set(demands(S,c).values()));parents+=1;checked+=len(Q)
        if c==192:
            forced={next(iter(w)) for w in F if len(w)==1};r=[(g,W) for g,W in base.items() if W and not W&forced];print('local probes',len(Q),'clauses',[sorted(w) for w in sorted(F,key=lambda w:(len(w),sorted(w)))],'blank gaps avoiding forced',[(g,len(W)) for g,W in r]);print('minimal clauses realized at',[(sorted(w),sorted(m for m,v in Q.items() if v==w)[:4]) for w in F])
    print('all legal parents',parents,'local probe keys',checked)
