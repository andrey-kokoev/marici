"""Read both anchored 3|7 splits from star incidence alone; hold out induced red links."""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).resolve().parents[1]/'results';r=json.loads((D/'ramsey_37_dual_stars.json').read_text());systems=[[set(s) for s in stars] for stars in r['stars']];M=set.union(*systems[0]);assert len(M)==10 and set.union(*systems[1])==M
rows=[];pred=set()
for v in sorted(M):
    triples=[]
    for stars in systems:
        incident=[s for s in stars if v in s];assert len(incident)==2
        t=M-set.union(*incident);assert len(t)==3;triples.append(t)
    common=set.intersection(*triples);assert len(common)==2
    pred.update(tuple(sorted((u,v))) for u in common);rows.append(dict(anchor=v,triples=[sorted(t) for t in triples],common=sorted(common)))
actual={tuple(sorted(e)) for e in r['red_edges'] if set(e)<=M};assert pred==actual
print(f'{len(rows)} anchors; {len(actual)} red out of {len(list(combinations(M,2)))} distinct middle pairs')
(D/'ramsey_37_anchored_pair_split.json').write_text(json.dumps(rows,indent=2)+'\n')
