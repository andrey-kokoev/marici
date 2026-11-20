"""Target-independent partial rule: maximize red links inside each four-position state (an induced C4); in each reversal triple take the red two-edge path through its midpoint. Verify that this partial pattern embeds, without requiring global reflection symmetry. Catalogue used ONLY as a completion oracle. Deterministic bounded searches: failure is not an impossibility result."""
from itertools import combinations,permutations
from pathlib import Path
import random,json
H=Path(__file__).parent; rng=random.Random(12345); best=-1;result=None
for idx,line in enumerate((H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines(),1):
    bits=''.join(f'{ord(c)-63:06b}' for c in line[1:]);N=[set() for _ in range(22)]
    for j in range(22):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
    squares=[s for s in combinations(range(22),4) if all(len(N[i].intersection(s))==2 for i in s)];edges=list(combinations(range(4),2))
    for trial in range(80):
        rng.shuffle(squares);blocks=[];used=set()
        for s in squares:
            if not used.intersection(s):blocks.append(s);used.update(s)
            if len(blocks)==4:break
        if len(blocks)!=4:continue
        remain=set(range(22))-used
        # Each link uses an unused port at each endpoint and one distinct midpoint.
        def fit(todo,free,mids,path):
            if not todo:return path
            opts=[]
            for a,b in todo:
                choices=[(x,y,m) for m in sorted(mids) for x in sorted(free[a]&N[m]) for y in sorted(free[b]&N[m])];opts.append((len(choices),a,b,choices))
            _,a,b,ch=min(opts)
            for x,y,m in ch:
                f=free.copy();f[a]=f[a]-{x};f[b]=f[b]-{y};z=fit(todo-{(a,b)},f,mids-{m},path+[(a,b,x,m,y)])
                if z:return z
        paths=fit(set(edges),list(map(set,blocks)),remain,[])
        if paths:
            assert len({m for a,b,x,m,y in paths})==6 and all(y not in N[x] and x in N[m] and y in N[m] for a,b,x,m,y in paths)
            assert not any(N[a]&N[b] for a in range(22) for b in N[a]);assert all(any(b in N[a] for a,b in combinations(s,2)) for s in combinations(range(22),7))
            result=dict(record=idx,trial=trial,blocks=blocks,paths=paths);break
    if result:break
assert result;print(result);(H/'ramsey_state_square_transport_seed.json').write_text(json.dumps(result,indent=2)+'\n')
