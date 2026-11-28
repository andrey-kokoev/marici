"""Projected parent blades; exhaustive port coloring holdout on fixed rows."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'voevodsky/checkers'))
from ramsey_repair_next_seam import graph,grow,check,D,json,combinations
from collections import Counter
mask=lambda vs:sum(1<<i for i in vs)
pairs=list(combinations(range(5),2)); data=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(i-1 for i in s) for s in data['supports']),data['gap']);exclude={mask(pairs.index((i-1,j-1)) for i,j in rep['edits']) for rep in data['representatives']};stats=Counter()
for c in range(1024):
    if c in exclude:continue
    a=graph(9,S,c)
    if not check(a,16383,3,7):continue
    stats['parents']+=1
    red=[mask((i,j)) for i,j in combinations(range(14),2) if a[i]>>j&1]
    blue={k:[b for t in combinations(range(14),k) for b in [mask(t)] if all(b&e!=e for e in red)] for k in (5,6)}
    for gap in range(10):
        fl=[i for i in (gap-1,gap) if 0<=i<9];f=mask(fl);base=grow(S,gap)
        veto=len(fl)==2 and any(not b&(f|a[fl[0]]|a[fl[1]]) for b in blue[5]);eligible=[b for b in blue[6] if not b&f];P={b>>9 for b in eligible};minimal={p for p in P if not any(q!=p and q&p==q for q in P)};stats['raw']+=len(eligible);stats['after_projection_before_veto']+=len(minimal);stats['retained']+=0 if veto else len(minimal);stats['vetoed_gaps']+=int(veto)
        for p in range(32):
            N=f|(p<<9);pred=not veto and not any(e!=f and e&N==e for e in red) and all(p&q for q in minimal);actual=check(graph(10,[(*s,gap) if p>>i&1 else s for i,s in enumerate(base)],c),32767,3,7);assert pred==actual,(c,gap,p);stats['moves']+=1;stats['legal']+=int(actual)
print(dict(stats))
