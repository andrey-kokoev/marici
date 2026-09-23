"""Candidate row edits are validated against complete staged catalogue before commit."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
staged=old[:3]+(((0,1),2),)
P=(Q(1),Q(2),Q(0),Q(0));R=(Q(0),Q(1),Q(1),Q(1));single=(Q(0),Q(1),Q(0),Q(0))
old_catalogue={'P':(P,Q(0)),'Q':(R,Q(0)),'single':(single,Q(1))}
def H(x):return sha256(repr(x).encode()).hexdigest()
def valid(rows,packet):
 m,c=packet
 return min((*m,c))>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==(Q(1),Q(0)) and sum(rows[i][1]*m[i] for i in range(4))+c==Q(2)
def commit(store,candidate,catalogue,candidate_id):
 if candidate_id in store['candidate_ids']:return store,'IDEMPOTENT_NO_CHANGE'
 if not all(valid(candidate,p) for p in catalogue.values()):return store,'REJECTED_KEEP_OLD_GENERATION'
 next_store={'generation':store['generation']+1,'rows':candidate,'catalogue':catalogue,'candidate_ids':store['candidate_ids']|{candidate_id}}
 return next_store,'LOCAL_MATH_COMMITTED_NO_AUTHORITY'
store={'generation':1,'rows':old,'catalogue':old_catalogue,'candidate_ids':set()}
assert all(valid(old,x) for x in old_catalogue.values())
rejected,status=commit(store,staged,old_catalogue,'candidate-y-upper-2')
assert rejected is store and status=='REJECTED_KEEP_OLD_GENERATION' and H(store['rows'])==H(old)
rebuilt={'P':old_catalogue['P'],'Q_reproved':(single,Q(1)),'single':old_catalogue['single']}
accepted,status=commit(store,staged,rebuilt,'candidate-y-upper-2-rebuilt')
assert status=='LOCAL_MATH_COMMITTED_NO_AUTHORITY' and accepted['generation']==2 and accepted['rows']==staged
assert store['generation']==1 and store['catalogue']==old_catalogue and H(store['rows'])==H(old)
repeat,status=commit(accepted,staged,rebuilt,'candidate-y-upper-2-rebuilt')
assert repeat is accepted and status=='IDEMPOTENT_NO_CHANGE'
report={'passed':True,'strict_old_catalogue':'REJECTED_KEEP_OLD_GENERATION','old_digest_unchanged':H(store['rows']),'rebuilt_catalogue':'LOCAL_MATH_COMMITTED_NO_AUTHORITY at generation2','duplicate_candidate':'IDEMPOTENT_NO_CHANGE','scope':'Pure in-memory local math transaction; no persisted source mutation, signer, grant, Site update or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/local-source-edit-transaction.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
