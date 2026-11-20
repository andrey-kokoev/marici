"""Strip-first generator. Inputs: labeled tetrahedron, column transposition, half-route length 11. No precomputed matchings, strips, distance profiles or graph catalogue. Alternate along a reflected path, then require a shared swap-invariant matching on the unused positions. Verify the first output graph directly."""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json
X=list(combinations(range(4),2));D=list(combinations(range(6),2));M=[m for m in combinations(D,3) if len(set(sum(m,())))==6];g=(0,2,1,3);e=[X.index(tuple(sorted(g[v] for v in x))) for x in X];tr=lambda d:tuple(sorted(e[v] for v in d));r=[D.index(tr(d)) for d in D]+[15+M.index(tuple(sorted(map(tr,m)))) for m in M];N=[set() for _ in r]
for i,d in enumerate(D):
    for j,m in enumerate(M,15):
        if d in m:N[i].add(j);N[j].add(i)
fixed={i for i,v in enumerate(r) if v==i};diagnostics=Counter();H=Counter();first=None;outputs=set();edges=lambda a,b:tuple(sorted((a,b)))
def fill(rem):
    if not rem:yield frozenset();return
    a=min(rem)
    for b in sorted(N[a]&rem):
        es=frozenset([edges(a,b),edges(r[a],r[b])]);used={v for edge in es for v in edge}
        if len(used)!=2*len(es):continue
        for c in fill(rem-used):yield c|es

def visit(p,used):
    global first
    x=p[-1]
    if len(p)==12:
        if x not in fixed or p[1]>r[p[1]]:return
        cycle=p+[r[y] for y in p[-2:0:-1]];assert len(set(cycle))==22
        m=frozenset(edges(cycle[i],cycle[i+1]) for i in range(0,22,2));rem=set(range(30))-set(cycle);cs=list(fill(rem));H[len(cs)]+=1;diagnostics[len(cs),sum(not(N[i]&rem) for i in rem)]+=1
        for c in cs:
            u=m|c;v=frozenset(edges(r[a],r[b]) for a,b in u);assert u&v==c and len(u)==15 and len({x for edge in u for x in edge})==30;outputs.add(frozenset([u,v]));
            if first is None:first=(p,c,u)
        return
    for y in sorted(N[x]-used):
        if (y in fixed)!=(len(p)==11):continue
        visit(p+[y],used|{y,r[y]})
for s in sorted(fixed&set(range(15))):visit([s],{s})
p,c,u=first;removed={tuple(sorted(D.index(d) for d in M[j-15] if d!=D[i])) for i,j in u};red={(0,1+i) for i in range(6)}|{(1+i,7+j) for j,d in enumerate(D) for i in d}|{(7+i,7+j) for i,j in combinations(range(15),2) if set(D[i]).isdisjoint(D[j]) and (i,j) not in removed};assert len(red)==66 and not any(all(z in red for z in combinations(t,2)) for t in combinations(range(22),3));assert all(any(z in red for z in combinations(t,2)) for t in combinations(range(22),7));print('residual completion counts -> routes:',H,'fill/isolation',diagnostics,'distinct swap pairs',len(outputs),'first path',p);Path(__file__).with_suffix('.json').write_text(json.dumps(dict(residual_hist=H,fill_isolation={str(k):v for k,v in diagnostics.items()},output_pairs=len(outputs),first_half=p,remaining=sorted(c),matching=sorted(u),red=sorted(red)),indent=2)+'\n')
