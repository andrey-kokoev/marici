"""Subjective cost/likelihood model and bounded Bayesian closure policy; no proof outcomes."""
from collections import Counter
from itertools import product
from pathlib import Path
import copy
import json
import sys

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'research/conjecture_net'))
from bayesian_outcome_planner import Planner, action_metrics, condition, marginal
from outcome_reference import file_hash, load, require

MODEL = 'research/nima/contracts/completion-refinement-planning.v1.json'
NET = 'research/nima/contracts/completion-refinement-conjecture-net.v1.json'
OUT = 'research/nima/results/completion-refinement-planning.json'


def build_worlds(model):
    c, j = model['claims'], model['joint_model']
    fields = ['pi_true', 'all_scale_regularity_true', 'pi_scale_regularity_given_all_scale_failure',
              'target_true_given_half_turn_true', 'target_true_given_half_turn_false']
    require(all(0 <= j[k] <= 1 for k in fields), 'invalid joint parameter')
    merged = {}
    for pi, regular, at_pi, target in product((False, True), repeat=4):
        ep = 1. if regular else j['pi_scale_regularity_given_all_scale_failure']
        half = pi and at_pi
        tp = j['target_true_given_half_turn_true' if half else 'target_true_given_half_turn_false']
        weight = (j['pi_true'] if pi else 1-j['pi_true']) * (j['all_scale_regularity_true'] if regular else 1-j['all_scale_regularity_true'])
        weight *= (ep if at_pi else 1-ep) * (tp if target else 1-tp)
        if weight <= 0:
            continue
        truth = {c['pi']: pi, c['regularity']: regular, c['flow']: regular, c['half_turn']: half, c['target']: target}
        key = tuple(sorted(truth.items()))
        merged[key] = merged.get(key, 0.) + weight
    worlds = [{'id': f'w{i}', 'probability': p, 'truth': dict(t)} for i, (t, p) in enumerate(sorted(merged.items()))]
    require(abs(sum(w['probability'] for w in worlds)-1) < 1e-12, 'joint model not normalized')
    require(all(w['truth'][c['flow']] == w['truth'][c['regularity']] for w in worlds), 'flow alias inconsistent')
    require(all(not (w['truth'][c['pi']] and w['truth'][c['flow']]) or w['truth'][c['half_turn']] for w in worlds), 'same-phase conjunction violated')
    require(any(w['truth'][c['target']] and not w['truth'][c['half_turn']] for w in worlds), 'alternative implementation route was erased')
    return worlds


def build_actions(model, net, worlds):
    nodes = {n['id']: n for n in net['conjectures']}
    historical = set(model.get('resolved_estimates_retained', []))
    require(all(nodes[c]['outcome'] in ('++', '-+') for c in historical), 'historical estimate is not resolved')
    estimates = {c: e for c, e in model['estimates'].items() if c not in historical}
    require(set(estimates) == {n['id'] for n in nodes.values() if n['outcome'] not in ('++', '-+')}, 'estimates do not cover exactly the unresolved nodes')
    actions = []
    for claim, e in estimates.items():
        for intent in ('prove', 'reject'):
            cost = e[intent + '_cost']
            low, high = e[intent + '_cost_range']
            require(0 < low <= cost <= high, 'invalid effort range')
            sensitivity = e['prove_success_given_true' if intent == 'prove' else 'reject_success_given_false']
            require(0 <= sensitivity <= 1, 'invalid sensitivity')
            require(nodes[claim]['cost_to_' + ('prove' if intent == 'prove' else 'reject')] == cost, 'net/model cost mismatch')
            alias = e.get('rejection_alias') if intent == 'reject' else None
            if alias:
                require(alias in model['estimates'] and all(w['truth'][claim] == w['truth'][alias] for w in worlds), 'invalid rejection alias')
                require(cost == model['estimates'][alias]['reject_cost'] and sensitivity == model['estimates'][alias]['reject_success_given_false'], 'alias costs/likelihood differ')
                continue
            actions.append({'id': intent + '/' + claim, 'claim': claim, 'intent': intent, 'cost': cost,
                            'sensitivity': sensitivity, 'requires': nodes[claim]['depends_on'] if intent == 'prove' else []})
    return actions


