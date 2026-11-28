"""Exact residual obstruction lists after forcing singleton witnesses, parent 192."""
from ga_seam_v5 import S,graph,mask,fl,combinations
from collections import defaultdict

def demands(S,c):
    a=graph(9,S,c);red=[mask(e) for e in combinations(range(14),2) if a[e[0]]>>e[1]&1];B={k:[b for t in combinations(range(14),k) for b in [mask(t)] if all(b&e!=e for e in red)] for k in (5,6)};out={}
    for gap,f in enumerate(fl):
        if 0<gap<9 and any(not b&(f|a[gap-1]|a[gap]) for b in B[5]):continue
        for p in range(32):
            N=f|(p<<9)
            if any(e!=f and N&e==e for e in red):continue
            w=frozenset(b for b in B[6] if not b&N)
            if w:out[gap,p]=w
    return out
if __name__=='__main__':
    D=demands(S,192);forced=set.union(set(),*(set(w) for w in D.values() if len(w)==1));R={m:w for m,w in D.items() if not forced&w};core=sorted({w for w in R.values() if not any(v<w for v in R.values())},key=sorted);print('forced',forced,'residual moves',len(R),'minimal lists and sample moves',[(m,sorted(w)) for w in core for m in [next(m for m,v in R.items() if v==w)] ]);pool=sorted(set.union(set(),*(set(w) for w in core))-{3860});
    for k in range(len(pool)+1):
        opt=[t for t in combinations(pool,k) if all(not w.isdisjoint(t) for w in core)]
        if opt:print('replacement size',k,'number',len(opt),'examples',opt[:4]);break
