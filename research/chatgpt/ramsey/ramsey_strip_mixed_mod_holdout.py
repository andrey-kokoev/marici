"""Freeze the mixed-mod prediction, vary only involution cycle type on the six Hall labels. All opposite-type fixed endpoints at distance 3; simple reflected paths disjoint in their interiors. Ground truth from invariant residual perfect matching, not residues."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
H=Path(__file__).parent;rules=[set(map(tuple,t)) for t in json.loads((H/'ramsey_strip_bridge_profiles.json').read_text())['whole']['examples']];D=list(combinations(range(6),2));M=[t for t in combinations(D,3) if len(set(sum(t,())))==6];N=[set() for _ in range(30)]
for i,d in enumerate(D):
 for j,t in enumerate(M,15):
    if d in t:N[i].add(j);N[j].add(i)
dist=[]
for s in range(30):
 q=[s];ds={s:0}
 for x in q:
    for y in N[x]-ds.keys():ds[y]=ds[x]+1;q.append(y)
 dist.append(ds)
def census(k):
 g=[i^1 if i<2*k else i for i in range(6)];f=lambda d:tuple(sorted(g[i] for i in d));r=[D.index(f(d)) for d in D]+[15+M.index(tuple(sorted(map(f,t)))) for t in M];fixed={i for i in range(30) if r[i]==i};h=Counter()
 @lru_cache(None)
 def fill(rem):
    if not rem:return True
    i=min(rem)
    for j in N[i]&rem:
        if (i==r[i])!=(j==r[j]):continue
        if fill(rem-{i,j,r[i],r[j]}):return True
    return False
 def walk(p,used):
    for x in N[p[-1]]-used:
        if len(p)==1 and x>=r[x]:continue
        if x not in fixed:walk(p+[x],used|{x,r[x]});continue
        s=p[0];
        if x<15 or dist[s][x]!=3:continue
        (br,)=[(s,i,j,x) for i in N[s] for j in N[x]&N[i]];S=sum(tuple(dist[v][i] for i in br) in rule for rule in rules for v in p[1:]);L=len(p);ok=fill(frozenset(range(30))-used-{x});pred=(L%3,S%4) not in {(0,0),(2,1)};h[L,S,ok,pred]+=1
 for s in fixed&set(range(15)):walk([s],{s})
 return h
if __name__=='__main__':
 base=census(2);assert sum(base.values())==96 and all(o==p for l,s,o,p in base);seen={(l,s) for l,s,o,p in base}
 for k in [1,3]:
    h=census(k);print('swaps',k,'all',sum(h.values()),'novel groups',[(key,n) for key,n in sorted(h.items()) if key[:2] not in seen]);print('confusion',Counter({(o,p):sum(n for (_,_,a,b),n in h.items() if (a,b)==(o,p)) for _,_,o,p in h}))
