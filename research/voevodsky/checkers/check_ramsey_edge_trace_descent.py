"""Exact prepared paired-trace fibers, before neutron transport or compression."""
from check_ramsey_prepared_edge_locality import ROOT,V,S,load,sha,restore,R,mm,serialize
import json

def witness(a,b):
    # Find k with a k=0 and b k!=0, without numerical inversion.
    for i in range(5):
        for j in range(i+1,5):
            if a[i]*b[j]-a[j]*b[i]!=R():
                k=[[R()] for _ in range(5)];k[i]=[a[j]];k[j]=[-a[i]]
                assert mm([a],k)==[[R()]]
                value=mm([b],k);assert value!=[[R()]]
                return {'coefficientVector':serialize(k),'forgottenTrace':serialize(mm([a],k)),
                        'requiredTrace':serialize(value),'minorCoordinates':[i,j]}
    return None

def main():
    paths=[V+'results/ramsey-geometric-edge-readout-v1.json',S+'full-five-channel-candidate/verification.json']
    edge,five=[load(p) for p in paths]
    for d,key in [(edge,'source_sha256'),(five,'sourceHashes')]:
        for p,h in d[key].items():assert sha(p)==h,'stale field source '+p
    prepared=mm(restore(edge['readout']),restore(five['protonFiveEmbedding']))
    results=[];sums=[]
    for i in range(0,12,2):
        a,b=prepared[i:i+2];da,db=edge['descriptors'][i:i+2]
        assert da['edge']==db['edge'] and da['parentFace']!=db['parentFace']
        forward=witness(a,b);reverse=witness(b,a)
        assert (forward is None)==(reverse is None)
        if forward is None:assert all(x+y==R() for x,y in zip(a,b))
        row=[x+y for x,y in zip(a,b)];sums.append(row)
        results.append({'edge':da['edge'],'occurrences':[da,db],
          'preparedPairRank':2 if forward else 1,'forwardNonfactorWitness':forward,
          'reverseNonfactorWitness':reverse,'oppositeSignEqualityOnFullPreparation':not any(x!=R() for x in row)})
    assert [r['edge'] for r in results if r['preparedPairRank']==2]==['AB','AC','AD','BC','BD']
    assert results[-1]['edge']=='CD' and results[-1]['oppositeSignEqualityOnFullPreparation']
    # Every signed discrepancy depends only on the two added channels.
    assert all(row[j]==R() for row in sums for j in range(3))
    ab=sums[0];ad=sums[2]
    assert ab[3]!=R() and ab[4]==R()
    assert ad[3]==R() and ad[4]!=R()
    # These two independent pivot equations force both added coefficients to zero.
    signed_domain=[[R(int(i==j)) for j in range(3)] for i in range(5)]
    assert mm(sums,signed_domain)==[[R() for _ in range(3)] for _ in range(6)]
    assert all(mm([prepared[i]],signed_domain)==[[-x for x in mm([prepared[i+1]],signed_domain)[0]]] for i in range(0,12,2))
    files=paths+[V+'contracts/ramsey-edge-trace-descent-attempt.v1.json',V+'checkers/check_ramsey_edge_trace_descent.py',
      V+'checkers/check_ramsey_prepared_edge_locality.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-edge-trace-descent.verification.v1','status':'passed',
      'scope_id':'prepared-proton-paired-edge-trace-factorization-v1',
      'verification_level':'exact multiradical runtime matrices and explicit fiber witnesses; no new kernel replay',
      'preparedReadout':serialize(prepared),'edges':results,'nonfactorEdges':5,'bothDirectionsWitnessed':True,
      'signedDiscrepancyRows':serialize(sums),'signedEqualizerRank':2,'signedEqualizerDimension':3,
      'signedEqualizerEquations':['coefficient[3] = 0','coefficient[4] = 0'],
      'independentPivotEdges':['AB','AD'],'signedEqualizerEmbedding':serialize(signed_domain),
      'signedConventionSourceSelected':False,'fullFiveChannelScalarEdgeGluing':False,
      'pairedRetainedObservationsRefuted':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-edge-trace-descent-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['preparedReadout','edges','signedDiscrepancyRows','source_sha256']},indent=2))
if __name__=='__main__':main()
