"""Can the three locally safe pair choices pay the same degree budget? Resolve incident removals one vertex at a time. The nine removed edges must be old red edges, never either addition."""
import gzip,json
from collections import Counter
from itertools import combinations,islice
from math import comb
from ramsey_retention_slice import CAT,D,decode,check

def solve(a,pair,z):
    vs=set(range(27))-{z};g=[n&~(1<<z) for n in a];g[z]=0
    for u,v in pair:g[u]|=1<<v;g[v]|=1<<u
    quota={4:6,6:12,7:8}
    def dfs(left,removed):
        if len(removed)>9:return None
        if not left:return list(removed) if len(removed)==9 else None
        best=None
        for u in sorted(left):
            # Removed edges to previously fixed vertices have already been decided.
            deg=g[u].bit_count();nb=[v for v in sorted(left) if a[u]>>v&1];opts=[(d,deg-d) for d,n in quota.items() if n and 0<=deg-d<=min(len(nb),9-len(removed))];size=sum(comb(len(nb),k) for d,k in opts)
            if not size:return None
            if best is None or size<best[0]:best=size,u,nb,opts
        _,u,nb,opts=best
        for d,k in opts:
            quota[d]-=1
            for chosen in combinations(nb,k):
                for v in chosen:g[u]^=1<<v;g[v]^=1<<u
                res=dfs(left-{u},removed+[(min(u,v),max(u,v)) for v in chosen])
                for v in chosen:g[u]^=1<<v;g[v]^=1<<u
                if res is not None:quota[d]+=1;return res
            quota[d]+=1
    return dfs(vs,[])

def audit():
    idx,z=262402,0
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    vs=[i for i in range(27) if i!=z];links=[(u,v) for u,v in combinations(vs,2) if not a[u]>>v&1 and a[u]&a[v]==1<<z];assert len(links)==3;out=[]
    for pair in combinations(links,2):
        assert not set.intersection(*map(set,pair));rm=solve(a,pair,z);row=dict(pair=pair,removals=rm)
        if rm is not None:
            g=[v&~(1<<z) for v in a];g[z]=0
            for u,v in pair:g[u]|=1<<v;g[v]|=1<<u
            assert len(set(rm))==9
            for u,v in rm:assert a[u]>>v&1 and z not in (u,v);g[u]^=1<<v;g[v]^=1<<u
            hist=Counter(g[i].bit_count() for i in vs);assert hist=={4:6,6:12,7:8} and sum(g[i].bit_count() for i in vs)==152;row['degree_counts']=dict(hist);row['avoids_blue_eight']=check(g,((1<<27)-1)^(1<<z),3,8)
        out.append(row)
    print(out);(D.parent/'ramsey_forward_degree_budget.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
