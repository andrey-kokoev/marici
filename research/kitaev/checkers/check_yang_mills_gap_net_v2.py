"""Successor-net consistency and fresh conditional controls, not proof certification."""
from hashlib import sha256
from pathlib import Path
import json
from check_yang_mills_physical_scaling_obstruction import report as scaling_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-gap-net.v2.json'
GUIDE = BASE+'yang-mills-witnessed-gap-net-v2.md'
SELF = BASE+'checkers/check_yang_mills_gap_net_v2.py'
OUT = ROOT/(BASE+'results/yang-mills-gap-net-v2.json')


def require(ok, reason):
    if not ok:
        raise AssertionError(reason)


def report():
    net = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    pred = net['predecessor']
    require(sha256((ROOT/pred['contract']).read_bytes()).hexdigest() == pred['sha256'], 'immutable v1 contract')
    old = json.loads((ROOT/pred['contract']).read_text(encoding='utf-8'))
    nodes = {n['id']: dict(n) for n in old['conjectures']}
    require(len(nodes) == len(old['conjectures']), 'unique inherited nodes')
    for update in net['conjecture_updates']:
        require(update['id'] in nodes, 'patch targets an inherited logical node')
        nodes[update['id']].update(update['patch'])
    for node in net['new_conjectures']:
        require(node['id'] not in nodes, 'new logical node identity')
        nodes[node['id']] = node
    done, active = set(), set()

    def visit(name):
        require(name in nodes, 'dependency exists: '+name)
        require(name not in active, 'acyclic dependency: '+name)
        if name in done:
            return
        active.add(name)
        for dep in nodes[name].get('depends_on', []):
            visit(dep)
        active.remove(name)
        done.add(name)

    for name in nodes:
        visit(name)
    artifacts = {a['id'] for a in old['artifacts']+net['new_artifacts']}
    for node in nodes.values():
        require(all(e in artifacts for e in node.get('evidence', [])), 'registered evidence: '+node['id'])
    derived = []
    for name, node in nodes.items():
        if node['status'] != 'open' or node.get('blockers') or node.get('requires') or node.get('executable') is False:
            continue
        if all(nodes[d]['status'] == 'resolved' for d in node.get('depends_on', [])):
            derived.append(name)
    require(set(derived) == set(net['ready_frontier']+net['optional_independent_frontier']), 'derived primary and optional frontier')
    require(net['recommendation']['next'] == net['ready_frontier'][0] == 'one-form-generator-identification-audit', 'R3 first')
    require(net['recommendation']['then'] == net['ready_frontier'][1] == 'parameterized-strong-map-lemma', 'R4 conditional alternative')
    require(all(v is False for v in net['boundary'].values()), 'no promotion')
    require(net['objective']['outcome'] is None and net['classical_problem_status'] == 'open', 'root remains open')
    for name in ['continuum-correlation-construction', 'uniform-energy-cost', 'physical-reconstruction', 'completion-stable-separation', 'reviewed-gap-assembly']:
        require(nodes[name]['status'] == 'open' and nodes[name]['outcome'] is None, 'undischarged programme gate: '+name)
    require(nodes['retained-window-continuum-promotion']['verdict'] == 'conditionally_obstructed', 'scoped negative branch')
    require(nodes['independent-fixed-lattice-analytic-review']['status'] == 'blocked' and not nodes['independent-fixed-lattice-analytic-review']['executable'], 'no review waiting leaf')
    require(nodes['fixed-lattice-native-construction']['verdict'] == 'written_candidate_constructed' and not nodes['fixed-lattice-native-construction']['independent_analytic_review_complete'], 'written does not mean reviewed')
    r = scaling_report()
    scaling_path = BASE+'results/yang-mills-physical-scaling-obstruction-v1.json'
    require(r['passed'] and r == json.loads((ROOT/scaling_path).read_text(encoding='utf-8')), 'fresh conditional scaling controls and unchanged predecessor evidence')
    require(not r['review_packet_dispatched'] and not r['external_bibliography_independently_verified'], 'review/citation status retained')
    paths = [CONTRACT, GUIDE, SELF, pred['contract'], scaling_path,
             BASE+'yang-mills-physical-scaling-obstruction-v1.md',
             BASE+'yang-mills-shoshin-second-pass-review-v1.md',
             BASE+'yang-mills-probe-pointwise-core-v1.md', BASE+'yang-mills-probe-strong-noise-v1.md']
    return {
        'schema': 'marici.yang-mills-gap-net.result.v2', 'passed': True,
        'inherited_nodes': len(old['conjectures']), 'logical_nodes_in_successor_view': len(nodes),
        'acyclic': True, 'ready_frontier': net['ready_frontier'],
        'optional_independent_frontier': net['optional_independent_frontier'],
        'recommended_next': net['recommendation']['next'],
        'conditional_scaling_control_packets_replayed': sum(r['coverage'].values()),
        'v1_and_frozen_constructor_evidence_unchanged': True,
        'review_or_Yang_Mills_root_certified': False,
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
