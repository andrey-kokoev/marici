"""Finite exact decision-fiber fixtures; no physical clock model."""
import json
from pathlib import Path

# Each tuple is (source, history, A reading, B reading, allowed actions).
# Source is shared across its history's observations, never independently joined.
worlds = (
    ('s0', 'h0', 0, 0, frozenset({'hold'})),
    ('s1', 'h1', 1, 1, frozenset({'hold'})),
)

def common(rows):
    # Empty evidence fibers are rejected, not treated as vacuous certificates.
    if not rows:
        return set()
    return set.intersection(*(set(row[4]) for row in rows))

assert common(worlds) == {'hold'}  # nonunique source, sufficient decision
assert not common(())
# Ground truth is one admitted source/history, not an independently drawn pair.
truth = worlds[0]
assert truth in worlds
# Forgetting the shared-history relation introduces inadmissible mixed states.
cartesian = tuple(('synthetic', 'unadmitted', a, b,
                   frozenset({'hold' if a == b else 'switch'}))
                  for a in {w[2] for w in worlds}
                  for b in {w[3] for w in worlds})
assert not common(cartesian)
# An A record from h0 and B record from h1 each pass marginal admission.
a_record, b_record = worlds[0][2], worlds[1][3]
assert any(w[2] == a_record for w in worlds)
assert any(w[3] == b_record for w in worlds)
joined = tuple(w for w in worlds if w[2] == a_record and w[3] == b_record)
assert not joined and not common(joined)
naive_action = 'hold' if a_record == b_record else 'switch'
assert naive_action == 'switch'  # invented joint state yields a false certificate

# A acts at deadline 1. B's distinguishing record arrives at A at time 2.
delayed = (
    ('s0', 'h0', 0, 0, frozenset({'hold'})),
    ('s1', 'h1', 0, 1, frozenset({'switch'})),
)

def transcript(w, time):
    return (w[2], w[3] if time >= 2 else None)

def fiber(actual, time):
    return tuple(w for w in delayed if transcript(w, time) == transcript(actual, time))

for actual in delayed:
    global_fiber = tuple(w for w in delayed if (w[2], w[3]) == (actual[2], actual[3]))
    assert common(global_fiber) == set(actual[4])
    assert not common(fiber(actual, 1))
    assert common(fiber(actual, 2)) == set(actual[4])
# Exhaust every deterministic action on the sole pre-deadline transcript.
assert all(any(action not in w[4] for w in delayed) for action in ('hold', 'switch'))
report = {
    'passed': True,
    'checks': {
        'nonunique_sources_allow_common_action': True,
        'empty_joint_fiber_rejected': True,
        'cartesian_relaxation_loses_decision_sufficiency': True,
        'mixed_history_packet_rejected_despite_marginal_admission': True,
        'global_evidence_sufficient_but_deadline_local_evidence_insufficient': True,
        'every_predeadline_deterministic_action_fails_some_admitted_history': True,
        'delivery_restores_local_decision_sufficiency': True,
    },
    'scope': 'Exact finite fixtures with explicit action tables and a stipulated delivery schedule. No claim of physical calibration, computational lower bounds, or necessity of periodic tact.',
}
path = Path(__file__).resolve().parents[1] / 'results/joint-history-decision-boundary.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
