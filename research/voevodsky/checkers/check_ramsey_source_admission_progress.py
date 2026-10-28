"""Keep native path, external compiler and operational-source claims separate."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
LEVEL='mixed safe-Cubical source-observation/compiler proofs and source-bound operational invariants; parity generalization uses a written source-level argument, not kernel JS semantics'
EXPECTED={
 'ramsey-atomic-seed-path':{'singletonPathClosedPolicyAdmitsSwappedSeed':True,'literalRecordEqualityFollowsFromPackageEquality':False},
 'ramsey-observed-comparisons':{'guardedIdentityInverseComposition':True,'visibleBooleanChangeImpossible':True,'allNativeOperationsGuarded':False},
 'ramsey-port-observation-gates':{'sameFacePairs':576,'geometryOnlyRecordIndexSwapAccepted':True,'geometryGuardImpliesRoleLawTransport':False},
 'ramsey-external-pe':{'sourceBoundVertexCompositions':24,'actualMiddleSourceIndexCells':24,'arbitraryNativeDerivationsLifted':False},
 'ramsey-external-seed-policy':{'twoChartPolicyActualTreesAdmitted':24,'baseOnlyActualTreesRefuted':24,'arbitraryNativeResolveImpossibilityClaimed':False},
 'ramsey-origin-zero-source':{'zeroIncrementReachablePacketCount':3,'canonicalComplementOriginZeroReachable':False,'javascriptSemanticsKernelVerified':False},
 'ramsey-role-parity-invariant':{'geometricParityForms':48,'markings':1152,'allOriginConclusionUsesSourceLevelCoverageArgument':True,'javascriptSemanticsKernelVerified':False}}
NAMES=list(EXPECTED)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    pins={};records=[]
    for name,expected in EXPECTED.items():
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d['status']=='passed' and d['parentDescentResolved'] is False and all(d[k]==v for k,v in expected.items())
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale source-admission evidence '+p
            assert p not in pins or pins[p]==h,'conflicting source pin '+p
            pins[p]=h
        relative=path.relative_to(ROOT).as_posix();pins[relative]=sha(path)
        records.append({'receipt':relative,'receipt_sha256':sha(path),'scope_id':d['scope_id'],'checked_fields':expected})
    for path in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v24.md']:
        pins[path.relative_to(ROOT).as_posix()]=sha(path)
    out={'schema':'marici.ramsey-source-admission-progress.verification.v1','status':'passed',
      'scope_id':'external-provenance-and-local-source-admission-boundary-v1','outcome':None,
      'parentResolved':False,'verification_level':LEVEL,'scientific_attempts_replayed':0,'receipt_count':7,
      'evidence_records':records,'source_sha256':pins,'externalFourFacetPolicyChecked':True,
      'rawPackagePathIsOperationalTransition':False,'independentTargetInputsEliminated':False,
      'localSourceParityKernelVerified':False,'allPossibleSourcePoliciesRefuted':False,
      'nextObligation':'audit-declared-marking-symmetry-against-fixed-vertex-observation'}
    (BASE/'results/ramsey-source-admission-progress-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
