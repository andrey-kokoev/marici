"""Same retained interaction in four lossless presentations.

Reuses the original three witness foci. The view payload is enlarged to the
whole interaction state/history; the old Packet-only view is NOT silently
asserted to contain state. This is an exact Python fixture, not an Agda
instantiation of physical mechanics or a native choice of execution policy.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
from check_retained_interaction_pipeline import (
    State, Event, advance, valid_event, valid_history, initial, c, packet, ZERO)
from check_three_witness_retained_cone import Packet, Comparison, View, focus, validate

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Whole:
    witness: Packet
    state: State
    duration: F
    events: tuple = ()


@dataclass(frozen=True)
class Presentation:
    slot: int
    whole: Whole


def encode(slot, whole):
    if slot not in range(4):
        raise ValueError('four declared presentations only')
    return Presentation(slot, whole)


def decode(v):
    return v.whole


def observed_focus(v):
    # Reuse, rather than relabel, the actual prior comparison foci.
    return focus(View(v.slot, v.whole.witness))


def transport(v, slot):
    return encode(slot, decode(v))


def valid_whole(w):
    return (validate(w.witness) and w.duration > 0 and valid_history(w.events)
            and (not w.events or w.events[-1].after == w.state))


def evolve(w):
    if not valid_whole(w):
        raise ValueError('invalid retained whole or broken attachment')
    event = replace(advance(w.state, w.witness.context, w.duration), witness=w.witness)
    if not valid_event(event):
        raise ValueError('invalid interaction')
    return replace(w, state=event.after, events=w.events+(event,))


def evolve_view(v):
    return encode(v.slot, evolve(decode(v)))


def act(w, count):
    for _ in range(count):
        w = evolve(w)
    return w


checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


w = Whole(packet(c), initial, F(1))
for i, j in product(range(4), repeat=2):
    vi = encode(i, w)
    check(f'view-inverse/{i}/{j}', transport(transport(vi, j), i) == vi)
    check(f'interaction-square/{i}/{j}',
          transport(evolve_view(vi), j) == evolve_view(transport(vi, j)))
    # Equality is of the WHOLE record, so includes both positions, momenta,
    # supply balance, duration, full witness routes and event attachments.
    check(f'full-state-readout/{i}/{j}',
          decode(transport(evolve_view(vi), j)) == evolve(w))
    for k in range(4):
        check(f'transport-composition/{i}/{j}/{k}',
              transport(transport(vi, j), k) == transport(vi, k))

for a, b in product(range(3), repeat=2):
    check(f'physical-action-composition/{a}/{b}', act(w, a+b) == act(act(w, a), b))

for i in range(4):
    result = decode(evolve_view(encode(i, w)))
    check(f'original-focus-reused/{i}', observed_focus(encode(i, w)) == focus(View(i, w.witness)))
    check(f'original-witness-history-retained/{i}', result.events[0].witness == w.witness)
    check(f'work-and-positions-retained/{i}', result.state.supply == 90
          and result.state.x1 == (F(-1), F(-2), F(1))
          and result.state.x2 == (F(2, 3), F(4, 3), F(-2, 3)))

# Same selected witness, different source preparation: a focus-only quotient
# cannot predict the position response, even when that comparison is valid.
shifted = replace(w, state=replace(initial, p1=(F(1), F(0), F(0))))
check('focus-only-not-closed', observed_focus(encode(1, w)) == observed_focus(encode(1, shifted))
      and evolve(w).state.x1 != evolve(shifted).state.x1)

# Equal physical responses must not collapse distinct comparison histories.
alternate = replace(w, witness=replace(w.witness,
                    bc=Comparison(('B',), ('C', 'identity'))))
check('equal-effect-history-distinction', valid_whole(alternate)
      and evolve(alternate).state == evolve(w).state
      and evolve(alternate).events != evolve(w).events)

# A tempting bad transport modifies only the target's duration. It keeps
# the triangle intact but no longer intertwines the interaction's positions.
def bad_transport(v, slot):
    return encode(slot, replace(decode(v), duration=2*decode(v).duration))

bad_left = bad_transport(evolve_view(encode(0, w)), 1)
bad_right = evolve_view(bad_transport(encode(0, w), 1))
check('duration-changing-adapter-rejected', bad_left != bad_right
      and bad_left.whole.state.x1 != bad_right.whole.state.x1)
check('duration-hostile-invisible-to-momentum', bad_left.whole.state.p1 == bad_right.whole.state.p1)

# Cone encoding does not add executions. These are Python presentation
# changes, not the actual Agda cone constructor; the formal theorem below
# separately establishes that property for actual Tick/cone histories.
check('presentation-change-adds-no-event', len(transport(encode(0, evolve(w)), 3).whole.events) == 1)

proof_path = ROOT/'results/agda-RetainedTickStateAction.json'
proof = json.loads(proof_path.read_text(encoding='utf-8-sig'))
formal_path = ROOT/'agda/RetainedTickStateAction.agda'
check('fresh-formal-action-receipt', proof['passed'] and proof['ignore_interfaces']
      and proof['inputs_stable_during_check']
      and proof['source_sha256'] == hashlib.sha256(formal_path.read_bytes()).hexdigest())

out = {
    'schema': 'marici.nima.interaction-presentation-squares.v1', 'status': 'pass', 'checks': checks,
    'square': 'transport after interaction = transported interaction after transport',
    'construction': 'conjugation through declared lossless views of the entire interaction whole',
    'retained': ['actual comparison packet and foci', 'positions', 'momenta', 'supply balance',
                 'supplied drift duration', 'complete event histories'],
    'hostiles': ['selected witness alone loses predictive state',
                 'equal effects must not erase distinct routes',
                 'duration-changing adapter breaks position covariance while momentum agrees'],
    'formal': 'generic actual-Tick action now proves lossless-view identity, composition, state squares and cone-encoding compatibility',
    'boundary': 'the physical model is not yet an Agda instantiation; execution policy, impulse kernel, masses, charges and duration remain supplied',
    'not_claimed': 'commutation of kick and drift; native excitation or coupling selection; physical time calibration',
    'formal_receipt_sha256': hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/interaction-presentation-squares.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(f'PASS: {len(checks)} presentation/action integration checks')
print('Same interaction commutes with lossless presentation transport, retaining positions and histories.')
print('Physical policy remains supplied; no kick/drift commutation or native control selection claimed.')
