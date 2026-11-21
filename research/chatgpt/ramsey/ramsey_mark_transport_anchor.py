"""Resolve the fivefold marking ambiguity by explicit anchors; distinguish selected-duad exchange from preservation of full old boundary flags."""
from pathlib import Path
import json
D=Path(__file__).parent
transports=json.loads((D/'ramsey_row_center_calculus.json').read_text())['mark_transports'];f={int(k):v for k,v in json.loads((D/'ramsey_center_transfer_seed_binding.json').read_text())['affine_to_catalogue'].items()};back={v:k for k,v in f.items()};pc=json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[1]['unique_C5_generator'];p=[back[pc[f[i]]] for i in range(22)];orbit=[];v=7
while v not in orbit:orbit.append(v);v=p[v]
assert len(orbit)==5 and 14 in orbit;coord={v:i for i,v in enumerate(orbit)};rows=[]
for t in transports:
 K=t['permutation'];c=coord[K[7]];assert all(coord[K[v]]==(c-i)%5 for i,v in enumerate(orbit));rows.append({'phase':t['phase'],'reflection_constant':c,'fix_entry':K[7]==7,'fix_exit':K[14]==14,'exchange_selected_duads':K[7]==14 and K[14]==7,'transported_entry':{'selected':K[7],'partition':sorted(K[v] for v in [7,17,20])},'transported_exit':{'selected':K[14],'partition':sorted(K[v] for v in [11,14,16])}})
for criterion in ('fix_entry','fix_exit','exchange_selected_duads'):assert sum(r[criterion] for r in rows)==1
assert not any(r['fix_entry'] and r['fix_exit'] for r in rows)
result={'cyclic_orbit_of_selected_duads':orbit,'exit_coordinate':coord[14],'transport_options':rows};(D/'ramsey_mark_transport_anchor.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
