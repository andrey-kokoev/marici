"""Validate revision 32: scoped fresh constructions and the candidate coherence theorem."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.conjecture_net.outcome_reference import PORTS, SEMANTICS
from check_ramsey_coherence_progress import RESULT_IDS as V32_RESULT_IDS, OPEN_IDS as V32_OPEN_IDS, validate as validate_coherence_progress

CONTRACT = 'research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json'
MANIFEST = 'research/voevodsky/scc-models/ramsey-tetrahedral-octahedral-net-v1.json'
RESULT = 'research/voevodsky/results/ramsey-tetrahedral-octahedral-net-v32.json'
V31_PRIOR_IDS = {'prior-local-metric-based-branch-lift', 'prior-completed-twelve-port-metric-route', 'prior-patch-Gram-shape-obstruction', 'prior-axial-polarity-constructor-boundary', 'prior-native-conditional-PN-patch-transport'}
V31_OPEN_IDS = {'T-seam-based-port-readout-binding'}
V30_PRIOR_IDS = {'prior-marked-P-field-attachment', 'prior-co-moving-N-reader-interface', 'prior-geometric-five-column-seed', 'prior-field-binding-convention-obstructions', 'prior-face-return-extension-obstructions'}
V30_OPEN_IDS = {'T-seam-marked-face-patch-sector-transport'}
V29_PRIOR_IDS = {'prior-joint-field-readout-sewing', 'prior-direction-indexed-reverse-validator', 'prior-native-reader-comparison-boundary', 'prior-reconstruction-aware-reference-change'}
V29_OPEN_IDS = {'T-seam-joint-field-readout-binding', 'dual-field-reverse-policy-compatibility'}
PRIOR_IDS = {'prior-moving-reference-seam', 'prior-fixed-coordinate-reversal-coherence', 'prior-dual-basis-native-numeric-binding'} | V29_PRIOR_IDS | V30_PRIOR_IDS | V31_PRIOR_IDS
NEW_OPEN_IDS = {'dual-reference-native-readout-binding', 'reversed-boundary-source-admission', 'admitted-reversal-overlap-coherence'} | V29_OPEN_IDS | V30_OPEN_IDS | V31_OPEN_IDS
NODE_IDS = {
    'space-admission', 'finite-certificate-interface', 'uniform-vertex-bound',
    'native-forcing-construction', 'reference-covariance',
    'pilot-native-assembly', 'graph-hypergraph-scope-extension',
    'plane-lattice-realization', 'fixed-scale-cell-forcing', 'marked-dilation-patch',
    'native-word-history-lift', 'endpoint-cache-query-descent',
    'native-query-selection', 'native-task-package-lift', 'single-leaf-query-completeness',
    'native-region-family-admission', 'native-word-family-selection', 'native-family-refinement-transport',
    'single-frame-full-face-admission', 'face-chart-transition-descent',
    'fixed-geometry-total-PN-domain-transport', 'overlap-restricted-native-PN-span',
    'native-retained-four-facet-correspondence',
} | PRIOR_IDS | NEW_OPEN_IDS | V32_RESULT_IDS | V32_OPEN_IDS
QUANTIFIER = ('For every r>=1 and finite nonempty S subset L, there exists a finite B(r,S) '
              'such that every coloring c:L_B -> {0,...,r-1} admits a in L and integer '
              'm>=1 with a+m*S subset L_B and c constant on a+m*S.')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def artifact(relative):
    require(isinstance(relative, str) and bool(relative), 'missing artifact path')
    path = (ROOT / relative).resolve()
    require(not Path(relative).is_absolute() and path.is_relative_to(ROOT), 'artifact escapes repository')
    require(path.is_file(), 'missing artifact: ' + relative)
    return path


def validate_interface(net, node):
    require(node['status'] == 'resolved' and node['outcome'] == '++', 'interface outcome')
    require(len(node['attempts']) == 1, 'interface attempt history')
    attempt = node['attempts'][0]
    require(attempt['intent'] == 'prove' and attempt['outcome'] == '++', 'attempt intent/outcome')
    require(attempt['scope_id'] == node['scope_id'], 'attempt scope mismatch')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'claim digest')
    receipt_path = artifact(attempt['receipt'])
    require(sha256(receipt_path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'receipt digest')
    receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-certificate-interface.verification.v1', 'receipt schema')
    require(receipt['status'] == 'passed' and receipt['outcome'] == '++', 'receipt outcome')
    require(receipt['scope_id'] == node['scope_id'], 'receipt scope')
    require(receipt['verification_level'] == attempt['verification_level'], 'verification upgrade')
    require(len(receipt['accepted_fixtures']) == 8 and len(receipt['rejected_controls']) == 44, 'fixture coverage')
    require(receipt['oracle']['certificate_comparisons'] == 65536, 'oracle coverage')
    require(receipt['template_bindings'] == {k: net['candidate_space'][k] for k in ('tetrahedron', 'octahedron')}, 'template drift')
    for key in ('uniform_existence_proved', 'native_source_admitted', 'native_histories_verified', 'root_resolved'):
        require(receipt[key] is False, 'out-of-scope promotion')
    require(set(receipt['source_sha256']) == {
        'research/voevodsky/ramsey_certificate.py',
        'research/voevodsky/ramsey-certificate-interface-v1.md',
        'research/voevodsky/checkers/check_ramsey_certificate_interface.py'}, 'missing source pins')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale interface evidence')
    artifact(attempt['freeze'])


def validate_plane_result(net, node):
    expected = '++' if node['id'] == 'plane-lattice-realization' else '-+'
    require(node['status'] == 'resolved' and node['outcome'] == expected, 'geometric result outcome')
    require(len(node['attempts']) == 1, 'geometric attempt history')
    attempt = node['attempts'][0]
    require(attempt['outcome'] == expected and attempt['intent'] == PORTS[expected]['attempt'], 'geometric attempt intent')
    require(attempt['scope_id'] == node['scope_id'], 'geometric attempt scope')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'geometric claim digest')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'geometric receipt digest')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-plane-lattice.verification.v1' and receipt['status'] == 'passed', 'geometric receipt status')
    require(receipt['outcomes'][node['id']] == {'scope_id': node['scope_id'], 'outcome': expected}, 'geometric receipt scope/outcome')
    level = 'written all-index proofs and exact rational/integer controls; not kernel verified'
    require(receipt['verification_level'] == attempt['verification_level'] == level, 'geometric verification upgrade')
    require(attempt['evidence_group'] == 'ramsey-plane-lattice-v1', 'shared evidence split')
    require(receipt['template_bindings'] == {k: net['candidate_space'][k] for k in ('tetrahedron', 'octahedron')}, 'geometric template drift')
    require(receipt['triple_intersections_checked'] == 500 and receipt['parity_split_chambers_checked'] == 200, 'geometric control coverage')
    for key in ('dilations_are_cell_automorphisms', 'homogeneous_template_implies_homogeneous_subdivision',
                'native_source_operations_admitted', 'dilation_allowing_pilot_refuted',
                'uniform_Ramsey_bound_proved', 'root_resolved'):
        require(receipt[key] is False, 'geometric overclaim')
    require(set(receipt['source_sha256']) == {
        'research/voevodsky/contracts/ramsey-plane-lattice-attempt.v1.json',
        'research/voevodsky/ramsey-plane-lattice-realization-v1.md',
        'research/voevodsky/checkers/check_ramsey_plane_lattice.py',
        'research/strominger/tetrahedral-plane-lattice-universal-witness-conjectures-v1.md'}, 'geometric source pins')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale geometric evidence')
    prospective = json.loads(artifact('research/voevodsky/contracts/ramsey-plane-lattice-attempt.v1.json').read_text(encoding='utf-8'))
    claim = next(c for c in prospective['claims'] if c['id'] == node['id'])
    require(claim['statement'] == node['statement'] and claim['scope_id'] == node['scope_id'], 'prospective scope changed')
    artifact(attempt['freeze'])


def validate_marked_patch(net, node):
    require(node['status'] == 'resolved' and node['outcome'] == '++', 'patch outcome')
    require(len(node['attempts']) == 1, 'patch attempt history')
    attempt = node['attempts'][0]
    require(attempt['intent'] == 'prove' and attempt['outcome'] == '++', 'patch attempt intent')
    require(attempt['scope_id'] == node['scope_id'], 'patch attempt scope')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'patch claim digest')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'patch receipt digest')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-marked-patch.verification.v1' and receipt['status'] == 'passed', 'patch receipt schema/status')
    require(receipt['scope_id'] == node['scope_id'] and receipt['outcome'] == '++', 'patch receipt scope/outcome')
    level = 'written geometric construction and exact-safe source-API controls; not native packet admission or kernel verified'
    require(receipt['verification_level'] == attempt['verification_level'] == level, 'patch verification upgrade')
    require((receipt['patch_cases'], receipt['composition_cases'], receipt['negative_controls']) == (27, 9, 10), 'patch control coverage')
    require(receipt['source_primitive_neighbor_replays'] == 4936, 'source API replay coverage')
    require(receipt['independent_certificate_fixture_accepted'] is True, 'missing independent readout')
    require(receipt['execution_envelope'] == {'scale_max': 16, 'coordinate_guard': 1048576, 'resource_refusal_is_counterexample': False}, 'execution scope upgrade')
    for key in ('homogeneous_marks_imply_homogeneous_patch', 'native_reader_packets_produced',
                'native_source_operations_fully_admitted', 'uniform_Ramsey_bound_proved', 'root_resolved'):
        require(receipt[key] is False, 'patch overclaim')
    for key in ('geometry_receipt', 'certificate_fixture'):
        ref = receipt[key]
        require(sha256(artifact(ref['path']).read_bytes()).hexdigest() == ref['sha256'], 'stale patch subreceipt')
    required = {'research/voevodsky/ramsey-marked-patch.mjs',
                'research/voevodsky/checkers/check_ramsey_marked_patch.mjs',
                'research/voevodsky/checkers/check_ramsey_marked_patch.py',
                'research/voevodsky/contracts/ramsey-marked-patch-attempt.v1.json',
                'research/voevodsky/ramsey-marked-dilation-patch-v1.md',
                'research/voevodsky/ramsey_certificate.py',
                'research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs',
                'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
                'research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs'}
    require(required <= set(receipt['source_sha256']), 'missing source API pins')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale patch source')
    prospective = json.loads(artifact('research/voevodsky/contracts/ramsey-marked-patch-attempt.v1.json').read_text(encoding='utf-8'))
    require(prospective['statement'] == node['statement'] and prospective['scope_id'] == node['scope_id'], 'patch prospective scope drift')
    artifact(attempt['freeze'])


def validate_uniform_bound(net, node):
    require(node['status'] == 'resolved' and node['outcome'] == '++', 'uniform mathematical bound outcome')
    require(len(node['attempts']) == 1, 'uniform bound attempt history')
    attempt = node['attempts'][0]
    require(attempt['intent'] == 'prove' and attempt['outcome'] == '++', 'uniform bound attempt intent')
    require(attempt['scope_id'] == node['scope_id'], 'uniform bound attempt scope')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'uniform claim digest')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'uniform receipt digest')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-uniform-bound.verification.v1' and receipt['status'] == 'passed', 'uniform receipt schema/status')
    require(receipt['scope_id'] == node['scope_id'] and receipt['outcome'] == '++', 'uniform receipt scope/outcome')
    level = 'written classical Hales-Jewett-based effective-bound proof and exact finite controls; not native forcing or kernel verified'
    require(receipt['verification_level'] == attempt['verification_level'] == level, 'uniform bound verification upgrade')
    require(receipt['abstract_algorithm_total_using_classical_HJ'] is True, 'missing termination argument')
    for key in ('classical_HJ_independently_proved_here', 'whole_word_encoder_injective', 'native_forcing_derivation_proved', 'root_resolved'):
        require(receipt[key] is False, 'classical bound overclaim')
    require((len(receipt['word_length_cases']), receipt['independent_word_colorings_checked'], receipt['two_point_affine_lattice_coloring_cases'], len(receipt['rejected_controls'])) == (12, 6577, 196, 13), 'uniform bound control coverage')
    require(receipt['practical_two_color_numeric_bounds_not_computed'] == ['tetrahedron', 'octahedron'], 'fabricated practical numeric result')
    prospective = json.loads(artifact('research/voevodsky/contracts/ramsey-uniform-bound-attempt.v1.json').read_text(encoding='utf-8'))
    require((prospective['statement'], prospective['scope_id']) == (node['statement'], node['scope_id']), 'uniform prospective scope drift')
    require(receipt['bound'] == prospective['candidate_bound'] and receipt['classical_dependency'] == prospective['termination_dependency'], 'external theorem dependency drift')
    require(set(receipt['source_sha256']) == {
        'research/voevodsky/contracts/ramsey-uniform-bound-attempt.v1.json',
        'research/voevodsky/ramsey-uniform-forcing-bound-v1.md',
        'research/voevodsky/results/ramsey-marked-patch-fixture-v1.json',
        'research/voevodsky/ramsey_forcing.py',
        'research/voevodsky/ramsey_certificate.py',
        'research/voevodsky/checkers/check_ramsey_uniform_bound.py'}, 'uniform bound source pins')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale uniform evidence')
    dependencies = net.get('external_mathematical_dependencies', [])
    require(any(d['name'] == 'finite Hales-Jewett theorem' and d['consumer'] == node['id']
                and d['is_cross_net_proof_import'] is False for d in dependencies), 'classical theorem dependency erased')
    artifact(attempt['freeze'])


def validate_covariance(net, node):
    require(node['status'] == 'resolved' and node['outcome'] == '++', 'covariance outcome')
    require(len(node['attempts']) == 1, 'covariance attempt history')
    attempt = node['attempts'][0]
    require(attempt['intent'] == 'prove' and attempt['outcome'] == '++', 'covariance attempt intent')
    require(attempt['scope_id'] == node['scope_id'], 'covariance attempt scope')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'covariance claim digest')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'covariance receipt digest')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-reference-covariance.verification.v1' and receipt['status'] == 'passed', 'covariance receipt schema/status')
    require(receipt['scope_id'] == node['scope_id'] and receipt['outcome'] == '++', 'covariance receipt scope/outcome')
    level = 'written certificate-relation action proof and exact finite/source-geometry controls; not native packet covariance or kernel verified'
    require(receipt['verification_level'] == attempt['verification_level'] == level, 'covariance verification upgrade')
    require((receipt['framed_transport_cases'], receipt['inverse_roundtrips'], receipt['matrix_composition_cases'], len(receipt['rejected_controls'])) == (2592, 432, 2304, 18), 'covariance control coverage')
    require((receipt['macro_carrier_matrices'], receipt['fixed_subdivision_matrices'], receipt['macro_neighbor_checks'], receipt['primitive_neighbor_checks']) == (48, 16, 768, 384), 'carrier/subdivision conflation')
    require(receipt['correct_offset_law'] == 'a_prime=Q*a+(1-m)*b when S_prime=Q*S+b', 'incorrect affine offset action')
    for key in ('reference_free_unique_selector_proved', 'full48_fixed_native_subdivision_covariance_proved', 'native_packet_covariance_proved', 'root_resolved'):
        require(receipt[key] is False, 'covariance overclaim')
    ref = receipt['geometry_receipt']
    require(sha256(artifact(ref['path']).read_bytes()).hexdigest() == ref['sha256'], 'stale source covariance subreceipt')
    required = {'research/voevodsky/ramsey_transport.py', 'research/voevodsky/ramsey_certificate.py',
                'research/voevodsky/contracts/ramsey-reference-covariance-attempt.v1.json',
                'research/voevodsky/ramsey-reference-covariance-v1.md',
                'research/voevodsky/checkers/check_ramsey_reference_covariance.py',
                'research/voevodsky/checkers/check_ramsey_transport_geometry.mjs',
                'research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs',
                'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs'}
    require(required <= set(receipt['source_sha256']), 'missing covariance source pins')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale covariance source')
    prospective = json.loads(artifact('research/voevodsky/contracts/ramsey-reference-covariance-attempt.v1.json').read_text(encoding='utf-8'))
    require((prospective['statement'], prospective['scope_id']) == (node['statement'], node['scope_id']), 'covariance prospective scope drift')
    artifact(attempt['freeze'])


def validate_native_word_lift(net, node):
    require(node['status'] == 'resolved' and node['outcome'] == '++', 'word lift outcome')
    require(len(node['attempts']) == 1, 'word lift attempt history')
    attempt = node['attempts'][0]
    require(attempt['intent'] == 'prove' and attempt['outcome'] == '++', 'word lift attempt intent')
    require(attempt['scope_id'] == node['scope_id'], 'word lift scope')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'word lift claim digest')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'word lift receipt digest')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-native-word-history.verification.v1' and receipt['status'] == 'passed', 'word lift receipt schema/status')
    require(receipt['scope_id'] == node['scope_id'] and receipt['outcome'] == '++', 'word lift receipt scope/outcome')
    level = 'written bounded model-native trace argument and actual packet/phase replay with independent decoder; not native forcing or kernel verified'
    require(receipt['verification_level'] == attempt['verification_level'] == level, 'word lift verification upgrade')
    require((receipt['word_cases'], receipt['append_cases'], receipt['associativity_cases'], receipt['selected_events_in_positive_word_cases'], receipt['negative_controls']) == (133, 49, 3, 926, 19), 'word lift control coverage')
    require(receipt['independent_decoder_agrees'] is True and receipt['repeated_zero_loop_leaves_cached_model_unchanged'] is True, 'missing word lift witnesses')
    for key in ('endpoint_projection_faithful_for_this_code', 'deduplicated_support_faithful_for_this_code',
                'codebook_native_seed_admission_proved', 'simultaneous_assembly_admission_proved',
                'native_forcing_control_proved', 'general_endpoint_encoding_impossibility_proved', 'root_resolved'):
        require(receipt[key] is False, 'word capacity overclaim')
    require(receipt['execution_envelope'] == {'max_alphabet': 256, 'max_word_symbols': 128, 'max_trace_events': 2048, 'resource_refusal_is_counterexample': False}, 'word lift execution scope upgrade')
    for key in ('replay_receipt', 'trace_fixture'):
        ref = receipt[key]
        require(sha256(artifact(ref['path']).read_bytes()).hexdigest() == ref['sha256'], 'stale word lift subreceipt')
    required = {'research/voevodsky/ramsey-native-word-trace.mjs',
                'research/voevodsky/contracts/ramsey-native-word-trace-attempt.v1.json',
                'research/voevodsky/ramsey-native-word-history-lift-v1.md',
                'research/voevodsky/checkers/check_ramsey_native_word_trace.mjs',
                'research/voevodsky/checkers/check_ramsey_native_word_trace.py',
                'research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs',
                'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
                'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs'}
    require(required <= set(receipt['source_sha256']), 'missing actual native packet/phase pins')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale word lift source')
    prospective = json.loads(artifact('research/voevodsky/contracts/ramsey-native-word-trace-attempt.v1.json').read_text(encoding='utf-8'))
    require((prospective['statement'], prospective['scope_id']) == (node['statement'], node['scope_id']), 'word lift prospective scope drift')
    artifact(attempt['freeze'])


def validate_query_descent(net, node):
    require(node['status'] == 'resolved' and node['outcome'] == '-+', 'query descent outcome')
    require(len(node['attempts']) == 1, 'query descent attempt history')
    attempt = node['attempts'][0]
    require(attempt['intent'] == 'reject' and attempt['outcome'] == '-+', 'query descent attempt intent')
    require(attempt['scope_id'] == node['scope_id'], 'query descent scope')
    require(attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'query descent claim digest')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'query descent receipt digest')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    require(receipt['schema'] == 'marici.ramsey-native-query-descent.verification.v1' and receipt['status'] == 'passed', 'query descent receipt schema/status')
    require(receipt['scope_id'] == node['scope_id'] and receipt['outcome'] == '-+', 'query descent receipt scope/outcome')
    level = 'written finite nonfactorization argument, fresh native packet replay and independent arithmetic; not a general native-forcing refutation or kernel proof'
    require(receipt['verification_level'] == attempt['verification_level'] == level, 'query descent verification upgrade')
    require(attempt['evidence_group'] == 'ramsey-native-word-trace-v1', 'shared native trace evidence split')
    for key in ('same_complete_endpoint', 'same_complete_cached_model', 'different_required_queries', 'different_required_colors', 'retained_history_query_recovers_both'):
        require(receipt[key] is True, 'query descent witness missing')
    for key in ('projected_query_factors', 'all_endpoint_encodings_refuted', 'native_forcing_refuted', 'root_resolved'):
        require(receipt[key] is False, 'query descent overclaim')
    require((receipt['fixed_word_length'], receipt['same_total_event_count']) == (2, 7), 'query task length drift')
    witness = receipt['witness']
    require(witness['words'] == [[0, 2], [1, 0]] and witness['colors'] == [0, 1], 'query witness drift')
    require(witness['traces'][0]['endpoint'] == witness['traces'][1]['endpoint'], 'query endpoints not equal')
    require(witness['cacheHashes'][0] == witness['cacheHashes'][1] and witness['completeCachedModelsEqual'] is True, 'query cache witness')
    prospective = json.loads(artifact('research/voevodsky/contracts/ramsey-native-query-descent-attempt.v1.json').read_text(encoding='utf-8'))
    require((prospective['statement'], prospective['scope_id']) == (node['statement'], node['scope_id']), 'query prospective scope drift')
    required = {'research/voevodsky/contracts/ramsey-native-query-descent-attempt.v1.json',
                'research/voevodsky/ramsey-native-query-descent-obstruction-v1.md',
                'research/voevodsky/checkers/check_ramsey_native_query_descent.py',
                'research/voevodsky/ramsey-native-word-trace.mjs',
                'research/voevodsky/checkers/check_ramsey_native_word_trace.py',
                'research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs'}
    require(required <= set(receipt['source_sha256']), 'query source pins missing')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale query descent source')
    artifact(attempt['freeze'])


def validate_selection_result(node):
    positive = node['id'] == 'native-query-selection'
    expected = '++' if positive else '-+'
    require(node['status'] == 'resolved' and node['outcome'] == expected and len(node['attempts']) == 1, 'selection/leaf outcome')
    attempt = node['attempts'][0]
    require(attempt['intent'] == PORTS[expected]['attempt'] and attempt['outcome'] == expected, 'selection/leaf intent')
    require(attempt['scope_id'] == node['scope_id'] and attempt['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'selection/leaf scope')
    path = artifact(attempt['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == attempt['receipt_sha256'], 'selection/leaf receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    name = 'ramsey-native-query-selection' if positive else 'ramsey-single-leaf-query'
    require(r['schema'] == 'marici.'+name+'.verification.v1' and r['status'] == 'passed', 'selection/leaf receipt')
    require(r['scope_id'] == node['scope_id'] and r['outcome'] == expected, 'selection/leaf receipt scope')
    level = ('written finite source-geometry argument, actual native packet/phase replay and independent Python checks; bounded host-compiled selection, not autonomous control or kernel proof' if positive else 'written exact-integer template-to-path induction and exhaustive native source controls; not all source policies or kernel verified')
    require(r['verification_level'] == attempt['verification_level'] == level, 'selection/leaf verification upgrade')
    require(attempt['evidence_group'] == 'ramsey-native-query-selection-v1', 'selection/leaf shared evidence split')
    if positive:
        require((r['exhaustive_length_two_words'], r['construction_cases'], r['native_witness_events'], r['negative_controls'], r['source_valid_wrong_query_controls']) == (9,27,81,13,2), 'selection controls')
        for key in ('native_forward_selected_points_realized', 'host_instruction_compiler_retained', 'input_color_table_observation_retained'):
            require(r[key] is True, 'selection interface boundary missing')
        for key in ('source_selection_depends_on_colors', 'autonomous_native_controller_proved', 'uniform_task_package_admitted', 'root_resolved'):
            require(r[key] is False, 'selection scope overclaim')
        prospective = 'research/voevodsky/contracts/ramsey-native-query-selection-attempt.v1.json'
        claim_key = 'claim'
    else:
        require((r['source_templates_admitted'], r['planar_templates_checked'], r['native_transfers_checked'], r['terminal_exits_checked']) == (96,32,96,16), 'leaf template coverage')
        require(r['query_excluded'] == [3,3,0] and r['single_leaf_uniform_query_lift_refuted'] is True, 'leaf counterexample')
        require(r['uniform_task_package_refuted'] is False and r['root_resolved'] is False and r['witness']['depthLimitedSearchUsed'] is False, 'leaf overclaim')
        require(node['candidate_for'] == 'native-task-package-lift', 'leaf rival disconnected')
        prospective = 'research/voevodsky/contracts/ramsey-single-leaf-query-attempt.v1.json'
        claim_key = 'statement'
    p = json.loads(artifact(prospective).read_text(encoding='utf-8'))
    require((p[claim_key], p['scope_id']) == (node['statement'], node['scope_id']), 'selection/leaf prospective drift')
    require(prospective in r['source_sha256'] and 'research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs' in r['source_sha256'], 'selection/leaf source missing')
    for relative, digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale selection/leaf source')
    artifact(attempt['freeze'])


def validate_region_family(node):
    require(node['status'] == 'resolved' and node['outcome'] == '++' and len(node['attempts']) == 1, 'prepared family outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == node['scope_id'], 'prepared family attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'prepared family claim')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'prepared family receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-native-region-family.verification.v1' and r['status'] == 'passed' and r['scope_id'] == node['scope_id'] and r['outcome'] == '++', 'prepared family receipt scope')
    level = 'fresh safe Cubical native P/E instance under explicit prepared-input policy plus runtime sector checks; not kernel verification of sector geometry or physical policy admissibility'
    require(a['verification_level'] == r['verification_level'] == level, 'prepared policy verification upgrade')
    require(a['evidence_group'] == 'ramsey-native-region-family-v1', 'prepared family evidence group')
    require((r['prepared_contexts'], r['prepared_M_planes'], r['native_P_premises'], r['native_E_premises_each'], r['source_controls']) == (171,7,171,171,7), 'prepared family coverage')
    for key in ('wrong_premise_module_rejected', 'native_derivations_typechecked', 'formal_contexts_equal_source_records', 'formal_colors_are_supplied_parameter', 'prepared_policy_differs_from_canonical'):
        require(r[key] is True, 'prepared native family binding missing')
    for key in ('simultaneous_assembly_admitted', 'word_to_index_constructed', 'physical_prepared_policy_admissibility_proved', 'uniform_task_package_proved', 'root_resolved'):
        require(r[key] is False, 'prepared family scope overclaim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-native-region-family-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'prepared family prospective drift')
    formal = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'] and formal['wrong_premise_rejected_as_expected'], 'formal family check not fresh/stable')
    require(formal['positive_source_sha256'] == r['formal_check']['positive_source_sha256'] and formal['negative_source_sha256'] == r['formal_check']['negative_source_sha256'], 'formal family sources changed')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale prepared family source')
    require(node['candidate_for'] == 'native-task-package-lift', 'prepared family disconnected')
    artifact(a['freeze'])


def validate_word_family(node):
    require(node['status'] == 'resolved' and node['outcome'] == '++' and len(node['attempts']) == 1, 'word-family outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == node['scope_id'], 'word-family attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'word-family claim')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'word-family receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-word-family-selection.verification.v1' and r['status'] == 'passed' and r['scope_id'] == node['scope_id'] and r['outcome'] == '++', 'word-family receipt scope')
    level = 'fresh safe Cubical native word-indexed P/E program and declared-point square, with runtime sector/trace binding; host compiler and decoder retained, not autonomous control or physical policy admission'
    require(a['verification_level'] == r['verification_level'] == level, 'word-family verification upgrade')
    require(a['evidence_group'] == 'ramsey-native-region-family-v1', 'word-family evidence split')
    require((r['word_cases'],r['query_cases'],r['recoloring_index_comparisons'],r['runtime_controls'],r['retained_field_premise_slots']) == (27,81,54,12,4617), 'word-family coverage')
    for key in ('native_program_typechecked','wrong_index_native_program_typechecks','wrong_index_task_square_rejected','wrong_word_premise_rejected','request_and_canonical_trace_observation_preserved','host_table_compiler_retained','host_sector_trace_decoder_retained'):
        require(r[key] is True, 'word-family source/task separation missing')
    for key in ('free_target_index_input','new_seed_policy_introduced','sector_geometry_kernel_proved','autonomous_native_controller_proved','physical_policy_admissibility_proved','uniform_task_package_proved','root_resolved'):
        require(r[key] is False, 'word-family scope overclaim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-word-family-selection-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'word-family prospective drift')
    formal = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'], 'word-family formal check not fresh')
    codes = formal['module_exit_codes']
    require(codes['RamseyWordFamilySelection'] == codes['RamseyWordFamilyWrongIndexNative'] == 0 and codes['RamseyWordFamilyWrongIndex'] != 0 and codes['RamseyWordFamilyWrongPremise'] != 0, 'word-family formal hostiles')
    require(formal['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'word-family compiled source changed')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale word-family source')
    require(node['candidate_for'] == 'native-task-package-lift', 'word-family disconnected')
    artifact(a['freeze'])


def validate_refinement(node):
    require(node['status'] == 'resolved' and node['outcome'] == '++' and len(node['attempts']) == 1, 'refinement outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == node['scope_id'], 'refinement attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'refinement claim')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'refinement receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-family-refinement.verification.v1' and r['status'] == 'passed' and r['scope_id'] == node['scope_id'] and r['outcome'] == '++', 'refinement receipt scope')
    level = 'fresh safe Cubical concrete seed inclusion, native derivation/history transport and overlap squares; runtime sector binding under prepared-input policies, not physical or all-region completion'
    require(a['verification_level'] == r['verification_level'] == level, 'refinement verification upgrade')
    require(a['evidence_group'] == 'ramsey-native-region-family-v1', 'refinement evidence split')
    require((r['old_contexts'],r['new_contexts'],r['added_contexts'],r['common_words'],r['overlap_checks'],r['source_controls'],r['fresh_rebuild_literal_mismatches'],r['fresh_rebuild_readout_checks']) == (171,365,194,27,81,6,171,81), 'refinement coverage')
    for key in ('typed_seed_inclusion','native_derivation_map','constructor_history_preserved','both_route_histories_retained','fresh_rebuild_native_only_typechecks','fresh_rebuild_identity_transport_rejected','wrong_seed_rejected','wrong_direct_query_rejected'):
        require(r[key] is True, 'refinement source/history evidence missing')
    for key in ('whole_family_equivalence_claimed','cofinal_all_region_theorem_proved','physical_policy_admissibility_proved','uniform_task_package_proved','root_resolved'):
        require(r[key] is False, 'refinement overclaim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-family-refinement-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'refinement prospective drift')
    formal = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'], 'refinement formal check not fresh')
    codes = formal['module_exit_codes']
    require(codes['RamseyFamilyRefinement'] == codes['RamseyFamilyFreshNativeOnly'] == 0 and all(codes[k] != 0 for k in ['RamseyFamilyFreshRebuild','RamseyFamilyWrongSeed','RamseyFamilyWrongQuery']), 'refinement formal hostiles')
    require(formal['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'refinement compiled source changed')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale refinement source')
    require(node['candidate_for'] == 'native-task-package-lift' and node['depends_on'] == ['native-region-family-admission','native-word-family-selection'], 'refinement disconnected')
    artifact(a['freeze'])


def validate_exact_source_progress(a):
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == 'uniform-exact-translated-context-source-realizer-v1', 'exact source progress scope')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-exact-source-attempt.v1.json').read_text(encoding='utf-8'))
    require(p['scope_id'] == a['scope_id'] and a['claim_sha256'] == sha256(p['claim'].encode()).hexdigest(), 'exact source prospective drift')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'exact source receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-exact-source.verification.v1' and r['status'] == 'passed' and r['outcome'] == '++' and r['scope_id'] == a['scope_id'], 'exact source receipt scope')
    level = 'written all-index exact local-PN source/region construction and fresh safe Cubical derived-context native query/substitution; bounded legacy renaming, not full operational embedding or unbounded Number API'
    require(r['verification_level'] == a['verification_level'] == level and a['evidence_group'] == 'ramsey-native-region-family-v1', 'exact source verification upgrade')
    require((r['region_context_controls'],r['cutoff_reference_comparisons'],r['legacy_local_bindings'],r['query_cases'],r['negative_controls']) == (1278,613,365,320,8), 'exact source controls')
    for key in ('uniform_exact_region_and_context_construction','derived_actual_point_binding','native_input_program_request_histories_retained','projected_word_and_substitution_laws','five_slot_PN_preserved','full_legacy_local_records_retained'):
        require(r[key] is True, 'exact source constructor evidence missing')
    for key in ('kernel_D3_enumerator_completeness_proved','full_uniform_task_package_proved','intended_operational_space_embedding_proved','legacy_whole_cache_equivalence_claimed','unbounded_Number_API_proved','physical_policy_admissibility_proved','root_resolved'):
        require(r[key] is False, 'exact interpretation promoted to stronger source')
    f = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check'] and f['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'exact source formal check')
    codes = f['module_exit_codes']
    require(codes['RamseyExactSource'] == codes['RamseyExactInstances'] == 0 and all(codes[k] != 0 for k in ['RamseyExactBadBinding','RamseyExactBadReference','RamseyExactBadMember','RamseyExactBadPermutation']), 'exact source formal hostiles')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale exact source')
    artifact(a['freeze'])


def validate_uniform_task(node):
    require(node['status'] == 'resolved' and node['outcome'] == '++' and len(node['attempts']) == 1, 'uniform task outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == node['scope_id'], 'uniform task attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'uniform task claim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-uniform-task-package-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'uniform task prospective drift')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'uniform task receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-uniform-task-package.verification.v1' and r['status'] == 'passed' and r['outcome'] == '++' and r['scope_id'] == node['scope_id'] and r['claim_sha256'] == a['claim_sha256'], 'uniform task receipt scope')
    level = 'written all-index finite-region/source construction plus fresh safe Cubical actual native WG chart policy, uniform query/refusal/substitution and source-target correspondence; explicit higher-index arity, not whole-space or physical forcing'
    require(r['verification_level'] == a['verification_level'] == level and a['evidence_group'] == 'ramsey-native-region-family-v1', 'uniform task verification upgrade')
    for key in ('all_pattern_palette_region_word_quantifiers','source_policy_independent_of_answer','no_exact_context_target_seed_assumed','native_query_refusal_and_substitution','target_full_reference_and_color_binding','higher_index_arity_explicit'):
        require(r[key] is True, 'uniform task required cell missing')
    for key in ('kernel_D3_enumerator_completeness_proved','whole_space_admission_proved','finite_Shift_premise_unfolding_proved','physical_policy_admissibility_proved','autonomous_native_forcing_proved','root_resolved'):
        require(r[key] is False, 'uniform task whole-space/physical overclaim')
    for key in ('chart_interpretation','exact_source'):
        ref = r[key]
        require(sha256(artifact(ref['receipt']).read_bytes()).hexdigest() == ref['sha256'], 'uniform task dependent receipt changed')
    c = json.loads(artifact(r['chart_interpretation']['receipt']).read_text(encoding='utf-8'))
    require(c['status'] == 'passed' and c['scope_id'] == 'exact-input-query-to-canonical-native-WG-charts-v1' and c['target_derived_without_exact_context_seed'] and c['source_target_policies_separate'] and c['actual_uniform_query_package_correspondence'] and c['unbounded_Shift_index_explicit'] and c['absolute_Number_port_refuted'], 'chart interpretation missing or boundary lost')
    require((c['input_chart_cases'],c['reference_comparisons'],c['program_cases'],c['runtime_controls']) == (613,3065,30,4), 'chart controls')
    f = json.loads(artifact(c['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check'] and f['module_source_sha256'] == c['formal_check']['module_source_sha256'], 'chart formal check')
    codes = f['module_exit_codes']
    require(codes['RamseyChartInterpretation'] == codes['RamseyChartInstances'] == 0 and all(codes[k] != 0 for k in ['RamseyChartBadReference','RamseyChartBadSourceSeed','RamseyChartBadSelector']), 'chart source/target adversaries')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale uniform task source')
    artifact(a['freeze'])


def validate_uniform_progress(node):
    validate_uniform_task(node)
    progress = node.get('progress_results', [])
    require(len(progress) == 2 and bool(node.get('broader_nonverification')), 'uniform history or broader boundary missing')
    validate_exact_source_progress(progress[1])
    a = progress[0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == 'all-finite-relative-native-query-refusal-substitution-v1', 'relative progress scope')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-uniform-relative-attempt.v1.json').read_text(encoding='utf-8'))
    require(p['net_node'] == node['id'] and p['scope_id'] == a['scope_id'] and a['claim_sha256'] == sha256(p['claim'].encode()).hexdigest(), 'relative prospective drift')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'relative receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-uniform-relative.verification.v1' and r['status'] == 'passed' and r['outcome'] == '++' and r['scope_id'] == a['scope_id'], 'relative receipt scope')
    level = 'fresh safe Cubical all-finite relative native query/refusal/history constructor and signed-integer substitution laws; opaque-context/source-region binding remains unproved'
    require(r['verification_level'] == a['verification_level'] == level and a['evidence_group'] == 'ramsey-native-region-family-v1', 'relative level or evidence split')
    require((r['runtime_query_cases'],r['runtime_substitution_cases'],r['runtime_controls']) == (423,1023,4), 'relative controls')
    for key in ('symbolic_all_finite_parameters_proved','computed_lookup_and_refusal_proved','native_family_program_request_retained','same_source_variable_substitution_proved','signed_integer_geometry_laws_proved','misbound_native_relative_program_typechecks','misbound_sector_binding_rejected'):
        require(r[key] is True, 'relative constructor or source countermodel missing')
    for key in ('full_uniform_task_package_proved','uniform_complete_sector_family_proved','physical_policy_admissibility_proved','root_resolved'):
        require(r[key] is False, 'relative source overclaim')
    formal = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'], 'relative check not fresh')
    require(formal['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'relative compiled source changed')
    codes = formal['module_exit_codes']
    require(all(codes[k] == 0 for k in ['RamseyUniformRelative','RamseyUniformSigned','RamseyUniformMisbound']) and all(codes[k] != 0 for k in ['RamseyUniformBadBinding','RamseyUniformBadLookup','RamseyUniformBadRefusal','RamseyUniformBadSubstitution']), 'relative formal hostiles')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale relative source')
    artifact(a['freeze'])


def validate_single_frame_faces(node):
    require(node['status'] == 'resolved' and node['outcome'] == '-+' and len(node['attempts']) == 1, 'single-frame outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'reject' and a['outcome'] == '-+' and a['scope_id'] == node['scope_id'], 'single-frame attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'single-frame claim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-single-frame-face-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'single-frame prospective drift')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'single-frame receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-single-frame-faces.verification.v1' and r['status'] == 'passed' and r['outcome'] == '-+' and r['scope_id'] == node['scope_id'], 'single-frame receipt scope')
    level = 'fresh safe Cubical universal finite C/M face-count obstruction and actual PN/reader/full-reference controls; rejects one role-coherent particle-port interpretation, not all source policies'
    require(a['verification_level'] == r['verification_level'] == level and a['evidence_group'] == 'ramsey-native-region-family-v1', 'single-frame verification upgrade')
    require((r['source_regular_cells'],r['native_markings'],r['role_groups'],r['validated_transfers'],r['geometric_neighbors'],r['controls']) == (4,96,24,288,16,12), 'single-frame coverage')
    for key in ('single_role_frame_full_face_policy_refuted','all_markings_grouped_by_roles','all_geometric_faces_have_neighbors','source_valid_incompatible_per_face_port_retained','global_role_sewing_rejects_counterexample'):
        require(r[key] is True, 'single-frame obstruction or rival missing')
    for key in ('all_native_interpretations_refuted','space_admission_refuted','WG_chart_task_package_refuted','root_resolved'):
        require(r[key] is False, 'single-frame rejection overclaim')
    f = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check'] and f['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'single-frame formal check')
    codes = f['module_exit_codes']
    require(codes['RamseySingleFrameFaces'] == 0 and codes['RamseySingleFrameBadAllFaces'] != 0 and codes['RamseySingleFrameBadRoleChange'] != 0, 'single-frame formal hostiles')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale single-frame source')
    require(node['candidate_for'] == 'space-admission' and node['depends_on'] == ['plane-lattice-realization','native-task-package-lift'], 'single-frame rival disconnected')
    artifact(a['freeze'])


def validate_role_domain_transport(node):
    require(node['status'] == 'resolved' and node['outcome'] == '-+' and len(node['attempts']) == 1, 'role-domain outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'reject' and a['outcome'] == '-+' and a['scope_id'] == node['scope_id'], 'role-domain attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'role-domain claim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-role-domain-transport-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'role-domain prospective drift')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'role-domain receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-role-domain-transport.verification.v1' and r['status'] == 'passed' and r['outcome'] == '-+' and r['scope_id'] == node['scope_id'], 'role-domain receipt scope')
    level = 'fresh safe Cubical geometric chart cocycle and no-total-fixed-face PN-domain map, with actual same-face full-reference source controls; not all partial/chart transitions refuted'
    require(a['verification_level'] == r['verification_level'] == level and a['evidence_group'] == 'ramsey-native-region-family-v1', 'role-domain verification upgrade')
    require((r['native_frames'],r['validated_transfers'],r['pair_cells'],r['changed_role_pairs'],r['triple_cocycles'],r['full_reference_cocycles'],r['same_face_changed_role_pairs'],r['controls']) == (24,72,576,480,13824,864,96,5), 'role-domain coverage')
    for key in ('geometric_cocycle_proved','same_face_full_reference_lower_gate_passed','total_geometry_fixed_PN_domain_map_refuted','shared_domain_partial_span_constructed'):
        require(r[key] is True, 'role-domain lower gate or obstruction missing')
    for key in ('partial_span_native_admission_proved','all_role_transitions_refuted','face_chart_descent_refuted','WG_task_package_refuted','root_resolved'):
        require(r[key] is False, 'role-domain rejection overclaim')
    f = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check'] and f['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'role-domain formal check')
    codes = f['module_exit_codes']
    require(codes['RamseyRoleDomainTransport'] == 0 and codes['RamseyRoleDomainBadTotal'] != 0 and codes['RamseyRoleDomainBadGauge'] != 0, 'role-domain formal hostiles')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale role-domain source')
    require(node['candidate_for'] == 'face-chart-transition-descent' and node['motivated_by'] == ['single-frame-full-face-admission'], 'role-domain rival disconnected')
    artifact(a['freeze'])


def validate_native_overlap_span(node):
    require(node['status'] == 'resolved' and node['outcome'] == '++' and len(node['attempts']) == 1, 'native overlap outcome')
    a = node['attempts'][0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == node['scope_id'], 'native overlap attempt')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'native overlap claim')
    p = json.loads(artifact('research/voevodsky/contracts/ramsey-native-PN-overlap-span-attempt.v1.json').read_text(encoding='utf-8'))
    require((p['claim'],p['scope_id']) == (node['statement'],node['scope_id']), 'native overlap prospective drift')
    path = artifact(a['receipt'])
    require(sha256(path.read_bytes()).hexdigest() == a['receipt_sha256'], 'native overlap receipt digest')
    r = json.loads(path.read_text(encoding='utf-8'))
    require(r['schema'] == 'marici.ramsey-native-PN-overlap-span.verification.v1' and r['status'] == 'passed' and r['outcome'] == '++' and r['scope_id'] == node['scope_id'], 'native overlap receipt scope')
    level = 'fresh safe Cubical actual native P/E partial spans, full-port retention and triple-domain composition/seam cells under validated-port input policy; runtime PN binding, not physical role motion or full descent'
    require(a['verification_level'] == r['verification_level'] == level and a['evidence_group'] == 'ramsey-native-region-family-v1', 'native overlap verification upgrade')
    require((r['input_port_records'],r['validated_transfers'],r['pair_cells'],r['empty_pairs'],r['common_pair_ports'],r['triple_cells'],r['empty_triples'],r['common_triple_ports'],r['pairwise_nonempty_empty_triples'],r['controls']) == (48,72,576,96,576,13824,7296,6912,1536,6), 'native overlap coverage')
    for key in ('independent_full_port_input_policy','actual_native_span_and_selection','both_role_domain_certificates_retained','middle_full_packet_and_derivation_cell','all_route_and_three_port_histories_retained','composition_on_declared_triple_domain','empty_pair_and_pairwise_nonempty_empty_triple_checked'):
        require(r[key] is True, 'native overlap constructor or seam missing')
    for key in ('kernel_sector_PN_interpretation_proved','total_PN_gauge_proved','physical_role_change_proved','global_occupied_assembly_proved','full_four_face_descent_proved','whole_space_admission_proved','root_resolved'):
        require(r[key] is False, 'native overlap partial-to-global overclaim')
    f = json.loads(artifact(r['formal_check']['receipt']).read_text(encoding='utf-8-sig'))
    require(f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check'] and f['module_source_sha256'] == r['formal_check']['module_source_sha256'], 'native overlap formal check')
    codes = f['module_exit_codes']
    require(codes['RamseyNativePNOverlapSpan'] == codes['RamseyPNOverlapExamples'] == 0 and all(codes[k] != 0 for k in ['RamseyPNOverlapBadEmptyPair','RamseyPNOverlapBadTriple','RamseyPNOverlapBadLostPort']), 'native overlap formal hostiles')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale native overlap source')
    require(node['candidate_for'] == 'face-chart-transition-descent' and node['motivated_by'] == ['fixed-geometry-total-PN-domain-transport'], 'native overlap disconnected')
    artifact(a['freeze'])


def validate_face_progress(net, node):
    from check_ramsey_face_descent_progress import LEVEL, GATES, NAMES
    progress = node.get('scoped_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'progress upgraded')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'progress receipt digest')
    receipt = json.loads(path.read_text())
    require(receipt['status'] == 'passed' and receipt['scope_id'] == progress.get('scope_id'), 'progress scope')
    require(receipt['outcome'] is None and receipt['parentResolved'] is False, 'progress closes parent')
    require(receipt['verification_level'] == LEVEL and receipt['scientific_attempts_replayed'] == 0, 'progress verification upgrade')
    require(receipt['receipt_count'] == len(NAMES) == 18 and receipt['unresolved_gates'] == GATES, 'progress gates/coverage')
    require(receipt['runtimeBoundFrameComparisons'] == 16 and receipt['runtimeBoundFrameTriangles'] == 64, 'progress comparison coverage')
    for key in ('concreteNumericalKernelInstantiation', 'physicalRoleTransport', 'localFieldGluing', 'RamseyForcing'):
        require(receipt[key] is False, 'progress semantic upgrade')
    require(len(receipt['evidence_records']) == 18, 'progress evidence records')
    for record in receipt['evidence_records']:
        require(sha256(artifact(record['receipt']).read_bytes()).hexdigest() == record['receipt_sha256'], 'stale progress receipt')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale progress source: ' + relative)
    artifact(progress['audit'])
    validate_face_followup(node)
    validate_incidence_progress(node)
    validate_source_admission_progress(node)
    validate_equivariant_progress(node)
    validate_endpoint_progress(node)
    validate_constructor_progress(node)
    update = net.get('local_update', {})
    require(update.get('status') == 'unpublished_working_copy' and update.get('latest_admitted_revision') == 19 and update.get('new_graph_event') is None, 'fabricated local revision admission')
    previous = json.loads(artifact(update.get('previous_contract')).read_text())
    require(previous['revision'] == 31 and previous['registration'] == net['registration'], 'historical admission changed')
    old = {n['id']: n for n in previous['nodes']}
    require({n['id'] for n in net['nodes']} == set(old) | V32_RESULT_IDS | V32_OPEN_IDS, 'unexpected scientific node change')
    for n in net['nodes']:
        if n['id'] in old:
            require(all(n[key] == old[n['id']][key] for key in ('statement', 'acceptance', 'falsifier', 'outcome', 'attempts')), 'previous scientific claim/outcome changed')


def validate_face_followup(node):
    from check_ramsey_face_descent_followup import LEVEL, NAMES, EXPECTED
    progress = node.get('continuation_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'followup upgraded')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'followup receipt digest')
    receipt = json.loads(path.read_text())
    require(receipt['status'] == 'passed' and receipt['scope_id'] == progress.get('scope_id'), 'followup scope')
    require(receipt['outcome'] is None and receipt['parentResolved'] is False, 'followup closes parent')
    require(receipt['verification_level'] == LEVEL and receipt['scientific_attempts_replayed'] == 0, 'followup verification upgrade')
    require(receipt['receipt_count'] == len(receipt['evidence_records']) == len(NAMES) == 5, 'followup coverage')
    require(receipt['sameFaceRequestInterfaceChecked'] is True, 'missing request interface')
    for key in ('fullPreparedScalarEdgeDescent', 'fixedSignedThreeDimensionalDomainClosed', 'allContextIndexedPoliciesRefuted'):
        require(receipt[key] is False, 'followup semantic upgrade')
    expected_paths = {'research/voevodsky/results/' + name + '-v1.json': name for name in NAMES}
    require({r['receipt'] for r in receipt['evidence_records']} == set(expected_paths), 'followup evidence identity')
    for record in receipt['evidence_records']:
        p = artifact(record['receipt'])
        require(sha256(p.read_bytes()).hexdigest() == record['receipt_sha256'], 'stale followup receipt')
        data = json.loads(p.read_text())
        require(data['parentDescentResolved'] is False and all(data[k] == v for k, v in EXPECTED[expected_paths[record['receipt']]].items()), 'followup result drift')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale followup source: ' + relative)
    artifact(progress['audit'])


def validate_incidence_progress(node):
    from check_ramsey_face_descent_incidence_progress import LEVEL, NAMES, EXPECTED
    progress = node.get('incidence_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'incidence progress upgraded')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'incidence progress digest')
    receipt = json.loads(path.read_text())
    require(receipt['status'] == 'passed' and receipt['scope_id'] == progress.get('scope_id'), 'incidence progress scope')
    require(receipt['outcome'] is None and receipt['parentResolved'] is False, 'incidence progress closes parent')
    require(receipt['verification_level'] == LEVEL and receipt['scientific_attempts_replayed'] == 0, 'incidence progress verification upgrade')
    require(receipt['receipt_count'] == len(receipt['evidence_records']) == len(NAMES) == 7, 'incidence progress coverage')
    require(receipt['retainedFourFacetVertexDiagramChecked'] is True, 'missing native four-facet diagram')
    for key in ('completeChoiceFiberEquivalenceClaimed', 'scalarConventionRequiredByParent', 'retainedSpanIdentifiedWithEquivalence'):
        require(receipt[key] is False, 'incidence semantics upgrade')
    expected_paths = {'research/voevodsky/results/' + name + '-v1.json': name for name in NAMES}
    require({r['receipt'] for r in receipt['evidence_records']} == set(expected_paths), 'incidence evidence identity')
    for record in receipt['evidence_records']:
        p = artifact(record['receipt'])
        require(sha256(p.read_bytes()).hexdigest() == record['receipt_sha256'], 'stale incidence receipt')
        data = json.loads(p.read_text())
        require(data['parentDescentResolved'] is False and all(data[k] == v for k, v in EXPECTED[expected_paths[record['receipt']]].items()), 'incidence result drift')
    for relative, digest in receipt['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale incidence source: ' + relative)
    artifact(progress['audit'])


def validate_retained_four_facet(node):
    from check_ramsey_retained_four_facet_correspondence import LEVEL, SCOPE
    require(node['status'] == 'resolved' and node['outcome'] == '++', 'retained four-facet outcome')
    require(node['scope_id'] == SCOPE and node['depends_on'] == ['overlap-restricted-native-PN-span'] and node['candidate_for'] == 'face-chart-transition-descent', 'retained four-facet scope/connection')
    require(len(node['attempts']) == 1, 'retained four-facet attempt history')
    a = node['attempts'][0]
    require(a['intent'] == 'prove' and a['outcome'] == '++' and a['scope_id'] == SCOPE, 'retained four-facet attempt scope')
    require(a['verification_level'] == LEVEL and a['evidence_group'] == 'ramsey-native-region-family-v1', 'retained four-facet verification upgrade')
    require(a['claim_sha256'] == sha256(node['statement'].encode()).hexdigest(), 'retained four-facet claim digest')
    p = artifact(a['receipt'])
    require(sha256(p.read_bytes()).hexdigest() == a['receipt_sha256'], 'retained four-facet receipt digest')
    r = json.loads(p.read_text())
    require(r['status'] == 'passed' and r['outcome'] == '++' and r['scope_id'] == SCOPE and r['verification_level'] == LEVEL and r['claim_sha256'] == a['claim_sha256'], 'retained four-facet receipt scope')
    require(r['freshSafeCubical'] and r['ignoreInterfaces'] and r['inputsStable'] and r['independentFullPortPolicy'], 'retained four-facet freshness/policy')
    require([r[k] for k in ('directedNativeEdgeSelections', 'nativeVertexTripleCompositions', 'differentEdgeRestrictionCells', 'fullMiddleDerivationSeams')] == [12,24,72,24], 'retained four-facet coverage')
    require(r['moduleExitCodes']['RamseyNativeEdgeAttachments'] == r['moduleExitCodes']['RamseyFourFacetVertexCells'] == 0 and r['moduleExitCodes']['RamseyFourFacetBadMiddle'] != 0, 'retained four-facet kernel results')
    for k in ('completeDomainEquivalence', 'physicalRoleMotion', 'scalarFieldGluing', 'wholeSpaceAdmission', 'parentDescentResolved', 'rootResolved'):
        require(r[k] is False, 'retained four-facet semantic promotion')
    for relative, digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale retained four-facet source: ' + relative)
    contract = json.loads(artifact('research/voevodsky/contracts/ramsey-retained-four-facet-correspondence-attempt.v1.json').read_text())
    require(all(node[k] == contract[k] for k in ('statement','acceptance','falsifier')), 'retained four-facet declared claim changed')
    artifact(a['freeze'])
    artifact(node['progress_packet'])


def validate_source_admission_progress(node):
    from check_ramsey_source_admission_progress import LEVEL, NAMES, EXPECTED
    progress = node.get('source_admission_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'source admission progress upgraded')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'source admission progress digest')
    r = json.loads(path.read_text())
    require(r['status'] == 'passed' and r['scope_id'] == progress.get('scope_id'), 'source admission progress scope')
    require(r['outcome'] is None and r['parentResolved'] is False, 'source admission progress closes parent')
    require(r['verification_level'] == LEVEL and r['scientific_attempts_replayed'] == 0, 'source admission verification upgrade')
    require(r['receipt_count'] == len(r['evidence_records']) == len(NAMES) == 7, 'source admission progress coverage')
    require(r['externalFourFacetPolicyChecked'] is True, 'missing external source policy')
    for k in ('rawPackagePathIsOperationalTransition','independentTargetInputsEliminated','localSourceParityKernelVerified','allPossibleSourcePoliciesRefuted'):
        require(r[k] is False, 'source admission semantic promotion')
    expected_paths = {'research/voevodsky/results/' + name + '-v1.json': name for name in NAMES}
    require({x['receipt'] for x in r['evidence_records']} == set(expected_paths), 'source admission evidence identity')
    for x in r['evidence_records']:
        p = artifact(x['receipt'])
        require(sha256(p.read_bytes()).hexdigest() == x['receipt_sha256'], 'stale source admission receipt')
        data = json.loads(p.read_text())
        require(data['parentDescentResolved'] is False and all(data[k] == v for k,v in EXPECTED[expected_paths[x['receipt']]].items()), 'source admission result drift')
    for relative,digest in r['source_sha256'].items():
        require(sha256(artifact(relative).read_bytes()).hexdigest() == digest, 'stale source admission source: ' + relative)
    artifact(progress['audit'])


def validate_equivariant_progress(node):
    from check_ramsey_equivariant_progress import LEVEL, build
    progress = node.get('equivariant_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'equivariant progress promoted')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'equivariant progress digest')
    receipt = json.loads(path.read_text())
    require(receipt == build(), 'equivariant progress evidence or boundary drift')
    require(receipt['scope_id'] == progress.get('scope_id'), 'equivariant progress scope')
    artifact(progress['audit'])


def validate_endpoint_progress(node):
    from check_ramsey_endpoint_progress import LEVEL, build
    progress = node.get('endpoint_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'endpoint progress promoted')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'endpoint progress digest')
    receipt = json.loads(path.read_text())
    require(receipt == build(), 'endpoint evidence or scope drift')
    require(receipt['scope_id'] == progress.get('scope_id'), 'endpoint progress scope')
    artifact(progress['audit'])


def validate_constructor_progress(node):
    from check_ramsey_constructor_progress import LEVEL, build
    progress = node.get('constructor_progress', {})
    require(progress.get('outcome') is None and progress.get('verification_level') == LEVEL, 'constructor progress promoted')
    path = artifact(progress.get('receipt'))
    require(sha256(path.read_bytes()).hexdigest() == progress.get('receipt_sha256'), 'constructor progress digest')
    receipt = json.loads(path.read_text())
    require(receipt == build(), 'constructor evidence or scope drift')
    require(receipt['scope_id'] == progress.get('scope_id'), 'constructor progress scope')
    artifact(progress['audit'])


def validate_prior_work(nodes):
    expected_dependencies = {
        'prior-moving-reference-seam': [],
        'prior-fixed-coordinate-reversal-coherence': [],
        'prior-dual-basis-native-numeric-binding': ['prior-moving-reference-seam'],
        'dual-reference-native-readout-binding': ['prior-moving-reference-seam', 'prior-dual-basis-native-numeric-binding'],
        'reversed-boundary-source-admission': ['dual-reference-native-readout-binding'],
        'admitted-reversal-overlap-coherence': ['reversed-boundary-source-admission', 'prior-fixed-coordinate-reversal-coherence'],
    }
    expected_dependencies.update({
        **{key: [] for key in V29_PRIOR_IDS | V30_PRIOR_IDS | V31_PRIOR_IDS},
        'T-seam-based-port-readout-binding': ['prior-moving-reference-seam', 'prior-co-moving-N-reader-interface', 'prior-geometric-five-column-seed', 'prior-local-metric-based-branch-lift', 'prior-completed-twelve-port-metric-route'],
        'T-seam-marked-face-patch-sector-transport': ['prior-moving-reference-seam', 'prior-co-moving-N-reader-interface', 'prior-geometric-five-column-seed'],
        'T-seam-joint-field-readout-binding': ['prior-moving-reference-seam', 'prior-joint-field-readout-sewing', 'prior-dual-basis-native-numeric-binding'],
        'dual-field-reverse-policy-compatibility': ['T-seam-joint-field-readout-binding', 'prior-direction-indexed-reverse-validator'],
    })
    binding_children = {'prior-joint-field-readout-sewing', 'prior-native-reader-comparison-boundary', 'prior-reconstruction-aware-reference-change', 'T-seam-joint-field-readout-binding'}
    admission_children = {'prior-direction-indexed-reverse-validator', 'dual-field-reverse-policy-compatibility'}
    for key in PRIOR_IDS | NEW_OPEN_IDS:
        n = nodes[key]
        require(n['status'] == ('confirmed_prior_result' if key in PRIOR_IDS else 'open_candidate'), 'prior confirmation/open gate conflated')
        require(n['outcome'] is None and n['attempts'] == [], 'prior record promoted to new proof outcome')
        parent = 'dual-reference-native-readout-binding' if key in binding_children else 'reversed-boundary-source-admission' if key in admission_children else 'face-chart-transition-descent'
        if key in V30_PRIOR_IDS | V30_OPEN_IDS:
            parent = 'T-seam-joint-field-readout-binding'
        if key in V31_PRIOR_IDS | V31_OPEN_IDS:
            parent = 'T-seam-marked-face-patch-sector-transport'
        require(n['depends_on'] == expected_dependencies[key] and n['candidate_for'] == parent, 'prior gate disconnected')
        require(bool(n['provenance']) and bool(n['evidence']), 'prior provenance absent')
        for path in n['evidence']:
            artifact(path)
        if key in PRIOR_IDS:
            require(bool(n['verification_level']) and bool(n['evidence_status']), 'prior evidence scope absent')
        else:
            require(n['protocol']['intent'] == 'prove' and bool(n['protocol']['stop_condition']), 'open prior gate protocol absent')
    require(nodes['prior-fixed-coordinate-reversal-coherence']['evidence_status'] == 'prior_source_inspected_not_freshly_replayed', 'old coherence replay fabricated')
    for key in V29_PRIOR_IDS:
        expected = 'prior_source_inspected_direct_pins_checked_not_scientifically_replayed' if key in {'prior-joint-field-readout-sewing', 'prior-direction-indexed-reverse-validator'} else 'prior_source_inspected_not_freshly_replayed'
        require(nodes[key]['evidence_status'] == expected, 'new prior replay or freshness fabricated')
    for key in V30_PRIOR_IDS | V31_PRIOR_IDS:
        require(nodes[key]['evidence_status'] == 'prior_source_inspected_direct_pins_checked_not_scientifically_replayed', 'processed prior finding promoted to fresh replay')
    require(nodes['T-seam-joint-field-readout-binding'].get('protocol', {}).get('recommended_child') == 'T-seam-marked-face-patch-sector-transport', 'marked geometric seam investigation missing')
    require(nodes['T-seam-marked-face-patch-sector-transport']['motivated_by'] == ['prior-marked-P-field-attachment', 'prior-field-binding-convention-obstructions', 'prior-face-return-extension-obstructions'], 'geometric seam scope controls missing')
    require(nodes['T-seam-marked-face-patch-sector-transport'].get('protocol', {}).get('recommended_child') == 'T-seam-based-port-readout-binding', 'based port binding investigation missing')
    require(nodes['T-seam-based-port-readout-binding']['motivated_by'] == ['prior-patch-Gram-shape-obstruction', 'prior-axial-polarity-constructor-boundary', 'prior-native-conditional-PN-patch-transport'], 'based port scope controls missing')
    for path, count in [('research/strominger/results/belt-local-field-lift/verification.json', 13),
                        ('research/strominger/results/belt-axial-witness/verification.json', 8),
                        ('research/strominger/results/belt-relative-assembly/verification.json', 10),
                        ('research/strominger/results/opposite-branch-cycle-lift/verification.json', 11),
                        ('research/strominger/results/native-patch-mode-transport/verification.json', 5),
                        ('research/strominger/results/joint-field-assembly-sewing.json', 10), ('research/strominger/results/screw-field-sewing.json', 14), ('research/strominger/results/dual-isotope-rules/verification.json', 6),
                        ('research/strominger/results/tetrahedral-field-attachment/verification.json', 6),
                        ('research/strominger/results/neutron-reader-field-interface/verification.json', 7),
                        ('research/strominger/results/five-coefficient-field-binding/verification.json', 4),
                        ('research/strominger/results/full-five-channel-candidate/verification.json', 10),
                        ('research/strominger/results/global-PN-NE-extension/verification.json', 7),
                        ('research/strominger/results/T-projector-field/verification.json', 3)]:
        report = json.loads(artifact(path).read_text())
        pins = report.get('sourceHashes', report.get('source_hashes', {}))
        require(len(pins) == count, 'prior direct-pin coverage drift')
        for source, digest in pins.items():
            require(sha256(artifact(source).read_bytes()).hexdigest() == digest, 'stale prior interface source: ' + source)
    require(nodes['dual-reference-native-readout-binding'].get('protocol', {}).get('recommended_child') == 'T-seam-joint-field-readout-binding', 'field binding investigation missing')
    require(nodes['reversed-boundary-source-admission'].get('protocol', {}).get('recommended_child') == 'dual-field-reverse-policy-compatibility', 'reverse policy investigation missing')
    receipt = json.loads(artifact('research/voevodsky/results/ramsey-prior-dual-basis-v1.json').read_text())
    require(receipt['status'] == 'passed' and (receipt['freshMarkings'], receipt['numericRebasedNativeChains'], receipt['shapeIneligible']) == (24, 8, 16), 'dual basis scope/count drift')
    require(receipt['priorBasisMap'] == [4,3,2,1,0] and receipt['incoming'] == ['C0','M0','C1','M1','C2'] and receipt['outgoing'] == ['M0','C1','M1','C2','M2'], 'reference basis conflated')
    require(all(r['requiredMarks'] != r['literalOutgoingMarksAtNativeSlots'] for r in receipt['readouts']), 'readout mismatch erased')
    for row in receipt['rows']:
        if row['nativeReverseChartEligible']:
            require(row['outgoingBasisBindingEstablished'] is False and row['originalElectronOutgoingCount'] == 0, 'numeric check promoted to admission')
    for path, digest in receipt['source_sha256'].items():
        require(sha256(artifact(path).read_bytes()).hexdigest() == digest, 'stale dual basis source: ' + path)
    require(nodes['face-chart-transition-descent'].get('protocol', {}).get('recommended_child') == 'dual-reference-native-readout-binding', 'prior next target missing')


def validate(net):
    require(net['schema'] == 'marici.owner-local-conjecture-net.v1', 'schema')
    require(net['id'] == 'ramsey-tetrahedral-octahedral' and net['revision'] == 32, 'identity/version')
    require(net['owner'] == 'marici.Voevodsky', 'owner')
    require(net['outcome_semantics'] == SEMANTICS and net['outcome_ports'] == PORTS, 'outcome semantics')
    require(net['objective']['outcome'] is None and net['objective']['attempts'] == [], 'root promotion')
    require(net['imports'] == [], 'unreviewed proof import')
    require(net['candidate_space']['status'] == 'candidate_not_admitted_as_native_source', 'unproved admission')
    require(net['pilot']['quantifier'] == QUANTIFIER, 'changed pilot quantifiers')
    require(net['pilot']['scope_id'] == 'D3-positive-integer-homotheties-vertex-coloring-v1', 'pilot scope')
    nodes = {n['id']: n for n in net['nodes']}
    require(len(nodes) == len(net['nodes']) and set(nodes) == NODE_IDS, 'node identity/duplicate')
    require(len({n['scope_id'] for n in nodes.values()}) == len(nodes), 'duplicate scope')
    for node in nodes.values():
        if node['id'] == 'native-retained-four-facet-correspondence':
            validate_retained_four_facet(node)
        elif node['id'] == 'overlap-restricted-native-PN-span':
            validate_native_overlap_span(node)
        elif node['id'] == 'fixed-geometry-total-PN-domain-transport':
            validate_role_domain_transport(node)
        elif node['id'] == 'single-frame-full-face-admission':
            validate_single_frame_faces(node)
        elif node['id'] == 'native-task-package-lift':
            validate_uniform_progress(node)
        elif node['id'] == 'native-family-refinement-transport':
            validate_refinement(node)
        elif node['id'] == 'native-word-family-selection':
            validate_word_family(node)
        elif node['id'] == 'native-region-family-admission':
            validate_region_family(node)
        elif node['id'] in {'native-query-selection', 'single-leaf-query-completeness'}:
            validate_selection_result(node)
        elif node['id'] == 'finite-certificate-interface':
            validate_interface(net, node)
        elif node['id'] == 'endpoint-cache-query-descent':
            validate_query_descent(net, node)
        elif node['id'] == 'native-word-history-lift':
            validate_native_word_lift(net, node)
        elif node['id'] == 'reference-covariance':
            validate_covariance(net, node)
        elif node['id'] == 'uniform-vertex-bound':
            validate_uniform_bound(net, node)
        elif node['id'] == 'marked-dilation-patch':
            validate_marked_patch(net, node)
        elif node['id'] in {'plane-lattice-realization', 'fixed-scale-cell-forcing'}:
            validate_plane_result(net, node)
        else:
            require(node['outcome'] is None and node['attempts'] == [], 'fabricated scientific outcome')
        require(bool(node['statement']) and bool(node['acceptance']) and bool(node['falsifier']), 'unbounded claim')
        require(len(set(node['depends_on'])) == len(node['depends_on']), 'duplicate dependency')
        require(set(node['depends_on']) <= set(nodes), 'unknown dependency')
    done, active = set(), set()

    def visit(key):
        require(key not in active, 'dependency cycle')
        if key in done:
            return
        active.add(key)
        for dep in nodes[key]['depends_on']:
            visit(dep)
        active.remove(key)
        done.add(key)

    for key in nodes:
        visit(key)
    require(nodes['finite-certificate-interface']['depends_on'] == [], 'pilot unnecessarily blocked')
    require(nodes['space-admission']['depends_on'] == ['plane-lattice-realization', 'marked-dilation-patch', 'native-task-package-lift'], 'source task bridge disconnected')
    require(nodes['native-task-package-lift']['depends_on'] == ['native-query-selection', 'marked-dilation-patch', 'finite-certificate-interface', 'native-word-family-selection', 'native-family-refinement-transport'], 'uniform package bridge disconnected')
    validate_prior_work(nodes)
    validate_coherence_progress(nodes, artifact, require)
    selected = net['recommended_start']
    require(selected == 'face-chart-transition-descent' and selected in nodes, 'missing or unrelated selected investigation')
    candidate = nodes[selected]
    validate_face_progress(net, candidate)
    require(candidate['status'] == 'open_candidate' and candidate['outcome'] is None, 'resolved investigation selected')
    require(candidate.get('candidate_for') == 'space-admission' and candidate.get('motivated_by') == ['single-frame-full-face-admission'] and candidate['depends_on'] == ['plane-lattice-realization','native-task-package-lift','overlap-restricted-native-PN-span'], 'face-chart successor disconnected')
    require(all(nodes[key]['outcome'] == '++' for key in candidate['depends_on']), 'selected investigation prerequisites unavailable')
    require(nodes['native-query-selection'].get('motivated_by') == ['endpoint-cache-query-descent'], 'query obstruction motivation missing')
    protocol = candidate.get('protocol', {})
    require(protocol.get('intent') == 'prove' and protocol.get('coherence_obligation') == 'native_role_chart_transition_and_overlap_cells_before_incidence_descent', 'query forward-construction protocol missing')
    require(nodes['native-query-selection']['protocol']['fixed_input']['words'] == [[0,2],[1,0]], 'query discriminator drift')
    require(bool(protocol.get('next_attempt')) and bool(protocol.get('stop_condition')) and len(protocol.get('rivals', [])) == 3, 'package attempt or stopping rule missing')
    require(bool(net.get('work_connection_policy')), 'unconnected research work allowed')
    require(nodes['fixed-scale-cell-forcing']['depends_on'] == ['plane-lattice-realization'], 'fixed-scale geometry prerequisite')
    require(nodes['finite-certificate-interface']['protocol']['intent'] == 'prove', 'protocol intent')
    require(set(nodes['uniform-vertex-bound']['depends_on']) == {'plane-lattice-realization', 'finite-certificate-interface'}, 'mathematical bound prerequisites')
    require(set(nodes['native-forcing-construction']['depends_on']) == {'uniform-vertex-bound', 'marked-dilation-patch', 'space-admission'}, 'full native policy bypass')
    require('graph-hypergraph-scope-extension' not in nodes['pilot-native-assembly']['depends_on'], 'extension conflated with pilot')
    registration = net['registration']
    require(registration['status'] in {'pending', 'admitted'}, 'registration status')
    require((registration['event_id'] is not None) == (registration['status'] == 'admitted'), 'registration evidence')
    for relative in [net['packet'], net['validator'], MANIFEST] + net['source_context']:
        artifact(relative)
    return nodes


def main():
    net = json.loads(artifact(CONTRACT).read_text(encoding='utf-8'))
    nodes = validate(net)
    controls = []

    def rejects(name, change):
        bad = deepcopy(net)
        change(bad)
        try:
            validate(bad)
        except ValueError:
            controls.append(name)
        else:
            raise AssertionError('corruption accepted: ' + name)

    rejects('candidate coherence promoted to source selection', lambda n: next(x for x in n['nodes'] if x['id'] == 'theorem-candidate-arbitrary-assembly-coherence')['scope_guards'].update(independent_source_selection=True))
    rejects('mathematical theorem promoted to kernel certificate', lambda n: next(x for x in n['nodes'] if x['id'] == 'theorem-candidate-arbitrary-assembly-coherence')['scope_guards'].update(formal_kernel_certificate=True))
    rejects('corrected E result erased', lambda n: next(x for x in n['nodes'] if x['id'] == 'result-ordered-outgoing-E-readout').update(status='open_candidate'))
    rejects('remaining source choice prematurely confirmed', lambda n: next(x for x in n['nodes'] if x['id'] == 'joint44-native-source-selection').update(status='confirmed_scoped_result'))
    rejects('coherence theorem candidate dependency erased', lambda n: next(x for x in n['nodes'] if x['id'] == 'theorem-candidate-arbitrary-assembly-coherence').update(depends_on=[]))
    rejects('based port binding prematurely confirmed', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-based-port-readout-binding').update(status='confirmed_prior_result'))
    rejects('local branch lift inspection promoted to replay', lambda n: next(x for x in n['nodes'] if x['id'] == 'prior-local-metric-based-branch-lift').update(evidence_status='fresh_exact_runtime_followup'))
    rejects('based port source dependency removed', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-based-port-readout-binding').update(depends_on=[]))
    rejects('based port obstruction controls removed', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-based-port-readout-binding').update(motivated_by=[]))
    rejects('marked seam action prematurely confirmed', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-marked-face-patch-sector-transport').update(status='confirmed_prior_result'))
    rejects('geometric seed inspection promoted to replay', lambda n: next(x for x in n['nodes'] if x['id'] == 'prior-geometric-five-column-seed').update(evidence_status='fresh_exact_runtime_followup'))
    rejects('marked seam source dependency removed', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-marked-face-patch-sector-transport').update(depends_on=[]))
    rejects('marked seam obstruction controls removed', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-marked-face-patch-sector-transport').update(motivated_by=[]))
    rejects('experimental reverse validator promoted to native proof', lambda n: next(x for x in n['nodes'] if x['id'] == 'prior-direction-indexed-reverse-validator').update(outcome='++'))
    rejects('joint-field inspection promoted to fresh replay', lambda n: next(x for x in n['nodes'] if x['id'] == 'prior-joint-field-readout-sewing').update(evidence_status='fresh_exact_runtime_followup'))
    rejects('combined reverse-policy gate prematurely confirmed', lambda n: next(x for x in n['nodes'] if x['id'] == 'dual-field-reverse-policy-compatibility').update(status='confirmed_prior_result'))
    rejects('field binding source dependency erased', lambda n: next(x for x in n['nodes'] if x['id'] == 'T-seam-joint-field-readout-binding').update(depends_on=[]))
    rejects('prior result promoted to proof outcome', lambda n: next(x for x in n['nodes'] if x['id'] == 'prior-moving-reference-seam').update(outcome='++'))
    rejects('open admission gate marked confirmed', lambda n: next(x for x in n['nodes'] if x['id'] == 'reversed-boundary-source-admission').update(status='confirmed_prior_result'))
    rejects('old coherence presented as fresh replay', lambda n: next(x for x in n['nodes'] if x['id'] == 'prior-fixed-coordinate-reversal-coherence').update(evidence_status='fresh_exact_runtime_followup'))
    rejects('readout binding disconnected', lambda n: next(x for x in n['nodes'] if x['id'] == 'dual-reference-native-readout-binding').update(depends_on=[]))
    rejects('empty research frontier despite explicit candidate', lambda n: n.update(recommended_start=None))
    rejects('completed node selected as new investigation', lambda n: n.update(recommended_start='native-word-history-lift'))
    rejects('total PN transport rejection promoted to all partial maps', lambda n: n['nodes'][20]['attempts'][0].update(scope_id='all-role-transition-maps-impossible'))
    rejects('PN transport rejection disconnected', lambda n: n['nodes'][20].update(candidate_for='unrelated'))
    rejects('single-frame rejection promoted to all sources', lambda n: n['nodes'][18]['attempts'][0].update(scope_id='all-native-spaces-refuted'))
    rejects('single-frame rival disconnected', lambda n: n['nodes'][18].update(candidate_for='unrelated'))
    rejects('full face-chart successor lacks a test protocol', lambda n: n['nodes'][19].pop('protocol'))
    rejects('full face-chart successor not connected to role-frame rejection', lambda n: n['nodes'][19].update(motivated_by=[]))
    rejects('native partial span promoted to physical role motion', lambda n: n['nodes'][21]['attempts'][0].update(verification_level='physical role gauge'))
    rejects('chart task package promoted to whole-space admission', lambda n: n['nodes'][0].update(outcome='++'))
    rejects('uniform higher-index and broader boundary erased', lambda n: n['nodes'][13].update(broader_nonverification=[]))
    rejects('uniform policy proof promoted to physical forcing', lambda n: n['nodes'][13]['attempts'][0].update(verification_level='physical forcing theorem'))
    rejects('exact source model promoted to whole operational embedding', lambda n: n['nodes'][13]['progress_results'][1].update(verification_level='complete operational source equivalence'))
    rejects('relative theorem scope widened to full task', lambda n: n['nodes'][13]['progress_results'][0].update(scope_id='uniform-native-Ramsey-input-query-package-v1'))
    rejects('refinement transport promoted to cofinal or physical completion', lambda n: n['nodes'][17]['attempts'][0].update(verification_level='all-region physical completion'))
    rejects('word-family program promoted to physical controller', lambda n: n['nodes'][16]['attempts'][0].update(verification_level='physical autonomous control'))
    rejects('prepared input policy promoted to original physical admission', lambda n: n['nodes'][15]['attempts'][0].update(verification_level='physical policy derived'))
    rejects('prepared family not connected to task package', lambda n: n['nodes'][15].update(candidate_for='unrelated'))
    rejects('refinement prerequisites erased', lambda n: n['nodes'][17].update(depends_on=[]))
    rejects('bounded native query promoted to kernel', lambda n: n['nodes'][12]['attempts'][0].update(verification_level='kernel verified'))
    rejects('single leaf rejection promoted to every policy', lambda n: n['nodes'][14]['attempts'][0].update(scope_id='all-Marici-impossible'))
    rejects('single leaf rival disconnected', lambda n: n['nodes'][14].update(candidate_for='unrelated-objective'))
    rejects('uniform package work disconnected from query witness', lambda n: n['nodes'][13].update(depends_on=[]))
    rejects('source admission bypasses task package', lambda n: n['nodes'][0].update(depends_on=['plane-lattice-realization', 'marked-dilation-patch']))
    rejects('root promotion', lambda n: n['objective'].update(outcome='++'))
    rejects('child promotion without attempt', lambda n: n['nodes'][0].update(outcome='++'))
    rejects('removed completed interface result', lambda n: n['nodes'][1].update(outcome=None))
    rejects('wrong attempt scope', lambda n: n['nodes'][1]['attempts'][0].update(scope_id='another-proposition'))
    rejects('wrong receipt digest', lambda n: n['nodes'][1]['attempts'][0].update(receipt_sha256='0' * 64))
    rejects('verification-level upgrade', lambda n: n['nodes'][1]['attempts'][0].update(verification_level='kernel verified'))
    rejects('fixed-scale rejection changed to proof', lambda n: n['nodes'][8].update(outcome='++'))
    rejects('geometric source result promoted to native admission', lambda n: n['nodes'][0].update(outcome='++'))
    rejects('geometric scope drift', lambda n: n['nodes'][7]['attempts'][0].update(scope_id='native-source-already-proved'))
    rejects('shared geometric evidence counted independently', lambda n: n['nodes'][8]['attempts'][0].update(evidence_group='independent-result'))
    rejects('classical uniform bound promoted to native forcing', lambda n: n['nodes'][3].update(outcome='++'))
    rejects('external HJ dependency erased', lambda n: n.update(external_mathematical_dependencies=[]))
    rejects('uniform mathematical proof upgraded to kernel', lambda n: n['nodes'][2]['attempts'][0].update(verification_level='kernel verified'))
    rejects('uniform bound receipt scope drift', lambda n: n['nodes'][2]['attempts'][0].update(scope_id='native-word-forcing'))
    rejects('covariance proof upgraded to native packet theorem', lambda n: n['nodes'][4]['attempts'][0].update(verification_level='full native packet covariance'))
    rejects('covariance receipt scope drift', lambda n: n['nodes'][4]['attempts'][0].update(scope_id='all-native-particle-symmetries'))
    rejects('covariance receipt digest tampered', lambda n: n['nodes'][4]['attempts'][0].update(receipt_sha256='0' * 64))
    rejects('word trace capacity upgraded to native forcing', lambda n: n['nodes'][3].update(outcome='++'))
    rejects('word trace scope upgraded to all native derivations', lambda n: n['nodes'][10]['attempts'][0].update(scope_id='all-native-source-policies'))
    rejects('word trace proof upgraded to kernel theorem', lambda n: n['nodes'][10]['attempts'][0].update(verification_level='kernel verified'))
    rejects('query projection rejection changed to confirmation', lambda n: n['nodes'][11].update(outcome='++'))
    rejects('query descent scope upgraded to all native forcing', lambda n: n['nodes'][11]['attempts'][0].update(scope_id='all-native-forcing-impossible'))
    rejects('query evidence counted independently of native trace', lambda n: n['nodes'][11]['attempts'][0].update(evidence_group='independent-universal-no-go'))
    rejects('polarity substituted for proof semantics', lambda n: n.update(outcome_semantics='signed-arrow-composition'))
    rejects('cycle', lambda n: n['nodes'][7].update(depends_on=['space-admission']))
    rejects('unknown dependency', lambda n: n['nodes'][0].update(depends_on=['nonexistent']))
    rejects('duplicate node', lambda n: n['nodes'].append(deepcopy(n['nodes'][0])))
    rejects('weakened arbitrary-coloring quantifier', lambda n: n['pilot'].update(quantifier='Only selected colorings'))
    rejects('unproved source admission', lambda n: n['candidate_space'].update(status='proved'))
    rejects('missing source', lambda n: n['source_context'].append('research/voevodsky/nonexistent-ramsey-source.md'))
    rejects('unreviewed import', lambda n: n['imports'].append({'outcome': '++'}))
    rejects('mathematical bound bypasses geometric carrier', lambda n: n['nodes'][2].update(depends_on=['finite-certificate-interface']))
    rejects('optional particle gate blocks mathematical bound', lambda n: n['nodes'][2]['depends_on'].append('space-admission'))
    rejects('patch evidence promoted to full source admission', lambda n: n['nodes'][0].update(outcome='++'))
    rejects('patch scope upgraded', lambda n: n['nodes'][9]['attempts'][0].update(verification_level='native particle theorem'))
    rejects('graph extension made prerequisite of pilot', lambda n: n['nodes'][5]['depends_on'].append('graph-hypergraph-scope-extension'))
    rejects('progress upgraded to complete kernel interpretation', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['scoped_progress'].update(verification_level='kernel verified'))
    rejects('progress given a parent outcome', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['scoped_progress'].update(outcome='++'))
    rejects('progress receipt digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['scoped_progress'].update(receipt_sha256='0' * 64))
    rejects('local revision presented as admitted', lambda n: n['local_update'].update(status='admitted'))
    rejects('followup promoted to full kernel field descent', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['continuation_progress'].update(verification_level='kernel verified'))
    rejects('followup given a parent outcome', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['continuation_progress'].update(outcome='++'))
    rejects('followup receipt digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['continuation_progress'].update(receipt_sha256='0' * 64))
    rejects('incidence spans promoted to complete equivalences', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['incidence_progress'].update(verification_level='complete domain equivalence'))
    rejects('incidence progress given a parent outcome', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['incidence_progress'].update(outcome='++'))
    rejects('incidence progress digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['incidence_progress'].update(receipt_sha256='0' * 64))
    rejects('retained correspondence promoted to complete role equivalence', lambda n: next(x for x in n['nodes'] if x['id'] == 'native-retained-four-facet-correspondence')['attempts'][0].update(verification_level='complete role equivalence'))
    rejects('retained correspondence scope widened', lambda n: next(x for x in n['nodes'] if x['id'] == 'native-retained-four-facet-correspondence').update(scope_id='full-face-descent'))
    rejects('retained correspondence disconnected', lambda n: next(x for x in n['nodes'] if x['id'] == 'native-retained-four-facet-correspondence').update(depends_on=[]))
    rejects('source parity argument promoted to kernel JS semantics', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['source_admission_progress'].update(verification_level='kernel verified JS semantics'))
    rejects('source admission progress given parent verdict', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['source_admission_progress'].update(outcome='-+'))
    rejects('source admission progress digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['source_admission_progress'].update(receipt_sha256='0' * 64))
    rejects('equivariant comparison promoted to source generation', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['equivariant_progress'].update(verification_level='native source generation proved'))
    rejects('equivariant comparison assigned parent verdict', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['equivariant_progress'].update(outcome='++'))
    rejects('equivariant receipt digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['equivariant_progress'].update(receipt_sha256='0' * 64))
    rejects('endpoint index coherence promoted to derivation equality', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['endpoint_progress'].update(verification_level='native derivation equality proved'))
    rejects('endpoint progress assigned parent verdict', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['endpoint_progress'].update(outcome='-+'))
    rejects('endpoint receipt digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['endpoint_progress'].update(receipt_sha256='0' * 64))
    rejects('constructor relation promoted to arbitrary derivation equality', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['constructor_progress'].update(verification_level='arbitrary native derivation equality'))
    rejects('constructor progress assigned parent verdict', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['constructor_progress'].update(outcome='++'))
    rejects('constructor receipt digest tampered', lambda n: next(x for x in n['nodes'] if x['id'] == 'face-chart-transition-descent')['constructor_progress'].update(receipt_sha256='0' * 64))
    paths = sorted(set([CONTRACT, net['packet'], net['validator'], MANIFEST,
                        'research/conjecture_net/outcome_reference.py',
                        'research/voevodsky/results/ramsey-certificate-interface-v1.json',
                        'research/voevodsky/results/ramsey-plane-lattice-v1.json',
                        'research/voevodsky/results/ramsey-marked-patch-v1.json',
                        'research/voevodsky/results/ramsey-uniform-bound-v1.json',
                        'research/voevodsky/results/ramsey-reference-covariance-v1.json',
                        'research/voevodsky/results/ramsey-native-word-trace-v1.json',
                        'research/voevodsky/results/ramsey-native-query-descent-v1.json',
                        'research/voevodsky/results/ramsey-native-query-selection-v1.json',
                        'research/voevodsky/results/ramsey-single-leaf-query-v1.json',
                        'research/voevodsky/results/ramsey-native-region-family-v1.json',
                        'research/voevodsky/results/ramsey-word-family-selection-v1.json',
                        'research/voevodsky/results/ramsey-family-refinement-v1.json',
                        'research/voevodsky/results/ramsey-uniform-relative-v1.json',
                        'research/voevodsky/results/ramsey-exact-source-v1.json',
                        'research/voevodsky/results/ramsey-chart-interpretation-v1.json',
                        'research/voevodsky/results/ramsey-uniform-task-package-v1.json',
                        'research/voevodsky/results/ramsey-single-frame-faces-v1.json',
                        'research/voevodsky/results/ramsey-role-domain-transport-v1.json',
                        'research/voevodsky/results/ramsey-native-PN-overlap-span-v1.json'] + net['source_context']))
    result = {
        'schema': 'marici.ramsey-net.verification.v32',
        'added_scoped_result_nodes_this_revision': sorted(V32_RESULT_IDS),
        'added_open_gates_this_revision': sorted(V32_OPEN_IDS),
        'coherence_progress': validate_coherence_progress({n['id']: n for n in net['nodes']}, artifact, require),
        'confirmed_prior_work_nodes': sorted(PRIOR_IDS),
        'new_open_prior_work_gates': sorted(NEW_OPEN_IDS),
        'status': 'passed',
        'verification_level': 'net integrity and pinned scoped evidence; not a Ramsey existence proof',
        'coherence_obligation': net['coherence_obligation'],
        'scientific_outcomes_changed': False,
        'previous_scientific_outcomes_changed': False,
        'new_scoped_scientific_outcomes': {},
        'scientific_attempts_replayed_by_this_validator': 0,
        'recorded_scientific_attempts': 20,
        'resolved_nodes': 18,
        'historical_scoped_progress_results': 2,
        'scoped_progress_results_on_open_nodes': 7,
        'consolidated_continuation_receipts': 52,
        'local_revision_admitted_to_graph': False,
        'distinct_evidence_groups': 8,
        'root_outcome': net['objective']['outcome'],
        'node_outcomes': {key: nodes[key]['outcome'] for key in sorted(nodes)},
        'selected_next_attempt': net['recommended_start'],
        'finite_certificate_verifier_implemented': True,
        'new_native_Ramsey_theorem_proved': False,
        'classical_uniform_vertex_bound_recorded': True,
        'native_source_admitted': False,
        'negative_controls_rejected': controls,
        'source_sha256': {p: sha256(artifact(p).read_bytes()).hexdigest() for p in paths},
    }
    target = ROOT / RESULT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key != 'source_sha256'}))


if __name__ == '__main__':
    main()
