"""Fixed-order rooted (3,6) capacity near the punctured cyclic graph. Stdlib."""
from itertools import combinations


def solve(edges):
    n=12; blue=[0]
    for i in range(n):
        r=sum(1<<j for j in range(i) if (j,i) in edges)
        blue += [s|(1<<i) for s in blue if not s&r]
    if max(map(int.bit_count,blue))>4 or any((a,b) in edges and (a,c) in edges and (b,c) in edges for a,b,c in combinations(range(n),3)):return None
    rows=[s for s in blue if not any(s!=t and s&t==s for t in blue)]
    # Budget 5-|B| misses per blue clique B. Track levels of exhausted budgets.
    initial=tuple(sum(1<<j for j,b in enumerate(blue) if 5-b.bit_count()==i) for i in range(6))
    misses=[sum(1<<j for j,b in enumerate(blue) if not r&b) for r in rows]
    def fit(left,start,levels):
        if not left:return []
        for i in range(start,len(rows)):
            m=misses[i]
            if levels[0]&m:continue
            nxt=tuple((v&~m)|((levels[j+1]&m) if j<5 else 0) for j,v in enumerate(levels))
            tail=fit(left-1,i,nxt)
            if tail is not None:return [rows[i]]+tail
        return None
    for d in range(5,-1,-1):
        witness=fit(d,0,initial)
        if witness is not None:
            assert all(b.bit_count()+sum(not r&b for r in witness)<=5 for b in blue)
            return d,[[i+1 for i in range(n) if r>>i&1] for r in witness]

if __name__=='__main__':
    pairs=set(combinations(range(12),2));base={p for p in pairs if p[1]-p[0] in (1,5,8,12)};ans=solve(base);print('base',ans)
    for p in sorted(pairs):
        other=solve(base^{p})
        if other and other[0]!=ans[0]:print('toggle',tuple(i+1 for i in p),other);break
    else:
        for e in sorted(base):
            for f in sorted(pairs-base):
                other=solve(base^{e,f})
                if other and other[0]!=ans[0]:print('replace',tuple(i+1 for i in e),'by',tuple(i+1 for i in f),other);quit()
        print('No difference at one toggle or one replacement.')
