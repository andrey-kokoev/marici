"""Consolidate scoped evidence without manufacturing a parent scientific outcome."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
NAMES=['ramsey-complementary-sewing','ramsey-marked-sewing-replay-diagnosis',
 'ramsey-world-frame-action','ramsey-neutron-world-action','ramsey-moving-carrier-PN',
 'ramsey-moving-carrier-NE','ramsey-NE-lift-context','ramsey-lifted-facet-incidence',
 'ramsey-native-incidence','ramsey-geometric-edge-readout','ramsey-prepared-edge-locality',
 'ramsey-minimal-edge-context','ramsey-trace-only-context-channel','ramsey-trace-channel-transport',
 'ramsey-retained-observation','ramsey-native-derived-comparison','ramsey-source-bound-comparison',
 'ramsey-native-field-interpretation']
GATES=['concrete_numerical_frame_equivalences_not_kernel_instantiated',
 'retained_comparison_context_not_physical_role_transport',
 'off_edge_observation_support_not_local_geometric_restriction',
 'full_face_chart_descent_acceptance_not_established']
LEVEL='mixed safe-Cubical generic constructors/semantic bridge and source-bound exact runtime evidence; pinned receipts, not replayed here'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    records=[];pins={}
    for name in NAMES:
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d.get('source_sha256'),name+' missing input bindings'
        for relative,h in d['source_sha256'].items():
            assert sha(ROOT/relative)==h,'stale progress source '+relative
            if relative in pins:assert pins[relative]==h,'incompatible receipts '+relative
            pins[relative]=h
        relative=path.relative_to(ROOT).as_posix();pins[relative]=sha(path)
        records.append({'receipt':relative,'receipt_sha256':sha(path),'scope_id':d.get('scope_id'),
                        'recorded_status':d.get('status'),'recorded_outcome':d.get('outcome')})
    field=json.loads((BASE/'results/ramsey-native-field-interpretation-v1.json').read_text())
    source=json.loads((BASE/'results/ramsey-source-bound-comparison-v1.json').read_text())
    assert field['genericNativeSemanticSquare'] and field['runtimeFrameTriangles']==64
    assert not field['actualNumericalFrameEquivalencesKernelInstantiated'] and not field['parentDescentResolved']
    assert source['nativeComparisons']==16 and source['nativeCompositions']==64
    assert source['payloadOmissionRejected'] and not source['kernelMatrixInterpretation']
    for path in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v20.md']:
        pins[path.relative_to(ROOT).as_posix()]=sha(path)
    out={'schema':'marici.ramsey-face-descent-progress.verification.v1','status':'passed',
      'scope_id':'four-port-retained-incidence-and-conditional-field-interpretation-v1',
      'parent':'face-chart-transition-descent','outcome':None,'parentResolved':False,
      'verification_level':LEVEL,'scientific_attempts_replayed':0,'receipt_count':len(records),
      'evidence_records':records,'unresolved_gates':GATES,
      'kernelGenericComparisonAndSemanticSquare':True,'runtimeBoundFrameComparisons':16,
      'runtimeBoundFrameTriangles':64,'concreteNumericalKernelInstantiation':False,
      'physicalRoleTransport':False,'localFieldGluing':False,'RamseyForcing':False,
      'source_sha256':pins}
    (BASE/'results/ramsey-face-descent-progress-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
