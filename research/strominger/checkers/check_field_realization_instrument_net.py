"""Typed net audit: dependencies, scoped dispositions, evidence hashes and frontier."""
from pathlib import Path
import copy,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
NET=ROOT/'research/strominger/contracts/field-realization-instrument-conjecture-net.v1.json'
CURRENT=NET.with_name('field-realization-instrument-conjecture-net.current.json')

def audit(net):
    assert net['owner']=='marici.Strominger'
    assert net['objective']['outcome'] is None and not net['objective']['physical_assignment_complete']
    nodes={n['id']:n for n in net['conjectures']};assert len(nodes)==len(net['conjectures'])
    for key in [net['objective']['target'],*net['objective']['companion_targets']]:assert key in nodes and nodes[key]['status']=='open'
    artifacts={a['id']:a for a in net['artifacts']};paths={net['parent_net']}
    for imp in net['imports']:paths.add(imp['contract'])
    for a in artifacts.values():paths.update(a['paths'])
    assert all((ROOT/p).is_file() for p in paths)
    visiting=set();seen=set()
    def visit(key):
        assert key in nodes and key not in visiting,'missing/cyclic dependency'
        if key in seen:return
        visiting.add(key);n=nodes[key]
        for d in n['depends_on']+[d for group in n.get('alternative_dependencies',[]) for d in group]:visit(d)
        visiting.remove(key);seen.add(key)
    for key in nodes:visit(key)
    def ready(n):
        common=all(nodes[d]['status']=='resolved' and nodes[d]['verdict']==n['required_verdicts'][d] for d in n['depends_on'])
        alternatives=n.get('alternative_dependencies')
        return common and (not alternatives or any(all(nodes[d]['status']=='resolved' and nodes[d]['verdict']=='constructed' for d in group) for group in alternatives))
    for n in nodes.values():
        assert n['outcome'] is None
        assert n['status'] in ['open','resolved'] and n['verdict'] in ['open','constructed','rejected']
        assert set(n['required_verdicts'])==set(n['depends_on'])
        assert all(n[k] for k in ['statement','scope','acceptance','falsifier','reopen_when'])
        assert set(n['evidence'])<=set(artifacts)
        if n['status']=='resolved':assert n['verdict']!='open' and n['evidence'] and not n['actionable']
        else:
            assert n['verdict']=='open'
            if n['actionable']:assert ready(n) and n['next_test']
            else:assert n.get('blocker')
    frontier=[n['id'] for n in nodes.values() if n['status']=='open' and n['actionable'] and ready(n)]
    assert net['frontier']==frontier
    assert net['recommended_start']=='task-relative-orbit-invariants' and net['recommended_start'] in frontier
    assert set(frontier)=={'task-relative-orbit-invariants','graded-parent-transport','field-transport-interface','instrument-signature-audit','crossing-specification','PNE-solid-specification'}
    task_deps={
        'task-first-explanatory-constraint':[],
        'task-four-state-extraction':['task-first-explanatory-constraint'],
        'task-symmetry-lift-classification':['task-four-state-extraction'],
        'task-presentation-relabel-equivalence':['task-four-state-extraction'],
        'task-full-field-interface-coherence':['task-presentation-relabel-equivalence'],
        'task-complete-readouts':['task-first-explanatory-constraint','task-full-field-interface-coherence']}
    for key,deps in task_deps.items():
        n=nodes[key]
        established=key=='task-first-explanatory-constraint'
        rejected=key=='task-four-state-extraction'
        assert n['status']==('resolved' if established or rejected else 'open')
        assert n['verdict']==('constructed' if established else 'rejected' if rejected else 'open') and '?' not in n['statement']
        assert n['depends_on']==deps and n['required_verdicts']=={d:'constructed' for d in deps}
        assert not n['actionable']
    decorated=nodes['task-decorated-carrier']
    assert decorated['status']=='resolved' and decorated['verdict']=='constructed' and not decorated['actionable']
    assert decorated['depends_on']==['task-four-state-extraction'] and decorated['required_verdicts']=={'task-four-state-extraction':'rejected'}
    lifts=nodes['task-decorated-index-lifts']
    assert lifts['status']=='resolved' and lifts['verdict']=='constructed' and not lifts['actionable'] and lifts['depends_on']==['task-decorated-carrier']
    assert lifts['required_verdicts']=={'task-decorated-carrier':'constructed'}
    interface=nodes['task-anchored-sector-interface']
    assert interface['status']=='resolved' and interface['verdict']=='constructed' and not interface['actionable']
    family=nodes['task-cyclic-presentation-family']
    assert family['status']=='resolved' and family['verdict']=='constructed' and not family['actionable'] and family['depends_on']==['task-anchored-sector-interface']
    assert family['required_verdicts']=={'task-anchored-sector-interface':'constructed'}
    descent=nodes['task-context-readout-descent']
    assert descent['status']=='resolved' and descent['verdict']=='constructed' and not descent['actionable']
    assert descent['depends_on']==['task-cyclic-presentation-family','task-anchored-sector-interface']
    assert descent['required_verdicts']=={key:'constructed' for key in descent['depends_on']}
    invariants=nodes['task-relative-orbit-invariants']
    assert invariants['status']=='open' and invariants['actionable'] and invariants['depends_on']==['task-context-readout-descent']
    assert invariants['required_verdicts']=={'task-context-readout-descent':'constructed'}
    assert interface['depends_on']==['task-decorated-carrier','task-decorated-index-lifts']
    assert interface['required_verdicts']=={k:'constructed' for k in interface['depends_on']} 
    assert nodes['graded-parent-transport']['status']=='open' and not nodes['graded-parent-transport']['depends_on']
    for key in ['horizontal-4d-leaves','fully-coherent-s5','geometric-pn-equivariance','native-four-progressions','native-convex-36-edge-solid']:assert nodes[key]['verdict']=='rejected'
    assert '0<c<1' in nodes['fixed-defect-4d']['statement']
    root=nodes['rung4-instrument-simplex'];assert root['alternative_dependencies']==[['instrument-triangle'],['instrument-tetrahedron']]
    assert 'instrument-triangle' not in root['depends_on'] and 'instrument-tetrahedron' not in root['depends_on']
    for key in ['instrument-vertices','instrument-overlaps','instrument-triangle','instrument-tetrahedron','physical-sector-bindings','field-rung-binding','PNE-solid-construction','PNE-field-sewing','PNE-space-cover','PNE-face-to-face-tiling','global-PNE-field-cover','upward-twelve-paths','postnikov-identification']:assert nodes[key]['status']=='open'
    params=net['candidate_parameters'];assert params['instrument_simplex_dimensions']==[2,3]
    assert params['graded_parent_transport']=={'assembly_required':False,'native_arbitrary_transport_derived':False,'canonical_parent_constructed':False,'monster_gate_activated':False,'baby_monster_action_constructed':False}
    p=params['upward_paths'];assert p['expected_count']==12 and p['max_steps']==3 and not p['verified'];assert all(p[k] is None for k in ['start_end_domain','allowed_transitions','step_cost','path_equivalence'])
    s=params['repeating_shape'];assert not s['arbitrary_centers'] and s['ambient_space'] is None
    assert not any(s[k] for k in ['space_cover_verified','tiling_verified','global_field_sewing_verified'])
    assert set(nodes['integer-field-periodicity']['depends_on'])=={'repeat-contract','PNE-field-sewing','repeat-center-scope'}
    assert 'PNE-space-cover' in nodes['PNE-face-to-face-tiling']['depends_on']
    assert net['verification']=={'registration_only':True,'fresh_scientific_replay':False,'fresh_formal_proof':False,'physical_validation':False,'parent_outcome_admitted':False}
    return nodes,paths

