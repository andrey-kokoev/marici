"""Independent packet-level replay of rank-one typed public/section square."""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as Q
import gzip,json,sys
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
sys.path.insert(0,str(V/'checkers'))
from checked_retirement_interface import migrate,verify_answer
from full_segment_checkpoint import verify_full_segment
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
state=migrate(plan,case,retain_lift=True,retain_archive=True)
packet=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
claimed=json.loads((V/'results/unified-local-laws.json').read_text())
assert claimed['passed'] and claimed['source_binding']==state.migration_binding==packet['migration_binding']
assert claimed['original_scope']==['0','1'] and claimed['refined_scope']==['0','3/4']
work=verify_full_segment(state,packet['vertices'],packet)
assert work['cells']==2 and work['coverage_implications']>0
assert tuple(map(Q,packet['vertices'][0]))==(0,0) and tuple(map(Q,packet['vertices'][-1]))==(1,1)
assert all(Q(v[0])==Q(v[1]) and tuple(map(Q,t))==(Q(v[0]),Q(0),Q(0)) for v,t in zip(packet['vertices'],packet['source_lifts']))
# Independent expected public state and query, not reconstructed from claimed answer.
refined=state.refine([1,0],'3/4');answer=refined.maximize([1,0]);verify_answer(refined.descriptor(),['1','0'],answer)
assert Q(answer['proof']['value'])==Q(3,4)
assert refined.reexpose()['frames'][-1]==claimed['fresh_archive_frame']=={'normal':['1','0','0'],'upper':'3/4'}
# The source formula and D_F coincide on the WHOLE interval by affine cells;
# deleting either attachment premise fails an independently called verifier.
rejected=[]
for name,change in (('missing-coverage',lambda p:p['coverage_weights'].pop()),('foreign-root',lambda p:p.update(migration_binding='foreign'))):
 bad=deepcopy(packet);change(bad)
 try:verify_full_segment(state,bad['vertices'],bad)
 except (AssertionError,ValueError):rejected.append(name)
 else:raise AssertionError('malformed proof accepted: '+name)
try:verify_answer(refined.descriptor(),['1','0'],state.maximize([1,0]))
except AssertionError:rejected.append('stale-answer-packet')
else:raise AssertionError('old answer accepted for successor')
assert {'missing-coverage','foreign-root'}<=set(claimed['refusals'])
report={'passed':True,'checked_cells':2,'refined_public_optimum':'3/4','hostiles':rejected,'verified_source_binding':state.migration_binding,'scope':'Independent semantic packet replay with owning verifiers; no producer import. Live handle and archive capability refusals require separate runtime tests, not inferable from this packet.'}
(V/'results/unified-local-laws-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='verified_source_binding'},indent=2))
