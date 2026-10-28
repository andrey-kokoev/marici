"""Owner-local AdS/dS adapter to the shared planning validator and workbench.
Run normally to refresh; --check verifies deterministic output without writing.
No graph mutations or scientific outcome inference are performed.
"""
import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/voevodsky/checkers'))
from check_conjecture_test_planning import initial, require, sha
from check_conjecture_workbench import build, blockers, index

INPUT = 'research/nima/contracts/ads-ds-workbench.v1.json'
SCRIPT = Path(__file__).relative_to(ROOT).as_posix()
REPORT = 'research/nima/results/ads-ds-workbench.v1.json'
VIEW = 'research/nima/ADS-DS-WORKBENCH.md'
ENGINE = ['research/voevodsky/checkers/check_conjecture_workbench.py',
          'research/voevodsky/checkers/check_conjecture_test_planning.py']


def adapt(data):
    tasks = data['tasks']
    ids = [t['id'] for t in tasks]
    require(len(set(ids)) == len(ids), 'duplicate task')
    nodes = []
    for t in tasks:
        require(set(t['depends_on']) <= set(ids), 'unknown dependency')
        require(set(t['required_verdicts']) <= set(t['depends_on']), 'unbound required verdict')
        status = t.get('status', 'open')
        require(status in ('open', 'resolved'), 'invalid task status')
        if status == 'resolved':
            require(t.get('verdict') in ('constructed', 'rejected') and t.get('evidence'), 'resolution without evidence')
            for path, digest in t['evidence'].items():
                require((ROOT / path).is_file() and sha(path) == digest, 'resolution evidence drift')
        nodes.append({k: t[k] for k in ('id', 'depends_on', 'required_verdicts',
                     'statement', 'acceptance', 'falsifier', 'next_action')} |
                     {'status': status, 'verdict': t.get('verdict', 'open'),
                      'requires': ['specified-protocol:' + t['id']] if status == 'open' and t.get('protocol_status') == 'requires_specification' else []})
    by_id = {n['id']: n for n in nodes}
    def visit(k, stack):
        require(k not in stack, 'dependency cycle')
        for d in by_id[k]['depends_on']:
            visit(d, stack | {k})
    for k in by_id:
        visit(k, set())
    goal = data.get('goal_task', 'interval-route-synthesis')
    require(goal in by_id, 'unknown goal')
    nets = {'adsds': {'conjectures': nodes, 'interfaces': [],
                      'objective': {'target': goal}}}
    paths = {'adsds': INPUT}
    planning = initial(nets, paths)
    # File timestamp records this elicitation artifact, not a scientific event date.
    stamp = datetime.fromtimestamp((ROOT / INPUT).stat().st_mtime, timezone.utc).isoformat()
    cards = []
    for t, p in zip(tasks, planning['conjectures']):
        if t.get('status') == 'resolved':
            continue
        specified = t.get('protocol_status', 'specified') == 'specified'
        require(t.get('protocol_status', 'specified') in ('specified', 'requires_specification'), 'invalid protocol status')
        if specified:
            require(len(t['forecast']) == 3, 'forecast length')
        else:
            require(t.get('forecast') is None and t.get('effort') is None, 'unspecified protocol has operative estimates')
        basis = data['estimate_basis'] + ' Input revision timestamp: ' + stamp + '. ' + t['rationale']
        p['test']['protocol_status'] = 'specified' if specified else 'requires_estimation_protocol'
        p['test']['preparation'] = t['next_action']
        p['test']['stopping_rule'] = 'Stop at the stated acceptance, scoped counterexample, or effort budget; report inconclusive otherwise.'
        if specified:
            p['probability'].update(status='estimated',
                values=dict(zip(('accepted', 'rejected', 'inconclusive'), t['forecast'])),
                conditioning='Conditional on all constructed-witness prerequisites being reviewed and available.',
                uncertainty='Uncalibrated subjective next-test forecast, not theorem probability; correlations are not modeled.',
                basis=basis)
            p['test_cost'].update(status='estimated', assistant_effort_units=t['effort'], basis=basis)
        cards.append({'id': 'adsds:' + t['id'], 'first_action': t['next_action'],
            'deliverable': 'Scoped witness or counterexample with source/domain bindings; no automatic conjecture promotion.',
            'acceptance': t['acceptance'], 'falsifier': t['falsifier'],
            'reuse_sources': t['sources'], 'reuse_policy': 'Inspect actual constructors before new machinery.',
            'stop_rule': p['test']['stopping_rule'],
            'review_promotion': 'Requires separate evidence review and graph admission.'})
    cards = {'schema': 'marici.conjecture-action-cards.v1', 'cards': cards,
             'source_sha256': {INPUT: sha(INPUT)}}
    return nets, planning, cards, paths


