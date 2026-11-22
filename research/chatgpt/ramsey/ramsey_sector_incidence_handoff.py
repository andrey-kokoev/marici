"""Frozen row-blind geometric bridge and paired indistinguishability control."""
from itertools import combinations,permutations,product
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent;load=lambda p:json.loads(p.read_text());V='ABCD';tri=[r['triangle'] for r in load(D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json')['triangles_and_transports']];points=sorted(set(sum(tri,[])));line=lambda s:s if s in V else next(v for v in V if v not in s[2:]);axis=lambda e:frozenset((frozenset(e),frozenset(set(V)-set(e))));axes={axis(e) for e in combinations(V,2)};data=load(D/'ramsey_folded_entry_handoff.json');duads={tuple(c) for c in combinations(range(7),2)}-{(0,1),(2,3),(4,5)};counts=Counter();example={};runs=0;checks=0
for rec in data:
 for r in rec['rows']:
    events=r['receipt'][:2];missing,=axes-{axis(e) for e in events}
    for s in points:
        v=line(s);edge,=[e for e in missing if v in e];tip,=edge-{v};sector,=[t for t in tri if (t[0]==s or t[1]==s) and t[2]==tip];runs+=1;local=Counter();others=sorted(set(V)-{v})
        for perm in permutations(others):
            for flips in product(range(2),repeat=3):
                ids=[z for w,f in zip(perm,flips) for z in sorted(x for x in points if line(x)==w)[::1-2*f]]+[s];assert {p for p in combinations(range(7),2) if line(ids[p[0]])!=line(ids[p[1]])}==duads
                pred=''.join(str(i) for i in range(6) if line(ids[i])!=tip);local[pred]+=1;checks+=1
                if runs==1:example.setdefault(pred,dict(events=events,singleton=s,sector=sector,chart_to_point=ids))
        assert set(local.values())=={16} and len(local)==3;counts.update(local)
oracle,=[m for m in load(D/'ramsey_seven_transport_synthesis.json')['addresses'] if m.bit_count()==4];truth=''.join(str(i) for i in range(7) if oracle>>i&1);out=dict(physical_cases=runs,labeled_cases=checks,predictions=counts,held_out=truth,matched=counts[truth],control=example);print(out);(D/'ramsey_sector_incidence_handoff.json').write_text(json.dumps(out,indent=2)+'\n')
