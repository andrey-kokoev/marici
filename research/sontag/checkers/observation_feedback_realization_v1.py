"""Exact event trace using existing energy controller; no physical binding."""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/strominger/checkers'))
import sympy as S
from energy_task_reduction import EnergyTaskState, gain_step, infer_components
from energy_target_controller import safe_probe, target_gain


def total_only_policy(total, target):
    """Decision uses only the two public scalar inputs."""
    total, target = map(S.sympify, (total, target))
    if total.is_nonnegative is not True or target.is_nonnegative is not True or (total-target).is_nonnegative is not True:
        raise ValueError('invalid exact target/readout')
    if total == target:
        return 'direct', S.Integer(1)
    if target == 0:
        return 'direct', S.Integer(0)
    return 'probe', safe_probe(total, target)


def run_trace(initial, target):
    target = S.sympify(target)
    gain_step(initial, S.Integer(1))  # validate source state
    total = initial.energy
    mode, q = total_only_policy(total, target)
    events = [{'role':'observation', 'event':'read-total', 'value':str(total)},
              {'role':'control', 'event':'gain', 'q':str(q),
               'information':{'total':str(total),'target':str(target)}}]
    first = gain_step(initial, q)
    if mode == 'direct':
        final = first
    else:
        after = first.result.energy
        events.append({'role':'observation','event':'read-total','value':str(after)})
        a, b = infer_components(total, after, q)
        inferred_initial = EnergyTaskState(a,b,'retained exact readout transcript')
        inferred_current = gain_step(inferred_initial,q).result
        feedback = target_gain(inferred_current,target)
        events.append({'role':'control','event':'gain','q':str(feedback),
                       'information':{'initial_total':str(total),'after_total':str(after),
                                      'probe':str(q),'target':str(target)},
                       'inferred_current':[str(inferred_current.one_leg),str(inferred_current.two_leg)]})
        final = gain_step(first.result,feedback)
    events.append({'role':'observation','event':'read-total','value':str(final.result.energy)})
    return events, first, final


fixtures = []
checks = {}
for a,b in ((0,0),(0,8),(8,0),(3,5)):
    state = EnergyTaskState(S.Integer(a),S.Integer(b),'source fixture')
    for ratio in (S.Integer(0),S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Integer(1)):
        target = ratio*state.energy
        events, first, final = run_trace(state,target)
        fixtures.append({'initial':[a,b],'target':str(target),'events':events})
        checks[f'target_{a}_{b}_{ratio}'] = S.simplify(final.result.energy-target)==0
        checks[f'energy_monotone_{a}_{b}_{ratio}'] = bool(state.energy >= first.result.energy >= final.result.energy)
        if 0 < target < state.energy:
            checks[f'updated_parent_{a}_{b}_{ratio}'] = final.parent == first.result
# Same initial reading implies same first decision despite hidden components.
left = EnergyTaskState(S.Integer(8),S.Integer(0),'left')
right = EnergyTaskState(S.Integer(0),S.Integer(8),'right')
L,_,_ = run_trace(left,4)
R,_,_ = run_trace(right,4)
checks['first_decision_uses_only_public_total'] = L[1] == R[1]
checks['after_reading_distinguishes_hidden_components'] = L[2]['value'] != R[2]['value']
checks['feedback_adapts_to_after_reading'] = L[3]['q'] != R[3]['q']
rejected = 0
for h in (-1,9):
    try:
        total_only_policy(8,h)
    except ValueError:
        rejected += 1
checks['invalid_targets_rejected'] = rejected == 2
blind = gain_step(left,S.Rational(1,2))
try:
    target_gain(blind.result,S.Integer(4))
    checks['blind_undershoot_not_reset'] = False
except ValueError:
    checks['blind_undershoot_not_reset'] = True
out = {'schema':'marici.sontag.observation-feedback-realization.v1',
       'scope':'declared exact energy model; total-only information policy; no physical reader or actuator',
       'checks':{k:bool(v) for k,v in checks.items()},'passed':all(checks.values()),
       'fixture_count':len(fixtures),'traces':fixtures}
p = ROOT / 'research/sontag/results/observation-feedback-realization-v1.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'fixtures':len(fixtures)},indent=2))
raise SystemExit(0 if out['passed'] else 1)
