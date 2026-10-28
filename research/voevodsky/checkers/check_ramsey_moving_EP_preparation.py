"""Conditional moving-preparation test; native operators are NOT conjugated away.
Connection: joint44-native-source-selection acceptance (retained choice family
and independent reader laws); negative-direction-policy-native-descent boundary.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json,sys
from check_ramsey_passive_EP_semantics import ROOT,load,restore,perm,minus,nz,pins,sha
from exact_multiradical import Radical as R,mm,adj,identity,serialize,decode_A
from assemble_metric_coefficient_protocol import read_operator

def main():
    tested=load('research/voevodsky/results/ramsey-passive-EP-semantics-v1.json')
    fields=load('research/strominger/results/full-five-channel-candidate/verification.json')
    pn=load('research/strominger/results/global-PN-transport/verification.json')
    nd=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    contract=load('research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json')
    # Preserve exact owning text as evidence; interpretation is a written audit,
    # not a claim that string absence mechanically proves non-necessity.
    nodes=contract['conjectures'] if 'conjectures' in contract else contract['nodes']
    excerpts={n['id']:{k:n[k] for k in ['scope_id','statement','acceptance','falsifier']} for n in nodes if n['id'] in ['face-chart-transition-descent','joint44-native-source-selection','negative-direction-policy-native-descent']}
    assert len(excerpts)==3
    B=restore(fields['protonFiveEmbedding']);BN=restore(fields['neutronFiveEmbedding']);PN=restore(pn['matrix'])
    m=list(map(F,nd['source']['metric']))
    def sharp(A):return [[v*m[j] for j,v in enumerate(row)] for row in adj(A)]
    PNinv=sharp(PN);assert mm(PNinv,PN)==identity(36)
    BE=mm(B,perm([4,3,2,1,0]));RE=adj(BE);Pi=perm([3,1,2,0,4])
    G=restore(next(t['geometricMap'] for t in tested['tests'] if t['convention']=='co_moving_tetrahedral_frame'))
    T=perm([3,4,1,2,0])
    BPnew=mm(mm(G,BE),adj(T));RPnew=adj(BPnew)
    BNnew=mm(mm(PN,BPnew),adj(Pi));RNnew=sharp(BNnew)
    assert mm(RPnew,BPnew)==mm(RNnew,BNnew)==identity(5)
    assert mm(RPnew,G)==mm(T,RE) # all36 inputs, not only five prepared columns
    assert mm(PN,BPnew)==mm(BNnew,Pi)
    assert mm(RNnew,PN)==mm(Pi,RPnew)
    oldPprojector=mm(B,adj(B));newPprojector=mm(BPnew,RPnew)
    assert newPprojector!=oldPprojector
    assert RNnew!=sharp(BN) and RPnew!=adj(B)
    actions=[];operators={}
    for name in ['L','G','N']:
        sparse=read_operator(nd['operators'][name],36)
        A=[[decode_A(sparse[i,j].record()) if (i,j) in sparse else R() for j in range(36)] for i in range(36)]
        operators[name]=A
        assert mm(A,BN)==mm(BN,mm(sharp(BN),mm(A,BN)))
        reduced=mm(RNnew,mm(A,BNnew))
        residual=minus(mm(A,BNnew),mm(BNnew,reduced))
        actions.append({'operator':name,'oldFivePreparationInvariant':True,
            'movingFivePreparationInvariant':not nz(residual),'residuals':nz(residual),
            'compressedAction':serialize(reduced),
            'sameNamedCoefficientAction':reduced==restore(fields['inducedNeutronFiveProjectors'][name]),
            'compressedActionIdempotent':mm(reduced,reduced)==reduced})
    # A phase/sign change inside the five coordinates does not alter this
    # preparation projector or cure its failure under unchanged native actions.
    Tminus=[row[:] for row in T];Tminus[4]=[-v for v in Tminus[4]]
    BPminus=mm(mm(G,BE),adj(Tminus))
    assert BPminus!=BPnew and mm(BPminus,adj(BPminus))==newPprojector
    # Exhaust all six positive coefficient permutations preserving the two
    # genuinely retained occurrences; do not fix the advancing pair in advance.
    candidates=[]
    for rest in permutations([0,1,2]):
        order=[3,4,*rest];choice=perm(order)
        bp=mm(mm(G,BE),adj(choice));bn=mm(mm(PN,bp),adj(Pi));rn=sharp(bn)
        matches={name:mm(rn,mm(A,bn))==restore(fields['inducedNeutronFiveProjectors'][name]) for name,A in operators.items()}
        assert mm(adj(bp),mm(G,BE))[:2]==[identity(5)[3],identity(5)[4]]
        candidates.append({'coefficientOrder':order,'nativeNamedActions':matches,'allPass':all(matches.values())})
    survivors=[c['coefficientOrder'] for c in candidates if c['allPass']]
    assert survivors==[[3,4,2,0,1],[3,4,2,1,0]]
    # General remaining freedom: U(2) on the two context coordinates.
    # Moving preparation depends on G and BE, not on its unitary five-frame.
    reference=perm([3,4,2,0,1]);bp=mm(mm(G,BE),adj(reference));bn=mm(mm(PN,bp),adj(Pi))
    assert mm(bp,adj(bp))==newPprojector
    sourceActions={}
    for name,A in operators.items():
        reduced=restore(fields['inducedNeutronFiveProjectors'][name])
        sourceAction=mm(adj(mm(PN,mm(G,BE))),[[m[i]*v for v in row] for i,row in enumerate(mm(A,mm(PN,mm(G,BE))))])
        expected=[[R() for _ in range(5)] for _ in range(5)]
        if name=='L':
            for i in [2,3,4]:expected[i][i]=R(1)
        else:
            for i in [2,3,4]:
                for j in [2,3,4]:expected[i][j]=R(F(1,3))
            if name=='G':expected[0][0]=expected[1][1]=R(1)
        assert sourceAction==expected
        sourceActions[name]=serialize(sourceAction)
        assert mm(A,bn)==mm(bn,reduced)
        # N contexts are slots0,4; each operator restricts to scalar0 or I
        # there, with no context/active cross terms. Hence arbitrary U(2)
        # on these coordinates commutes, not just sampled permutations.
        assert all(reduced[i][j]==0 for i in [0,4] for j in [1,2,3])
        assert all(reduced[j][i]==0 for i in [0,4] for j in [1,2,3])
        assert reduced[0][0]==reduced[4][4] and reduced[0][4]==reduced[4][0]==0
    for module in list(sys.modules.values()):
        filename=getattr(module,'__file__',None)
        if filename:
            try:rel=Path(filename).resolve().relative_to(ROOT).as_posix()
            except ValueError:continue
            pins[rel]=sha(rel)
    rel=Path(__file__).relative_to(ROOT).as_posix();pins[rel]=sha(rel)
    out={'status':'passed','node':'joint44-native-source-selection','governingParent':'face-chart-transition-descent',
      'contractExcerpts':excerpts,'movingPreparation':serialize(BPnew),'movingPNPreparation':serialize(BNnew),
      'allInputEPReadoutSquare':True,'allInputPNReadoutSquare':True,'fiveNormPreserved':True,
      'samePhysicalPreparationProjector':False,'oldNativeReadoutsUnchanged':False,
      'nativeActions':actions,'outsideSignDoesNotChangePreparationSubspace':True,
      'retainedPairPermutationCandidates':candidates,'nativeActionCompatiblePermutations':survivors,
      'residualChoiceFamily':'P coefficients (x3,x4,x2,U(x0,x1)), U any2x2 unitary. Both retained coefficients and unchanged native named L/G/N actions are preserved; the moving preparation projector is the same for all U.',
      'contextBlockCommutantVerified':True,'sourceCoefficientActions':sourceActions,
      'scope':'Explicit moving preparation for the co-moving geometric map and declared coefficient convention. Tests unchanged L/G/N operators; does not replace them by conjugates or assert these operators are mandatory parent axioms.',
      'parentResolved':False,'sourcePolicyChanged':False,'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-moving-EP-preparation-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','allInputEPReadoutSquare','allInputPNReadoutSquare','fiveNormPreserved','samePhysicalPreparationProjector','oldNativeReadoutsUnchanged']} | {'nativeActions':[{k:a[k] for k in ['operator','movingFivePreparationInvariant','compressedActionIdempotent','sameNamedCoefficientAction']} for a in actions],'compatiblePositivePermutations':survivors,'remainingFreedom':'U(2) on two context coefficients'},indent=2))
if __name__=='__main__':main()
