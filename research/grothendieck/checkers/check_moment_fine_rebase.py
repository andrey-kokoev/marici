"""Authorized fine-rebase controls, independent replay, and nonlocal repair."""
from fractions import Fraction as Q
from pathlib import Path
import json,copy,hashlib
from moment_fine_rebase import RebaseSession,solve,compress,propose
from verify_moment_fine_rebase import successor,from_answer,verify_rebase,closure_potential,data,admitted
from moment_column_checkpoints import encode
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
class OwnerApprovals:
 # Test owner authority, not candidate-supplied provenance or archive import.
 def __init__(self):self.records=[]
 def admit(self,event,before,operation):
  token=object();self.records.append((token,event,encode(before),encode(operation),encode(successor(before,operation))));return token
 def check(self,event,before,operation,after,token):
  return any(t is token and e is event and b==encode(before) and o==encode(operation) and a==encode(after) for t,e,b,o,a in self.records)
def reject(f):
 try:f()
 except (AssertionError,IndexError,KeyError,ValueError):return
 raise AssertionError('invalid fine rebase accepted')
def edge(b,j,bound):return {'block':b,'tail':None,'head':j,'upper':str(bound)}
owner=OwnerApprovals();initial={'intervals':[[0,3],[3,7]],'objective':['0','0','1','0'],'frames':[]};answer=solve(initial);cp=compress(initial,answer)
session=RebaseSession(initial,answer,cp,owner.check);handle=session.initial_handle;initial_head=session.snapshot(handle);records=[];refusals=0
operations=[edge(0,0,1),edge(0,0,Q(1,2)),edge(0,3,10),edge(1,7,Q(7,2)),edge(1,7,3),edge(0,0,Q(1,3))]
for op in operations:
 head=session.snapshot(handle);candidate=propose(head,op);grant=owner.admit(session.event,head['state'],op)
 reject(lambda:session.advance(handle,head['state'],op,{'self_asserted':'approved'},candidate));refusals+=1
 foreign_grant=owner.admit(object(),head['state'],op);reject(lambda:session.advance(handle,head['state'],op,foreign_grant,candidate));refusals+=1
 bad=copy.deepcopy(candidate);bad['bounds'][0]['flow'][-1]=str(Q(bad['bounds'][0]['flow'][-1])+1);reject(lambda:session.advance(handle,head['state'],op,grant,bad));assert session.snapshot(handle)==head;refusals+=1
 bad=copy.deepcopy(candidate);bad['column_status'][0]='DROP' if bad['column_status'][0]=='KEEP' else 'KEEP';reject(lambda:session.advance(handle,head['state'],op,grant,bad));assert session.snapshot(handle)==head;refusals+=1
 wrong=copy.deepcopy(op);wrong['upper']=str(Q(op['upper'])+1);reject(lambda:session.advance(handle,head['state'],wrong,grant,candidate));refusals+=1
 wrong_before=copy.deepcopy(head['state']);wrong_before['objective'][0]='1';reject(lambda:session.advance(handle,wrong_before,op,grant,candidate));refusals+=1
 for b,bound in enumerate(candidate['bounds']):
  if bound['witness'] is None and head['bounds'][b]['witness'] is not None:
   bad=copy.deepcopy(candidate);bad['bounds'][b]['witness']=head['bounds'][b]['witness'];reject(lambda:session.advance(handle,head['state'],op,grant,bad));refusals+=1;break
 if not records:
  after=successor(head['state'],op);fresh=solve(after,head['columns']);fresh_cp=compress(after,fresh);from_answer(after,fresh,fresh_cp,head['columns'])
  bad=copy.deepcopy(candidate);bad.update(mode='REPAIRED',seeds=head['columns'],reseed=[],answer=fresh,compact=fresh_cp)
  reject(lambda:session.advance(handle,head['state'],op,grant,bad));refusals+=1
 replay=verify_rebase(head,op,candidate);old_handle=handle;handle,receipt=session.advance(handle,head['state'],op,grant,candidate);assert replay==session.snapshot(handle)
 reject(lambda:session.snapshot(old_handle));refusals+=1
 reject(lambda:session.advance(handle,replay['state'],op,grant,candidate));assert session.snapshot(handle)==replay;refusals+=1
 if candidate['mode']=='REPAIRED':
  cold=solve(replay['state']);cold_head=from_answer(replay['state'],cold,compress(replay['state'],cold));assert cold_head['result']['status']==replay['result']['status']
  if replay['result']['status']=='OPTIMUM':assert cold_head['result']['value']==replay['result']['value']
 else:cold=None
 regenerated=sorted({t['added']['block'] for t in candidate.get('answer',{}).get('trace',[]) if 'added' in t and t['added']['block']!=op['block']})
 potential=[closure_potential(head['state']),closure_potential(replay['state'])];assert potential[1]<=potential[0]
 if candidate['mode']=='REPAIRED':assert potential[1]<potential[0]
 records.append({'operation':op,'candidate':candidate,'cold':cold,'receipt':receipt,'unchanged_blocks_regenerated':regenerated,'closure_potential':potential})
 print(op,candidate['mode'],replay['result'].get('value'),receipt['new_master_solves'],regenerated,flush=True)