def analyze(model, net, structure, include_sensitivity=True):
    require(model['estimate_status'] == 'subjective_uncalibrated_planning_only', 'planning estimates must be labeled')
    require(model['objective']['target'] == net['objective']['target'], 'wrong closure target')
    worlds = build_worlds(model)
    known = {k for k, v in structure['imports'].items() if v['outcome'] == '++'} | set(structure['locally_proved_claims'])
    require(known == set(model['required_known_proofs']), 'proof context changed: re-estimate the portfolio explicitly')
    observations = {c: True for c in known if c in model['claims'].values()}
    worlds = condition(worlds, observations) if observations else worlds
    actions = build_actions(model, net, worlds)
    target = model['objective']['target']
    budget = model['objective']['budget_effort_units']
    if target in known:
        require(structure['terminal'] and structure['target_outcome'] == '++' and not actions,
                'terminal planning requires an admitted target and empty portfolio')
        return {
            'schema': 'marici.nima.completion-refinement-planning-result.v1', 'status': 'pass',
            'planning_only': True, 'scientific_outcomes_changed': False,
            'estimate_status': model['estimate_status'], 'objective': model['objective'],
            'central': {'first_action': None, 'success_probability': 1.0, 'expected_total_effort': 0.0,
                        'budget': budget, 'success_branch_trace': [], 'states_evaluated': 0},
            'rows': [], 'joint_worlds': worlds, 'continuation_action': None,
            'forecast_scope': 'Terminal admitted positive certificate at its recorded mixed verification level; no remaining proof action or budget forecast.',
            'paused_attempts': [], 'canonical_action_count': 0, 'known_proof_certificates': sorted(known),
            'information_diagnostic': [],
            'sensitivity': {'scenario_count': 0, 'first_action_counts': {}, 'recommendation_stable': True, 'scenarios': []},
            'boundary': 'Terminal observation comes from theorem-specific admission, not planner probability or kernel semantic interpretation.',
        }
    central = Planner(worlds, actions, target, known, budget).solve()
    active = list(structure.get('in_progress', {}).values())
    require(len(active) <= 1, 'multiple active attempts require an explicit continuation policy')
    paused_ready = [p for c, p in structure.get('paused', {}).items() if c in structure['ready_proof_frontier']]
    continuation = ('continue/' + active[0]['active_action'] if active else
                    'resume/' + paused_ready[0]['active_action'] if len(paused_ready) == 1 else None)
    forecast_scope = ('Original pre-attempt portfolio estimates; the active attempt is unfinished. '
                      'Paused checkpoints are retained; operator branch selection does not reset their budgets. '
                      'No terminal observation, independent retry, or remaining-effort re-estimate is asserted.'
                      if active else 'Conditioned on the operator-accepted pi certificate. Original costs and 24-EU scenario are retained, not a measured remaining budget or a reset of the paused regularity attempt. Resume its existing derivative checkpoint; no independent retry is inferred.')
    if active and model['claims']['pi'] in known:
        forecast_scope = ('Conditioned on the operator-accepted pi certificate. Continue the same resumed regularity attempt at its origin derivative bound. '
                          'Original costs and 24-EU scenario are retained, not a measured remaining budget or an independent retry. '
                          'The new kernel origin reduction is a component, not full derivative closure.')
    if model['claims']['regularity'] in known:
        forecast_scope = ('Conditioned on accepted pi and fresh kernel regularity closure. Remaining work is certificate assembly. '
                          'Original costs and 24-EU scenario are retained, not a measured remaining budget or an independent retry; '
                          'resolved analytic actions are omitted and no completed attempt is reset.')
    rows, ready_information = [], []
    proofs = {a['claim']: a for a in actions if a['intent'] == 'prove'}
    def proof_ancestors(claim):
        if claim in known:
            return set()
        return {claim} | set().union(*(proof_ancestors(d) for d in proofs[claim]['requires']))
    for claim, e in model['estimates'].items():
        if claim in known:
            continue
        row = {'claim': claim, 'subjective_probability_true': marginal(worlds, claim),
               'proof_route_effort_if_all_successful': sum(proofs[d]['cost'] for d in proof_ancestors(claim))}
        for intent in ('prove', 'reject'):
            canonical = e.get('rejection_alias', claim) if intent == 'reject' else claim
            if canonical in known:
                row[intent] = {'available': False, 'canonical_action': intent + '/' + canonical,
                               'reason': 'The aliased analytic claim is already proved; no rejection retry is scheduled.'}
                continue
            action = next(a for a in actions if a['id'] == intent + '/' + canonical)
            prerequisites = {d: True for d in action['requires'] if d not in known}
            context = condition(worlds, prerequisites) if prerequisites else worlds
            metrics = action_metrics(context, action, target)
            ready = set(action['requires']) <= known
            row[intent] = dict(metrics, cost=action['cost'], cost_range=e[intent + '_cost_range'],
                               canonical_action=action['id'], ready_now=ready,
                               context='current state' if ready else 'conditional on prerequisite proof certificates',
                               prerequisite_certificates=action['requires'],
                               use=e['proof_use' if intent == 'prove' else 'rejection_use'])
            if ready and canonical == claim:
                ready_information.append({'action': action['id'], 'target_information_per_effort': metrics['target_information_per_effort'],
                                          'claim_information_per_effort': metrics['claim_information_per_effort']})
        rows.append(row)
    scenarios = []
    if include_sensitivity:
        c = model['claims']
        s = model['sensitivity']
        for pc, rc, (ps, rs) in product(s['pi_proof_costs'], s['regularity_proof_costs'], s['likelihood_pairs']):
            changed = copy.deepcopy(actions)
            for a in changed:
                if a['id'] == 'prove/' + c['pi']:
                    a.update(cost=pc, sensitivity=ps)
                if a['id'] == 'prove/' + c['regularity']:
                    a.update(cost=rc, sensitivity=rs)
            result = Planner(worlds, changed, target, known, budget).solve()
            scenarios.append(dict(result, pi_proof_cost=pc, regularity_proof_cost=rc,
                                  pi_sensitivity=ps, regularity_sensitivity=rs))
    counts = Counter(s['first_action'] or 'no-positive-route-within-budget' for s in scenarios)
    return {
        'schema': 'marici.nima.completion-refinement-planning-result.v1', 'status': 'pass',
        'planning_only': True, 'scientific_outcomes_changed': False,
        'estimate_status': model['estimate_status'], 'objective': model['objective'],
        'central': central, 'rows': rows, 'joint_worlds': worlds,
        'continuation_action': continuation, 'forecast_scope': forecast_scope,
        'paused_attempts': sorted(structure.get('paused', {})),
        'canonical_action_count': len(actions), 'known_proof_certificates': sorted(known),
        'information_diagnostic': sorted(ready_information, key=lambda r: (-r['target_information_per_effort'], r['action'])),
        'sensitivity': {'scenario_count': len(scenarios), 'first_action_counts': dict(counts),
                        'recommendation_stable': bool(scenarios) and all(s['first_action'] == central['first_action'] for s in scenarios),
                        'scenarios': scenarios},
        'boundary': 'Model-optimal finite one-shot policy, not a calibrated or global optimum. After any real observation, record and replan; no actions are executed by this checker.',
    }


def main():
    from check_completion_refinement_net import validate
    net, model = load(REPO, NET), load(REPO, MODEL)
    structure = validate(REPO, net)
    result = analyze(model, net, structure)
    pins = dict(structure['source_sha256'])
    for path in (MODEL, NET, 'research/conjecture_net/bayesian_outcome_planner.py',
                 'research/nima/checkers/check_completion_refinement_planning.py',
                 'research/nima/checkers/check_completion_refinement_net.py'):
        pins[path] = file_hash(REPO, path)
    result['source_sha256'] = pins
    result['external_dependency_sha256'] = structure['external_dependency_sha256']
    (REPO / OUT).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'central': result['central'],
                      'sensitivity_first_actions': result['sensitivity']['first_action_counts']}, indent=2))

if __name__ == '__main__':
    main()
