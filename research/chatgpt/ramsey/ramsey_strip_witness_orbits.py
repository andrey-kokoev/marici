"""Compare literal 11-step outputs under all six-ground-label permutations (each lifts to a pole-preserving graph isomorphism). Verify edge maps on the actual 22-vertex witnesses. Compare all 288 Hall choices as a scope control."""
from ramsey_strip_first_generator import D,M,r,fill,edges
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
import json
rows=[z for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(0,29)]
acts=[]
for p in permutations(range(6)):
 a=tuple(D.index(tuple(sorted((p[i],p[j])))) for i,j in D);b=tuple(M.index(tuple(sorted(D[a[D.index(d)]] for d in t))) for t in M);acts.append((p,a,b))
def transform(u,a,b):return frozenset((a[i],b[j]) for i,j in u)
def red(u):
 deleted={edges(*(D.index(d) for d in M[j] if d!=D[i])) for i,j in u};return {(0,i+1) for i in range(6)}|{(i+1,j+7) for j,d in enumerate(D) for i in d}|{(7+i,7+j) for i,j in combinations(range(15),2) if not set(D[i])&set(D[j]) and (i,j) not in deleted}
orbits={};stats=[];first=None
for idx,z in enumerate(rows,1):
 if not z['closes']:continue
 p=z['path'];c=p+[r[v] for v in p[-2:0:-1]];extra,=fill(set(range(30))-set(c));shared=len(set.intersection(*map(set,z['selected'])))
 for parity in (0,1):
    u=frozenset((i,j-15) for i,j in extra|{edges(c[i],c[(i+1)%22]) for i in range(parity,22,2)});R=red(u);assert len(R)==66
    if u not in orbits:
        n=len(set(orbits.values()))+1
        for _,a,b in acts:orbits[transform(u,a,b)]=n
    if first is None:first=u
    maps=[]
    for perm,a,b in acts:
        if transform(first,a,b)==u:
            lift=(0,*(1+i for i in perm),*(7+j for j in a));assert {edges(lift[i],lift[j]) for i,j in red(first)}==R;maps.append(perm)
    stats.append((idx,shared,parity,orbits[u],maps[:1]));
print('literal outputs',stats,'orbit sizes',Counter(orbits.values()))
def allm(u,used):
 if len(u)==15:yield frozenset(enumerate(u));return
 for j,t in enumerate(M):
    if j not in used and D[len(u)] in t:yield from allm(u+[j],used|{j})
choices=set(allm([],set()));assert len(choices)==288
for u in choices-set(orbits):
 if u in orbits:continue
 n=max(orbits.values())+1
 for _,a,b in acts:orbits[transform(u,a,b)]=n
assert set(orbits)==choices;print('all Hall orbit sizes',Counter(orbits.values()))
for n in sorted(set(orbits.values())):
 R=red(next(u for u,k in orbits.items() if k==n));count=sum(not any(e in R for e in combinations(w,2)) for w in combinations(range(22),6));assert count=={1:139,2:137}[n];print('orbit',n,'independent six-sets',count)