def calculate(data):
    nets, planning, cards, paths = adapt(data)
    attempts = []
    catalog_paths = []
    if data.get('attempt_catalog'):
        catalog_paths.append(data['attempt_catalog'])
        catalog = json.loads((ROOT / data['attempt_catalog']).read_text(encoding='utf-8'))
        require(catalog['net_id'] == data['graph_net_id'], 'attempt catalog net mismatch')
        attempts = catalog['conjectures']
        require(len({a['id'] for a in attempts}) == len(attempts), 'duplicate rejection attempt')
        for a in attempts:
            require(a['outcome'] == '-+' and a['attempt'] == 'reject', 'invalid rejection outcome')
            require(a['counterexample'] and a['verification'] and a['survives'] and a['sources'], 'unscoped rejection')
            for path in a['sources']:
                require((ROOT / path).is_file(), 'missing rejection evidence')
                catalog_paths.append(path)
    sources = sorted(set([INPUT, SCRIPT, *ENGINE, *catalog_paths] + [p for t in data['tasks'] for p in [*t['sources'], *t.get('evidence', {})]]))
    report = build(nets, planning, cards, paths=paths, source_paths=sources)
    report['graph_binding'] = {k: data[k] for k in ('graph_net_id', 'graph_snapshot_head', 'scope')}
    report['objective'] = data['objective']
    report['retired_tasks'] = data.get('retired_tasks', [])
    report['deferred_questions'] = data.get('deferred_questions', [])
    report['goal_key'] = 'adsds:' + data.get('goal_task', 'interval-route-synthesis')
    report['estimates'] = planning
    report['claim_relevance'] = {t['id']: t['affected_claims'] for t in data['tasks']}
    report['scientific_outcomes_changed'] = False
    report['recorded_rejection_attempts'] = attempts
    report['attempt_boundary'] = 'Imported explicit attempts, not new inference by this planner; reviewed prior results are not fresh executions.'
    report['resolved_tasks'] = [{'id': t['id'], 'verdict': t['verdict'], 'scope': t.get('resolution_scope'), 'evidence': t['evidence']} for t in data['tasks'] if t.get('status') == 'resolved']
    # All rankings use the shared engine, including sensitivity scenarios.
    scenarios = []
    for t in data['tasks']:
        if t.get('status') == 'resolved' or t.get('protocol_status') == 'requires_specification':
            continue
        changed = copy.deepcopy(planning)
        row = next(r for r in changed['conjectures'] if r['id'] == 'adsds:' + t['id'])
        row['test_cost']['assistant_effort_units'] *= 2
        alt = build(nets, changed, cards, paths=paths, source_paths=sources)
        scenarios.append({'change': 'double effort for ' + t['id'],
                          'recommendation': alt['recommendation']})
    report['sensitivity'] = scenarios
    return report, (nets, planning, cards, paths, sources)


def controls(data, context):
    nets, planning, cards, paths, sources = context
    passed = []
    for mode in ('duplicate', 'cycle', 'negative-effort', 'unnormalized', 'missing-source'):
        bad = copy.deepcopy(data)
        first_open = next(t for t in bad['tasks'] if t.get('status', 'open') == 'open' and t.get('protocol_status', 'specified') == 'specified')
        if mode == 'duplicate': bad['tasks'].append(copy.deepcopy(bad['tasks'][0]))
        elif mode == 'cycle': bad['tasks'][0]['depends_on'] = [bad['tasks'][0]['id']]
        elif mode == 'negative-effort': first_open['effort'] = -1
        elif mode == 'unnormalized': first_open['forecast'] = [1, 1, 1]
        else: first_open['sources'] = ['research/nima/NO-SUCH-SOURCE.md']
        try:
            n, p, c, ps = adapt(bad)
            build(n, p, c, paths=ps, source_paths=sources)
        except ValueError:
            passed.append(mode)
        else:
            raise AssertionError('accepted corruption: ' + mode)
    by = copy.deepcopy(index(nets))
    key = 'adsds:wg-interval-dictionary'
    target = 'adsds:wg-interval-operation-square'
    by[key].update(status='resolved', verdict='rejected')
    require(bool(blockers(target, by, nets)), 'rejection unlocked construction')
    by[key]['verdict'] = 'constructed'
    require(not blockers(target, by, nets), 'construction failed to unlock')
    passed += ['rejection-blocks-construction', 'construction-unlocks-square']
    unknown = copy.deepcopy(planning)
    for r in unknown['conjectures']:
        if r['probability']['status'] == 'not_applicable':
            continue
        r['probability'].update(status='unknown', values=None, basis=None, reason='control')
        r['test_cost'].update(status='unknown', assistant_effort_units=None, basis=None, reason='control')
    require(build(nets, unknown, cards, paths=paths, source_paths=sources)['recommendation'] is None,
            'unknown estimates ranked')
    passed.append('unknown-not-zero')
    stale = copy.deepcopy(cards)
    stale['source_sha256'][INPUT] = '0' * 64
    try: build(nets, planning, stale, paths=paths, source_paths=sources)
    except ValueError: passed.append('source-drift-rejected')
    else: raise AssertionError('source drift accepted')
    for t in data['tasks']:
        if t.get('status') == 'resolved':
            bad = copy.deepcopy(data)
            bad_task = next(x for x in bad['tasks'] if x['id'] == t['id'])
            bad_task['evidence'][next(iter(bad_task['evidence']))] = '0' * 64
            try: adapt(bad)
            except ValueError: passed.append('resolved-evidence-drift:' + t['id'])
            else: raise AssertionError('stale resolution accepted')
    unready = [t['id'] for t in data['tasks'] if t.get('protocol_status') == 'requires_specification' and t.get('status', 'open') == 'open']
    checked = build(nets, planning, cards, paths=paths, source_paths=sources)
    frontier_ids = {r['id'] for r in checked['frontier']}
    require(all('adsds:' + k not in frontier_ids for k in unready), 'unspecified task ranked')
    require(all(r['probability'] is None for r in checked['blocked'] if r['id'].split(':',1)[1] in unready), 'unspecified forecast retained')
    passed.append('unspecified-protocols-unranked')
    return passed


