"""Compare the held-out red link directly with the previously registered probe slots. Also check the older transport algebra's stored Boolean formula for the target slot. No geometric reference or fitted orientation per wiring."""
from pathlib import Path
import json,itertools
D=Path(__file__).resolve().parents[1];S=D.parent/'chatgpt/ramsey';source=json.loads((S/'ramsey_seven_all_wirings.json').read_text());masks=source['address_masks'];edges=list(map(tuple,source['edge_order']));mask=lambda *xs:sum(1<<i for i in xs);slot=lambda a,b:edges.index(tuple(sorted([masks.index(a),masks.index(b)])));target=slot(mask(3,6),mask(2,5));other=slot(mask(3,6),mask(2,4));formula=json.loads((S/'ramsey_seven_transport_algebra.json').read_text())['edge_formulas'];rows=[]
for w in source['wirings']:
 bit=lambda i:(w>>i)&1;assert bit(target)==bit(4)==1-bit(other);rows.append(dict(w=w,probes=[bit(i) for i in (0,4,6)],step=bit(target)))
assert len({tuple(r['probes']) for r in rows})==8;out=dict(step_slot=target,other_slot=other,probe_slot=4,step_formula=formula[target],other_formula=formula[other],least_wiring=min(rows,key=lambda r:r['w']),rows=rows);print(target,other,formula[target],formula[other]);(D/'results/ramsey_red_reference_probe.json').write_text(json.dumps(out,indent=2)+'\n')
