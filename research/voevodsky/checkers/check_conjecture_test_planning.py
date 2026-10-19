"""Validate probability/cost annotations without promoting estimates to evidence."""
import argparse
import copy
import json
import math
from hashlib import sha256
from pathlib import Path
from check_math_rh_port_connections import PATHS, ROOT

MODEL = 'research/conjecture_net/contracts/conjecture-test-planning.v10.json'
RESULT = 'research/voevodsky/results/conjecture-test-planning-v1.json'
OUTCOMES = ['accepted', 'rejected', 'inconclusive']


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def initial(nets, paths=None):
    paths = PATHS if paths is None else paths
    records = []
    for alias, net in nets.items():
        for n in net['conjectures']:
            settled = n['status'] == 'resolved'
            records.append({
                'id': alias + ':' + n['id'],
                'test': {'acceptance': n['acceptance'], 'falsifier': n['falsifier'],
                         'next_action': n.get('next_action', 'Review the acceptance and falsifier under the declared scope.'),
                         'scope': n.get('scope', n['statement']),
                         'protocol_status': 'requires_estimation_protocol'},
                'probability': {
                    'status': 'not_applicable' if settled else 'unknown',
                    'event': 'Outcome of the next scoped test/review, not universal conjecture truth.',
                    'outcomes': OUTCOMES, 'values': None, 'conditioning': None,
                    'uncertainty': None, 'basis': None,
                    'reason': 'Historical verdict is evidence, not a forecast.' if settled else 'No elicited or calibrated test-outcome forecast.'},
                'test_cost': {
                    'status': 'not_applicable' if settled else 'unknown',
                    'scope': 'Next scoped test including preparation, execution and review; excludes downstream assembly and total research programme.',
                    'assistant_effort_units': None,
                    'basis': None,
                    'reason': 'No new test selected for this resolved candidate; a rerun requires a separate estimate.' if settled else 'No assistant-effort estimate for a specified test protocol.'},
                'decision_value': {'expected_information_gain_bits': None,
                    'expected_utility': None,
                    'reason': 'Requires a hypothesis/observation model or utility model; outcome entropy alone is not information gain.'}
            })
    return {'schema': 'marici.conjecture-test-planning.v1',
        'contracts': paths, 'source_sha256': {p: sha(p) for p in paths.values()},
        'semantics': {
            'accepted': 'Scoped acceptance met in the selected review/test; not universal truth.',
            'rejected': 'Scoped candidate falsified in the selected review/test.',
            'inconclusive': 'Neither acceptance nor scoped rejection established.',
            'unknown_is_not_zero': True, 'independence_assumed': False,
            'effort_unit': 'One focused assistant read/edit/test/review cycle; relative planning unit, not elapsed time or compute usage.',
            'forecast_uncertainty': 'Qualitative limitation statement attached to each elicited distribution; not a confidence interval.',
            'ranking_policy': 'No numerical prioritization until protocol, forecast and costs are supplied; information gain additionally requires an observation model.'},
        'conjectures': records}


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def validate(m, nets, paths=None):
    paths = PATHS if paths is None else paths
    require(m['schema'] == 'marici.conjecture-test-planning.v1' and m['contracts'] == paths, 'schema/contracts')
    require(m['source_sha256'] == {p: sha(p) for p in paths.values()}, 'source drift')
    require(m['semantics'] == initial(nets, paths)['semantics'], 'planning semantics changed')
    expected = {alias + ':' + n['id']: n for alias, net in nets.items() for n in net['conjectures']}
    rows = {r['id']: r for r in m['conjectures']}
    require(len(rows) == len(m['conjectures']) and set(rows) == set(expected), 'missing/duplicate conjecture')
    for key, r in rows.items():
        n = expected[key]
        require(r['test']['acceptance'] == n['acceptance'] and r['test']['falsifier'] == n['falsifier'], 'test gate drift')
        require(r['test']['protocol_status'] in ('requires_estimation_protocol', 'specified'), 'protocol status')
        p, c = r['probability'], r['test_cost']
        require(p['outcomes'] == OUTCOMES, 'outcome domain')
        require(p['status'] in ('unknown', 'estimated', 'not_applicable'), 'probability status')
        require(c['status'] in ('unknown', 'estimated', 'not_applicable'), 'cost status')
        if n['status'] == 'resolved':
            require(p['status'] == c['status'] == 'not_applicable', 'historical verdict used as forecast')
        else:
            require(p['status'] != 'not_applicable' and c['status'] != 'not_applicable', 'open estimate omitted')
        if p['status'] == 'estimated':
            v = p['values']
            require(r['test']['protocol_status'] == 'specified', 'forecast without protocol')
            require(isinstance(v, dict) and set(v) == set(OUTCOMES), 'probability keys')
            require(all(number(x) and 0 <= x <= 1 for x in v.values()) and abs(sum(v.values()) - 1) < 1e-9, 'probability normalization')
            require(p['conditioning'] and p['uncertainty'] and p['basis'], 'forecast provenance missing')
        else:
            require(p['values'] is None and p['basis'] is None and p['reason'], 'fabricated probability')
        require(set(c) == {'status', 'scope', 'assistant_effort_units', 'basis', 'reason'}, 'unexpected cost fields')
        if c['status'] == 'estimated':
            require(r['test']['protocol_status'] == 'specified' and c['basis'], 'cost without protocol/basis')
            require(number(c['assistant_effort_units']) and c['assistant_effort_units'] >= 0, 'invalid assistant effort')
        else:
            require(c['assistant_effort_units'] is None and c['basis'] is None and c['reason'], 'fabricated cost')
        require(r['decision_value']['expected_information_gain_bits'] is None and r['decision_value']['expected_utility'] is None,
                'decision value needs separately reviewed observation/utility model')
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', action='store_true')
    args = parser.parse_args()
    nets = {k: load(p) for k, p in PATHS.items()}
    if args.record:
        require(not (ROOT / MODEL).exists(), 'refusing implicit overwrite')
        (ROOT / MODEL).write_text(json.dumps(initial(nets), indent=2) + '\n', encoding='utf-8')
    m = load(MODEL)
    rows = validate(m, nets)
    hostiles = []
    for mode in ('missing-node', 'fake-unknown', 'negative-cost', 'unnormalized-probability', 'historical-forecast', 'invented-information-gain', 'stale-source'):
        bad = copy.deepcopy(m)
        r = next(x for x in bad['conjectures'] if x['probability']['status'] != 'not_applicable')
        if mode == 'missing-node': bad['conjectures'].pop()
        elif mode == 'fake-unknown': r['probability'].update(status='unknown', values=dict.fromkeys(OUTCOMES, 1/3))
        elif mode == 'negative-cost':
            r['test']['protocol_status'] = 'specified'
            r['test_cost'].update(status='estimated', basis='hostile fixture', assistant_effort_units=-1)
        elif mode == 'unnormalized-probability':
            r['test']['protocol_status'] = 'specified'
            r['probability'].update(status='estimated', values=dict.fromkeys(OUTCOMES, .5), basis='hostile fixture', conditioning='fixture', uncertainty='fixture')
        elif mode == 'historical-forecast':
            next(x for x in bad['conjectures'] if x['probability']['status'] == 'not_applicable')['probability']['status'] = 'unknown'
        elif mode == 'invented-information-gain': r['decision_value']['expected_information_gain_bits'] = 2
        else: bad['source_sha256'][next(iter(PATHS.values()))] = '0' * 64
        try: validate(bad, nets)
        except ValueError: hostiles.append(mode)
        else: raise AssertionError('hostile accepted: ' + mode)
    # Positive validation of a hypothetical elicitation; never persisted as a forecast.
    fixture = copy.deepcopy(m)
    r = next(x for x in fixture['conjectures'] if x['probability']['status'] != 'not_applicable')
    r['test']['protocol_status'] = 'specified'
    r['probability'].update(status='estimated', values={'accepted': .2, 'rejected': .3, 'inconclusive': .5}, conditioning='synthetic validation only', uncertainty='synthetic', basis='test fixture, not research evidence')
    r['test_cost'].update(status='estimated', basis='synthetic fixture', assistant_effort_units=2)
    validate(fixture, nets)
    result = {'schema': 'marici.conjecture-test-planning-validation.v1', 'passed': True,
        'conjecture_count': len(rows), 'probability_status_counts': {s: sum(r['probability']['status'] == s for r in rows.values()) for s in ('estimated', 'unknown', 'not_applicable')},
        'cost_status_counts': {s: sum(r['test_cost']['status'] == s for r in rows.values()) for s in ('estimated', 'unknown', 'not_applicable')},
        'numerical_ranking_available': all(r['probability']['status'] == r['test_cost']['status'] == 'estimated' for r in rows.values() if r['probability']['status'] != 'not_applicable'), 'corruptions_rejected': hostiles,
        'synthetic_estimate_validation_passed': True,
        'model_sha256': sha(MODEL), 'checker_sha256': sha(Path(__file__).relative_to(ROOT).as_posix())}
    (ROOT / RESULT).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
