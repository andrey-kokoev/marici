"""Consolidate endpoint results without strengthening the parent or erasing provenance."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
LEVEL='safe-Cubical full edge restriction, scoped selector obstructions and retained endpoint index coherence; not native derivation equality or source generation'
EXPECTED={
 'ramsey-edge-naturality':{'fullEdgePermitEquivalences':12,'arbitraryRestrictionNaturalityLaws':24,'emptyDomainNaturalityLaws':4,'omittedEndpointFlipHostileRejected':True},
 'ramsey-endpoint-policy':{'invariantEdgeOnlySelectorRefuted':True,'chartAwareCovarianceCells':12,'chartAwareSelectionRefuted':False},
 'ramsey-common-selection':{'orderedSharedSelectionCovariant':True,'nonemptyMixedChartWitness':True,'fullWitnessDependentCovariantReversalInvariantSelectorRefuted':True,'retainedBothEndpointComparisonRefuted':False},
 'ramsey-endpoint-family':{'bothEndpointsRetained':True,'arbitraryCommonCovariance':True,'arbitraryPairReversalCompatibility':True,'covarianceReversalPathInterchange':True,'bothEndpointNativeSelections':True,'nativeDerivationProofEqualityClaimed':False,'invariantSingleEndpointSelectionClaimed':False}}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
    pins={};records=[]
    for name,expected in EXPECTED.items():
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d['status']=='passed' and d['parentDescentResolved'] is False and d['independentTargetInputsEliminated'] is False
        assert d['freshSafeCubical'] and d['ignoreInterfaces'] and d['inputsStable']
        assert all(d[k]==v for k,v in expected.items()),'scope drift '+name
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale endpoint evidence '+p
            assert p not in pins or pins[p]==h,'conflicting pin '+p
            pins[p]=h
        rel=path.relative_to(ROOT).as_posix();pins[rel]=sha(path)
        records.append({'receipt':rel,'receipt_sha256':sha(path),'scope_id':d['scope_id'],'checked_fields':expected})
    for path in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v26.md']:pins[path.relative_to(ROOT).as_posix()]=sha(path)
    return {'schema':'marici.ramsey-endpoint-progress.verification.v1','status':'passed',
      'scope_id':'retained-endpoint-coherence-and-selection-boundaries-v1','outcome':None,'parentResolved':False,
      'verification_level':LEVEL,'scientific_attempts_replayed':0,'receipt_count':4,'evidence_records':records,'source_sha256':pins,
      'retainedEndpointIndexCoherenceChecked':True,'nativeDerivationEqualityProved':False,
      'invariantSingletonSelectionProved':False,'singletonSelectionRequiredByParent':False,
      'nativeSourceGenerationProved':False,'nextObligation':'triple-common-projection-and-endpoint-naturality'}
def main():
    out=build();(BASE/'results/ramsey-endpoint-progress-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
