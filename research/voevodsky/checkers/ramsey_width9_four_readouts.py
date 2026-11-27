"""Input: unordered distinct rows on anonymous columns, with undirected single swaps. No placement or display order passed to recover()."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json

def recover(rows,swaps):
    cubes=set()
    for r in rows:
        for ds in combinations([r^s for s in swaps[r]],3):
            if len(set.union(set(),*ds))!=6:continue
            c={r}
            for d in ds:c|={s^d for s in c}
            if c<=rows and all(s^d in swaps[s] for s in c for d in ds):cubes.add(frozenset(c))
    return cubes

def run():
    U=range(1,10);rows={frozenset(t) for t in combinations(U,3) if min(t[1]-t[0],t[2]-t[1])>=2};swaps={r:{s for s in rows if len(s^r)==2 and max(s^r)-min(s^r)==1} for r in rows};cs=recover(rows,swaps)
    def relabel(f):
        F=lambda r:frozenset(map(f,r));return F,{F(r):{F(s) for s in v} for r,v in swaps.items()}
    F,G=relabel(lambda i:(4*i)%9);assert recover(set(G),G)=={frozenset(map(F,c)) for c in cs}
    M,H=relabel(lambda i:10-i);assert H==swaps
    starts=[(1,4,7),(1,4,8),(1,5,8),(2,5,8)];ordered=[frozenset(frozenset(t) for t in product(*(range(i,i+2) for i in a))) for a in starts];assert set(ordered)==cs
    dims=Counter()
    for a,b in combinations(cs,2):
        I=a&b;ds={len(swaps[s]&I) for s in I};d,=ds;assert len(I)==2**d;dims[d]+=1
    owners=lambda seq:{r:next(i for i in seq if r in ordered[i]) for r in set().union(*cs)}
    x=owners(range(4));y=owners(tuple(reversed(range(4))))
    changes=sum(x[r]!=y[r] for r in x);r=frozenset((2,5,8));assert (x[r],y[r])==(0,3);assert M(r)==r and frozenset(map(M,ordered[0]))==ordered[-1]
    out=dict(distinct_rows=len(rows),placements=len(cs),pair_overlap_dimensions=dict(sorted(dims.items())),covered_rows=len(x),changed_first_owner=changes,example=dict(row=sorted(r),forward_start=starts[x[r]],reverse_start=starts[y[r]]));print(out);p=Path(__file__).resolve().parents[1]/'results/ramsey_width9_four_readouts.json';s=json.dumps(out,indent=2)+'\n';assert not p.exists() or p.read_text()==s;p.write_text(s)
if __name__=='__main__':run()
