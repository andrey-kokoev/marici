"""Compress point tests into panels of named points, preserving all six survivors."""
from itertools import combinations
from ramsey_point_witness_ablation import T,bits,minimal,search
panels={}
for k in (2,3,4):
    for p in combinations('abcdef',k):
        pool=[i for i,t in enumerate(T) if not set(p).intersection(t)]
        cs=minimal({sum(bits.get(e,0) for e in combinations(U,2)) for U in combinations(pool,7-k)})
        if cs:panels[''.join(p)]=cs
names=list(panels);patterns={}
def visit(N):
    m=sum(b for (i,j),b in bits.items() if j in N[i]);f=sum(1<<i for i,cs in enumerate(panels.values()) if any(not m&c for c in cs));patterns[f]=patterns.get(f,0)+1
if __name__=='__main__':
    search(set(range(15)),visit);assert patterns[0]==6
    # Only inclusion-minimal violation patterns matter for a hitting set.
    req=minimal(set(patterns)-{0});best=(1<<len(names))-1
    def hit(chosen,remaining):
        global best
        if chosen.bit_count()>=best.bit_count():return
        if not remaining:best=chosen;return
        m=min(remaining,key=int.bit_count)
        while m:
            b=m&-m;m-=b;hit(chosen|b,[r for r in remaining if not r&b])
    print('minimal violation sets',[[s for i,s in enumerate(names) if r>>i&1] for r in req]);hit(0,req);print('available',len(names),'patterns',len(patterns),'minimal patterns',len(req),'minimum panels',[s for i,s in enumerate(names) if best>>i&1]);print('indispensable',[s for i,s in enumerate(names) if 1<<i in patterns]);print('private near misses',[(s,sum(n for f,n in patterns.items() if f&best==1<<i)) for i,s in enumerate(names) if best>>i&1]);assert sum(n for f,n in patterns.items() if not f&best)==6
