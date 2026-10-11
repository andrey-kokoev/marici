"""Conditional end-to-end interaction harness, reusing today's real packet.

This is NOT a map from Agda square Ticks to physical interactions. It tests
what can already be assembled and keeps that missing attachment explicit.
Kick then free drift is a supplied split evolution, not a derived WG law.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as S
from check_charge_mass_recoil_triangle import add, sub, scale, impulse, energy
from check_three_witness_retained_cone import Context, Comparison, Packet, View, move, validate

ROOT = Path(__file__).resolve().parents[1]
ZERO = (F(0),)*3


@dataclass(frozen=True)
class State:
    x1: tuple
    x2: tuple
    p1: tuple
    p2: tuple
    supply: F  # bookkeeping balance, NOT a derived reservoir dynamics


@dataclass(frozen=True)
class Event:
    witness: Packet
    before: State
    after: State
    duration: F  # supplied drift duration; not a Tick-derived time
    work: F


def packet(c):
    if min(c.m1, c.m2) <= 0:
        raise ValueError("positive masses required")
    return Packet(c, Comparison(('A',), ('B',)),
                  Comparison(('B',), ('C',)), Comparison(('A',), ('C',)))


def kinetic(s, c):
    return energy(s.p1, c.m1)+energy(s.p2, c.m2)


def advance(s, c, duration):
    if duration <= 0:
        raise ValueError("positive supplied drift duration required")
    w = packet(c)
    j, k = impulse(c.q1, c.q2, c.kernel)
    p1, p2 = add(s.p1, j), add(s.p2, k)
    work = energy(p1, c.m1)+energy(p2, c.m2)-kinetic(s, c)
    after = State(add(s.x1, scale(duration/c.m1, p1)),
                  add(s.x2, scale(duration/c.m2, p2)),
                  p1, p2, s.supply-work)
    return Event(w, s, after, duration, work)


def valid_event(e):
    try:
        expected = advance(e.before, e.witness.context, e.duration)
        return validate(e.witness) and e == replace(expected, witness=e.witness)
    except ValueError:
        return False


def undo(e):
    # Reverse ORDER: inverse drift, then inverse kick. This is not a
    # second positive-duration forward event under the original policy.
    c, s = e.witness.context, e.after
    j, k = impulse(c.q1, c.q2, c.kernel)
    return State(sub(s.x1, scale(e.duration/c.m1, s.p1)),
                 sub(s.x2, scale(e.duration/c.m2, s.p2)),
                 sub(s.p1, j), sub(s.p2, k), s.supply+e.work)


def valid_history(events):
    return all(valid_event(e) for e in events) and all(
        a.after == b.before for a, b in zip(events, events[1:]))


checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


c = Context(F(1), F(-2), F(2), F(3), (F(1), F(2), F(-1)))
initial = State(ZERO, ZERO, ZERO, ZERO, F(100))
e = advance(initial, c, F(1))
check('actual-prior-triangle-valid', validate(e.witness))
check('actual-prior-work-ten', e.work == 10)
check('explicit-supply-debit', e.after.supply == 90)
check('event-validated', valid_event(e))

# Reuse today's actual witness views, without pretending that those views
# by themselves retain the added state trajectory. The outer Event must be
# carried as well; an attached view is (event, View(slot,event.witness)).
for slot in range(4):
    attached = (e, View(slot, e.witness))
    transported = (attached[0], move(attached[1], (slot+1) % 4))
    check(f'attached-view-packet/{slot}', transported[1].whole == transported[0].witness)
    check(f'attached-view-event-recovery/{slot}', transported[0] == e)

for q1, q2, tau in product(map(F, (-1, 0, 1)), map(F, (-2, 1)), (F(1, 2), F(1), F(2))):
    ctx = replace(c, q1=q1, q2=q2)
    s = replace(initial, p1=(F(1), F(-2), F(3)), p2=(F(-1), F(1), F(0)))
    event = advance(s, ctx, tau)
    j, k = impulse(q1, q2, ctx.kernel)
    name = f'{q1}/{q2}/{tau}'
    check('balanced-recoil/'+name, add(event.after.p1, event.after.p2) == add(s.p1, s.p2))
    check('inertia-readout/'+name,
          scale(1/ctx.m1, sub(event.after.p1, s.p1)) == scale(1/ctx.m1, j)
          and scale(1/ctx.m2, sub(event.after.p2, s.p2)) == scale(1/ctx.m2, k))
    check('supplied-work-budget/'+name,
          kinetic(event.after, ctx)+event.after.supply == kinetic(s, ctx)+s.supply)
    check('inverse-recovers-whole-state/'+name, undo(event) == s)

# Source-independent canonical verification of the declared physical model.
# Q here means positions, not the earlier Clifford observable.
x = S.Matrix(S.symbols('x0:6'))
p = S.Matrix(S.symbols('p0:6'))
m1, m2, tau = S.symbols('m1 m2 tau', positive=True)
charge = S.symbols('charge', real=True)
g = S.Matrix(S.symbols('g0:3'))
Minv = S.diag(*([1/m1]*3+[1/m2]*3))
j = charge*g.col_join(-g)
Hkick = -charge*(g.T*(x[:3, :]-x[3:, :]))[0]
Hfree = (p.T*Minv*p)[0]/2
check('kick-from-declared-interaction-Hamiltonian', -S.Matrix([S.diff(Hkick, v) for v in x]) == j)
check('drift-from-declared-kinetic-Hamiltonian', S.Matrix([S.diff(Hfree, v) for v in p]) == Minv*p)
y = (x+tau*Minv*(p+j)).col_join(p+j)
Jac = y.jacobian(x.col_join(p))
Omega = S.zeros(6).row_join(S.eye(6)).col_join((-S.eye(6)).row_join(S.zeros(6)))
check('full-split-map-symplectic', S.simplify(Jac.T*Omega*Jac-Omega) == S.zeros(12))

second = advance(e.after, c, F(1))
history = (e, second)
check('composable-history', valid_history(history))
check('broken-source-target-attachment-rejected', not valid_history((e, e)))
check('wrong-supply-rejected', not valid_event(replace(e, after=replace(e.after, supply=F(100)))))
check('wrong-state-rejected', not valid_event(replace(e, after=replace(e.after, p2=ZERO))))
check('false-triangle-rejected', not valid_event(replace(e, witness=replace(e.witness,
      bc=Comparison(('B',), ('C', 'unit-x'))))))

alternate = replace(e, witness=replace(e.witness,
                    bc=Comparison(('B',), ('C', 'identity'))))
check('distinct-valid-comparison-history-retained', valid_event(alternate)
      and alternate != e and alternate.after == e.after)

# Concrete information-loss controls. These are NOT proofs about all WG
# histories; they test this admitted, externally driven interaction model.
slow = advance(initial, c, F(2))
check('packet-alone-does-not-determine-duration', e.witness == slow.witness and e.duration != slow.duration)
check('packet-alone-does-not-determine-position', e.witness == slow.witness and e.after.x1 != slow.after.x1)
check('same-event-count-different-elapsed-time', len((e,)) == len((slow,)) and e.duration != slow.duration)
neutral = advance(initial, replace(c, q1=F(0)), F(1))
check('endpoint-alone-does-not-count-events', neutral.before == neutral.after and len(()) != len((neutral,)))
check('nonzero-kick-is-not-Bool-involution', add(e.after.p1, impulse(c.q1, c.q2, c.kernel)[0]) != initial.p1)
# Event-count concatenation is elementary list accounting. No square Tick
# is constructed here, so it must not be called the proven square clock.
check('external-event-count-additive', len(history) == len((e,))+len((second,)))

inputs = ['checkers/check_charge_mass_recoil_triangle.py',
          'checkers/check_three_witness_retained_cone.py',
          'agda/RetainedSquareConeClock.agda',
          'checkers/check_retained_interaction_pipeline.py']
result = {
    'schema': 'marici.nima.retained-interaction-pipeline.v1',
    'status': 'pass', 'checks': checks,
    'assembled': ['actual charge-mass-recoil Packet and validator',
                  'lossless event attachment to existing witness views',
                  'externally supplied canonical kick then free drift',
                  'recoil, inverse, composable histories and work bookkeeping'],
    'work_fixture': {'kinetic_gain': '10', 'supply_debit': '10'},
    'clock_attachment': 'NOT CONSTRUCTED: no map from actual Agda square-return records to these state-changing events',
    'clock_control': 'identical comparison packet and one event admit different supplied drift durations and positions',
    'supply_scope': 'balance bookkeeping only; no autonomous reservoir dynamics or positivity guarantee for arbitrary histories',
    'physical_scope': 'supplied classical impulse/drift model; not a WG charge law, mass derivation, native excitation or physical clock',
    'next_obligation': 'construct a source-supported action of retained histories on an interaction-state fiber, preserving witness attachments and specifying duration/control data',
    'input_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
}
(ROOT/'results/retained-interaction-pipeline.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'PASS: {len(checks)} exact/symbolic retained-interaction integration checks')
print('Original physical comparison packet reused; recoil, canonical update and supplied-work budget agree.')
print('OPEN: actual square-Tick attachment, source-generated controls, and physical duration.')
