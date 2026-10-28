"""Consolidate constructor comparisons without promoting their relation to equality."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
LEVEL='safe-Cubical actual route, canonical P/E constructor and occurrence comparisons; owner-local native relation, not arbitrary derivation equality or source generation'
EXPECTED={
 'ramsey-triple-naturality':{'edgeProjectionLaws':3,'vertexProjectionLaws':3,'projectionPathInterchangeLaws':3,'differentEdgeFourFacetSeamsCovered':False},
 'ramsey-different-edge-transport':{'actualDifferentEdgeRouteCells':72,'transportedMiddleIndexSeams':24,'existingTargetNativeMiddleSeamsChecked':24,'nativeDerivationTransportProved':False},
 'ramsey-pe-constructor-comparison':{'genericConstructorComparisonCompiler':True,'actualCompiledNativeProofIndices':True,'allSelectionPremisesCompared':True,'nativeComparisonIsOwnerLocalRelation':True,'actualFourFacetComparisonInstantiated':False},
 'ramsey-four-facet-constructor':{'actualConstructorComparisons':24,'actualCompiledNativeComparisons':24,'compiledMiddleDerivationSeams':24,'middlePremiseComparisons':48,'middleComparisonAgreementCells':24,'wholeNativeDerivationEqualityClaimed':False},
 'ramsey-constructor-occurrence-agreement':{'arbitraryOccurrenceAgreementLaws':24,'dependentSourceWitnessAgreementLaws':24,'inducedOccurrenceEquivalences':24,'constructorCorrespondenceRoundTripEqualityClaimed':False}}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
    pins={};records=[]
    for name,expected in EXPECTED.items():
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d['status']=='passed' and d['parentDescentResolved'] is False and d['independentTargetInputsEliminated'] is False
        assert d['freshSafeCubical'] and d['ignoreInterfaces'] and d['inputsStable']
        assert all(d[k]==v for k,v in expected.items()),'scope drift '+name
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale constructor evidence '+p
            assert p not in pins or pins[p]==h,'conflicting pin '+p
            pins[p]=h
        rel=path.relative_to(ROOT).as_posix();pins[rel]=sha(path)
        records.append({'receipt':rel,'receipt_sha256':sha(path),'scope_id':d['scope_id'],'checked_fields':expected})
    for path in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v27.md']:pins[path.relative_to(ROOT).as_posix()]=sha(path)
    return {'schema':'marici.ramsey-constructor-progress.verification.v1','status':'passed',
      'scope_id':'actual-constructor-and-occurrence-comparison-progress-v1','outcome':None,'parentResolved':False,
      'verification_level':LEVEL,'scientific_attempts_replayed':0,'receipt_count':5,'evidence_records':records,'source_sha256':pins,
      'actualConstructorOccurrenceAgreementChecked':True,'nativeRelationPromotedToEquality':False,
      'arbitraryNativeResolveTransportProved':False,'nativeSourceGenerationProved':False,
      'nextObligation':'constructor-induced-policy-transfer-and-particular-realization-agreement'}
def main():
    out=build();(BASE/'results/ramsey-constructor-progress-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