assert records[0]['candidate']['mode']=='RETAINED_OPTIMUM'
assert records[2]['unchanged_blocks_regenerated']==[1]
assert records[4]['candidate']['mode']=='REPAIRED' and records[4]['receipt']['status']=='INCONSISTENT'
assert records[5]['candidate']['mode']=='INHERITED_INCONSISTENCY'
# Authority-free service cannot execute even a fully valid fine successor.
unauthorized=RebaseSession(initial,answer,cp);op=operations[0];candidate=propose(unauthorized.snapshot(unauthorized.initial_handle),op)
reject(lambda:unauthorized.advance(unauthorized.initial_handle,initial,op,None,candidate));assert unauthorized.snapshot(unauthorized.initial_handle)==initial_head;refusals+=1
# Actual local graph emptiness has a cycle proof, not just an exhausted pool.
local=RebaseSession(initial,answer,cp,owner.check);op=edge(0,0,-1);candidate=propose(local.snapshot(local.initial_handle),op);assert candidate['mode']=='LOCAL_NEGATIVE_CYCLE'
grant=owner.admit(local.event,initial,op);bad=copy.deepcopy(candidate);bad['cycle_edges']=[];reject(lambda:local.advance(local.initial_handle,initial,op,grant,bad));refusals+=1
local_handle,local_receipt=local.advance(local.initial_handle,initial,op,grant,candidate)
# One changed last block forces an unchanged remote first block to regenerate.
remote_state={'intervals':[[0,3],[3,7],[7,11],[11,15]],'objective':['0','0','1','0'],'frames':[]};remote_answer=solve(remote_state);remote_cp=compress(remote_state,remote_answer);remote=RebaseSession(remote_state,remote_answer,remote_cp,owner.check);before=remote.snapshot(remote.initial_handle)
op=edge(3,15,Q(15,2));remote_candidate=propose(before,op);remote_grant=owner.admit(remote.event,remote_state,op);remote_handle,remote_receipt=remote.advance(remote.initial_handle,remote_state,op,remote_grant,remote_candidate)
after=remote.snapshot(remote_handle);assert remote_candidate['mode']=='REPAIRED';added={t['added']['block'] for t in remote_candidate['answer']['trace'] if 'added' in t};assert 0 in added
old_raw=tuple(map(Q,before['result']['source_lift']));new_raw=tuple(map(Q,after['result']['source_lift']))
assert new_raw==tuple(Q(1+j%3)*Q(j,2) for j in range(16)) and all(a>b for a,b in zip(old_raw,new_raw))
print('remote changed block 3; generated blocks',sorted(added),'master solves',remote_receipt['new_master_solves'],flush=True)
# A genuinely moment-coupled query: the U+V frame stays active after a fine
# hidden-atom cap, and an unchanged block must generate new source columns.
raw=tuple(map(Q,initial_head['result']['source_lift']));budget=sum((1+Q(1,128**j))*(v+Q(1+j%3)*Q(j,2))/2 for j,v in enumerate(raw))
coupled_state={**initial,'frames':[{'normal':['1','0','0','0'],'upper':'1/2'},{'normal':['0','0','1','1'],'upper':str(budget)}]}
coupled_answer=solve(coupled_state);coupled_cp=compress(coupled_state,coupled_answer);coupled=RebaseSession(coupled_state,coupled_answer,coupled_cp,owner.check);coupled_before=coupled.snapshot(coupled.initial_handle)
coupled_op=edge(1,5,15);coupled_candidate=propose(coupled_before,coupled_op);coupled_grant=owner.admit(coupled.event,coupled_state,coupled_op);coupled_handle,coupled_receipt=coupled.advance(coupled.initial_handle,coupled_state,coupled_op,coupled_grant,coupled_candidate);coupled_after=coupled.snapshot(coupled_handle)
assert coupled_candidate['mode']=='REPAIRED' and Q(coupled_after['result']['value'])<Q(coupled_before['result']['value'])
for h in (coupled_before,coupled_after):assert sum((1+Q(1,128**j))*Q(v) for j,v in enumerate(h['result']['source_lift']))==budget
assert any(t.get('added',{}).get('block')==0 for t in coupled_candidate['answer']['trace'])
coupled_cold=solve(coupled_after['state']);from_answer(coupled_after['state'],coupled_cold,compress(coupled_after['state'],coupled_cold));assert coupled_cold['value']==coupled_after['result']['value']
print('coupled U+V remains active; hidden fine cap regenerates unchanged block 0; master solves',coupled_receipt['new_master_solves'],flush=True)
fiber_pair=[]
for sign in (-1,1):
 right=tuple(Q(v)+Q(sign,1000)*d for v,d in zip((13,28,45,16,34),(0,1,-129,128,0)));source=data(coupled_state)[1];admitted(source,tuple(v/s for v,s in zip(right,source[1])))
 fiber_pair.append(list(map(str,(Q(0),Q(2),Q(15),*right))))
