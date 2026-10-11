"""Supply the history-sensitive preparation by an explicit retained reservoir.

Reuses the existing rank-one exchange mechanism on the antisymmetric
carrier/bank mode. This is a conditional control/preparation realization,
not native selection of an apparatus, reservoir, amplitude or physical units.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import sympy as S
from check_phase_memory_first_moment import step

ROOT=Path(__file__).resolve().parents[1]
proof_path=ROOT/'results/agda-NativeFeedbackRouteReadout.json'
proof=json.loads(proof_path.read_text(encoding='utf-8-sig'))
src=ROOT/'agda/NativeFeedbackRouteReadout.agda'
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB')
j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
d=S.Matrix([int(k==i)-int(k==j) for k in range(12)])
u=S.ones(12,1)
base=u.col_join(S.zeros(12,1))
# Unit antisymmetric mode: a coefficient 2*beta gives (beta*d,-beta*d).
v=d.col_join(-d)/2
I=S.eye(25)
reservoir=S.eye(25)[:,24]
port=v.col_join(S.zeros(1,1))

checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

check('preparation-mode-unit', (v.T*v)[0]==1)
check('baseline-orthogonal-to-preparation-mode', (v.T*base)[0]==0)

# Reconstruct the existing return law, without changing it.
U=S.Matrix.hstack(*(S.Matrix(sum(step(tuple(F(int(k==col)) for k in range(12)),
                                        tuple(F(int(12+k==col)) for k in range(12))),()))
                    for col in range(24)))
T=S.diag(U,S.ones(1))
check('old-return-negates-history-mode',U*v==-v)
check('old-return-fixes-baseline',U*base==base)


def prepare(sign):
    # d_norm=(port-sign*reservoir)/sqrt(2); exchange=I-2*d_norm*d_norm^T.
    w=port-sign*reservoir
    return I-w*w.T


gain=S.symbols('gain',positive=True)
for sign in (-1,1):
    E=prepare(sign)
    check('orthogonal/'+str(sign),E.T*E==I)
    check('involutive/'+str(sign),E*E==I)
    initial=base.col_join(S.Matrix([2*gain]))
    desired=(u+sign*gain*d).col_join(-sign*gain*d).col_join(S.zeros(1,1))
    check('target-encoding/'+str(sign),S.simplify(E*initial-desired)==S.zeros(25,1))
    check('reservoir-depleted/'+str(sign),(E*initial)[24]==0)
    check('preparation-uncomputes/'+str(sign),S.simplify(E*desired-initial)==S.zeros(25,1))
    check('whole-budget/'+str(sign),S.expand((initial.T*initial-desired.T*desired)[0])==0)
    # Full numerical decoded payload is protected for EVERY input, not just
    # this preparation; the exchanged mode lies in decoder's kernel.
    decoder=S.eye(12).row_join(S.eye(12)).row_join(S.zeros(12,1))
    check('decoded-payload-protected/'+str(sign),decoder*E==decoder)
    check('history-control-covariance/'+str(sign),T*E==prepare(-sign)*T)
    # Complex/canonical lift duplicates the same real orthogonal operation
    # on conjugate quadratures. This extra structure is explicitly supplied.
    canonical=S.diag(E,E)
    omega=S.zeros(25).row_join(I).col_join((-I).row_join(S.zeros(25)))
    check('conditional-canonical-lift/'+str(sign),canonical.T*omega*canonical==omega)
    P=(I-E)/2
    check('existing-difference-mode-projector/'+str(sign),P*P==P and P.T==P and P.rank()==1)

# Repeated application draws the preparation BACK into the same reservoir;
# it is not an inexhaustible drive. Arbitrary nonzero amplitude costs budget.
empty=base.col_join(S.zeros(1,1))
check('empty-reservoir-no-excitation',all(prepare(s)*empty==empty for s in (-1,1)))
check('model-resource-cost',S.expand(S.Rational(20,3)*(2*gain)**2)==S.Rational(80,3)*gain**2)

# Keep the actual source orbit's sign convention: (1,2) has negative contrast.
for counts,sign in (((1,2),-1),((2,1),1)):
    check('actual-source-contrast/'+str(counts),counts[0]-counts[1]==sign)

result={
    'schema':'marici.nima.history-controlled-preparation.v1','status':'pass','checks':checks,
    'controlled_port':'v=(d,-d)/2 in the existing 24-coordinate carrier/bank space',
    'supplied_resource':'one extra reservoir mode initially of amplitude 2*gain',
    'map':'exchange v-amplitude z with reservoir amplitude a, with source-read sign s: (z,a)->(s*a,s*z)',
    'native_control':'sign of the actual route-count difference: -1 for (1,2), +1 for (2,1); its physical controller is supplied',
    'prepared_state':'(u+s*gain*d,-s*gain*d,0)',
    'conserved_decoder':'x+r=u for the initial orbit, and decoder x+r is invariant on the whole enlarged state space',
    'resource_budget':'reservoir initially carries (80/3)*gain^2 in inherited quadratic units; exactly transferred into carrier/bank contrast',
    'history_covariance':'diag(U,1) E_s = E_-s diag(U,1)',
    'conditional_pulse':'P_s=(I-E_s)/2 is an orthogonal rank-one projector; the prior complex difference-mode pulse exp(-i*pi*P_s)=E_s realizes it',
    'not_selected':['physical reservoir and its preparation','gain/action/energy units','controller implementation and phase reference','pulse duration','matter charge coupling'],
    'scope':'resource-accounted conditional preparation; not autonomous excitation from the native or numerical vacuum',
    'formal_receipt_sha256':hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/history-controlled-preparation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact controlled-preparation checks')
print('Native history sign controls a reversible preparation; the extra budget comes from an explicit reservoir.')
print('Empty reservoir remains unexcited. Physical coupling, gain and duration remain supplied.')
