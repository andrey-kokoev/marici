"""Construct one embedding per S4 orbit of local square choices in a single verified witness. A square choice is f(a)=the neighbor whose port is opposite the corner in that square."""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter
import random,json
H=Path(__file__).parent;V=range(4);P=list(permutations(V));rng=random.Random(42)
def act(f,p):return tuple(p[f[p.index(i)]] for i in V)
canon={f:min(act(f,p) for p in P) for f in product(V,repeat=4) if all(f[i]!=i for i in V)};sizes=Counter(canon.values());cert={};edges=list(combinations(V,2))
line=(H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()[0];bits=''.join(f'{ord(x)-63:06b}' for x in line[1:]);N=[set() for _ in range(22)]
for j in range(22):
    for i in range(j):
        if bits[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
assert not any(N[i]&N[j] for i in range(22) for j in N[i]);assert all(any(b in N[a] for a,b in combinations(s,2)) for s in combinations(range(22),7))
squares=[s for s in combinations(range(22),4) if all(len(N[v]&set(s))==2 for v in s)]
for trial in range(1000):
    if len(cert)==len(sizes):break
    rng.shuffle(squares);blocks=[];used=set()
    for s in squares:
        if not used.intersection(s):blocks.append(s);used.update(s)
        if len(blocks)==4:break
    if len(blocks)<4:continue
    def fit(todo,F,M,path):
        if len(cert)==len(sizes):return
        if not todo:
            cs=[next(iter(s)) for s in F];ports=[{} for _ in V]
            for a,b,x,m,y in path:ports[a][b]=x;ports[b][a]=y;assert x in N[m] and y in N[m] and y not in N[x]
            f=tuple(next(b for b,x in ports[a].items() if x not in N[cs[a]]) for a in V);key=canon[f]
            if key not in cert:cert[key]=dict(f=f,blocks=blocks,corners=cs,paths=path,trial=trial)
            return
        options=[([(x,y,m) for m in sorted(M) for x in sorted(F[a]&N[m]) for y in sorted(F[b]&N[m])],a,b) for a,b in todo];ch,a,b=min(options,key=lambda t:(len(t[0]),t[1:]));
        for x,y,m in ch:
            L=F.copy();L[a]=F[a]-{x};L[b]=F[b]-{y};fit(todo-{(a,b)},L,M-{m},path+[(a,b,x,m,y)])
    fit(set(edges),list(map(set,blocks)),set(range(22))-used,[])
assert len(cert)==len(sizes);out=[dict(representative=k,orbit_size=sizes[k],**cert[k]) for k in sorted(sizes)];print([(x['representative'],x['orbit_size'],x['trial']) for x in out]);(H/'ramsey_state_square_types.json').write_text(json.dumps(dict(record=1,types=out),indent=2)+'\n')