def render(r):
    out = ['# AdS–dS conjecture workbench', '',
           'Generated by `research/nima/checkers/check_ads_ds_workbench.py` using the shared planning validator and dependency-aware workbench engine.', '',
           '**Global efficiency recommendation:** `' + str(r['recommendation']) + '`.',
           '**WG-I1-route recommendation:** `' + str(r['goal_frontiers'][r['goal_key']]['recommendation']) + '`.', '',
           r['objective'], '',
           '| Ready bounded test | Effort | Decisive forecast | Score |', '|---|---:|---:|---:|']
    for row in r['frontier']:
        p = row['probability']
        out.append(f"| {row['id']} | {row['assistant_effort_units']} | {p['accepted'] + p['rejected']:.0%} | {row['decisive_result_per_effort']} |")
    out += ['', '## Completed bounded tests', '']
    for row in r['resolved_tasks']:
        out.append('- ' + row['id'] + ': ' + row['verdict'] + '. ' + str(row['scope']))
    out += ['', '## Recorded successful rejection attempts', '', r['attempt_boundary'], '']
    for a in r['recorded_rejection_attempts']:
        out.append('- **' + a['outcome'] + '** `' + a['id'] + '`: ' + a['counterexample'] + ' Scope retained: ' + a['survives'])
    out += ['', '## Retired and deferred questions', '']
    for item in r['retired_tasks'] + r['deferred_questions']:
        out.append('- ' + item['id'] + ': ' + item['reason'])
    out += ['', '## Blocked tests', '']
    for row in r['blocked']:
        out.append('- ' + row['id'] + ': ' + ', '.join(b['id'] for b in row['blockers']))
    out += ['', '## Sensitivity: double one task cost', '']
    for s in r['sensitivity']:
        out.append('- ' + s['change'] + ' → ' + str(s['recommendation']))
    out += ['', '## Ready action cards', '']
    for row in r['frontier']:
        c = row['action_card']
        out += ['### ' + row['id'], '', c['first_action'], '', '**Acceptance:** ' + c['acceptance'],
                '', '**Falsifier:** ' + c['falsifier'], '', '**Stop:** ' + c['stop_rule'], '']
    out += ['## Boundaries', '',
            'Forecasts are subjective, uncalibrated and concern bounded tests, not conjecture truth. Effort is relative assistant cycles, not measured tokens or time. Scores do not measure expected information gain or structural synthesis; affected-claim links provide relevance context only.',
            'This is a bounded-test planning overlay, not an exhaustive graph census. Blocked forecasts assume their prerequisites. No dependency is a proof implication. Local task resolution does not promote broader graph conjectures.',
            'The graph binding is an explicit snapshot, not automatic synchronization. Resolved tasks require hash-pinned evidence and carry no next-test forecast. Reconcile new graph outcomes before changing local task statuses.',
            'Inputs: `research/nima/contracts/ads-ds-workbench.v1.json`. Report: `research/nima/results/ads-ds-workbench.v1.json`.',
            'Refresh: `python research/nima/checkers/check_ads_ds_workbench.py`; drift check: append `--check`.', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / INPUT).read_text(encoding='utf-8'))
    report, context = calculate(data)
    report['validation_controls'] = controls(data, context)
    outputs = {REPORT: json.dumps(report, indent=2) + '\n', VIEW: render(report)}
    for path, content in outputs.items():
        dest = ROOT / path
        if args.check:
            require(dest.is_file() and dest.read_text(encoding='utf-8') == content, 'generated drift: ' + path)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding='utf-8')
    print(json.dumps({'passed': True, 'recommendation': report['recommendation'],
                      'coverage': report['coverage'], 'controls': report['validation_controls'],
                      'check_only': args.check}, indent=2))


if __name__ == '__main__':
    main()
