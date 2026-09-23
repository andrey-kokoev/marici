"""Three independent checks: endpoint, path, source binding; authority separate."""
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
y_edit=(old[0],old[1],old[2],(old[3][0],2))
coupled=(((-1,0),-2),((1,0),2),((0,-1),-1),((0,1),1))
P=(1,2,0,0);Q=(0,1,1,1);K=tuple(Q[i]-P[i] for i in range(4))
def digest(r):return sha256(repr(r).encode()).hexdigest()
def image(v,rows):return tuple(sum(rows[i][0][j]*v[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*v[i] for i in range(4))
def inspect(rows,record_root):
 ep=image(P,rows)==((1,0),2)
 path=ep and image(Q,rows)==((1,0),2) and image(K,rows)==((0,0),0)
 identity=record_root==digest(rows)
 return {'endpoint_math':ep,'path_math':path,'record_bound_to_current_source':identity,
         'historical_old_source_math':True,'live_authority':False}
old_root=digest(old)
normal=inspect(old,old_root);broken=inspect(y_edit,digest(y_edit));stale=inspect(coupled,old_root);rebound=inspect(coupled,digest(coupled))
assert (normal['endpoint_math'],normal['path_math'],normal['record_bound_to_current_source'])==(True,True,True)
assert (broken['endpoint_math'],broken['path_math'],broken['record_bound_to_current_source'])==(True,False,True)
assert (stale['endpoint_math'],stale['path_math'],stale['record_bound_to_current_source'])==(True,True,False)
assert (rebound['endpoint_math'],rebound['path_math'],rebound['record_bound_to_current_source'])==(True,True,True)
assert all(not x['live_authority'] for x in (normal,broken,stale,rebound))
def protected_action(status):
 if not status['path_math']:return 'REFUSE_INVALID_PATH'
 if not status['record_bound_to_current_source']:return 'REFUSE_FOREIGN_SOURCE_RECORD'
 if not status['live_authority']:return 'REFUSE_NO_OWNER_CAPABILITY'
 raise AssertionError('this locally assumed test cannot grant owner authority')
assert protected_action(broken)=='REFUSE_INVALID_PATH'
assert protected_action(stale)=='REFUSE_FOREIGN_SOURCE_RECORD'
assert protected_action(rebound)=='REFUSE_NO_OWNER_CAPABILITY'
report={'passed':True,'old_source':normal,'y_high_edit':broken,'coupled_edit_old_record':stale,'coupled_edit_reverified_record':rebound,'refusals':['REFUSE_INVALID_PATH','REFUSE_FOREIGN_SOURCE_RECORD','REFUSE_NO_OWNER_CAPABILITY'],'scope':'Four finite mathematical/local-binding cases. digest equality does not authenticate owner; no real source migration or grant.'}
out=Path(__file__).resolve().parents[1]/'results/path-identity-authority-gate.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
