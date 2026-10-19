"""Bounded interface tests; reuses sources, does not recheck WG Agda."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/strominger/checkers'))
import sympy as S
from energy_task_reduction import EnergyTaskState, gain_step, infer_components
from energy_target_controller import safe_probe, finish_after_probe

spec = importlib.util.spec_from_file_location('context_source', ROOT / 'research/sontag/checkers/contextual_capability_coalgebra.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def replay_context(initial, events):
    state = initial
    if state not in c.CONTEXTS:
        raise ValueError('unknown context')
    for event in events:
        if event not in c.CONTEXT_COMMANDS:
            raise ValueError('unknown event')
        state = c.advance(state, event)
    return state


def replay_gain(initial, events):
    state = initial
    for q in events:
        state = gain_step(state, q).result
    return state


def same_components(left, right):
    return all(S.simplify(a-b) == 0 for a, b in zip(
        (left.one_leg, left.two_leg), (right.one_leg, right.two_leg)))


initial = EnergyTaskState(S.Integer(3), S.Integer(5), 'interface fixture')
q, r = S.Rational(3, 4), S.Rational(2, 3)
sequential = replay_gain(initial, [q, r])
flattened = gain_step(initial, q*r).result
h = S.Integer(4)
probe = safe_probe(initial.energy, h)
after = gain_step(initial, probe).result.energy
inferred = infer_components(initial.energy, after, probe)
probed, final = finish_after_probe(initial.energy, after, probe, h, 'retained exact readings')
invalid_context = False
try:
    replay_context(('observer', 0), ['self-authorize'])
except ValueError:
    invalid_context = True
invalid_gain = False
try:
    gain_step(initial, S.Integer(2))
except ValueError:
    invalid_gain = True

checks = {
    'context_replay_append_square': all(
        replay_context(x, list(word)+[e]) == c.advance(replay_context(x, word), e)
        for x in c.CONTEXTS for word in c.words(2) for e in c.CONTEXT_COMMANDS),
    'context_observation_square': all(
        c.context_trace(x, word)[-1] == c.enabled_actions(replay_context(x, word))
        for x in c.CONTEXTS for word in c.words(2)),
    'context_invalid_event_rejected': invalid_context,
    'gain_append_and_composition_components': same_components(sequential, flattened),
    'distinct_provenance_retained': sequential.provenance != flattened.provenance,
    'gain_invalid_amplification_rejected': invalid_gain,
    'two_readings_identify_initial_components': all(S.simplify(a-b)==0 for a,b in zip(inferred,(3,5))),
    'probe_result_is_current_parent': final.parent == probed.result,
    'safe_probe_does_not_undershoot': bool(after >= h),
    'target_reached_from_updated_state': S.simplify(final.result.energy-h)==0,
    'H_only_hostile_preserved': gain_step(EnergyTaskState(S.Integer(8),S.Integer(0),'one'),S.Rational(1,2)).result.energy == 2
        and gain_step(EnergyTaskState(S.Integer(0),S.Integer(8),'two'),S.Rational(1,2)).result.energy == S.Rational(1,2),
    'immediate_capability_hostile_preserved': not c.transition_well_defined(0,0),
}
out = {'schema':'marici.sontag.typed-event-control-interface.v1',
       'scope':'bounded Python source interface checks; WG source maps cited, not freshly typechecked',
       'checks':{k:bool(v) for k,v in checks.items()}, 'passed':all(checks.values())}
path = ROOT / 'research/sontag/results/typed-event-control-interface-v1.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out,indent=2)+'\n', encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
