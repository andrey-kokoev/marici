"""Local boundary-order obstructions at every degree-seven root of catalogue graph 1."""
from itertools import combinations,permutations
from collections import Counter
from ramsey38_support_ball_completion import N

def inspect(root):
    P=N[root]; rows={v:frozenset(N[v]&P) for v in N if v!=root and v not in P}
    if max(map(len,rows.values()))>4:return 'dimension',[(v,sorted(r)) for v,r in rows.items() if len(r)>4]
    bad={}
    for c in sorted(P):
        link={frozenset(e) for r in rows.values() if c in r for e in combinations(r-{c},2)}
        ds={v:r-{c} for v,r in rows.items() if c in r and 2<=len(r)<=3}
        # Forget unrequested rim vertices: deletion preserves cyclic order and
        # cannot turn alternating endpoints into nonalternating ones.
        cache={};found=[]
        for k in range(1,len(ds)+1):
            for q in combinations(ds,k):
                if any(s.issubset(q) for s in found):continue
                req=frozenset(ds[v] for v in q)
                if req not in cache:
                    labels=sorted(set().union(*req));ok=False
                    for tail in permutations(labels[1:]):
                        cyc=labels[:1]+list(tail);rim={frozenset((cyc[i-1],b)) for i,b in enumerate(cyc)}
                        if any(len(d)==2 and d not in rim for d in req):continue
                        chords=[sorted(cyc.index(v) for v in e) for e in link if e.issubset(cyc)]
                        if not any(a<c<b<d or c<a<d<b for (a,b),(c,d) in combinations(chords,2)):ok=True;break
                    cache[req]=ok
                if not cache[req]:found.append(frozenset(q))
        for s in found:bad.setdefault(s,[]).append(c)
    return 'rim',{tuple(sorted(s)):bad[s] for s in bad if not any(t<s for t in bad)}

if __name__=='__main__':
    for r in N:
        if len(N[r])==7:
            typ,x=inspect(r);print(r,typ, len(x),x)
