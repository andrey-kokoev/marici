"""Registration audit; does not execute the scientific sources or construct bridges."""
from hashlib import sha256
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
NET='research/strominger/contracts/packet-assembly-bridge-conjecture-net.v1.json'
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def digest(p): return sha256((ROOT/p).read_bytes()).hexdigest()
def audit(net):
    nodes=net['conjectures']; by_id={n['id']:n for n in nodes}
    assert len(by_id)==len(nodes)==15
    assert net['owner']=='marici.Strominger' and net['objective']['outcome'] is None
    assert net['objective']['target'] in by_id
    artifacts={a['id']:a for a in net['artifacts']}; references=set()
    for a in artifacts.values(): references.update(a['paths'])
    for a in net['attachments']: references.add(a.get('contract',a.get('path')))
    references.update(net['historical_receipts'])
    for p in references: assert (ROOT/p).is_file(),p
    visited=set(); visiting=set()
    def visit(key):
        assert key in by_id,key
        assert key not in visiting, 'dependency cycle'
        if key in visited: return
        visiting.add(key)
        for d in by_id[key]['depends_on']: visit(d)
        visiting.remove(key); visited.add(key)
    for n in nodes:
        visit(n['id'])
        assert n['outcome'] is None
        assert all(n[k] for k in ('statement','scope','acceptance','falsifier'))
        assert all(e in artifacts for e in n['evidence'])
        if n['status']=='open':
            assert n['verdict']=='open' and not n['evidence']
            assert n['next_action'] and n['deliverable']
        else:
            assert n['status']=='resolved' and n['evidence']
            assert n['verdict'] in ('constructed','rejected')
            if n['verdict']=='rejected': assert n['counterexample']
        for dep,verdict in n.get('required_verdicts',{}).items():
            assert dep in n['depends_on'] and verdict=='constructed'
    frontier=[n['id'] for n in nodes if n['status']=='open' and n.get('actionable',True) and all(by_id[d]['status']=='resolved' for d in n['depends_on'])]
    coupling=by_id['proton-neutron-spin-coupling-binding']
    assert coupling['status']=='open' and coupling['actionable'] is False and coupling['blocker']['missing']
    assert 'proton-neutron-spin-coupling-binding' in by_id['packet-assembly-bridge']['required_verdicts']
    cost=by_id['certificate-to-stage-cost-correspondence']
    assert cost['planning_revision']['scope_frozen_before_test'] and coupling['id'] not in cost['depends_on']
    assert cost['verdict']=='constructed' and cost['resolution_scope'] and cost['negative_findings']
    assert cost['evidence']==['stage-cost-comparison']
    assert net['frontier']==frontier==[] and net['recommended_start'] is None
    assert sum(n['status']=='open' for n in nodes)==2
    assert net['execution_stop']['status']=='blocked_not_complete'
    splitting=by_id['source-spin-lift-splitting']
    assert splitting['status']=='resolved' and splitting['verdict']=='constructed'
    assert splitting['actionable'] is False and splitting['evidence']==['source-spin-lift-splitting']
    assert splitting['resolution_scope']
    assert splitting['depends_on']==['shared-source-spin-frame-transport']
    assert splitting['plan']=='source-spin-lift-splitting-plan'
    assert splitting['plan'] in artifacts and splitting['test_state']=='checks_passed'
    assert 'source-spin-lift-splitting' in by_id['packet-assembly-bridge']['depends_on']
    assert by_id['packet-assembly-bridge']['required_verdicts']['source-spin-lift-splitting']=='constructed'
    proposition=load('research/strominger/contracts/source-spin-lift-splitting.v1.json')
    assert proposition['id']==splitting['id'] and proposition['status']=='resolved'
    assert proposition['disposition']['proposition_tested'] is True
    assert proposition['disposition']['verdict']=='constructed'
    assert proposition['disposition']['exact_check_groups']==16
    assert proposition['disposition']['physical_selection'] is False
    assert proposition['disposition']['prediction_is_not_evidence'] is True
    assert proposition['test_plan']['state']=='checks_passed'
    for path in proposition['disposition']['evidence']:
        assert (ROOT/path).is_file(),path
        references.add(path)
    assert proposition['bold_conjecture']['neutron']=='There exists a section sigma_n of q_n.'
    assert proposition['bold_conjecture']['proton']=='There does not exist a section sigma_p of q_p.'
    for path in proposition['source_inputs']:
        assert (ROOT/path).is_file(),path
        references.add(path)
    assert by_id['packet-assembly-bridge']['status']=='open'
    transport=by_id['native-versus-supplied-transport']
    assert transport['verdict']=='constructed' and transport['resolution_scope']
    assert transport['evidence']==['transport-policy']
    extraction=by_id['source-bound-packet-extraction']
    assert extraction['verdict']=='constructed' and extraction['resolution_scope']
    assert set(extraction['evidence'])=={'electron-extraction','rank-one-extraction'}
    assert sum(n['verdict']=='rejected' for n in nodes)==3
    for key in ('native-path-sector-generating-calculus','shared-source-packet-language',
                'conditional-three-carrier-path-language','shared-source-spin-frame-transport'):
        assert by_id[key]['status']=='resolved' and by_id[key]['verdict']=='constructed'
        assert by_id[key]['resolution_scope']
    native=by_id['native-three-carrier-spin-language']
    assert native['verdict']=='rejected' and native['counterexample']
    extension=by_id['conditional-three-carrier-path-language']['carrier_enlargement']
    assert extension=={'raw_coordinates':[36,72],'return_rank':[1,2],
                       'stage_occurrences':[1836,3672],'physical_selection':False}
    frame=by_id['shared-source-spin-frame-transport']['coordinate_change']
    assert frame=={'encoder':"K'=Ktilde C^-1",'decoder':"D'=C Dtilde",
                   'gram_factor':'rho/r','keeps_raw_projector':True,'physical_selection':False}
    for key in ('shared-source-packet-language','conditional-three-carrier-path-language',
                'shared-source-spin-frame-transport'):
        assert by_id['packet-assembly-bridge']['required_verdicts'][key]=='constructed'
    assert net['shared_language_resolution']=={
        'native_grammar':'constructed','native_generating_calculus':'constructed',
        'conditional_doublet_path_language':'constructed','source_coordinate_frame_transport':'constructed',
        'same_spin_action_on_unextended_native_lines':'rejected','physical_source_selection':'still_missing',
        'fresh_shared_language_checks':12,'fresh_frame_adapter_checks':10,
        'source_spin_extension':{'neutron':'split','proton':'nonsplit'}}
    assert net['verification']=={'registration_only':True,'fresh_scientific_replay':False,'fresh_formal_proof':False,'physical_validation':False,'parent_outcome_admitted':False}
    branch_path='research/strominger/contracts/port-incidence-conjecture-net.v1.json'
    assert any(a.get('contract')==branch_path for a in net['attachments'])
    assert 'port-incidence-comparison' in artifacts
    branch=load(branch_path)
    assert branch['parent_net']==NET and branch['objective']['verdict']=='constructed_comparison'
    assert branch['physical_validation'] is False and branch['neutrino']['tested'] is False
    branch_audit=load('research/strominger/results/port-incidence-net-audit-v1.json')
    assert branch_audit['status']=='pass' and branch_audit['fresh_scientific_check_groups']==22
    for path,expected in branch_audit['source_sha256'].items():
        assert digest(path)==expected,'stale attached port branch: '+path
        references.add(path)
    return references
