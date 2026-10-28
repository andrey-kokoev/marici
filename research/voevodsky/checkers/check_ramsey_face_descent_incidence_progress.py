"""Consolidate retained incidence and its semantic boundaries without verdict promotion."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
LEVEL='mixed safe-Cubical retained incidence cells and exact finite/field boundary checks; pinned receipts, not replayed here'
EXPECTED={
 'ramsey-signed-invariant-core':{'maximalActualSectorInvariantSubspaceDimension':0,'movingPairSquares':9,'movingCompositionTriangles':27},
 'ramsey-moving-edge-geometry':{'geometricRelabelingsPerFrame':24,'nontrivialFramesAreFixedGeometryEdgeRelabelings':False},
 'ramsey-edge-observation-closure':{'closedObservationDimension':36,'discardedFieldDimension':0},
 'ramsey-edge-law-domain':{'identityEdgeDomainInclusions':96,'identityEdgeDomainFailures':480},
 'ramsey-native-edge-attachments':{'sourceBoundEdgeAttachments':144,'endpointRestrictionAdmissionMap':True,'allDerivationsTransportAlongAdmissionMap':True},
 'ramsey-four-facet-vertex-cells':{'directedNativeEdgeSelections':12,'nativeVertexTripleCompositions':24,'differentEdgeRestrictionCells':72,'fullMiddleDerivationSeams':24},
 'ramsey-attachment-fiber-equivalence':{'selectedCoverEdgeCardinalitiesAgree':True,'selectedCoverVertexTriplesWithMixedCardinalities':24,'parentRequiresCompleteFiberEquivalenceAsserted':False}}
NAMES=list(EXPECTED)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    pins={};records=[]
    for name,expected in EXPECTED.items():
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d['status']=='passed' and d['parentDescentResolved'] is False
        assert all(d[k]==v for k,v in expected.items())
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale incidence progress '+p
            assert p not in pins or pins[p]==h,'conflicting source '+p
            pins[p]=h
        relative=path.relative_to(ROOT).as_posix();pins[relative]=sha(path)
        records.append({'receipt':relative,'receipt_sha256':sha(path),'scope_id':d['scope_id'],'checked_fields':expected})
    for p in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v22.md']:
        pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-face-descent-incidence-progress.verification.v1','status':'passed',
      'scope_id':'retained-four-facet-incidence-and-transition-semantics-audit-v1',
      'outcome':None,'parentResolved':False,'verification_level':LEVEL,'scientific_attempts_replayed':0,
      'receipt_count':7,'evidence_records':records,'source_sha256':pins,
      'retainedFourFacetVertexDiagramChecked':True,'completeChoiceFiberEquivalenceClaimed':False,
      'scalarConventionRequiredByParent':False,'retainedSpanIdentifiedWithEquivalence':False,
      'nextObligation':'classify-retained-correspondence-composition-and-round-trip-identities'}
    (BASE/'results/ramsey-face-descent-incidence-progress-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
