"""Reverting matrix bytes creates fresh local proof/edge occurrences at new generation."""
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
changed=old[:3]+(((0,1),2),)
H=lambda x:sha256(repr(x).encode()).hexdigest()
assert H(old)!=H(changed)
first={'generation':1,'rows':old,'packet_id':'P-g1','edge_id':'E-g1','issuer':None}
second={'generation':2,'rows':changed,'packet_id':'P-g2','edge_id':'E-g2','issuer':None}
third={'generation':3,'rows':old,'packet_id':'P-g3','edge_id':'E-g3','issuer':None}
def validate(v):
 rows=v['rows'];m=(0,1,0,0);c=1
 return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==(1,0) and sum(rows[i][1]*m[i] for i in range(4))+c==2
assert all(map(validate,(first,second,third)))
assert H(first['rows'])==H(third['rows']) and first['generation']!=third['generation']
assert len({v['packet_id'] for v in (first,second,third)})==3 and len({v['edge_id'] for v in (first,second,third)})==3
assert all(v['issuer'] is None for v in (first,second,third))
report={'passed':True,'math_source':'generation1 and3 ordered matrix digests equal','fresh_generation':'3, distinct from old1','fresh_catalogue':'new packet and edge occurrence IDs with local x<=2 proof rechecked','issuer':'None; no grant inherited','scope':'In-memory reversion fixture only, not persisted edit or validated comparison-edge semantics.'}
out=Path(__file__).resolve().parents[1]/'results/source-reversion-catalogue.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
