"""Validate conjecture-net structure and parent wiring, not physical claims."""
from pathlib import Path
import copy
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from outcome_reference import PORTS, SEMANTICS, file_hash
CONTRACT = 'research/strominger/contracts/marici-tower-cut-domain-net.v1.json'
OVERLAY = 'research/strominger/contracts/wg-symmetry-programme-scope-overlay.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def claim_hash(node):
    claim = {key: node[key] for key in ('id', 'statement', 'scope_id')}
    return hashlib.sha256(json.dumps(claim, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def attempt_outcome(attempts):
    """Conclusive outcomes decide truth; failed attempts never negate them."""
    decisions = {a['outcome'] for a in attempts if a['outcome'] in ('++', '-+')}
    require(len(decisions) <= 1, 'Conflicting outcomes require a scoped correction')
    return next(iter(decisions)) if decisions else (attempts[-1]['outcome'] if attempts else None)


def validate_attempts(node):
    require(isinstance(node.get('scope_id'), str) and node['scope_id'], 'Missing claim scope')
    require('outcome' in node and (node['outcome'] is None or node['outcome'] in PORTS),
            'Unknown proof-attempt outcome')
    require(isinstance(node.get('attempts'), list), 'Missing attempt history')
    for attempt in node['attempts']:
        require(attempt.get('outcome') in PORTS, 'Unknown attempt port')
        require(attempt.get('intent') == PORTS[attempt['outcome']]['attempt'],
                'Attempt intent/outcome mismatch')
        require(attempt.get('scope_id') == node['scope_id'], 'Attempt scope mismatch')
        require(attempt.get('verification_level') and attempt.get('evidence_group'),
                'Missing verification level or shared-evidence identity')
        require(attempt.get('claim_sha256') == claim_hash(node), 'Attempt claim binding changed')
        require(attempt.get('receipt_sha256') == file_hash(ROOT, attempt['receipt']),
                'Attempt receipt changed; explicit evidence review required')
        receipt = load(attempt['receipt'])
        require(receipt['status'] == 'pass', 'Attempt evidence check did not pass')
        # A checker pass verifies its stated control, including counterexamples.
        # It is never by itself interpreted as a ++ outcome.
        for path, digest in receipt.get('sha256', {}).items():
            require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest,
                    'Attempt evidence source drift: ' + path)
    require(node['outcome'] == attempt_outcome(node['attempts']), 'Outcome/history disagreement')
    if node['status'] == 'recorded':
        require(node['outcome'] is None and not node['attempts'],
                'Inspected prior result silently imported as an outcome')
    if node['status'] == 'resolved':
        require(node['outcome'] in ('++', '-+'), 'Failed attempt treated as resolution')
    if node['status'] == 'open':
        require(node['outcome'] not in ('++', '-+'), 'Conclusive outcome left open')
    if node['status'] == 'unformulated':
        require(node['outcome'] is None and not node['attempts'],
                'Unformulated note assigned a proof-attempt outcome')
        require(node.get('kind') == 'research_note' and node.get('next_action') is None
                and not node.get('attempt_protocol') and node.get('reactivation_condition'),
                'Unformulated note advertised as executable')


def validate_target_coverage(net, nodes):
    link = net.get('target_coverage', {})
    require(link.get('role') == 'intended_target_inventory_not_executable_frontier'
            and link.get('status') == 'working_target_inventory_not_exhaustive'
            and link.get('all_known_laws_enumerated') is False
            and link.get('promotes_proof_status') is False, 'Target inventory promoted to coverage')
    require(link.get('catalog') == 'research/strominger/contracts/tower-physical-target-coverage.v1.json',
            'Missing target coverage catalogue')
    catalog = load(link['catalog'])
    require(catalog['schema'] == 'marici.tower-physical-target-coverage.v1'
            and catalog['governing_net'] == CONTRACT
            and catalog['governing_node'] == net['objective']['target']
            and catalog['all_known_laws_enumerated'] is False
            and catalog['status'] == link['status']
            and catalog['revision'] == link.get('catalog_revision') == 4
            and link.get('structural_matrix') == 'structural_obligations',
            'Wrong target catalogue scope')
    require((ROOT / catalog['central_catalog']).is_file(), 'Missing central target locator')
    audit = catalog.get('prior_research_audit', {})
    require(audit.get('evidence_status') == 'bounded_source_inspection_not_scientific_reverification'
            and audit.get('successor_policy') and audit.get('packet')
            and (ROOT / audit['packet']).is_file()
            and audit.get('successor_sweep_packet')
            and (ROOT / audit['successor_sweep_packet']).is_file()
            and set(audit.get('disposition_vocabulary', [])) == {
                'closed_at_scope', 'obstructed', 'genuinely_open', 'unresolved_after_search'},
            'Missing or overpromoted prior-work audit')
    for key in ('operator_stimulus', 'scope_policy', 'coverage_policy', 'scheduling_policy'):
        require(catalog.get(key), 'Missing target inventory policy')
    targets = {t['id']: t for t in catalog['targets']}
    require(len(targets) == len(catalog['targets']), 'Duplicate physical target')
    laws = {'classical-mechanics', 'conservation-and-noether', 'electromagnetism',
            'quantum-dynamics-and-observables', 'quantum-measurement-and-open-systems',
            'quantum-composition-and-statistics', 'special-relativity', 'general-relativity',
            'thermal-and-statistical-physics', 'strong-interaction', 'electroweak-interaction',
            'matter-fields-and-scattering', 'geometric-phase-and-topological-response',
            'continuum-matter-and-transport', 'collective-phases-and-critical-phenomena',
            'kinetic-and-stochastic-evolution'}
    predictions = {'couplings-and-dimensionless-constants', 'particle-spectra-and-bound-states',
                   'cosmological-observables'}
    require(laws | predictions <= set(targets), 'Missing intended physical target family')
    for key, target in targets.items():
        require(target['kind'] in ('law_domain', 'prediction_target'), 'Unknown target kind')
        if key in laws | predictions:
            require(target['kind'] == ('law_domain' if key in laws else 'prediction_target'),
                    'Law and prediction targets conflated')
        require(target['status'] == 'open_coverage' and target.get('attempt_protocol') is None,
                'Inventory target silently proved or scheduled')
        require(all(target.get(k) for k in ('law_domain', 'symmetries', 'supplied_assumptions',
                                           'missing_comparison')), 'Incomplete physical target')
        require(all(n in nodes for n in target['prior_nodes']), 'Unknown target evidence node')
        require(all((ROOT / p).is_file() for p in target.get('prior_packets', [])),
                'Missing target prior packet')
    matrix = catalog['structural_obligations']
    require(matrix.get('policy') and matrix.get('unlisted_pair_status') == 'unassessed',
            'Unassessed applicability silently excluded')
    obligations = {o['id']: o for o in matrix['entries']}
    required = {'scale-change-and-effective-theories', 'locality-and-composition',
                'discrete-antiunitary-and-projective-symmetries',
                'global-sectors-and-extended-observables', 'boundary-and-asymptotic-structure'}
    require(len(obligations) == len(matrix['entries']) and required <= set(obligations),
            'Missing or duplicate structural obligation')
    for obligation in obligations.values():
        require(obligation['status'] == 'open_preservation_obligation'
                and obligation.get('attempt_protocol') is None,
                'Structural inventory silently proved or scheduled')
        require(all(obligation.get(k) for k in ('structure', 'required_comparison',
                    'failure_witness', 'evidence_boundary')), 'Incomplete structural obligation')
        applies = obligation['applies_to']
        require(applies and len(applies) == len(set(applies)) and set(applies) <= set(targets),
                'Invalid structural applicability edge')
        require(all((ROOT / p).is_file() for p in obligation.get('prior_packets', [])),
                'Missing structural prior packet')


def validate(net):
    require(net['id'] == 'marici-tower-cut-domain', 'Wrong net')
    require(net['outcome_semantics'] == SEMANTICS and net['outcome_ports'] == PORTS,
            'Proof outcomes replaced by polarity semantics')
    parent = load(net['parent']['contract'])
    require(parent['revision'] == net['parent']['revision'], 'Parent revision mismatch')
    parent_ids = {n['id'] for n in parent['nodes']}
    require(set(net['parent']['nodes']) <= parent_ids, 'Unknown parent node')
    require(net['parent']['primary_node'] in net['parent']['nodes'], 'Invalid primary parent')
    require(net['parent']['imports_proof'] is False, 'Parent proof import')
    require(net['parent']['mutates_parent_verdicts'] is False, 'Parent verdict mutation')
    require(net['evidence_policy']['governing_claim_verified'] is False, 'Unreviewed universal promotion')
    nodes = {n['id']: n for n in net['nodes']}
    require(len(nodes) == len(net['nodes']), 'Duplicate node')
    validate_target_coverage(net, nodes)
    require(net['objective']['target'] in nodes, 'Missing objective')
    require(net['objective']['status'] == 'open' and net['objective']['outcome'] is None,
            'Unreviewed objective closure')
    objective = nodes[net['objective']['target']]
    require(objective['statement'] == net['objective']['statement']
            == net['operator_stimulus']['current_wording'], 'Clarified objective mismatch')
    representation = net['representation_scope']
    require(representation['quantifiers'] == {'domain': 'forall', 'representation': 'exists',
            'cut': 'exists', 'domain_comparison': 'exists'}, 'Coverage quantifier changed')
    require(representation['required_geometry'] is None
            and {'formed triangle', 'FCC', 'tetrahedral presentation', 'the current retained-record format'}
                <= set(representation['not_required']), 'Privileged geometry reintroduced')
    require(representation['admissibility_status'] == 'not_yet_frozen'
            and objective['formulation_status'] == 'representation_and_cut_admissibility_not_yet_frozen'
            and representation['definition_obligations'] and representation['anti_vacuity'],
            'Unresolved admissibility silently assumed')
    optional = {'intrinsic-law-domain-cut', 'cut-determines-law-domain',
                'original-physical-face-source-binding'}
    require(not optional.intersection(objective['depends_on']), 'Optional triangle branch made prerequisite')
    require(all(nodes[k].get('governing_role', '').startswith('optional_stronger') for k in optional),
            'Missing optional-branch boundary')
    if objective.get('formal_status') == 'fresh_safe_cubical_pass':
        receipt = json.loads((ROOT / objective['formal_receipt']).read_text(encoding='utf-8-sig'))
        require(receipt['passed'] and receipt['exit_code'] == 0 and receipt['ignore_interfaces']
                and receipt['inputs_stable_during_check'], 'Invalid formal receipt')
        data = (ROOT / objective['formal_module']).read_bytes()
        require(hashlib.sha256(data).hexdigest() == receipt['source_sha256'].lower(), 'Formal source drift')
        require(data == (ROOT / objective['formal_source_copy']).read_bytes(), 'Formal copies differ')
    for binding_key in ('native_binding', 'readout_binding', 'composition_binding'):
        if binding_key not in objective:
            continue
        binding = objective[binding_key]
        require(binding['status'] == 'fresh_safe_cubical_pass', 'Unverified native binding')
        receipt = json.loads((ROOT / binding['receipt']).read_text(encoding='utf-8-sig'))
        require(receipt['passed'] and receipt['exit_code'] == 0 and receipt['ignore_interfaces']
                and receipt['inputs_stable_during_check'], 'Invalid native receipt')
        require(hashlib.sha256((ROOT / binding['module']).read_bytes()).hexdigest()
                == receipt['source_sha256'].lower(), 'Native binding source drift')
        require((ROOT / binding['packet']).is_file(), 'Missing native audit')
    recorded_results = {
        'native-symmetry-sector-inventory': 'prior_scoped_symmetry_sectors_inspected',
        'field-tower-automorphism-classification': 'prior_complete_in_category_automorphisms_inspected',
        'canonical-source-pulse-hamiltonians': 'prior_all_port_hamiltonian_derivation_inspected',
        'retained-coefficient-hamiltonian-transport': 'prior_conditional_hamiltonian_transport_and_observer_inspected',
        'mixed-comparison-quartic-residual': 'prior_conditional_quartic_residual_inspected',
        'endpoint-phase-covariant-comparison-adapter': 'prior_endpoint_phase_covariance_inspected',
        'conditional-optical-detector-model-assembly': 'prior_imported_law_optical_assembly_inspected',
        'original-versus-presentation-triangle': 'prior_distinction_and_false_comparison_control_inspected',
        'conditional-seed-elastic-bridge': 'prior_conditional_single_port_elastic_readout_inspected',
        'exchange-charge-independence': 'prior_exchange_has_no_charge_input_inspected',
        'charged-impulse-identification-rejected': 'prior_fixed_exchange_charged_impulse_identification_rejected',
        'multiport-elastic-domain-binding': 'prior_generalized_multiport_binding_found',
        'scalar-star-multiport-obstruction': 'prior_nonzero_tetrad_obstruction_inspected',
        'shared-recoil-cotangent-embedding': 'prior_all_port_constrained_embedding_inspected',
        'old-spatial-recoil-canonical-obstruction': 'prior_full_source_poisson_rank_obstruction_inspected',
        'exchange-shared-leg-factorization-obstruction': 'prior_addressed_rectangle_obstruction_inspected',
        'source-labelled-exchange-compiler': 'prior_weaker_labelled_experiment_compiler_inspected',
    }
    require(set(recorded_results) <= set(nodes), 'Missing inspected prior result')
    visiting, done = set(), set()

    def visit(key):
        require(key in nodes, 'Unknown dependency')
        require(key not in visiting, 'Dependency cycle')
        if key in done:
            return
        visiting.add(key)
        n = nodes[key]
        bounded_resolutions = {'formed-triangle-cut-source-binding': 'constructed_bounded_representation_interface',
                               'loss-noise-domain-cut': 'constructed_bounded_markov_domain_representation',
                               'anomaly-inflow-domain-cut': 'constructed_bounded_relational_inflow_representation',
                               'berry-domain-cut': 'constructed_scoped_CP1_connection_representation',
                               'seed-route-flattening-mechanical-obstruction': 'exact_scoped_mechanical_route_residual',
                               'native-feedback-elastic-observer-binding': 'conditional_native_observer_action_binding',
                               'coefficient-cut-prepared-noise-completeness': 'frozen_coefficient_cut_prepared_noise_refuted',
                               'prepared-oscillator-source-recovery': 'constructed_prepared_source_left_inverse',
                               'route-count-elastic-full-domain-coverage': 'fixed_route_count_full_domain_coverage_refuted',
                               'refining-canonical-berry-cuts': 'proved_canonical_rank_one_refinement_at_written_level'}
        if key in bounded_resolutions:
            require(n['status'] == 'resolved' and n['verdict'] == bounded_resolutions[key], 'Wrong bounded resolution')
        elif key in recorded_results:
            require(n['status'] == 'recorded' and n['verdict'] == recorded_results[key],
                    'Prior result verdict changed')
            require(n.get('evidence_status') == 'prior_source_inspected_not_freshly_verified'
                    and n.get('progress_packet') and n.get('claim_boundary'),
                    'Prior result falsely promoted or unscoped')
        elif key == 'original-physical-face-source-binding':
            require(n['status'] == 'unformulated', 'Unformulated branch silently reopened')
        else:
            require(n['status'] == 'open', 'Unreviewed claim promotion')
        validate_attempts(n)
        expected_refutations = {'seed-route-flattening-mechanical-obstruction',
                                'coefficient-cut-prepared-noise-completeness',
                                'route-count-elastic-full-domain-coverage'}
        if key in bounded_resolutions:
            require(n['outcome'] == ('-+' if key in expected_refutations else '++'),
                    'Scoped construction/refutation outcome reversed')
        require(all(n.get(k) for k in ('statement', 'acceptance', 'falsifier')), 'Incomplete claim')
        for field in ('progress_packet', 'checker'):
            if field in n:
                require((ROOT / n[field]).is_file(), 'Missing progress artifact')
        for path in n.get('prior_work', []) + n.get('source_basis', []):
            require((ROOT / path).is_file(), 'Missing source or prior packet')
        if 'target_implementation' in n:
            require((ROOT / n['target_implementation']).is_file(), 'Missing target implementation')
        for probe in n.get('research_probes', []):
            require(probe in nodes, 'Unknown research probe')
            require(probe not in n['depends_on'], 'Optional probe promoted to prerequisite')
        for dep in n['depends_on']:
            visit(dep)
        visiting.remove(key)
        done.add(key)

    for key in nodes:
        visit(key)
    implication_ids = set()
    for link in net.get('implication_links', []):
        require(link['id'] not in implication_ids, 'Duplicate implication')
        implication_ids.add(link['id'])
        require(link['antecedents'] and all(x in nodes for x in link['antecedents'])
                and link['consequent'] in nodes, 'Unknown implication endpoint')
        require(link['consequent'] not in link['antecedents'], 'Self implication')
        prior_links = {
            'charge-independence-obstructs-fixed-charged-impulse':
                (['exchange-charge-independence'], 'charged-impulse-identification-rejected'),
            'shared-embedding-supplies-scoped-multiport-binding':
                (['shared-recoil-cotangent-embedding'], 'multiport-elastic-domain-binding'),
        }
        prior_link = link['id'] in prior_links
        expected_status = ('conditional_entailment_prior_result_inspected' if prior_link
                           else 'conditional_entailment_not_verified_antecedent')
        require(link['status'] == expected_status
                and link['promotes_proof_status'] is False, 'Implication promoted to proof')
        if prior_link:
            antecedents, consequent = prior_links[link['id']]
            require(link['antecedents'] == antecedents and link['consequent'] == consequent,
                    'Scoped prior implication misdirected')
        require(link['conditions'] and all(isinstance(x,str) and x.strip() for x in link['conditions']),
                'Missing implication conditions')
        if link['id'] == 'determination-and-coverage-imply-governing':
            require(set(link['antecedents']) == {'cut-determines-law-domain','physical-domain-source-coverage'},
                    'Coverage conjunction lost')
    for link in net.get('non_implications', []):
        require(link['from'] in nodes and link['to'] in nodes and link['reason'], 'Invalid non-implication')
    evidence_relations = {'distinguishes_obligation', 'bounded_component',
                          'rules_out_specific_identification', 'bounded_probe',
                          'source_operation_adequacy_probe'}
    for link in net.get('evidence_links', []):
        require(link['from'] in nodes and link['to'] in nodes and link['reason'],
                'Invalid evidence link')
        require(link['relation'] in evidence_relations, 'Evidence link promoted to entailment')
    frontier = [n['id'] for n in nodes.values() if n['status'] == 'open'
                and all(nodes[d]['status'] in ('resolved', 'recorded') for d in n['depends_on'])]
    require(frontier == net['frontier'], 'Stale frontier')
    selected = net['recommended_start']
    if selected is None:
        require(net.get('recommendation_disposition'), 'Missing no-recommendation disposition')
        require(not any(nodes[k].get('attempt_protocol', {}).get('state') == 'planned_not_executed'
                        for k in frontier), 'Ready bounded protocol silently dropped')
    else:
        require(selected in frontier, 'Invalid start')
        protocol = nodes[selected].get('attempt_protocol', {})
        require(protocol.get('intent') in ('prove', 'reject')
                and protocol.get('state') == 'planned_not_executed'
                and all(isinstance(protocol.get(k), str) and protocol[k].strip()
                        for k in ('source', 'target', 'comparison', 'protocol', 'success',
                                  'counterexample', 'failure_policy')),
                'Recommendation lacks a bounded attempt protocol')
    require((ROOT / net['packet']).is_file(), 'Missing packet')
    links = load(OVERLAY).get('child_nets', [])
    require(any(x['contract'] == CONTRACT and x['node_id'] == net['parent']['primary_node'] for x in links), 'Missing parent backlink')
    return frontier


def main():
    net = load(CONTRACT)
    frontier = validate(net)
    rejected = []
    for label, mutate in [
        ('inventory-not-exhaustive-proof', lambda n: n['target_coverage'].update(all_known_laws_enumerated=True)),
        ('inventory-not-executable', lambda n: n['target_coverage'].update(role='executable_frontier')),
        ('inventory-not-proof-promotion', lambda n: n['target_coverage'].update(promotes_proof_status=True)),
        ('stale-target-revision', lambda n: n['target_coverage'].update(catalog_revision=1)),
        ('missing-structural-matrix', lambda n: n['target_coverage'].update(structural_matrix='absent')),
        ('missing-target-catalogue', lambda n: n['target_coverage'].update(catalog='missing.json')),
        ('polarity-not-proof-semantics', lambda n: n.update(outcome_semantics='signed-port-composition')),
        ('wrong-port-definition', lambda n: n['outcome_ports']['--'].update(result='proved')),
        ('attempt-intent-mismatch', lambda n: n['nodes'][0]['attempts'][0].update(intent='reject')),
        ('attempt-scope-mismatch', lambda n: n['nodes'][0]['attempts'][0].update(scope_id='all-physical-domains')),
        ('lost-attempt-history', lambda n: n['nodes'][0].update(attempts=[])),
        ('changed-attempt-claim', lambda n: n['nodes'][0].update(statement='Every physical domain is proved')),
        ('changed-receipt-pin', lambda n: n['nodes'][0]['attempts'][0].update(receipt_sha256='0'*64)),
        ('failed-proof-is-not-resolution', lambda n: (n['nodes'][0].update(outcome='+-'), n['nodes'][0]['attempts'][0].update(outcome='+-'))),
        ('failed-refutation-is-not-resolution', lambda n: (n['nodes'][0].update(outcome='--'), n['nodes'][0]['attempts'][0].update(intent='reject',outcome='--'))),
        ('component-not-parent-proof', lambda n: n['nodes'][-1].update(outcome='++')),
        ('atlas-not-local-proof', lambda n: next(x for x in n['nodes'] if x['id']=='field-tower-automorphism-classification').update(outcome='++')),
        ('optical-import-not-source-proof', lambda n: next(x for x in n['nodes'] if x['id']=='conditional-optical-detector-model-assembly').update(status='resolved')),
        ('prior-not-local-proof', lambda n: next(x for x in n['nodes'] if x['id']=='conditional-seed-elastic-bridge').update(outcome='++')),
        ('counterexample-pass-not-proof', lambda n: next(x for x in n['nodes'] if x['id']=='coefficient-cut-prepared-noise-completeness').update(outcome='++')),
        ('unknown-parent', lambda n: n['parent']['nodes'].append('absent')),
        ('proof-import', lambda n: n['parent'].update(imports_proof=True)),
        ('universal-promotion', lambda n: n['evidence_policy'].update(governing_claim_verified=True)),
        ('cycle', lambda n: n['nodes'][0]['depends_on'].append(n['objective']['target'])),
        ('false-resolution', lambda n: n['nodes'][-1].update(status='resolved')),
        ('missing-evidence', lambda n: n['nodes'][1]['prior_work'].append('missing-packet.md')),
        ('stale-frontier', lambda n: n.update(frontier=[])),
        ('unformulated-note-recommended', lambda n: n.update(recommended_start='original-physical-face-source-binding')),
        ('unformulated-note-reopened', lambda n: next(x for x in n['nodes'] if x['id']=='original-physical-face-source-binding').update(status='open')),
        ('withdrawal-is-not-refutation', lambda n: next(x for x in n['nodes'] if x['id']=='original-physical-face-source-binding').update(outcome='-+')),
        ('recommendation-without-protocol', lambda n: n.update(recommended_start='native-incoming-promotion-compilation')),
        ('completed-berry-recommended', lambda n: n.update(recommended_start='refining-canonical-berry-cuts')),
        ('unknown-probe', lambda n: next(x for x in n['nodes'] if x['id']=='physical-domain-source-coverage')['research_probes'].append('absent')),
        ('unknown-implication', lambda n: n['implication_links'][0].update(consequent='absent')),
        ('implication-proof-promotion', lambda n: n['implication_links'][0].update(promotes_proof_status=True)),
        ('lost-implication-condition', lambda n: n['implication_links'][1].update(conditions=[])),
        ('lost-coverage-conjunct', lambda n: next(x for x in n['implication_links'] if x['id']=='determination-and-coverage-imply-governing').update(antecedents=['cut-determines-law-domain'])),
        ('prior-result-freshness-promotion', lambda n: next(x for x in n['nodes'] if x['id']=='conditional-seed-elastic-bridge').update(evidence_status='freshly_verified')),
        ('prior-result-false-resolution', lambda n: next(x for x in n['nodes'] if x['id']=='original-versus-presentation-triangle').update(status='resolved')),
        ('unknown-evidence-endpoint', lambda n: n['evidence_links'][0].update(to='absent')),
        ('evidence-as-implication', lambda n: n['evidence_links'][0].update(relation='implies')),
        ('charge-obstruction-overreach', lambda n: next(x for x in n['implication_links'] if x['id']=='charge-independence-obstructs-fixed-charged-impulse').update(consequent='physical-domain-source-coverage')),
        ('multiport-overreach', lambda n: next(x for x in n['implication_links'] if x['id']=='shared-embedding-supplies-scoped-multiport-binding').update(consequent='physical-law-domain-as-tower-cut')),
        ('triangle-not-governing-prerequisite', lambda n: n['nodes'][-1]['depends_on'].append('intrinsic-law-domain-cut')),
        ('fcc-not-required', lambda n: n['representation_scope'].update(required_geometry='FCC')),
        ('not-every-representation', lambda n: n['representation_scope']['quantifiers'].update(representation='forall')),
        ('admissibility-not-proved', lambda n: n['representation_scope'].update(admissibility_status='proved')),
        ('stale-multiport-reopening', lambda n: next(x for x in n['nodes'] if x['id']=='multiport-elastic-domain-binding').update(status='open')),
    ]:
        bad = copy.deepcopy(net)
        mutate(bad)
        try:
            validate(bad)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError('Accepted corruption: ' + label)
    result = dict(status='pass', net=net['id'], frontier=frontier,
                  outcome_semantics=SEMANTICS,
                  claims=[{'id': n['id'], 'scope_id': n['scope_id'], 'outcome': n['outcome'],
                           'proposition_truth': {'++': True, '-+': False}.get(n['outcome']),
                           'resolved_proposition': n['outcome'] in ('++', '-+'),
                           'attempts': n['attempts']} for n in net['nodes']],
                  corruption_controls=rejected, scientific_claims_verified=False)
    output = ROOT / 'research/strominger/results/marici-tower-cut-domain-net/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'claims'}))


if __name__ == '__main__':
    main()