net=json.loads(NET.read_text(encoding='utf8'));nodes,paths=audit(net)
current=json.loads(CURRENT.read_text(encoding='utf8'));assert current['current_contract']==NET.relative_to(ROOT).as_posix() and current['frontier']==net['frontier'] and current['recommended_start']==net['recommended_start']
assert not current['physical_validation'] and current['formal_outcome'] is None
mutations=[]
for name in ['cycle','false_outcome','false_frontier','shortcut_revived','physical_promotion','both_simplex_branches_required','arbitrary_centers','path_count_without_contract','coverage_without_shape','tiling_from_coverage','stale_source_reference','monster_promotion','assembly_required_for_transport','parent_promoted_from_screen','task_symmetry_promoted','carrier_task_dependency_erased','readout_dependency_erased','discrete_carrier_revived']:
    bad=copy.deepcopy(net);bn={n['id']:n for n in bad['conjectures']}
    if name=='cycle':bn['alignment-s5']['depends_on']=['alignment-s5'];bn['alignment-s5']['required_verdicts']={'alignment-s5':'constructed'}
    elif name=='false_outcome':bad['objective']['outcome']='++'
    elif name=='false_frontier':bad['frontier'].append('rung4-instrument-simplex')
    elif name=='shortcut_revived':bn['horizontal-4d-leaves']['verdict']='constructed'
    elif name=='physical_promotion':bn['physical-sector-bindings'].update(status='resolved',verdict='constructed',evidence=['comparison'])
    elif name=='both_simplex_branches_required':bn['rung4-instrument-simplex']['alternative_dependencies']=[['instrument-triangle','instrument-tetrahedron']]
    elif name=='arbitrary_centers':bad['candidate_parameters']['repeating_shape']['arbitrary_centers']=True
    elif name=='path_count_without_contract':bad['candidate_parameters']['upward_paths']['verified']=True
    elif name=='coverage_without_shape':bad['candidate_parameters']['repeating_shape']['space_cover_verified']=True
    elif name=='tiling_from_coverage':bn['PNE-face-to-face-tiling'].update(status='resolved',verdict='constructed',evidence=['shape-screen'])
    elif name=='stale_source_reference':bad['artifacts'][0]['paths'].append('research/strominger/missing-evidence-never-created.json')
    elif name=='monster_promotion':bad['candidate_parameters']['graded_parent_transport']['monster_gate_activated']=True
    elif name=='assembly_required_for_transport':bad['candidate_parameters']['graded_parent_transport']['assembly_required']=True
    elif name=='parent_promoted_from_screen':bn['graded-parent-transport'].update(status='resolved',verdict='constructed',actionable=False)
    elif name=='task_symmetry_promoted':bn['task-symmetry-lift-classification'].update(status='resolved',verdict='constructed')
    elif name=='carrier_task_dependency_erased':bn['task-four-state-extraction'].update(depends_on=[],required_verdicts={})
    elif name=='readout_dependency_erased':bn['task-complete-readouts'].update(depends_on=[],required_verdicts={})
    elif name=='discrete_carrier_revived':bn['task-four-state-extraction']['verdict']='constructed'
    try:audit(bad)
    except AssertionError:mutations.append(name)
    else:raise AssertionError('accepted hostile '+name)