net=load(NET); references=audit(net)
checks={'fifteen_typed_nodes_acyclic_with_null_formal_outcomes':True,
        'empty_frontier_two_blocked_open_gates_root_not_complete':True,
        'source_splitting_disposition_has_actual_scientific_receipt_not_plan_only':True,
        'historical_evidence_and_three_rejected_inferences_retained':True,
        'shared_language_enlargement_and_coordinate_transport_boundaries_explicit':True,
        'all_artifacts_and_parent_links_exist':True}
# Hostile against the registration checker, not a new particle/scientific experiment.
for mutation in ('cycle','outcome','false_frontier','reactivate_blocked_lane',
                 'promote_native_spin','erase_enlargement','hide_frame_normalizer','drop_frame_gate',
                 'fabricate_ready_frontier','substitute_splitting_plan_for_result','skip_splitting_prerequisite'):
    bad=json.loads(json.dumps(net))
    if mutation=='cycle': bad['conjectures'][0]['depends_on']=['packet-assembly-bridge']
    if mutation=='outcome': bad['conjectures'][-1]['outcome']='++'
    if mutation=='false_frontier': bad['frontier']=['packet-assembly-bridge']
    if mutation=='reactivate_blocked_lane':
        next(n for n in bad['conjectures'] if n['id']=='proton-neutron-spin-coupling-binding')['actionable']=True
    if mutation=='promote_native_spin':
        next(n for n in bad['conjectures'] if n['id']=='native-three-carrier-spin-language')['verdict']='constructed'
    if mutation=='erase_enlargement':
        next(n for n in bad['conjectures'] if n['id']=='conditional-three-carrier-path-language')['carrier_enlargement']['raw_coordinates']=[36,36]
    if mutation=='hide_frame_normalizer':
        next(n for n in bad['conjectures'] if n['id']=='shared-source-spin-frame-transport')['coordinate_change']['gram_factor']='rho'
    if mutation=='drop_frame_gate':
        root=next(n for n in bad['conjectures'] if n['id']=='packet-assembly-bridge')
        del root['required_verdicts']['shared-source-spin-frame-transport']
    if mutation=='fabricate_ready_frontier':
        bad['frontier']=['source-spin-lift-splitting'];bad['recommended_start']='source-spin-lift-splitting'
    if mutation=='substitute_splitting_plan_for_result':
        node=next(n for n in bad['conjectures'] if n['id']=='source-spin-lift-splitting')
        node['evidence']=['source-spin-lift-splitting-plan']
    if mutation=='skip_splitting_prerequisite':
        root=next(n for n in bad['conjectures'] if n['id']=='packet-assembly-bridge')
        root['depends_on'].remove('source-spin-lift-splitting')
        del root['required_verdicts']['source-spin-lift-splitting']
    try: audit(bad)
    except (AssertionError,KeyError): pass
    else: raise AssertionError('accepted malformed net: '+mutation)
