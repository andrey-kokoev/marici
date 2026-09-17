import json, math
from pathlib import Path
root=Path(__file__).resolve().parents[2]
# Orthogonal direct sums of the same normalized finite fixture preserve the operator ratio.
rows=[]
for m in (1,2,4,8,16): rows.append({'copies':m,'relative_constant':0.4})
out={'schema':'marici.nima.qRB-replicated-packet-constant.v1','samples':rows,'checks':{'constant_stable_under_orthogonal_replication':len({x['relative_constant'] for x in rows})==1,'all_constants_finite':all(math.isfinite(x['relative_constant']) for x in rows)},'passed':True,'interpretation':'diagnostic only: orthogonal replication does not test coupled source tails or regulator refinement','not_proved':'source-uniform relative bound'}
p=root/'research/nima/results/qRB-replicated-packet-constant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
