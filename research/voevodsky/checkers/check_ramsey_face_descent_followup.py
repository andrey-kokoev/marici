"""Pin the request/semantic-restriction continuation, without a parent verdict."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
NAMES=['ramsey-comparison-forgetting','ramsey-port-completion','ramsey-requested-port','ramsey-edge-trace-descent','ramsey-signed-domain-transport']
LEVEL='mixed safe-Cubical request/factorization proofs and exact runtime restriction/action witnesses; pinned receipts, not replayed here'
EXPECTED={
 'ramsey-comparison-forgetting':{'actualFixedPolicySourceOnlyFactorExists':True,'sourceGeneratedNativeRoleTransportProved':False},
 'ramsey-port-completion':{'admissiblePairs':576,'requestedChartAccepted':576,'requestedChartRefused':576},
 'ramsey-requested-port':{'kernelComputedRequests':1152,'kernelAccepted':576,'kernelRefused':576,'nativeSpanSelectorReused':True},
 'ramsey-edge-trace-descent':{'nonfactorEdges':5,'signedEqualizerDimension':3,'signedEqualizerRank':2},
 'ramsey-signed-domain-transport':{'speciesAwareLoopPreservesSignedDomain':True,'actualProtonSectorEqualsPNConjugatedNeutronAction':False,'actualProtonSectorPreservesSignedDomain':False}}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    pins={};records=[]
    for name in NAMES:
        path=BASE/'results'/(name+'-v1.json');d=json.loads(path.read_text())
        assert d['status']=='passed' and d['parentDescentResolved'] is False
        assert all(d[k]==v for k,v in EXPECTED[name].items())
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale continuation '+p
            assert p not in pins or pins[p]==h,'conflicting pin '+p
            pins[p]=h
        relative=path.relative_to(ROOT).as_posix();pins[relative]=sha(path)
        records.append({'receipt':relative,'receipt_sha256':sha(path),'scope_id':d['scope_id'],'checked_fields':EXPECTED[name]})
    for p in [Path(__file__),BASE/'ramsey-face-descent-consolidation-v21.md']:
        pins[p.relative_to(ROOT).as_posix()]=sha(p)
    out={'schema':'marici.ramsey-face-descent-followup.verification.v1','status':'passed',
      'scope_id':'requested-port-interface-and-semantic-restriction-audit-v1','outcome':None,
      'parentResolved':False,'verification_level':LEVEL,'scientific_attempts_replayed':0,
      'receipt_count':5,'evidence_records':records,'source_sha256':pins,
      'sameFaceRequestInterfaceChecked':True,'fullPreparedScalarEdgeDescent':False,
      'fixedSignedThreeDimensionalDomainClosed':False,'allContextIndexedPoliciesRefuted':False,
      'nextObligation':'actual-proton-sector-invariant-subspace-or-explicit-moving-domain'}
    (BASE/'results/ramsey-face-descent-followup-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','evidence_records']},indent=2))
if __name__=='__main__':main()
