"""All24 index permutations, character projectors and native cyclic blocks."""
from pathlib import Path
from itertools import permutations
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_decorated_sector_carrier as d
A,I,mul,add,scale=d.A,d.I,d.mul,d.add,d.scale
ranksP,ranksN=[row['complexRanks'] for row in d.rows]
perms=list(permutations(range(4)))
def census(source,target):
    rows=[]
    for sigma in perms:
        obstruction=next((i for i in range(4) if source[i]!=target[sigma[i]]),None)
        rows.append({'permutation':list(sigma),'rankCompatible':obstruction is None,
                     'firstRankObstruction':None if obstruction is None else {'sourceSector':obstruction,'sourceRank':source[obstruction],'targetRank':target[sigma[obstruction]]}})
    return rows
pp,nn,pn=census(ranksP,ranksP),census(ranksN,ranksN),census(ranksP,ranksN)
compatible=lambda rows:[row['permutation'] for row in rows if row['rankCompatible']]
assert compatible(pp)==compatible(nn)==[[0,1,2,3]]
assert compatible(pn)==[[0,2,1,3]]
assert d.substituted==[d.N[i] for i in [0,2,1,3]]
assert not d.task.result['strictTaskPossibleInDeclaredClass']
# Actual Klein-four character projectors and their multiplicities.
RL=d.sub(scale(A(2),d.r.Pop['L']),I)
RG=d.sub(scale(A(2),d.r.Pop['G']),I)
characters=[]
for label,E in zip(d.orders,d.P):
    a,b=map(int,label);sa,sb=2*a-1,2*b-1
    fourier=scale(A(d.task.pn.F(1,4)),mul(add(I,scale(A(sa),RL)),add(I,scale(A(sb),RG))))
    assert fourier==E
    assert mul(RL,E)==scale(A(sa),E) and mul(RG,E)==scale(A(sb),E)
    characters.append({'sector':label,'RL_eigenvalue':sa,'RG_eigenvalue':sb,'multiplicity':ranksP[len(characters)]})
# All original field generators commute with these idempotents, verified in d.
assert d.result['operatorTransport']['properRotationsChecked']==12
assert d.result['operatorTransport']['derivedReflectionsChecked']==2
C=d.cycle;C2=mul(C,C)
assert mul(C2,C)==mul(C,C2)==I
metric_unitary=mul(d.r.sharp(C,d.task.pmetric),C)==I
assert not metric_unitary
blocks2=[[mul(mul(E,C2),F) for F in d.P] for E in d.P]
assert add(*(block for row in blocks2 for block in row))==C2
def incidence(blocks):
    return [{'source':d.orders[j],'target':d.orders[i],'nonzeroMatrixEntries':len(blocks[i][j])}
            for i in range(4) for j in range(4) if blocks[i][j]]
forward,inverse=incidence(d.cycle_blocks),incidence(blocks2)
forward_pairs={(x['source'],x['target']) for x in forward}
inverse_pairs={(x['source'],x['target']) for x in inverse}
assert forward_pairs==inverse_pairs
assert {(a,b) for a,b in forward_pairs if a!=b}=={('01','11'),('00','10')}
assert all((b,a) not in forward_pairs for a,b in forward_pairs if a!=b)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'fixed-field-index-lift-trivial-PN-role-exchange-coarse-only',
        'abstractProjectorAlgebraAutomorphisms':'S4 on the four primitive idempotents of C^4',
        'fixedFieldIndexImages':{'P':compatible(pp),'N':compatible(nn),'permutationsTestedPerField':24,'excludedPerField':23,'realization':'identity map','withinSectorAutomorphismsNotClassified':True},
        'PNComparison':{'rankCompatiblePermutations':compatible(pn),'coarseMetricProjectorLiftExists':True,'strictGeometricC3LiftExists':False,'certificate':'Fresh coarse PN factor/role identities and universal geometric-C3 obstruction; not rank matching alone.'},
        'rankCensuses':{'PtoP':pp,'NtoN':nn,'PtoN':pn},
        'KleinCharacterProjectors':characters,'previous48ElementGroupIndexImage':'identity only; acts within character sectors',
        'orderedCornerCycle':{'cubeIdentity':True,'inverse':'C^2','metricUnitary':False,'blocks':forward,'inverseBlocks':inverse,'sameForwardAndInverseBlockSupport':True,'offDiagonalDirections':[['01','11'],['00','10']]},
        'scope':'Only index permutations of entire represented sectors. Abstract S4 need not lift. Directed block incidence is not a stochastic transition or whole-sector bijection; reversible linear cycles need not preserve the native metric. No physical constructor or global sewing claim.',
        'fullS4FieldLift':False,'monsterGateActivated':False,
        'nextObligation':'Test exact block-composition laws and cancellation before treating block incidence as a transition grammar; keep metric-adjoint transport distinct from inverse transport.'}
sources=[Path(__file__),Path(d.__file__),ROOT/'research/strominger/decorated-index-lifts-v1.md',BASE/'decorated-sector-carrier/verification.json',BASE/'task-first-PN-conversion/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'decorated-index-lifts';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','fixedFieldIndexImages','PNComparison','orderedCornerCycle']}))
