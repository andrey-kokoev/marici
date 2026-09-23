"""Fresh owning-migration and full polygon attachment replay.

Uses the same exact attachment kernel, not a second implementation.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from full_polygon_checkpoint import verify_full_polygon,weights,interpolate,check_section
from checked_retirement_interface import migrate,verify_answer
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/nima/results'
def check_point(state,packet,p,t):
    check_section(state,[p],{'migration_binding':state.migration_binding,'vertices':[p],'source_lifts':[t]})
    vertices=[tuple(map(Q,v)) for v in packet['vertices']];lifts=[tuple(map(Q,v)) for v in packet['source_lifts']]
    point=tuple(map(Q,p));seen=False
    for ids in packet['triangles']:
        triangle=[vertices[i] for i in ids]
        if all(w>=0 for w in weights(triangle,point)):
            assert interpolate(triangle,[lifts[i] for i in ids],point)==tuple(map(Q,t));seen=True
    assert seen

def main():
    report=json.loads((OUT/'full-polygon-checkpoint.json').read_text())
    for p,h in report['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    i=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');plan=plans[i]
    assert report['expected_plan']==plan and report['migration']==plan['name']
    state=migrate(plan,cases[i],retain_lift=True);packet=report['packet']
    work=verify_full_polygon(state,report['polygon'],packet)
    assert work==report['attachment']['attachment_work']
    assert report['attachment']['state']==state.descriptor() and report['attachment']['coverage']=='full-current-domain'
    assert len(report['answers'])==11
    for a in report['answers']:check_point(state,packet,a['point'],a['source_lift'])
    op={'kind':'append-public','normal':['1','0'],'upper':'162'}
    restriction=report['restriction'];assert restriction['operation']==op
    after=state.refine(op['normal'],op['upper']);verify_answer(after.descriptor(),['1','0'],restriction['answer'])
    check_point(after,packet,restriction['point'],restriction['source_lift'])
    assert report['successor']['state']==after.descriptor()==report['final']['state']
    assert report['final']['section_work']=={'vertex_checks':6,'interpolated_lifts':12}
    assert report['final']['state']['capabilities']=={'lift':True,'reexpose':False}
    result={'passed':True,'migration':plan['name'],'attachment_work':work,'section_points_replayed':12,
      'scope':'Fresh owning migration, full-domain attachment, coherent interpolation and restriction replay; same verification kernel.'}
    (OUT/'full-polygon-checkpoint-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
