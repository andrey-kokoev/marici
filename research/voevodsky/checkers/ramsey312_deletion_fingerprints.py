"""For a fixed circular certificate lifted unchanged to the 49-core, which extra deletions repair its eleven- and ten-set defects? Test all 1176 masks, allowing projection and either incident color."""
from ramsey312_google_two_step import *
from itertools import combinations
from collections import Counter

def main():
 rows=json.loads((D/'ramsey312_conditioned_packing.json').read_text());T=list(sets(F,10));E=list(sets(F,11));out=[]
 for tri in sorted({tuple(r['triple']) for r in rows if r['cert']}):
    h=F^sum(1<<i for i in tri);c=h&adj[tri[0]]&adj[tri[1]]&adj[tri[2]];P=[(1<<i)|(1<<j) for i,j in combinations(bits(h),2)];full=(1<<len(P))-1;tv=[t for t in T if t&~h==0];ev=[t for t in E if t&~h==0];inc={i:sum(1<<j for j,p in enumerate(P) if p>>i&1) for i in bits(h)}
    from functools import lru_cache
    @lru_cache(None)
    def hit(t):
        v=0
        for i in bits(t):v|=inc[i]
        return v
    @lru_cache(None)
    def defect(x,k):
        v=full;ds=[t for t in (ev if k==11 else tv) if not x&t];
        for t in ds:v&=hit(t)
        return v,len(ds)
    @lru_cache(None)
    def edge(x,y):
        u=x&y;red=full
        for i in bits(u):red&=inc[i]
        return red|defect(x|y,10)[0]
    def pairlabels(v):return [list(bits(P[j])) for j in bits(v)]
    result=[];total=[0]*4
    for r in rows:
        if tuple(r['triple'])!=tri:continue
        for z in r['cert']:
            cyc=z['cycle'];x,y=z['endpoints'];v=full
            for s in cyc:v&=defect(s,11)[0]
            a=v;n=len(cyc);q=n//3
            for i,j in combinations(range(n),2):
                if q<=j-i<=n-q:v&=edge(cyc[i],cyc[j])
            b=v;v&=defect(x,11)[0]&defect(y,11)[0];k=v;v&=edge(x,y)
            for s in cyc:v&=edge(s,x)&edge(s,y)
            for j in list(bits(v)):
                d=P[j];ss=[s&~d for s in [*cyc,x,y]]
                if len(set(ss))<n+2 or not (c&~d) or all((ss[-1]&c&~d)==(c&~d) for _ in [0]) or ss[-2]&c&~d==c&~d:v^=1<<j
            assert v>>P.index(sum(1<<i for i in set(r['d'])-set(tri)))&1
            for j,m in enumerate([a,b,k,v]):total[j]|=m
            result.append(dict(source=r['d'],end=[x,y],legal=a.bit_count(),cycle=b.bit_count(),cycle_pairs=pairlabels(b),plus_legal_end=k.bit_count(),complete=pairlabels(v)))
    summary=[m.bit_count() for m in total];print(tri,'stage unions',summary,'full',pairlabels(total[-1]),'cycle-only',pairlabels(total[1])[:60]);out.append(dict(triple=tri,stage_unions=summary,tests=result))
 (D/'ramsey312_deletion_fingerprints.json').write_text(json.dumps(out))
if __name__=='__main__':main()
