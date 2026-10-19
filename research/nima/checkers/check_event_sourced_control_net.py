"""Validate the populated event-sourced control research net and source snapshot."""
import argparse
import copy
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph
CONTRACT = 'research/conjecture_net/contracts/event-sourced-control-work-net.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def sources(c):
    return {p for a in c['artifacts'] for p in a['paths']}


def validate(c, pins):
    by = {n['id']: n for n in c['conjectures']}
    status = {'open':'active', 'resolved':'resolved', 'deferred':'pruned'}
    require(all(n['status'] in status for n in c['conjectures']), 'invalid status')
    MetricGraph(tuple(MetricAction(n['id'], frozenset(n['depends_on']), status=status[n['status']])
                      for n in c['conjectures'])).validate()
    artifacts = {a['id'] for a in c['artifacts']}
    require(len(artifacts) == len(c['artifacts']), 'duplicate artifact')
    for n in by.values():
        require(n['statement'] and n['scope'] and n['acceptance'] and n['falsifier'], 'missing scope/test')
        require(n['outcome'] is None and set(n['evidence']) <= artifacts, 'formal outcome/evidence')
        if n['status'] == 'resolved':
            require(n['verdict'] in ('constructed','rejected') and n['evidence'], 'unsupported disposition')
            require(all(by[d]['status'] == 'resolved' for d in n['depends_on']), 'unresolved predecessor')
        else:
            require(n['verdict'] == 'open' and n['next_action'] and n['deliverable'], 'unactionable task')
            if n['status'] == 'deferred':
                require(n.get('blocker') and n.get('reopening_condition'), 'untyped deferral')
        for dep, verdict in n.get('required_verdicts', {}).items():
            require(dep in n['depends_on'] and verdict == 'constructed', 'assembly requirement')
            if n['status'] == 'resolved':
                require(by[dep]['verdict'] == verdict, 'nonpositive assembly premise')
    for node in ('total-energy-is-sufficient-state','static-coordinates-determine-plant'):
        require(by[node]['verdict'] == 'rejected' and by[node]['counterexample'], 'lost rejection')
    require('contextual-capability-witness' in by['typed-event-control-interface']['depends_on'], 'lost Sontag context witness')
    require('static-coordinates-determine-plant' in by['typed-event-control-interface']['depends_on'], 'lost static audit')
    require('total-energy-is-sufficient-state' in by['history-to-state-congruence']['depends_on'], 'lost continuation hostile')
    def ancestors(node):
        result = set()
        for dep in by[node]['depends_on']:
            result.add(dep)
            result.update(ancestors(dep))
        return result
    require('physical-control-binding' not in ancestors('mathematical-control-realization'), 'physical gate blocks mathematical branch')
    require(set(by['same-source-control-comparison']['depends_on']) ==
            {'mathematical-control-realization','physical-control-binding'}, 'same-source bypass')
    require(set(by['mathematical-control-realization']['required_verdicts']) ==
            {'history-to-state-congruence','observation-feedback-realization','presentation-naturality'}, 'math assembly bypass')
    target = c['objective']['target']
    require(target == 'common-event-sourced-control-realization' and c['objective']['outcome'] is None, 'root')
    require(set(by[target]['required_verdicts']) == {'same-source-control-comparison','extension-and-coverage'}, 'coverage bypass')
    frontier = [n['id'] for n in c['conjectures'] if n['status'] == 'open' and
                all(by[d]['status'] == 'resolved' for d in n['depends_on'])]
    require(c['frontier'] == frontier, 'stale frontier')
    require(c['recommended_start'] in frontier if frontier else c['recommended_start'] is None, 'invalid start')
    for a in c['attachments']:
        require(set(a['nodes']) <= {n['id'] for n in load(a['contract'])['conjectures']}, 'attachment')
    for a in c['cross_references']:
        other = load(a['contract'])
        if 'nodes' in a:
            require(set(a['nodes']) <= {n['id'] for n in other['conjectures']}, 'cross-reference')
    require(set(pins['source_sha256']) == sources(c), 'pin coverage')
    for path, digest in pins['source_sha256'].items():
        require((ROOT/path).resolve().is_relative_to(ROOT) and sha(path) == digest, 'source drift: '+path)
    return frontier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', action='store_true')
    args = parser.parse_args()
    c = load(CONTRACT)
    pinpath = ROOT/c['source_pins']
    if args.pin:
        require(not pinpath.exists(), 'refusing implicit re-pin')
        data = {p:sha(p) for p in sorted(sources(c))}
        pinpath.write_text(json.dumps({'schema':'marici.event-sourced-control-pins.v1','source_sha256':data},indent=2)+'\n',encoding='utf-8')
    pins = load(pinpath)
    frontier = validate(c,pins)
    rejected = []
    for name in ('cycle','unknown-edge','lost-rejection','lost-context','lost-hostile','physical-math-conflation',
                 'same-source-bypass','math-assembly-bypass','coverage-bypass','premature-root','stale-frontier','untyped-deferral','stale-pin'):
        b,p = copy.deepcopy(c),copy.deepcopy(pins)
        by = {n['id']:n for n in b['conjectures']}
        if name == 'cycle': by['retained-history-composition']['depends_on'] = ['common-event-sourced-control-realization']
        elif name == 'unknown-edge': by['retained-history-composition']['depends_on'] = ['absent']
        elif name == 'lost-rejection': by['total-energy-is-sufficient-state']['verdict'] = 'constructed'
        elif name == 'lost-context': by['typed-event-control-interface']['depends_on'].remove('contextual-capability-witness')
        elif name == 'lost-hostile': by['history-to-state-congruence']['depends_on'].remove('total-energy-is-sufficient-state')
        elif name == 'physical-math-conflation': by['mathematical-control-realization']['depends_on'].append('physical-control-binding')
        elif name == 'same-source-bypass': by['same-source-control-comparison']['depends_on'] = ['mathematical-control-realization']
        elif name == 'math-assembly-bypass': by['mathematical-control-realization']['required_verdicts'] = {}
        elif name == 'coverage-bypass': by['common-event-sourced-control-realization']['required_verdicts'] = {}
        elif name == 'premature-root': by['common-event-sourced-control-realization'].update(status='resolved',verdict='constructed',evidence=['wg'])
        elif name == 'stale-frontier': b['frontier'] = []
        elif name == 'untyped-deferral': by['physical-control-binding']['status'] = 'deferred'
        else: p['source_sha256'][next(iter(p['source_sha256']))] = '0'*64
        try:
            validate(b,p)
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('hostile accepted: '+name)
    require(sum(e['contract'] == CONTRACT for e in load('research/conjecture_net/registry.json')['nets']) == 1,'registry')
    result = {'schema':'marici.event-sourced-control-net-validation.v1','status':'pass',
        'node_count':len(c['conjectures']),'frontier':frontier,'source_pin_count':len(sources(c)),
        'rejected_hostiles':rejected,'contract_sha256':sha(CONTRACT),'pins_sha256':sha(pinpath),
        'checker_sha256':sha(Path(__file__)),'source_suites_rerun':False}
    (ROOT/'research/nima/results/event-sourced-control-net-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
