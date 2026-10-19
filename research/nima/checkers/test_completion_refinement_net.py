import copy
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import check_completion_refinement_net as checker
from check_completion_refinement_net import CONTRACT, REPO, validate
from outcome_reference import OutcomeReferenceError, load

class SuccessorNetTests(unittest.TestCase):
    def setUp(self):
        self.net = copy.deepcopy(load(REPO, CONTRACT))
        target = next(n for n in self.net['conjectures'] if n['id'] == 'operational-spectral-whole-return-certificate')
        target['outcome'] = None
        # Replay the pre-acceptance checkpoint for the existing component
        # admission regressions; test current accepted state separately below.
        pi = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        if pi['outcome'] == '++':
            pi['outcome'] = None
            pi['progress'] = pi.pop('completed_progress')
        regularity = next(n for n in self.net['conjectures'] if n['id'] == 'completion-phase-metric-regularity')
        if regularity['outcome'] == '++':
            regularity['outcome'] = None
            regularity['progress'] = regularity.pop('completed_progress')
        regularity['progress']['attempt_state'] = 'paused'
        regularity['progress']['pause_reason'] = 'Historical checkpoint retained during pi work.'
        regularity['progress'].pop('supporting_components', None)
        flow = next(n for n in self.net['conjectures'] if n['id'] == 'completion-unit-circle-flow')
        flow['outcome'] = None
        half_turn = next(n for n in self.net['conjectures'] if n['id'] == 'operational-unitary-half-turn')
        if half_turn['outcome'] == '++':
            half_turn['outcome'] = '+-'
            half_turn['attempts'].pop()

    def test_current_analytic_closures_leave_assembly_open(self):
        result = validate(REPO, load(REPO, CONTRACT))
        self.assertEqual(result['local_outcomes']['completion-pi-half-turn'], '++')
        self.assertNotIn('completion-pi-half-turn', result['in_progress'])
        self.assertEqual(result['ready_proof_frontier'], [])
        self.assertEqual(result['blocked_on'], {})
        self.assertEqual(result['local_outcomes']['operational-unitary-half-turn'], '++')
        self.assertEqual(result['local_outcomes']['completion-unit-circle-flow'], '++')
        self.assertNotIn('completion-phase-metric-regularity', result['in_progress'])
        self.assertEqual(result['local_outcomes']['completion-phase-metric-regularity'], '++')
        self.assertTrue(result['terminal'])
        self.assertEqual(result['target_outcome'], '++')
        self.assertEqual(result['net_state'], 'positive_terminal')
        self.assertEqual(result['outcome_counts'], {'++': 7, '+-': 0, 'in_progress': 0, 'paused': 0, 'unattempted': 0})
        self.assertIn('research/nima/agda/TickPhaseDerivativeReduction.agda', result['source_sha256'])

    def test_operational_bundle_does_not_admit_semantic_target(self):
        receipt = load(REPO, 'research/nima/results/operational-whole-return-kernel-fresh.json')
        self.assertEqual(receipt['status'], 'pass')
        self.assertTrue(receipt['operational_kernel_bundle_proved'])
        self.assertTrue(receipt['fresh_closure_completed'])
        self.assertFalse(receipt['standard_real_phase_interpretation_proved'])
        self.assertFalse(receipt['whole_return_proved'])
        self.assertIsNone(receipt['target_outcome'])
        net = load(REPO, CONTRACT)
        target = next(n for n in net['conjectures'] if n['id'] == 'operational-spectral-whole-return-certificate')
        self.assertEqual(target['outcome'], '++')
        target['outcome'] = '++'
        target['attempts'] = [{'intent': 'prove', 'outcome': '++',
                               'receipt': 'research/nima/results/operational-whole-return-kernel-fresh.json'}]
        with self.assertRaisesRegex(OutcomeReferenceError, 'proof/attempt claim mismatch'):
            validate(REPO, net)

    def test_written_spectral_correspondence_needs_additional_acceptance(self):
        path = 'research/nima/results/standard-spectral-correspondence.json'
        receipt = load(REPO, path)
        self.assertEqual(receipt['status'], 'pass')
        self.assertTrue(receipt['fresh_closure_completed'])
        self.assertTrue(receipt['written_semantic_correspondence_supplied'])
        self.assertFalse(receipt['semantic_correspondence_kernel_proved'])
        self.assertFalse(receipt['additional_mixed_level_accepted'])
        self.assertFalse(receipt['whole_return_proved_at_admitted_level'])
        net = load(REPO, CONTRACT)
        target = next(n for n in net['conjectures'] if n['id'] == 'operational-spectral-whole-return-certificate')
        target['outcome'] = '++'
        target['attempts'] = [{'intent': 'prove', 'outcome': '++', 'receipt': path}]
        with self.assertRaisesRegex(OutcomeReferenceError, 'proof/attempt claim mismatch'):
            validate(REPO, net)

    def test_whole_return_requires_scoped_acceptance_and_preserves_level(self):
        net = load(REPO, CONTRACT)
        cases = [
            ('research/nima/contracts/whole-return-mixed-level-acceptance.v1.json', 'accepted', False),
            ('research/nima/contracts/whole-return-mixed-level-acceptance.v1.json', 'claim', 'completion-pi-half-turn'),
            ('research/nima/results/whole-return-mixed-level-accepted.json', 'semantic_correspondence_kernel_proved', True),
            ('research/nima/results/whole-return-mixed-level-accepted.json', 'C1_at_seam_claimed', True),
            ('research/nima/results/whole-return-mixed-level-accepted.json', 'remaining_obligations_at_accepted_level', ['interpretation']),
        ]
        for path, field, value in cases:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'whole-return requires explicit scoped mixed acceptance'):
                    validate(REPO, net)

    def test_whole_return_rejects_cached_and_stale_evidence(self):
        net = load(REPO, CONTRACT)
        def cached(root, path):
            r = load(root, path)
            if path == 'research/nima/results/operational-whole-return-kernel-fresh.json':
                r['fresh_closure_completed'] = False
            return r
        with patch.object(checker, 'load', side_effect=cached):
            with self.assertRaisesRegex(OutcomeReferenceError, 'whole-return lacks fresh operational bundle'):
                validate(REPO, net)
        def stale(root, path):
            r = load(root, path)
            if path == 'research/nima/results/whole-return-mixed-level-accepted.json':
                r['source_sha256']['research/nima/standard-spectral-correspondence.md'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=stale):
            with self.assertRaisesRegex(OutcomeReferenceError, 'whole-return omits dependency pins'):
                validate(REPO, net)

    def test_derivative_reduction_does_not_promote_analytic_bound(self):
        net = load(REPO, CONTRACT)
        path = 'research/nima/results/phase-derivative-reduction-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('local_derivative_bound_proved', True),
                             ('derivative_proved', True), ('full_metric_regularity_proved', True),
                             ('outcome', '++')]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'derivative reduction lacks fresh closure'):
                    validate(REPO, net)

    def test_stale_derivative_reduction_is_rejected(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/phase-derivative-reduction-fresh.json':
                r['source_sha256']['research/nima/agda/TickPhaseDerivativeReduction.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale derivative reduction evidence'):
                validate(REPO, net)

    def test_order_transfer_requires_fresh_proof_without_derivative_overclaim(self):
        net = load(REPO, CONTRACT)
        result = validate(REPO, net)
        self.assertIn('research/nima/agda/TickCompletionOrderLimits.agda', result['source_sha256'])
        self.assertEqual(result['local_outcomes']['completion-phase-metric-regularity'], '++')
        path = 'research/nima/results/completion-order-limits-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('requires_nonzero_increment', True),
                             ('rational_derivative_estimate_proved', True), ('derivative_proved', True),
                             ('outcome', '++')]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'order transfer lacks fresh closure'):
                    validate(REPO, net)

    def test_stale_order_transfer_is_rejected(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/completion-order-limits-fresh.json':
                r['source_sha256']['research/nima/agda/TickCompletionOrderLimits.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale order transfer evidence'):
                validate(REPO, net)

    def test_rational_bound_does_not_claim_all_completion_inputs(self):
        net = load(REPO, CONTRACT)
        result = validate(REPO, net)
        self.assertIn('research/nima/agda/TickRationalPhaseDerivativeBound.agda', result['source_sha256'])
        self.assertEqual(result['local_outcomes']['completion-phase-metric-regularity'], '++')
        path = 'research/nima/results/rational-phase-derivative-bound-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('all_completion_inputs_proved', True),
                             ('explicit_radius_budget_required', False), ('derivative_proved', True),
                             ('outcome', '++')]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'rational bound lacks fresh closure'):
                    validate(REPO, net)

    def test_stale_rational_bound_is_rejected(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/rational-phase-derivative-bound-fresh.json':
                r['source_sha256']['research/nima/agda/TickTrigRelativeRemainder.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale rational bound evidence'):
                validate(REPO, net)

    def test_completion_bound_does_not_claim_derivative_modulus(self):
        net = load(REPO, CONTRACT)
        result = validate(REPO, net)
        self.assertIn('research/nima/agda/TickCompletionRelativeBound.agda', result['source_sha256'])
        self.assertEqual(result['local_outcomes']['completion-phase-metric-regularity'], '++')
        path = 'research/nima/results/completion-relative-bound-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('dyadic_modulus_constructed', True),
                             ('explicit_radius_budget_and_eventual_bounds_required', False),
                             ('derivative_proved', True), ('outcome', '++')]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'completion bound lacks fresh closure'):
                    validate(REPO, net)

    def test_stale_completion_bound_is_rejected(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/completion-relative-bound-fresh.json':
                r['source_sha256']['research/nima/agda/TickCompletionClosedOrder.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale completion bound evidence'):
                validate(REPO, net)

    def test_regularity_requires_fresh_all_input_derivative(self):
        net = load(REPO, CONTRACT)
        path = 'research/nima/results/constructed-phase-derivative-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('dyadic_modulus_constructed', False),
                             ('derivative_proved', False), ('all_completion_scales_times_and_increments', False),
                             ('unitary_half_turn_proved', True), ('remaining_regularity_obligations', ['modulus'])]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'regularity proof lacks fresh all-input'):
                    validate(REPO, net)

    def test_stale_derivative_modulus_blocks_regularity_closure(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/constructed-phase-derivative-fresh.json':
                r['source_sha256']['research/nima/agda/TickPhaseDerivativeModulus.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale proof/attempt evidence'):
                validate(REPO, net)

    def test_flow_requires_fresh_same_phase_closure(self):
        net = load(REPO, CONTRACT)
        path = 'research/nima/results/constructed-unit-circle-flow-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('same_operational_phase', False),
                             ('norm_continuity_and_derivative_proved', False), ('unitary_half_turn_proved', True),
                             ('theorems', ['OperationalUnitCircleFlow', 'operational-unit-circle-flow'])]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'flow proof lacks fresh same-phase'):
                    validate(REPO, net)

    def test_stale_flow_record_blocks_closure(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/constructed-unit-circle-flow-fresh.json':
                r['source_sha256']['research/nima/agda/TickConstructedUnitCircleFlow.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale proof/attempt evidence'):
                validate(REPO, net)

    def test_half_turn_preserves_identification_level_and_history(self):
        net = load(REPO, CONTRACT)
        half = next(n for n in net['conjectures'] if n['id'] == 'operational-unitary-half-turn')
        self.assertEqual([a['outcome'] for a in half['attempts']], ['+-', '+-', '++'])
        path = 'research/nima/results/constructed-unitary-half-turn-fresh.json'
        for field, value in [('fresh_closure_completed', False), ('standard_pi_identification_kernel_proved', True),
                             ('mixed_level_accepted', False), ('same_operational_phase_and_machin_candidate', False),
                             ('whole_return_proved', True)]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'half-turn lacks fresh same-phase'):
                    validate(REPO, net)

    def test_stale_half_turn_assembly_blocks_closure(self):
        net = load(REPO, CONTRACT)
        def altered(root, requested):
            r = load(root, requested)
            if requested == 'research/nima/results/constructed-unitary-half-turn-fresh.json':
                r['source_sha256']['research/nima/agda/TickConstructedUnitaryHalfTurn.agda'] = '0'*64
            return r
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale proof/attempt evidence'):
                validate(REPO, net)

    def test_pi_acceptance_requires_operator_and_preserves_level(self):
        net = load(REPO, CONTRACT)
        pi = next(n for n in net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        receipt_path = pi['attempts'][-1]['receipt']
        acceptance_path = pi['acceptance_record']
        for path, field, value in [(acceptance_path, 'accepted', False),
                                   (acceptance_path, 'operator_instruction', 'implicit'),
                                   (receipt_path, 'standard_pi_identification_kernel_proved', True),
                                   (receipt_path, 'unitary_half_turn_proved', True)]:
            def altered(root, requested):
                r = load(root, requested)
                if requested == path:
                    r[field] = value
                return r
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'explicit scoped mixed-level acceptance'):
                    validate(REPO, net)

    def test_import_is_proved_but_new_target_is_not(self):
        result = validate(REPO, self.net)
        imported = result['imports']['standard-spectral-whole-return-exists']
        self.assertEqual(imported['outcome'], '++')
        self.assertFalse(imported['verification']['completion_backend_verified'])
        self.assertIsNone(result['target_outcome'])
        self.assertFalse(result['terminal'])
        self.assertEqual(set(result['ready_proof_frontier']), {'completion-pi-half-turn', 'completion-phase-metric-regularity'})
        self.assertEqual(result['local_outcomes']['completion-phase-unit-norm'], '++')
        self.assertEqual(result['blocked_on']['completion-unit-circle-flow'], ['completion-phase-metric-regularity'])
        self.assertEqual(result['outcome_counts'], {'++': 2, '+-': 1, 'in_progress': 1, 'paused': 1, 'unattempted': 2})
        self.assertEqual(result['paused']['completion-phase-metric-regularity']['remaining_obligations'], ['PhaseDerivativeLaw'])
        self.assertEqual(result['in_progress']['completion-pi-half-turn']['completed_component'], 'convergent-Machin-candidate')
        self.assertEqual(len(result['blocked_on']['operational-spectral-whole-return-certificate']), 1)
        self.assertEqual(result['local_outcomes']['operational-unitary-half-turn'], '+-')

    def test_no_cached_or_conditional_norm_promotion(self):
        path = self.net['conjectures'][0]['attempts'][-1]['receipt']
        for field, value in [('fresh_closure_completed', False), ('norm_bound_is_assumed_input', True)]:
            def altered(root, requested):
                result = load(root, requested)
                if requested == path:
                    result[field] = value
                return result
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh unconditional closure'):
                    validate(REPO, self.net)

    def test_no_cached_or_full_goal_continuity_promotion(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-phase-metric-regularity')
        path = node['progress']['component_receipt']
        for field, value in [('fresh_closure_completed', False), ('derivative_proved', True), ('outcome', '++')]:
            def altered(root, requested):
                result = load(root, requested)
                if requested == path:
                    result[field] = value
                return result
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh component closure or overclaims'):
                    validate(REPO, self.net)

    def test_no_candidate_to_endpoint_promotion(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = node['progress']['component_receipt']
        for field, value in [('fresh_closure_completed', False), ('pi_endpoints_proved', True),
                             ('assumed_arctangent_or_pi_constant', True), ('outcome', '++')]:
            def altered(root, requested):
                result = load(root, requested)
                if requested == path:
                    result[field] = value
                return result
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh component closure or overclaims'):
                    validate(REPO, self.net)

    def test_addition_foundations_are_pinned_without_resolving_pi(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        self.assertEqual(progress['supporting_components'][0]['id'], 'trig-addition-foundations')
        self.assertIn(progress['supporting_components'][0]['receipt'], result['source_sha256'])
        self.assertIn('research/nima/agda/TickTrigAdditionResidual.agda', result['source_sha256'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])

    def test_addition_foundations_cannot_promote_completion_laws(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = node['progress']['supporting_components'][0]['receipt']
        mutations = [('fresh_closure_completed', False), ('fresh_dependency_check', False),
                     ('sources_stable', False), ('outcome', '++'),
                     ('completion_addition_laws_proved', True), ('arctangent_cayley_bridge_proved', True),
                     ('pi_endpoints_proved', True), ('standard_pi_identification_kernel_proved', True),
                     ('all_later_cutoffs', False), ('uniform_on_bounded_input_pairs', False),
                     ('rational_partial_sum_transfer_freshly_proved', False), ('theorems', [])]
        for field, value in mutations:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == path:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh component closure or overclaim'):
                    validate(REPO, self.net)

    def test_stale_addition_foundations_are_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = node['progress']['supporting_components'][0]['receipt']
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/agda/TickTrigAdditionResidual.agda'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_unknown_or_duplicate_supporting_component_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        supporting = node['progress']['supporting_components']
        original = copy.deepcopy(supporting[0])
        supporting[0]['id'] = 'unreviewed-proof'
        with self.assertRaisesRegex(OutcomeReferenceError, 'unknown supporting component'):
            validate(REPO, self.net)
        supporting[:] = [original, original]
        with self.assertRaisesRegex(OutcomeReferenceError, 'duplicate supporting component'):
            validate(REPO, self.net)

    def test_completion_addition_is_admitted_without_pi_promotion(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        addition = next(c for c in progress['supporting_components'] if c['id'] == 'completion-trig-addition')
        self.assertIn(addition['receipt'], result['source_sha256'])
        self.assertIn('research/nima/agda/TickCompletionTrigAddition.agda', result['source_sha256'])
        self.assertIn('research/nima/agda/TickPhaseComposition.agda', result['source_sha256'])
        self.assertEqual(progress['remaining_obligations'], [
            'standard-pi identification at the accepted formal level'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])
        self.assertIn('completion-phase-metric-regularity', result['paused'])

    def test_completion_addition_receipt_scope_is_strict(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'completion-trig-addition')
        mutations = [('fresh_closure_completed', False), ('fresh_dependency_check', False),
                     ('sources_stable', False), ('outcome', '++'),
                     ('completion_addition_laws_proved', False), ('phase_addition_law_proved', False),
                     ('all_completion_inputs', False), ('all_completion_scales_and_times', False),
                     ('uses_operational_sine_cosine_and_phase', False), ('assumed_addition_law', True),
                     ('arctangent_cayley_bridge_proved', True), ('pi_endpoints_proved', True),
                     ('derivative_proved', True), ('standard_pi_identification_kernel_proved', True),
                     ('unitary_half_turn_proved', True), ('full_claim_proved', True),
                     ('component_scope_id', 'rational-inputs-only'), ('module', 'TickTrigPartialSumTransfer'),
                     ('theorems', []), ('remaining_obligations', []), ('command', ['agda', '--safe'])]
        for field, value in mutations:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == path:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh unconditional closure or overclaims'):
                    validate(REPO, self.net)

    def test_completed_addition_obligation_requires_admitted_component(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        node['progress']['supporting_components'] = [c for c in node['progress']['supporting_components']
                                                   if c['id'] != 'completion-trig-addition']
        with self.assertRaisesRegex(OutcomeReferenceError, 'remaining obligations'):
            validate(REPO, self.net)

    def test_stale_completion_addition_is_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'completion-trig-addition')
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/agda/TickCompletionTrigAddition.agda'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_cayley_is_pinned_without_parent_promotion(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        component = next(c for c in progress['supporting_components'] if c['id'] == 'operational-cayley-grid')
        self.assertIn(component['receipt'], result['source_sha256'])
        self.assertIn('research/nima/agda/TickOperationalCayleyIdentity.agda', result['source_sha256'])
        self.assertNotIn('operational arctangent/Cayley bridge', progress['remaining_obligations'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])
        self.assertFalse(result['terminal'])

    def test_cayley_scope_and_freshness_are_strict(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'operational-cayley-grid')
        mutations = [('fresh_dependency_check', False), ('sources_stable', False),
                     ('operational_cayley_bridge_proved', False), ('machin_endpoints_proved', True),
                     ('unitary_half_turn_proved', True), ('operational_cayley_bridge_domain', 'all reals'),
                     ('concrete_cayley_invariant_constancy_proved', False),
                     ('module', 'TickCayleyInvariantStep'), ('command', ['agda', '--safe'])]
        for field, value in mutations:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == path:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh scoped closure or overclaims'):
                    validate(REPO, self.net)

    def test_stale_cayley_is_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'operational-cayley-grid')
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/agda/TickOperationalCayleyIdentity.agda'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_cayley_removal_reopens_obligation(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        node['progress']['supporting_components'] = [c for c in node['progress']['supporting_components']
                                                   if c['id'] != 'operational-cayley-grid']
        with self.assertRaisesRegex(OutcomeReferenceError, 'remaining obligations'):
            validate(REPO, self.net)

    def test_endpoint_reduction_is_not_an_endpoint_proof(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        component = next(c for c in progress['supporting_components'] if c['id'] == 'machin-endpoint-reduction')
        self.assertIn(component['receipt'], result['source_sha256'])
        self.assertFalse(load(REPO, component['receipt'])['pi_endpoints_proved'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])
        for field, value in [('fresh_closure_completed', False), ('outcome', '++'),
                             ('rational_machin_gate_proved', True), ('pi_endpoints_proved', True),
                             ('theorems', []), ('endpoint_reduction_proved', False)]:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == component['receipt']:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh conditional closure or overclaims'):
                    validate(REPO, self.net)

    def test_stale_endpoint_reduction_is_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'machin-endpoint-reduction')
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/agda/TickMachinCayleyInputs.agda'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_endpoints_are_admitted_but_standard_pi_remains_open(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        component = next(c for c in progress['supporting_components'] if c['id'] == 'machin-endpoints')
        self.assertIn(component['receipt'], result['source_sha256'])
        self.assertEqual(progress['remaining_obligations'], ['standard-pi identification at the accepted formal level'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])
        for field, value in [('fresh_closure_completed', False), ('outcome', '++'),
                             ('machin_endpoints_proved', False), ('standard_pi_identification_kernel_proved', True),
                             ('unitary_half_turn_proved', True), ('theorems', [])]:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == component['receipt']:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh closure or overclaim'):
                    validate(REPO, self.net)

    def test_endpoint_removal_reopens_obligation(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        node['progress']['supporting_components'] = [c for c in node['progress']['supporting_components'] if c['id'] != 'machin-endpoints']
        with self.assertRaisesRegex(OutcomeReferenceError, 'remaining obligations'):
            validate(REPO, self.net)

    def test_stale_endpoint_proof_is_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'machin-endpoints')
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/agda/TickMachinRationalGate.agda'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_reference_series_does_not_identify_pi_by_renaming(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        component = next(c for c in progress['supporting_components'] if c['id'] == 'machin-reference-series')
        self.assertIn(component['receipt'], result['source_sha256'])
        self.assertEqual(progress['remaining_obligations'], ['standard-pi identification at the accepted formal level'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])
        for field, value in [('fresh_closure_completed', False), ('reference_pi_instantiated', True),
                             ('standard_pi_identification_kernel_proved', True), ('theorems', []),
                             ('machin_series_convergence_proved', False)]:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == component['receipt']:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'fresh conditional closure or overclaims'):
                    validate(REPO, self.net)

    def test_stale_reference_series_is_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'machin-reference-series')
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/agda/TickMachinReferenceSeries.agda'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_written_identification_cannot_promote_kernel_claim(self):
        result = validate(REPO, self.net)
        progress = result['in_progress']['completion-pi-half-turn']
        component = next(c for c in progress['supporting_components'] if c['id'] == 'standard-real-identification-written')
        self.assertIn(component['receipt'], result['source_sha256'])
        self.assertIsNone(result['local_outcomes']['completion-pi-half-turn'])
        for field, value in [('standard_pi_identification_kernel_proved', True), ('outcome', '++'),
                             ('mixed_level_acceptance_required', False), ('full_claim_promoted', True)]:
            def altered(root, requested):
                receipt = load(root, requested)
                if requested == component['receipt']:
                    receipt[field] = value
                return receipt
            with self.subTest(field=field), patch.object(checker, 'load', side_effect=altered):
                with self.assertRaisesRegex(OutcomeReferenceError, 'overclaims kernel verification'):
                    validate(REPO, self.net)

    def test_stale_written_identification_is_rejected(self):
        node = next(n for n in self.net['conjectures'] if n['id'] == 'completion-pi-half-turn')
        path = next(c['receipt'] for c in node['progress']['supporting_components'] if c['id'] == 'standard-real-identification-written')
        def altered(root, requested):
            receipt = load(root, requested)
            if requested == path:
                receipt['source_sha256']['research/nima/standard-pi-identification.md'] = '0'*64
            return receipt
        with patch.object(checker, 'load', side_effect=altered):
            with self.assertRaisesRegex(OutcomeReferenceError, 'stale supporting component evidence'):
                validate(REPO, self.net)

    def test_pause_is_not_an_outcome_or_a_fresh_attempt(self):
        result = validate(REPO, self.net)
        claim = 'completion-phase-metric-regularity'
        self.assertIsNone(result['local_outcomes'][claim])
        self.assertNotIn(claim, result['in_progress'])
        self.assertIn(claim, result['paused'])

    def test_no_bare_resolution_admission(self):
        self.net['conjectures'][-1]['outcome'] = '++'
        with self.assertRaisesRegex(OutcomeReferenceError, 'proof-receipt admission'):
            validate(REPO, self.net)

    def test_no_automatic_prerequisite_aggregation(self):
        for n in self.net['conjectures'][:-1]:
            n['outcome'] = '++'
        with self.assertRaisesRegex(OutcomeReferenceError, 'proof-receipt admission|in-progress component'):
            validate(REPO, self.net)

    def test_blocked_check_replaces_old_success_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'result.json'
            output.write_text('{"status":"pass"}', encoding='utf-8')
            with patch.object(checker, 'OUT', output), patch.object(checker, 'load', side_effect=OutcomeReferenceError('stale import')):
                with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as raised:
                    checker.main()
            self.assertEqual(raised.exception.code, 1)
            result = json.loads(output.read_text(encoding='utf-8'))
            self.assertEqual(result['status'], 'blocked')
            self.assertFalse(result['scientific_outcome_recorded'])
            self.assertIsNone(result['target_outcome'])

    def test_cycle_is_rejected(self):
        self.net['conjectures'][0]['depends_on'] = [self.net['conjectures'][-1]['id']]
        with self.assertRaisesRegex(OutcomeReferenceError, 'cyclic'):
            validate(REPO, self.net)

    def test_unknown_dependency_is_rejected(self):
        self.net['conjectures'][0]['depends_on'] = ['missing']
        with self.assertRaisesRegex(OutcomeReferenceError, 'unknown dependency'):
            validate(REPO, self.net)

if __name__ == '__main__':
    unittest.main()
