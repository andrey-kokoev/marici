"""Certify alpha(R+S)<=5 on twelve vertices without testing rows: partition into small certified induced subgraphs. Compare odd-cycle factors with general tight block partitions; find size of largest necessary block and blocks' isomorphism-independent size/alpha profiles."""
from functools import lru_cache
from itertools import combinations
from ramsey_inverse_five_motifs import D,json,graph,inds,bits,Counter

def audit(H,R,S):
    V=R|S;F=V;I={t for t in inds(H) if not t&~V};
    @lru_cache(None)
    def alpha(v):
        if not v:return 0
        x=v&-v;return max(alpha(v^x),1+alpha(v&~(x|H[x.bit_length()-1])))
    @lru_cache(None)
    def path(v,end,start):
        if v==1<<end:return (end,) if H[end]>>start&1 else None
        for j in bits(H[end]&v):
            p=path(v^(1<<end),j,start)
            if p:return (end,)+p
    def cycle(v):
        x=next(bits(v));return next(((x,)+p for y in bits(H[x]&v) if (p:=path(v^(1<<x),y,x))),None)
    blocks={};odd={};v=V
    while v:
        n=v.bit_count();a=(v&S).bit_count()
        if a and alpha(v)==a:
            blocks[v]=(n,a)
            if n==1 or n==2 and a==1:odd[v]=list(bits(v))
            elif n%2 and a==n//2:
                p=cycle(v)
                if p:odd[v]=p
        v=(v-1)&V
    def split(pool):
        @lru_cache(None)
        def rec(v):
            if not v:return ()
            x=v&-v;ans=None
            for b in pool:
                if not b&x or b&~v:continue
                t=rec(v^b)
                if t is not None:
                    r=tuple(sorted((b,)+t,key=int.bit_count,reverse=True));key=lambda a:tuple(b.bit_count() for b in a)
                    if ans is None or key(r)<key(ans):ans=r
            return ans
        return rec(V)
    cert=split(odd);general=split(blocks);return dict(S=S,odd=[odd[b] for b in cert] if cert else None,blocks=general,profile=[blocks[b] for b in general])
if __name__=='__main__':
    ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();z=json.loads((D/'ramsey_uncovered_five.json').read_text());out={i:[dict(R=r['leftover'],full=not r['bad'],supports=[audit(graph(ls[int(i)-1]),r['leftover'],s) for s in r['S']]) for r in rows] for i,rows in z.items()};rs=sum(out.values(),[]);print(Counter((r['full'],sum(s['odd'] is not None for s in r['supports'])) for r in rs));print(Counter(tuple(tuple(p) for p in s['profile']) for r in rs for s in r['supports']));(D/'ramsey_odd_block_cover.json').write_text(json.dumps(out)+'\n')
