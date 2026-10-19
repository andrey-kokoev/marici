"""Lossless metric direct-sum carrier from actual P/N joint projectors."""
from pathlib import Path
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_task_first_PN_conversion as task
s=task.square;r=s.r
A,I,ZERO,ONE=s.A,s.I,s.ZERO,s.ONE
mul,add,scale=s.product,s.plus,s.scaled
sub=s.minus
orders=['11','10','01','00']
def sectors(ops):
    L,G,N=(ops[k] for k in ['L','G','N'])
    return [N,sub(L,N),sub(G,N),add(I,scale(A(-1),L),scale(A(-1),G),N)]
P,N=sectors(r.Pop),sectors(r.Nop)
rows=[]
for name,blocks,metric,expected in [('P',P,task.pmetric,[1,11,2,22]),('N',N,task.nmetric,[1,2,11,22])]:
    assert add(*blocks)==I
    for i,E in enumerate(blocks):
        assert E and r.sharp(E,metric)==E
        assert r.trace(E)==A(expected[i])
        for j,F in enumerate(blocks):assert mul(E,F)==(E if i==j else {})
    assert add(*(mul(r.sharp(E,metric),E) for E in blocks))==I
    # sum is inverse to extraction on the constrained product of sector ranges.
    # Each E_i fixes its own range and annihilates all other ranges, as above.
    rows.append({'species':name,'sectorOrder':orders,'complexRanks':expected,'totalDimension':sum(expected),
                 'projectorProductsChecked':16,'metricOrthogonal':True,'bothInverseLaws':True,'allInputMetricIdentity':True})
# The coarse PN construction freshly checked the exact two role identities
# through its native36-coordinate normalization and tensor factors.
assert 'S L_P=G_N S' in task.pn.result['identities']
assert 'S G_P=L_N S' in task.pn.result['identities']
role_swap=[0,2,1,3]
assert [rows[1]['complexRanks'][i] for i in role_swap]==rows[0]['complexRanks']
# Verify the induced label substitution at the polynomial level: E_ab(L,G)
# goes to E_ba(L_N,G_N). Variables here are the exact source projectors.
LN,GN,NN=(r.Nop[k] for k in ['L','G','N'])
substituted=[mul(GN,LN),sub(GN,mul(GN,LN)),sub(LN,mul(GN,LN)),add(I,scale(A(-1),GN),scale(A(-1),LN),mul(GN,LN))]
assert substituted==[N[i] for i in role_swap]
# These already independently constructed rotations preserve every projector.
for U in s.targetActions.values():
    for E in P:assert mul(U,E)==mul(E,U)
for reflection in [sub(scale(A(2),r.Pop['L']),I),sub(scale(A(2),r.Pop['G']),I)]:
    for E in P:assert mul(reflection,E)==mul(E,reflection)
# A source-defined ordered corner cycle need not be block diagonal. Retain
# off-diagonal blocks instead of assuming all operations preserve the sectors.
cycle=r.cycleP
cycle_blocks=[[mul(mul(E,cycle),F) for F in P] for E in P]
assert add(*(block for row in cycle_blocks for block in row))==cycle
nonzero_offdiagonal=sum(bool(cycle_blocks[i][j]) for i in range(4) for j in range(4) if i!=j)
# Phase-sensitive control from actual return and relative-sector source vectors.
j=next(j for j in range(36) if (j,j) in r.Pop['N'])
u=[task.decode(r.Pop['N'].get((i,j),ZERO).record()) for i in range(36)]
norm=task.norm(u,task.pmetric)
u=[x*task.sqrt(1/task.rational(norm)) for x in u]
v=task.x
from fractions import Fraction as F
states=[[task.sqrt(F(1,2))*(a+sign*b) for a,b in zip(u,v)] for sign in [1,-1]]
packets=[[task.apply(E,x) for E in P] for x in states]
assert packets[0]!=packets[1]
for x,packet in zip(states,packets):assert [sum((v[i] for v in packet),task.R()) for i in range(36)]==x
weights=[[task.rational(task.norm(v,task.pmetric)) for v in packet] for packet in packets]
assert weights[0]==weights[1]==[F(1,2),0,F(1,2),0]
Up,Un=r.Pthird[0],r.Nthird[0]
def residual(x):return [a-b for a,b in zip(task.apply(Un,task.convert(x)),task.convert(task.apply(Up,x)))]
e0,e1=map(residual,states)
assert e0!=e1 and e0==[-a for a in e1]
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'lossless-four-index-continuous-sector-carrier-constructed',
        'carriers':rows,'extraction':'x -> (E11 x,E10 x,E01 x,E00 x)',
        'inverse':'sum of sector vectors','carrierType':'direct sum of complex subspaces, not a four-value set',
        'PNRoleExchange':{'sourceOrder':orders,'targetLabels':['11','01','10','00'],'certificate':'Fresh full-coefficient factor proof of S L_P=G_N S and S G_P=L_N S; polynomial substitution gives each sector intertwiner.'},
        'operatorTransport':{'formula':'A_ij=E_i A E_j','compositionLaw':'(AB)_ik=sum_j A_ij B_jk','properRotationsChecked':12,'derivedReflectionsChecked':2,'orderedCornerCycleBlocksRecovered':True,'orderedCornerCycleNonzeroOffDiagonalBlocks':nonzero_offdiagonal},
        'weightsOnlyLosesRelativePhase':True,'fullVectorsRecoverFixedReferenceField':True,
        'strictPNGeometricObstructionRepaired':False,'fourDiscreteStateClaimRevived':False,
        'S4FieldLiftEstablished':False,'physicalConstructorEstablished':False,'monsterGateActivated':False,
        'scope':'Exact coordinate reconstruction and typed operation blocks of supplied P/N fields. No new native move, arbitrary sector permutation, physical four-state system or global interface sewing.',
        'nextObligation':'Classify index relabellings within a fixed field versus between role-exchanged presentations, retaining metric, ranks and source operation labels.'}
sources=[Path(__file__),Path(task.__file__),ROOT/'research/strominger/decorated-sector-carrier-v1.md',BASE/'task-first-PN-conversion/verification.json',BASE/'global-PN-transport/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'decorated-sector-carrier';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','carriers','operatorTransport','weightsOnlyLosesRelativePhase','S4FieldLiftEstablished']}))
