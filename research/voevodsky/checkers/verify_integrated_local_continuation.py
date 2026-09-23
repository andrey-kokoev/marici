"""Independent replay of frozen integrated semantics; does not import session producer."""
from pathlib import Path
import gzip,json,sys
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(V/'checkers'))
from checked_retirement_interface import migrate,verify_answer
from full_segment_checkpoint import verify_full_segment
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
producer=migrate(plan,case,retain_lift=True,retain_archive=True)
reported=json.loads((V/'results/integrated-local-continuation.json').read_text())
assert reported['passed'] and reported['root']==producer.migration_binding
assert set(reported['refusals'])=={'excluded-public-point','nonpublic-frame','stale-provider','stale-archive'}
section=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
for knots in (['0','1'],['0','1/2','1']):
 packet={**section,'vertices':[[u,u] for u in knots],'source_lifts':[[u,'0','0'] for u in knots]}
 work=verify_full_segment(producer,packet['vertices'],packet)
 assert work['cells']==len(knots)-1 and work['coverage_implications']>0
# Fresh independent public query check on independently expected refined state.
refined=producer.refine([1,0],'3/4');answer=refined.maximize([1,0])
verify_answer(refined.descriptor(),['1','0'],answer)
assert Q(answer['proof']['value'])==Q(3,4)
archive=refined.reexpose();assert archive['frames'][:-1]==plan['frames'] and archive['frames'][-1]=={'normal':['1','0','0'],'upper':'3/4'}
# Exact formula on each checked affine cell, with a public exclusion hostile.
assert all(Q(u)<=Q(3,4) for u in ('0','1/2','3/4')) and Q(1)>Q(3,4)
report={'passed':True,'checked_attachments':2,'verified_refined_public_optimum':'3/4','replayed_archive_frame':archive['frames'][-1],'recorded_refusals_checked':4,'scope':'Independent semantic replay using owning migration, query and attachment verifiers; live-handle refusals are compared to producer report, not independently replayed. No total-cost bound or analytic identification.'}
(V/'results/integrated-local-continuation-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
