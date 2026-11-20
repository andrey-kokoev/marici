"""Exact two-bit pruning on partial core readings vs raw and subset-closed Hoffman bounds.
Each of six block readings is revealed separately; within it reveal the 28 unordered column pairs.
A plane can be forbidden only after two opposite readings have actually disagreed."""
from itertools import combinations,combinations_with_replacement
from collections import Counter
from pathlib import Path
import random,json

F=(3,5,6,7); P=[]
for a,b,c,d in combinations(range(8),4):
    if a^b^c^d==0:P.append((sum(1<<i for i,x in enumerate(F) if x in (a,b,c,d)),[(a,b,c,d),(a,c,b,d),(a,d,b,c)]))
B=[b for b,_ in P];lines={tuple(sorted((x,y,x^y))) for x,y in combinations(range(1,16),2)};kernels=[sum(1<<i for i,b in enumerate(B) if b in line) for line in lines];assert len(lines)==35
cuts=[sum(1<<i for i,b in enumerate(B) if (b&h).bit_count()%2) for h in range(1,16)]
exact=[];spec=[];closure=[]
for m in range(1<<14):
    exact.append(all(m&s for s in kernels));d=m.bit_count();eig=d-2*max((m&c).bit_count() for c in cuts);spec.append(d>3*(-eig) if m else False);closure.append(spec[m] or any(closure[m^(1<<i)] for i in range(14) if m>>i&1));assert not closure[m] or exact[m]
assert all(exact[m]==all(m & ~(u|v) for u,v in combinations(cuts,2)) for m in range(1<<14))
print('impossible/raw/closed',sum(exact),sum(spec),sum(closure));print('minimal obstructions by size',Counter(m.bit_count() for m in range(1<<14) if exact[m] and all(not exact[m^(1<<i)] for i in range(14) if m>>i&1)))
for name in ('5bit_26','6bit_26','6bit_27_from_catalogue'):
    rows=json.loads(Path(__file__).with_name('ramsey_38_cell_'+name+'.json').read_text())['rows'];obs={};deps={}
    for i,j in combinations_with_replacement(range(3),2):
        for a,b in combinations(range(8),2):obs[i,j,a,b]=rows[8*i+a]>>(8*j+b)&1
        for idx,(_,match) in enumerate(P):
            for a,b,c,d in match:
                x=(i,j,a,b);y=(i,j,c,d)
                if obs[x]!=obs[y]:deps.setdefault(x,[]).append((y,idx));deps.setdefault(y,[]).append((x,idx))
    rng=random.Random(38);steps=[[],[],[]];keys=list(obs)
    for _ in range(200):
        rng.shuffle(keys);known=set();m=0;first=[169]*3
        for t,x in enumerate(keys,1):
            known.add(x)
            for y,idx in deps.get(x,[]):
                if y in known:m|=1<<idx
            for a,rule in enumerate((exact,spec,closure)):
                if rule[m] and first[a]==169:first[a]=t
        for u,v in zip(steps,first):u.append(v)
    print(name,'median first prune of 168 (169=never): exact/raw/closed',*[sorted(s)[99] for s in steps]);print('full forbidden directions',m.bit_count())
