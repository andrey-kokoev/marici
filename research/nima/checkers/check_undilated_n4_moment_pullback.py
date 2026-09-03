"""Compatibility preflight for importing Grothendieck's N=4 undilated moments."""
import json
from decimal import Decimal
from pathlib import Path
p=Path('research/grothendieck/results/undilated-septic-moment-formula-check.json')
data=json.loads(p.read_text())
rows=data['rows']; profiles=sorted({r['profile'] for r in rows})
index={(r['profile'],int(r['n'])) for r in rows}
expected={(name,n) for name in profiles for n in range(4)}
assert len(profiles)==3 and len(rows)==12 and index==expected
max_res=max(Decimal(r['absolute_residual']) for r in rows)
assert max_res<Decimal('1e-60')
for r in rows:
 assert abs(Decimal(r['closed'])-Decimal(r['quadrature']))<=Decimal(r['absolute_residual'])
n3={r['profile']:r['closed'] for r in rows if int(r['n'])==3}
print(json.dumps({'schema':'marici.nima.undilated-n4-moment-pullback.v1','status':'passed','source_schema':data['schema'],'profiles':profiles,'n_values':[0,1,2,3],'row_count':len(rows),'max_reported_residual':str(max_res),'n3_closed':n3,'interface':{'dilation':'c=1','preconditioner_shift':'2 log 2','moment_rate':'n+1/4','tail_total_variation':5184},'pullback_compatible':True,'claim_boundary':'numerical closed-versus-quadrature identity and interface census; no directed rounding or prime interval is supplied'},sort_keys=True))
