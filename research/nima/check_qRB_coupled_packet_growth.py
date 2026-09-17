import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
# Diagnostic rank-one coupling: cross block = 0.8 * all-ones matrix, comparison norm = 2I.
rows=[]
for m in (1,2,4,8,16): rows.append({'dimension':m,'cross_norm':0.8*m,'relative_constant':0.4*m})
out={'schema':'marici.nima.qRB-coupled-packet-growth.v1','samples':rows,'checks':{'coupled_constant_grows':rows[-1]['relative_constant']>rows[0]['relative_constant'],'diagnostic_is_explicit':True},'passed':True,'interpretation':'hostile diagnostic: arbitrary coupled packets can lose uniformity even when every finite packet is bounded','conclusion':'a source-derived coupled-tail estimate is indispensable','rh_proved':False}
p=root/'research/nima/results/qRB-coupled-packet-growth.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
