"""Consolidate explicit equivariant comparisons without promoting source admission."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
LEVEL='finite runtime marking covariance plus safe-Cubical full permit/occurrence and policy transport; not native source generation or pointwise identity'
EXPECTED={
 'ramsey-marking-symmetry':{'fixedSubdivisionSymmetries':8,'complementaryRoleSymmetries':4,'complementarySymmetriesFixingVertices':0,'operationCovarianceCells':576,'nativeOperationAdded':False},
 'ramsey-diagram-involution':{'canonicalOccurrences':1320,'kernelSelectedIndexBindingCells':144,'kernelWholeDependentTreeEquivalence':False},
 'ramsey-permit-fibers':{'fixedFacetPermitFiberPropositional':True,'canonicalNormalizationCells':12,'distinctFacetCollapseHostileRejected':True},
 'ramsey-permit-equivalence':{'fullPermitEquivalences':8,'arbitraryPermitRoundTrips':8,'canonicalAgreementCells':12,'wrongFacetTransportHostileRejected':True},
 'ramsey-occurrence-equivalence':{'fullOccurrenceEquivalences':24,'arbitrarySourceOriginTransportLaws':24,'selectedOccurrenceAgreementCells':144,'unselectedEPrerequisitesRetained':True,'rawPackageEqualityProved':False},
 'ramsey-policy-transport':{'twoChartGoodTransfers':24,'singletonExchangeTransfers':48,'transportedRestrictedNativeRealizations':24,'nonvacuousSingletonLeafExchange':True,'baseOnlyTargetLeafRefuted':True,'arbitraryNativeResolveTransportClaimed':False}}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
    pins={};records=[]
    for name,expected in EXPECTED.items():
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d['status']=='passed' and d['parentDescentResolved'] is False and d['independentTargetInputsEliminated'] is False
        assert all(d[k]==v for k,v in expected.items()),'scope drift '+name
        if name!='ramsey-marking-symmetry':assert d['freshSafeCubical'] and d['ignoreInterfaces'] and d['inputsStable']
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale equivariant evidence '+p
            assert p not in pins or pins[p]==h,'conflicting pin '+p
            pins[p]=h
        rel=path.relative_to(ROOT).as_posix();pins[rel]=sha(path)
        records.append({'receipt':rel,'receipt_sha256':sha(path),'scope_id':d['scope_id'],'checked_fields':expected})
    for path in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v25.md']:pins[path.relative_to(ROOT).as_posix()]=sha(path)
    return {'schema':'marici.ramsey-equivariant-progress.verification.v1','status':'passed',
      'scope_id':'full-occurrence-and-policy-equivariance-progress-v1','outcome':None,'parentResolved':False,
      'verification_level':LEVEL,'scientific_attempts_replayed':0,'receipt_count':6,
      'evidence_records':records,'source_sha256':pins,'fullOccurrenceTransportChecked':True,
      'nativeSourceGenerationProved':False,'pointwiseVertexIdentityProved':False,
      'singletonMixedChartTreesAdmitted':False,'runtimeMarkingActionKernelVerified':False,
      'nextObligation':'full-edge-permit-restriction-naturality-with-endpoint-order-transport'}
def main():
    out=build();(BASE/'results/ramsey-equivariant-progress-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
