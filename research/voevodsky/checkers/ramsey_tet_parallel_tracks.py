"""Use distinct Excel swap tracks, not graph vertex IDs, to keep both witnesses named."""
from collections import defaultdict,Counter
from itertools import product,combinations
from pathlib import Path
from functools import lru_cache
import json
from ramsey_table_cube_differences import analyze
from ramsey_quartet_live_probe import independent_sets


def audit():
    k=9;tracks=defaultdict(set)
    for p in analyze(k)['pieces']:
        a=p['start']
        for i in range(3):
            for s in product(*[(v,) if j==i else (v,v+1) for j,v in enumerate(a)]):
                t=list(s);t[i]+=1;tracks[i,a[i]].add((s,tuple(t)))
    @lru_cache(None)
    def legal(rows,mark):
        g={(i,i+1) for i in range(1,k)}|{(v,k+j) for j,r in enumerate(rows,1) for v in r}
        if mark:g.add((k+1,k+3))
        tris=[t for t in combinations(range(1,k+5),3) if all(e in g for e in combinations(t,2))];seven=bool(independent_sets(k+4,g,7));return not tris and not seven
    counts=Counter();ex=None
    for (i,x),pool in sorted(tracks.items()):
        for four in combinations(sorted(pool),4):
            for R in combinations(four,2):
                B=tuple(p for p in four if p not in R);fixed=lambda t:set(t[0])-{x}
                if any(fixed(r)&fixed(b) for r in R for b in B):continue
                rows=R+B;a=tuple(t[j] for t,j in zip(rows,(0,1,0,1)));b=tuple(t[j] for t,j in zip(rows,(0,1,1,0)));assert set(a[0])&set(a[2])=={x} and set(b[0]).isdisjoint(b[2]);la,lb=legal(a,False),legal(b,False);counts[la,lb]+=1
                if la and lb:
                    assert not legal(a,True) and legal(b,True)
                    if ex is None:ex=dict(rank=i+1,sites=[x,x+1],matched=a,crossed=b)
    print(counts,ex);res=dict(baseline_counts={str(k):v for k,v in counts.items()},example=ex);(Path(__file__).resolve().parents[1]/'results/ramsey_tet_parallel_tracks.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':audit()
