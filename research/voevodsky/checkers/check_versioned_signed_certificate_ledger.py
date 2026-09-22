"""Safe local use of projection/theta/signed task certificates out of order."""
from pathlib import Path
import importlib.util,json,hashlib,copy
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck';OUT=ROOT/'research/voevodsky/results'
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
t=module('task',G/'checkers/three_channel_source_task.py');v=module('verify',G/'certificates/verify_source_task_transition.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p):return json.loads(p.read_text())
R=G/'results';D=R/'portable-source-task-transitions';frozen=load(R/'calibration-refinement-frozen-inputs.json')
task=copy.deepcopy(frozen['cases']['private']['middle_threshold']);binding=digest(task)
specs=[('projection272','three-channel-source-task-calibration-projection272.json','private-middle_threshold-projection272.json'),
 ('theta-taylor','three-channel-source-task-calibration-theta-taylor.json','private-middle_threshold-theta-taylor.json'),
 ('signed-pairing','three-channel-source-task-calibration-signed-pairing.json','private-middle_threshold-signed-pairing.json')]
versions=[]
for rank,(name,calname,chainname) in enumerate(specs):
 cal=R/calname;chain=D/chainname;content=load(cal);c=load(chain);v.verify(c)
 engine=t.SourceTask(cal);result=engine.certify(task);last=c['nodes'][-1];cert=c['certificates'][-1]
 assert last['evidence']['calibration']==sha(cal) and cert['status']==result['status']
 if rank:
  parent=R/content['parent_calibration_file'];assert content['parent_calibration_sha256']==sha(parent)
  edge=c['edges'][-1];assert edge['kind']=='identity-calibration-refinement'
  assert edge['old_sha256']==v.sha(c['nodes'][-2]) and edge['new_sha256']==v.sha(last)
 else: parent=None
 envelope={'schema':'marici.versioned-source-task-certificate.v1','task_binding':binding,'rank':rank,'version':name,
  'calibration_sha256':sha(cal),'parent_calibration_sha256':None if parent is None else sha(parent),
  'chain_sha256':sha(chain),'chain_terminal_problem_sha256':v.sha(last),'status':result['status'],
  'necessary_cost':result['necessary_moment_cost_lower_bound']}
 envelope['envelope_sha256']=digest(envelope);versions.append(envelope)
assert [x['status'] for x in versions]==['UNRESOLVED','UNRESOLVED','CERTIFIED_INFEASIBLE']
# The admission set is closed: acceptance always replays source arithmetic and
# portable ancestry, rather than trusting rank labels or an asserted outcome.
def verify_envelope(x):
 y=dict(x);claimed=y.pop('envelope_sha256');assert claimed==digest(y)
 assert y['schema']=='marici.versioned-source-task-certificate.v1' and y['task_binding']==binding
 assert type(y['rank']) is int and 0<=y['rank']<len(versions)
 expected=versions[y['rank']]
 assert y=={k:v for k,v in expected.items() if k!='envelope_sha256'}
 y['envelope_sha256']=claimed
 return y
class Ledger:
 def __init__(self):self.active=None;self.quarantined=False;self.events=[]
 def receive(self,x):
  try:y=verify_envelope(x)
  except (AssertionError,KeyError,TypeError):self.quarantined=True;out='ABSTAIN_REJECTED'
  else:
   if self.active is None:self.active=y;out='ACCEPTED'
   elif y['envelope_sha256']==self.active['envelope_sha256']:out='DUPLICATE_IGNORED'
   elif y['rank']<self.active['rank']:out='STALE_IGNORED'
   elif y['rank']==self.active['rank']:self.quarantined=True;out='ABSTAIN_CONFLICT'
   elif y['rank']==self.active['rank']+1 and y['parent_calibration_sha256']==self.active['calibration_sha256']:
    self.active=y;out='ACCEPTED'
   elif y['rank']>self.active['rank']:
    # The whitelisted terminal chain was independently verified above and
    # carries every skipped identity-refinement edge.
    self.active=y;out='ACCEPTED_WITH_EMBEDDED_LINEAGE'
   else:self.quarantined=True;out='ABSTAIN_NON_DESCENDING'
  self.events.append(out);return out
 def decision(self):return 'ABSTAIN' if self.quarantined or self.active is None else self.active['status']
# In-order evolution and late replay: signed resolution cannot be overwritten.
a=Ledger();assert [a.receive(x) for x in versions]==['ACCEPTED']*3
assert a.decision()=='CERTIFIED_INFEASIBLE';assert a.receive(versions[1])=='STALE_IGNORED';assert a.decision()=='CERTIFIED_INFEASIBLE'
assert a.receive(versions[2])=='DUPLICATE_IGNORED'
# A signed terminal artifact includes its verified portable ancestry, so a
# receiver may safely catch up without separately receiving theta first.
b=Ledger();assert b.receive(versions[0])=='ACCEPTED';assert b.receive(versions[2])=='ACCEPTED_WITH_EMBEDDED_LINEAGE';assert b.decision()=='CERTIFIED_INFEASIBLE'
# Non-source or non-calibration equivocation cannot select a conclusion.
corruptions=[]
for label,change in (
 ('wrong task binding',lambda x:x.__setitem__('task_binding','0'*64)),
 ('wrong status',lambda x:x.__setitem__('status','CERTIFIED_FEASIBLE')),
 ('forged rank',lambda x:x.__setitem__('rank',1)),
 ('wrong parent',lambda x:x.__setitem__('parent_calibration_sha256','0'*64))):
 bad=copy.deepcopy(versions[2]);change(bad);bad['envelope_sha256']=digest({k:v for k,v in bad.items() if k!='envelope_sha256'})
 c=Ledger();assert c.receive(versions[0])=='ACCEPTED';assert c.receive(bad)=='ABSTAIN_REJECTED' and c.decision()=='ABSTAIN';corruptions.append(label)
# A syntactically different same-rank item is treated as equivocation even
# before a receiver tries to interpret its content.
conflict=copy.deepcopy(versions[1]);conflict['envelope_sha256']='f'*64
c=Ledger();assert c.receive(versions[0])=='ACCEPTED';assert c.receive(versions[1])=='ACCEPTED';assert c.receive(conflict)=='ABSTAIN_REJECTED';assert c.decision()=='ABSTAIN'
protected={str((R/p).relative_to(ROOT)):sha(R/p) for _,p,_ in specs}
protected.update({str((D/p).relative_to(ROOT)):sha(D/p) for _,_,p in specs})
report={'passed':True,'task_binding_sha256':binding,'versions':versions,'in_order_events':a.events,
 'late_replay_result':'STALE_IGNORED','catch_up_result':'ACCEPTED_WITH_EMBEDDED_LINEAGE','corruptions_rejected':corruptions,
 'same_rank_equivocation_result':'ABSTAIN_REJECTED','protected_file_hashes':protected,
 'scope':'A finite local ledger for this declared calibration lineage and frozen task. It proves safe artifact ordering and replay behavior only after hash/chain/source-task validation; it supplies no signatures, network authentication, consensus, or universal refinement order.'}
(OUT/'versioned-signed-certificate-ledger.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'terminal_decision':a.decision(),'late_replay':'STALE_IGNORED','invalid_upgrade':'ABSTAIN'},indent=2))
