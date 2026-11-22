"""See frozen protocol; the oracle quartet is compared only after axis selection."""
from itertools import permutations,combinations
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent;V='ABCD'
def axis(e):return tuple(sorted((''.join(sorted(e)),''.join(sorted(set(V)-set(e))))))
axes=set(map(axis,combinations(V,2)))
def predict(events):
    seen={axis(e) for e in events[:2]};assert len(seen)==2;return (axes-seen).pop()
rows=[];stats=Counter()
for b in json.loads((D/'ramsey_folded_entry_handoff.json').read_text()):
    p=b['binding'];target=axis(p[1:3]);assert target==axis((p[0],p[3]))
    for row in b['rows']:
        e=row['receipt'][:2];y=predict(e);stats['rows']+=1;stats['first_matches']+=axis(e[0])==target;stats['missing_matches']+=y==target
        for h in permutations(V):
            rename=lambda x:''.join(h[V.index(v)] for v in x);assert predict(list(map(rename,e)))==axis(rename(y[0]))==axis(rename(p[1:3]));stats['transported']+=1
        rows.append(dict(binding=p,prefix=row['prefix'],first_events=e,omitted=y));
# Actual seven-label chart: axis exchange fixed one block. Derive its complement without reading S.
blocks=[(0,1),(2,3),(4,5)];swap=(0,1,4,5,2,3,6);fixed=[t for t in blocks if {swap[i] for i in t}==set(t)];assert len(fixed)==1;pred=sorted(set(range(6))-set(fixed[0]));oracle=json.loads((D/'ramsey_seven_transport_synthesis.json').read_text())['addresses'];assert [sum(1<<i for i in pred)]==[s for s in oracle if s.bit_count()==4];maps=list(permutations(blocks));hits=sum(m[0]==fixed[0] for m in maps);r=dict(counts=stats,rows=rows,chart_prediction=pred,unbound_axis_bijections=[hits,len(maps)],scope='physical missing axis matches row; chart match requires row-intertwining bridge');print(r);(D/'ramsey_boundary_quartet_blind.json').write_text(json.dumps(r,indent=2)+'\n')