checks['cycle_outcome_frontier_native_promotion_enlargement_and_frame_hostiles_rejected']=True
common=load(net['historical_receipts'][0]); spinor=load(net['historical_receipts'][1])
assert common['status']=='passed' and all(common['checks'].values())
assert spinor['verification_passed'] and len(spinor['checks'])==17 and all(spinor['checks'].values())
for name in ('proton','neutron','electron'):
    src=common['carriers'][name]; row=net['historical_measures'][name]
    assert row['raw_complex_coordinates']==src['raw_complex_coordinates']
    assert row['return_rank']==src['return_rank']
    assert row['stage_supports']==src['stage_transfer_supports']
    assert row['transfers']==src['protocol_transfer_count']==sum(row['stage_supports'])
checks['recorded_measures_match_historical_receipt_not_new_replay']=True
n=3; assert n**3*2**(n-1)+n**3*2**(2*n-2)+n**4*2**(2*n-2)==net['historical_measures']['candidate_J3']
checks['candidate_J3_arithmetic_only']=True
for path in ('research/strominger/results/electron-packet-extraction-v1.json',
             'research/strominger/results/rank-one-return-packets-v1.json',
             'research/strominger/results/packet-transport-policy-v1.json',
             'research/strominger/results/baryon-coefficient-spin-binding-v1.json',
             'research/strominger/results/packet-stage-cost-comparison-v1.json',
             'research/strominger/results/native-path-sector-calculus-v1.json',
             'research/strominger/results/shared-packet-path-language-v1.json',
             'research/strominger/results/shared-packet-frame-adapter-v1.json',
             'research/strominger/results/source-spin-lift-splitting-v1.json'):
    receipt=load(path)
    assert receipt['status']=='pass' and all(receipt['checks'].values())
    for source,expected in receipt['source_sha256'].items():
        assert digest(source)==expected,'stale extraction evidence: '+source
