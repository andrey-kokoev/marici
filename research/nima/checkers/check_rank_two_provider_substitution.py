"""Different witnesses, same rank-two lifting relation, different contracts."""
from pathlib import Path
from fractions import Fraction as Q
import copy,json,gzip,hashlib
from rank_two_provider_substitution import ProviderRouter,ADMISSIBLE,SELECTED,map_comparison,digest
from full_polygon_checkpoint import FullPolygonSession,coverage_rows,polygon_targets,check_section,verify_full_polygon
from checked_retirement_interface import migrate,source
from check_full_polygon_checkpoint import certificate
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/nima/results'
def main():
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    index=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');plan=plans[index];case=cases[index]
    state=migrate(plan,case,retain_lift=True);_,_,observe,caps=source(plan['m'],plan['audits'])
    assert plan['m']==3 and plan['audits']==[0] and plan['retire']==0
    a,b,c=Q(10),caps[1],caps[2];z=Q(0)
    lifts=[(z,z,z),(z,z,c),(z,b,c),(a,b,c),(a,b,z),(a,z,z)]
    vertices=[list(map(str,observe(t)[:2])) for t in lifts];polygon=[tuple(map(Q,p)) for p in vertices]
    original={'migration_binding':state.migration_binding,'polygon':vertices,'vertices':vertices,
      'source_lifts':[list(map(str,t)) for t in lifts],'triangles':[[0,i,i+1] for i in range(1,5)],
      'coverage_weights':[certificate(coverage_rows(state),target) for target in polygon_targets(polygon)]}
    center=[str((x+y)/2) for x,y in zip(polygon[0],polygon[3])]
    center_source=[str((x+y)/2) for x,y in zip(lifts[0],lifts[3])]
    alternative=copy.deepcopy(original)
    alternative['vertices']=copy.deepcopy(vertices)+[center]
    different=[str(Q(x)+Q(k,1000)) for x,k in zip(center_source,(1,-129,128))]
    alternative['source_lifts'].append(different)
    alternative['triangles']=[[6,i,(i+1)%6] for i in range(6)]
    def provider(packet):
        p=FullPolygonSession();boot=p.bootstrap(plan,case,retain_lift=True)
        admitted=p.attach_full_polygon(boot['handle'],boot['state'],vertices,packet)
        return p,admitted
    left,l=provider(original);right,r=provider(alternative);clone,copied=provider(original)
    for packet in (original,alternative):verify_full_polygon(state,vertices,packet)
    assert left.covered_lift(l['handle'],l['section_id'],center)==center_source
    assert right.covered_lift(r['handle'],r['section_id'],center)==different!=center_source
    comparison=map_comparison(original,alternative);assert not comparison['pointwise_equal']
    for label,packet,source_point in (('left',original,center_source),('right',alternative,different)):
        check_section(state,[center],{'migration_binding':state.migration_binding,'vertices':[center],'source_lifts':[source_point]})
    weak=ProviderRouter();weak_before=weak.bootstrap(left,l['handle'],l['section_id'],l['state'],vertices,ADMISSIBLE)
    strong=ProviderRouter();strong_before=strong.bootstrap(left,l['handle'],l['section_id'],l['state'],vertices,SELECTED)
    strong_refusal=strong.substitute(strong_before['handle'],strong_before,right,r['handle'],r['section_id'],r['state'])
    assert strong_refusal['status']=='REFUSED_SELECTED_WITNESS_CHANGE' and strong.receipt()==strong_before
    assert strong.lift(strong_before['handle'],center)==center_source
    accepted=weak.substitute(weak_before['handle'],weak_before,right,r['handle'],r['section_id'],r['state'])
    assert accepted['status']=='SUBSTITUTED' and weak.lift(accepted['receipt']['handle'],center)==different
    # Strong substitution is not universally refused: an independent live
    # provider of the same selected map passes the whole-overlap equality gate.
    strong_success=strong.substitute(strong_before['handle'],strong_before,clone,copied['handle'],copied['section_id'],copied['state'])
    assert strong_success['status']=='SUBSTITUTED' and strong_success['comparison']['map_comparison']['pointwise_equal']
    rejected=[]
    def reject(name,action):
        try:action()
        except (AssertionError,ValueError,PermissionError,KeyError,TypeError):rejected.append(name)
        else:raise AssertionError(name+' accepted')
    reject('stale-router-head',lambda:weak.lift(weak_before['handle'],center))
    reject('archive-escalation',lambda:weak.reexpose(accepted['receipt']['handle']))
    reject('forged-provider-descriptor',lambda:ProviderRouter().bootstrap({'capabilities':{'lift':True}},r['handle'],r['section_id'],r['state'],vertices))
    wrong=copy.deepcopy(r['state']);wrong['migration_binding']='foreign'
    reject('foreign-migration-context',lambda:ProviderRouter().bootstrap(right,r['handle'],r['section_id'],wrong,vertices))
    scope=copy.deepcopy(vertices);scope[0]=['1','1']
    reject('altered-scope',lambda:ProviderRouter().bootstrap(right,r['handle'],r['section_id'],r['state'],scope))
    unchanged=weak.receipt();forged=copy.deepcopy(unchanged);forged['contract']=SELECTED
    reject('caller-changed-contract',lambda:weak.substitute(unchanged['handle'],forged,clone,copied['handle'],copied['section_id'],copied['state']))
    assert weak.receipt()==unchanged
    # Positive whole-domain premises, supplemented with finite live queries.
    answers=[]
    for point in vertices+[center]:
        lt=left.covered_lift(l['handle'],l['section_id'],point);rt=weak.lift(unchanged['handle'],point)
        for t in (lt,rt):check_section(state,[point],{'migration_binding':state.migration_binding,'vertices':[point],'source_lifts':[t]})
        answers.append({'point':point,'left':lt,'right':rt})
    # A genuine generation change invalidates a previously admitted provider,
    # even though its stored polygon and formula encodings have not changed.
    op={'kind':'append-public','normal':['1','0'],'upper':'162'};refined=state.refine(op['normal'],op['upper'])
    answer=refined.maximize([1,0]);advanced=right.advance(r['handle'],r['state'],op,[1,0],answer)
    reject('stale-active-provider',lambda:weak.lift(unchanged['handle'],center))
    reject('stale-candidate-provider',lambda:strong.substitute(strong_success['receipt']['handle'],strong_success['receipt'],right,r['handle'],r['section_id'],r['state']))
    assert strong.lift(strong_success['receipt']['handle'],center)==center_source
    paths=[Path(__file__),Path(__file__).with_name('rank_two_provider_substitution.py'),Path(__file__).with_name('full_polygon_checkpoint.py'),
      Path(__file__).with_name('verify_scalar_envelope_band.py'),ROOT/'research/voevodsky/checkers/migration_section_checkpoint.py',
      ROOT/'research/voevodsky/checkers/migration_checkpoint.py',ROOT/'research/voevodsky/checkers/checked_retirement_interface.py',
      G/'audit-elimination-contract.json',G/'audit-elimination.json.gz']
    result={'passed':True,'plan':plan,'polygon':vertices,'original_section':original,'alternative_section':alternative,
      'source_attachment':l,'target_attachment':r,'center':center,'original_center_lift':center_source,'alternative_center_lift':different,
      'admissible_substitution':accepted,'selected_witness_refusal':strong_refusal,'equal_map_substitution':strong_success,
      'answers':answers,'provider_refinement':{'operation':op,'answer':answer,'receipt':advanced},'rejections':rejected,
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
      'scope':'Contract-preserving replacement of different exact sections; not equality of returned vectors or unrestricted observational equivalence.'}
    (OUT/'rank-two-provider-substitution.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'source_cells':4,'target_cells':6,'different_center_witnesses':True,
      'admissible_contract_substitution':True,'selected_witness_contract_refused':True,'equal_map_control':True,'additional_rejections':len(rejected)},indent=2))
if __name__=='__main__':main()
