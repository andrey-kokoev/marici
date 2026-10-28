"""Exact semantic test of geometry-induced E/P re-reading, without fitted phases."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize
import check_twelve_triangle_positive_geometry as geo
pins={}
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def load(p):
    pins[p]=sha(p);d=json.loads((ROOT/p).read_text())
    for k,h in d.get('source_sha256',d.get('sourceHashes',{})).items():
        assert sha(k)==h,'stale '+k;pins[k]=h
    return d
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def minus(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def nz(a):return [{'row':i,'column':j,'value':v.record()} for i,row in enumerate(a) for j,v in enumerate(row) if v!=0]
def main():
    inputs=load('research/voevodsky/results/ramsey-passive-EP-port-input-v1.json')
    load('research/voevodsky/results/ramsey-passive-EP-port-v1.json')
    five=load('research/strominger/results/full-five-channel-candidate/verification.json')
    reversedFields=load('research/voevodsky/results/ramsey-reversed-certificate-fields-v1.json')
    pd=load('research/strominger/results/common-three-carrier-protocol/proton.json')
    nd=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    pn=load('research/strominger/results/global-PN-transport/verification.json')
    B=restore(five['protonFiveEmbedding']);BN=restore(five['neutronFiveEmbedding']);PN=restore(pn['matrix'])
    metric=list(map(F,nd['source']['metric']));RP=adj(B);RN=[[v*metric[j] for j,v in enumerate(row)] for row in adj(BN)]
    Q=perm([4,3,2,1,0]);BE=mm(B,Q);RE=adj(BE);PiPN=perm([3,1,2,0,4])
    assert restore(reversedFields['dualBindings'][0])==BE+[[R() for _ in range(5)] for _ in range(8)]
    assert mm(RP,B)==mm(RE,BE)==identity(5)
    assert mm(PN,B)==mm(BN,PiPN) and mm(RN,PN)==mm(PiPN,RP)
    labels=pd['source']['coordinates'];assert len(labels)==36
    def geometric(p,rotate=True):
        rename=dict(zip('ABCD',('ABCD'[i] for i in p)))
        rotation=geo.rotation(p) if rotate else [[1,0,0],[0,1,0],[0,0,1]]
        U=[[R() for _ in range(36)] for _ in range(36)]
        for j,label in enumerate(labels):
            edge,axis=label.split(':');target=''.join(rename[v] for v in edge)
            for i in range(3):U[labels.index(target+':'+'xyz'[i])][j]=R(rotation[i]['xyz'.index(axis)])
        assert mm(adj(U),U)==identity(36);return U
    # The existing P reader is the CDAB half-turn. Two reader steps return
    # its field and coefficient frames, so +2 alone does not change this seed.
    reader=geometric((2,3,0,1));readerPi=perm([2,3,0,1,4])
    assert mm(reader,reader)==identity(36) and mm(readerPi,readerPi)==identity(5)
    # Original P body order ABCD becomes BADC in the complementary chart.
    # The passive re-reading retains C2/M2: old E slots3/4 -> target P slots0/1.
    expectedRetained=[identity(5)[3],identity(5)[4]]
    reports=[]
    for name,rotate in [('fixed_xyz_edge_relabelling',False),('co_moving_tetrahedral_frame',True)]:
        G=geometric((1,0,3,2),rotate)
        image=mm(G,BE);T=mm(RP,image);residual=minus(image,mm(B,T))
        kept=minus(T[:2],expectedRetained)
        # This is a non-tautological geometric map. PN compatibility is then
        # checked on ALL36 inputs, separately from the five-preparation test.
        readoutSquare=mm(RN,mm(PN,G))==mm(PiPN,mm(RP,G));assert readoutSquare
        deficit=minus(identity(5),mm(adj(T),T))
        assert mm(adj(residual),residual)==deficit
        reports.append({'convention':name,'geometricMap':serialize(G),
          'inducedFiveReadout':serialize(T),'fivePreparationPreserved':not nz(residual),
          'retainedC2M2ValuesPreserved':not nz(kept),'full36PNReadoutSquare':readoutSquare,
          'preparationResiduals':nz(residual),'retainedValueResiduals':nz(kept),
          'readoutNormDeficit':serialize(deficit)})
    # Exact small witness for the co-moving convention, without numerical rank.
    moving=reports[1];T=restore(moving['inducedFiveReadout'])
    assert all(T[i][1]==0 for i in range(5))
    assert [T[i][3] for i in range(5)]==[R(),R(1),R(),R(),R()]
    assert T[4][0]!=0
    assert all(T[i][j]==0 for i in range(5) for j in range(5) if (i,j) not in [(0,4),(1,3),(2,2),(4,0)])
    assert T[0][4]==T[1][3]==T[2][2]==R(1)
    assert restore(moving['readoutNormDeficit'])[1][1]==R(1)
    moving['exactInducedReadoutRank']=4
    moving['unitWitness']={'sourceOutgoingCoefficientSlot':1,'sourceOccurrence':'C1',
      'fullFieldNormSquared':1,'allFiveTargetReadouts':[0,0,0,0,0],
      'interpretation':'the geometric image is not lost in full36; it lies outside the chosen target five-preparation'}
    moving['retainedC2Witness']={'sourceSlot':3,'expectedTargetSlot':0,'actualTargetSlot':1,
      'expectedName':'P.C0 at origin2 = retained C2','actualName':'P.M0 at origin2 = M2'}
    assert all(not r['fivePreparationPreserved'] and not r['retainedC2M2ValuesPreserved'] for r in reports)
    # In contrast, constructing a comparison from the desired seed map can
    # always pass the same coefficient squares. This does not choose a geometry map.
    choices=[]
    for sign in [1,-1]:
        T=perm([3,4,1,2,0]);T[4]=[sign*v for v in T[4]]
        A=mm(mm(B,T),RE) # prepared-space partial isometry, NOT a full36 unitary
        assert mm(A,BE)==mm(B,T)
        assert mm(RP,mm(A,BE))[:2]==expectedRetained
        assert mm(PN,mm(A,BE))==mm(BN,mm(PiPN,T))
        assert mm(adj(T),T)==identity(5)
        assert mm(adj(A),A)!=identity(36) # no full-carrier isometry claimed for this partial map
        choices.append({'outsideSign':sign,'coefficientMap':serialize(T),'preparedMap':serialize(A)})
    assert choices[0]['coefficientMap']!=choices[1]['coefficientMap']
    pnChoices=[mm(PiPN,restore(c['coefficientMap'])) for c in choices]
    assert [pnChoices[0][i] for i in [1,2,3]]==[pnChoices[1][i] for i in [1,2,3]]
    assert pnChoices[0][4]!=pnChoices[1][4] # full PN context still distinguishes the choices
    # Bind local scalar-index bookkeeping to every actual contextual record.
    for ctx in inputs['contexts']:
        e=ctx['e']['chart']['aliases'];p=ctx['p']['chart']['aliases']
        assert [p[n] for n in ['C0','M0','C1','M1']]==[e[n] for n in ['C2','M2','C1','M1']]
        assert sorted(x['delta'] for x in ctx['occurrences'])==[0,0,2,2]
    for module in list(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            try:rel=Path(path).resolve().relative_to(ROOT).as_posix()
            except ValueError:continue
            pins[rel]=sha(rel)
    pins[Path(__file__).relative_to(ROOT).as_posix()]=sha(Path(__file__).relative_to(ROOT).as_posix())
    out={'status':'passed','scope':'two explicit geometry-induced passive maps for the retained negative-E carrier and unchanged P seed; not every possible adapter',
      'sourceConvention':'negative E retains old P36 plus zero prepared E8, with five binding B_P Q; outgoing labels M0,C1,M1,C2,M2. Not silently replaced by forward native E8.',
      'markingsBound':len(inputs['contexts']),'tests':reports,'competingPreparedComparisons':choices,
      'conclusion':'PN readout intertwining alone does not force an E/P comparison. Check geometry-induced preparation and retained-value residuals separately.',
      'fieldMapRefitted':False,'parentResolved':False,'formalKernelProofClaimed':False,'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-passive-EP-semantics-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'passed','tests':[{k:r[k] for k in ['convention','fivePreparationPreserved','retainedC2M2ValuesPreserved','full36PNReadoutSquare']} for r in reports],'competingPreparedComparisons':2},indent=2))
if __name__=='__main__':main()
