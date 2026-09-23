"""Four-case replay needs distinct mathematical, path, identity and owner accounts."""
from copy import deepcopy
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
yedit=(old[0],old[1],old[2],(old[3][0],2))
coupled=(((-1,0),-2),((1,0),2),((0,-1),-1),((0,1),1))
P=(1,2,0,0);Q=(0,1,1,1)
record={'old_rows':old,'current_rows':yedit,'source_binding':old,'P':P,'Q':Q,
        'edge_plan':('P','Q','P'),'target':((1,0),2),'owner_registry_observation':'no_admitted_owner_in_this_local_fixture'}
def image(m,rows):return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))
def replay(r):
 mandatory=('old_rows','current_rows','source_binding','P','Q','edge_plan','target')
 for key in mandatory:
  if key not in r:return 'MISSING_'+key.upper()
 if r['edge_plan']!=('P','Q','P'):return 'UNSUPPORTED_EDGE_PLAN'
 if any(image(r[k],r['old_rows'])!=r['target'] for k in ('P','Q')):return 'INVALID_OLD_PROOF'
 delta=tuple(r['Q'][i]-r['P'][i] for i in range(4))
 if image(delta,r['old_rows'])!=((0,0),0):return 'INVALID_OLD_SYZYGY'
 endpoint=image(r['P'],r['current_rows'])==r['target']
 path=endpoint and image(r['Q'],r['current_rows'])==r['target'] and image(delta,r['current_rows'])==((0,0),0)
 bound=r['source_binding']==r['current_rows']
 owner='UNKNOWN_UNATTESTED' if 'owner_registry_observation' not in r else 'NO_ADMITTED_OWNER_IN_LOCAL_FIXTURE'
 return {'endpoint':endpoint,'path':path,'bound':bound,'owner':owner}
assert replay(record)=={'endpoint':True,'path':False,'bound':False,'owner':'NO_ADMITTED_OWNER_IN_LOCAL_FIXTURE'}
assert replay({**record,'current_rows':coupled})['path'] is True
assert replay({**record,'current_rows':coupled,'source_binding':coupled})['bound'] is True
for key in ('old_rows','current_rows','source_binding','P','Q','edge_plan','target'):
 reduced={k:v for k,v in record.items() if k!=key}
 assert replay(reduced)=='MISSING_'+key.upper()
assert replay({k:v for k,v in record.items() if k!='owner_registry_observation'})['owner']=='UNKNOWN_UNATTESTED'
assert replay({**record,'Q':(0,1,1,2)})=='INVALID_OLD_PROOF'
assert replay({**record,'edge_plan':('P','P')})=='UNSUPPORTED_EDGE_PLAN'
report={'passed':True,'mandatory_accounts':['old_rows','current_rows','source_binding','P','Q','edge_plan','target'],'edge_syzygy':'recomputed from Q-P; no separate vector required for this deterministic two-edge workload','owner_account':'omission yields UNKNOWN_UNATTESTED, never permission','omission_controls_checked':8,'mutation_controls_checked':2,'scope':'Workload-relative fields in one direct encoding. No universal storage lower bound, independently authenticated owner registry, measured memory or real authorization.'}
out=Path(__file__).resolve().parents[1]/'results/bounded-replay-retention.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
