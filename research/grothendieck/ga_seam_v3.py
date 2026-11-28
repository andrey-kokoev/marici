"""One exact minimum dictionary per parent, with gaps as set-cover bits."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'voevodsky/checkers'))
from ramsey_repair_next_seam import graph,grow,check,D,json,combinations
from collections import defaultdict,Counter
mask=lambda xs:sum(1<<x for x in xs)
pairs=list(combinations(range(5),2));d=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(i-1 for i in s) for s in d['supports']),d['gap']);omit={mask(pairs.index((i-1,j-1)) for i,j in r['edits']) for r in d['representatives']};stats=Counter()
for c in range(1024):
    if c in omit:continue
    a=graph(9,S,c)
    if not check(a,16383,3,7):continue
    red=[mask((i,j)) for i,j in combinations(range(14),2) if a[i]>>j&1];blue={k:[b for t in combinations(range(14),k) for b in [mask(t)] if all(e&b!=e for e in red)] for k in (5,6)}
    needs=defaultdict(int);flanks=[];veto=[]
    for gap in range(10):
        fl=[i for i in (gap-1,gap) if 0<=i<9];f=mask(fl);flanks.append(f);veto.append(len(fl)==2 and any(not b&(f|a[fl[0]]|a[fl[1]]) for b in blue[5]))
        if not veto[-1]:
            P={b>>9 for b in blue[6] if not b&f}
            for p in P:
                if not any(p!=q and q&p==q for q in P):needs[p]|=1<<gap
    keep=[];num=0
    for p,target in needs.items():
        best={0:()}
        for b in blue[6]:
            if b>>9!=p:continue
            hits=target&mask(i for i,f in enumerate(flanks) if not f&b)
            for t,L in list(best.items()):
                if t|hits not in best or len(best[t|hits])>len(L)+1:best[t|hits]=L+(b,)
        keep.extend(best[target]);num+=len(best[target])>1
    local=sum(t.bit_count() for t in needs.values());print(c,local,len(keep),num);stats.update(local=local,shared=len(keep),multiple=num,projection_groups=len(needs))
    for i,f in enumerate(flanks):
        base=grow(S,i)
        for p in range(32):
            N=f|(p<<9);pred=not veto[i] and not any(e!=f and N&e==e for e in red) and all(b&N for b in keep);actual=check(graph(10,[(*s,i) if p>>j&1 else s for j,s in enumerate(base)],c),32767,3,7);assert actual==pred;stats['moves']+=1;stats['legal']+=int(actual)
print(stats)
