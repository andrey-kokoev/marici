"""Compare checkpoint section replay with fresh verification; refusal controls."""
from pathlib import Path
from copy import deepcopy
import json
from section_checkpoint import Session,initial_state,verify
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 packet=json.loads((OUT/'polyhedral-common-section.json').read_text())
 # Keep only the proof data consumed by this contract; no producer claims.
 packet={k:packet[k] for k in ('public_vertices','triangles','fine_rows','vertex_source_lifts')}
 s=Session();state=initial_state();receipt=s.bootstrap(state,packet);bootstrap=deepcopy(receipt)
 rejected=[];trace=[]
 def reject(name,call):
  try:call()
  except (ValueError,AssertionError,PermissionError):rejected.append(name)
  else:raise AssertionError(name+' accepted')
 # Caller mutations cannot affect the trusted checkpoint snapshot.
 state['frames'].append({'normal':['0','0'],'upper':'-1'})
 receipt['state']['capabilities']['archive']=True
 before=initial_state();handle=receipt['handle'];packet0=deepcopy(packet)
 packet['vertex_source_lifts'][0][0]='-1'
 s.lift(handle,['0','0']);packet=packet0
 for row in ({'normal':['1','1'],'upper':'3/2'},{'normal':['-1','0'],'upper':'-1/4'},{'normal':['0','0'],'upper':'-1'}):
  op={'kind':'append-public','row':row};after=deepcopy(before);after['frames'].append(row)
  candidate={'state':after,'section':deepcopy(packet)}
  bad=deepcopy(candidate);bad['section']['vertex_source_lifts'][0][0]='-1'
  reject('altered-vertex',lambda:s.advance(handle,before,op,bad))
  bad=deepcopy(candidate);bad['state']['capabilities']['archive']=True
  reject('capability-escalation',lambda:s.advance(handle,before,op,bad))
  bad=deepcopy(candidate);bad['section']['triangles'].pop()
  reject('missing-cover-cell',lambda:s.advance(handle,before,op,bad))
  reject('hidden-refinement',lambda:s.advance(handle,before,{'kind':'append-fine','row':row},candidate))
  reject('foreign-handle',lambda:s.advance('foreign',before,op,candidate))
  reject('false-predecessor',lambda:s.advance(handle,initial_state() if before!=initial_state() else after,op,candidate))
  _,full=verify(after,packet);new=s.advance(handle,before,op,candidate)
  assert new['work']['local_hits']==4 and new['work']['local_checks']==0 and full['local_checks']==4
  old_handle=handle
  reject('stale-handle',lambda:s.advance(old_handle,before,op,candidate))
  reject('archive-request',lambda:s.reexpose(new['handle']))
  trace.append({'state':after,'checkpoint_work':new['work'],'full_replay_work':full,'bytes':new['bytes']})
  before=after;handle=new['handle']
  if row['upper']!='-1':
   s.lift(handle,['1/2','1/2'])
   reject('excluded-lift',lambda:s.lift(handle,['1','1']))
  else:reject('empty-domain-lift',lambda:s.lift(handle,['1/2','1/2']))
 report={'passed':True,'bootstrap_work':bootstrap['work'],'transitions':trace,
 'rejection_count':len(rejected),'rejections':rejected,
 'scope':'Fixed square-section checkpoint adapter. Full replay uses the same exact kernel; no migration issuance, generic domain triangulation, archive service or Nima backend integration.'}
 (OUT/'section-checkpoint.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'transitions':3,'successor_local_checks':0,'successor_local_hits':12,'full_successor_local_checks':12,'rejections':len(rejected)},indent=2))
if __name__=='__main__':main()
