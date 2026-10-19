"""Validate the structure-first programme scaffold, not its conjecture truth."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


def validate(hierarchy, terms):
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    require(hierarchy['phase'] == 'structure_before_term_review', 'not a structure-only scaffold')
    nodes = [hierarchy['root']] + hierarchy['obligations']
    ids = [node['id'] for node in nodes]
    require(len(ids) == len(set(ids)), 'duplicate node')
    term_ids = [term['id'] for term in terms['terms']]
    require(len(term_ids) == len(set(term_ids)), 'duplicate term')
    for node in nodes:
        require(node['outcome'] is None and node['attempt_status'] == 'unattempted',
                'scaffold cannot admit an outcome')
        require(node['formulation_status'] == 'underspecified', 'unreviewed formulation promoted')
        for slot in node.get('scope_terms', node.get('term_slots', [])):
            require(slot in term_ids, 'unknown term slot: ' + slot)
    for term in terms['terms']:
        require(term['status'] == 'unresolved' and term['definition'] is None and not term['evidence'],
                'terms must await repository review')
    require(terms['review_status'] == 'not_started', 'term review not recorded consistently')
    edges = hierarchy['structural_edges']
    adjacency = {key: [] for key in ids}
    for edge in edges:
        require(edge['from'] in ids and edge['to'] in ids, 'unknown edge endpoint')
        require(edge['relation'] == 'candidate_obligation' and edge['proof_bearing'] is False,
                'structural edge cannot imply proof')
        adjacency[edge['from']].append(edge['to'])
    visiting, done = set(), set()
    def visit(key):
        require(key not in visiting, 'cyclic hierarchy')
        if key in done:
            return
        visiting.add(key)
        for target in adjacency[key]:
            visit(target)
        visiting.remove(key)
        done.add(key)
    for key in ids:
        visit(key)
    require({edge['from'] for edge in edges if edge['to'] == ids[0]} == set(ids[1:]),
            'root obligation coverage incomplete')
    require(not hierarchy['existing_net_links'], 'existing net links await repository review')
    policy = hierarchy['promotion_policy']
    require(policy['automatic_child_outcome_aggregation'] is False and
            policy['registry_presence_is_evidence'] is False, 'unsafe promotion policy')
    require(all(policy[key] is True for key in ('terms_before_attempt',
            'explicit_scoped_imports_required', 'common_witness_transport_required',
            'logical_assembly_rule_required', 'mixed_evidence_must_retain_verification_level',
            'branch_failure_does_not_refute_existential_root')), 'missing admission boundary')
    return {'status': 'pass', 'validation_only': True, 'nodes': len(nodes),
            'unresolved_terms': len(term_ids), 'admitted_links': 0,
            'root_outcome': None, 'boundary': 'Structure only; no theorem or physical verification.'}


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v1.json').read_text())
    terms = json.loads((HOME / 'contracts/programme-terms.v1.json').read_text())
    print(json.dumps(validate(hierarchy, terms), indent=2))
