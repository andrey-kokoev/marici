"""Identical inequalities at different row slots have different packet occurrence traces."""
from hashlib import sha256
from pathlib import Path
import json
rows=({'id':'row-A','normal':(1,0),'bound':1},{'id':'row-B','normal':(1,0),'bound':1})
P=(1,0);Q=(0,1)
def proof(m):return (tuple(sum(m[i]*rows[i]['normal'][j] for i in range(2)) for j in (0,1)),sum(m[i]*rows[i]['bound'] for i in range(2)))
def H(x):return sha256(repr(x).encode()).hexdigest()
assert proof(P)==proof(Q)==((1,0),1)
assert H({'weights':P,'row_ids':tuple(r['id'] for r in rows)})!=H({'weights':Q,'row_ids':tuple(r['id'] for r in rows)})
renamed=(dict(rows[0],id='row-A-new'),rows[1])
assert H({'weights':P,'row_ids':tuple(r['id'] for r in rows)})!=H({'weights':P,'row_ids':tuple(r['id'] for r in renamed)})
report={'passed':True,'duplicate_rows':'two x<=1 inequalities with distinct row occurrence IDs','one_row_proofs':'same implied normal/bound','packet_identity':'different multiplier slot binding; renaming used row changes identity','scope':'Local mathematical row fixture, not observed row publication or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/duplicate-row-packet-slots.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
