"""Distinguish lifted rotor closure, reduced action, full action and clock.

Uses the completed module-compatible phase lift, not its C=0 predecessor.
Exit zero verifies a counterexample to periodicity-implies-area-quantization.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import sympy as S
import check_retained_rotor_phase_transport as phase
import check_clock_calibration as calibration

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'results/rotor-period-action-boundary.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    model = phase.main()
    calibration.main()
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def clean(expr):
    return S.simplify(S.trigsimp(S.expand_trig(expr)))


def integral(expr):
    return S.simplify(S.integrate(S.expand_trig(expr), (theta, 0, 2*S.pi)))


k, theta = model['kappa'], model['theta']
s0, u, v, z0, phi0 = S.symbols('s0 q0 p0 z0 phi0', real=True)
initial = S.Matrix([s0, u, v, z0])
target, phi = model['lift'](theta, 0, initial, phi0)
check('whole-algebra-state-retained', target[0] == s0 and target[3] == z0)
check('same-angular-flow', clean(S.diff(target[1], theta)-2*target[2]) == 0
      and clean(S.diff(target[2], theta)+2*target[1]) == 0)
H = clean(model['contact_H'].subs(dict(zip(model['x'], target)), simultaneous=True))
check('completed-module-constant-kept', H == u*u+v*v+k)
beta_dot = clean(model['beta'](target).dot(S.diff(target, theta)))
alpha_dot = clean(S.diff(phi, theta)-beta_dot/k)
Fdelta = clean(model['F'](target)-model['F'](initial))
clock = model['F'](target)/k-phi
check('correct-angular-clock', clean(S.diff(clock, theta)) == 1)
check('connection-is-not-clock-differential', alpha_dot == -(u*u+v*v+k)/k)
check('missing-primitive-term', clean(beta_dot-S.diff(Fdelta, theta)) == u*u+v*v)

reduced = integral(beta_dot)
complete = integral(beta_dot-H)
connection = integral(alpha_dot)
delta_phi = clean((phi-phi0).subs(theta, 2*S.pi))
delta_F = clean(Fdelta.subs(theta, 2*S.pi))
check('lift-and-base-return', model['U'](2*S.pi) == S.eye(2)
      and target.subs(theta, 2*S.pi) == initial)
check('phase-circle-closes', delta_phi == -2*S.pi and S.exp(S.I*delta_phi) == 1)
check('unwrapped-clock-retains-cycle', clean((clock-clock.subs(theta, 0)).subs(theta, 2*S.pi)) == 2*S.pi)
check('reduced-action-family', reduced == 2*S.pi*(u*u+v*v))
check('complete-action-family', complete == -2*S.pi*k)
check('complete-action-phase-matches-module', S.simplify(S.exp(S.I*complete/k)) == 1)
check('dynamical-connection-integral', connection == -2*S.pi*(u*u+v*v+k)/k)
missing = S.simplify(connection-(delta_phi-delta_F/k))
check('overview-dropped-term', S.simplify(missing+reduced/k) == 0)
# The half-turn sign is retained too; the test never repairs the model by
# discarding its -1 or double-counting the already selected phase correction.
check('half-turn-sign-retained', model['U'](S.pi) == -S.eye(2)
      and clean((phi-phi0).subs(theta, S.pi)) == -S.pi)

sigma = S.symbols('sigma', positive=True)
family = {u: S.sqrt(k*sigma), v: 0}
check('continuous-off-lattice-freedom', S.simplify(reduced.subs(family)/(2*S.pi*k)) == sigma)
example = {u: S.sqrt(k/2), v: 0}
I0 = S.simplify(reduced.subs(example))
S0 = S.simplify(complete.subs(example))
A0 = S.simplify(connection.subs(example))
check('nonzero-admitted-counterexample', I0 == S.pi*k and H.subs(example) == 3*k/2)
check('not-two-pi-lattice', S.simplify(I0/(2*S.pi*k)) == S.Rational(1, 2))
check('not-four-pi-lattice', S.simplify(I0/(4*S.pi*k)) == S.Rational(1, 4))
check('same-complete-phase-closure-off-lattice', S.simplify(S.exp(S.I*S0/k)) == 1)
check('wrong-clock-connection-equality-rejected', A0 == -3*S.pi
      and delta_phi-delta_F/k == -2*S.pi)

# A horizontal lift along the SAME base loop is a different protocol. Its
# phase increment is integral(beta)/k and it need not close in the phase fiber.
horizontal_phase = S.simplify(I0/k)
check('horizontal-lift-not-closed-in-counterexample', S.exp(S.I*horizontal_phase) == -1)
check('actual-rotor-is-not-horizontal', alpha_dot.subs(example) == -S.Rational(3, 2))
check('omitting-dynamical-term-changes-return', S.exp(S.I*horizontal_phase) != S.exp(S.I*delta_phi))
refused = False
try:
    check('deliberately-false-claim', False)
except AssertionError:
    refused = True
check('failure-gate-refuses', refused)

files = [Path(__file__), Path(phase.__file__), Path(calibration.__file__), Path(phase.source.__file__)]
result = {
    'schema': 'marici.nima.rotor-period-action-boundary.v1', 'status': 'pass',
    'scientific_disposition': 'lifted-period-does-not-imply-reduced-action-lattice',
    'source': 'completed defining-module phase transport with H=q^2+p^2+kappa',
    'parameter': 'theta, dimensionless; phase circle period 2*pi; adjoint angle 2*theta',
    'full_lift_period': '2*pi in theta, 4*pi in adjoint angle',
    'reduced_action': str(reduced), 'complete_action': str(complete),
    'connection_integral': str(connection), 'omitted_term': str(missing),
    'counterexample': {
        'radius_squared': 'kappa/2', 'reduced_action': str(I0),
        'complete_action': str(S0), 'actual_connection_integral': str(A0),
        'claimed_connection_integral': str(delta_phi-delta_F/k),
        'dynamical_phase': '1', 'horizontal_phase': '-1',
        'two_pi_lattice_ratio': '1/2', 'four_pi_lattice_ratio': '1/4',
    },
    'conditional_horizontal_closure': 'For alpha=0, additional phase-fiber closure requires integral(beta) in 2*pi*kappa*Z; not imposed on dynamical rotor paths.',
    'scope': 'declared real Clifford phase realization; not a universal quantization no-go, physical clock, Planck constant or quantum theory derivation',
    'checks': checks, 'check_count': len(checks),
    'source_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
}
OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print('PASS: closed full lift with reduced action pi*kappa, outside both proposed lattices')
print('Complete action -2*pi*kappa; connection integral -3*pi, not -2*pi')
