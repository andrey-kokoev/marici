"""Exact orbit-color search on 4 corners, 12 directed ports, 6 edge positions.
A red triangle forbids an all-red orbit mask; a blue k-set forbids an all-blue mask.
Remove redundant supersets before solving by unit propagation and binary splitting."""
from itertools import combinations, permutations
from pathlib import Path
import json
V=range(4); X=[('c',i) for i in V]+[('p',*t) for t in permutations(V,2)]+[('e',*t) for t in combinations(V,2)]
def act(g,x):
    a=[g[i] for i in x[1:]];return (x[0],*(sorted(a) if x[0]=='e' else a))
def minimal(masks):
    out=[]
    for m in sorted(set(masks),key=lambda x:(x.bit_count(),x)):
        if not any(v&m==v for v in out):out.append(m)
    return out
def solve(neg,pos):
    def visit(r,b):
        while True:
            rr=bb=0;pick=0
            for clauses,good,bad,positive in ((neg,b,r,False),(pos,r,b,True)):
                for m in clauses:
                    if m&good:continue
                    v=m&~bad
                    if not v:return None
                    if v&(v-1)==0:
                        if positive:rr|=v
                        else:bb|=v
                    if not pick or v.bit_count()<pick.bit_count():pick=v
            if rr&bb:return None
            if not(rr|bb):break
            r|=rr;b|=bb
        if not pick:return r
        bit=pick&-pick;t=visit(r|bit,b);return t if t is not None else visit(r,b|bit)
    return visit(0,0)
def test(group):
    bits={};orbits=[]
    for e in combinations(range(22),2):
        if e not in bits:
            orbit={tuple(sorted(X.index(act(g,X[i])) for i in e)) for g in group};v=1<<len(orbits);orbits.append(sorted(orbit));bits.update(dict.fromkeys(orbit,v))
    # enumerate subsets modulo the group by deduplicating their orbit masks
    def layer(k):
        ms=set()
        def rec(prefix,first,m):
            if len(prefix)==k:ms.add(m);return
            for j in range(first,22-k+len(prefix)+1):
                n=m
                for i in prefix:n|=bits[i,j]
                rec((*prefix,j),j+1,n)
        rec((),0,0);return minimal(ms)
    neg=layer(3);res={}
    for k in [7,8]:
        pos=layer(k);t=solve(neg,pos);res[k]=None if t is None else [e for e,v in bits.items() if v&t];
        if t is not None:
            E=set(res[k]);assert not any(all(e in E for e in combinations(c,2)) for c in combinations(range(22),3));assert all(any(e in E for e in combinations(c,2)) for c in combinations(range(22),k));break
    return dict(pair_orbits=len(orbits),red_edges=res)
G=list(permutations(V));A=[g for g in G if sum(g[i]>g[j] for i,j in combinations(V,2))%2==0];out={n:test(g) for n,g in [('S4',G),('A4',A)]};print([(n,r['pair_orbits'],[(k,None if v is None else len(v)) for k,v in r['red_edges'].items()]) for n,r in out.items()]);Path(__file__).with_suffix('.json').write_text(json.dumps(dict(positions=X,results=out),indent=2)+'\n')
