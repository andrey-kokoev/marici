"""Compare ordered outgoing E observation with the unchanged joint44 candidate."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,sqrt,serialize,rational
pins={}
def load(path):
    raw=(ROOT/path).read_bytes();pins[path]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sharp(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def gram(a,m):return mm(sharp(a,m),a)
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def residual(a,b):return [{'row':i,'column':j,'value':(x-y).record()} for i,(r,s) in enumerate(zip(a,b)) for j,(x,y) in enumerate(zip(r,s)) if x!=y]
def main():
    corrected=load('research/voevodsky/results/ramsey-outgoing-E-readout-v1.json')
    fields=load('research/strominger/results/full-five-channel-candidate/verification.json')
    contrast=load('research/strominger/results/neutron-contrast-electron-transport/verification.json')
    native=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    port=load('research/voevodsky/results/ramsey-based-port-readout-v1.json')
    for report in [corrected,fields,contrast]:
        for path,digest in report.get('source_sha256',report.get('sourceHashes',{})).items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
            pins[path]=digest
    B=restore(fields['neutronFiveEmbedding']);Bout=restore(fields['postNEJointEmbedding'])
    S=restore(contrast['NEcandidateMatrix']);K=restore(contrast['contrastFrame']);EF=restore(contrast['electronFrame'])
    reflection=restore(contrast['fiveCoefficientTest']['activeContrastReflection'])
    m=list(map(F,native['source']['metric']));Q=perm([4,3,2,1,0]);Pi=perm(contrast['fiveCoefficientTest']['nativePermutation'])
    C=mm(K,sharp(K,m));U=restore(port['fullFieldMap'])
    # y=Qx denotes the outgoing five-reference coordinates throughout.
    # The unchanged NE exchange acts on B y, with the E input zero.
    actualE=mm(S,B);actualN=add(B,mm(C,B),-1)
    assert mm(Bout,Pi)==actualN+actualE
    assert mm(U,B)==mm(B,Q)
    assert mm(S,mm(U,B))==mm(actualE,Q)
    q=[[sqrt(F(1,2)),sqrt(F(1,6))],[-sqrt(F(1,2)),sqrt(F(1,6))],[R(),-sqrt(F(2,3))]]
    D=[[R() for _ in range(5)] for _ in range(2)]
    slots=corrected['outgoingWindowSlots'];assert slots==[2,1,3]
    for j in range(2):
        for i,slot in enumerate(slots):D[j][slot]=q[i][j]
    # Reuse the saved E contrast-binding convention, no fitted E rotation.
    targetE=mm(mm(EF,adj(reflection)),D)
    # Active E names determine native output slots3,2,4. M0 fixes slot1.
    # The only remaining numerical slot is0, but its native label C0 differs
    # from outgoing M2: record this as a PROVISIONAL complement comparison.
    Hindices=[4,0,1,2,3];H=perm(Hindices)
    assert mm(Bout[36:],H)==targetE
    targetN=mm(Bout[:36],H)
    G_E=gram(actualE,[F(1)]*8);G_N=gram(actualN,m)
    assert G_E==gram(targetE,[F(1)]*8) and G_N==gram(targetN,m)
    assert add(G_E,G_N)==identity(5)
    assert mm(G_E,G_E)==G_E and mm(G_N,G_N)==G_N
    assert sum(rational(G_E[i][i]) for i in range(5))==2
    assert sum(rational(G_N[i][i]) for i in range(5))==3
    # Compare exact vectors as well as the ranks/Gram projectors.
    er,nr=residual(actualE,targetE),residual(actualN,targetN)
    assert er and nr
    # Diagnose, not silently repair, the E difference in the existing contrast frame.
    rotation=mm(mm(adj(EF),targetE),adj(mm(adj(EF),actualE)))
    sourceRotation=[[-R(F(1,2)),-sqrt(F(3,4))],[sqrt(F(3,4)),-R(F(1,2))]]
    powers=[identity(2),sourceRotation,mm(sourceRotation,sourceRotation)]
    matching=[i for i,p in enumerate(powers) if p==rotation]
    assert len(matching)==1 and matching[0]!=0
    assert mm(mm(EF,rotation),mm(adj(EF),actualE))==targetE
    # Independently check relation to the actual retained native electron action.
    store=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    def spinor(v):return R(F(v[0][0]))+F(v[0][1])*sqrt(3)+F(v[1][0])*sqrt(-1)+F(v[1][1])*sqrt(-3)
    J=[[sqrt(F(1,2))*spinor(v) for v in row] for face in store['face_projectors'] for row in face]
    V=restore(contrast['nativeElectronAction']);Vp=identity(2)
    for _ in range(matching[0]):Vp=mm(Vp,V)
    nativeAction=mm(mm(J,Vp),adj(J))
    assert mm(nativeAction,actualE)==targetE
    # Baryon difference is exactly the two context columns, not the common mode.
    contextSwap=perm([4,1,2,3,0])
    assert mm(actualN,contextSwap)==targetN
    assert all(actualN[i][j]==targetN[i][j] for i in range(36) for j in [1,2,3])
    # Both full prepared outputs recover all five, but with different frames.
    actual=actualN+actualE;target=targetN+targetE;metric=m+[F(1)]*8
    assert gram(actual,metric)==gram(target,metric)==identity(5)
    assert mm(sharp(actual,metric),actual)==identity(5)
    assert mm(sharp(target,metric),target)==identity(5)
    # The exact five-frame difference needed BEFORE the unchanged exchange.
    A=mm(Pi,H);assert mm(actual,A)==target
    assert A!=identity(5)
    rawDE=mm(EF,D)
    assert rawDE!=targetE,'dropping prior NE contrast reflection should fail'
    result={'schema':'marici.ramsey-E-joint44-comparison.v1','node':'T-seam-based-port-readout-binding',
      'checkerStatus':'passed','scientificStatus':'same_rank_split_but_nontrivial_frame_difference',
      'coefficientConvention':'y=Qx in outgoing reference M0,C1,M1,C2,M2; E order M1,C1,C2',
      'unchangedExchangeElectronBlockMatches':False,'provisionalBaryonBlockMatches':False,
      'electronRank':2,'retainedBaryonRank':3,'complementaryGramProjectorsMatch':True,
      'bothPreparedOutputsRecoverFiveCoefficients':True,
      'electronResidualEntries':len(er),'baryonResidualEntries':len(nr),
      'electronResiduals':er,'baryonResiduals':nr,
      'electronContrastFrameDifference':serialize(rotation),'matchingNativeC3Power':matching[0],
      'nativeElectronDictionaryActionMatch':True,
      'baryonDifference':'Common active combination agrees; context columns0 and4 exchange.',
      'requiredPreExchangeCoefficientFrame':serialize(A),
      'provisionalOutgoingToNativeOutputIndices':Hindices,
      'unresolvedComplementProvenance':{'nativeSlot':0,'nativeName':'C0','outgoingName':'M2','identified':False},
      'controls':['Exact E vector inequality survives equal rank/Gram tests','Exact baryon inequality survives equal rank/Gram tests','Identity coefficient frame fails','Omitting saved NE contrast reflection fails'],
      'scope':'The E difference is an actual retained native C3 action on the return image. This does not make it an already admitted part of the unchanged NE exchange. The baryon comparison uses an explicitly provisional unmatched C0/M2 slot; no new occurrence identification or native transition is admitted.',
      'netOutcomeChanged':False}
    for path in ['research/voevodsky/checkers/check_ramsey_E_joint44_comparison.py','research/strominger/checkers/exact_multiradical.py']:
        pins[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
    result['source_sha256']=pins
    (ROOT/'research/voevodsky/results/ramsey-E-joint44-comparison-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['checkerStatus','scientificStatus','electronRank','retainedBaryonRank','electronResidualEntries','baryonResidualEntries','matchingNativeC3Power','nativeElectronDictionaryActionMatch']}))
if __name__=='__main__':main()
