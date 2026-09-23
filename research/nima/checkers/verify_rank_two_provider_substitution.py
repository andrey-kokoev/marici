"""Fresh section and contract replay; no provider-router import.

Live handle validity is exercised in-process, not authenticated by this JSON.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from full_polygon_checkpoint import verify_full_polygon,intersection,interpolate
from verify_full_polygon_checkpoint import check_point
from checked_retirement_interface import migrate,freeze,verify_answer
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';G=ROOT/'research/grothendieck/results'
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
def maps(left,right):
    def cells(packet):
        v=[tuple(map(Q,p)) for p in packet['vertices']];t=[tuple(map(Q,p)) for p in packet['source_lifts']]
        return [([v[i] for i in ids],[t[i] for i in ids]) for ids in packet['triangles']]
    count=0;counter=None
    for p,t in cells(left):
        for q,u in cells(right):
            for v in intersection(p,q):
                a,b=interpolate(p,t,v),interpolate(q,u,v);count+=1
                if a!=b and counter is None:counter={'point':list(map(str,v)),'left_lift':list(map(str,a)),'right_lift':list(map(str,b))}
    return {'pointwise_equal':counter is None,'intersection_vertex_checks':count,'counterexample':counter}
def main():
    report=json.loads((OUT/'rank-two-provider-substitution.json').read_text())
    for p,h in report['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    i=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');assert report['plan']==plans[i]
    state=migrate(plans[i],cases[i],retain_lift=True);left,right=report['original_section'],report['alternative_section']
    for packet,attachment in ((left,report['source_attachment']),(right,report['target_attachment'])):
        assert verify_full_polygon(state,report['polygon'],packet)==attachment['attachment_work']
        assert attachment['state']==state.descriptor()
    comparison=maps(left,right);assert not comparison['pointwise_equal']
    for result,contract in ((report['admissible_substitution'],'return-some-exact-admissible-fine-lift'),
                             (report['selected_witness_refusal'],'preserve-selected-source-vector')):
        c=result['comparison'];assert c['contract']==contract and c['map_comparison']==comparison
        assert c['migration_binding']==state.migration_binding and c['scope_digest']==digest(report['polygon'])
        assert c['fine_context_digest']==hashlib.sha256(state.lift_json.encode()).hexdigest()
        assert c['source_section']==digest(left) and c['target_section']==digest(right)
        assert c['source_generation']==report['source_attachment']['handle'] and c['target_generation']==report['target_attachment']['handle']
    assert report['admissible_substitution']['status']=='SUBSTITUTED'
    assert report['selected_witness_refusal']['status']=='REFUSED_SELECTED_WITNESS_CHANGE'
    assert report['selected_witness_refusal']['head_unchanged'] is True
    assert report['equal_map_substitution']['comparison']['map_comparison']==maps(left,left)
    assert report['equal_map_substitution']['status']=='SUBSTITUTED'
    for record in report['answers']:
        check_point(state,left,record['point'],record['left']);check_point(state,right,record['point'],record['right'])
    for packet,lift in ((left,report['original_center_lift']),(right,report['alternative_center_lift'])):
        check_point(state,packet,report['center'],lift)
    delta=[Q(b)-Q(a) for a,b in zip(report['original_center_lift'],report['alternative_center_lift'])]
    assert delta==[Q(1,1000),Q(-129,1000),Q(128,1000)]
    ref=report['provider_refinement'];assert ref['operation']=={'kind':'append-public','normal':['1','0'],'upper':'162'}
    after=state.refine(['1','0'],'162');verify_answer(after.descriptor(),['1','0'],ref['answer'])
    assert ref['receipt']['state']==after.descriptor()
    result={'passed':True,'source_cells':len(left['triangles']),'target_cells':len(right['triangles']),
      'center_atom_infinity_distance':str(max(map(abs,delta))),'whole_domain_admissibility':True,
      'selected_witness_equality':False,'scope':'Independent routing-free replay using shared exact geometric and owning-source kernels; not live-authority authentication.'}
    (OUT/'rank-two-provider-substitution-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
