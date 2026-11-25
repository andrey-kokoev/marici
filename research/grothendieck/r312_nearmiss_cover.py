"""Old independent 12-set covering bound on arbitrary graph edits."""
from itertools import combinations
n=49
D={6,11,16,21,23,24}
V=(1<<n)-1
adj=[sum(1<<w for w in range(n) if min((v-w)%n,(w-v)%n) in D) for v in range(n)]
def independent(p,need,s=0):
    if not need:
        yield s
        return
    while p.bit_count()>=need:
        b=p&-p;p^=b
        yield from independent(p&~adj[b.bit_length()-1],need-1,s|b)
old=list(independent(V,12))
assert old and not next(independent(V,13),0)
counts={}
for d in range(1,25):
    if d not in D:
        counts[d]=sum(1 for s in old if s&1 and s&(1<<d))
print('12-sets',len(old),'coverage by distance',counts)
m=max(counts.values()); print('necessary additions',(len(old)+m-1)//m)
# Stronger witness: greedily pack 12-sets sharing at most one vertex,
# so a single added pair cannot kill two packed sets.
pack=[]
for s in old:
    if all((s&t).bit_count()<2 for t in pack):pack.append(s)
print('pair-disjoint packing size',len(pack))
print('minimum common neighbors on a nonedge',min((adj[0]&adj[d]).bit_count() for d in counts))