# Read source receipts and check their current direct fingerprints. This is not
# a fresh scientific replay or a formal proof closure.
receipts=[p for p in paths if p.endswith('/verification.json') or p.endswith('/rank-verification.json')]
hashesChecked=0
for p in receipts:
    evidence=json.loads((ROOT/p).read_text(encoding='utf8'))
    for source,digest in evidence.get('sourceHashes',{}).items():
        assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==digest,source
        hashesChecked+=1
comparison=json.loads((ROOT/'research/strominger/results/field-comparison-preparation/verification.json').read_text(encoding='utf8'))
assert comparison['alignmentGeometry']['horizontalCurvatureWitness']=={'0':'2'}
assert comparison['alignmentGeometry']['fixedDefectLevels']['independentProjectorPreservingTangentGeneratorsChecked']==4
shape=json.loads((ROOT/'research/strominger/results/space-filling-36-shape/verification.json').read_text(encoding='utf8'))
assert shape['candidates']['truncated_octahedron']['edges']==36 and shape['nativeGate']['maximumConvexGeometricEdges']==30
count=json.loads((ROOT/'research/strominger/results/native-36-count-screen/verification.json').read_text(encoding='utf8'))
assert nodes['native-baryon-36-grid']['verdict']=='constructed'
assert count['rawDimensions']=={'proton':36,'neutron':36,'electron':8}
assert count['columnBlockSizes']==[12,12,12] and not count['interpretationSelected'] and not count['PNESolidConstructed']
graded=json.loads((ROOT/nodes['graded-parent-transport']['last_execution']['receipt']).read_text(encoding='utf8'))
assert graded['status']=='pass' and not graded['monsterGateActivated'] and not graded['canonicalParentConstructed']
assert not graded['nativeArbitraryTransportDerived'] and not graded['wholeCellAssemblyRequired']
assert [c['dimensions'] for c in graded['gradedCandidates']]==[[1,3,6,10],[1,36,666,8436]]
rigid=json.loads((ROOT/nodes['graded-parent-transport']['followup_execution']['receipt']).read_text(encoding='utf8'))
assert nodes['PN-rigid-copy-transport']['verdict']=='constructed'
assert rigid['rigidCopyCovarianceVerified'] and rigid['freshNativeCoefficientReconstructions']==['proton','neutron']
assert rigid['proton']['rawAbsoluteFramesSingularUnderControlShift']==12 and rigid['neutron']['patches']==18
assert not any(rigid[k] for k in ['nativeArbitraryReaderTransportDerived','electronCovered','exteriorAttachmentSewingVerified','canonicalParentConstructed','monsterGateActivated'])
algebra=json.loads((ROOT/nodes['graded-parent-transport']['operation_algebra_execution']['receipt']).read_text(encoding='utf8'))
assert nodes['declared-simplex-operation-algebra']['verdict']=='constructed'
assert algebra['projectorAlgebra']['dimension']==4 and algebra['combinedGroup']['order']==48
assert not algebra['monsterIdentified'] and not algebra['babyMonsterIdentified'] and not algebra['canonicalParentConstructed']
task=json.loads((ROOT/nodes['task-first-explanatory-constraint']['last_execution']['receipt']).read_text(encoding='utf8'))
assert task['status']=='pass' and task['rivalVerdict']=='rejected' and task['coarseImplementationConstructed']
assert not task['strictTaskPossibleInDeclaredClass'] and task['unitRelativeProbeSquaredResidual']==3
assert len(task['explicitCandidateRotationPairs'])==16 and not task['physicalConstructorEstablished'] and not task['fourStateCarrierDerived']
sufficiency=json.loads((ROOT/nodes['task-four-state-extraction']['last_execution']['receipt']).read_text(encoding='utf8'))
assert sufficiency['status']=='pass' and sufficiency['fourLabelAssignmentsRejected']==1024
assert not sufficiency['fourDiscreteStateExtractionSufficient'] and not sufficiency['fullFieldRecoveryEstablished']
assert sufficiency['requiredDistinctOutputsOnWitnessFamily']==5 and sufficiency['sameSectorWeightsDifferentResidualVectors']
carrier=json.loads((ROOT/nodes['task-decorated-carrier']['last_execution']['receipt']).read_text(encoding='utf8'))
assert carrier['status']=='pass' and carrier['fullVectorsRecoverFixedReferenceField'] and carrier['weightsOnlyLosesRelativePhase']
assert [c['complexRanks'] for c in carrier['carriers']]==[[1,11,2,22],[1,2,11,22]]
assert not carrier['S4FieldLiftEstablished'] and not carrier['fourDiscreteStateClaimRevived']
assert carrier['operatorTransport']['orderedCornerCycleNonzeroOffDiagonalBlocks']==2
lift_result=json.loads((ROOT/nodes['task-decorated-index-lifts']['last_execution']['receipt']).read_text(encoding='utf8'))
assert lift_result['status']=='pass' and lift_result['fixedFieldIndexImages']['P']==[[0,1,2,3]]
assert lift_result['fixedFieldIndexImages']['N']==[[0,1,2,3]] and not lift_result['fullS4FieldLift']
assert lift_result['PNComparison']['rankCompatiblePermutations']==[[0,2,1,3]]
assert lift_result['orderedCornerCycle']['cubeIdentity'] and not lift_result['orderedCornerCycle']['metricUnitary']
interface_result=json.loads((ROOT/nodes['task-anchored-sector-interface']['last_execution']['receipt']).read_text(encoding='utf8'))
assert interface_result['status']=='pass' and interface_result['preparationSquareEqual'] and interface_result['recoverySquareEqual']
assert len(interface_result['comparisonFixtures'])==9 and interface_result['completeBlocksPerFixture']==900
assert interface_result['routeResidualGram']==[[{'1':'3'},{}],[{},{'1':'3'}]]
assert not interface_result['PNGeometricSquareCommutes'] and not interface_result['physicalSewingEstablished']
family_result=json.loads((ROOT/nodes['task-cyclic-presentation-family']['last_execution']['receipt']).read_text(encoding='utf8'))
assert family_result['status']=='pass' and family_result['distinctFullMatrices']==3 and family_result['cyclicReturn']
assert family_result['groupActionCompositions']==9 and family_result['averagedAlignmentRank']==1 and family_result['annihilatedRelativeDimension']==2
assert family_result['anchoredContextPacketsRecovered']==3 and not family_result['fixedEquivariantMapConstructed'] and not family_result['physicalSewingEstablished']
orbit=json.loads((ROOT/nodes['task-context-readout-descent']['last_execution']['receipt']).read_text(encoding='utf8'))
assert orbit['status']=='pass' and orbit['counterexample']['differentFullOrbits']
assert orbit['counterexample']['sameMeanFields'] and orbit['counterexample']['sameMeanComparisonBlocks'] and orbit['counterexample']['sameRetainedPAnchor']
assert len(orbit['negativeControls'])==5 and not orbit['averagedBlocksAcceptedAsCoherentPacket']
assert not orbit['canonicalContextSelected'] and not orbit['PNFixedMapObstructionRepaired']
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
from collect import registry
entry=next(x for x in registry({NET.relative_to(ROOT).as_posix():'owner-local net'})['nets'] if x['contract']==NET.relative_to(ROOT).as_posix())
assert entry['classification']=='conjecture-net contract'
report={'schema':'marici.field-realization-instrument-net-audit.v1','status':'pass','classification':'typed_net_registered_with_open_instrument_crossing_PNE_cover_conjectures','nodeCount':len(nodes),'resolvedConstructed':sum(n['verdict']=='constructed' for n in nodes.values()),'resolvedRejected':sum(n['verdict']=='rejected' for n in nodes.values()),'open':sum(n['status']=='open' for n in nodes.values()),'frontier':net['frontier'],'recommendedStart':net['recommended_start'],'rejectedMutations':mutations,'currentDirectEvidenceHashesChecked':hashesChecked,'collectorRecognizesNet':True,'physicalValidation':False,'freshScientificReplay':False,'formalOutcome':None,'sourceHashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [NET,CURRENT,Path(__file__)]},'evidenceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(paths)}}
out=ROOT/'research/strominger/results/field-realization-instrument-net';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print(json.dumps({k:report[k] for k in ['status','classification','nodeCount','resolvedConstructed','resolvedRejected','open','frontier','recommendedStart','currentDirectEvidenceHashesChecked']}))
