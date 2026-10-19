"""Validate the proposed v3 interfaces/targets; no recovery or empirical verdict."""
import copy
import hashlib
import json
from pathlib import Path
from check_programme_review import documents as previous_documents, validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def documents():
    paths = ('contracts/programme-hierarchy.v3.json', 'contracts/programme-terms.v3.json',
             'contracts/programme-source-interface.v1.json', 'contracts/programme-targets.v1.json',
             'reviews/programme-source-target-review.v1.json')
    return [json.loads((HOME / path).read_text(encoding='utf-8')) for path in paths]


def validate(hierarchy, terms, interface, targets, review):
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    old_hierarchy, old_terms, old_review = previous_documents()
    validate_previous(old_hierarchy, old_terms, old_review)
    require(hierarchy['phase'] == 'proposed_source_interface_and_bounded_targets', 'wrong pilot phase')
    require(hierarchy['root']['outcome'] is None and hierarchy['root']['attempt_status'] == 'unattempted', 'root promotion')
    require(hierarchy['root']['formulation_status'] == 'underspecified' and
            hierarchy['root']['remaining_formulation_gates'], 'premature formulation closure')
    require(hierarchy['promotion_policy'] == old_hierarchy['promotion_policy'], 'promotion policy changed')
    require(hierarchy['existing_net_links'] == old_hierarchy['existing_net_links'], 'candidate links promoted or changed')
    require(hierarchy['obligations'] == old_hierarchy['obligations'] and
            hierarchy['structural_edges'] == old_hierarchy['structural_edges'], 'structural obligations changed without review')
    sources = {item['source_path']: item for item in review['sources']}
    require(review['review_kind'] == 'bounded_textual_and_interface_review_not_theorem_verification', 'review evidence upgrade')
    for path, source in sources.items():
        destination = (ROOT / path).resolve()
        require(destination.is_relative_to(ROOT) and not Path(path).is_absolute(), 'review source escapes repository')
        require(hashlib.sha256(destination.read_bytes()).hexdigest() == source['source_sha256'], 'stale pilot source: ' + path)
    for missing in review['missing_evidence']:
        require(missing['status'] == 'absent' and not (ROOT / missing['source_path']).exists(),
                'missing-evidence inventory changed; explicit review required')
    all_sources = {s['source_path']: s for s in old_review['sources']}
    all_sources.update(sources)
    require(terms['review_status'] == 'partial_review_with_proposed_source_and_targets', 'wrong term phase')
    require({t['id'] for t in terms['terms']} == {t['id'] for t in old_terms['terms']}, 'term slots changed')
    unresolved = []
    for term in terms['terms']:
        if term['id'] == 'shared_regimes':
            require(term['status'] == 'unresolved' and term['definition'] is None and not term['evidence'], 'unreviewed overlap promotion')
            unresolved.append(term['id'])
            continue
        require(term['status'] == 'reviewed_candidate' and term['definition'] and
                term['assumptions'] and term['counterexamples'] and term['residuals'], 'missing candidate term boundaries')
        for evidence in term['evidence']:
            require(evidence['source_path'] in all_sources and
                    evidence['source_sha256'] == all_sources[evidence['source_path']]['source_sha256'], 'term source mismatch')
            require(evidence['role'] == 'textual_scope_and_counterexample_review_not_proof_import', 'term proof promotion')
    require(interface['status'] == 'proposed_candidate' and
            interface['implementation_status'] == 'not_implemented_as_common_carrier', 'common carrier implementation overclaim')
    primitive_ids = {p['id'] for p in interface['primitives']}
    require(len(primitive_ids) == len(interface['primitives']), 'duplicate primitive')
    require(all(p['required_data'] and p['boundary'] for p in interface['primitives']), 'untyped primitive')
    roles = set(interface['source_record_contract']['roles'])
    require({'fitting_input', 'held_out_test', 'imported_physical_theory', 'declared_constructor_convention',
             'derived_source_data', 'measured_calibration'} <= roles, 'missing provenance distinction')
    require(interface['source_record_contract']['rules'] and interface['shared_witness_contract']['required_fields'],
            'missing source/witness policy')
    require(interface['first_source_instance']['common_carrier_embedding'] is None, 'unproved carrier embedding')
    require(targets['selection_status'] == 'proposed_candidate', 'target set prematurely admitted')
    target_ids = {target['id'] for target in targets['targets']}
    require(len(target_ids) == len(targets['targets']) and len(target_ids) == 3, 'unexpected target set')
    require({link['source_primitive'] for link in hierarchy['source_primitive_links']} == primitive_ids,
            'primitive hierarchy coverage incomplete')
    require({link['target_id'] for link in hierarchy['target_links']} == target_ids, 'target hierarchy coverage incomplete')
    for link in hierarchy['source_primitive_links'] + hierarchy['target_links']:
        require(link['proof_bearing'] is False, 'specification link promoted to proof')
        require(link['target_obligation'] in {n['id'] for n in hierarchy['obligations']}, 'unknown obligation')
    for target in targets['targets']:
        require(target['status'] == 'proposed_candidate' and target['outcome'] is None and
                target['attempt_status'] == 'unattempted_as_programme_target', 'pilot outcome/admission overclaim')
        require(target['physical_confirmation'] is False and target['empirical_dataset'] is None, 'empirical confirmation overclaim')
        require(target['required_laws'] and target['allowed_inputs'] and target['excluded'] and
                target['success_criterion'] and target['failure_criterion'] and target['verification_boundary'], 'incomplete pilot scope')
        require(target['class'] in {'structural_recovery', 'prospective_empirical_interface'}, 'unknown target class')
        if target['class'] == 'structural_recovery':
            require(target['source_instance'] == interface['first_source_instance']['id'], 'same-source pilot mismatch')
        else:
            require(target['source_instance'] is None and target['protocol'] is None and
                    target['statistical_rule'] is None, 'unreviewed experimental readiness')
            require('imported Born pairing and Klein-Nishina law' in target['allowed_inputs'], 'imported-law provenance removed')
    policy = targets['empirical_policy']
    require(policy['observed_data_available'] is False and policy['fitting_is_confirmation'] is False and
            policy['imported_law_is_derived_law'] is False, 'empirical circularity policy changed')
    return {'status': 'pass', 'validation_only': True, 'source_primitives': len(primitive_ids),
            'proposed_targets': len(target_ids), 'reviewed_candidate_terms': 8,
            'unresolved_terms': unresolved, 'empirical_datasets': 0, 'admitted_links': 0,
            'root_outcome': None, 'boundary': 'Proposed specification and source integrity only; no physical recovery verified.'}


if __name__ == '__main__':
    print(json.dumps(validate(*documents()), indent=2))
