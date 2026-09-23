"""Live-service resource-aware fixed-base controls.
Snapshots below are verifier-observed service facts, not imported attestations.
"""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import json,gzip,hashlib,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
sys.path.insert(0,str(ROOT/'research/grothendieck/checkers'))
from allocation_continuation_checkpoint import AllocationSession,kernel
from full_segment_checkpoint import FullSegmentSession
from checked_retirement_interface import migrate
G=ROOT/'research/grothendieck/results';N=ROOT/'research/nima/results';OUT=ROOT/'research/voevodsky/results'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def gate(before,after,required):
 # This deliberately sufficient rule checks unchanged support resources.
 # Other implementations could realize a task with a different provider.
 assert before['base']==after['base'] and before['authority']==after['authority']
 for task in required:
  if not before['tasks'].get(task) or not after['tasks'].get(task):raise PermissionError('CAPABILITY_LOSS:'+task)
  for name in before['dependencies'][task]:
   assert name in before['resources'] and before['resources'][name]==after['resources'].get(name)
 return {'fixed_base_for':required,'scope':'Declared tasks, scopes and unchanged trusted providers only.'}
def main():
 # Positive: use a base that actually survives, not the entire old domain.
 plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
 case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
 packet=json.loads((OUT/'full-segment-checkpoint.json').read_text())['section']
 s=FullSegmentSession();boot=s.bootstrap(plan,case,retain_lift=True)
 attachment=s.attach_full_segment(boot['handle'],boot['state'],packet['vertices'],packet)
 sid=attachment['section_id'];base=[['0','0'],['1/2','1/2']]
 for p in base:assert s.covered_lift(attachment['handle'],sid,p)==[p[0],'0','0']
 resources={'section':digest(packet),'fine_context':digest(plan),'source_rule':case['runtime']['source_binding']}
 positive_before={'base':digest(base),'authority':boot['state']['migration_binding'],
  'tasks':{'exact_lift_on_base':True},'dependencies':{'exact_lift_on_base':list(resources)},'resources':resources}
 producer=migrate(plan,case,retain_lift=True);op={'kind':'append-public','normal':['1','0'],'upper':'3/4'}
 # Affine endpoint check certifies all of B remains in the new public frame.
 assert all(Q(p[0])<=Q(op['upper']) for p in base)
 answer=producer.refine(op['normal'],op['upper']).maximize([1,0])
 successor=s.advance(attachment['handle'],attachment['state'],op,[1,0],answer)
 for p in base+[['1/4','1/4']]:assert s.covered_lift(successor['handle'],sid,p)==[p[0],'0','0']
 positive_after=deepcopy(positive_before)
 assert digest(json.loads(s._covers[sid]))==resources['section']
 assert s._state.migration_binding==positive_before['authority']
 positive=gate(positive_before,positive_after,['exact_lift_on_base'])
 # Negative: real attached allocation becomes detached with identical capsule.
 fixture=json.loads((G/'moment-column-checkpoints.json').read_text());record=fixture['records'][0]
 a=AllocationSession();attached=a.bootstrap(record['state'],record['warm'],record['compact'])
 before_replay=a.replay_allocation(attached['handle'])
 assert a.check_new_query(attached['handle'],record['state'],record['warm'])['status']=='OPTIMUM'
 negative_before={'base':attached['capsule_digest'],'authority':'NO_HISTORY_AUTHORITY',
 'tasks':{'replay':True,'fresh_query':True},'dependencies':{'replay':['capsule'],'fresh_query':['capsule','backend']},
 'resources':{'capsule':attached['capsule_digest'],'backend':'live-source-pricing-verifier'}}
 detached=a.detach(attached['handle'],record['state']);assert detached['capsule_digest']==attached['capsule_digest']
 assert a._engine is None and a._engine_handle is None
 negative_after={**negative_before,'tasks':{'replay':True,'fresh_query':False},'resources':{'capsule':detached['capsule_digest']}}
 rejected=[];names=('verify','verify_pricing','block','admitted');saved={name:getattr(kernel,name) for name in names}
 def forbidden(*args,**kwargs):raise RuntimeError('DETACHED_BACKEND_USED')
 try:
  for name in names:setattr(kernel,name,forbidden)
  assert a.replay_allocation(detached['handle'])==before_replay
  try:a.check_new_query(detached['handle'],record['state'],record['warm'])
  except PermissionError:rejected.append('live-new-query-refused')
  else:raise AssertionError('detached query accepted')
 finally:
  for name,fn in saved.items():setattr(kernel,name,fn)
 replay_gate=gate(negative_before,negative_after,['replay'])
 try:gate(negative_before,negative_after,['replay','fresh_query'])
 except PermissionError:rejected.append('full-contract-base-collapse-refused')
 else:raise AssertionError('capability-losing base collapsed')
 # Even a forged positive flag cannot supply the absent trusted provider.
 bad=deepcopy(negative_after);bad['tasks']['fresh_query']=True
 try:gate(negative_before,bad,['fresh_query'])
 except AssertionError:rejected.append('capability-flag-without-provider')
 else:raise AssertionError('missing dependency accepted')
 # Fresh current-kernel replay of the six-exposure obstruction; do not
 # treat an upstream archived report with a changed source hash as current.
 data=kernel.block([0,3]);exposed=[]
 for e in fixture['six_exposures']:
  objective=tuple(map(Q,e['objective']));scales=data[1]
  q=tuple(scales[j]*(objective[0]*int(j==0)+objective[1]*int(j==3)+objective[2]+objective[3]*Q(1,128**j)) for j in range(4))
  potential,upper=kernel.verify_pricing(data,q,e['certificate']);z=potential[1:]
  increments=(z[0],z[1]-z[0],z[2]-z[1],z[3]-z[2]);signs=tuple(map(Q,e['increment_objective']))
  assert q==(signs[0]-signs[1],signs[1]-signs[2],signs[2]-signs[3],signs[3])
  assert all(s in (-1,1) and v==(hi if s==1 else lo) for s,v,lo,hi in zip(signs,increments,(Q(0),Q(1,2),Q(1,2),Q(1,2)),(Q(1),Q(20),Q(20),Q(20))))
  exposed.append((tuple(z),objective,upper))
 assert len(exposed)==6 and len({z for z,o,b in exposed})==6
 objective=exposed[-1][1]
 def score(z):
  raw=[Q(1+j%3)*v for j,v in enumerate(z)]
  obs=(raw[0],raw[-1],sum(raw),sum(Q(1,128**j)*v for j,v in enumerate(raw)))
  return sum(a*b for a,b in zip(objective,obs))
 restricted=max(score(z) for z,o,b in exposed[:5]);full=exposed[-1][2]
 assert restricted==19 and full==20
 report={'passed':True,'fresh_support_gap':{'dictionary':'19','full_source':'20','exposures_verified':6},'positive_section_base':{'before':positive_before,'after':positive_after,'gate':positive},
 'detachment':{'before':negative_before,'after':negative_after,'replay_only_gate':replay_gate,
  'capsule_unchanged':True,'source_entrypoints_trapped':list(names)},'rejections':rejected,
 'scope':'Sufficient resource-aware base rule tested against live verified services. Not universal physical impossibility, arbitrary provider substitution, or proof of deletion.'}
 (OUT/'resource-aware-base.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'positive_fixed_base':True,'detached_replay_base':True,'detached_fresh_query_base':False,'rejections':rejected},indent=2))
if __name__=='__main__':main()
