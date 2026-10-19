"""Validate populated WG research graph, source snapshot and attachment wiring."""
import argparse
import copy
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph

CONTRACT = 'research/conjecture_net/contracts/wg-identity-composition-work-net.v1.json'
ATTACHMENTS = 'research/conjecture_net/contracts/wg-foundational-attachments.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def digest(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def sources(c):
    return {p for a in c['artifacts'] for key in ('paths', 'checks', 'receipts')
            for p in a.get(key, [])}


def validate(c, pins, attachment):
    nodes = c['conjectures']
    by = {n['id']: n for n in nodes}
    MetricGraph(tuple(MetricAction(n['id'], frozenset(n['depends_on']),
        status='active' if n['status'] == 'open' else n['status']) for n in nodes)).validate()
    require(c['objective']['target'] in by and c['objective']['outcome'] is None, 'objective')
    artifacts = {a['id']: a for a in c['artifacts']}
    require(len(artifacts) == len(c['artifacts']), 'duplicate artifact')
    for n in nodes:
        require(n['scope'] and n['statement'] and n['acceptance'] and n['falsifier'], 'missing scope/test')
        require(n['outcome'] is None, 'unassigned formal verdict promoted')
        require(set(n['evidence']) <= set(artifacts), 'unknown evidence')
        if n['status'] == 'resolved':
            require(n['verdict'] in ('constructed', 'rejected') and n['evidence'], 'unsupported disposition')
            require(all(by[d]['status'] == 'resolved' for d in n['depends_on']), 'unresolved prerequisite')
        else:
            require(n['status'] == n['verdict'] == 'open' and n['next_action'] and n['deliverable'], 'unactionable open task')
        for dep, verdict in n.get('required_verdicts', {}).items():
            require(dep in n['depends_on'] and verdict == 'constructed', 'untyped assembly gate')
            if n['status'] == 'resolved':
                require(by[dep]['verdict'] == verdict, 'assembly without positive witness')
    for node in ('ordinary-quotient-suffices', 'serial-local-roots-compose', 'equal-energy-is-continuation-identity'):
        require(by[node]['verdict'] == 'rejected' and by[node]['counterexample'], 'lost rejection')
    root = by[c['objective']['target']]
    require(set(root['required_verdicts']) == {'rung-operation-schedule', 'relation-layer-wg-binding',
        'continuation-interface', 'energy-example-interface-comparison'}, 'assembly bypass')
    def ancestors(node):
        result = set()
        for dep in by[node]['depends_on']:
            result.add(dep)
            result.update(ancestors(dep))
        return result
    require(not ({'retained-hamiltonian-example', 'energy-task-example'} & ancestors('rung-operation-schedule')), 'control blocks software WG')
    require('ordinary-quotient-suffices' in ancestors('relation-layer-wg-binding'), 'lost attachment obstruction')
    require('serial-local-roots-compose' in ancestors('whole-package-half-step-binding'), 'lost half-step obstruction')
    require('whole-package-half-step-binding' not in ancestors(c['objective']['target']), 'optional half-step made prerequisite')
    frontier = [n['id'] for n in nodes if n['status'] == 'open' and
                all(by[d]['status'] == 'resolved' for d in n['depends_on'])]
    require(c['frontier'] == frontier, 'stale frontier')
    require(c['recommended_start'] in frontier if frontier else c['recommended_start'] is None, 'invalid start')
    require(attachment['work_net'] == CONTRACT and attachment['attachments'] == c['attachments'], 'attachment mismatch')
    for a in c['attachments']:
        parent = load(a['contract'])
        require(set(a['nodes']) <= {n['id'] for n in parent['conjectures']}, 'missing parent node')
    for ref in c['cross_references']:
        require((ROOT / ref['contract']).is_file(), 'missing cross-reference')
    require(set(pins['source_sha256']) == sources(c), 'pin coverage')
    for p, h in pins['source_sha256'].items():
        require((ROOT / p).resolve().is_relative_to(ROOT) and digest(p) == h, 'source drift: ' + p)
    return frontier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', action='store_true')
    args = parser.parse_args()
    c, attachment = load(CONTRACT), load(ATTACHMENTS)
    pinpath = ROOT / c['source_pins']
    if args.pin:
        require(not pinpath.exists(), 'refusing implicit re-pin')
        data = {p: digest(p) for p in sorted(sources(c))}
        pinpath.write_text(json.dumps({'schema': 'marici.wg-source-pins.v1', 'source_sha256': data}, indent=2) + '\n', encoding='utf-8')
    pins = load(pinpath)
    frontier = validate(c, pins, attachment)
    hostiles = []
    for name in ('cycle', 'unknown-edge', 'lost-rejection', 'lost-lineage', 'control-prerequisite',
                 'optional-to-mandatory', 'assembly-bypass', 'premature-assembly', 'stale-frontier', 'wrong-parent', 'stale-pin'):
        b, p, a = copy.deepcopy(c), copy.deepcopy(pins), copy.deepcopy(attachment)
        by = {n['id']: n for n in b['conjectures']}
        if name == 'cycle': by['whole-package-iteration']['depends_on'] = ['wg-reusable-identity-assembly']
        elif name == 'unknown-edge': by['whole-package-iteration']['depends_on'] = ['absent']
        elif name == 'lost-rejection': by['ordinary-quotient-suffices']['verdict'] = 'constructed'
        elif name == 'lost-lineage': by['relation-layer-wg-binding']['depends_on'] = ['witnessed-composition']
        elif name == 'control-prerequisite': by['rung-operation-schedule']['depends_on'].append('retained-hamiltonian-example')
        elif name == 'optional-to-mandatory': by['wg-reusable-identity-assembly']['depends_on'].append('whole-package-half-step-binding')
        elif name == 'assembly-bypass': by['wg-reusable-identity-assembly']['required_verdicts'] = {}
        elif name == 'premature-assembly':
            # Remain hostile after legitimate root completion: explicitly
            # remove a required prerequisite, not merely repeat root closure.
            by['rung-operation-schedule'].update(status='open', verdict='open')
            by['wg-reusable-identity-assembly'].update(status='resolved', verdict='constructed', evidence=['whole'])
        elif name == 'stale-frontier':
            # Both active and legitimately completed nets need a real mutant.
            b['frontier'] = [] if c['frontier'] else [c['objective']['target']]
        elif name == 'wrong-parent': a['attachments'][0]['nodes'] = ['absent']
        else: p['source_sha256'][next(iter(p['source_sha256']))] = '0' * 64
        try:
            validate(b, p, a)
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('hostile accepted: ' + name)
    require(sum(n['contract'] == CONTRACT for n in load('research/conjecture_net/registry.json')['nets']) == 1, 'registry')
    result = {'schema': 'marici.wg-identity-composition-net-validation.v1', 'status': 'pass',
        'node_count': len(c['conjectures']), 'frontier': frontier,
        'constructed': sum(n['verdict'] == 'constructed' for n in c['conjectures']),
        'rejected': sum(n['verdict'] == 'rejected' for n in c['conjectures']),
        'open': sum(n['status'] == 'open' for n in c['conjectures']),
        'source_pin_count': len(sources(c)), 'rejected_hostiles': hostiles,
        'contract_sha256': digest(CONTRACT), 'attachments_sha256': digest(ATTACHMENTS),
        'pins_sha256': digest(pinpath), 'checker_sha256': digest(Path(__file__)), 'source_suites_rerun': False}
    (ROOT / 'research/nima/results/wg-identity-composition-net-validation.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
