"""Typed same-source law: public restriction commutes extensionally with checked section; not authority."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as Q
import gzip,json,sys
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(V/'checkers'))
from full_segment_checkpoint import FullSegmentSession,verify_full_segment
from checked_retirement_interface import migrate
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
template=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
base=migrate(plan,case,retain_lift=True,retain_archive=True)
s=FullSegmentSession();boot=s.bootstrap(plan,case,retain_lift=True,retain_archive=True)
packet=deepcopy(template);assert verify_full_segment(s._state,packet['vertices'],packet)['cells']==2
attached=s.attach_full_segment(boot['handle'],boot['state'],packet['vertices'],packet)
old_handle=attached['handle'];sid=attached['section_id'];root=attached['state']['migration_binding']
assert root==base.migration_binding
# Source-level square: for every u in [0,3/4], restriction of the verified
# affine formula (u,0,0) agrees with the successor's covered-lift formula.
# Interval proof is cellwise affine plus verified full coverage, not samples.
assert all(tuple(map(Q,t))==(Q(v[0]),Q(0),Q(0)) for v,t in zip(packet['vertices'],packet['source_lifts']))
F=('0','3/4');answer=base.refine([1,0],F[1]).maximize([1,0])
advanced=s.advance(old_handle,attached['state'],{'kind':'append-public','normal':['1','0'],'upper':F[1]},[1,0],answer)
assert advanced['state']['migration_binding']==root
assert s.covered_lift(advanced['handle'],sid,['1/2','1/2'])==['1/2','0','0']
refusals=[]
def reject(name,fn):
 try:fn()
 except (ValueError,PermissionError,AssertionError):refusals.append(name)
 else:raise AssertionError('unexpected admission '+name)
reject('stale-old-handle',lambda:s.covered_lift(old_handle,sid,['1/2','1/2']))
reject('outside-refined-domain',lambda:s.covered_lift(advanced['handle'],sid,['1','1']))
reject('nonpublic-operation',lambda:s.advance(advanced['handle'],advanced['state'],{'kind':'append-public','normal':['1','0','0'],'upper':'0'},[1,0],{}))
assert s._receipt()['handle']==advanced['handle'] and s._state.descriptor()==advanced['state']
# Independently remove attachment coverage, source binding and archive context;
# failed attachment is atomic and cannot publish a new provider generation.
for name,mutate in (('missing-coverage',lambda p:p['coverage_weights'].pop()),
                    ('foreign-root',lambda p:p.update(migration_binding='foreign'))):
 bad=deepcopy(packet);mutate(bad)
 candidate=FullSegmentSession();initial=candidate.bootstrap(plan,case,retain_lift=True)
 reject(name,lambda bad=bad,candidate=candidate,initial=initial:candidate.attach_full_segment(initial['handle'],initial['state'],packet['vertices'],bad))
 assert candidate._receipt()['handle']==initial['handle'] and candidate._state.descriptor()==initial['state']
no_archive=FullSegmentSession();empty=no_archive.bootstrap(plan,case,retain_lift=True,retain_archive=False)
reject('missing-archive-capability',lambda:no_archive.reexpose(empty['handle']))
assert no_archive._receipt()['handle']==empty['handle']
restored=s.reexpose(advanced['handle'])
assert restored['frames'][:-1]==plan['frames'] and restored['frames'][-1]=={'normal':['1','0','0'],'upper':'3/4'}
report={'passed':True,'source_binding':root,'original_scope':['0','1'],'refined_scope':list(F),'whole_section_law':'restrict((u,u)->(u,0,0),[0,3/4]) equals checked successor section on [0,3/4]','original_cells':2,'refusals':refusals,'fresh_archive_frame':restored['frames'][-1],'cost_receipt_fields':sorted(advanced['bytes']),'scope':'Fixed verified rank-one migration, exact affine coverage, owner-checked public advance. No equality of handles, archive grants, proof paths, full cost or analytic roles.'}
(V/'results/unified-local-laws.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='source_binding'},indent=2))
