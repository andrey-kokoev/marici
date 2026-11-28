"""Decision-only minimum on the v3 domain; no child calls until replay."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'voevodsky/checkers'))
from ramsey_repair_next_seam import graph,grow,check,D,json,combinations
mask=lambda xs:sum(1<<x for x in xs)
pairs=list(combinations(range(5),2));d=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(i-1 for i in s) for s in d['supports']),d['gap']);omit={mask(pairs.index((i-1,j-1)) for i,j in r['edits']) for r in d['representatives']}
for c in range(1024):
    if c in omit:continue
    a=graph(9,S,c)
    if not check(a,16383,3,7):continue
    red=[mask((i,j)) for i,j in combinations(range(14),2) if a[i]>>j&1];blue={k:[b for t in combinations(range(14),k) for b in [mask(t)] if all(e&b!=e for e in red)] for k in (5,6)};moves=[];constraints=set()
    for gap in range(10):
        fl=[i for i in (gap-1,gap) if 0<=i<9];f=mask(fl);veto=len(fl)==2 and any(not b&(f|a[fl[0]]|a[fl[1]]) for b in blue[5]);
        for p in range(32):
            N=f|(p<<9);gate=not veto and not any(e!=f and N&e==e for e in red);w=frozenset(b for b in blue[6] if not b&N);moves.append((gap,p,gate,w))
            if gate and w:constraints.add(w)
    pool=sorted(set().union(*constraints));cons=sorted(constraints,key=len)
    for k in range(len(pool)+1):
        opt=[frozenset(t) for t in combinations(pool,k) if all(not w.isdisjoint(t) for w in cons)]
        if opt:break
    legal=0
    for gap,p,gate,w in moves:
        base=grow(S,gap);actual=check(graph(10,[(*s,gap) if p>>j&1 else s for j,s in enumerate(base)],c),32767,3,7);assert all((gate and w.isdisjoint(t))==actual for t in opt);legal+=int(actual)
    print(c,'minimum',k,'optima',len(opt),'moves',len(moves),'legal',legal,flush=True)
