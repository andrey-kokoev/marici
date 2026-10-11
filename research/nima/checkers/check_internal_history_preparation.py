"""Can internal carrier/bank allocation fund a history-sensitive contrast?

New conditional preparation map; old return U is unchanged. The bank's
previous zero-mean restriction is explicitly relaxed. This does not reproduce
(u+beta*d,-beta*d), and does not derive native physical preparation.
"""
from pathlib import Path
import hashlib
import json
import sympy as S
from fractions import Fraction as F
from check_phase_memory_first_moment import step, total

ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB')
j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
d=S.Matrix([int(k==i)-int(k==j) for k in range(12)])
u=S.ones(12,1)
base=u.col_join(S.zeros(12,1))
D=S.eye(12).row_join(S.eye(12))
# Two existing decoder-kernel directions. Neither is an added reservoir.
a=u.col_join(-u)/2
b=d.col_join(-d)
V=a.row_join(b)
G=V.T*V
checklist=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checklist.append(name)

check('internal-mode-Gram',G==S.diag(6,4))
check('both-modes-in-decoder-kernel',D*V==S.zeros(12,2))
C=G.inv()*V.T
P=V*C
U=S.Matrix.hstack(*(S.Matrix(sum(step(tuple(F(int(k==col)) for k in range(12)),
                                        tuple(F(int(12+k==col)) for k in range(12))),()))
                    for col in range(24)))
check('old-return-on-internal-modes',U*V==V*S.diag(1,-1))

t=S.symbols('t',real=True)
c=(3-2*t*t)/(3+2*t*t)
beta=6*t/(3+2*t*t)
# Rotation for metric diag(6,4), rationally parametrized.
R=S.Matrix([[c,-S.Rational(2,3)*beta],[beta,c]])
check('internal-rotation-isometry',S.simplify(R.T*G*R-G)==S.zeros(2))
check('preparation-amplitude-relation',S.simplify(3*c*c+2*beta*beta-3)==0)
E=S.eye(24)-P+V*R*C
check('full-preparation-isometry',S.simplify(E.T*E-S.eye(24))==S.zeros(24))
check('decoded-payload-protected',S.simplify(D*E-D)==S.zeros(12,24))
check('history-control-covariance',S.simplify(U*E-E.subs(t,-t)*U)==S.zeros(24))
check('inverse-control',S.simplify(E.subs(t,-t)*E-S.eye(24))==S.zeros(24))
expected=((1+c)*u/2+beta*d).col_join((1-c)*u/2-beta*d)
check('prepared-state',S.simplify(E*base-expected)==S.zeros(24,1))
check('total-original-budget',S.simplify(S.Rational(20,3)*(expected.T*expected)[0]-80)==0)
check('record-mean-explicitly-nonzero',S.simplify(sum(expected[12:,0])/12-(1-c)/2)==0)

first=S.simplify(expected.subs(t,-1))
second=S.simplify(expected.subs(t,1))
check('actual-history-sign-orbit',U*first==second and U*second==first and first!=second)
check('fixture-common-allocation',sum(first[:12,0])/12==S.Rational(3,5)
      and sum(first[12:,0])/12==S.Rational(2,5))
check('fixture-contrast-magnitude',abs(beta.subs(t,1))==S.Rational(6,5))
check('fixture-carrier-budget',S.Rational(20,3)*(first[:12,:].T*first[:12,:])[0]==48)
check('fixture-record-budget',S.Rational(20,3)*(first[12:,:].T*first[12:,:])[0]==32)
check('old-return-cannot-prepare',U*base==base and first!=base)
check('not-the-old-field-encoding',first[:12,:] != u-beta.subs(t,1)*d)

# Exact boundary: with decoded payload u AND mean-zero bank, write
# x=u-r; then budget=80+(40/3)||r||^2. Any nonzero bank exceeds 80.
r=S.Matrix(S.symbols('r0:12',real=True))
raw=S.expand(S.Rational(20,3)*((u-r).dot(u-r)+r.dot(r)))
check('zero-mean-bank-budget-obstruction',S.expand(raw-80+S.Rational(40,3)*sum(r)
       -S.Rational(40,3)*r.dot(r))==0)

result={
    'schema':'marici.nima.internal-history-preparation.v1','status':'pass','checks':checklist,
    'preparation':'rotate the existing common antisymmetric allocation into the AB/BA antisymmetric contrast',
    'formula':'c=(3-2t^2)/(3+2t^2), beta=6t/(3+2t^2); x=(1+c)u/2+beta*d; r=(1-c)u/2-beta*d',
    'invariants':['x+r=u','total inherited budget=80','U E_t = E_-t U'],
    'fixture':{'t':[-1,1],'carrier_common':'3/5','bank_common':'2/5','contrast_magnitude':'6/5',
               'carrier_budget':48,'bank_budget':32,'total_budget':80},
    'amplitude_bound':'|beta|<=sqrt(3/2) for this internal allocation budget',
    'changed_assumption':'bank mean is now allowed to be nonzero; no identification with prior zero-mean-bank preparation',
    'unselected':'the rotation/preparation operation, control magnitude t and physical coupling are supplied, not native-derived',
    'unchanged_obstruction':'the original return fixes the initial state; this preparation is an additional operation',
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/internal-history-preparation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checklist)} exact internal-preparation checks')
print('Budget 80 can prepare a contrast WITHOUT an extra mode, if the bank mean is allowed to change.')
print('Fixture: carrier 48 + bank 32. Preparation coupling remains supplied; original U alone cannot do it.')
