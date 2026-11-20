"""Adversarial test: delete a swap orbit of red links from an aligned witness, enumerate all independent sevens, and seek a future partition (not moving the seed pair) for which each seven hits all three pairs and >=4 new slots, with at least one 3-old/4-new seven. Prefer old hosts with no independent six, as in the blind generator. Independently verify the first counterexample by exhaustive subsets."""
from itertools import combinations
from pathlib import Path
import json
H=Path(__file__).parent;E={tuple(e) for e in json.loads((H/'ramsey_reserved_blind.json').read_text())['edges']};V=range(22);pair=lambda i,j:tuple(sorted((i,j)));orbits=sorted({tuple(sorted({(i,j),pair(i^1,j^1)})) for i,j in E});assert all(set(o)<=E for o in orbits)
def find(E,strict):
 for o in sorted({tuple(sorted({(i,j),pair(i^1,j^1)})) for i,j in E}):
    R=E-set(o);N=[0]*22
    for i,j in R:N[i]|=1<<j;N[j]|=1<<i
    I=[0]
    for i in V:I += [s|1<<i for s in I if s&N[i]==0]
    six=[s for s in I if s.bit_count()==6];seven=[s for s in I if s.bit_count()==7]
    if not seven:continue
    for P in combinations(range(1,11),3):
        masks=[3<<(2*p) for p in P];m=sum(masks)
        if strict and any(not s&m for s in six):continue
        if not all(all(s&a for a in masks) and (s&m).bit_count()>=4 for s in seven):continue
        if not any((s&m).bit_count()==4 for s in seven):continue
        new=[i for i in V if m>>i&1];ss=[tuple(s) for s in combinations(V,7) if not any(e in R for e in combinations(s,2))];assert len(ss)==len(seven);assert all(not all(e in R for e in combinations(t,2)) for t in combinations(V,3));return dict(deleted=o,future_pairs=[[2*p,2*p+1] for p in P],old_alpha=max(s.bit_count() for s in I if not s&m),blue_sevens=ss,shapes=[len(set(s)&set(new)) for s in ss])
def run():
    sources=[('blind',E)];cat=(H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()
    for row in json.loads((H/'ramsey_37_strip_coherence.json').read_text()):
        p=row['swap'];
        if not p:continue
        order=[x for i in V if i<p[str(i)] for x in (i,p[str(i)])];bits=''.join(f'{ord(c)-63:06b}' for c in cat[row['record']-1][1:]);red=set()
        for i,j in combinations(V,2):
            a,b=sorted((order[i],order[j]));
            if bits[b*(b-1)//2+a]=='1':red.add((i,j))
        sources.append((row['record'],red))
    for strict in (True,False):
        for name,red in sources:
            r=find(red,strict)
            if r:return dict(source=name,red_edges=sorted(red),**r)
r=run();print({k:v for k,v in r.items() if k!='red_edges'} if r else None);(H/'ramsey_blue_shape_counterexample.json').write_text(json.dumps(r,indent=2)+'\n')
