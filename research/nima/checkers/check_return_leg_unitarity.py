"""Exact rational/complex tests; projector identities support the all-time proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
checks = []
def check(name, ok):
    if not ok:
        raise AssertionError(name)
    checks.append(name)

def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))
def add(a, b):
    return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(x, a):
    return tuple(tuple(x*y for y in r) for r in a)
def mm(a,b):
    return tuple(tuple(sum(x*y for x,y in zip(r,c)) for c in zip(*b)) for r in a)
def transpose(a):
    return tuple(zip(*a))
def kron(a,b):
    return tuple(tuple(x*y for x in r for y in s) for r in a for s in b)

I = eye(4)
Z = scale(0,I)
X = ((F(0),F(1)),(F(1),F(0)))
flips = {'left': kron(X,eye(2)), 'right': kron(eye(2),X)}
source = ROOT / 'agda/TickPolynomialRealization.agda'
check('source-affine-leg', 'leg A a v q = (1r + (- a)) · v q + a · A v q' in source.read_text(encoding='utf-8'))
# Complex matrices are pairs of rational matrices: no floating arithmetic.
def cmul(a,b):
    ar,ai=a; br,bi=b
    return add(mm(ar,br),scale(-1,mm(ai,bi))), add(mm(ar,bi),mm(ai,br))
def adj(a):
    return transpose(a[0]),scale(-1,transpose(a[1]))
def phase(Q,c,s):
    return add(I,scale(c-1,Q)),scale(s,Q)

for name,P in flips.items():
    Q=scale(F(1,2),add(I,scale(-1,P)))
    A=add(I,scale(-1,Q))
    check(name+'/involution',mm(P,P)==I and transpose(P)==P)
    check(name+'/orthogonal-spectral-projectors',mm(Q,Q)==Q and mm(A,A)==A and mm(A,Q)==Z and mm(Q,A)==Z and add(A,Q)==I)
    midpoint=scale(F(1,2),add(I,P))
    for j in range(4):
        check(name+f'/affine-midpoint-basis-{j}',sum(midpoint[i][j]**2 for i in range(4))==F(1,2))
    check(name+'/affine-not-unitary',mm(transpose(midpoint),midpoint)!=I)
    check(name+'/unitary-start',phase(Q,F(1),F(0))==(I,Z))
    check(name+'/unitary-finish',phase(Q,F(-1),F(0))==(P,Z))
    phases=[(F(1),F(0)),(F(0),F(-1)),(F(-1),F(0)),(F(3,5),F(-4,5))]
    for k,(c,s) in enumerate(phases):
        U=phase(Q,c,s)
        check(name+f'/exact-phase-unitarity-{k}',cmul(adj(U),U)==(I,Z))
    # Q is the dimensionless generator; the actual time generator is pi Q.
    q2=scale(F(1,2),add(eye(2),scale(-1,X)))
    check(name+'/generator-tensor-local',Q==(kron(q2,eye(2)) if name=='left' else kron(eye(2),q2)))
    check(name+'/midpoint-replacement-norm',sum(phase(Q,F(0),F(-1))[0][i][0]**2+phase(Q,F(0),F(-1))[1][i][0]**2 for i in range(4))==1)

QL=scale(F(1,2),add(I,scale(-1,flips['left'])))
QR=scale(F(1,2),add(I,scale(-1,flips['right'])))
check('local-generators-commute',mm(QL,QR)==mm(QR,QL))
result={'status':'pass','checks_passed':len(checks),'checks':checks,
        'affine_midpoint_norm_squared':'1/2',
        'replacement':'U(t)=(I-Q)+exp(-i*pi*t)Q; Q=(I-P)/2',
        'all_time_argument':'Q and I-Q are orthogonal self-adjoint projectors; |exp(-i*pi*t)|=1 for real t',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_note_sha256':hashlib.sha256((ROOT/'return-leg-unitarity.md').read_bytes()).hexdigest(),
        'scope':'exact matrix test and analytic projector proof; not a Cauchy-completion exponential implementation'}
(ROOT/'results/return-leg-unitarity.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
