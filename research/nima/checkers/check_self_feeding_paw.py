"""Run the same retained-fiber adapter3 times without per-stage graph fixtures."""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import combinations
import io
import json
import runpy

HERE = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    adapter = runpy.run_path(str(HERE/'check_retained_paw_promotion.py'))
compile_promotion = adapter['compile_promotion']


def inspect(packets):
    vertices = {v for p in packets for v in (p.source,p.target)}
    edges = {tuple(sorted((p.source,p.target))) for p in packets}
    cliques = [vs for vs in combinations(sorted(vertices),4)
               if all(tuple(sorted(pair)) in edges for pair in combinations(vs,2))]
    assert len(packets)==2*len(edges)
    return {'records':len(vertices),'relationships':len(edges),
            'packets':len(packets),'tetrahedra':cliques}


state = {'cycle':0,'packets':adapter['packets'],'previous':None,'receipt':None}
rows = [{'cycle':0,**inspect(state['packets'])}]
for _ in range(3):
    next_cycle = state['cycle']+1
    fibers,links,packets = compile_promotion(state['packets'],generation=next_cycle)
    old_ids = {p.id:p for p in state['packets']}
    assert {p.id:p for f in fibers.values() for p in f['members']}==old_ids
    assert all(w in old_ids for link in links for w in link['source_packet_witnesses'])
    assert not ({p.id for p in packets} & set(old_ids))
    state = {'cycle':next_cycle,'packets':packets,'previous':state,
             'receipt':{'fibers':fibers,'links':links}}
    rows.append({'cycle':state['cycle'],**inspect(state['packets'])})

assert [(r['records'],r['relationships'],r['packets']) for r in rows]==[
    (4,4,8),(4,5,10),(5,8,16),(8,18,36)]
assert [len(r['tetrahedra']) for r in rows]==[0,0,0,1]
# Recover each actual prior stage, all the way to the initial eight packet IDs.
current = state
seen_ids = set()
while current['previous'] is not None:
    ids = {p.id for p in current['packets']}
    assert not (seen_ids & ids)
    seen_ids |= ids
    assert current['cycle']==current['previous']['cycle']+1
    current = current['previous']
assert current['packets']==adapter['packets']
assert len(current['packets'])==8

report = {'status':'passed','cycles':rows,
          'checks':['single repeated constructor','cycle-qualified generated packet IDs',
                    'generated endpoint maps and ordering','all lower packet identities retained',
                    'real endpoint witnesses','independent combinatorial agreement at every step',
                    'first tetrahedron at promotion3'],
          'scope':'Three self-fed promotions of the explicit shared-endpoint rule; no particle identification.'}
(HERE.parent/'results/self-feeding-paw.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
