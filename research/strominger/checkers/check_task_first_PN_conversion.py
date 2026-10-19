"""Frozen PN task: exact explicit counterexample plus universal source obstruction."""
from pathlib import Path
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_rotation_realization_square as square
    import construct_global_PN_transport as pn
r=square.r
R,sqrt,decode,rational=pn.R,pn.sqrt,pn.decode_A,pn.rational
relative=square.minus(r.Pop['G'],r.Pop['N'])
column=next(j for j in range(36) if (j,j) in relative)
x=[decode(relative.get((i,column),r.ZERO).record()) for i in range(36)]
def norm(v,metric):return sum((v[i].conj()*v[i]*metric[i] for i in range(36)),R())
pmetric=pn.p['metric'];nmetric=pn.n['metric']
x=[a*sqrt(1/rational(norm(x,pmetric))) for a in x]
assert norm(x,pmetric)==R(1)
def apply(op,v):
    out=[R() for _ in range(36)]
    for (i,j),a in op.items():out[i]+=decode(a.record())*v[j]
    return out
def convert(v):return [sum((a*b for a,b in zip(row,v)),R()) for row in pn.S]
assert apply(relative,x)==x
assert apply(r.Pop['N'],x)==[R()]*36
# Independently evaluate both actual routes, not the expected residual formula.
y=convert(x)
assert norm(y,nmetric)==R(1)
assert apply(r.Nop['L'],y)==y and apply(r.Nop['N'],y)==[R()]*36
rows=[]
for a,Up in enumerate(r.Pthird):
    assert apply(Up,x)==x
    right=convert(apply(Up,x))
    for b,Un in enumerate(r.Nthird):
        left=apply(Un,y);residual=[u-v for u,v in zip(left,right)]
        assert norm(residual,nmetric)==R(3)
        assert apply(r.Nop['N'],left)==apply(r.Nop['N'],right)==[R()]*36
        rows.append({'sourceC3Index':a,'targetC3Index':b,'fullSquaredResidual':3,'returnResidualZero':True})
assert len(rows)==16
assert all(row['returnReadoutResidualZero'] for row in square.localizations)
# Universality follows from the freshly checked native identities, role
# exchange and metric unitarity, rather than from finite candidate sampling.
assert square.result['universalConditionalConsequence'].startswith('For any metric-unitary S')
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'frozen-linear-PN-task-impossible-return-only-certificate-refuted',
        'taskDomain':'full36-component supplied P/N field charts; fixed metric/projectors/geometric C3 and reference conventions',
        'implementationClass':'metric-unitary linear maps exchanging native projector roles',
        'coarseImplementationConstructed':True,'strictTaskPossibleInDeclaredClass':False,
        'universalObstruction':'E^sharp E=3(G_P-N_P); N_N E=0',
        'relativeSectorDimension':2,'unitRelativeProbeSquaredResidual':3,
        'explicitCandidateRotationPairs':rows,'probeColumn':column,
        'normalizedProbe':pn.serialize([[a] for a in x]),
        'rival':'return-only route agreement certifies full geometric covariance on alignment inputs',
        'rivalVerdict':'rejected','fullMetricComparatorFrozenBeforeExecution':True,
        'physicalConstructorEstablished':False,'fourStateCarrierDerived':False,'monsterGateActivated':False,
        'noveltyBoundary':'Task formulation and explicit counterexample replay of an existing source obstruction; not a new obstruction theorem or explanation of why the source is physical.',
        'nextObligation':'Test a task-sufficient carrier extraction without fitting cardinality4; preserve the distinctions between operations, joint sectors and state values.'}
sources=[Path(__file__),Path(square.__file__),Path(pn.__file__),ROOT/'research/strominger/task-first-PN-conversion-v1.md',BASE/'rotation-realization-square/verification.json',BASE/'global-PN-transport/verification.json']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=BASE/'task-first-PN-conversion';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','coarseImplementationConstructed','strictTaskPossibleInDeclaredClass','unitRelativeProbeSquaredResidual','rivalVerdict','fourStateCarrierDerived']}))
