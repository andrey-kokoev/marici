"""Live WG programme view: validate historical net, then apply scope overlays.

Does not change historical verdicts/pins or infer theorem completion.
Run without arguments to validate and materialize the effective work view.
"""
from pathlib import Path
import copy
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OVERLAY = 'research/strominger/contracts/wg-symmetry-programme-scope-overlay.v1.json'
OUTPUT = 'research/strominger/results/wg-symmetry-programme/effective-net.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def local(name):
    p = (ROOT / name).resolve()
    require(p.is_relative_to(ROOT), 'Path outside repository')
    return p


def load(name):
    return json.loads(local(name).read_text(encoding='utf-8'))


def effective(base, overlay):
    require(overlay['base_revision'] == base['revision'], 'Base revision mismatch')
    require(overlay['kind'] == 'interpretation_correction_not_new_net', 'Wrong overlay kind')
    require(overlay['execution']['proof_status_changes'] is False, 'Proof status mutation')
    result = copy.deepcopy(base)
    nodes = {n['id']: n for n in result['nodes']}
    require(len(nodes) == len(result['nodes']), 'Duplicate base node')
    seen = set()
    for correction in overlay['overrides']:
        key = correction['node_id']
        require(key in nodes and key not in seen, 'Unknown or duplicate override')
        seen.add(key)
        require(correction['historical_verdict_changed'] is False, 'Verdict mutation')
        require(correction['current_kind'] == 'specification_obligation', 'Unsupported correction kind')
        require(correction['current_disposition'] == 'underspecified_not_ready_for_proof', 'Unsupported disposition')
        require(correction['topology_change_required_for_governing_objective'] is False,
                'Topology change promoted to mandatory prerequisite')
        require(len(correction['required_specification']) == 6, 'Incomplete specification contract')
        require(all(isinstance(x, str) and x.strip() for x in correction['required_specification']),
                'Empty specification requirement')
        n = nodes[key]
        require(n['status'] == 'open', 'Cannot relabel a resolved theorem as an open gate')
        n['historical_statement'] = n['statement']
        n['historical_next_action'] = n.get('next_action')
        n['statement'] = correction['statement']
        n['next_action'] = correction['next_action']
        n['current_label'] = correction['current_label']
        n['current_kind'] = correction['current_kind']
        n['current_disposition'] = correction['current_disposition']
        n['required_specification'] = correction['required_specification']
        n['proof_ready'] = False
        n['scope_overlay'] = OVERLAY
        n['specified_existing_instances'] = []
        for reference in correction.get('specified_existing_instances', []):
            instance = load(reference)
            require(instance['parent_node'] == key, 'Instance parent mismatch')
            require(instance['status'] == 'specified_existing_constructed_instance', 'Wrong instance disposition')
            require(instance['topology_change_required'] is False, 'Instance requires topology change')
            require(all(local(p).is_file() for p in instance['evidence']), 'Missing instance evidence')
            n['specified_existing_instances'].append({'contract': reference,
                'sha256': hashlib.sha256(local(reference).read_bytes()).hexdigest(),
                'status': instance['status'], 'contribution': instance['contribution_to_symmetry_coverage']})
        # Existing blocked_by requirements remain in force. Specification work
        # is visible separately, never promoted into an executable proof task.
    require(seen == {'topological-realization-bridge'}, 'Unexpected correction scope')
    for evidence in overlay.get('branch_evidence', []):
        require(evidence['node_id'] in nodes, 'Unknown evidence node')
        require(local(evidence['path']).is_file(), 'Missing branch evidence')
        item = copy.deepcopy(evidence)
        item['sha256'] = hashlib.sha256(local(evidence['path']).read_bytes()).hexdigest()
        nodes[evidence['node_id']].setdefault('current_branch_evidence', []).append(item)
    children = []
    for link in overlay.get('child_nets', []):
        require(link['node_id'] in nodes, 'Unknown child parent')
        child = load(link['contract'])
        require(child['parent']['contract'] == overlay['base_contract'], 'Child base mismatch')
        require(child['parent']['revision'] == base['revision'], 'Child revision mismatch')
        require(child['parent']['primary_node'] == link['node_id'], 'Child parent mismatch')
        require(link['imports_proof'] is False and child['parent']['imports_proof'] is False,
                'Child proof promotion')
        item = {'id': child['id'], 'contract': link['contract'],
                'sha256': hashlib.sha256(local(link['contract']).read_bytes()).hexdigest(),
                'frontier': child['frontier'], 'recommended_start': child['recommended_start'],
                'parent_node': link['node_id']}
        children.append(item)
        nodes[link['node_id']].setdefault('active_child_nets', []).append(item)
    ready = [n['id'] for n in nodes.values() if n['status'] == 'open'
             and not n.get('blocked_by') and n.get('proof_ready', True)
             and all(nodes[d]['status'] == 'resolved' for d in n['depends_on'])]
    selected_child = next((c for c in children if c['recommended_start'] is not None), None)
    return {
        'schema': 'marici.wg-symmetry-effective-view.v1',
        'governing_objective': overlay['governing_objective'],
        'local_objective': base['objective'],
        'nodes': list(nodes.values()),
        'frontier': ready,
        'specification_queue': [k for k in seen if nodes[k]['current_kind'] == 'specification_obligation'],
        'active_child_nets': children,
        'child_frontier': [{'net': c['id'], 'node': k} for c in children for k in c['frontier']],
        'recommended_start': ({'net': selected_child['id'], 'node': selected_child['recommended_start']} if selected_child else None),
        'recommendation_reason': ('Operator-authorized child conjecture; child frontier is research ordering, not parent proof completion.' if selected_child else 'No active child has selected an executable attempt.'),
        'historical_frontier': base['frontier'],
        'proof_status_changes': False,
    }


def main():
    overlay = load(OVERLAY)
    base = load(overlay['base_contract'])
    require(base['revision'] == 27, 'Review required for new base')
    validator = local(base['validator'])
    subprocess.run([sys.executable, str(validator)], cwd=ROOT, check=True)
    result = effective(base, overlay)
    for link in overlay.get('child_nets', []):
        child = load(link['contract'])
        subprocess.run([sys.executable, str(local(child['validator']))], cwd=ROOT, check=True)
    mutants = []
    for label, mutate in [
        ('revision', lambda o: o.update(base_revision=0)),
        ('unknown-node', lambda o: o['overrides'][0].update(node_id='missing')),
        ('proof-status', lambda o: o['execution'].update(proof_status_changes=True)),
        ('topology-required', lambda o: o['overrides'][0].update(topology_change_required_for_governing_objective=True)),
        ('empty-specification', lambda o: o['overrides'][0].update(required_specification=[])),
        ('duplicate-override', lambda o: o['overrides'].append(copy.deepcopy(o['overrides'][0]))),
    ]:
        bad = copy.deepcopy(overlay)
        mutate(bad)
        try:
            effective(base, bad)
        except ValueError:
            mutants.append(label)
        else:
            raise AssertionError('Corruption accepted: ' + label)
    result['status'] = 'pass'
    result['corruption_controls'] = mutants
    result['sha256'] = {p: hashlib.sha256(local(p).read_bytes()).hexdigest()
                        for p in (OVERLAY, overlay['base_contract'], str(Path(__file__).resolve().relative_to(ROOT)).replace('\\', '/'))}
    out = local(OUTPUT)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'frontier', 'specification_queue', 'recommended_start', 'corruption_controls')}))


if __name__ == '__main__':
    main()
