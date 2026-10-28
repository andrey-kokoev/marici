"""Actual paired geometric traces and native PN edge locality for the U(2) family.
Connection: face-chart-transition-descent overlap/law-domain acceptance;
joint44-native-source-selection retained-family/independent-reader acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys
from check_ramsey_passive_EP_semantics import ROOT,load,restore,perm,minus,nz,pins,sha
from exact_multiradical import Radical as R,mm,adj,identity,serialize
from check_ramsey_edge_trace_descent import witness

def main():
    moving=load('research/voevodsky/results/ramsey-moving-EP-preparation-v1.json')
    semantic=load('research/voevodsky/results/ramsey-passive-EP-semantics-v1.json')
    edge=load('research/voevodsky/results/ramsey-geometric-edge-readout-v1.json')
    locality=load('research/voevodsky/results/ramsey-prepared-edge-locality-v1.json')
    priorTraces=load('research/voevodsky/results/ramsey-edge-trace-descent-v1.json')
    five=load('research/strominger/results/full-five-channel-candidate/verification.json')
    pn=load('research/strominger/results/global-PN-transport/verification.json')
    nd=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    H=restore(edge['readout']);W=restore(edge['edgeAction'])
    G=restore(next(t['geometricMap'] for t in semantic['tests'] if t['convention']=='co_moving_tetrahedral_frame'))
    BE=mm(restore(five['protonFiveEmbedding']),perm([4,3,2,1,0]))
    # Reference member of the compatible family. Every other member is its
    # right-unitary context-frame change, not a different preparation subspace.
    T=perm([3,4,2,0,1]);BP=mm(mm(G,BE),adj(T))
    PN=restore(pn['matrix']);Pi=perm([3,1,2,0,4]);m=list(map(F,nd['source']['metric']))
    def sharp(A):return [[v*m[j] for j,v in enumerate(row)] for row in adj(A)]
    PNi=sharp(PN);BN=mm(mm(PN,BP),adj(Pi))
    assert mm(PNi,PN)==identity(36) and mm(sharp(BN),BN)==identity(5)
    # This equation uses the saved geometric rows, not newly defined moving readers.
    assert mm(H,G)==mm(W,H)
    assert mm(W,W)==identity(12) and mm(adj(W),W)==identity(12)
    # Check geometric edge AND parent-face labels, including orientation sign.
    rename=dict(zip('ABCD','BADC'));bindings=[]
    for old,d in enumerate(edge['descriptors']):
        new=next(i for i in range(12) if W[i][old]!=0);target=edge['descriptors'][new]
        assert target['edge']==''.join(sorted(rename[v] for v in d['edge']))
        assert target['patch']==''.join(rename[v] for v in d['patch'])
        assert target['parentFace']=='F_'+''.join(sorted(rename[v] for v in d['parentFace'][2:]))
        sign=1 if rename[d['edge'][0]]<rename[d['edge'][1]] else -1
        assert W[new][old]==R(sign)
        bindings.append({'source':d,'target':target,'orientationSign':sign})
    prepared=mm(H,BP)
    assert mm(prepared,T)==mm(W,mm(H,BE))
    pulled=mm(H,PNi)
    assert pulled==restore(edge['PNPulledReadout'])
    assert mm(pulled,PN)==H
    assert mm(pulled,BN)==mm(prepared,adj(Pi))
    pairs=[]
    for i in range(0,12,2):
        a,b=prepared[i:i+2];forward,back=witness(a,b),witness(b,a)
        assert (forward is None)==(back is None)
        summed=[x+y for x,y in zip(a,b)]
        if forward is None:assert all(v==0 for v in summed)
        pairs.append({'edge':edge['descriptors'][i]['edge'],
          'parentFaces':[edge['descriptors'][i]['parentFace'],edge['descriptors'][i+1]['parentFace']],
          'pairRank':2 if forward else 1,'oppositeSignEquality':not any(v!=0 for v in summed),
          'forwardNonfactorWitness':forward,'reverseNonfactorWitness':back})
    assert [p['edge'] for p in pairs if p['pairRank']==2]==['AB','AC','AD','BC','BD']
    assert pairs[-1]['edge']=='CD' and pairs[-1]['oppositeSignEquality']
    # Strict native local-instrument test, not the dense PN pullback readout.
    localSlots=locality['localIntrinsicSlots'];assert localSlots==[0,1,6,7]
    local=[BN[i] for i in localSlots]
    rows=[i for i,d in enumerate(edge['descriptors']) if d['edge']=='CD'];assert len(rows)==2
    desired=mm([prepared[i] for i in rows],adj(Pi))
    j=2 # an active N coefficient, hence fixed by every context U(2)
    assert all(row[j]==0 for row in local)
    assert any(row[j]!=0 for row in desired)
    state=[[row[j]] for row in BN]
    assert mm(sharp(state),state)==[[R(1)]]
    lost={'neutronCoefficientSlot':j,'localReadout':serialize([[row[j]] for row in local]),
      'requiredPairedCDReadout':serialize([[row[j]] for row in desired]),'fullPreparedNormSquared':1,
      'unchangedForEveryContextUnitary':True}
    # Prepared-domain repair with the already declared three-sector instrument.
    # Its support is three geometric edges, not one edge renamed as a larger one.
    expandedSlots=locality['expandedSlots'];assert len(expandedSlots)==12
    expanded=[BN[i] for i in expandedSlots];em=[m[i] for i in expandedSlots]
    esharp=[[v*em[k] for k,v in enumerate(row)] for row in adj(expanded)]
    gram=mm(esharp,expanded)
    # The old diagonal-Gram decoder is NOT reusable: moving context modes
    # have cross terms in this restricted instrument. Use the exact adjugate.
    assert any(gram[i][j]!=0 for i in [1,2,3] for j in [0,4])
    def determinant(A):
        if not A:return R(1)
        return sum(((-1 if j%2 else 1)*v*determinant([row[:j]+row[j+1:] for row in A[1:]])
                    for j,v in enumerate(A[0]) if v!=0),R())
    denominator=determinant(gram);assert denominator!=0
    adjugate=[[(-1 if (i+j)%2 else 1)*determinant([[gram[a][b] for b in range(5) if b!=i]
                 for a in range(5) if a!=j]) for j in range(5)] for i in range(5)]
    assert mm(adjugate,gram)==[[denominator*v for v in row] for row in identity(5)]
    assert all(row[0]==row[4]==0 for row in desired)
    decoderNumerator=mm(adjugate,esharp)
    assert mm(decoderNumerator,expanded)==[[denominator*v for v in row] for row in identity(5)]
    enlargedNumerator=mm(desired,decoderNumerator)
    assert mm(enlargedNumerator,expanded)==[[denominator*v for v in row] for row in desired]
    omitted=[]
    for group in range(3):
        kept=[row for i,row in enumerate(expanded) if i//4!=group]
        missing=next(k for k in [1,2,3] if all(row[k]==0 for row in kept))
        assert any(row[missing]!=0 for row in desired)
        omitted.append({'omittedSector':group,'lostActiveCoefficient':missing,
          'remainingTwoSectorEdgesInsufficient':True})
    repair={'supportSlots':expandedSlots,'distinctGeometricEdges':locality['expandedDistinctGeometricEdges'],
      'readoutNumerator':serialize(enlargedNumerator),'nonzeroDenominator':denominator.record(),
      'representation':'readout = numerator / denominator; identity checked after multiplying by the exact nonzero denominator',
      'oldDiagonalGramDecoderApplicable':False,'preparedFactorization':True,
      'fiveCoefficientDecoderNumerator':serialize(decoderNumerator),'allFivePreparedCoefficientsRecoverable':True,
      'allTwelvePairedTracesRecoverableOnPreparedDomain':True,
      'allThreeSectorEdgesNecessaryWithinThisInstrumentFamily':omitted,
      'edgeLocal':False,'validForAllContextU2':True}
    # Both surviving permutation members give identical active-column witness.
    second=perm([3,4,2,1,0]);BP2=mm(mm(G,BE),adj(second));BN2=mm(mm(PN,BP2),adj(Pi))
    assert [[row[j]] for row in BN2]==state
    # For arbitrary U on P slots3,4, Pi transports U to N slots0,4,
    # so active column2 and the locality witness cannot be changed by U.
    assert Pi[0][3]==Pi[4][4]==R(1) and Pi[2][2]==R(1)
    # All pair ranks and failure/success of equality/factorization are invariant
    # under a shared invertible right action on their five coefficient columns.
    # Display one nontrivial member as a regression, not a universal substitute.
    assert mm(BP2,adj(BP2))==mm(BP,adj(BP))
    controls=['wrong scalar identification rejected by exact pair minors',
      'single native uv-edge instrument rejected by active unit-vector witness',
      'dense PN pullback not misreported as edge-local support',
      'context gauge cannot change an active coefficient column']
    for module in list(sys.modules.values()):
        filename=getattr(module,'__file__',None)
        if filename:
            try:rel=Path(filename).resolve().relative_to(ROOT).as_posix()
            except ValueError:continue
            pins[rel]=sha(rel)
    rel=Path(__file__).relative_to(ROOT).as_posix();pins[rel]=sha(rel)
    out={'status':'passed','node':'face-chart-transition-descent',
      'scope':'actual saved paired proton edge traces and sector0 native uv-edge instrument, under the moving-preparation U(2) family; not all possible detectors',
      'geometricFaceEdgeBindings':bindings,'full36RetainedTraceCovariance':True,
      'full36PNPullbackSquare':True,'geometricVertexRenamingIsCoordinateChangeNotPNPermit':True,
      'preparedPairedReadout':serialize(prepared),'edges':pairs,
      'scalarPairFactorizationFailsOnFiveEdgesForEveryU':True,
      'nativeSingleEdgeFactorization':False,'localInstrumentSlots':localSlots,
      'uniformLocalityCounterexample':lost,'threeEdgeRepair':repair,'PNPullbackSupportCounts':edge['PNPullbackCoordinateSupportCounts'],
      'controls':controls,'parentResolved':False,'owningNativePolicyChanged':False,
      'verification':'exact multiradical runtime checks and written all-U right-unitary argument; no fresh formal-kernel claim',
      'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-moving-EP-edge-restrictions-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'passed','retainedTraceCovariance':True,'PNPullbackSquare':True,
      'rankTwoEdges':[p['edge'] for p in pairs if p['pairRank']==2],
      'uniformLocalityWitness':lost,'threeEdgeRepairPasses':True,'remainingU2SelectedByTheseTests':False},indent=2))
if __name__=='__main__':main()
