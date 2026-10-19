"""Validate the partial term review and candidate links; no proof promotion."""
import hashlib
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def validate(hierarchy, terms, review):
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    def live_pin(path, expected):
        resolved = (ROOT / path).resolve()
        require(resolved.is_relative_to(ROOT) and not Path(path).is_absolute(), 'source escapes repository')
        require(hashlib.sha256(resolved.read_bytes()).hexdigest() == expected, 'stale reviewed source: ' + path)
    require(hierarchy['phase'] == 'partial_term_review_candidate_links', 'wrong review phase')
    require(terms['review_status'] == 'partial_candidate_review', 'wrong term-review state')
    require(review['review_kind'] == 'textual_repository_review_not_theorem_verification', 'review overclaim')
    sources = {s['source_path']: s for s in review['sources']}
    require(len(sources) == len(review['sources']), 'duplicate reviewed source')
    for source in sources.values():
        live_pin(source['source_path'], source['source_sha256'])
        require(source['claim'] and source['scope'] and source['verification_level'], 'untyped review evidence')
    reviewed = set(review['reviewed_terms'])
    require(reviewed == {'carrier', 'geometry', 'dynamics', 'observables'}, 'unexpected reviewed term set')
    ids = {hierarchy['root']['id']} | {n['id'] for n in hierarchy['obligations']}
    term_ids = {t['id'] for t in terms['terms']}
    require(len(ids) == len(hierarchy['obligations']) + 1 and len(term_ids) == len(terms['terms']), 'duplicate ID')
    for node in [hierarchy['root']] + hierarchy['obligations']:
        require(node['outcome'] is None and node['attempt_status'] == 'unattempted' and
                node['formulation_status'] == 'underspecified', 'premature programme outcome/formulation')
        require(set(node.get('scope_terms', node.get('term_slots', []))) <= term_ids, 'unknown term slot')
    for term in terms['terms']:
        if term['id'] in reviewed:
            require(term['status'] == 'reviewed_candidate' and bool(term['definition']), 'missing candidate definition')
            require(term['assumptions'] and term['counterexamples'] and term['residuals'], 'missing review boundaries')
            require(bool(term['evidence']), 'unsupported candidate term')
            for evidence in term['evidence']:
                source = sources.get(evidence['source_path'])
                require(source is not None and source['source_sha256'] == evidence['source_sha256'], 'term pin mismatch')
                require(evidence['role'] == 'textual_scope_and_counterexample_review_not_proof_import', 'term evidence upgrade')
        else:
            require(term['status'] == 'unresolved' and term['definition'] is None and not term['evidence'],
                    'unreviewed term promoted')
    for edge in hierarchy['structural_edges']:
        require(edge['from'] in ids and edge['to'] in ids and edge['proof_bearing'] is False and
                edge['relation'] == 'candidate_obligation', 'structural proof-edge promotion')
    links = hierarchy['existing_net_links']
    require(len({link['id'] for link in links}) == len(links), 'duplicate net link')
    for link in links:
        require(set(hierarchy['link_contract']['required_fields']) <= set(link), 'incomplete net-link contract')
        require(link['target_obligation'] in ids and link['target_obligation'] != hierarchy['root']['id'], 'wrong link target')
        require(link['status'] == 'candidate' and link['relation'] == 'candidate_prerequisite' and
                link['proof_bearing'] is False, 'candidate link cannot admit proof')
        require(link['source_net'] in sources, 'unreviewed linked net')
        require(link['source_sha256'] == sources[link['source_net']]['source_sha256'], 'linked source pin mismatch')
        source = json.loads((ROOT / link['source_net']).read_text(encoding='utf-8'))
        claims = {n['id'] for n in source.get('conjectures', source.get('nodes', []))}
        claims.add(source.get('claim'))
        require(link['source_claim'] in claims, 'unknown source claim')
        require(link['scope_transport'] and link['witness_transport'] and link['verification_boundary'], 'missing transport boundary')
        if link['outcome_pointer'] is not None:
            require((ROOT / link['outcome_pointer']).is_file(), 'missing candidate export pointer')
    policy = hierarchy['promotion_policy']
    require(policy['automatic_child_outcome_aggregation'] is False and policy['registry_presence_is_evidence'] is False
            and policy['common_witness_transport_required'] is True, 'unsafe promotion policy')
    for task in hierarchy['next_refinements']:
        require(task['parent'] in ids and task['outcome'] is None and task['kind'] == 'specification_task',
                'specification task promoted to theorem')
    return {'status': 'pass', 'validation_only': True, 'reviewed_sources': len(sources),
            'candidate_terms': len(reviewed), 'unresolved_terms': len(term_ids - reviewed),
            'candidate_links': len(links), 'admitted_links': 0, 'root_outcome': None,
            'boundary': 'Source integrity and review structure only; no fresh theorem or physical verification.'}


def documents():
    paths = ('contracts/programme-hierarchy.v2.json', 'contracts/programme-terms.v2.json',
             'reviews/programme-term-review.v1.json')
    return [json.loads((HOME / path).read_text(encoding='utf-8')) for path in paths]


if __name__ == '__main__':
    print(json.dumps(validate(*documents()), indent=2))
