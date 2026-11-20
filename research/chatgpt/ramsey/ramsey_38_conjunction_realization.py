"""Add nonempty conjunctions as distinct addresses with exact truth-table cross signs."""
from itertools import combinations

def audit(tests):
    # 111 satisfies every test; therefore all test-test pairs are negative.
    types=range(8);truth=lambda p,t:p&t==t
    free=[(p,q) for p,q in combinations(types,2) if not any(truth(p,t) and truth(q,t) for t in tests)]
    def mask(verts):return sum(1<<i for i,(p,q) in enumerate(free) if p in verts and q in verts)
    triangles=[m for tri in combinations(types,3) if (m:=mask(tri)).bit_count()==3]
    clauses=set()
    for k in range(len(tests)+1):
        for ts in combinations(tests,k):
            neg=[p for p in types if all(not truth(p,t) for t in ts)]
            for vs in combinations(neg,8-k):clauses.add(mask(vs))
    return sum(all(x&c for c in clauses) and all(x&t!=t for t in triangles) for x in range(1<<len(free)))
if __name__=='__main__':
    ts=[]
    for t in [4,2,1,6,5,3,7]:
        ts.append(t)
        if len(ts)>=3:print(t,len(ts)+8,audit(ts))
