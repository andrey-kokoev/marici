"""Finite execution of the typed reciprocal-fiber promotion adapter.

Checks source membership, actual endpoint witnesses, next-packet construction,
all original IDs, and agreement with independent line-graph incidence.
"""
from dataclasses import dataclass, replace
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json

@dataclass(frozen=True)
class Packet:
    id: str
    label: str
    source: str
    target: str


def compile_promotion(packets, generation=1):
    unique = {}
    for packet in packets:
        if packet.id in unique and unique[packet.id] != packet:
            raise ValueError('conflicting values for one packet identity')
        unique[packet.id] = packet
    groups = defaultdict(list)
    for p in unique.values(): groups[p.label].append(p)
    fibers = {}
    for label, members in sorted(groups.items()):
        if len(members) != 2: raise ValueError('reciprocal fiber must have two members')
        p,q = members
        if p.source == p.target or (p.source,p.target)!=(q.target,q.source):
            raise ValueError('fiber members must be opposite directions')
        fibers[label] = {'members':tuple(members),'endpoints':tuple(sorted((p.source,p.target)))}
    assert {p.id:p for f in fibers.values() for p in f['members']} == unique
    # Fiber over the shared endpoint: form ordered pairs only within that fiber.
    incidence = defaultdict(list)
    for label, fiber in fibers.items():
        for endpoint in fiber['endpoints']: incidence[endpoint].append(label)
    links = []
    for endpoint, labels in sorted(incidence.items()):
        for left,right in combinations(sorted(labels),2):
            # These retained leaf IDs witness each side's incidence.
            witnesses = tuple(next(p.id for p in fibers[e]['members'] if p.source==endpoint)
                              for e in (left,right))
            assert all(unique[p].source==endpoint for p in witnesses)
            links.append({'left':left,'right':right,'shared':endpoint,
                          'source_packet_witnesses':witnesses})
    pairs = {(r['left'],r['right']) for r in links}
    assert len(pairs)==len(links), 'parallel source edges need a richer rule'
    # Independent oracle: compare old edge endpoint sets, not incidence fibers.
    oracle = {(a,b) for a,b in combinations(sorted(fibers),2)
              if set(fibers[a]['endpoints']) & set(fibers[b]['endpoints'])}
    assert pairs == oracle
    next_packets = []
    for i,link in enumerate(sorted(links,key=lambda r:(r['left'],r['right']))):
        a,b=link['left'],link['right']
        for direction,(s,t) in enumerate(((a,b),(b,a))):
            next_packets.append(Packet(f'cycle{generation}:{i}:{direction}',f'cycle{generation}:{i}',s,t))
    return fibers,links,next_packets

ends = {'AB':('A','B'),'AC':('A','C'),'BC':('B','C'),'AD':('A','D')}
packets = [Packet(f'{e}:{direction}',e,s,t) for e,(a,b) in ends.items()
           for direction,(s,t) in enumerate(((a,b),(b,a)))]
fibers,links,next_packets = compile_promotion(packets)
assert len(packets)==8 and len(fibers)==4 and len(links)==5 and len(next_packets)==10
assert {(r['left'],r['right'],r['shared']) for r in links} == {
    ('AB','AC','A'),('AB','AD','A'),('AB','BC','B'),('AC','AD','A'),('AC','BC','C')}
# No invented connection between disjoint BC and AD.
assert not any({r['left'],r['right']}=={'BC','AD'} for r in links)
# Aliasing an existing input identity does not create an extra packet or fiber.
assert compile_promotion(packets+[packets[0]]) == (fibers,links,next_packets)
try:
    compile_promotion(packets+[replace(packets[0],target='D')])
except ValueError: pass
else: raise AssertionError('conflicting packet alias accepted')
try:
    compile_promotion([p for p in packets if p.id!='AB:1'])
except ValueError: pass
else: raise AssertionError('missing reverse packet accepted')
# The generated ten packets really feed a subsequent promotion.
next_fibers,next_links,_ = compile_promotion(next_packets, generation=2)
assert len(next_fibers)==5 and len(next_links)==8

result = {'status':'passed','input_packet_count':len(packets),
          'retained_fibers':{key:[p.id for p in value['members']] for key,value in fibers.items()},
          'generated_connections':links,'next_packet_count':len(next_packets),
          'following_promotion':{'records':len(next_fibers),'relationships':len(next_links)},
          'checks':['exact original-ID recovery','real shared-endpoint witnesses',
                    'independent line-graph agreement','duplicate-reference invariance',
                    'conflicting-ID rejection','missing-reverse rejection','next-input execution'],
          'scope':'Explicit new promotion rule implemented through retained fibers; not inferred from normalization.'}
HERE = Path(__file__).resolve().parents[1]
(HERE/'results/retained-paw-promotion.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
