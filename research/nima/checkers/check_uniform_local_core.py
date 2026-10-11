"""Exact algebraic controls for the written all-time standard-C4 existence proof."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,ok):
    if not ok: raise AssertionError(name)
    checks.append(name)
def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(c,a): return tuple(tuple(c*x for x in r) for r in a)
def mul(a,b): return tuple(tuple(sum(x*y for x,y in zip(r,s)) for s in zip(*b)) for r in a)
def tr(a): return tuple(zip(*a))
def kron(a,b): return tuple(tuple(x*y for x in r for y in s) for r in a for s in b)
def linearize(mapping):
    if sorted(mapping)!=list(range(len(mapping))): raise ValueError('not a bijection')
    return tuple(tuple(F(i==mapping[j]) for j in range(len(mapping))) for i in range(len(mapping)))
def projector(p): return scale(F(1,2),add(eye(len(p)),scale(-1,p)))
def phase(q,c,s): return add(eye(len(q)),scale(c-1,q)),scale(s,q)
def cmul(a,b): return add(mul(a[0],b[0]),scale(-1,mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))
def adj(a): return tr(a[0]),scale(-1,tr(a[1]))
def conj(p,a): return mul(mul(p,a),tr(p))
I=eye(4); Z=scale(0,I)
left=linearize(tuple(j^2 for j in range(4)))
right=linearize(tuple(j^1 for j in range(4)))
X=linearize((1,0)); q=projector(X)
check('source-map-left-tensor',left==kron(X,eye(2)))
check('source-map-right-tensor',right==kron(eye(2),X))
phases=[(F(1),F(0)),(F(-1),F(0)),(F(0),F(-1)),(F(3,5),F(-4,5))]
for name,p,side in [('left',left,0),('right',right,1)]:
    Q=projector(p); complement=add(I,scale(-1,Q))
    check(name+'/native-basis-action',all(p[i][j]==F(i==(j^(2 if side==0 else 1))) for i in range(4) for j in range(4)))
    check(name+'/self-adjoint-involution',tr(p)==p and mul(p,p)==I)
    check(name+'/orthogonal-projectors',mul(Q,Q)==Q and tr(Q)==Q and mul(Q,complement)==Z and mul(complement,Q)==Z)
    check(name+'/derived-generator-local',Q==(kron(q,eye(2)) if side==0 else kron(eye(2),q)))
    check(name+'/zero-endpoint',phase(Q,F(1),F(0))==(I,Z))
    check(name+'/one-endpoint',phase(Q,F(-1),F(0))==(p,Z))
    for k,(c,s) in enumerate(phases):
        u=phase(q,c,s); U=phase(Q,c,s)
        check(f'{name}/unitarity/{k}',cmul(adj(U),U)==(I,Z))
        expected=tuple(kron(part,eye(2)) if side==0 else kron(eye(2),part) for part in u)
        check(f'{name}/leg-tensor/{k}',U==expected)
        for i in range(2):
            for j in range(2):
                E=tuple(tuple(F(a==i and b==j) for b in range(2)) for a in range(2))
                e=(E,scale(0,E)); local=cmul(cmul(u,e),adj(u))
                own=kron(E,eye(2)) if side==0 else kron(eye(2),E)
                other=kron(eye(2),E) if side==0 else kron(E,eye(2))
                expected=tuple(kron(part,eye(2)) if side==0 else kron(eye(2),part) for part in local)
                check(f'{name}/factor-algebra/{k}/{i}/{j}',cmul(cmul(U,(own,Z)),adj(U))==expected)
                check(f'{name}/other-factor-fixed/{k}/{i}/{j}',cmul(cmul(U,(other,Z)),adj(U))==(other,Z))
    for index,mapping in enumerate(permutations(range(4))):
        T=linearize(mapping)
        check(f'{name}/projector-covariance/{index}',projector(conj(T,p))==conj(T,Q))
        c,s=phases[-1]
        check(f'{name}/leg-covariance/{index}',phase(projector(conj(T,p)),c,s)==tuple(conj(T,part) for part in phase(Q,c,s)))
check('square-commutes',mul(left,right)==mul(right,left))
check('generator-commutes',mul(projector(left),projector(right))==mul(projector(right),projector(left)))
S=linearize((0,2,1,3))
check('factor-exchange',conj(S,left)==right and conj(S,right)==left)
for a in (0,1):
    for b in (0,1):
        p=mul(right if b else I,left if a else I)
        check(f'corner/{a}/{b}',p==linearize(tuple(j^(2*a)^b for j in range(4))))
contract=ROOT/'contracts/uniform-local-core-test.v1.json'
note=ROOT/'uniform-local-core-proof.md'
r={'status':'pass','claim':'source-derived-local-core-exists','outcome':'++',
   'proof_kind':'written_all_time_mathematical_proof_supported_by_exact_algebraic_checks',
   'semantic_backend':'standard finite-dimensional complex Hilbert spaces',
   'checks_passed':len(checks),'checks':checks,
   'witness':'free-linearized native flips with H_j=pi*(I-P_j)/2 and U_j(t)=exp(-i*t*H_j)',
   'phase_is_constructor_output_not_input':True,
   'proof_note':note.relative_to(ROOT).as_posix(),
   'kernel_verified_analytic_theorem':False,'completion_backend_verified':False,'whole_tick_return_verified':False,
   'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (contract,note,Path(__file__).resolve())}}
(ROOT/'results/uniform-local-core.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='checks'},indent=2))
