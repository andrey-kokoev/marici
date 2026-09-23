"""Same owning migration: live lift replacement and independent archive re-exposure."""
from pathlib import Path
from copy import deepcopy
import gzip,json,sys
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(V/'checkers'))
from full_segment_checkpoint import FullSegmentSession
from checked_retirement_interface import migrate
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
section=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
root=migrate(plan,case,retain_lift=True,retain_archive=True).migration_binding
nodes=[]
for knots in (['0','1'],['0','1/2','1']):
 proof=deepcopy(section);proof['vertices']=[[u,u] for u in knots];proof['source_lifts']=[[u,'0','0'] for u in knots]
 service=FullSegmentSession();boot=service.bootstrap(plan,case,retain_lift=True,retain_archive=True)
 receipt=service.attach_full_segment(boot['handle'],boot['state'],proof['vertices'],proof)
 assert receipt['state']['migration_binding']==root
 nodes.append((service,receipt,proof))
def lift(i,u):
 service,receipt,_=nodes[i]
 return service.covered_lift(receipt['handle'],receipt['section_id'],[u,u])
for u in ('0','1/4','1/2','3/4','1'):
 assert lift(0,u)==lift(1,u)==[u,'0','0']
archive_before=nodes[0][0].reexpose(nodes[0][1]['handle'])
assert archive_before==nodes[1][0].reexpose(nodes[1][1]['handle'])
# Revoke generation 0 through an owner-checked append-public advancement.
s,r,_=nodes[0];state=s._state
answer=state.refine([1,0],'3/4').maximize([1,0]);op={'kind':'append-public','normal':['1','0'],'upper':'3/4'}
fresh=s.advance(r['handle'],r['state'],op,[1,0],answer)
try:lift(0,'1/2')
except ValueError:stale=True
else:raise AssertionError('stale generation supplied a lift')
assert lift(1,'1/2')==['1/2','0','0']
try:s.reexpose(r['handle'])
except ValueError:stale_archive=True
else:raise AssertionError('stale generation supplied archive')
restored=s.reexpose(fresh['handle'])
assert restored['frames'][:-1]==plan['frames'] and restored['frames'][-1]['upper']=='3/4'
assert nodes[1][0].reexpose(nodes[1][1]['handle'])==archive_before
report={'passed':True,'migration_binding':root,'live_providers':2,'full_domain_lift_comparisons':5,'stale_lift_refused':stale,'stale_archive_refused':stale_archive,'replacement_lift_passed':True,'fresh_archive_carries_public_refinement':True,'bytes':[fresh['bytes'],nodes[1][1]['bytes']],'scope':'One real owner-verified migration; two separately bootstrapped sessions, owner-checked public advance. Not a portable archive grant, optimizer or physical authority.'}
(V/'results/same-base-live-archive-services.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('bytes','migration_binding')},indent=2))
