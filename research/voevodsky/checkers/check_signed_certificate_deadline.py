"""Causal availability of the signed-pairing source-task certificate.

This is a finite reliable-message experiment over existing frozen task artifacts.
It does not model acquisition latency or prove that any physical observation occurs.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck';OUT=ROOT/'research/voevodsky/results'
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
t=module('task',G/'checkers/three_channel_source_task.py')
v=module('verify',G/'certificates/verify_source_task_transition.py')
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
cal=G/'results/three-channel-source-task-calibration-signed-pairing.json'
theta=G/'results/three-channel-source-task-calibration-theta-taylor.json'
refinement=G/'results/signed-pairing-task-refinement.json'
transport_path=ROOT/'research/voevodsky/results/signed-task-transport.json'
transport=load(transport_path);assert transport['passed'] and transport['calibration_sha256']==sha(cal)
chain_dir=G/'results/portable-source-task-transitions'
frozen=load(G/'results/calibration-refinement-frozen-inputs.json')
engine=t.SourceTask(cal);old=t.SourceTask(theta)
v.verify(v.load(chain_dir/'private-lower_threshold-signed-pairing.json'))
v.verify(v.load(chain_dir/'private-upper_threshold-signed-pairing.json'))
protected=[cal,theta,refinement,transport_path,G/'results/calibration-refinement-frozen-inputs.json',
           chain_dir/'private-lower_threshold-signed-pairing.json',chain_dir/'private-upper_threshold-signed-pairing.json']
hashes={str(p.relative_to(ROOT)):sha(p) for p in protected}
DEADLINE=5
# The two worlds share every A-visible observation. Only the positive
# readout differs, and it is retained by B until its certified report arrives.
def coarse(data):return {k:data['raw'][k] for k in ('vacuum','crossed')}
def wire(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def outcome(data,who):
 result=engine.certify(data);assert result['status'] in ('CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE')
 if who=='A': assert old.certify(data)['status']=='UNRESOLVED'
 return result['status']
def run(name,delay):
 data=frozen['cases']['private'][name];status=outcome(data,'B')
 frame=transport['frames'][name]
 assert frame['task_id']==name and frame['claimed_status']==status and frame['raw']==data['raw']
 assert engine.certify({k:frame[k] for k in ('mode','budget','auto_witness','raw')})['necessary_moment_cost_lower_bound']==frame['necessary_cost']
 A={'time':1,'kind':'coarse-source-observation','payload':coarse(data)}
 B={'time':4,'kind':'signed-pairing-task-transport-frame','payload':frame}
 arrivals={'A':[(1,A),(4+delay,B)],'B':[(4,B)]}
 traces={}
 for actor in ('A','B'):
  visible=[message for time,message in arrivals[actor] if time<=DEADLINE]
  has_signed=any(m['kind']=='signed-pairing-task-transport-frame' for m in visible)
  certificate=status if has_signed else 'ABSTAIN'
  # A's coarse record cannot reproduce a task certificate: the withheld
  # positive row is part of the source-task obligation.
  if actor=='A' and not has_signed:assert wire(visible)==wire([A])
  traces[actor]={'received_by_deadline':visible,'certificate':certificate}
 return {'world':name,'correct_status':status,'B_to_A_delay':delay,'traces':traces,
         'B_issues_at':4,'A_can_issue_at':4+delay if delay<=DEADLINE-4 else None}
fast=[run(n,1) for n in ('lower_threshold','upper_threshold')]
slow=[run(n,6) for n in ('lower_threshold','upper_threshold')]
assert [x['correct_status'] for x in fast]==['CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE']
for x in fast:
 assert x['traces']['B']['certificate']==x['correct_status']
 assert x['traces']['A']['certificate']==x['correct_status']
 assert x['A_can_issue_at']==5
for x in slow:
 assert x['traces']['B']['certificate']==x['correct_status']
 assert x['traces']['A']['certificate']=='ABSTAIN' and x['A_can_issue_at'] is None
# Exact transcript equality plus opposite required definite outputs gives a
# causal indistinguishability result, not a claim about commit barriers.
assert wire(slow[0]['traces']['A']['received_by_deadline'])==wire(slow[1]['traces']['A']['received_by_deadline'])
assert slow[0]['correct_status']!=slow[1]['correct_status']
# A fixed commit works when distinguishing information arrives. A particular
# mutual-ready handshake does not, but is not a universal barrier lower bound.
ack_time=8
assert all(x['A_can_issue_at']<=DEADLINE for x in fast) and ack_time>DEADLINE
assert hashes=={str(p.relative_to(ROOT)):sha(p) for p in protected}
report={'passed':True,'decision_contract':'certify the frozen source task as feasible or infeasible using the signed-pairing calibration by deadline 5; abstention is allowed when evidence is absent',
 'source_contract':['unchanged raw source-task intervals','unchanged source family and prior','signed-pairing calibration hash','exact task checker'],
 'protected_file_hashes':hashes,'schedule':{'A_coarse_observation_complete':1,'B_full_certificate_issued':4,
   'B_to_A_fast_delay':1,'B_to_A_delayed_delay':6,'deadline':DEADLINE,'specified_mutual_ready_ack_time':ack_time},
 'fast_cases':fast,'delayed_cases':slow,
 'checks':{'signed_calibration_replays_existing_lower_and_upper_frozen_tasks':True,
   'theta_only_calibration_is_unresolved_for_these_tasks':True,
   'both_observers_certify_without_mutual_ack_when_the_signed_certificate_arrives':True,
   'fixed_commit_at_deadline_can_succeed':True,
   'delayed_A_transcripts_are_identical_while_required_definite_outcomes_differ':True,
   'absence_of_the_positive_source_row_not_clock_synchronization_causes_the_obstruction':True},
 'scope':'Conditional finite reliable-delivery schedule over already-generated mathematical certificates. It establishes availability and indistinguishability only for these declared frozen task worlds; no physical sensing, source occurrence, consensus-under-loss, or universal coordination theorem is claimed.'}
(OUT/'signed-certificate-deadline.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'fast_A_time':5,'delayed_A_status':'ABSTAIN','opposite_hidden_outcomes':True},indent=2))
