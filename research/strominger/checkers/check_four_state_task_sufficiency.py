"""Exact five-output obstruction to a four-value task-discrepancy carrier."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_task_first_PN_conversion as task
R=task.R
N,G,Q=task.r.Pop['N'],task.r.Pop['G'],task.relative
j=next(j for j in range(36) if (j,j) in N)
u=[task.decode(N.get((i,j),task.r.ZERO).record()) for i in range(36)]
norm=task.norm(u,task.pmetric)
u=[a*task.sqrt(1/task.rational(norm)) for a in u]
v=task.x
inner=lambda a,b:sum((x.conj()*y*m for x,y,m in zip(a,b,task.pmetric)),R())
assert inner(u,v)==R() and inner(u,u)==inner(v,v)==R(1)
assert task.apply(N,u)==u and task.apply(Q,u)==[R()]*36
assert task.apply(G,u)==u and task.apply(Q,v)==v
Up,Un=task.r.Pthird[0],task.r.Nthird[0]
def residual(x):
    left=task.apply(Un,task.convert(x));right=task.convert(task.apply(Up,x))
    return [a-b for a,b in zip(left,right)]
sectors=[N,task.square.minus(task.r.Pop['L'],N),Q,
         task.square.plus(task.square.I,task.square.scaled(task.square.A(-1),task.r.Pop['L']),task.square.scaled(task.square.A(-1),G),N)]
rows=[]
for t in map(F,['0','1/4','1/2','3/4','1']):
    x=[task.sqrt(1-t)*a+task.sqrt(t)*b for a,b in zip(u,v)]
    assert task.norm(x,task.pmetric)==R(1) and task.apply(G,x)==x
    weights=[task.rational(task.norm(task.apply(P,x),task.pmetric)) for P in sectors]
    assert weights==[1-t,0,t,0]
    e=residual(x);value=task.rational(task.norm(e,task.nmetric))
    assert value==3*t and task.apply(task.r.Nop['N'],e)==[R()]*36
    rows.append({'relativeWeight':str(t),'sectorWeights':list(map(str,weights)),'fullSquaredDiscrepancy':str(value),'returnDiscrepancy':0})
values=[row['fullSquaredDiscrepancy'] for row in rows]
assert len(set(values))==5
rejected=0
for assignment in product(range(4),repeat=5):
    assert any(assignment[i]==assignment[j] and values[i]!=values[j] for i in range(5) for j in range(i))
    rejected+=1
assert rejected==1024
# Fixed support on the three interior probes does not retain the discrepancy.
supports=[tuple(i for i,w in enumerate(row['sectorWeights']) if F(w)) for row in rows[1:4]]
assert supports==[(0,2)]*3 and len({row['fullSquaredDiscrepancy'] for row in rows[1:4]})==3
# Weights are sufficient for this norm diagnostic, not the full residual vector.
plus=[task.sqrt(F(1,2))*(a+b) for a,b in zip(u,v)]
minus=[task.sqrt(F(1,2))*(a-b) for a,b in zip(u,v)]
eplus,eminus=residual(plus),residual(minus)
assert eplus!=eminus and eplus==[-a for a in eminus]
assert task.norm(eplus,task.nmetric)==task.norm(eminus,task.nmetric)==R(F(3,2))
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'four-discrete-value-extraction-refuted-for-frozen-exact-task-readout',
        'probeFamily':rows,'fourLabelAssignmentsRejected':rejected,
        'finiteCarrierCardinality':4,'requiredDistinctOutputsOnWitnessFamily':5,
        'fourDiscreteStateExtractionSufficient':False,
        'sameSectorSupportDifferentDiscrepancies':True,
        'relativeWeightRecoversAlignedDiscrepancy':True,
        'sameSectorWeightsDifferentResidualVectors':True,
        'universalScalarIdentity':'For aligned x, ||E x||_N^2 = 3 ||(G_P-N_P)x||_P^2',
        'scope':'Deterministic four-value extraction with no side channel cannot preserve the frozen exact discrepancy. Does not reject four index labels with continuous fibers. Relative-weight sufficiency is only for this aligned norm diagnostic, not full-state recovery.',
        'fullFieldRecoveryEstablished':False,'physicalValidation':False,'monsterGateActivated':False,
        'nextObligation':'Specify a continuously decorated task carrier and which data it retains; do not rename four continuous sector weights as four discrete states.'}
sources=[Path(__file__),Path(task.__file__),ROOT/'research/strominger/four-state-task-sufficiency-v1.md',BASE/'task-first-PN-conversion/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'four-state-task-sufficiency';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','probeFamily','fourLabelAssignmentsRejected','sameSectorWeightsDifferentResidualVectors']}))
