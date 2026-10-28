"""Full-image invariant-core certificate, with separate moving-domain repair."""
from check_ramsey_prepared_edge_locality import ROOT,V,S,load,sha,restore,R,F,mm,serialize,identity,sharp
import json

def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
      -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
      +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def main():
    paths=[V+'results/ramsey-signed-domain-transport-v1.json',V+'results/ramsey-edge-trace-descent-v1.json',
      S+'full-five-channel-candidate/verification.json',S+'common-three-carrier-protocol/proton.json']
    transport,signed,five,proton=[load(p) for p in paths]
    for d,key in [(transport,'source_sha256'),(signed,'source_sha256'),(five,'sourceHashes')]:
        for p,h in d[key].items():assert sha(p)==h,'stale invariant-core input '+p
    b=mm(restore(five['protonFiveEmbedding']),restore(signed['signedEqualizerEmbedding']))
    metric=list(map(F,proton['source']['metric']));left=sharp(b,metric)
    assert mm(left,b)==identity(3)
    r=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)]
    powers=[identity(36),r,mm(r,r)];assert mm(powers[2],r)==identity(36)
    rb=mm(r,b);projected=mm(b,mm(left,rb));residual=sub(rb,projected)
    minor=residual[:3];det=det3(minor)
    assert det==R({3:F(-5,486)}) and det!=R()
    # L B=I makes B L an exact projector onto image(B). E x=0 iff
    # R B x belongs to image(B). The nonzero minor forces x=0.
    assert mm(b,mm(left,b))==b
    domains=[mm(power,b) for power in powers]
    decoders=[mm(left,powers[(-t)%3]) for t in range(3)]
    for t in range(3):assert mm(decoders[t],domains[t])==identity(3)
    squares=triangles=0
    for t in range(3):
        for u in range(3):
            action=powers[(u-t)%3]
            assert mm(action,domains[t])==domains[u]
            assert mm(decoders[u],action)==decoders[t]
            squares+=1
            for v in range(3):
                assert mm(powers[(v-u)%3],action)==powers[(v-t)%3];triangles+=1
    files=paths+[V+'contracts/ramsey-signed-invariant-core-attempt.v1.json',V+'checkers/check_ramsey_signed_invariant_core.py',
      V+'checkers/check_ramsey_prepared_edge_locality.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-signed-invariant-core.verification.v1','status':'passed',
      'scope_id':'actual-proton-sector-invariant-core-of-signed-preparation-v1',
      'verification_level':'exact multiradical full-image residual and nonzero minor; no new kernel numerical interpretation',
      'preparedEmbedding':serialize(b),'metricLeftInverse':serialize(left),
      'membershipResidual':serialize(residual),'rankCertificateRows':[0,1,2],
      'rankCertificateMinor':serialize(minor),'rankCertificateDeterminant':det.record(),
      'membershipResidualRank':3,'intersectionWithFirstRotatedImageDimension':0,
      'maximalActualSectorInvariantSubspaceDimension':0,'allPairwiseMovingImageIntersectionsDimension':0,
      'movingDomainDimensions':[3,3,3],'movingEmbeddings':[serialize(x) for x in domains],
      'movingDecoders':[serialize(x) for x in decoders],'movingPairSquares':squares,'movingCompositionTriangles':triangles,
      'movingDomainIsFixedPreparation':False,'signedConventionSourceSelected':False,
      'allHigherContextPoliciesRefuted':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-signed-invariant-core-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','preparedEmbedding','metricLeftInverse','membershipResidual','rankCertificateMinor','movingEmbeddings','movingDecoders']},indent=2))
if __name__=='__main__':main()
