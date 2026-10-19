"""Two independent baryon returns feed E; frame copies need not be independent."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from exact_multiradical import Radical as R,sqrt,mm,adj,identity,decode_A,rational,serialize
from assemble_metric_coefficient_protocol import read_operator
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
n=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());e=json.loads((BASE/'common-three-carrier-protocol/electron.json').read_text());grid=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text())['carriers']['neutron'];metric=list(map(F,n['source']['metric']));z=[decode_A(v) for v in grid['sourceReturnColumn']];norm=rational(sum((metric[i]*v.conj()*v for i,v in enumerate(z)),R()));u=[v*sqrt(1/norm) for v in z]
assert sum((metric[i]*v.conj()*v for i,v in enumerate(u)),R())==1
nReturn=read_operator(n['operators']['N'],36)
for i in range(36):
    for j in range(36):assert u[i]*u[j].conj()*metric[j]==decode_A(nReturn[i,j].record())
storePath=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json';store=json.loads(storePath.read_text())
def decode_spinor(v):return R(F(v[0][0]))+F(v[0][1])*sqrt(3)+F(v[1][0])*sqrt(-1)+F(v[1][1])*sqrt(-3)
J=[[sqrt(F(1,2))*decode_spinor(v) for v in row] for face in store['face_projectors'] for row in face];assert mm(adj(J),J)==identity(2);Eret=mm(J,adj(J))
eReturn=read_operator(e['operators']['N'],8)
for i in range(8):
    for j in range(8):assert Eret[i][j]==decode_A(eReturn[i,j].record()) if (i,j) in eReturn else Eret[i][j]==0
# R reads one normalized return amplitude from each independent native N copy.
readout=[[u[j%36].conj()*metric[j%36] if j//36==i else R() for j in range(72)] for i in range(2)]
lift=[[u[i%36] if i//36==j else R() for j in range(2)] for i in range(72)];assert mm(readout,lift)==identity(2)
S=mm(J,readout);Ssharp=mm(lift,adj(J));assert mm(S,Ssharp)==Eret
# On source return coordinates, S* S is identity. On their orthogonal
# complement readout is zero, hence S* S=diag(N_N,N_N) exactly.
assert mm(mm(readout,Ssharp),mm(S,lift))==identity(2)
# Both source/target L,G act as identity on the checked return frames.
for key in ['L','G']:
    nop=read_operator(n['operators'][key],36);ev=read_operator(e['operators'][key],8)
    Nmat=[[decode_A(nop[i,j].record()) if (i,j) in nop else R() for j in range(36)] for i in range(36)];Emat=[[decode_A(ev[i,j].record()) if (i,j) in ev else R() for j in range(8)] for i in range(8)]
    assert mm(Nmat,[[v] for v in u])==[[v] for v in u];assert mm(Emat,J)==J
# Distinguish true extra data from an observed frame holonomy.
paths=json.loads((BASE/'window-combination-coherence/verification.json').read_text());witness=next(x for x in paths['coefficientFrameHolonomyExamples'] if len(x['paths'][0]['word'])==3 and all(p['retainedCombinationAudit'].get('allContactsWitnessed') for p in x['paths']));h=witness['relativeCoefficientPermutation'];H=[[R(int(j==h[i])) for j in range(5)] for i in range(5)];ell=[[R(F(1,2)) if i<4 else R() for i in range(5)]]
second=mm(ell,H);gram=mm([ell[0],second[0]],adj([ell[0],second[0]]));assert gram==[[R(1),R(F(3,4))],[R(F(3,4)),R(1)]]
# Holding the geometric readout fixed gives two independent candidate rows.
# If holonomy is only a frame change, its operator/readout must transform too.
covariantSecond=mm(mm(ell,adj(H)),H);assert covariantSecond==ell
result={'status':'two-independent-return-channel-interface-constructed','source':'two independent copies of the native N return line, embedded in their 72-coordinate direct sum','target':'the complete two-dimensional native E return image in its eight-coordinate raw field','sourceReturnVector':[v.record() for v in u],'electronReturnFrame':serialize(J),'matrix':serialize(S),'identities':['S Ssharp=N_E','Ssharp S=diag(N_N,N_N)','S diag(N_N,N_N)=N_E S=S'],'rank':2,'sourceComplementDiscardedDimension':70,'targetRawComplementNotPopulatedDimension':6,'pathIndependenceTest':{'fixedReadoutOverlap':'3/4','fixedReadoutGramDeterminant':'7/16','covariantlyTransportedReadoutsCoincide':True,'conclusion':'Two frame-related histories do not themselves supply two independent physical return channels. Holding the readout fixed and transforming it with the frame are different hypotheses.'},'scope':'Exact metric partial-isometry construction from two independent native return inputs, not a full-surjective NE map or a derivation of which two physical windows supply them. Rank-two output is not manufactured by declaring two coordinate frames independent. Native E projectors verified; five-slot NE permutation and global path sewing remain unbound. No production/viewer change.'}
files=[Path(__file__).resolve(),Path(__file__).with_name('exact_multiradical.py'),storePath,BASE/'baryon-tensor-grid/verification.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'common-three-carrier-protocol/electron.json',BASE/'window-combination-coherence/verification.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=BASE/'two-channel-electron-interface';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'nativeElectronReturnRankReached':2,'frameOnlyHistoriesSupplyExtraChannel':False}))