def observation(raw):
 raw=tuple(map(Q,raw));return (raw[0],raw[-1],sum(raw),sum(Q(1,128**j)*v for j,v in enumerate(raw)))
assert observation(fiber_pair[0])==observation(fiber_pair[1]) and Q(fiber_pair[0][5])>45>Q(fiber_pair[1][5])
# Losing cached columns need not lose the old optimum. The old left priced
# witness is excluded, but a surviving column still attains its flow bound.
replacement=RebaseSession(initial,answer,cp,owner.check);replacement_before=replacement.snapshot(replacement.initial_handle)
replacement_op={'block':0,'tail':3,'head':None,'upper':'-71/2'};replacement_candidate=propose(replacement_before,replacement_op);replacement_grant=owner.admit(replacement.event,initial,replacement_op)
replacement_handle,replacement_receipt=replacement.advance(replacement.initial_handle,initial,replacement_op,replacement_grant,replacement_candidate);replacement_after=replacement.snapshot(replacement_handle)
assert replacement_candidate['mode']=='REPAIRED' and replacement_after['result']['value']==replacement_before['result']['value']
assert replacement_candidate['bounds'][0]['witness'] is not None and replacement_candidate['bounds'][0]['witness']!=replacement_before['bounds'][0]['witness']
print('replacement support witness preserves old optimum after cached-column loss; master solves',replacement_receipt['new_master_solves'],flush=True)
# Full semantic replay has no access to authority objects or producer state.
replayed=from_answer(initial,answer,cp)
for record in records:replayed=verify_rebase(replayed,record['operation'],record['candidate'])
assert replayed==session.snapshot(handle)
report={'schema':'moment-fine-rebase.v1','initial':{'state':initial,'answer':answer,'compact':cp},'records':records,'local_empty':{'operation':edge(0,0,-1),'candidate':candidate,'receipt':local_receipt},'replacement':{'operation':replacement_op,'candidate':replacement_candidate,'receipt':replacement_receipt},'coupled':{'state':coupled_state,'answer':coupled_answer,'compact':coupled_cp,'operation':coupled_op,'candidate':coupled_candidate,'cold':coupled_cold,'receipt':coupled_receipt,'same_observation_fiber_pair':fiber_pair},'remote':{'state':remote_state,'answer':remote_answer,'compact':remote_cp,'operation':op,'candidate':remote_candidate,'receipt':remote_receipt,'generated_blocks':sorted(added)},'counts':{'main_transitions':len(records),'refusals':refusals,'remote_generated_blocks':sorted(added),'owner_approval_records':len(owner.records),'owner_statement_bytes':sum(len(b)+len(o)+len(a) for t,e,b,o,a in owner.records)},'scope':'owner-admitted event/state/operation approvals; fixed chart; no history recovery or archive authentication','bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'moment_fine_rebase.py',HERE/'verify_moment_fine_rebase.py',HERE/'active_cap_moment_master.py',HERE/'verify_active_cap_moment_master.py',HERE/'moment_column_checkpoints.py')}}
(R/'moment-fine-rebase.json').write_bytes(encode(report));print('PASS',report['counts'])