checks['resolved_extraction_policy_cost_and_shared_language_have_current_scoped_receipts']=True
language=load('research/strominger/results/shared-packet-path-language-v1.json')
assert len(language['checks'])==12
assert language['dispositions']=={'shared_native_grammar':'constructed',
    'conditional_shared_path_language':'constructed_on_explicit_doublet_extensions',
    'unextended_native_full_spin_language':'rejected'}
assert language['coverage_on_two_doublets']=={'sectors':24,'situated_encounters':72,
    'placement_equations':144,'critical_pair_joins':16,'permutation_routes':96}
assert [r['conjugated_shared_operations_remaining_in_dictionary'] for r in language['geometric_attachments']]==[4,4,2,2,4,4]
frame=load('research/strominger/results/shared-packet-frame-adapter-v1.json')
assert len(frame['checks'])==10 and len(frame['source_bindings'])==6
assert all(r['transported_lift_in_common_dictionary'] and r['transported_conjugations_remaining']==24 for r in frame['source_bindings'])
assert frame['physical_frame_lift_or_coupling_selected'] is False
checks['shared_language_and_frame_receipts_match_the_exact_net_dispositions']=True
splitting=load('research/strominger/results/source-spin-lift-splitting-v1.json')
assert len(splitting['checks'])==16 and splitting['disposition']=={'neutron':'split','proton':'nonsplit'}
for name,size,extension,choices,sections in (('proton',12,24,2048,0),('neutron',3,6,4,1)):
    row=splitting['carriers'][name]
    assert (row['group_size'],row['full_extension_size'],row['normalized_sign_choices_tested'],row['section_count'])==(size,extension,choices,sections)
    assert len(row['homomorphic_sections'])==sections
assert splitting['carriers']['proton']['obstruction']['identity_word']==[0,0,1,0,0,1]
assert splitting['physical_source_selection'] is False
proposition=load('research/strominger/contracts/source-spin-lift-splitting.v1.json')
semantic={k:v for k,v in proposition.items() if k not in ('status','test_plan','disposition')}
semantic_hash=sha256(json.dumps(semantic,sort_keys=True,separators=(',',':')).encode()).hexdigest()
test=load('research/strominger/contracts/source-spin-lift-splitting-test.v1.json')
assert semantic_hash==test['proposition_semantic_sha256']==splitting['proposition_semantic_sha256']
checks['source_splitting_receipt_matches_disposition_and_unchanged_mathematical_statement']=True
result={'schema':'marici.packet-assembly-bridge-net-audit.v1','status':'pass','checks':checks,
        'node_count':15,'open_count':2,'frontier':net['frontier'],
        'recommended_start':net['recommended_start'],'splitting_proposition_tested':True,
        'contract_sha256':digest(NET),'checker_sha256':digest('research/strominger/checkers/check_packet_assembly_bridge_net.py'),
        'referenced_file_sha256':{p:digest(p) for p in sorted(references)},
        'fresh_scope':'registration structure, historical receipt metadata, recorded measures, arithmetic and malformed-net hostiles',
        'scientific_sources_replayed':False,'formal_proofs_recompiled':False,'parent_outcomes_admitted':False}
out=ROOT/'research/strominger/results/packet-assembly-bridge-net-audit-v1.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='referenced_file_sha256'},indent=2))
