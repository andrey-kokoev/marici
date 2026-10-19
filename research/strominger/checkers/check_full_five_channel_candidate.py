"""Full-five joint-field candidate, conditional defect ledger, and path frames."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
from exact_multiradical import Radical as R,sqrt,mm,adj,identity,decode_A,serialize,rational
from assemble_metric_coefficient_protocol import read_operator
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
BASE=ROOT/'research/strominger/results'
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(row,col)] for row,col in zip(a,b)]
def metric_adj(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def gram(a,m):return mm(metric_adj(a,m),a)
def op(d,k,n):
    s=read_operator(d['operators'][k],n);return [[decode_A(s[i,j].record()) if (i,j) in s else R() for j in range(n)] for i in range(n)]
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
nd=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());ed=json.loads((BASE/'common-three-carrier-protocol/electron.json').read_text());pd=json.loads((BASE/'common-three-carrier-protocol/proton.json').read_text());m=list(map(F,nd['source']['metric']));grid=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text())['carriers']['neutron'];z=[decode_A(x) for x in grid['sourceReturnColumn']];norm=rational(sum((m[i]*z[i].conj()*z[i] for i in range(12)),R()));v=[x*sqrt(1/norm) for x in z[:12]]
# Three active coefficients populate the three native sector-local modes.
BN=[[R() for _ in range(5)] for _ in range(36)]
for sector in range(3):
    for i in range(12):BN[12*sector+i][1+sector]=v[i]
# Select the unique patch on each reader face incident to their common edge.
# Replicate its orthogonal mode across all three sectors: outside coefficients
# are fixed under the active C3 cycle, so their fields must also be invariant.
reader=json.loads((BASE/'neutron-reader-field-interface/verification.json').read_text());patches=reader['charts'][0]['readerPatches'];contextSlots=[]
for column,face in [(0,'F_buv'),(4,'F_cuv')]:
    slot=next(i for i,t in enumerate(patches) if t[0]==face and set(t[1:])=={'u','v'});a,b=2*slot,2*slot+1;contextSlots.append({'coefficient':column,'patch':patches[slot],'referenceSlots':[a,b]})
    fa,fb=sqrt(m[a])*z[a],sqrt(m[b])*z[b];n=rational(fa.conj()*fa+fb.conj()*fb)
    for sector in range(3):BN[a+12*sector][column]=fb.conj()*sqrt(1/(3*n*m[a]));BN[b+12*sector][column]=-fa.conj()*sqrt(1/(3*n*m[b]))
assert gram(BN,m)==identity(5)
sectorCycle=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)];activeCycle=perm([0,3,1,2,4]);assert mm(sectorCycle,BN)==mm(BN,activeCycle)
LN0,GN0,NN0=[op(nd,k,36) for k in ['L','G','N']];reduced={}
for key,X in [('L',LN0),('G',GN0),('N',NN0)]:
    reduced[key]=mm(metric_adj(BN,m),mm(X,BN));assert mm(X,BN)==mm(BN,reduced[key])
contrast=json.loads((BASE/'neutron-contrast-electron-transport/verification.json').read_text());K=restore(contrast['contrastFrame']);EF=restore(contrast['electronFrame']);S=restore(contrast['NEcandidateMatrix']);Ssharp=mm(K,adj(EF));C=mm(K,metric_adj(K,m));NE=op(ed,'N',8)
# Isometric input into the joint 36+8 field. NE is a subspace exchange, not
# an assertion that all five reference coefficients belong to E alone.
zero8=[[R() for _ in range(5)] for _ in range(8)];Bin=BN+zero8;PiNE=perm([0,4,2,3,1]);afterN=add(BN,mm(C,BN),-1);afterE=mm(S,BN);Bout=mm(afterN+afterE,PiNE);assert gram(Bin,m+[F(1)]*8)==identity(5);assert gram(Bout,m+[F(1)]*8)==identity(5)
assert mm(Bout,PiNE)==afterN+afterE
# Independently verify that the E block is the prior contrast binding.
q=[[sqrt(F(1,2)),sqrt(F(1,6))],[-sqrt(F(1,2)),sqrt(F(1,6))],[R(),-sqrt(F(2,3))]];DN=[[R() for _ in range(5)] for _ in range(2)];DE=[[R() for _ in range(5)] for _ in range(2)]
for j in range(2):
    for i in range(3):DN[j][[1,2,3][i]]=q[i][j];DE[j][[3,2,4][i]]=q[i][j]
reflection=mm(mm(DE,PiNE),adj(DN));expectedE=mm(mm(EF,adj(reflection)),DE);assert Bout[36:]==expectedE
assert gram(afterE,[F(1)]*8)==mm(adj(DN),DN);assert add(gram(afterN,m),gram(afterE,[F(1)]*8))==identity(5)
# Conditional accounting: add electron-return occupation to the existing
# defect measure. Its coefficient is forced to one by the checked gap.
HN=add(add([[2*x for x in row] for row in identity(36)],op(nd,'L',36),-1),op(nd,'G',36),-1);HE=add(add([[2*x for x in row] for row in identity(8)],op(ed,'L',8),-1),op(ed,'G',8),-1);QE=add(HE,NE)
assert mm(S,HN)==mm(QE,S);assert mm(HN,C)==mm(C,HN);assert mm(QE,NE)==mm(NE,QE)
# Hence Q=HN direct-sum (HE+NE) commutes with the exact involutive swap.
# Bind PN algebraically, retaining the explicit freedom in the supplied map.
globalPN=json.loads((BASE/'global-PN-transport/verification.json').read_text());PN=restore(globalPN['matrix']);PNsharp=[[x*m[j] for j,x in enumerate(row)] for row in adj(PN)];PiPN=perm([3,1,2,0,4]);BP=mm(mm(PNsharp,BN),PiPN);assert gram(BP,[F(1)]*36)==identity(5);assert mm(PN,BP)==mm(BN,PiPN)
# Native P reader rotation on its full geometric field.
labels=pd['source']['coordinates'];rotation=geo.rotation((2,3,0,1));rename=dict(zip('ABCD','CDAB'));UP=[[R() for _ in range(36)] for _ in range(36)]
for j,label in enumerate(labels):
    edge,axis=label.split(':');new=''.join(rename[v] for v in edge)
    for i in range(3):
        if rotation[i]['xyz'.index(axis)]:UP[labels.index(new+':'+'xyz'[i])][j]=R(rotation[i]['xyz'.index(axis)])
pathData=json.loads((BASE/'window-combination-coherence/verification.json').read_text());witness=next(x for x in pathData['coefficientFrameHolonomyExamples'] if len(x['paths'][0]['word'])==3 and all(p['retainedCombinationAudit'].get('allContactsWitnessed') for p in x['paths']));pathResults=[]
for path in witness['paths']:
    B=BP;coeff=identity(5);species='proton';fieldRoot=BP
    for kind in path['word']:
        if kind=='PN':U=PN;pi=PiPN;species='neutron'
        elif kind=='inverse-PN':U=PNsharp;pi=PiPN;species='proton'
        elif kind=='reader-phase-advance':U=UP if species=='proton' else identity(36);pi=perm([2,3,0,1,4] if species=='proton' else [0,3,4,1,2])
        else:raise AssertionError(kind)
        fieldRoot=mm(U,fieldRoot);B=mm(mm(U,B),adj(pi));coeff=mm(pi,coeff);assert mm(B,coeff)==fieldRoot
        assert gram(B,[F(1)]*36 if species=='proton' else m)==identity(5)
    assert species=='proton';assert coeff==perm(path['permutation']);assert fieldRoot==mm(UP,BP)
    pathResults.append({'word':path['word'],'coefficientPermutation':path['permutation'],'binding':serialize(B)})
assert pathResults[0]['binding']!=pathResults[1]['binding']
result={'status':'full-five-framed-joint-field-candidate-passed','neutronFiveEmbedding':serialize(BN),'protonFiveEmbedding':serialize(BP),'postNEJointEmbedding':serialize(Bout),'NE':{'jointDimension':44,'fiveInputNormPreserved':True,'electronBlockRank':2,'retainedBaryonBlockRank':3,'independentPriorContrastBindingMatches':True,'outsideContextChoice':contextSlots,'fullC3Equivariance':True,'exactFiveDimensionalProjectorReduction':True},'inducedNeutronFiveProjectors':{k:serialize(v) for k,v in reduced.items()},'PN':{'fullFiveIdentity':'S_PN B_P=B_N Pi_PN','metricIsometric':True,'PBindingDerivedByPullbackNotIndependentGeometrySelection':True},'pathPair':{'samePhysicalRootFieldMapInThisCandidate':True,'differentCoefficientFrames':True,'frameDependentBindingsRequired':True,'paths':pathResults,'scope':'One checked native open path pair. B_next=U B Pi^-1 is a construction rule, not an independently derived field coupling. No arbitrary loops or simultaneous assemblies certified.'},'accounting':{'conservedCandidate':'Q=H_N direct-sum (H_E+N_E)','commutesWithSwap':True,'nativeDefectAloneConserved':False,'meaning':'Explicit dimensionless ledger term restores algebraic conservation. Its physical interpretation, units and dynamics are unassigned.'},'scope':'A coherent algebraic candidate using previously constructed PN and contrast-NE maps, phase/frame-dependent coefficient bindings and explicit context choices. All five coefficients survive in the joint field, not solely the E return. Window-to-sector identification, context selection and field map choices remain hypotheses. No production admission change, physical dynamics, electron creation law, or global assembly coherence claimed.'}
files=[Path(__file__).resolve(),Path(__file__).with_name('exact_multiradical.py'),BASE/'neutron-reader-field-interface/verification.json',BASE/'global-PN-transport/verification.json',BASE/'neutron-contrast-electron-transport/verification.json',BASE/'window-combination-coherence/verification.json',BASE/'baryon-tensor-grid/verification.json',*[BASE/f'common-three-carrier-protocol/{s}.json' for s in ['proton','neutron','electron']]];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=BASE/'full-five-channel-candidate';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'allFivePreserved':True,'electronChannels':2,'baryonChannelsRetained':3,'PNFiveIdentity':True,'nativePathPairCoherentWithFrames':True,'augmentedLedgerConserved':True}))
