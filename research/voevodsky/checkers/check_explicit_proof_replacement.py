"""Rebased proof replacement needs new packet and comparison-edge identities."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
rows=(((-1,0),Q(0)),((1,0),Q(7,4)),((0,-1),Q(0)),((0,1),Q(7,4)))
old_q={'id':'Q-old','weights':(Q(0),Q(1),Q(1),Q(1)),'surplus':Q(1)}
old_single={'id':'S-old','weights':(Q(0),Q(1),Q(0),Q(0)),'surplus':Q(2)}
new_q={'id':'Q-new','weights':(Q(0),Q(1),Q(0),Q(0)),'surplus':Q(5,4)}
new_single={'id':'S-new','weights':(Q(0),Q(1),Q(0),Q(0)),'surplus':Q(5,4)}
def valid(p):
 m=p['weights'];c=p['surplus']
 return min((*m,c))>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==(Q(1),Q(0)) and sum(rows[i][1]*m[i] for i in range(4))+c==Q(3)
assert not valid(old_q) and not valid(old_single) and valid(new_q) and valid(new_single)
old_edge={'id':'edge-old','source':'S-old','target':'Q-old'}
new_edge={'id':'edge-new','source':'S-new','target':'Q-new'}
def edge_ok(edge,packets):
 if edge['source'] not in packets or edge['target'] not in packets:raise ValueError('EDGE_ENDPOINT_ID_STALE')
 a=packets[edge['source']];b=packets[edge['target']]
 if not valid(a) or not valid(b):raise ValueError('EDGE_ENDPOINT_PACKET_INVALID')
 return True
new_catalogue={p['id']:p for p in (new_q,new_single)}
try:edge_ok(old_edge,new_catalogue)
except ValueError as err:assert str(err)=='EDGE_ENDPOINT_ID_STALE'
else:raise AssertionError('old history edge carried')
assert edge_ok(new_edge,new_catalogue)
assert new_edge['id']!=old_edge['id']
report={'passed':True,'rebased_source_digest':sha256(repr(rows).encode()).hexdigest(),'old_Q_and_S':'invalid on combined row source','replacement_Q_and_S':'new IDs, x-upper multiplier1 surplus5/4 prove x<=3','old_edge':'EDGE_ENDPOINT_ID_STALE','new_edge':'new edge ID with revalidated endpoints, not same old history','scope':'In-memory local math replacement; no actual row-source editing, signed owner grant, or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/explicit-proof-replacement.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
