"""Check the RH research graph and handoff wiring; do not run scientific suites."""
import argparse
import copy
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph

CONTRACT = ROOT / 'research/conjecture_net/contracts/rh-realization-work-net.v1.json'
RESULT = ROOT / 'research/nima/results/rh-realization-work-net-validation.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def digest(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def sources(c):
    return ({c['baseline']} | set(c['context_sources']) |
            {a[k] for a in c['artifacts'] for k in ('note', 'checker', 'receipt')})


def validate(c, pins, branches):
    nodes = c['conjectures']
    by = {n['id']: n for n in nodes}
    # MetricGraph calls unfinished nodes active, while the research contract calls them open.
    graph = MetricGraph(tuple(MetricAction(n['id'], frozenset(n['depends_on']),
        status='active' if n['status'] == 'open' else n['status'],
        terminal=n['id'] == c['objective']['target']) for n in nodes))
    graph.validate()
    require(c['objective']['target'] in by and c['objective']['outcome'] is None, 'objective')
    artifacts = {a['id']: a for a in c['artifacts']}
    require(len(artifacts) == len(c['artifacts']), 'duplicate artifact')
    for n in nodes:
        require(n['outcome'] is None, 'unreviewed formal outcome')
        require(n['scope'] and n['acceptance'] and n['falsifier'] and n['statement'], 'missing scoped gate')
        require(set(n['evidence']) <= set(artifacts), 'unknown evidence')
        if n['status'] == 'resolved':
            require(n['verdict'] in ('constructed', 'rejected') and n['evidence'], 'resolved without evidence/verdict')
        else:
            require(n['status'] == n['verdict'] == 'open' and n['next_action'] and n['deliverable'], 'unactionable task')
        for dep, verdict in n.get('required_verdicts', {}).items():
            require(dep in n['depends_on'] and verdict == 'constructed', 'assembly gate')
            if n['status'] == 'resolved':
                require(by[dep]['verdict'] == verdict, 'assembly from rejected/open candidate')
    for rejected in ('native-tick-is-fourier', 'current-source-weil-pullback'):
        require(by[rejected]['verdict'] == 'rejected' and by[rejected]['counterexample'], 'lost rejection')
    require(by['current-source-weil-pullback']['evidence'] == ['weil-counterexample'], 'wrong form evidence')
    require('current-source-weil-pullback' in by['successor-form-candidate']['depends_on'], 'lost repair lineage')
    require(set(by['rh-cross-realization-assembly']['required_verdicts']) ==
            {'rh-math-assembly', 'same-source-continuation-comparison', 'weil-form-comparison'}, 'assembly bypass')
    require(by['rh-math-assembly']['required_verdicts'] == {'rh-stagewise-interface': 'constructed'}, 'math assembly bypass')
    children = {'rh-stage-dictionary', 'rh-operation-composition-squares',
                'rh-identity-continuation-transport', 'rh-analytic-domain-completion-transport'}
    require(set(by['rh-stagewise-interface']['depends_on']) == children and
            by['rh-stagewise-interface']['required_verdicts'] == dict.fromkeys(children, 'constructed'), 'split assembly bypass')
    for child in children - {'rh-stage-dictionary'}:
        require(by[child]['depends_on'] == ['rh-stage-dictionary'] and
                by[child]['required_verdicts'] == {'rh-stage-dictionary': 'constructed'}, 'dictionary gate bypass')
    frontier = [n['id'] for n in nodes if n['status'] == 'open' and
                all(by[d]['status'] == 'resolved' for d in n['depends_on'])]
    require(c['frontier'] == frontier and c['recommended_start'] in frontier, 'stale frontier')
    roles = set()
    for p in c['branch_projections']:
        roles.add(p['role'])
        branch = branches[p['contract']]
        attachment = next(a for a in branch['example_attachments'] if a['id'] == c['shared_example_id'])
        require(attachment['contract'] == c['baseline'] and attachment['role'] == p['role'], 'shared RH/role mismatch')
        links = [w for w in branch['work_nets'] if w['node'] == p['node']]
        require(len(links) == 1, 'branch link missing/duplicated')
        link = links[0]
        require(link['contract'] == CONTRACT.relative_to(ROOT).as_posix() and
                link['target'] == p['target'] and link['role'] == p['role'] and
                link['shared_example_id'] == c['shared_example_id'], 'branch target mismatch')
        require(p['target'] in p['focus'] and set(p['focus']) <= set(by), 'unknown projection node')
        require(set(link['entry_nodes']) <= set(frontier) & set(p['focus']), 'invalid branch entry')
    require(roles == {'mathematical_realization', 'same_source_compatibility'} and len(c['branch_projections']) == 2, 'dual role loss')
    require(set(pins['source_sha256']) == sources(c), 'pin coverage')
    for path, expected in pins['source_sha256'].items():
        require((ROOT / path).resolve().is_relative_to(ROOT), 'external source')
        require(digest(path) == expected, 'source drift: ' + path)
    baseline = load(c['baseline'])
    require(set(c['legacy_frontiers']['routes']) <= set(baseline['active_frontier']), 'legacy route missing')
    require(baseline['transverse_unchanged_evans']['status'] == 'rejected_for_tested_criterion', 'legacy rejection lost')
    return frontier, {
        'open_tasks': sum(n['status'] == 'open' for n in nodes),
        'ready_tasks': len(frontier),
        'resolved_constructions': sum(n['verdict'] == 'constructed' for n in nodes),
        'resolved_rejected_candidates': sum(n['verdict'] == 'rejected' for n in nodes),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', action='store_true')
    args = parser.parse_args()
    c = load(CONTRACT)
    pinpath = ROOT / c['source_pins']
    if args.pin:
        require(not pinpath.exists(), 'refusing implicit re-pin')
        pinpath.write_text(json.dumps({'schema': 'marici.rh-realization-work-source-pins.v1',
            'source_sha256': {p: digest(p) for p in sorted(sources(c))}}, indent=2) + '\n', encoding='utf-8')
    pins = load(pinpath)
    branches = {p['contract']: load(p['contract']) for p in c['branch_projections']}
    frontier, metrics = validate(c, pins, branches)
    hostiles = []
    for name in ('cycle', 'unknown-edge', 'lost-rejection', 'lost-lineage', 'wrong-evidence',
                 'stale-frontier', 'role-conflation', 'different-rh', 'assembly-bypass', 'split-assembly-bypass', 'dictionary-gate-bypass', 'stale-pin'):
        b, p, bs = copy.deepcopy(c), copy.deepcopy(pins), copy.deepcopy(branches)
        by = {n['id']: n for n in b['conjectures']}
        if name == 'cycle': by['carrier-fourier-attachment']['depends_on'] = ['rh-cross-realization-assembly']
        elif name == 'unknown-edge': by['carrier-fourier-attachment']['depends_on'] = ['absent']
        elif name == 'lost-rejection': by['current-source-weil-pullback']['verdict'] = 'constructed'
        elif name == 'lost-lineage': by['successor-form-candidate']['depends_on'] = ['signed-weil-quotient']
        elif name == 'wrong-evidence': by['current-source-weil-pullback']['evidence'] = ['additive']
        elif name == 'stale-frontier': b['frontier'] = []
        elif name == 'role-conflation': b['branch_projections'][1]['role'] = 'mathematical_realization'
        elif name == 'different-rh': next(iter(bs.values()))['example_attachments'][0]['contract'] = 'different.json'
        elif name == 'assembly-bypass': by['rh-cross-realization-assembly']['required_verdicts'] = {}
        elif name == 'split-assembly-bypass': by['rh-stagewise-interface']['required_verdicts'] = {'rh-stage-dictionary': 'constructed'}
        elif name == 'dictionary-gate-bypass': by['rh-operation-composition-squares']['required_verdicts'] = {}
        else: p['source_sha256'][next(iter(p['source_sha256']))] = '0' * 64
        try:
            validate(b, p, bs)
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('hostile accepted: ' + name)
    registry = load('research/conjecture_net/registry.json')
    require(sum(n['contract'] == CONTRACT.relative_to(ROOT).as_posix() for n in registry['nets']) == 1, 'registry')
    result = {'schema': 'marici.rh-realization-work-net-validation.v1', 'status': 'pass',
        'node_count': len(c['conjectures']), 'frontier': frontier, 'metrics': metrics,
        'source_pin_count': len(sources(c)), 'rejected_hostiles': hostiles,
        'contract_sha256': digest(CONTRACT), 'checker_sha256': digest(Path(__file__)),
        'pins_sha256': digest(pinpath), 'source_suites_rerun': False}
    RESULT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
