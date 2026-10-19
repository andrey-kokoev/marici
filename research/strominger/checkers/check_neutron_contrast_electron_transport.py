"""Candidate NE interaction from N's existing two-dimensional sector contrast."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from exact_multiradical import Radical as R,sqrt,mm,adj,identity,decode_A,serialize,rational
from assemble_metric_coefficient_protocol import read_operator
from electron_packet_interface import ACTIONS
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
def matrix(d,key,n):
    sparse=read_operator(d['operators'][key],n);return [[decode_A(sparse[i,j].record()) if (i,j) in sparse else R() for j in range(n)] for i in range(n)]
def minus(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def plus(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(q,a):return [[q*x for x in row] for row in a]
def metric_adj(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def decode_spinor(v):return R(F(v[0][0]))+F(v[0][1])*sqrt(3)+F(v[1][0])*sqrt(-1)+F(v[1][1])*sqrt(-3)
n=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());e=json.loads((BASE/'common-three-carrier-protocol/electron.json').read_text());grid=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text())['carriers']['neutron'];metric=list(map(F,n['source']['metric']));z=[decode_A(v) for v in grid['sourceReturnColumn']];assert z[:12]==z[12:24]==z[24:]
sectorNorm=rational(sum((metric[i]*z[i].conj()*z[i] for i in range(12)),R()));v=[x*sqrt(1/sectorNorm) for x in z[:12]]
q=[[sqrt(F(1,2)),sqrt(F(1,6))],[-sqrt(F(1,2)),sqrt(F(1,6))],[R(),-sqrt(F(2,3))]];assert mm(adj(q),q)==identity(2)
K=[[q[i//12][j]*v[i%12] for j in range(2)] for i in range(36)];Ksharp=metric_adj(K,metric);assert mm(Ksharp,K)==identity(2)
LN,GN,NN=[matrix(n,key,36) for key in ['L','G','N']];contrast=minus(LN,NN);assert mm(K,Ksharp)==contrast
assert mm(LN,K)==K;assert mm(GN,K)==[[R(),R()] for _ in range(36)]
# Source-derived C3 sector rotation acts as the real 120-degree contrast rotation.
sectorRotation=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)];rotation=mm(mm(Ksharp,sectorRotation),K);assert rotation==[[R(F(-1,2)),-sqrt(F(3,4))],[sqrt(F(3,4)),R(F(-1,2))]]
storePath=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json';store=json.loads(storePath.read_text());J=[[sqrt(F(1,2))*decode_spinor(v) for v in row] for face in store['face_projectors'] for row in face];assert mm(adj(J),J)==identity(2)
# Choose an actual retained native order-three electron action, not an arbitrary
# SU(2) operation. W aligns its axis with the real source contrast frame.
i=sqrt(-1);V=[[R(F(-1,2))+F(1,2)*i,R(F(1,2))+F(1,2)*i],[R(F(-1,2))+F(1,2)*i,R(F(-1,2))-F(1,2)*i]]
actions=[[[R(z[0])+z[1]*i for z in row] for row in action] for action in ACTIONS];assert V in actions;assert mm(mm(V,V),V)==identity(2)
w=[[sqrt(F(1,2))],[(R(1)-i)*F(1,2)]];axisGenerator=scale(sqrt(F(4,3)),plus(V,scale(R(F(1,2)),identity(2))));w2=mm(axisGenerator,w);W=[[w[r][0],w2[r][0]] for r in range(2)];assert mm(adj(W),W)==identity(2);assert mm(V,W)==mm(W,rotation)
Eframe=mm(J,W);LE,GE,NE=[matrix(e,key,8) for key in ['L','G','N']];assert mm(Eframe,adj(Eframe))==NE;assert mm(LE,Eframe)==Eframe and mm(GE,Eframe)==Eframe
S=mm(Eframe,Ksharp);Ssharp=mm(K,adj(Eframe));assert mm(S,Ssharp)==NE;assert mm(Ssharp,S)==contrast
assert mm(S,NN)==[[R() for _ in range(36)] for _ in range(8)];assert mm(NE,S)==S
# The target native rotation is J V J* on its image. Check the actual field
# intertwiner, not only equal eigenvalues or matching dimensions.
electronAction=mm(mm(J,V),adj(J));assert mm(S,sectorRotation)==mm(electronAction,S)
# Five-slot NE: the native ordered active triple reverses. Pair the window
# contrast coefficients with sector contrast as an explicit candidate ansatz.
phasePath=ROOT/'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';text=phasePath.read_text();assert 'neutron:[1,2,3]' in text and 'electron:[3,2,4]' in text
rulesPath=ROOT/'research/nima/generative-phase-assembly.mjs';assert 'NE=[0,4,2,3,1]' in rulesPath.read_text();pi=[0,4,2,3,1];Pi=[[R(int(j==pi[k])) for j in range(5)] for k in range(5)]
DN=[[R() for _ in range(5)] for _ in range(2)];DE=[[R() for _ in range(5)] for _ in range(2)]
for axis in range(2):
    for t in range(3):DN[axis][[1,2,3][t]]=q[t][axis];DE[axis][[3,2,4][t]]=q[t][axis]
reflection=mm(mm(DE,Pi),adj(DN));assert mm(adj(reflection),reflection)==identity(2);assert mm(DE,Pi)==mm(reflection,DN)
BN=mm(K,DN);BE=mm(mm(Eframe,adj(reflection)),DE);assert mm(S,BN)==mm(BE,Pi)
# This conversion is NOT a return-preserving NE map. Its source contrast has
# one unit of projector defect; target return has zero.
HN=minus(minus(scale(R(2),identity(36)),LN),GN);HE=minus(minus(scale(R(2),identity(8)),LE),GE);assert mm(HN,K)==K;assert mm(HE,Eframe)==[[R(),R()] for _ in range(8)]
# Partial-isometry identities imply the 44-channel swap is metric-unitary:
# [[I-C,Ssharp],[S,I-NE]] squared is I. All off-diagonal vanish exactly.
assert mm(minus(identity(8),NE),S)==[[R() for _ in range(36)] for _ in range(8)];assert mm(S,minus(identity(36),contrast))==[[R() for _ in range(36)] for _ in range(8)]
result={'status':'native-sector-contrast-to-electron-candidate-constructed','sourceSubspace':'C_N=L_N-N_N, rank 2; already inside one native N field','contrastFrame':serialize(K),'electronFrame':serialize(Eframe),'NEcandidateMatrix':serialize(S),'identities':['S Ssharp=N_E','Ssharp S=L_N-N_N','S N_N=0','N_E S=S','S R_C3=(J V_native J*) S'],'nativeElectronAction':serialize(V),'fiveCoefficientTest':{'ansatz':'Identify the native active-window contrast coordinates with the native three-sector contrast coordinates in the stated real basis.','sourceActiveSlots':[1,2,3],'targetActiveSlots':[3,2,4],'nativePermutation':pi,'activeContrastReflection':serialize(reflection),'exactIdentity':'S B_N=B_E Pi_NE on all five input coordinates','representedRank':2,'unrepresentedInputDimension':3,'geometricIdentificationOfWindowCycleAndSectorRotationDerived':False},'losslessExtension':{'dimension':44,'metric':'diag(M_N,I_8)','formula':'[[I-C_N,Ssharp],[S,I-N_E]]','squareIdentity':True,'interpretation':'Unitary exchange between two channel subspaces in a direct sum, not cloning or a particle-creation/Fock-space law.'},'defectAccounting':{'sourceContrastDefectEigenvalue':1,'targetReturnDefectEigenvalue':0,'conservedBySwap':False,'requiredInput':'A dynamics/work/reservoir rule if this conversion is to be interpreted physically.'},'scope':'Uses actual native N contrast projector and an actual native electron C3 action; no second independent baryon copy added. Replaces exact return-intertwining with an explicit conversion of previously rejected relative-sector modes. Five-slot contrast ansatz passes NE algebra but its geometric/source identification and the remaining three coefficients are not derived. Does not complete PN/NE path coherence or establish physical dynamics. Production/viewer unchanged.'}
files=[Path(__file__).resolve(),Path(__file__).with_name('exact_multiradical.py'),storePath,phasePath,rulesPath,BASE/'common-three-carrier-protocol/neutron.json',BASE/'common-three-carrier-protocol/electron.json',BASE/'baryon-tensor-grid/verification.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=BASE/'neutron-contrast-electron-transport';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'sourceContrastRank':2,'nativeElectronReturnRank':2,'nativeC3Intertwining':True,'fiveSlotNEContrastIdentity':True,'directSumSwapDimension':44,'defectConserved':False}))
