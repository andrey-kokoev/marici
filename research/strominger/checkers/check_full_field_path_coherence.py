"""Lift native coefficient path comparison; test fixed vs framed alignment."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
from assemble_metric_coefficient_protocol import A,ONE,ZERO,read_operator,product,plus,scaled
BASE=ROOT/'research/strominger/results'
def decode(d):return A(tuple(F(d.get(str(i),0)) for i in range(16)))
def adj(m):return {(j,i):v.flip(8) for (i,j),v in m.items()}
def perm(p):return {(i,j):ONE for i,j in enumerate(p)}
def embed(entries):return {(e['row'],e['column']):decode(e['value']) for e in entries}
paths=json.loads((BASE/'window-combination-coherence/verification.json').read_text());witness=next(e for e in paths['coefficientFrameHolonomyExamples'] if len(e['paths'][0]['word'])==3 and all(p['retainedCombinationAudit'].get('allContactsWitnessed') for p in e['paths']))
h=witness['relativeCoefficientPermutation'];H=perm(h);I5=perm(list(range(5)));I36=perm(list(range(36)));power=I5
for i in range(5):power=product(H,power);assert (power==I5)==(i==4)
source=json.loads((BASE/'common-three-carrier-protocol/proton.json').read_text());labels=source['source']['coordinates'];ops={k:read_operator(source['operators'][k],36) for k in ['L','G','N']};bindings=json.loads((BASE/'geometric-coefficient-binding/verification.json').read_text());B=embed(bindings['geometricSeeds'][0]['embedding']);assert product(adj(B),B)==I5
# The fixed-alignment obstruction is independent of this particular B:
# any A4-equivariant B intertwines the group averages G36 and Q5.
group={(0,1,2,3)};q=list(group)
for g in q:
    for s in [(1,2,0,3),(3,0,2,1)]:
        t=geo.compose(s,g)
        if t not in group:group.add(t);q.append(t)
Us=[];Vs=[]
for g in group:
    R=geo.rotation(g);U={};V={(g[j],j):ONE for j in range(4)};V[4,4]=ONE
    for j,label in enumerate(labels):
        edge,axis=label.split(':');new=''.join('ABCD'[g['ABCD'.index(v)]] for v in edge)
        for i in range(3):
            if R[i]['xyz'.index(axis)]:U[labels.index(new+':'+'xyz'[i]),j]=A(R[i]['xyz'.index(axis)])
    Us.append(U);Vs.append(V)
    assert product(U,B)==product(B,V)
Gavg=scaled(A(F(1,12)),plus(*Us));Q=scaled(A(F(1,12)),plus(*Vs));assert Gavg==ops['G'];assert product(ops['G'],B)==product(B,Q)
comm=plus(product(Q,H),scaled(A(-1),product(H,Q)));assert comm
# Algebraic coefficient comparison group; not asserted spatial A5 symmetry.
compose=lambda p,q:tuple(p[q[i]] for i in range(5))
generators=[(1,2,0,3,4),(3,0,2,1,4),tuple(h)];closure={tuple(range(5))};queue=list(closure)
for p in queue:
    for g in generators:
        t=compose(g,p)
        if t not in closure:closure.add(t);queue.append(t)
assert len(closure)==60
# A concrete full-fiber lift. It acts as H on the five-dimensional embedded
# subspace and as identity on its orthogonal 31-dimensional complement.
projector=product(B,adj(B));complement=plus(I36,scaled(A(-1),projector))
def lift(X):return plus(product(product(B,X),adj(B)),complement)
U=lift(H);assert product(U,B)==product(B,H);assert product(adj(U),U)==I36
# Certify the composition law on this generator, then iterate exact powers.
U2=product(U,U);assert U2==lift(product(H,H));U4=product(U2,U2);assert product(U4,U)==I36
failures={k:product(op,U)!=product(U,op) for k,op in ops.items()};assert all(failures.values())
framed={k:product(product(U,op),adj(U)) for k,op in ops.items()}
for k in ops:assert product(framed[k],U)==product(U,ops[k])
assert product(framed['G'],framed['L'])==framed['N']
# A visible five-component witness to the universal fixed-G obstruction.
entry=sorted(comm)[0]
result={'status':'full-field-lift-works-only-with-covariant-frame-for-this-binding','nativePathWitness':witness,'relativeCoefficientOrder':5,'coefficientGroupWithTetrahedralRotationsOrder':len(closure),'universalFixedAlignmentObstruction':{'nativeGIsTetrahedralGroupAverage':True,'domainAverage':'Q=diag(J_4/4,1)','QCommutesWithObservedFiveCycle':False,'commutatorWitness':{'entry':entry,'value':comm[entry].record()},'proof':'For any injective A4-equivariant B, G B=B Q. If U B=B H and UG=GU, then B(QH-HQ)=0, contradicting injectivity. Thus no choice of geometric A4-equivariant B removes this fixed-G obstruction.'},'full36Lift':{'formula':'U_H=B H B* + I-B B*','metricUnitary':True,'order':5,'embeddedCoefficientsIntertwine':True,'complementDimension':31,'fixedNativeOperatorFailures':failures,'covariantFrameRule':'X_new=U_H X_old U_H* for X=L,G,N','allCovariantIntertwiningChecksPass':True},'scope':'Exact P endpoint-fiber comparison for a contact-witnessed open native path pair. Constructed lift uses one geometric candidate embedding and identity on its complement; this extension is not unique. A coefficient-frame change can preserve physical operator equivalence while changing component matrices. No native species-changing 36-component PN/NE connection derived, no identification of the coefficient A5 group as spatial symmetry, and no completed electron-exit assembly claimed.'}
files=[Path(__file__).resolve(),BASE/'window-combination-coherence/verification.json',BASE/'geometric-coefficient-binding/verification.json',BASE/'common-three-carrier-protocol/proton.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=BASE/'full-field-path-coherence';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'unitary36Lift':True,'order':5,'fixedNativeProjectorsPreserved':False,'frameCovariantProjectors':True,'universalA4FixedAlignmentObstruction':True}))
