"""Separate transported species domains from the actual source sector action."""
from check_ramsey_prepared_edge_locality import ROOT,V,S,load,sha,restore,R,mm,serialize,identity
import json

def main():
    paths=[V+'results/ramsey-edge-trace-descent-v1.json',V+'results/ramsey-geometric-edge-readout-v1.json',
      S+'full-five-channel-candidate/verification.json',V+'results/ramsey-trace-channel-transport-v1.json']
    signed,edge,five,transport=[load(p) for p in paths]
    for d,key in [(signed,'source_sha256'),(edge,'source_sha256'),(five,'sourceHashes'),(transport,'source_sha256')]:
        for p,h in d[key].items():assert sha(p)==h,'stale action input '+p
    p=[[R(int(j==[3,1,2,0,4][i])) for j in range(5)] for i in range(5)]
    c=[[R(int(j==[0,3,1,2,4][i])) for j in range(5)] for i in range(5)]
    w=restore(signed['signedEqualizerEmbedding']);nw=mm(p,w);loop=mm(p,mm(c,p))
    assert mm(p,p)==identity(5) and mm(c,mm(c,c))==identity(5)
    # Column extraction gives the internal action, no assumed commutation square.
    internal=mm(loop,w)[:3]
    assert mm(loop,w)==mm(w,internal)
    assert mm(c,nw)==mm(nw,internal)
    assert mm(internal,mm(internal,internal))==identity(3)
    assert all(x==R() for i in [0,4] for x in nw[i])
    bp=restore(five['protonFiveEmbedding']);bn=restore(five['neutronFiveEmbedding'])
    rotation=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)]
    assert mm(rotation,bn)==mm(bn,c)
    physical=mm(bp,w);rotated=mm(rotation,physical);induced=mm(bp,mm(loop,w))
    assert rotated!=induced
    h=restore(edge['readout']);before=mm(h,physical);after=mm(h,rotated)
    sumrows=lambda a:[[x+y for x,y in zip(a[i],a[i+1])] for i in range(0,12,2)]
    assert all(x==R() for row in sumrows(before) for x in row)
    discrepancy=sumrows(after);assert any(x!=R() for row in discrepancy for x in row)
    i,j=next((i,j) for i,row in enumerate(discrepancy) for j,x in enumerate(row) if x!=R())
    k=[[R(int(t==j))] for t in range(5)]
    state=mm(bp,k);future=mm(rotation,state)
    assert sumrows(mm(h,state))==[[R()] for _ in range(6)]
    value=sumrows(mm(h,future))[i][0];assert value==discrepancy[i][j]!=R()
    # A nonzero signed discrepancy also proves this state is outside Bp(W),
    # since every element of Bp(W) satisfies all the signed equalities.
    files=paths+[V+'contracts/ramsey-signed-domain-transport-attempt.v1.json',
      V+'checkers/check_ramsey_signed_domain_transport.py',V+'checkers/check_ramsey_prepared_edge_locality.py',
      'research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-signed-domain-transport.verification.v1','status':'passed',
      'scope_id':'signed-edge-domain-under-species-aware-and-source-sector-actions-v1',
      'verification_level':'exact multiradical source action and coefficient transport checks; no new kernel replay',
      'protonDomain':serialize(w),'transportedNeutronDomain':serialize(nw),
      'neutronDomainEquations':['coefficient[0] = 0','coefficient[4] = 0'],
      'PNCoefficientAction':serialize(p),'neutronSectorCoefficientAction':serialize(c),
      'protonLoopCoefficientAction':serialize(loop),'domainInternalCycle':serialize(internal),
      'speciesAwareLoopPreservesSignedDomain':True,'neutronSectorIntertwinerChecked':True,
      'actualProtonSectorEqualsPNConjugatedNeutronAction':False,
      'actualProtonSectorPreservesSignedDomain':False,
      'witness':{'preparedCoefficientBasis':j,'edge':edge['descriptors'][2*i]['edge'],
        'initialSignedDiscrepancy':{},'afterOneSourceSectorCycle':value.record(),
        'fullPreparedState':serialize(state),'rotatedState':serialize(future)},
      'rotatedSignedDiscrepancyOnDomain':serialize(discrepancy),
      'sameCoordinateDomainRequiredAcrossSpecies':False,'signedConventionSourceSelected':False,
      'allHigherContextPoliciesRefuted':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-signed-domain-transport-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','witness','rotatedSignedDiscrepancyOnDomain','protonDomain','transportedNeutronDomain','PNCoefficientAction','neutronSectorCoefficientAction','protonLoopCoefficientAction','domainInternalCycle']},indent=2))
if __name__=='__main__':main()
