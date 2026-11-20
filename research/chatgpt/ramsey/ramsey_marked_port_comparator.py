"""Catalogue-free pair reader. Corner i emits the transported seed at i; port ij emits j from i; edge ij emits both ij and ji. For each possible orientation of a midpoint compare emissions across their bases, and also compare each with the transported seed locally. Record all triples of booleans without ordering the two endpoints. Enumerate maximal triangle-free unions of signature classes, via deletion on triangle conflicts. Monotonicity makes these sufficient for minimizing independence number."""
from itertools import permutations,combinations,product
from pathlib import Path
from functools import lru_cache
import json
V=range(4);X=[('c',i) for i in V]+[('p',*e) for e in permutations(V,2)]+[('e',*e) for e in combinations(V,2)]
def test(flat):
    def carry(a,b,i):
        if a==b:return i
        if i==b:return a
        return 6-a-b-i if flat else i
    seed=[carry(0,i,1) for i in V]
    def emits(x):
        t,i,*js=x
        if t=='c':return [(i,seed[i])]
        j,=js;return [(i,j)] if t=='p' else [(i,j),(j,i)]
    def sig(x,y):
        v=[]
        for (a,i),(b,j) in product(emits(x),emits(y)):
            v.append((int(i==seed[a])+int(j==seed[b]),int(carry(a,b,i)==j)))
        return tuple(sorted(v))
    keys={};E={}
    for i,j in combinations(range(22),2):
        s=sig(X[i],X[j]);E[i,j]=1<<keys.setdefault(s,len(keys))
    neg=set(E[i,j]|E[i,k]|E[j,k] for i,j,k in combinations(range(22),3));cs=[]
    for n in sorted(neg,key=int.bit_count):
        if not any(c&n==c for c in cs):cs.append(n)
    leaves=set();visited=set()
    def branch(m):
        if m in visited:return
        visited.add(m);n=next((n for n in cs if n&m==n),0)
        if not n:leaves.add(m);return
        while n:
            b=n&-n;n-=b;branch(m^b)
    branch((1<<len(keys))-1);best=22;example=None
    for m in leaves:
        adj=[0]*22
        for (i,j),b in E.items():
            if m&b:adj[i]|=1<<j;adj[j]|=1<<i
        @lru_cache(None)
        def alpha(w):
            if not w:return 0
            b=w&-w;i=b.bit_length()-1;return max(alpha(w^b),1+alpha((w^b)&~adj[i]))
        a=alpha((1<<22)-1)
        if a<best:best=a;example=[s for s,i in keys.items() if m>>i&1]
    return dict(seed=seed,classes=len(keys),best_alpha=best,red_signatures=example)
r={name:test(f) for name,f in [('flat',True),('route_sensitive',False)]};print([(k,v['classes'],v['best_alpha']) for k,v in r.items()]);Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
