# /// script
# dependencies = ["sympy"]
# ///
"""Prior fixed-Gram bridge reuse, witnessed descent, and refusal controls."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from hamiltonian_descent_wg import generate, state, zero

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PRIOR = ROOT.parent/'nima/checkers/check_rotor_rung4_intertwiner.py'
OUT = ROOT/'results/hamiltonian-descent-wg.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(PRIOR))
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def refused(name, call, expected):
    try:
        call()
    except ValueError as error:
        check(name, expected in str(error))
    else:
        raise AssertionError(name)


check('fresh-prior-45-check-bridge', prior['out']['status'] == 'pass' and len(prior['checks']) == 45)
P4 = prior['P']
# This is explicitly a lift constructed FROM the existing bottom rotor;
# it is not an independently derived physical rung12 Hamiltonian.
source = state(prior['G12'], prior['D12'], P4.T*prior['Omega4']*P4,
               P4.T*prior['Hessian4']*P4,
               ('prior fixed-Gram rotor, declared bottom-up compatible lift',))
direct = generate(source, prior['E'], P4, 'existing direct fixed-Gram projection12->4')
check('prior-generator-recovered', zero(direct.target.D-prior['D4']))
check('prior-form-recovered', zero(direct.target.Omega-prior['Omega4']))
check('prior-energy-recovered', zero(direct.target.K-prior['Hessian4']))
x = S.Matrix(S.symbols('x0:12', real=True))
check('all-source-coordinates-reconstructed', zero(direct.E*direct.P*x+direct.N*x-x))
check('full-energy-split', S.simplify((x.T*source.K*x)[0]
      -((direct.P*x).T*direct.target.K*(direct.P*x))[0]
      -((direct.N*x).T*source.K*(direct.N*x))[0]) == 0)


def chain(schedule):
    current, composite = source, S.eye(12)
    for n, m in zip(schedule, schedule[1:]):
        E = S.eye(n)[:, :m]
        Gm = E.T*current.G*E
        P = Gm.inv()*E.T*current.G
        witness = generate(current, E, P, f'declared fixed-Gram block{n}->{m}')
        check(f'step-witness/{schedule}/{n}->{m}', zero(P*current.D-witness.target.D*P))
        composite = P*composite
        current = witness.target
    check(f'composite-projection/{schedule}', zero(composite-P4))
    check(f'composite-generator/{schedule}', zero(current.D-prior['D4']))
    check(f'composite-energy/{schedule}', zero(current.K-prior['Hessian4']))
    check(f'composite-form/{schedule}', zero(current.Omega-prior['Omega4']))
    return current


chain((12, 11, 10, 9, 8, 7, 6, 5, 4))
# Six operations can reach4 by explicitly grouping dimensional drops.
# This schedule is a declared mathematical example, NOT native rung roles.
chain((12, 10, 8, 7, 6, 5, 4))

# Hidden sector need not be stationary: give it its own oscillator and retain
# its energy. This example is separate from the specific prior rotor source.
J = S.Matrix([[0, 1], [-1, 0]])
D = S.diag(J, 2*J)
Omega = S.diag(J, J)
K = D.T*Omega
separate = state(S.eye(4), D, Omega, K, ('two declared decoupled oscillators',))
E = S.eye(4)[:, :2]
P = E.T
split = generate(separate, E, P, 'visible first oscillator; hidden second retained')
check('nonstationary-hidden-sector-retained', not zero(split.N*separate.D*split.N))
check('nonzero-hidden-energy-retained', not zero(split.N.T*separate.K*split.N))
check('hidden-can-change-total-energy-with-same-visible', P*S.Matrix([0,0,1,0]) == S.zeros(2,1)
      and (S.Matrix([0,0,1,0]).T*K*S.Matrix([0,0,1,0]))[0] == 2)
# Valid metric-conservative Hamiltonian whose coupled hidden direction
# prevents closed projected evolution.
B = S.zeros(4)
B[0,2], B[2,0] = 1, -1
coupled = state(S.eye(4), B, B, B.T*B, ('declared cross-sector rotation',))
refused('coupled-hidden-state-refused', lambda: generate(coupled,E,P,'hostile interface'),
        'hidden-to-visible dynamical obstruction')
v = S.Matrix([0,0,1,0])
check('same-projection-different-projected-derivative', P*v == S.zeros(2,1) and P*B*v != S.zeros(2,1))
refused('coordinate-deletion-is-not-Gram-projection',
        lambda: generate(source,prior['E'],prior['E'].T,'wrong projection'), 'metric adjoint projection')
refused('unprovenanced-interface-refused', lambda: generate(source,prior['E'],P4,''), 'interface provenance')
refused('broken-Hamiltonian-refused', lambda: generate(
        state(source.G,source.D,source.Omega,source.K+S.eye(12),source.provenance),
        prior['E'],P4,'hostile Hessian'), 'Hamiltonian equation')
# A stationary flow descends, but its mixed form need not define the required
# split Hamiltonian structure. This restricted WG refuses that weaker input.
mixed_form = state(S.eye(4), S.zeros(4), B, S.zeros(4), ('declared mixed form',))
refused('flow-agreement-does-not-certify-form-split',
        lambda: generate(mixed_form,E,P,'mixed form hostile'), 'mixed symplectic-form obstruction')
check('retained-metric-budget', zero(source.G-P4.T*direct.target.G*P4-direct.N.T*source.G*direct.N))
for power in range(7):
    check(f'flow-series-coefficient/{power}', zero(P4*source.D**power-direct.target.D**power*P4))

result = {
    'schema':'marici.strominger.hamiltonian-descent-wg.v1', 'status':'pass',
    'checks':checks, 'source':'existing fixed-Gram rotor lift from D4; not independently selected H12',
    'direct_projection':'existing metric-adjoint P12,4',
    'schedules':[[12,11,10,9,8,7,6,5,4],[12,10,8,7,6,5,4]],
    'six_step_schedule_status':'declared block grouping, not native rung or Postnikov identification',
    'witness_identities':direct.identities,
    'continuous_flow':'P exp(t D_source)=exp(t D_target) P for all real t, from exact finite-dimensional generator equality',
    'retained_source_and_hidden_sector':True,
    'physical_admission':False, 'native_T9_identification':False, 'Postnikov_tower_constructed':False,
    'scope':'restricted quadratic real Hamiltonian WG on supplied reducing interfaces; no universal existence or canonical interface selection',
    'input_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (Path(__file__),HERE/'hamiltonian_descent_wg.py',PRIOR)}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} Hamiltonian-descent WG checks; prior45-check bridge freshly rerun')
print('Exact continuous descent on a declared fixed-Gram source; coupled hidden dynamics rejected.')
print('Six steps are a chosen grouping, not a Postnikov/native rung derivation or physical Hamiltonian selection.')
