"""Look for a single root witness clause that completes the point-only proof."""
from ramsey_point_witness_ablation import clauses,minimal,combinations,bits,T
from ramsey_shared_frame_propagation import rules
from ramsey_shared_frame_reconstruction import degree

# Preserve the cardinality rules only; replace the full independence obligations.
base=rules[:len(T)+sum(all(e in bits for e in combinations(t,2)) for t in combinations(range(len(T)),3))]
base+= [(m,1,m.bit_count()) for m in minimal(set.union(*(clauses(p) for p in range(1,7))))]
def solutions(y=0,n=0):
    while True:
        old=y,n
        for m,l,h in base:
            a=(m&y).bit_count();f=m&~(y|n)
            if a>h or a+f.bit_count()<l:return
            if a==h:n|=f
            elif a+f.bit_count()==l:y|=f
        if old==(y,n):break
    b=next((b for b in bits.values() if not (y|n)&b),0)
    if not b:yield y;return
    yield from solutions(y|b,n);yield from solutions(y,n|b)

if __name__=='__main__':
    S=list(solutions());assert len(S)==6
    core=sum(b for e,b in bits.items() if not set(e)&{10,11});patterns={s&core for s in S};assert len(patterns)==2
    cycle=[1,5,6,13,2,4,9,12];cyclemask=sum(bits[tuple(sorted((i,j)))] for i,j in zip(cycle,cycle[1:]+cycle[:1]));u,v=patterns;assert u^v==cyclemask
    both=[]
    for U in combinations(range(15),6):
        C=sum(bits.get(e,0) for e in combinations(U,2));bad=[s for s in S if not s&C]
        if len(bad)==2:
            both.append((U,C));print('root gate',[T[i] for i in U], 'intersections', [ [(T[i],T[j]) for (i,j),b in bits.items() if b&s&C] for s in S])
    print('shared gates',len(both));print('exception masks',[hex(s) for s in S if any(not s&C for _,C in both)])
