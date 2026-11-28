"""Coordinate exterior product is nonzero iff basis supports are disjoint."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'voevodsky/checkers'))
from ramsey_repair_next_seam import graph,grow,check,D,json,combinations
from collections import Counter
pairs=list(combinations(range(5),2)); mask=lambda v:sum(1<<i for i in v)
data=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(x-1 for x in s) for s in data['supports']),data['gap'])
for rep in data['representatives']:
    C=[tuple(sorted((i-1,j-1))) for i,j in rep['edits']]; frames=[]
    for reflected in (False,True):
        ss=tuple(tuple(8-x for x in s) for s in reversed(S)) if reflected else S
        c=mask(pairs.index((4-j,4-i) if reflected else (i,j)) for i,j in C);a=graph(9,ss,c);assert check(a,16383,3,7)
        red=[mask((i,j)) for i,j in combinations(range(14),2) if a[i]>>j&1];blue={k:[m for t in combinations(range(14),k) if not any((m:=mask(t))&e==e for e in red)] for k in (5,6)};ans={};counts=Counter()
        for gap in range(10):
            fl=[i for i in (gap-1,gap) if 0<=i<9];f=mask(fl);veto=len(fl)==2 and any(not b&(f|a[fl[0]]|a[fl[1]]) for b in blue[5]);base=grow(ss,gap)
            for k in (1,2,3):
                for p in combinations(range(5),k):
                    N=f|mask(i+9 for i in p);pred=not(veto or any(e!=f and e&N==e for e in red) or any(not b&N for b in blue[6]));actual=check(graph(10,[(*s,gap) if i in p else s for i,s in enumerate(base)],c),32767,3,7);assert pred==actual,(gap,p)
                    ans[(9-gap,tuple(sorted(4-i for i in p))) if reflected else (gap,p)]=pred;counts[k]+=pred
        frames.append(ans)
    assert frames[0]==frames[1];print('edits',C,'legal by mark count',dict(counts),'per frame',len(ans))
