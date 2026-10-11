"""Validate the scoped four-proof-outcome net and its directional-cost frontier."""
import hashlib
import json
import sys
from pathlib import Path

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
CONTRACT = OWNER / 'contracts/current-problem-conjecture-net.v1.json'
OUT = OWNER / 'results/current-problem-conjecture-net.json'
sys.path.insert(0, str(REPO / 'research/conjecture_net'))
from interpretation_planner import OUTCOMES
from check_lift_outcome_split import active_branches, local_core_consequences

EXPECTED = {
    '++': ('prove', 'proved'),
    '+-': ('prove', 'failed_to_prove'),
    '-+': ('reject', 'succeeded_in_rejecting'),
    '--': ('reject', 'failed_at_rejecting'),
}
CHECKS = []


def require(name, ok):
    if not ok:
        raise AssertionError(name)
    CHECKS.append(name)


def main():
    OUT.unlink(missing_ok=True)
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    require('existing-four-outcome-domain', set(OUTCOMES) == set(EXPECTED))
    require('user-outcome-port-meanings', c['outcome_ports'] == {
        k: {'attempt': v[0], 'result': v[1]} for k, v in EXPECTED.items()})
    require('failed-attempts-do-not-infer-opposite',
            c['logic_boundary']['+-'].endswith('does not prove the negation')
            and c['logic_boundary']['--'].endswith('does not prove the conjecture'))
    require('directional-costs-separate', c['cost_model']['separate_by_intent'] is True
            and c['cost_model']['fields'] == ['cost_to_prove', 'cost_to_reject'])

    nodes = {n['id']: n for n in c['conjectures']}
    require('unique-conjecture-nodes', len(nodes) == len(c['conjectures']))
    require('known-conjecture-outcomes-match-port-intent', all(
        n.get('outcome') is None or n.get('attempted') is True
        and EXPECTED[n['outcome']][0] == ('prove' if n['outcome'][0] == '+' else 'reject')
        for n in nodes.values()))
    require('both-cost-fields-on-every-node', all(
        'cost_to_prove' in n and 'cost_to_reject' in n for n in nodes.values()))
    require('unattempted-is-not-failure-port', all(
        n.get('outcome') is not None or n.get('attempted') is False for n in nodes.values()))
    require('underdefined-global-node-excluded',
            nodes['ten-topic-joint-observable-relation']['scope_status'] == 'underdefined_not_in_solver'
            and nodes['ten-topic-joint-observable-relation']['scope_id'] is None)

    finite = json.loads((OWNER / 'results/joint-compatibility-free-completion.json').read_text())
    locality = json.loads((OWNER / 'results/tick-unitary-image-nonuniqueness.json').read_text())
    bridge = json.loads((OWNER / 'results/factorwise-locality-bridge.json').read_text())
    lift_attempt = json.loads((OWNER / 'results/source-to-local-lift-attempt.json').read_text())
    stochastic = json.loads((OWNER / 'results/tick-interpretation-nonuniqueness.json').read_text())
    unitary = json.loads((OWNER / 'results/tick-unitary-image-nonuniqueness.json').read_text())
    tick_classification = json.loads((OWNER / 'results/agda-TickRetainedStructure.json').read_text(encoding='utf-8-sig'))
    require('finite-completion-receipt-current-shape', finite['status'] == 'pass'
            and finite['checks_passed'] == 878
            and finite['classification'] == 'prediction-preserving-section-falsifies-strict-added-selection-in-declared-completion')
    for receipt_name, receipt, base in (
            ('finite', finite, REPO), ('locality', locality, OWNER), ('unitary', unitary, OWNER)):
        for relative, expected in receipt.get('source_sha256', {}).items():
            actual = hashlib.sha256((base / relative).read_bytes()).hexdigest()
            require(f'{receipt_name}-receipt-source-current/{relative}', actual == expected)
    require('selection-claim-recorded-as-successful-rejection',
            nodes['finite-compatibility-adds-selection']['outcome'] == '-+')
    require('completion-recorded-as-successful-proof',
            nodes['finite-prediction-preserving-completion']['outcome'] == '++')
    require('locality-is-only-named-rival-exclusion',
            'baseline-tensor-locality' in locality['checks']
            and 'rival-not-tensor-local' in locality['checks']
            and nodes['intermediate-locality-excludes-k2-rival']['outcome'] == '++')
    require('factorwise-locality-bridge-checker-current', bridge['status'] == 'pass'
            and bridge['check_count'] == 17
            and 'k2-countermodel-passes-current-class-and-fails-locality' in bridge['checks'])
    require('source-to-lift-proof-attempt-recorded-as-failed-proof-only',
            lift_attempt['status'] == 'partial_attempt_failed_to_prove_full_bridge'
            and lift_attempt['attempt_outcome'] == '+-'
            and lift_attempt['check_count'] == 26
            and nodes['source-derived-intermediate-locality-preserving-lift']['attempts'][0]['outcome'] == '+-'
            and lift_attempt['attempt_checker_sha256'] == hashlib.sha256(
                (OWNER / 'checkers/check_source_to_local_lift_attempt.py').read_bytes()).hexdigest())
    for relative, expected in lift_attempt['source_sha256'].items():
        require('lift-attempt-source-current/' + relative,
                hashlib.sha256((OWNER / relative).read_bytes()).hexdigest() == expected)
    require('discrete-source-locality-proved',
            nodes['native-discrete-factorwise-square']['outcome'] == '++'
            and nodes['native-discrete-factorwise-square']['scope_id'] == 'native-Bool-square')
    require('continuous-generator-locality-not-implied',
            nodes['declared-class-implies-factorwise-locality']['outcome'] == '-+'
            and bridge['exact_criterion'].endswith('iff k=0'))
    require('full-Tick-return-section-classification-current',
            tick_classification['passed'] and tick_classification['inputs_stable_during_check']
            and tick_classification['source_sha256'] == hashlib.sha256(
                (OWNER / 'agda/TickRetainedStructure.agda').read_bytes()).hexdigest()
            and nodes['full-bool-tick-has-independent-return-section-data']['outcome'] == '-+')
    require('stochastic-path-nonuniqueness-receipt', stochastic['status'] == 'pass'
            and len(stochastic['checks']) == 208
            and nodes['stochastic-tick-selects-path-up-to-reparameterization']['outcome'] == '-+')
    require('unitary-path-image-nonuniqueness-receipt', unitary['status'] == 'pass'
            and unitary['check_count'] == 384
            and 'ANY real angle pair' in unitary['rival_obstruction']
            and nodes['unitary-tick-selects-path-image-up-to-parameters-and-phase']['outcome'] == '-+')
    require('scoped-path-nonuniqueness-does-not-refute-new-lift',
            len(c['scope_constraints']) == 4
            and c['scope_constraints'][1]['id'] == 'path-nonuniqueness-is-scope-local')
    relation_obstruction = nodes['no-total-single-valued-return-correspondence']
    require('functional-return-correspondence-rejected-with-narrow-scope',
            relation_obstruction['outcome'] == '-+'
            and relation_obstruction['scope_status'] == 'typed_interface_obstruction'
            and 'multivalued' in relation_obstruction['disposition']
            and 'partial' in relation_obstruction['disposition']
            and c['scope_constraints'][2]['source_claim'] == relation_obstruction['id'])
    leg = json.loads((OWNER / 'results/return-leg-unitarity.json').read_text(encoding='utf-8'))
    require('return-leg-exact-test-passed', leg['status'] == 'pass'
            and leg['checks_passed'] == len(leg['checks']) == 32
            and leg['affine_midpoint_norm_squared'] == '1/2')
    for field, path in (
            ('source_sha256', 'agda/TickPolynomialRealization.agda'),
            ('checker_sha256', 'checkers/check_return_leg_unitarity.py'),
            ('proof_note_sha256', 'return-leg-unitarity.md')):
        require('return-leg-evidence-current/' + field,
                leg[field] == hashlib.sha256((OWNER / path).read_bytes()).hexdigest())
    require('return-leg-outcomes-scoped',
            nodes['affine-return-legs-are-unitary']['outcome'] == '-+'
            and nodes['spectral-return-legs-are-local-unitary']['outcome'] == '++'
            and nodes['affine-return-legs-are-unitary']['scope_id'] == 'current-affine-C4-return-legs'
            and nodes['spectral-return-legs-are-local-unitary']['scope_id'] == 'standard-complex-C4-spectral-return-legs')
    require('spectral-completion-bridge-still-open', any(
        gap['id'] == 'spectral-return-to-completion-phase'
        and gap['source_fact'] == 'spectral-return-legs-are-local-unitary'
        and gap['target_claim'] == 'source-derived-intermediate-locality-preserving-lift'
        and gap['status'] == 'missing_completion_phase_implementation'
        and gap['blocks_standard_complex_existence'] is False
        for gap in c['bridge_gaps']))
    norm_error = json.loads((OWNER / 'results/agda-TickPhaseNormError.json').read_text(encoding='utf-8'))
    require('phase-norm-perturbation-bound-Agda-checked',
            norm_error['status'] == 'pass' and norm_error['fresh_dependency_check']
            and norm_error['source_sha256'] == hashlib.sha256((OWNER / 'agda/TickPhaseNormError.agda').read_bytes()).hexdigest())
    series = json.loads((OWNER / 'results/phase-pythagorean-series.json').read_text(encoding='utf-8'))
    require('phase-series-exact-controls', series['status'] == 'pass'
            and series['checks_passed'] == len(series['checks']) == 305)
    for path, digest in series['source_sha256'].items():
        require('phase-series-evidence-current/' + path,
                hashlib.sha256((OWNER / path).read_bytes()).hexdigest() == digest)
    phase = json.loads((OWNER / 'results/agda-TickCompletionPhase.json').read_text(encoding='utf-8'))
    require('completion-phase-fragment-checked-full-test-open',
            phase['status'] == 'pass' and phase['fresh_dependency_check']
            and phase['source_sha256'] == hashlib.sha256((OWNER / 'agda/TickCompletionPhase.agda').read_bytes()).hexdigest()
            and phase['full_phase_test_outcome'] == '+-'
            and c['next_tests'][0]['completion_phase_attempt']['outcome'] == '+-')
    whole_return = json.loads((OWNER / 'results/agda-TickWholeReturnRealization.json').read_text(encoding='utf-8'))
    require('whole-Tick-return-construction-Agda-checked',
            whole_return['status'] == 'pass'
            and whole_return['fresh_dependency_check']
            and whole_return['source_sha256'] == hashlib.sha256(
                (OWNER / 'agda/TickWholeReturnRealization.agda').read_bytes()).hexdigest())
    return_agda = (OWNER / 'agda/TickLocalReturnSection.agda').read_text(encoding='utf-8')
    require('current-return-surface-tag-erasure-recorded-with-proof',
            nodes['current-return-surface-erases-schedule-tags']['outcome'] == '++'
            and 'return-target t = G.run G.leftFirst (src (B.D.extract t))' in return_agda
            and 'return-surface t a b = R.U a b (R.basis (return-target t))' in return_agda
            and 'cong (λ q → U a b (basis (run leftFirst q))) p' in
                (OWNER / 'return-correspondence-functional-obstruction.md').read_text(encoding='utf-8')
            and c['scope_constraints'][3]['source_claim'] == 'current-return-surface-erases-schedule-tags'
            and c['next_tests'][0]['id'] == 'whole-section-metric-realization-certificate'
            and c['next_tests'][0]['status'] == 'standard_external_return_proved_completion_refinement_open'
            and 'endpoint matching alone' in c['next_tests'][0]['scope_warning'].lower()
            and 'No pointwise selector' in
                (OWNER / 'whole-section-metric-realization-contract.md').read_text(encoding='utf-8'))

    relations = c['proof_relations']
    completion_relation = next(r for r in relations if r['id'] == 'completion-refutes-selection')
    require('same-scope-completion-refutation-link',
            completion_relation['premise'] == 'finite-prediction-preserving-completion'
            and completion_relation['premise_outcome'] == '++'
            and completion_relation['conclusion'] == 'finite-compatibility-adds-selection'
            and completion_relation['conclusion_outcome'] == '-+'
            and nodes[completion_relation['premise']]['scope_id'] == completion_relation['scope_id']
            == nodes[completion_relation['conclusion']]['scope_id'])
    locality_relation = next(r for r in relations if r['id'] == 'k2-counterexample-refutes-class-locality')
    require('k2-counterexample-scoped-refutation-link',
            locality_relation['premise'] == 'intermediate-locality-excludes-k2-rival'
            and locality_relation['conclusion'] == 'declared-class-implies-factorwise-locality'
            and locality_relation['conclusion_outcome'] == '-+'
            and nodes[locality_relation['conclusion']]['scope_id'] == locality_relation['scope_id'])
    split_receipt = json.loads((OWNER/'results/lift-outcome-split.json').read_text(encoding='utf-8'))
    require('conditional-split-schemas-fresh-checked',split_receipt['status']=='pass'
            and split_receipt['fresh_dependency_check'] and split_receipt['parent_truth_established'] is False)
    for path,digest in split_receipt['source_sha256'].items():
        require('conditional-split-evidence-current/'+path,hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    parent = c['lift_outcome_split']['parent']
    require('conditional-split-parent-is-full-lift',parent=='source-derived-intermediate-locality-preserving-lift')
    split_rows=[]
    for branch,node_id,required,edge_id in (
            ('positive','full-lift-proof-implies-local-core','++','parent-proof-activates-local-core-branch'),
            ('negative','full-lift-rejection-obstructs-return-extension','-+','parent-rejection-activates-return-obstruction-branch')):
        node=nodes[node_id]; edge=next(r for r in relations if r['id']==edge_id)
        require('conditional-split-scope/'+branch,node['scope_id']==nodes[parent]['scope_id']==edge['scope_id']
                and node['scope_status']=='typed_conditional_logical_schema' and node['outcome']=='++')
        require('conditional-split-gate/'+branch,node['assumption']=={'parent':parent,'required_outcome':required}
                and edge['premise']==parent and edge['premise_outcome']==required and edge['conclusion']==node_id
                and edge['relation']=='conditional_branch_activation' and edge['conclusion_kind']=='activate_consequent_not_prove_schema')
        for outcome in (None,'++','+-','-+','--'):
            require('conditional-split-truth-table/'+branch+'/'+str(outcome),
                    active_branches(outcome)[branch]==(outcome==edge['premise_outcome']))
        split_rows.append({'node':node_id,'schema_outcome':node['outcome'],'requires_parent_outcome':required,
                           'consequent':node['consequent'],'consequent_active':active_branches(nodes[parent]['outcome'])[branch]})
    require('proved-parent-activates-only-positive-branch',[row['consequent_active'] for row in split_rows]==[True,False])
    gap = next(g for g in c['bridge_gaps'] if g['id'] == 'discrete-square-to-continuous-local-lift')
    require('discrete-to-continuous-lift-constructed-in-standard-semantics',
            gap['source_fact'] == 'native-discrete-factorwise-square'
            and gap['target_claim'] == 'source-derived-intermediate-locality-preserving-lift'
            and gap['status'] == 'constructed_standard_complex_core')
    route = c['conditional_route']
    require('locality-route-does-not-promote-source-authority',
            route['status'] == 'local_realization_exists_rival_exclusion_remains_class_relative'
            and route['conclusion_scope'] == 'excludes-the-named-k2-rival-only'
            and 'uniqueness or a universal observable law' in route['does_not_establish'])
    require('no-inferred-ten-topic-edge', not any(
        x.get('premise') == 'ten-topic-joint-observable-relation'
        or x.get('conclusion') == 'ten-topic-joint-observable-relation'
        for x in relations))

    typed = [n for n in nodes.values() if n['scope_status'] != 'underdefined_not_in_solver']
    open_typed = [n for n in typed if n.get('outcome') is None or n.get('outcome') in ('+-', '--')]
    core_information=json.loads((OWNER/'results/local-core-information.json').read_text(encoding='utf-8'))
    require('local-core-information-no-invented-joint-prior',core_information['status']=='pass'
            and core_information['free_parameter']['value'] is None
            and core_information['net_entropy_identified'] is True and core_information['observational_update'] is True)
    require('same-witness-return-proof-leaves-one-world',len(core_information['possible_worlds'])==1
            and all(w['local_core_exists'] for w in core_information['possible_worlds'])
            and all(not w['full_lift_exists'] or w['local_core_exists'] for w in core_information['possible_worlds'])
            and all(w['universal_return_obstruction']==(not w['full_lift_exists']) for w in core_information['possible_worlds']))
    for path,digest in core_information['source_sha256'].items():
        require('local-core-information-current/'+path,hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    core_id='source-derived-local-core-exists'
    require('clarified-existence-claims-closed',not open_typed)
    core=nodes[core_id]
    local_proof=json.loads((OWNER/'results/uniform-local-core.json').read_text(encoding='utf-8'))
    require('local-core-proof-with-analytic-boundary',core['outcome']=='++' and core['attempted']
            and 'assumption' not in core and local_proof['status']=='pass'
            and local_proof['phase_is_constructor_output_not_input']
            and local_proof['completion_backend_verified'] is False and local_proof['whole_tick_return_verified'] is False
            and core['test_readiness']=='proved_standard_complex_core')
    require('uniform-construction-meaning-shared-with-parent',set(c['source_derivation_policy']['applies_to'])=={parent,core_id}
            and c['source_derivation_policy']['meaning']=='uniform-construction-existence-not-source-uniqueness')
    for path,digest in local_proof['source_sha256'].items():
        require('uniform-local-core-current/'+path,hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    for edge_id,premise,port,conclusion,result in (
            ('full-lift-proof-entails-standalone-local-core',parent,'++',core_id,'++'),
            ('local-core-rejection-refutes-full-lift',core_id,'-+',parent,'-+')):
        edge=next(r for r in relations if r['id']==edge_id)
        require('local-core-inference/'+edge_id,edge['premise']==premise and edge['premise_outcome']==port
                and edge['conclusion']==conclusion and edge['conclusion_outcome']==result
                and edge['scope_id']==core['scope_id']==nodes[parent]['scope_id'])
    for outcome in (None,'++','+-','-+','--'):
        effects=local_core_consequences(outcome)
        require('local-core-routing/'+str(outcome),effects['parent_rejection']==(outcome=='-+')
                and effects['witness_return_test_enabled']==(outcome=='++') and effects['parent_proof'] is False)
    require('local-core-alone-does-not-close-parent',
            local_core_consequences(core['outcome'])=={'parent_rejection':False,'witness_return_test_enabled':True,'parent_proof':False})
    extension_id='spectral-local-core-admits-whole-tick-return'
    extension=json.loads((OWNER/'results/spectral-whole-return.json').read_text(encoding='utf-8'))
    require('same-witness-return-proves-clarified-parent',nodes[extension_id]['outcome']==nodes[parent]['outcome']=='++'
            and extension['status']=='pass' and extension['witness']==local_proof['witness']
            and extension['completion_backend_verified'] is False
            and extension['cubical_pointwise_decoder_constructed'] is False)
    intro=next(r for r in relations if r['id']=='same-witness-core-and-return-prove-full-lift')
    require('same-witness-introduction-edge',intro['premises']==[core_id,extension_id]
            and intro['premise_outcomes']==['++','++'] and intro['conclusion']==parent and intro['conclusion_outcome']=='++')
    for path,digest in extension['source_sha256'].items():
        require('spectral-whole-return-current/'+path,hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    require('same-witness-return-obligation-explicit','same witnessed f' in c['local_core_test_route']['required_to_close_parent'])
    for n in nodes.values():
        for path in n.get('evidence', []):
            require('evidence-path-exists/' + path, (REPO / path).is_file())
    weights = json.loads((OWNER/'results/taylor-binomial-weights-cached.json').read_text(encoding='utf-8'))
    require('binomial-weights-cached-only-coefficient-sum-open',weights['status']=='pass'
            and weights['fresh_dependency_check'] is False and weights['leibniz_coefficient_sum_identification_proved'] is False
            and weights['vanishing_norm_defect_proved'] is False)
    for path,digest in weights['source_sha256'].items():
        require('binomial-weights-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    weights_fresh = json.loads((OWNER/'results/taylor-binomial-weights.json').read_text(encoding='utf-8'))
    require('binomial-fresh-timeout-retained',weights_fresh['status']=='timeout'
            and weights_fresh['source_sha256']['agda/TickTaylorBinomialWeights.agda']==weights['source_sha256']['agda/TickTaylorBinomialWeights.agda'])
    degrees = json.loads((OWNER/'results/taylor-degree-regrouping.json').read_text(encoding='utf-8'))
    require('degree-regrouping-checked-weight-identification-open',degrees['status']=='pass'
            and degrees['fresh_dependency_check'] and degrees['factorial_binomial_identification_proved'] is False
            and degrees['vanishing_norm_defect_proved'] is False)
    for path,digest in degrees['source_sha256'].items():
        require('taylor-degree-regrouping-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    expansion = json.loads((OWNER/'results/taylor-product-expansion.json').read_text(encoding='utf-8'))
    require('finite-taylor-products-checked-diagonal-transfer-open',expansion['status']=='pass'
            and expansion['fresh_dependency_check'] and expansion['diagonal_leibniz_bridge_proved'] is False
            and expansion['vanishing_norm_defect_proved'] is False)
    for path,digest in expansion['source_sha256'].items():
        require('taylor-product-expansion-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    normalization = json.loads((OWNER/'results/trig-taylor-normalization.json').read_text(encoding='utf-8'))
    require('operational-term-normalization-checked-product-open',normalization['status']=='pass'
            and normalization['fresh_dependency_check'] and normalization['product_convolution_bridge_proved'] is False
            and normalization['vanishing_norm_defect_proved'] is False)
    for path,digest in normalization['source_sha256'].items():
        require('trig-term-normalization-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    cancellation = json.loads((OWNER/'results/trig-coefficient-cancellation.json').read_text(encoding='utf-8'))
    require('all-order-coefficient-cancellation-checked-transfer-open',cancellation['status']=='pass'
            and cancellation['fresh_dependency_check'] and cancellation['operational_taylor_coefficient_bridge_proved'] is False
            and cancellation['vanishing_norm_defect_proved'] is False)
    for path,digest in cancellation['source_sha256'].items():
        require('coefficient-cancellation-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    common = json.loads((OWNER/'results/common-taylor-controls.json').read_text(encoding='utf-8'))
    require('common-taylor-controls-checked-norm-defect-open',common['status']=='pass'
            and common['fresh_dependency_check'] and common['control_norm_defect_proved'] is False
            and common['eventual_sample_controls_inhabited'] is False)
    for path,digest in common['source_sha256'].items():
        require('common-taylor-controls-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    control = json.loads((OWNER/'results/scheduled-norm-control.json').read_text(encoding='utf-8'))
    require('actual-schedule-controls-checked-bound-still-open',control['status']=='pass'
            and control['fresh_dependency_check'] and control['eventual_controls_constructed'] is False
            and control['scheduled_norm_bound_instantiated'] is False)
    for path,digest in control['source_sha256'].items():
        require('actual-schedule-control-evidence-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    locality = json.loads((OWNER / 'results/relative-locality.json').read_text(encoding='utf-8'))
    require('relative-locality-covariance-checked-not-analytic-closure',locality['status']=='pass'
            and locality['fresh_dependency_check'] and locality['original_source_lift_closed'] is False
            and locality['full_analytic_interface_instantiated'] is False
            and c['next_tests'][0]['relative_source_contract']['locality_covariance']['outcome']=='++')
    for path,digest in locality['source_sha256'].items():
        require('relative-locality-evidence-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    relative = json.loads((OWNER / 'results/relative-source-contract.json').read_text(encoding='utf-8'))
    require('relative-source-contract-checked-without-scope-promotion', relative['status']=='pass'
            and relative['fresh_dependency_check'] and relative['original_source_lift_closed'] is False
            and relative['full_analytic_interface_instantiated'] is False
            and relative['whole_path_contract_instantiated'] is False
            and c['next_tests'][0]['relative_source_contract']['original_planner_token_unlocked'] is False)
    for path,digest in relative['source_sha256'].items():
        require('relative-source-evidence-current/'+path,
                hashlib.sha256((OWNER/path).read_bytes()).hexdigest()==digest)
    audit = json.loads((OWNER / 'results/source-contract-audit.json').read_text(encoding='utf-8'))
    require('source-contract-audit-fresh-checked', audit['status']=='pass' and audit['fresh_dependency_check']
            and audit['source_sha256']==hashlib.sha256((OWNER/'agda/TickSourceContractAudit.agda').read_bytes()).hexdigest())
    require('source-contract-audit-does-not-unlock-or-refute-lift', audit['audit_stage_outcome']=='+-'
            and audit['source_contract_unlocked'] is False and audit['lift_refuted'] is False
            and c['next_tests'][0]['source_contract_audit']['outcome']=='+-')
    closure = json.loads((OWNER / 'results/closure-planning.json').read_text(encoding='utf-8'))
    require('observed-audit-triggers-replan', closure['decision_status']=='replan_required_after_observed_attempt'
            and closure['central']['first_action'] is None)
    require('closure-objective-not-local-information',
            c['closure_planning']['engine'] == 'research/conjecture_net/interpretation_planner.py'
            and closure['status'] == 'pass' and closure['planning_only'] is True
            and closure['objective']['functional'] == 'reachability_then_expected_cost')
    require('closure-engines-agree', closure['central']['first_action'] == closure['central']['objective_projection']['action'])
    for path, digest in closure['source_sha256'].items():
        require('closure-planning-evidence-current/' + path,
                hashlib.sha256((REPO / path).read_bytes()).hexdigest() == digest)
    planning = json.loads((OWNER / 'results/bridge-planning.json').read_text(encoding='utf-8'))
    require('bridge-planning-linked-and-non-evidential',
            c['bridge_planning']['status'] == planning['estimate_status'] == 'subjective_uncalibrated_planning_only'
            and planning['status'] == 'pass' and planning['global_optimum_established'] is False)
    require('bridge-planning-six-directional-actions', len(planning['conditional_ranking']) == 6
            and all(row['ready'] for row in planning['ready_ranking']))
    require('bridge-planning-sensitivity-accounting',
            sum(planning['scenario_winner_counts'].values()) == planning['scenario_count'])
    for path, digest in planning['source_sha256'].items():
        require('bridge-planning-evidence-current/' + path,
                hashlib.sha256((OWNER / path).read_bytes()).hexdigest() == digest)
    model = c['cost_model']
    open_node = nodes[parent]
    require('provisional-costs-only-on-open-claim',
            all(n.get('cost_to_prove') is None and n.get('cost_to_reject') is None
                for n in nodes.values() if n['id'] != open_node['id'])
            and open_node['cost_to_prove'] == 3 and open_node['cost_to_reject'] == 6
            and model['unit'] == 'assistant_effort_unit')
    probabilities = model['probabilities']
    require('four-outcome-likelihoods-normalized-and-sound',
            probabilities['status'] == 'provisional_subjective_prior_updated_after_one_attempt'
            and abs(sum(probabilities['conditional_outcomes']['prove']['if_claim_true'].values()) - 1) < 1e-12
            and abs(sum(probabilities['conditional_outcomes']['prove']['if_claim_false'].values()) - 1) < 1e-12
            and abs(sum(probabilities['conditional_outcomes']['reject']['if_claim_true'].values()) - 1) < 1e-12
            and abs(sum(probabilities['conditional_outcomes']['reject']['if_claim_false'].values()) - 1) < 1e-12
            and probabilities['conditional_outcomes']['prove']['if_claim_false']['++'] == 0
            and probabilities['conditional_outcomes']['reject']['if_claim_true']['-+'] == 0)
    prior = probabilities['claim_prior_probability']
    initial_prior = probabilities['initial_claim_prior_probability']
    expected_posterior = initial_prior * 0.45 / (initial_prior * 0.45 + (1 - initial_prior))
    require('prior-updated-from-failed-proof-attempt',
            abs(prior - expected_posterior) < 1e-9
            and nodes[open_node['id']]['attempted'] is True
            and nodes[open_node['id']]['attempts'][0]['outcome'] == '+-')
    entropy = lambda p: 0.0 if p in (0, 1) else -p*__import__('math').log2(p) - (1-p)*__import__('math').log2(1-p)
    p_proved = prior * probabilities['conditional_outcomes']['prove']['if_claim_true']['++']
    p_prove_fail = 1 - p_proved
    post_true_after_prove_fail = prior * (1 - probabilities['conditional_outcomes']['prove']['if_claim_true']['++']) / p_prove_fail
    ig_prove = entropy(prior) - p_prove_fail * entropy(post_true_after_prove_fail)
    p_rejected = (1-prior) * probabilities['conditional_outcomes']['reject']['if_claim_false']['-+']
    p_reject_fail = 1 - p_rejected
    post_true_after_reject_fail = prior / p_reject_fail
    ig_reject = entropy(prior) - p_reject_fail * entropy(post_true_after_reject_fail)
    rate_prove = ig_prove / open_node['cost_to_prove']
    rate_reject = ig_reject / open_node['cost_to_reject']
    require('provisional-information-per-cost-ranks-proof-attempt-first',
            model['selection_objective'] == 'expected_information_gain_bits_per_assistant_effort_unit'
            and rate_prove > rate_reject > 0)

    sources = [Path(__file__).resolve(), CONTRACT,
               OWNER / 'agda/TickLiftOutcomeSplit.agda',
               OWNER / 'checkers/check_lift_outcome_split.py',
               OWNER / 'results/lift-outcome-split.json',
               OWNER / 'lift-outcome-split.md',
               OWNER / 'local-core-test.md',
               OWNER / 'contracts/uniform-local-core-test.v1.json',
               OWNER / 'uniform-local-core-proof.md',
               OWNER / 'checkers/check_uniform_local_core.py',
               OWNER / 'results/uniform-local-core.json',
               OWNER / 'contracts/spectral-whole-return-test.v1.json',
               OWNER / 'spectral-whole-return-proof.md',
               OWNER / 'checkers/check_spectral_whole_return.py',
               OWNER / 'results/spectral-whole-return.json',
               OWNER / 'local-core-information.md',
               OWNER / 'checkers/check_local_core_information.py',
               OWNER / 'results/local-core-information.json',
               OWNER / 'contracts/current-problem-closure-planning.v1.json',
               OWNER / 'checkers/check_closure_planning.py',
               OWNER / 'checkers/test_closure_planning.py',
               OWNER / 'results/closure-planning.json',
               OWNER / 'closure-planning-remediation.md',
               OWNER / 'agda/TickSourceContractAudit.agda',
               OWNER / 'checkers/check_source_contract_audit.py',
               OWNER / 'source-contract-audit.md',
               OWNER / 'relative-source-derivation.md',
               OWNER / 'agda/TickScheduledNormControl.agda',
               OWNER / 'checkers/check_scheduled_norm_control.py',
               OWNER / 'results/scheduled-norm-control.json',
               OWNER / 'scheduled-norm-control.md',
               OWNER / 'agda/TickTaylorBinomialWeights.agda',
               OWNER / 'checkers/check_taylor_binomial_weights.py',
               OWNER / 'results/taylor-binomial-weights-cached.json',
               OWNER / 'results/taylor-binomial-weights.json',
               OWNER / 'agda/TickTaylorDegreeRegrouping.agda',
               OWNER / 'checkers/check_taylor_degree_regrouping.py',
               OWNER / 'results/taylor-degree-regrouping.json',
               OWNER / 'agda/TickTaylorProductExpansion.agda',
               OWNER / 'checkers/check_taylor_product_expansion.py',
               OWNER / 'results/taylor-product-expansion.json',
               OWNER / 'agda/TickTrigTaylorNormalization.agda',
               OWNER / 'checkers/check_trig_taylor_normalization.py',
               OWNER / 'results/trig-taylor-normalization.json',
               OWNER / 'agda/TickTrigCoefficientCancellation.agda',
               OWNER / 'checkers/check_trig_coefficient_cancellation.py',
               OWNER / 'results/trig-coefficient-cancellation.json',
               OWNER / 'agda/TickCommonTaylorControls.agda',
               OWNER / 'checkers/check_common_taylor_controls.py',
               OWNER / 'results/common-taylor-controls.json',
               OWNER / 'agda/TickRelativeLocality.agda',
               OWNER / 'checkers/check_relative_locality.py',
               OWNER / 'results/relative-locality.json',
               OWNER / 'contracts/relative-source-derivation.v1.json',
               OWNER / 'agda/TickRelativeSourceContract.agda',
               OWNER / 'checkers/check_relative_source_contract.py',
               OWNER / 'results/relative-source-contract.json',
               OWNER / 'results/source-contract-audit.json',
               OWNER / 'contracts/current-problem-bridge-planning.v1.json',
               OWNER / 'checkers/check_bridge_planning.py',
               OWNER / 'results/bridge-planning.json',
               OWNER / 'bridge-planning.md',
               OWNER / 'scc-models/current-problem-conjecture-net.json',
               OWNER / 'current-problem-conjecture-net.md',
               REPO / 'research/conjecture_net/interpretation_planner.py',
               REPO / 'research/conjecture_net/coherence_pyramid.py',
               REPO / 'research/conjecture_net/composite_arrow_tests.py',
               REPO / 'research/conjecture_net/path_polarity_constraints.py',
               REPO / 'research/conjecture_replay/results/del_pezzo_cost_model.json',
               OWNER / 'results/joint-compatibility-free-completion.json',
               OWNER / 'results/tick-unitary-image-nonuniqueness.json',
               OWNER / 'checkers/check_factorwise_locality_bridge.py',
               OWNER / 'results/factorwise-locality-bridge.json',
               OWNER / 'checkers/check_source_to_local_lift_attempt.py',
               OWNER / 'results/source-to-local-lift-attempt.json',
               OWNER / 'return-correspondence-functional-obstruction.md',
               OWNER / 'whole-section-metric-realization-contract.md',
               OWNER / 'return-leg-unitarity.md',
               OWNER / 'phase-pythagorean-series.md',
               OWNER / 'agda/TickPhaseNormError.agda',
               OWNER / 'checkers/check_phase_norm_error.py',
               OWNER / 'results/agda-TickPhaseNormError.json',
               OWNER / 'checkers/check_phase_pythagorean_series.py',
               OWNER / 'results/phase-pythagorean-series.json',
               OWNER / 'agda/TickCompletionPhase.agda',
               OWNER / 'results/agda-TickCompletionPhase.json',
               OWNER / 'checkers/check_completion_phase.py',
               OWNER / 'checkers/check_return_leg_unitarity.py',
               OWNER / 'results/return-leg-unitarity.json',
               OWNER / 'agda/TickWholeReturnRealization.agda',
               OWNER / 'results/agda-TickWholeReturnRealization.json',
               OWNER / 'agda/TickLocalReturnSection.agda',
               OWNER / 'tick-full-structure-classification.md',
               OWNER / 'tick-admissible-interpretations.md',
               OWNER / 'results/agda-TickRetainedStructure.json',
               OWNER / 'results/tick-interpretation-nonuniqueness.json',
               OWNER / 'tick-unitary-image-nonuniqueness.md',
               OWNER / 'results/tick-unitary-image-nonuniqueness.json']
    result = {
        'schema': 'marici.nima.current-problem-proof-outcome-net-result.v1',
        'status': 'pass',
        'checks_passed': len(CHECKS),
        'proof_outcomes': {k: {'intent': v[0], 'result': v[1]} for k, v in EXPECTED.items()},
        'typed_conjectures': len(typed),
        'conditional_logical_schemas': sum(n['scope_status']=='typed_conditional_logical_schema' for n in typed),
        'local_core_information': {'net_entropy_identified':True,'joint_parameter_elicited':False,'current_proved_pair_entropy_bits':0,
                                   'possible_world_count':len(core_information['possible_worlds']),
                                   'details':c['lift_outcome_split']['information_diagnostic']['result']},
        'lift_outcome_split': {'parent':parent,'parent_outcome':nodes[parent]['outcome'],'branches':split_rows},
        'recorded_outcomes': sum(n.get('outcome') is not None for n in typed),
        'next_unresolved_conjecture': None,
        'unresolved_conjectures': [n['id'] for n in open_typed],
        'standalone_local_core_test': {'node':core_id,'outcome':core['outcome'],'readiness':core['test_readiness'],
                                      'effects':local_core_consequences(core['outcome'])},
        'next_tests': c['next_tests'],
        'last_attempt': {'conjecture_id': extension_id,
                          'intent': 'prove', 'outcome': '++',
                          'scope_note': 'Faithful external whole-Tick return for the same standard-C4 witness. Operational completion and pointwise Cubical decoding are not claimed.'},
        'lift_attempt_effort_units_spent_estimate': lift_attempt['effort_units_spent_estimate'],
        'potential_next_attempts': [],
        'optimizer': {
            'status': 'clarified_standard_complex_existence_goal_proved_historical_portfolio_stopped',
            'historical_portfolio_status': closure['decision_status'],
            'engine': c['closure_planning']['engine'],
            'selection_objective': closure['objective'],
            'recommended_first_action': None,
            'structural_next_test': None,
            'separate_open_refinement': 'operational-completion-backend',
            'expected_total_effort': None,
            'success_probability': None,
            'stable_in_tested_scenarios': closure['stable_in_tested_scenarios'],
            'global_optimum_established': False,
            'details': c['closure_planning']['result'],
        },
        'historical_single_claim_information_diagnostic': {
            'status': 'non_authoritative_for_closure',
            'reason': 'historical uncalibrated local-information model; superseded for closure decisions',
            'selection_objective': model['selection_objective'],
            'prior_claim_probability': prior,
            'actions': {
                'prove': {'cost_effort_units': open_node['cost_to_prove'],
                          'expected_information_gain_bits': round(ig_prove, 4),
                          'gain_per_effort_unit': round(rate_prove, 4),
                          'outcome_probabilities': {'++': round(p_proved, 4), '+-': round(p_prove_fail, 4)}},
                'reject': {'cost_effort_units': open_node['cost_to_reject'],
                           'expected_information_gain_bits': round(ig_reject, 4),
                           'gain_per_effort_unit': round(rate_reject, 4),
                           'outcome_probabilities': {'-+': round(p_rejected, 4), '--': round(p_reject_fail, 4)}}
            },
            'recommended_first_action': 'prove',
        },
        'critical_paths': [
            {'id': 'finite-refutation', 'status': 'verified',
             'nodes': ['finite-prediction-preserving-completion', 'finite-compatibility-adds-selection'],
             'ports': ['++', '-+'], 'scope_id': relations[0]['scope_id']},
            {'id': 'conditional-locality-selector', 'status': 'local-realization-proved-exclusion-class-relative',
             'nodes': ['source-derived-intermediate-locality-preserving-lift', 'intermediate-locality-excludes-k2-rival'],
             'boundary': 'existence of a factor-local realization is proved; source necessity or uniqueness of that realization is not',
             'ceiling': 'named rival only'},
            {'id': 'factorwise-locality-test', 'status': 'verified-counterexample-to-current-class-entailment',
             'nodes': ['native-discrete-factorwise-square', 'declared-class-implies-factorwise-locality'],
             'ports': ['++', '-+'], 'counterexample': 'k=2'},
            {'id': 'prior-path-nonuniqueness', 'status': 'verified-in-separate-classes',
             'nodes': ['stochastic-tick-selects-path-up-to-reparameterization',
                       'unitary-tick-selects-path-image-up-to-parameters-and-phase'],
             'ports': ['-+', '-+']},
            {'id': 'functional-return-correspondence-obstruction',
             'status': 'verified-within-narrow-Cubical-state-correspondence-scope',
             'nodes': ['no-total-single-valued-return-correspondence',
                       'source-derived-intermediate-locality-preserving-lift'],
             'ports': ['-+'], 'limitation': 'does not refute the now-constructed external metric whole-record interpretation'},
            {'id': 'schedule-tag-fidelity-gap', 'status': 'verified-for-current-surface-only',
             'node': 'current-return-surface-erases-schedule-tags',
             'replacement': 'spectral-local-core-admits-whole-tick-return',
             'limitation': 'does not establish that every valid lift must be tag-sensitive'},

            {'id': 'return-leg-unitarity-replacement', 'status': 'matrix-theorem-proved-completion-bridge-open',
             'nodes': ['affine-return-legs-are-unitary', 'spectral-return-legs-are-local-unitary'],
             'ports': ['-+', '++'],
             'blocker': 'complex completion phase, continuity, and generator compatibility'},
            {'id': 'ten-topic-integration', 'status': 'not-yet-typed',
             'blocker': 'shared carrier, cross-topic maps, equations, observable, costs'},
        ],
        'cost_model_finding': c['cost_model']['legacy_finding'],
        'scope': 'standard-C4 uniform local-core and faithful external whole-return existence proved; operational completion, source uniqueness and ten-topic interpretation remain outside this closure',
        'source_sha256': {p.relative_to(REPO).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in sources},
    }
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in (
        'status', 'checks_passed', 'typed_conjectures', 'recorded_outcomes',
        'next_unresolved_conjecture', 'optimizer', 'critical_paths')}, indent=2))


if __name__ == '__main__':
    main()
