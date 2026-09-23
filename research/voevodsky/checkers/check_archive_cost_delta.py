"""Same migration, same covered section, differing archive permission and payload."""
from pathlib import Path
import gzip,json,sys
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(V/'checkers'))
from full_segment_checkpoint import FullSegmentSession
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
proof=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
receipts=[];services=[]
for enabled in (False,True):
 s=FullSegmentSession();boot=s.bootstrap(plan,case,retain_lift=True,retain_archive=enabled)
 receipt=s.attach_full_segment(boot['handle'],boot['state'],proof['vertices'],proof)
 assert s.covered_lift(receipt['handle'],receipt['section_id'],['1/2','1/2'])==['1/2','0','0']
 receipts.append(receipt);services.append(s)
assert receipts[0]['state']['migration_binding']==receipts[1]['state']['migration_binding']
assert receipts[0]['state']['capabilities']=={'lift':True,'reexpose':False}
assert receipts[1]['state']['capabilities']=={'lift':True,'reexpose':True}
try:services[0].reexpose(receipts[0]['handle'])
except PermissionError:refused=True
else:raise AssertionError('archive-free provider re-exposed fine state')
assert services[1].reexpose(receipts[1]['handle'])==plan
left,right=(r['bytes'] for r in receipts)
assert left['lift_context']==right['lift_context'] and left['full_segment_encodings']==right['full_segment_encodings']
assert left['archive']==0 and right['archive']>0
# Descriptor also changes because advertised capability differs; never
# attribute that byte difference to the fine-relation encoding itself.
delta={key:right[key]-left[key] for key in left}
assert sum(delta.values())==sum(right.values())-sum(left.values())
report={'passed':True,'migration_binding':receipts[0]['state']['migration_binding'],'without_archive':left,'with_archive':right,'field_delta':delta,'archive_free_reexposure_refused':refused,'same_lift_and_coverage':True,'scope':'Two independently bootstrapped sessions, same owner migration and section. Canonical receipt bytes only; duplicate bootstraps and shared code/proof costs are additional, not measured by delta.'}
(V/'results/archive-cost-delta.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('migration_binding','without_archive','with_archive')},indent=2))
