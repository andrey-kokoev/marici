"""Full44 binding/readout squares for the complete Q-rebased reverse certificates."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize
pins={}
def load(path):
    raw=(ROOT/path).read_bytes();pins[path]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def sharp(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def block(a,b):return [row+[R() for _ in b] for row in a]+[[R() for _ in a]+row for row in b]
def main():
    cert=load('research/voevodsky/results/ramsey-complete-reversed-reference-v1.json')
    five=load('research/strominger/results/full-five-channel-candidate/verification.json')
    ne=load('research/strominger/results/neutron-contrast-electron-transport/verification.json')
    pn=load('research/strominger/results/global-PN-transport/verification.json')
    native=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    for report in [cert,five,ne,pn]:
        for path,digest in report.get('source_sha256',report.get('sourceHashes',{})).items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
            pins[path]=digest
    m=list(map(F,native['source']['metric']));metrics=[[F(1)]*44,m+[F(1)]*8,m+[F(1)]*8]
    zeros=[[R() for _ in range(5)] for _ in range(8)]
    B=[restore(five['protonFiveEmbedding'])+zeros,restore(five['neutronFiveEmbedding'])+zeros,restore(five['postNEJointEmbedding'])]
    PN=restore(pn['matrix']);PNinverse=sharp(PN,m)
    K=restore(ne['contrastFrame']);J=restore(ne['electronFrame']);S=restore(ne['NEcandidateMatrix'])
    C=mm(K,sharp(K,m));PE=mm(J,adj(J));Ssharp=mm(K,adj(J))
    W=[r+s for r,s in zip(add(identity(36),C,-1),Ssharp)]+[r+s for r,s in zip(S,add(identity(8),PE,-1))]
    forward=[block(PN,identity(8)),W];backward=[block(PNinverse,identity(8)),W]
    Q=perm(cert['basisMap']);dualB=[mm(b,Q) for b in B]
    dualR=[sharp(b,m) for b,m in zip(dualB,metrics)]
    for b,r in zip(dualB,dualR):assert mm(r,b)==identity(5)
    results=[]
    for edge,(a,b) in enumerate([(0,1),(1,2)]):
        # Source in the reverse direction is b, target is a.
        pi=perm(cert['rows'][0]['dual']['edges'][edge]['permutation'])
        assert mm(backward[edge],dualB[b])==mm(dualB[a],pi)
        assert mm(dualR[a],backward[edge])==mm(pi,dualR[b])
        # The same equations in the forward direction recover the old bindings.
        original=perm(cert['rows'][0]['forward']['edges'][edge]['permutation'])
        assert mm(forward[edge],B[a])==mm(B[b],original)
        results.append({'originalEdge':edge,'dualKind':cert['rows'][0]['dual']['edges'][edge]['kind'],
                        'full44ReadoutSquare':True,'fiveColumnBindingSquare':True})
    # Matrices represent retained co-moving carriers. All24 certificates use
    # exactly these two coefficient maps; no extra geometric covariance inferred.
    for row in cert['rows']:
        assert [e['permutation'] for e in row['dual']['edges']]==[e['permutation'] for e in cert['rows'][0]['dual']['edges']]
        assert row['dualEWindowReferenceSlots']==[2,1,3]
    # Dual E is the old P packet. Its five-slot E readout is exact, but its
    # retained E8 block is zero: do not identify its new role with native E return.
    dualE=dualB[0]
    assert all(x==0 for row in dualE[36:] for x in row)
    assert any(x!=0 for row in dualB[2][36:] for x in row)
    # Wrong inverse-only coefficient convention must fail against the Q basis.
    rawInverse=perm(cert['rows'][0]['forward']['edges'][1]['permutation'])
    assert mm(backward[1],dualB[2])!=mm(dualB[1],rawInverse)
    for path in ['research/voevodsky/checkers/check_ramsey_reversed_certificate_fields.py','research/strominger/checkers/exact_multiradical.py']:
        pins[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
    result={'schema':'marici.ramsey-reversed-certificate-fields.v1','node':'T-seam-based-port-readout-binding','checkerStatus':'passed',
      'scientificStatus':'complete_reference_reversal_and_retained_field_readout_squares_pass',
      'certificateMarkings':24,'matrixScope':'One retained co-moving field candidate, common coefficient maps across24 geometric certificates',
      'edgeChecks':results,'everyPacketRecoversFiveCoefficients':True,
      'dualBindings':[serialize(b) for b in dualB],
      'dualElectronRetainedE8BlockRank':0,
      'remainingCarrierIdentification':'Dual E names the old P packet and retains its P36-plus-E8 carrier. Its E8 block is zero, not the native E rank-two return. These retained carriers are not automatically reidentified with forward native species carriers.',
      'scope':'Positive direction-indexed pullback comparison with complete labels/boundaries and exact readout equations. No new forward native operation, carrier-retyping theorem, arbitrary-assembly coherence or physical reversal law.',
      'netOutcomeChanged':False,'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-reversed-certificate-fields-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['checkerStatus','scientificStatus','certificateMarkings','edgeChecks','everyPacketRecoversFiveCoefficients','dualElectronRetainedE8BlockRank']}))
if __name__=='__main__':main()
