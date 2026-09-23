"""Finite live provider bundle synthesis for three scoped services; receipt bytes only."""
from pathlib import Path
from copy import deepcopy
from itertools import combinations
from fractions import Fraction as Q
import gzip,json,sys
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(V/'checkers'))
from full_segment_checkpoint import FullSegmentSession
from checked_retirement_interface import migrate
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
template=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
root=migrate(plan,case,retain_lift=True,retain_archive=True).migration_binding
nodes={}
for name,archive,knots in [('restricted_archive',True,['0','1']),('full_archive',True,['0','1/2','1']),('full_lift',False,['0','1/2','1'])]:
 proof=deepcopy(template);proof['vertices']=[[u,u] for u in knots];proof['source_lifts']=[[u,'0','0'] for u in knots]
 s=FullSegmentSession();boot=s.bootstrap(plan,case,retain_lift=True,retain_archive=archive)
 r=s.attach_full_segment(boot['handle'],boot['state'],proof['vertices'],proof);sid=r['section_id']
 if name=='restricted_archive':
  answer=s._state.refine([1,0],'3/4').maximize([1,0])
  r=s.advance(r['handle'],r['state'],{'kind':'append-public','normal':['1','0'],'upper':'3/4'},[1,0],answer)
 assert r['state']['migration_binding']==root
 nodes[name]=(s,r,proof,sid)
def serves(name,service):
 s,r,p,sid=nodes[name]
 try:s._current(r['handle'])
 except ValueError:return False
 if service=='public_answer_restricted':
  return name=='restricted_archive' and Q(s._state.maximize([1,0])['proof']['value'])==Q(3,4)
 if service=='whole_domain_lift':
  try:return s.covered_lift(r['handle'],sid,['1','1'])==['1','0','0']
  except (ValueError,PermissionError):return False
 if service=='restricted_fine_reexposure':
  try:
   restored=s.reexpose(r['handle']);return name=='restricted_archive' and restored['frames'][-1]=={'normal':['1','0','0'],'upper':'3/4'}
  except (ValueError,PermissionError):return False
 raise AssertionError(service)
services=('public_answer_restricted','whole_domain_lift','restricted_fine_reexposure')
cost={name:sum(r['bytes'].values()) for name,(s,r,p,sid) in nodes.items()}
bundles=[]
for k in range(1,4):
 for group in combinations(nodes,k):
  covering={task:[n for n in group if serves(n,task)] for task in services}
  if all(covering.values()):bundles.append({'providers':list(group),'receipt_bytes':sum(cost[n] for n in group),'covering':covering})
assert bundles
best=min(b['receipt_bytes'] for b in bundles)
winners=[b for b in bundles if b['receipt_bytes']==best]
assert len(winners)==1 and set(winners[0]['providers'])=={'restricted_archive','full_lift'}
assert cost['full_archive']-cost['full_lift']==180
# Hostile: the archive-free provider cannot fill archive service even when
# its fine section formula and coverage equal the archived full provider.
assert not serves('full_lift','restricted_fine_reexposure')
# Deleting the restricted archive loses both the scoped answer and re-exposure.
assert not any(all(any(serves(n,t) for n in group) for t in services) for group in [('full_archive','full_lift'),('full_archive',),('full_lift',)])
# Real generation change, not deletion of a field in a serialized packet.
cs,cr,cp,csid=nodes['full_lift'];assert cr['state']['public_frames']==[]
reply=cs._state.refine([1,0],'3/4').maximize([1,0])
new_c=cs.advance(cr['handle'],cr['state'],{'kind':'append-public','normal':['1','0'],'upper':'3/4'},[1,0],reply)
assert not serves('full_lift','whole_domain_lift')  # recorded old handle is stale
assert not any(serves(n,'whole_domain_lift') for n in ('restricted_archive','full_lift'))
assert serves('full_archive','whole_domain_lift')
assert cs.covered_lift(new_c['handle'],csid,['1/2','1/2'])==['1/2','0','0']
report={'passed':True,'migration_binding':root,'service_menu':list(services),'provider_receipt_bytes':cost,'admissible_bundles':bundles,'minimum_receipt_bundle':winners[0],'no_archive_escalation':True,'restricted_archive_deletion_loses_tasks':True,'stale_full_lift_forces_archive_enabled_replacement':True,'scope':'Finite three-provider owner-verified sessions, receipt-field-byte scalar ONLY. No total-cost or universal optimum, portable grants, or physical source authentication.'}
(V/'results/fixed-menu-provider-bundles.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('migration_binding','admissible_bundles')},indent=2))
