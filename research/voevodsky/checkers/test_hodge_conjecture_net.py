"""Regression/hostile tests for the Hodge research setup, not Hodge truth."""
import copy
import json
import subprocess
import sys
import unittest

from check_hodge_conjecture_net import load_bundle, validate, validate_pins, load, digest, ROOT
from check_hodge_obstruction_controls import FIXTURES, evaluate
from check_hodge_cycle_map_scope import CONTRACT as SCOPE_CONTRACT, validate_scope, factor
from check_hodge_cycle_packet_dictionary import (
    CONTRACT as DICTIONARY_CONTRACT, validate_dictionary, boundary, cross, prism, lift, add)
from check_hodge_literature_boundary_audit import (
    CONTRACT as AUDIT_CONTRACT, validate_audit, validate_sources, weil_forms, pullback_one_plus_i)
from check_hodge_explicit_sixfold_candidate import (
    CONTRACT as CANDIDATE_CONTRACT, validate_candidate, exact_core, sparse_rank,
    base_J, lie_action, full_pullback)
from check_hodge_weil_projector import (
    CONTRACT as PROJECTOR_CONTRACT, validate_projector, projection_polynomial,
    MODULI, remainder, pmul, padd, witness_coefficients)
from check_hodge_tautological_witness_search import (
    CONTRACT as SEARCH_CONTRACT, validate_search, fourier, scale, DS, wedge,
    exact_core as search_core)
from check_hodge_weil_projector import apply_polynomial, combine
from check_hodge_middle_hodge_kernel import (
    CONTRACT as KERNEL_CONTRACT, validate_kernel, modular_rank, residue, cyclic_product,
    exact_core as kernel_core)
from check_hodge_secant_sheaf_transplant import (
    CONTRACT as TRANSPLANT_CONTRACT, validate_transplant, validate_sources as validate_transplant_sources,
    valuation3, norm as gaussian_norm, gdet, igusa_rank_two)
from check_hodge_split_eightfold_stabilization import (
    CONTRACT as STABILIZATION_CONTRACT, validate_stabilization,
    forward as stabilize, recover as recover_stabilization, integrate_B, E_B,
    exact_core as stabilization_core)
from check_hodge_eightfold_weil_filter import (
    CONTRACT as EIGHTFOLD_FILTER_CONTRACT, validate_filter, weil_filter, filtered_reverse,
    R_B, I_B, exact_core as eightfold_filter_core)
from check_hodge_eightfold_hodge_kernel import (
    CONTRACT as EIGHTFOLD_KERNEL_CONTRACT, validate_kernel as validate_eightfold_kernel,
    exact_core as eightfold_hodge_core, channels, contraction, insertion,
    exceptional_projector, chow_exceptional_action)
from check_hodge_chern_witness_transfer import (
    CONTRACT as CHERN_TRANSFER_CONTRACT, validate_transfer,
    exact_core as chern_transfer_core, normalized_chern, locally_free_restriction,
    times as chern_times, pscale as chern_scale, chern_character)
from check_hodge_reflexive_rank_reduction import (
    CONTRACT as REDUCTION_CONTRACT, validate_reduction, strata,
    exact_core as reduction_core)
from check_hodge_cyclic_prym_audit import (
    CONTRACT as PRYM_CONTRACT, SNAPSHOT as PRYM_SNAPSHOT, validate_audit as validate_prym,
    validate_sources as validate_prym_sources, exact_core as prym_core)
from check_hodge_gaussian_principal_isogeny import (
    CONTRACT as PRINCIPAL_CONTRACT, validate_isogeny, exact_core as principal_core,
    q_pull, q_push, forward_Y, reverse_Y, channels_Y)
from check_hodge_principal_prym_membership import (
    CONTRACT as MEMBERSHIP_CONTRACT, SNAPSHOT as MEMBERSHIP_SNAPSHOT,
    validate_membership, validate_sources as validate_membership_sources,
    exact_core as membership_core, coprime_genus_bound)
from check_hodge_indecomposable_principal_model import (
    CONTRACT as INDECOMPOSABLE_CONTRACT, validate_model, exact_core as indecomposable_core,
    f_pull, forward_new, reverse_new)
from check_hodge_y2_curve_audit import (
    CONTRACT as Y2_CURVE_CONTRACT, SNAPSHOT as Y2_CURVE_SNAPSHOT,
    validate_audit as validate_y2_curve, validate_sources as validate_y2_curve_sources,
    exact_core as y2_curve_core, hyperelliptic_elliptic_genus_bound,
    trigonal_free_involution_obstruction, conditional_prym_gate)
from check_hodge_hyperelliptic_bottom_audit import (
    CONTRACT as BOTTOM_CONTRACT, validate_audit as validate_bottom,
    exact_core as bottom_core, torsion_roots, conditional_family,
    unique_bielliptic_involution_for_genus)
from check_hodge_bielliptic_lift_audit import (
    CONTRACT as LIFT_CONTRACT, validate_audit as validate_lift,
    exact_core as lift_core, norm as lift_norm, pullback as lift_pullback,
    deck_action as lift_deck_action, lift_type)
from check_hodge_commuting_prym_audit import (
    CONTRACT as COMMUTING_CONTRACT, SNAPSHOT as COMMUTING_SNAPSHOT,
    validate_audit as validate_commuting, validate_sources as validate_commuting_sources,
    exact_core as commuting_core, quotient_case, valuation3 as commuting_v3)
from check_hodge_even_scalar_cover import (
    CONTRACT as EVEN_CONTRACT, validate_audit as validate_even,
    exact_core as even_core, models as even_models, gcd as polynomial_gcd,
    derivative as polynomial_derivative)
from check_hodge_asymmetric_scalar_cover import (
    CONTRACT as ASYMMETRIC_CONTRACT, validate_control as validate_asymmetric,
    exact_core as asymmetric_core, source_equations, point_profile,
    modgcd_degree, good_reduction)
from check_hodge_asymmetric_reflections import (
    CONTRACT as AUT_CONTRACT, validate_certificate as validate_aut,
    exact_core as aut_core, BranchRing, elliptic_points, double, eight,
    reflection_residue, translation_residue)
from check_hodge_asymmetric_frobenius import (
    CONTRACT as FROB_CONTRACT, COUNTS as FROB_COUNTS, FACTORS as FROB_FACTORS,
    validate_certificate as validate_frob, verify_counts as verify_frob_counts,
    newton_polynomial, factor_degree_certificate, small49_counts)
from check_hodge_asymmetric_absolute import (
    CONTRACT as ABS_CONTRACT, validate_certificate as validate_absolute,
    possible_orders, cyclotomic, ratio_polynomial, verify_ratio_resultants,
    root_ratio_certificate)
from check_hodge_scalar_family_localization import (
    CONTRACT as FAMILY_CONTRACT, BASE as FAMILY_BASE,
    validate_certificate as validate_family, branch_norm as family_norm,
    residues as family_residues, mod_seven as family_mod_seven,
    sieve as family_sieve, geometry as family_geometry, finite_controls as family_controls)
from check_hodge_scalar_polarized_obstruction import (
    CONTRACT as SCALAR_POLARIZED_CONTRACT, validate_certificate as validate_scalar_polarized,
    curve_map_degree, joint_degrees, independent_elliptic_genus_bound,
    minimum_elliptic_degree, census as scalar_polarized_census, exact_core as scalar_polarized_core)
from check_hodge_nonlifting_polarized_obstruction import (
    CONTRACT as NONLIFTING_CONTRACT, validate_certificate as validate_nonlifting,
    birational_case, joint_case, v4_control, theta_gate as nonlifting_theta_gate,
    exact_core as nonlifting_core)
from check_hodge_equivariant_tetragonal_gate import (
    CONTRACT as TETRAGONAL_CONTRACT, validate_certificate as validate_tetragonal,
    pencil_joint_case as tetragonal_joint_case, even_partition as tetragonal_even_partition,
    ramification_budget as tetragonal_budget, legendre_j as tetragonal_j,
    lift_order as tetragonal_lift_order, exact_core as tetragonal_core)
from check_hodge_eightfold_literature_audit import (
    CONTRACT as EIGHTFOLD_LITERATURE_CONTRACT, validate_audit as validate_eightfold_literature,
    secant_character, in_secant_plane, cyclic_genera, validate_sources as validate_eightfold_literature_sources)
from check_hodge_secant_local_ext_gate import (
    CONTRACT as SECANT_LOCAL_CONTRACT, validate_gate as validate_secant_local,
    incidence as secant_incidence, local_lengths as secant_local_lengths,
    local_models as secant_local_models, exact_local_checks as secant_local_checks,
    variables as secant_variables, generates_maximal as secant_generates_maximal,
    minimal as secant_minimal)
from check_hodge_secant_source_semiregularity import (
    CONTRACT as SOURCE_SEMI_CONTRACT, validate_scope as validate_source_semi,
    exact_core as source_semi_core, character as source_semi_character,
    hkr_columns as source_hkr_columns, rank as source_hkr_rank,
    annihilator_residual, local_at_square, euler_pairing,
    contract as source_contract, bivector as source_bivector,
    add as source_add, theta as source_theta, wedge as source_wedge)
import check_hodge_secant_criterion_persistence as persistence
import check_hodge_ramified_trigonal_family as ramified_family
import check_hodge_trigonal_principal_match_obstruction as principal_match
import check_hodge_cyclic_prym_odd_axis_obstruction as odd_axis
import check_hodge_two_branch_odd_axis_obstruction as two_branch
import check_hodge_even_axis_principal_model as even_axis
import check_hodge_even_axis_coupled_kummer_gate as coupled_kummer
import check_hodge_even_axis_joint_degree_gate as joint_degree
import check_hodge_minimal_axis_scalar_source as minimal_source
import check_hodge_minimal_axis_frobenius_obstruction as minimal_frob
import check_hodge_minimal_axis_b_line as b_line
import check_hodge_minimal_axis_second_prime as second_prime
import check_hodge_scalar_reflection_decomposition as reflection
import check_hodge_off_reflection_a_line as a_line
import check_hodge_off_reflection_joint_screen as joint_screen
import check_hodge_inert_elliptic_projector as inert
import check_hodge_off_reflection_third_prime as third
import check_hodge_scalar_37_census as census37
from fractions import Fraction
from unittest.mock import patch


class HodgeNetTests(unittest.TestCase):
    def setUp(self):
        self.bundle = copy.deepcopy(load_bundle())
        self.c, self.a, self.refs, self.controls, self.registry = self.bundle

    def validate(self):
        return validate(*self.bundle)

    def test_live_net_has_only_refutation_frontier_with_all_ports_accounted_for(self):
        result = self.validate()
        self.assertEqual(result['node_count'], 70)
        self.assertEqual(result['frontier'], ['all-algebraic-cycles-annihilation', 'fixed-candidate-nonalgebraicity', 'higher-coherence-counterexample-existence'])
        self.assertEqual(result['open_research_nodes'], 5)
        self.assertEqual(result['active_refutation_count'], 4)
        self.assertEqual(result['dismissed_construction_count'], 52)
        self.assertEqual(result['input_port_count'], 143)
        self.assertEqual(result['cross_net_connections'], 7)
        self.assertEqual(len(result['external_obligations']), 1)
        self.assertGreater(result['input_port_count'], result['cross_net_connections'])

    def test_only_reviewed_bounded_results_and_scoped_rejection_are_resolved(self):
        resolved = [n for n in self.c['conjectures'] if n['status'] == 'resolved']
        self.assertEqual([n['id'] for n in resolved], ['scope-and-cycle-map', 'literature-boundary-audit', 'positive-and-rational-controls',
                                                    'candidate-variety-and-class', 'packet-coherence-dictionary',
                                                    'bare-chain-closure-obstruction', 'obstruction-construction',
                                                    'uniform-weil-projector-annihilation', 'cohomology-descent', 'rational-survival',
                                                    'candidate-hodge-membership', 'candidate-obstruction-nonzero',
                                                    'tautological-power-witness-search', 'generic-middle-hodge-kernel', 'secant-sheaf-transplant', 'split-eightfold-stabilization', 'eightfold-weil-filter', 'eightfold-full-hodge-kernel', 'higher-chern-witness-transfer', 'reflexive-rank-reduction', 'cyclic-quartic-prym-transplant', 'gaussian-principal-isogeny', 'principal-prym-membership-audit', 'indecomposable-principal-model', 'y2-jacobian-low-gonality-transplant', 'hyperelliptic-bottom-prym-transplant', 'bielliptic-involution-lift-transplant', 'commuting-prym-factor-transplant', 'inversion-symmetric-scalar-transplant', 'asymmetric-scalar-cover-control', 'asymmetric-cover-automorphisms', 'asymmetric-prym-frobenius7', 'asymmetric-scalar-target-transplant', 'scalar-family-localization', 'scalar-polarized-prym-transplant', 'nonlifting-polarized-prym-transplant', 'equivariant-tetragonal-gate', 'eightfold-literature-and-secant-audit', 'secant-local-ext-gate', 'secant-source-weak-semiregularity-transplant', 'eightfold-secant-weak-criterion-transplant', 'ramified-trigonal-auxiliary-family', 'ramified-trigonal-principal-target-transplant', 'y2-etale-cyclic-quartic-polarized-transplant', 'y2-two-branch-cyclic-quartic-transplant', 'even-axis-principal-model', 'even-axis-coupled-kummer-gate', 'even-axis-joint-degree-gate', 'minimal-axis-scalar-source', 'minimal-axis-b-line-screen', 'minimal-axis-scalar-target-transplant', 'minimal-axis-second-prime-screen', 'minimal-axis-b6-target-transplant', 'scalar-reflection-quotient-decomposition', 'reflection-symmetric-scalar-target-transplant', 'off-reflection-a-line-screen', 'off-reflection-a-line-target-transplant', 'off-reflection-two-prime-screen', 'off-reflection-two-prime-target-transplant', 'inert-elliptic-projector-gate', 'inert-degree-parity-target-transplant', 'off-reflection-third-prime-generic-gate', 'third-prime-and-generic-target-transplant', 'scalar-37-full-screen', 'scalar-37-typed-polarized-target-transplant'])
        self.assertEqual(next(n for n in resolved if n['id'] == 'bare-chain-closure-obstruction')['verdict'], 'rejected')
        self.assertTrue(all(n['outcome'] is None for n in self.c['conjectures']))

    def test_hodge_outcome_promotion_rejected(self):
        self.c['classical_conjecture']['outcome'] = '-+'
        with self.assertRaisesRegex(ValueError, 'Hodge outcome'):
            self.validate()

    def test_boundary_promotion_rejected(self):
        self.c['boundary']['Hodge_refuted'] = True
        with self.assertRaisesRegex(ValueError, 'promotion'):
            self.validate()

    def test_integral_substitution_rejected(self):
        self.c['classical_conjecture']['coefficients'] = 'Z'
        with self.assertRaisesRegex(ValueError, 'coefficients'):
            self.validate()

    def test_nonsmooth_scope_rejected(self):
        self.c['classical_conjecture']['smooth'] = False
        with self.assertRaisesRegex(ValueError, 'scope'):
            self.validate()

    def test_divisor_only_classical_quantifier_rejected(self):
        self.c['classical_conjecture']['quantifiers']['cycles'] = 'divisor_products_only'
        with self.assertRaisesRegex(ValueError, 'quantifier'):
            self.validate()

    def test_cycle_class_equivalence_assumption_rejected(self):
        self.c['scope']['cycle_map_is_equivalence'] = True
        with self.assertRaisesRegex(ValueError, 'not equivalence'):
            self.validate()

    def test_torsion_target_cannot_replace_rational_obstruction(self):
        self.c['obstruction_contract']['target_coefficients'] = 'Z/2'
        with self.assertRaisesRegex(ValueError, 'obstruction'):
            self.validate()

    def test_divisor_only_annihilation_cannot_close_all_cycle_gate(self):
        self.c['obstruction_contract']['required_annihilation'] = 'divisor_products_only'
        with self.assertRaisesRegex(ValueError, 'annihilation'):
            self.validate()

    def test_representative_level_detector_cannot_replace_class_invariant(self):
        self.c['obstruction_contract']['required_domain'] = 'selected_packet_histories'
        with self.assertRaisesRegex(ValueError, 'representative-level'):
            self.validate()

    def test_omitting_rational_survival_property_rejected(self):
        self.c['obstruction_contract']['required_properties'].remove('non_torsion_rational_detection')
        with self.assertRaisesRegex(ValueError, 'gate bypass'):
            self.validate()

    def test_dependency_cycle_rejected_by_shared_graph_validator(self):
        self.c['conjectures'][0]['depends_on'] = ['counterexample-assembly']
        with self.assertRaisesRegex(ValueError, 'cycle'):
            self.validate()

    def test_unknown_local_dependency_rejected(self):
        self.c['conjectures'][0]['depends_on'] = ['imaginary-node']
        with self.assertRaisesRegex(ValueError, 'unknown dependency'):
            self.validate()

    def test_rejected_result_cannot_satisfy_constructed_witness_port(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'packet-coherence-dictionary')
        node['required_verdicts']['positive-and-rational-controls'] = 'rejected'
        with self.assertRaisesRegex(ValueError, 'constructed-witness'):
            self.validate()

    def test_missing_all_cycle_input_cannot_bypass_assembly(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'counterexample-assembly')
        node['depends_on'].remove('all-algebraic-cycles-annihilation')
        node['required_verdicts'].pop('all-algebraic-cycles-annihilation')
        with self.assertRaisesRegex(ValueError, 'assembly bypass'):
            self.validate()

    def test_independent_review_port_cannot_disappear(self):
        self.a['external_obligations'] = []
        with self.assertRaisesRegex(ValueError, 'review gate'):
            self.validate()

    def test_missing_foundational_link_rejected(self):
        self.a['connections'].pop(0)
        with self.assertRaisesRegex(ValueError, 'link coverage'):
            self.validate()

    def test_wrong_external_endpoint_rejected(self):
        self.a['connections'][0]['source_node'] = 'imaginary-node'
        with self.assertRaisesRegex(ValueError, 'endpoint'):
            self.validate()

    def test_context_reference_cannot_become_proof_import(self):
        self.a['connections'][0]['proof_bearing'] = True
        with self.assertRaisesRegex(ValueError, 'promoted'):
            self.validate()

    def test_context_port_type_mismatch_rejected(self):
        self.a['connections'][0]['type'] = 'candidate_review'
        with self.assertRaisesRegex(ValueError, 'port type'):
            self.validate()

    def test_undeclared_receiving_port_rejected(self):
        self.c['conjectures'][0]['external_inputs'].remove('common-foundations-context')
        with self.assertRaisesRegex(ValueError, 'input port'):
            self.validate()

    def test_main_net_backlink_is_required(self):
        self.refs['identity']['research_branches'] = []
        with self.assertRaisesRegex(ValueError, 'backlink'):
            self.validate()

    def test_main_net_backlink_cannot_discharge_parent(self):
        self.refs['identity']['research_branches'][0]['discharges_parent'] = True
        with self.assertRaisesRegex(ValueError, 'backlink'):
            self.validate()

    def test_registry_discovery_is_required(self):
        self.registry['nets'] = [e for e in self.registry['nets'] if e['id'] != self.c['id']]
        with self.assertRaisesRegex(ValueError, 'not registered'):
            self.validate()

    def test_finite_controls_cannot_resolve_obstruction_construction(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'obstruction-construction')
        node.update(status='resolved', verdict='constructed', evidence=['control-bundle'])
        with self.assertRaisesRegex(ValueError, 'projector gate binding'):
            self.validate()

    def test_scope_lemma_cannot_resolve_candidate_specific_descent(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'cohomology-descent')
        node.update(status='resolved', verdict='constructed', evidence=['cycle-map-scope'])
        with self.assertRaisesRegex(ValueError, 'projector gate binding'):
            self.validate()

    def test_missing_scope_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'cycle-map-scope']
        with self.assertRaisesRegex(ValueError, 'artifact census'):
            self.validate()

    def test_rejected_closure_route_cannot_become_constructed(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'bare-chain-closure-obstruction')
        node['verdict'] = 'constructed'
        with self.assertRaisesRegex(ValueError, 'rejection binding'):
            self.validate()

    def test_dictionary_cannot_close_universal_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved', verdict='constructed', evidence=['cycle-packet-dictionary'])
        with self.assertRaisesRegex(ValueError, 'research resolution'):
            self.validate()

    def test_rejected_candidate_history_cannot_disappear(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'obstruction-construction')
        node['rejected_candidate_controls'] = []
        with self.assertRaisesRegex(ValueError, 'history lost'):
            self.validate()

    def test_dictionary_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'cycle-packet-dictionary')
        altered = load(artifact['receipt'])
        altered['prism_four_chain_top_simplex_count'] = 479
        with patch('check_hodge_conjecture_net.dictionary_report', return_value=altered):
            with self.assertRaisesRegex(ValueError, 'dictionary receipt stale'):
                self.validate()

    def test_family_shortlist_cannot_select_actual_candidate(self):
        self.c['scope']['candidate_X'] = 'generic nonsplit sixfold'
        with self.assertRaisesRegex(ValueError, 'candidate selection'):
            self.validate()

    def test_literature_audit_cannot_close_hodge_membership(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'candidate-hodge-membership')
        node.update(status='resolved', verdict='constructed', evidence=['literature-boundary-audit'])
        with self.assertRaisesRegex(ValueError, 'membership binding'):
            self.validate()

    def test_literature_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'literature-boundary-audit')
        altered = load(artifact['receipt'])
        altered['monodromy_rank_Q_upper_bound'] = 6
        with patch('check_hodge_conjecture_net.audit_report', return_value=altered):
            with self.assertRaisesRegex(ValueError, 'literature receipt stale'):
                self.validate()

    def test_candidate_cannot_change_codimension_without_successor(self):
        self.c['scope']['candidate_p'] = 2
        with self.assertRaisesRegex(ValueError, 'candidate selection'):
            self.validate()

    def test_divisor_nonmembership_cannot_close_all_cycle_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved', verdict='constructed', evidence=['explicit-sixfold-candidate'])
        with self.assertRaisesRegex(ValueError, 'research resolution'):
            self.validate()

    def test_missing_candidate_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'explicit-sixfold-candidate']
        with self.assertRaisesRegex(ValueError, 'artifact census'):
            self.validate()

    def test_candidate_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'explicit-sixfold-candidate')
        altered = load(artifact['receipt'])
        altered['alpha_x_torus_period'] = 0
        with patch('check_hodge_conjecture_net.candidate_report', return_value=altered):
            with self.assertRaisesRegex(ValueError, 'candidate receipt stale'):
                self.validate()

    def test_projector_cannot_close_all_cycle_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved', verdict='constructed', evidence=['weil-projector'])
        with self.assertRaisesRegex(ValueError, 'research resolution'):
            self.validate()

    def test_candidate_map_cannot_be_promoted_to_validated_hodge_obstruction(self):
        self.c['obstruction_contract']['validated_hodge_obstruction'] = True
        with self.assertRaisesRegex(ValueError, 'unreviewed obstruction'):
            self.validate()

    def test_uniform_rejection_cannot_be_constructed(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'uniform-weil-projector-annihilation')
        node['verdict'] = 'constructed'
        with self.assertRaisesRegex(ValueError, 'uniform rejection binding'):
            self.validate()

    def test_projector_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'weil-projector')
        altered = load(artifact['receipt'])
        altered['candidate_value'] = 'O(alpha)=0'
        with patch('check_hodge_conjecture_net.projector_report', return_value=altered):
            with self.assertRaisesRegex(ValueError, 'projector receipt stale'):
                self.validate()

    def test_missing_projector_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'weil-projector']
        with self.assertRaisesRegex(ValueError, 'artifact census'):
            self.validate()

    def test_bounded_library_failure_cannot_close_global_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='rejected',evidence=['tautological-witness-search'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_bounded_library_failure_cannot_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['tautological-witness-search'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_rejected_library_cannot_become_a_constructed_witness(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'tautological-power-witness-search')
        node['verdict'] = 'constructed'
        with self.assertRaisesRegex(ValueError,'bounded witness rejection binding'):
            self.validate()

    def test_bounded_attempt_history_cannot_disappear(self):
        next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')['bounded_attempts'] = []
        with self.assertRaisesRegex(ValueError,'bounded witness history lost'):
            self.validate()

    def test_missing_bounded_search_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'tautological-witness-search']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_search_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'tautological-witness-search')
        altered = load(artifact['receipt'])
        altered['finite_search_count'] = 44
        with patch('check_hodge_conjecture_net.search_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'witness search receipt stale'):
                self.validate()

    def test_Hodge_kernel_does_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['middle-hodge-kernel'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_Hodge_membership_artifact_cannot_replace_full_kernel_certificate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'generic-middle-hodge-kernel')
        node['evidence'] = ['explicit-sixfold-candidate']
        with self.assertRaisesRegex(ValueError,'middle Hodge kernel binding'):
            self.validate()

    def test_kernel_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'middle-hodge-kernel')
        altered = load(artifact['receipt'])
        altered['selected_minor_determinant_mod_prime'] = 0
        with patch('check_hodge_conjecture_net.kernel_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'Hodge kernel receipt stale'):
                self.validate()

    def test_missing_full_kernel_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'middle-hodge-kernel']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_middle_Hodge_progress_cannot_disappear(self):
        next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')['structural_progress'] = []
        with self.assertRaisesRegex(ValueError,'middle Hodge progress lost'):
            self.validate()

    def test_rejected_split_theorem_transplant_cannot_be_a_witness(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'secant-sheaf-transplant')
        node['verdict'] = 'constructed'
        with self.assertRaisesRegex(ValueError,'secant transplant rejection binding'):
            self.validate()

    def test_split_theorem_failure_cannot_close_global_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='rejected',evidence=['secant-sheaf-transplant'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_secant_transplant_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'secant-sheaf-transplant']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_transplant_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'secant-sheaf-transplant')
        altered = load(artifact['receipt'])
        altered['retained_theorem_applicable_to_fixed_isogeny_class'] = True
        with patch('check_hodge_conjecture_net.transplant_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'secant transplant receipt stale'):
                self.validate()

    def test_stabilization_reduction_does_not_close_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['split-eightfold-stabilization'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_stabilization_does_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['split-eightfold-stabilization'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_stabilization_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'split-eightfold-stabilization']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_stabilization_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'split-eightfold-stabilization')
        altered = load(artifact['receipt'])
        altered['full_H8_retraction_image_projector_rank'] = 2
        with patch('check_hodge_conjecture_net.stabilization_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'stabilization receipt stale'):
                self.validate()

    def test_eightfold_filter_does_not_close_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['eightfold-weil-filter'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_eightfold_filter_does_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['eightfold-weil-filter'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_eightfold_filter_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'eightfold-weil-filter']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_eightfold_filter_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'eightfold-weil-filter')
        altered = load(artifact['receipt'])
        altered['rational_Weil_projector_rank'] = 4902
        with patch('check_hodge_conjecture_net.eightfold_filter_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'eightfold filter receipt stale'):
                self.validate()

    def test_full_eightfold_Hodge_space_does_not_close_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['eightfold-hodge-kernel'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_full_eightfold_Hodge_space_does_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['eightfold-hodge-kernel'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_eightfold_Hodge_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'eightfold-hodge-kernel']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_eightfold_Hodge_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'eightfold-hodge-kernel')
        altered = load(artifact['receipt'])
        altered['algebraic_dimension_decided'] = True
        with patch('check_hodge_conjecture_net.eightfold_kernel_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'eightfold Hodge receipt stale'):
                self.validate()

    def test_conditional_Chern_transfer_does_not_supply_a_witness(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['chern-witness-transfer'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_Chern_rank_bounds_do_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['chern-witness-transfer'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_Chern_transfer_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'chern-witness-transfer']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_Chern_transfer_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'chern-witness-transfer')
        altered = load(artifact['receipt'])
        altered['nonzero_Weil_bundle_constructed'] = True
        with patch('check_hodge_conjecture_net.chern_transfer_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'Chern transfer receipt stale'):
                self.validate()

    def test_rank_reduction_does_not_supply_a_missing_threefold(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['reflexive-rank-reduction'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_rank_reduction_does_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['reflexive-rank-reduction'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_rank_reduction_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'reflexive-rank-reduction']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_rank_reduction_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'reflexive-rank-reduction')
        altered = load(artifact['receipt'])
        altered['nonzero_Weil_smooth_threefold_constructed'] = True
        with patch('check_hodge_conjecture_net.reduction_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'reflexive reduction receipt stale'):
                self.validate()

    def test_Prym_rejection_does_not_close_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['cyclic-quartic-prym-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_Prym_rejection_does_not_close_all_cycle_gate(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['cyclic-quartic-prym-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_Prym_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'cyclic-quartic-prym-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_Prym_recomputation_detects_receipt_drift(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'cyclic-quartic-prym-audit')
        altered = load(artifact['receipt'])
        altered['alpha_nonalgebraic_proved'] = True
        with patch('check_hodge_conjecture_net.prym_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'cyclic Prym receipt stale'):
                self.validate()

    def test_principal_quotient_does_not_supply_an_algebraic_witness(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['gaussian-principal-isogeny'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_principal_quotient_does_not_prove_all_cycle_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['gaussian-principal-isogeny'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_principal_isogeny_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'gaussian-principal-isogeny']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_principal_isogeny_receipt_recomputed_not_promoted(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'gaussian-principal-isogeny')
        altered = load(artifact['receipt'])
        altered['Prym_cover_constructed'] = True
        with patch('check_hodge_conjecture_net.principal_isogeny_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'principal isogeny receipt stale'):
                self.validate()

    def test_fixed_Prym_exclusion_does_not_complete_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['principal-prym-membership-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_fixed_Prym_exclusion_does_not_prove_all_cycle_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['principal-prym-membership-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_principal_Prym_membership_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'principal-prym-membership-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_principal_Prym_receipt_recomputed_without_global_exclusion(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'principal-prym-membership-audit')
        altered = load(artifact['receipt'])
        altered['all_isogenous_principal_models_excluded'] = True
        with patch('check_hodge_conjecture_net.principal_prym_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'principal Prym receipt stale'):
                self.validate()

    def test_indecomposable_model_does_not_supply_cycle_witness(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['indecomposable-principal-model'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_indecomposable_model_does_not_prove_all_cycle_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['indecomposable-principal-model'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_indecomposable_model_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'indecomposable-principal-model']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_indecomposable_receipt_recomputed_not_promoted_to_Prym(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'indecomposable-principal-model')
        altered = load(artifact['receipt'])
        altered['Prym_cover_constructed'] = True
        with patch('check_hodge_conjecture_net.indecomposable_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'indecomposable model receipt stale'):
                self.validate()

    def test_Jacobian_exclusion_does_not_close_witness_search(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        node.update(status='resolved',verdict='constructed',evidence=['y2-curve-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_Jacobian_exclusion_does_not_prove_all_cycle_annihilation(self):
        node = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        node.update(status='resolved',verdict='constructed',evidence=['y2-curve-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_Y2_curve_artifact_rejected(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'y2-curve-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_Y2_curve_receipt_cannot_select_uncomputed_theta_dimension(self):
        artifact = next(a for a in self.c['artifacts'] if a['id'] == 'y2-curve-audit')
        altered = load(artifact['receipt'])
        altered['actual_theta_singularity_dimension'] = 4
        with patch('check_hodge_conjecture_net.y2_curve_report',return_value=altered):
            with self.assertRaisesRegex(ValueError,'Y2 curve receipt stale'):
                self.validate()

    def test_bottom_exclusion_not_a_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['hyperelliptic-bottom-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_bottom_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'hyperelliptic-bottom-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_formal_roots_cannot_be_matching_cover(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'hyperelliptic-bottom-audit')
        changed = load(a['receipt'])
        changed['actual_cover_matching_Y2_constructed'] = True
        with patch('check_hodge_conjecture_net.bottom_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'bottom-cover receipt stale'):
                self.validate()

    def test_norm_root_filter_not_a_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['bielliptic-lift-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_lift_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'bielliptic-lift-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_abstract_retained_root_cannot_be_target_cover(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'bielliptic-lift-audit')
        changed = load(a['receipt'])
        changed['actual_matching_root_label'] = [1]+[0]*9
        with patch('check_hodge_conjecture_net.lift_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'bielliptic-lift receipt stale'):
                self.validate()

    def test_commuting_root_filter_not_a_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['commuting-prym-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_commuting_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'commuting-prym-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_pulled_root_cannot_be_matching_target(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'commuting-prym-audit')
        changed = load(a['receipt'])
        changed['actual_matching_root_label'] = [1]+[0]*9
        with patch('check_hodge_conjecture_net.commuting_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'commuting Prym receipt stale'):
                self.validate()

    def test_actual_even_tower_not_a_target_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['even-scalar-cover'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_even_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'even-scalar-cover']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_actual_control_cannot_be_promoted_to_Y2_cover(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'even-scalar-cover')
        changed = load(a['receipt'])
        changed['actual_cover_matching_Y2_constructed'] = True
        with patch('check_hodge_conjecture_net.even_scalar_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'even scalar receipt stale'):
                self.validate()

    def test_asymmetric_control_is_not_a_target_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['asymmetric-scalar-cover'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_asymmetric_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'asymmetric-scalar-cover']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_n1_profile_cannot_be_target_isogeny(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'asymmetric-scalar-cover')
        changed = load(a['receipt'])
        changed['actual_target_isogeny'] = 'inferred_from_n1'
        with patch('check_hodge_conjecture_net.asymmetric_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'asymmetric receipt stale'):
                self.validate()

    def test_curve_aut_group_not_a_cycle_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['asymmetric-reflections'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_automorphism_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'asymmetric-reflections']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_incomplete_center_certificate_rejected(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'asymmetric-reflections')
        changed = load(a['receipt'])
        changed['center_certificates'].pop()
        with patch('check_hodge_conjecture_net.automorphism_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'automorphism receipt stale'):
                self.validate()

    def test_finite_field_simple_not_a_cycle_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['asymmetric-frobenius'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_frobenius_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'asymmetric-frobenius']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_F7_simple_cannot_be_promoted_to_geometric_simple(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'asymmetric-frobenius')
        changed = load(a['receipt'])
        changed['geometric_simplicity_proved'] = True
        with patch('check_hodge_conjecture_net.frobenius_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'Frobenius receipt stale'):
                self.validate()

    def test_absolute_simple_auxiliary_not_a_Hodge_counterexample(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='rejected',evidence=['asymmetric-absolute'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_absolute_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'asymmetric-absolute']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_absolute_result_cannot_exclude_entire_scalar_family(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'asymmetric-absolute')
        changed = load(a['receipt'])
        changed['all_scalar_parameters_excluded'] = True
        with patch('check_hodge_conjecture_net.absolute_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'absolute receipt stale'):
                self.validate()

    def test_absolute_rejection_requires_actual_target_port(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'asymmetric-scalar-target-transplant')
        n['depends_on'] = ['asymmetric-prym-frobenius7']
        n['required_verdicts'] = {'asymmetric-prym-frobenius7':'constructed'}
        with self.assertRaisesRegex(ValueError,'absolute node binding'):
            self.validate()

    def test_scalar_family_progress_is_not_a_cycle_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['scalar-family-localization'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_scalar_family_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'scalar-family-localization']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_countable_target_locus_cannot_be_promoted_to_finite(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'scalar-family-localization')
        changed = load(a['receipt']);changed['fixed_target_isogeny_locus_claimed_finite'] = True
        with patch('check_hodge_conjecture_net.scalar_family_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'scalar family receipt stale'):
                self.validate()

    def test_family_negative_anchor_does_not_weaken_cycle_gates(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        n['depends_on'].append('asymmetric-scalar-target-transplant')
        n['required_verdicts']['asymmetric-scalar-target-transplant'] = 'rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_scalar_family_consumes_the_scoped_rejection(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'scalar-family-localization')
        n['required_verdicts']['asymmetric-scalar-target-transplant'] = 'constructed'
        with self.assertRaises(ValueError):
            self.validate()

    def test_scalar_polarized_rejection_not_all_cycle_annihilation(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='rejected',evidence=['scalar-polarized-obstruction'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_scalar_polarized_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'scalar-polarized-obstruction']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_scalar_polarized_result_not_nonlifting_exclusion(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'scalar-polarized-obstruction')
        changed = load(a['receipt']);changed['nonlifting_labels_excluded'] = True
        with patch('check_hodge_conjecture_net.scalar_polarized_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'scalar polarized receipt stale'):
                self.validate()

    def test_polarized_census_cannot_replace_unpolarized_census(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'scalar-polarized-obstruction')
        changed = load(a['receipt']);changed['conditional_unpolarized_isogeny_survivor_labels'] = 512
        with patch('check_hodge_conjecture_net.scalar_polarized_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'scalar polarized receipt stale'):
                self.validate()

    def test_nonlifting_rejection_not_a_Hodge_verdict(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='rejected',evidence=['nonlifting-polarized-obstruction'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_nonlifting_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'nonlifting-polarized-obstruction']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_nonlifting_result_cannot_claim_actual_theta_dimension(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'nonlifting-polarized-obstruction')
        changed = load(a['receipt']);changed['actual_theta_singularity_dimension'] = 3
        with patch('check_hodge_conjecture_net.nonlifting_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'nonlifting receipt stale'):
                self.validate()

    def test_nonlifting_cannot_exclude_general_Prym_membership(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'nonlifting-polarized-obstruction')
        changed = load(a['receipt']);changed['all_smooth_etale_Prym_presentations_excluded'] = True
        with patch('check_hodge_conjecture_net.nonlifting_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'nonlifting receipt stale'):
                self.validate()

    def test_scoped_nonlifting_rejection_inputs_do_not_weaken_cycle_gates(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'all-algebraic-cycles-annihilation')
        n['depends_on'].append('nonlifting-polarized-prym-transplant')
        n['required_verdicts']['nonlifting-polarized-prym-transplant'] = 'rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_tetragonal_necessary_gate_is_not_a_cycle_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['equivariant-tetragonal-gate'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_missing_tetragonal_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'equivariant-tetragonal-gate']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_tetragonal_gate_does_not_supply_theta_lower_bound(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'equivariant-tetragonal-gate')
        changed = load(a['receipt']);changed['theta_lower_bound_four_asserted'] = True
        with patch('check_hodge_conjecture_net.tetragonal_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'tetragonal receipt stale'):
                self.validate()

    def test_tetragonal_necessary_conditions_not_sufficient_for_Y2(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'equivariant-tetragonal-gate')
        changed = load(a['receipt']);changed['diagram_conditions_sufficient_for_target'] = True
        with patch('check_hodge_conjecture_net.tetragonal_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'tetragonal receipt stale'):
                self.validate()

    def test_tetragonal_scoped_rejection_inputs_not_witness_authority(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n['depends_on'].append('hyperelliptic-bottom-prym-transplant')
        n['required_verdicts']['hyperelliptic-bottom-prym-transplant'] = 'rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_missing_eightfold_literature_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'eightfold-literature-audit']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_eightfold_literature_not_a_cycle_witness(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['eightfold-literature-audit'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_eightfold_literature_node_binding(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'eightfold-literature-and-secant-audit')
        n['resolution_kind'] = 'actual_exceptional_cycle'
        with self.assertRaisesRegex(ValueError,'eightfold literature node binding'):
            self.validate()

    def test_eightfold_literature_promotion_stales_receipt(self):
        a = next(a for a in self.c['artifacts'] if a['id'] == 'eightfold-literature-audit')
        changed = load(a['receipt']);changed['secant_semiregularity_proved'] = True
        with patch('check_hodge_conjecture_net.eightfold_literature_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'eightfold literature receipt stale'):
                self.validate()

    def test_missing_secant_local_ext_artifact(self):
        self.c['artifacts'] = [a for a in self.c['artifacts'] if a['id'] != 'secant-local-ext-gate']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_local_ext_is_not_an_actual_cycle(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['secant-local-ext-gate'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_local_ext_node_binding(self):
        n = next(n for n in self.c['conjectures'] if n['id'] == 'secant-local-ext-gate')
        n['resolution_kind']='global_obstruction_dimension'
        with self.assertRaisesRegex(ValueError,'local Ext node binding'):
            self.validate()

    def test_local_ext_global_dimension_promotion_stales_receipt(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='secant-local-ext-gate')
        changed=load(a['receipt']);changed['local_Ext2_length_is_global_Ext2_dimension']=True
        with patch('check_hodge_conjecture_net.local_ext_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'local Ext receipt stale'):
                self.validate()

    def test_missing_source_semiregularity_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='secant-source-semiregularity']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_source_semiregularity_scope_rejection_not_cycle_witness(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['secant-source-semiregularity'])
        with self.assertRaisesRegex(ValueError,'research resolution'):
            self.validate()

    def test_source_semiregularity_node_not_constructed_witness(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='secant-source-weak-semiregularity-transplant')
        n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'source semiregularity node binding'):
            self.validate()

    def test_source_semiregularity_does_not_refute_question(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='secant-source-semiregularity')
        changed=load(a['receipt']);changed['Question11_4_refuted']=True
        with patch('check_hodge_conjecture_net.source_semireg_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'source semiregularity receipt stale'):
                self.validate()

    def test_missing_full37_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='scalar-37-census']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_full37_target_veto_not_construction(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='scalar-37-typed-polarized-target-transplant');n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'full37 target veto node binding'):self.validate()

    def test_full37_finite_multiplicity3_not_automatic_veto(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='scalar-37-census');changed=load(a['receipt'])
        changed['finite_CM_multiplicity3_alone_excludes_target']=True
        with patch('check_hodge_conjecture_net.census37_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'full37 receipt stale'):self.validate()

    def test_full37_survivor_not_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['scalar-37-census'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_missing_third_prime_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='off-reflection-third-prime']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_third_prime_target_veto_not_construction(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='third-prime-and-generic-target-transplant');n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'third-prime generic target veto node binding'):self.validate()

    def test_third_prime_generic_gate_not_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['off-reflection-third-prime'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_third_prime_not_all_transcendental_tuples(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='off-reflection-third-prime');changed=load(a['receipt'])
        changed['all_transcendental_scalar_tuples_excluded']=True
        with patch('check_hodge_conjecture_net.third_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'third-prime receipt stale'):self.validate()

    def test_missing_inert_projector_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='inert-elliptic-projector']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_inert_projector_veto_not_constructed_target(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='inert-degree-parity-target-transplant');n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'inert norm veto node binding'):self.validate()

    def test_inert_projector_not_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['inert-elliptic-projector'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_inert_nonunit_control_cannot_be_promoted(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='inert-elliptic-projector');changed=load(a['receipt'])
        changed['nonunit_a6_control']['integral_at3']=True
        with patch('check_hodge_conjecture_net.inert_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'inert projector receipt stale'):self.validate()

    def test_missing_joint_screen_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='off-reflection-joint-screen']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_joint_screen_target_veto_not_construction(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='off-reflection-two-prime-target-transplant')
        n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'two-prime target veto node binding'):self.validate()

    def test_joint_screen_survivor_not_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['off-reflection-joint-screen'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_joint_screen_uncertified_classes_not_excluded(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='off-reflection-joint-screen')
        changed=load(a['receipt']);changed['CRT_partition']['typed_excluded']+=changed['CRT_partition']['uncertified']
        changed['CRT_partition']['uncertified']=[]
        with patch('check_hodge_conjecture_net.joint_screen_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'two-prime receipt stale'):self.validate()

    def test_missing_off_reflection_a_line_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='off-reflection-a-line']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_a_line_rejected_target_not_constructed(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='off-reflection-a-line-target-transplant')
        n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'off-reflection target exclusion node binding'):self.validate()

    def test_a_line_census_not_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['off-reflection-a-line'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_a_line_degree12_factor_not_fixed_X6(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='off-reflection-a-line')
        changed=load(a['receipt']);changed['finite_field_degree12_factor_identified_with_fixed_X6']=True
        with patch('check_hodge_conjecture_net.a_line_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'a-line receipt stale'):self.validate()

    def test_missing_reflection_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='scalar-reflection-decomposition']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_reflection_rejected_target_cannot_be_constructed(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='reflection-symmetric-scalar-target-transplant')
        n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'reflection target exclusion node binding'):self.validate()

    def test_reflection_source_degree256_not_target_identification(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='scalar-reflection-decomposition')
        changed=load(a['receipt']);changed['source_degree256_isogeny_identified_with_target_isogeny']=True
        with patch('check_hodge_conjecture_net.reflection_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'reflection receipt stale'):self.validate()

    def test_reflection_quotients_not_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['scalar-reflection-decomposition'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_missing_second_prime_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='minimal-axis-second-prime']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_second_prime_cannot_reconstruct_rejected_b6_target(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='minimal-axis-b6-target-transplant')
        n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'b6 target exclusion node binding'):self.validate()

    def test_second_prime_survival_not_a_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['minimal-axis-second-prime'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_second_prime_not_all_b_line_exclusion(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='minimal-axis-second-prime')
        changed=load(a['receipt']);changed['all_b_line_parameters_excluded']=True
        with patch('check_hodge_conjecture_net.second_prime_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'second-prime receipt stale'):self.validate()

    def test_missing_b_line_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='minimal-axis-b-line']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_b_line_preserves_scoped_rejection(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='minimal-axis-b-line-screen')
        n['required_verdicts']['minimal-axis-scalar-target-transplant']='constructed'
        with self.assertRaisesRegex(ValueError,'b-line node binding'):self.validate()

    def test_b_line_is_not_a_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['minimal-axis-b-line'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_b_line_cannot_lift_finite_field_Hom(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='minimal-axis-b-line')
        changed=load(a['receipt']);changed['surviving_reduction_lifts_a_complex_CM_axis']=True
        with patch('check_hodge_conjecture_net.b_line_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'b-line receipt stale'):self.validate()

    def test_missing_minimal_frobenius_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='minimal-axis-frobenius-obstruction']
        with self.assertRaisesRegex(ValueError,'artifact census'):self.validate()

    def test_minimal_frobenius_requires_actual_source_and_target(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='minimal-axis-scalar-target-transplant')
        n['depends_on']=['minimal-axis-scalar-source'];n['required_verdicts']={'minimal-axis-scalar-source':'constructed'}
        with self.assertRaisesRegex(ValueError,'minimal Frobenius node binding'):self.validate()

    def test_minimal_frobenius_not_a_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['minimal-axis-frobenius-obstruction'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):self.validate()

    def test_minimal_frobenius_not_whole_family_exclusion(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='minimal-axis-frobenius-obstruction')
        changed=load(a['receipt']);changed['all_scalar_parameters_excluded']=True
        with patch('check_hodge_conjecture_net.minimal_frob_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'minimal Frobenius receipt stale'):self.validate()

    def test_missing_minimal_source_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='minimal-axis-scalar-source']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_minimal_source_requires_joint_gate_and_cycle_theorem(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='minimal-axis-scalar-source')
        n['depends_on']=['even-axis-joint-degree-gate']
        n['required_verdicts']={'even-axis-joint-degree-gate':'constructed'}
        with self.assertRaisesRegex(ValueError,'minimal source node binding'):
            self.validate()

    def test_minimal_source_is_not_a_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['minimal-axis-scalar-source'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):
            self.validate()

    def test_minimal_source_one_axis_is_not_Y3_match(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='minimal-axis-scalar-source')
        changed=load(a['receipt']);changed['fixed_Y3_Prym_membership_constructed']=True
        with patch('check_hodge_conjecture_net.minimal_source_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'minimal source receipt stale'):
                self.validate()

    def test_missing_joint_degree_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='even-axis-joint-degree-gate']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_joint_degree_gate_requires_both_positive_inputs(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='even-axis-joint-degree-gate')
        n['depends_on']=['even-axis-principal-model']
        n['required_verdicts']={'even-axis-principal-model':'constructed'}
        with self.assertRaisesRegex(ValueError,'joint-degree node binding'):
            self.validate()

    def test_joint_degree_gate_is_not_a_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['even-axis-joint-degree-gate'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):
            self.validate()

    def test_joint_degree_two_branch_not_all_rejected(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='even-axis-joint-degree-gate')
        changed=load(a['receipt']);changed['all_degree_two_joint_maps_excluded']=True
        with patch('check_hodge_conjecture_net.joint_degree_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'joint-degree receipt stale'):
                self.validate()

    def test_missing_coupled_kummer_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='even-axis-coupled-kummer-gate']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_coupled_kummer_gate_requires_fresh_geometry_and_literature(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='even-axis-coupled-kummer-gate')
        n['depends_on']=['even-axis-principal-model']
        n['required_verdicts']={'even-axis-principal-model':'constructed'}
        with self.assertRaisesRegex(ValueError,'coupled Kummer node binding'):
            self.validate()

    def test_coupled_kummer_reconstruction_not_a_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['even-axis-coupled-kummer-gate'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):
            self.validate()

    def test_coupled_kummer_data_not_fixed_Prym_membership(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='even-axis-coupled-kummer-gate')
        changed=load(a['receipt']);changed['fixed_Y3_Prym_membership_constructed']=True
        with patch('check_hodge_conjecture_net.coupled_kummer_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'coupled Kummer receipt stale'):
                self.validate()

    def test_missing_even_axis_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='even-axis-principal-model']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_even_axis_construction_keeps_negative_inputs_scoped(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='even-axis-principal-model')
        n['required_verdicts']['y2-two-branch-cyclic-quartic-transplant']='constructed'
        with self.assertRaisesRegex(ValueError,'required constructed-witness gate'):
            self.validate()

    def test_even_axis_model_not_a_target_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['even-axis-principal-model'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):
            self.validate()

    def test_even_axis_geometry_not_Prym_membership(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='even-axis-principal-model')
        changed=load(a['receipt']);changed['Prym_membership_constructed']=True
        with patch('check_hodge_conjecture_net.even_axis_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'even-axis receipt stale'):
                self.validate()

    def test_missing_two_branch_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='two-branch-odd-axis-obstruction']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_two_branch_negative_input_binding(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='y2-two-branch-cyclic-quartic-transplant')
        n['required_verdicts']['y2-etale-cyclic-quartic-polarized-transplant']='constructed'
        with self.assertRaisesRegex(ValueError,'two-branch node binding'):
            self.validate()

    def test_two_branch_rejection_not_cycle_witness(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n['depends_on'].append('y2-two-branch-cyclic-quartic-transplant')
        n['required_verdicts']['y2-two-branch-cyclic-quartic-transplant']='rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_two_branch_obstruction_not_all_ramified_Pryms(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='two-branch-odd-axis-obstruction')
        changed=load(a['receipt']);changed['all_ramified_Prym_presentations_excluded']=True
        with patch('check_hodge_conjecture_net.two_branch_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'two-branch receipt stale'):
                self.validate()

    def test_missing_odd_axis_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='cyclic-prym-odd-axis-obstruction']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_odd_axis_negative_input_is_not_constructed(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='y2-etale-cyclic-quartic-polarized-transplant')
        n['required_verdicts']['ramified-trigonal-principal-target-transplant']='constructed'
        with self.assertRaisesRegex(ValueError,'odd-axis node binding'):
            self.validate()

    def test_odd_axis_rejection_is_not_cycle_witness(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n['depends_on'].append('y2-etale-cyclic-quartic-polarized-transplant')
        n['required_verdicts']['y2-etale-cyclic-quartic-polarized-transplant']='rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_odd_axis_obstruction_does_not_exclude_ramified_presentations(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='cyclic-prym-odd-axis-obstruction')
        changed=load(a['receipt']);changed['all_ramified_Prym_presentations_excluded']=True
        with patch('check_hodge_conjecture_net.odd_axis_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'odd-axis receipt stale'):
                self.validate()

    def test_missing_principal_match_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='trigonal-principal-match-obstruction']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_principal_match_rejection_input_binding(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='ramified-trigonal-principal-target-transplant')
        n['required_verdicts']['cyclic-quartic-prym-transplant']='constructed'
        with self.assertRaisesRegex(ValueError,'principal match node binding'):
            self.validate()

    def test_principal_rejection_not_a_cycle_witness(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n['depends_on'].append('ramified-trigonal-principal-target-transplant')
        n['required_verdicts']['ramified-trigonal-principal-target-transplant']='rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_principal_obstruction_not_unpolarized_isogeny_exclusion(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='trigonal-principal-match-obstruction')
        changed=load(a['receipt']);changed['all_unpolarized_K_isogenies_to_Y2_excluded']=True
        with patch('check_hodge_conjecture_net.principal_match_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'principal match receipt stale'):
                self.validate()

    def test_missing_ramified_family_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='ramified-trigonal-family']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_ramified_family_gate_dependency_frozen(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='ramified-trigonal-auxiliary-family')
        n['depends_on'].remove('equivariant-tetragonal-gate')
        del n['required_verdicts']['equivariant-tetragonal-gate']
        with self.assertRaisesRegex(ValueError,'ramified family node binding'):
            self.validate()

    def test_auxiliary_algebraicity_cannot_resolve_target_witness(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n.update(status='resolved',verdict='constructed',evidence=['ramified-trigonal-family'])
        with self.assertRaisesRegex(ValueError,'unreviewed research resolution'):
            self.validate()

    def test_auxiliary_isomorphism_not_target_isogeny(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='ramified-trigonal-family')
        changed=load(a['receipt']);changed['target_K_isogeny_constructed']=True
        with patch('check_hodge_conjecture_net.ramified_family_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'ramified family receipt stale'):
                self.validate()

    def test_missing_persistence_artifact(self):
        self.c['artifacts']=[a for a in self.c['artifacts'] if a['id']!='secant-criterion-persistence']
        with self.assertRaisesRegex(ValueError,'artifact census'):
            self.validate()

    def test_persistence_negative_input_not_witness_authority(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='algebraic-witness-search')
        n['depends_on'].append('secant-source-weak-semiregularity-transplant')
        n['required_verdicts']['secant-source-weak-semiregularity-transplant']='rejected'
        with self.assertRaisesRegex(ValueError,'constructed-witness gate'):
            self.validate()

    def test_persistence_rejection_is_not_constructed_cycle(self):
        n=next(n for n in self.c['conjectures'] if n['id']=='eightfold-secant-weak-criterion-transplant')
        n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'persistence node binding'):
            self.validate()

    def test_persistence_does_not_admit_arbitrary_quotients(self):
        a=next(a for a in self.c['artifacts'] if a['id']=='secant-criterion-persistence')
        changed=load(a['receipt']);changed['arbitrary_quotients_admitted']=True
        with patch('check_hodge_conjecture_net.persistence_report',return_value=changed):
            with self.assertRaisesRegex(ValueError,'persistence receipt stale'):
                self.validate()

    def test_altered_control_receipt_rejected(self):
        self.controls['results']['quadric_middle_cycle_span_rank'] = 1
        with self.assertRaisesRegex(ValueError, 'receipt stale'):
            self.validate()

    def test_current_source_pins_and_stale_pin_hostile(self):
        pins = load(self.c['source_pins'])
        validate_pins(self.c, self.a, pins)
        key = next(iter(pins['source_sha256']))
        pins['source_sha256'][key] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'source drift'):
            validate_pins(self.c, self.a, pins)

    def test_existing_pin_snapshot_cannot_be_overwritten(self):
        before = digest(self.c['source_pins'])
        run = subprocess.run([sys.executable, str(ROOT / 'research/voevodsky/checkers/check_hodge_conjecture_net.py'), '--pin'],
                             capture_output=True, text=True, timeout=30)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('refusing to overwrite immutable pins', run.stderr)
        self.assertEqual(digest(self.c['source_pins']), before)


class HodgeControlTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FIXTURES.read_text(encoding='utf-8'))

    def test_primitive_nondivisor_class_can_still_be_algebraic(self):
        result = evaluate(self.data)
        self.assertEqual(result['quadric_middle_cycle_span_rank'], 2)
        self.assertEqual(result['quadric_divisor_square_span_rank'], 1)
        self.assertEqual(result['quadric_primitive_algebraic_class'], [1, -1])
        self.assertEqual(result['naive_obstruction_disposition'], 'rejected_as_Hodge_obstruction')

    def test_integral_nonmembership_can_have_rational_witness(self):
        result = evaluate(self.data)
        self.assertEqual(result['rational_witness_for_integral_nonmember'], '1/2')
        self.assertEqual(result['torsion_cokernel_dimension_over_Q'], 0)

    def test_fake_quadric_plane_is_rejected(self):
        self.data['quadric']['plane_A_free_coordinates'] = [0, 1, 5]
        with self.assertRaisesRegex(ValueError, 'plane not on quadric'):
            evaluate(self.data)

    def test_wrong_middle_intersection_model_is_rejected(self):
        self.data['quadric']['intersection_matrix'] = [[0, 1], [1, 0]]
        with self.assertRaisesRegex(ValueError, 'intersection'):
            evaluate(self.data)


class HodgeScopeTests(unittest.TestCase):
    def setUp(self):
        self.scope = json.loads(SCOPE_CONTRACT.read_text(encoding='utf-8'))

    def test_scope_is_typed_without_constructing_packet_bridge(self):
        validate_scope(self.scope)
        self.assertFalse(self.scope['boundary']['general_packet_cohomology_bridge_constructed'])

    def test_unique_factor_on_full_hodge_space_cannot_be_assumed(self):
        self.scope['descent_lemma']['full_H_extension_unique_without_surjectivity'] = True
        with self.assertRaisesRegex(ValueError, 'conflation'):
            validate_scope(self.scope)

    def test_packet_cycle_generation_cannot_be_promoted(self):
        self.scope['maps'][2]['status'] = 'all_cycles_generated'
        with self.assertRaisesRegex(ValueError, 'generation bridge'):
            validate_scope(self.scope)

    def test_witness_sensitive_functional_has_no_class_factor(self):
        self.assertIsNone(factor(((1, 0, 1), (0, 1, 1), (0, 0, 0)), ((0, 0, 1),)))


class HodgeDictionaryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(DICTIONARY_CONTRACT.read_text(encoding='utf-8'))

    def test_real_torus_cannot_be_promoted_to_hodge_counterexample(self):
        self.data['negative_example']['Hodge_type_p_p'] = True
        with self.assertRaisesRegex(ValueError, 'non-Hodge control promoted'):
            validate_dictionary(self.data)

    def test_cycle_supplied_dictionary_cannot_claim_full_source_generation(self):
        self.data['boundary']['general_packet_source_generation_constructed'] = True
        with self.assertRaisesRegex(ValueError, 'scope promoted'):
            validate_dictionary(self.data)

    def test_rational_negative_multiplicities_preserve_chain_and_prism_identities(self):
        sphere = boundary({(0, 1, 2, 3): Fraction(-2, 3)})
        circle = boundary({(0, 1, 2): Fraction(5, 7)})
        chain = cross(sphere, circle, 3)
        self.assertTrue(chain)
        self.assertEqual(boundary(chain), {})
        self.assertEqual(boundary(prism(chain)), add(lift(chain, 1), lift(chain, 0), -1))

    def test_prism_identity_retains_boundary_term_on_open_simplex(self):
        chain = {(0, 1, 2): 1}
        self.assertNotEqual(boundary(prism(chain)), add(lift(chain, 1), lift(chain, 0), -1))
        self.assertEqual(add(boundary(prism(chain)), prism(boundary(chain))),
                         add(lift(chain, 1), lift(chain, 0), -1))


class HodgeLiteratureAuditTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(AUDIT_CONTRACT.read_text(encoding='utf-8'))

    def test_bounded_search_cannot_certify_exhaustive_status(self):
        self.data['boundary']['global_exhaustive_literature_status_certified'] = True
        with self.assertRaisesRegex(ValueError, 'audit promoted'):
            validate_audit(self.data)

    def test_nonexistent_source_quote_is_rejected(self):
        self.data['citations'][0]['quote'] = 'This source proves the general Hodge conjecture.'
        with self.assertRaisesRegex(ValueError, 'citation does not occur'):
            validate_sources(self.data)

    def test_nonsplit_discriminant_cannot_silently_become_split(self):
        self.data['shortlist'][0]['discriminant'] = -1
        with self.assertRaisesRegex(ValueError, 'discriminant scope'):
            validate_audit(self.data)

    def test_weil_character_square_has_nonunit_scale(self):
        real, imaginary = weil_forms(6)
        twice = pullback_one_plus_i(pullback_one_plus_i(real))
        self.assertEqual(twice, {s: -64*v for s, v in real.items()})
        self.assertEqual(len(imaginary), 32)


class HodgeExplicitCandidateTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(CANDIDATE_CONTRACT.read_text(encoding='utf-8'))

    def test_rational_special_point_cannot_replace_exact_period_formula(self):
        self.data['geometry']['Z_formula'] = 'Z=0'
        with self.assertRaisesRegex(ValueError, 'marked period changed'):
            validate_candidate(self.data)

    def test_class_cannot_be_selected_by_assuming_nonalgebraicity(self):
        self.data['class']['selection_depends_on_nonalgebraicity'] = True
        with self.assertRaisesRegex(ValueError, 'circularly'):
            validate_candidate(self.data)

    def test_divisor_exclusion_cannot_become_all_cycle_exclusion(self):
        self.data['picard_certificate']['all_algebraic_cycles_excluded'] = True
        with self.assertRaisesRegex(ValueError, 'divisor-only conclusion promoted'):
            validate_candidate(self.data)

    def test_rank_certificate_retains_65_independent_rows(self):
        result = exact_core()
        self.assertEqual(len(set(result['degree_two_independent_row_indices'])), 65)
        self.assertEqual(result['alpha_x_torus_period'], 1)
        self.assertEqual(sparse_rank([[Fraction(1, 2), 1, 0], [1, 2, 0], [0, 0, -3]]), 2)

    def test_degree_six_J_invariance_is_not_hodge_type_33(self):
        real, imaginary = weil_forms(6)
        def conjugate_factors(form):
            return {indices: value*(-1)**sum(i in indices for i in (7, 9)) for indices, value in form.items()}
        bad_real, bad_imaginary = conjugate_factors(real), conjugate_factors(imaginary)
        self.assertEqual(full_pullback(base_J(), bad_real), bad_real)
        self.assertEqual(lie_action(base_J(), bad_real), {s: -4*v for s, v in bad_imaginary.items()})
        self.assertTrue(lie_action(base_J(), bad_real))

    def test_hodge_membership_cannot_be_promoted_to_hodge_refutation(self):
        self.data['boundary']['Hodge_refuted'] = True
        with self.assertRaisesRegex(ValueError, 'Hodge verdict'):
            validate_candidate(self.data)


class HodgeWeilProjectorTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(PROJECTOR_CONTRACT.read_text(encoding='utf-8'))

    def test_coarse_generator_cannot_replace_separating_endomorphism(self):
        self.data['definition']['endomorphism'] = 'f=1+i'
        with self.assertRaisesRegex(ValueError, 'projector formula'):
            validate_projector(self.data)

    def test_cycle_preservation_cannot_become_all_cycle_annihilation(self):
        self.data['algebraic_cycle_policy']['annihilates_all_algebraic_cycles_on_selected_X'] = True
        with self.assertRaisesRegex(ValueError, 'preservation promoted'):
            validate_projector(self.data)

    def test_cohomology_idempotence_cannot_become_chow_idempotence(self):
        self.data['algebraic_cycle_policy']['Chow_idempotence_claimed'] = True
        with self.assertRaisesRegex(ValueError, 'preservation promoted'):
            validate_projector(self.data)

    def test_displayed_denominator_cannot_be_changed(self):
        self.data['definition']['common_denominator'] = 1
        with self.assertRaisesRegex(ValueError, 'projector formula'):
            validate_projector(self.data)

    def test_zero_projected_cycle_cannot_generate_alpha(self):
        with self.assertRaisesRegex(ValueError, 'zero Weil witness'):
            witness_coefficients(0,0)

    def test_signed_rational_witness_conversion(self):
        a,b = Fraction(-2,7),Fraction(5,11)
        c,d = witness_coefficients(a,b)
        self.assertEqual(c*a+d*(-117*a+44*b),1)
        self.assertEqual(c*b+d*(-44*a-117*b),0)

    def test_projector_remainders_and_idempotence_are_exact(self):
        p,q,s = projection_polynomial()
        self.assertEqual(remainder(p,MODULI[0]),[1])
        self.assertTrue(all(not remainder(p,m) for m in MODULI[1:]))
        minimal = [1]
        for m in MODULI:
            minimal = pmul(minimal,m)
        self.assertEqual(remainder(padd(pmul(p,p),p,-1),minimal),[])
        corrupted = padd(p,[1])
        self.assertNotEqual(remainder(padd(pmul(corrupted,corrupted),corrupted,-1),minimal),[])


class HodgeTautologicalSearchTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SEARCH_CONTRACT.read_text(encoding='utf-8'))

    def test_arbitrary_higher_Chern_classes_cannot_be_added_to_excluded_library(self):
        self.data['library']['arbitrary_higher_Chern_classes_included'] = True
        with self.assertRaisesRegex(ValueError,'bounded library promoted'):
            validate_search(self.data)

    def test_arbitrary_subvarieties_cannot_be_added_to_excluded_library(self):
        self.data['library']['arbitrary_algebraic_subvarieties_included'] = True
        with self.assertRaisesRegex(ValueError,'bounded library promoted'):
            validate_search(self.data)

    def test_bounded_search_cannot_claim_nonalgebraicity(self):
        self.data['boundary']['alpha_nonalgebraic_proved'] = True
        with self.assertRaisesRegex(ValueError,'bounded failure promoted'):
            validate_search(self.data)

    def test_changed_centralizer_rank_rejected(self):
        self.data['endomorphism_certificate']['stacked_commutator_rank'] = 141
        with self.assertRaisesRegex(ValueError,'centralizer certificate binding'):
            validate_search(self.data)

    def test_unlicensed_Fourier_normalization_rejected(self):
        self.data['fourier_control']['on_alpha'] = 1
        with self.assertRaisesRegex(ValueError,'Fourier normalization'):
            validate_search(self.data)

    def test_Weil_plane_cannot_be_declared_symmetry_invariant(self):
        self.data['symmetry']['on_weil_space'] = 'tau*=Id'
        with self.assertRaisesRegex(ValueError,'symmetry binding'):
            validate_search(self.data)

    def test_Fourier_distinguishes_divisor_cube_and_Weil_signs(self):
        E = {(2*j,2*j+1):Fraction(d) for j,d in enumerate(DS)}
        cube = wedge(wedge(E,E),E)
        real,_ = weil_forms(6)
        self.assertEqual(fourier(cube),scale(cube,-3))
        self.assertEqual(fourier(real),scale(real,3))

    def test_Fourier_square_retains_odd_degree_inversion(self):
        dx = {(0,):Fraction(1)}
        self.assertEqual(fourier(fourier(dx)),scale(dx,-9))

    def test_special_fiber_cannot_replace_actual_point_End0(self):
        result = search_core()
        self.assertEqual(result['special_fiber_End0_dimension'],72)
        self.assertEqual(result['End0_dimension_from_written_genericity_proof'],2)

    def test_synthetic_kappa_identity_does_not_construct_an_algebraic_bundle(self):
        # Pure cohomology control: this formal record is NOT an asserted bundle.
        E = {(2*j,2*j+1):Fraction(d) for j,d in enumerate(DS)}
        c1, ch2 = scale(E,3), {(0,2,4,6):Fraction(2,7)}
        real,_ = weil_forms(6)
        kappa3 = combine(combine(real,scale(wedge(c1,ch2),Fraction(-1,2))),
                         scale(wedge(wedge(c1,c1),c1),Fraction(1,12)))
        p,_,_ = projection_polynomial()
        self.assertEqual(apply_polynomial(p,kappa3),real)
        self.assertFalse(self.data['boundary']['algebraic_representative_of_alpha_constructed'])


class HodgeMiddleKernelTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(KERNEL_CONTRACT.read_text(encoding='utf-8'))

    def test_composite_modulus_cannot_certify_field_rank(self):
        with self.assertRaisesRegex(ValueError,'modulus must be prime'):
            modular_rank([{0:1}],15)

    def test_bad_denominator_cannot_be_reduced(self):
        with self.assertRaisesRegex(ValueError,'noninvertible rational denominator'):
            residue(Fraction(1,7),7)

    def test_modular_rank_is_only_a_rational_rank_lower_bound(self):
        # diag(1,7) has rational rank two but rank one modulo seven.
        self.assertEqual(modular_rank([{0:1},{1:7}],7)[0],1)

    def test_minor_determinant_tracks_nonmonotone_pivots_and_sign(self):
        for a,b,c,d in ((0,2,3,4),(2,-3,4,5),(1,1,1,2),(1,101,0,1)):
            rank,_,_,det = modular_rank([{0:a,1:b},{0:c,1:d}],101)
            self.assertEqual(rank,2)
            self.assertEqual(det,(a*d-b*c)%101)

    def test_four_term_group_algebra_projector_is_idempotent(self):
        e = [Fraction(1,4),Fraction(-1,4),Fraction(1,4),Fraction(-1,4)]
        self.assertEqual(cyclic_product(e,e),e)
        self.assertEqual(cyclic_product([0,1,0,0],e),[-v for v in e])

    def test_half_difference_has_nonzero_formal_Chow_remainder(self):
        h = [Fraction(1,2),Fraction(-1,2),0,0]
        self.assertEqual([a-b for a,b in zip(cyclic_product(h,h),h)],
                         [Fraction(-1,4),0,Fraction(1,4),0])

    def test_anti_i_cannot_be_rank_two_on_full_cohomology(self):
        self.data['projectors']['anti_i_full_H6_rank'] = 2
        with self.assertRaisesRegex(ValueError,'projector scope'):
            validate_kernel(self.data)

    def test_Hodge_dimension_cannot_be_changed_without_certificate(self):
        self.data['certificate']['rational_kernel_dimension'] = 2
        with self.assertRaisesRegex(ValueError,'kernel certificate binding'):
            validate_kernel(self.data)

    def test_Chow_idempotent_alone_cannot_construct_nonzero_homological_cycle(self):
        self.data['boundary']['nonzero_homological_anti_i_cycle_constructed'] = True
        with self.assertRaisesRegex(ValueError,'promoted to algebraicity verdict'):
            validate_kernel(self.data)

    def test_class_level_agreement_cannot_become_Chow_equality(self):
        self.data['projectors']['P_CH_equals_four_term_projector_on_Chow_claimed'] = True
        with self.assertRaisesRegex(ValueError,'Chow idempotence error'):
            validate_kernel(self.data)

    def test_full_certificate_keeps_three_rational_generators(self):
        result = kernel_core()
        self.assertEqual(result['rank_mod_prime'],921)
        self.assertEqual(result['Hodge_basis'],['E^3','R','I'])
        self.assertNotEqual(result['selected_minor_determinant_mod_prime'],0)


class HodgeSecantTransplantTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TRANSPLANT_CONTRACT.read_text(encoding='utf-8'))

    def test_selected_discriminant_cannot_be_changed_to_split(self):
        self.data['hypotheses']['selected_determinant'] = -1
        with self.assertRaisesRegex(ValueError,'hypothesis binding'):
            validate_transplant(self.data)

    def test_rank_one_NS_hypothesis_is_essential(self):
        self.data['hypotheses']['NS_Q_rank'] = 2
        with self.assertRaisesRegex(ValueError,'hypothesis binding'):
            validate_transplant(self.data)

    def test_extra_endomorphisms_cannot_be_assumed(self):
        self.data['hypotheses']['End0'] = 'M_6(Q(i))'
        with self.assertRaisesRegex(ValueError,'hypothesis binding'):
            validate_transplant(self.data)

    def test_one_theorem_failure_cannot_exclude_all_sheaves(self):
        self.data['boundary']['all_sheaf_routes_excluded'] = True
        with self.assertRaisesRegex(ValueError,'failure promoted'):
            validate_transplant(self.data)

    def test_source_quote_cannot_be_changed_to_nonsplit_theorem(self):
        self.data['citations'][1]['quote'] = 'every nonsplit sixfold is covered'
        with self.assertRaisesRegex(ValueError,'source quote absent'):
            validate_transplant_sources(self.data)

    def test_Gaussian_norm_valuation_handles_denominators(self):
        self.assertEqual(valuation3(gaussian_norm((Fraction(1,3),Fraction(1,3)))),-2)
        self.assertEqual(valuation3(3),1)

    def test_Gaussian_determinant_retains_nonreal_values(self):
        self.assertEqual(gdet([[(0,1),(1,0)],[(2,0),(1,1)]]),(Fraction(-3),Fraction(1)))

    def test_Igusa_normalization_from_Pfaffian(self):
        for d in range(1,9):
            self.assertEqual(igusa_rank_two(d),16*d**3)
        self.assertEqual(igusa_rank_two(4),1024)

    def test_zero_has_no_finite_valuation(self):
        with self.assertRaisesRegex(ValueError,'valuation of zero'):
            valuation3(0)


class HodgeEightfoldStabilizationTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(STABILIZATION_CONTRACT.read_text(encoding='utf-8'))

    def test_auxiliary_target_cannot_replace_fixed_sixfold_codimension(self):
        self.data['fixed_target']['X_codimension'] = 4
        with self.assertRaisesRegex(ValueError,'replaced fixed candidate'):
            validate_stabilization(self.data)

    def test_auxiliary_dimension_cannot_be_six_for_theorem_application(self):
        self.data['auxiliary']['dimension'] = 6
        with self.assertRaisesRegex(ValueError,'auxiliary geometry'):
            validate_stabilization(self.data)

    def test_sixfold_theorem_is_not_applied_to_eightfold(self):
        self.data['source_boundary']['sixfold_theorem_applied_to_A'] = True
        with self.assertRaisesRegex(ValueError,'dimension-shift theorem misuse'):
            validate_stabilization(self.data)

    def test_complex_orientation_cannot_be_positive_native_orientation(self):
        self.data['auxiliary']['B_integration_orientation'] = 1
        with self.assertRaisesRegex(ValueError,'orientation'):
            validate_stabilization(self.data)

    def test_wrong_reverse_normalization_rejected(self):
        self.data['transfer']['reverse_coefficient'] = '1/2'
        with self.assertRaisesRegex(ValueError,'Chow transfer scope'):
            validate_stabilization(self.data)

    def test_full_Chow_image_projector_cannot_be_rank_two(self):
        self.data['transfer']['full_H8_image_projector_rank'] = 2
        with self.assertRaisesRegex(ValueError,'Chow transfer scope'):
            validate_stabilization(self.data)

    def test_retraction_is_not_identity_on_all_target_Chow(self):
        self.data['transfer']['Chow_S_D_identity_on_all_CH4_A_claimed'] = True
        with self.assertRaisesRegex(ValueError,'Chow transfer scope'):
            validate_stabilization(self.data)

    def test_transfer_alone_does_not_construct_an_algebraic_Weil_class(self):
        self.data['boundary']['nonzero_algebraic_W8_class_constructed'] = True
        with self.assertRaisesRegex(ValueError,'promoted to algebraicity'):
            validate_stabilization(self.data)

    def test_diagonal_eightfold_i_is_not_anti_on_Weil_plane(self):
        self.data['Weil_classes']['diagonal_i_action_on_W8'] = -1
        with self.assertRaisesRegex(ValueError,'changed-dimensional symmetry scope'):
            validate_stabilization(self.data)

    def test_reverse_transfer_needs_correct_divisor_and_sign(self):
        r8,_ = weil_forms(8)
        r6,_ = weil_forms(6)
        self.assertEqual(recover_stabilization(r8),r6)
        self.assertEqual(integrate_B(r8),{})
        self.assertEqual(recover_stabilization(r8,E_B),{})

    def test_known_divisor_cube_retraction_does_not_supply_Weil_witness(self):
        E = {(2*j,2*j+1):Fraction(d) for j,d in enumerate(DS)}
        cube = wedge(wedge(E,E),E)
        image = stabilize(cube)
        r8,i8 = weil_forms(8)
        self.assertTrue(image)
        self.assertEqual(recover_stabilization(image),cube)
        self.assertFalse(set(image)&(set(r8)|set(i8)))

    def test_hyperbolic_basis_and_intersection_degrees_are_exact(self):
        result = stabilization_core()
        self.assertEqual(result['A_K_Witt_index_from_explicit_basis'],4)
        self.assertEqual(result['hyperbolic_basis_determinant'],['-1/3','0'])
        self.assertEqual(result['B_divisor_intersection_degrees'],[-2,0,-2])

    def test_missing_divisor_degree_shift_is_rejected(self):
        self.data['transfer']['codimension_shifts']['D'] = -2
        with self.assertRaisesRegex(ValueError,'Chow transfer scope'):
            validate_stabilization(self.data)


class HodgeEightfoldFilterTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(EIGHTFOLD_FILTER_CONTRACT.read_text(encoding='utf-8'))

    def test_minimal_factor_cannot_be_changed(self):
        self.data['definition']['minimal_factors_ascending'][0][1] = 1170
        with self.assertRaisesRegex(ValueError,'spectral binding'):
            validate_filter(self.data)

    def test_sixfold_dimension_cannot_replace_auxiliary_eightfold(self):
        self.data['definition']['complex_dimension'] = 6
        with self.assertRaisesRegex(ValueError,'spectral binding'):
            validate_filter(self.data)

    def test_cohomology_idempotence_cannot_become_Chow_idempotence(self):
        self.data['cycle_policy']['Chow_idempotence_claimed'] = True
        with self.assertRaisesRegex(ValueError,'projector promoted'):
            validate_filter(self.data)

    def test_15_zero_controls_cannot_become_all_cycle_annihilation(self):
        self.data['cycle_policy']['annihilates_all_algebraic_cycles_proved'] = True
        with self.assertRaisesRegex(ValueError,'projector promoted'):
            validate_filter(self.data)

    def test_reverse_filter_order_cannot_be_changed(self):
        self.data['transfer']['D_P8_equals_P6_D_on_all_H8'] = True
        with self.assertRaisesRegex(ValueError,'transfer scope'):
            validate_filter(self.data)

    def test_projectors_cannot_be_assumed_to_commute(self):
        self.data['transfer']['P8_commutes_with_SD_on_all_H8'] = True
        with self.assertRaisesRegex(ValueError,'transfer scope'):
            validate_filter(self.data)

    def test_sixfold_form_cannot_be_read_as_degree_eight_input(self):
        r6,_ = weil_forms(6)
        with self.assertRaisesRegex(ValueError,'wrong degree'):
            weil_filter(r6,8)

    def test_displayed_CRT_numerator_is_bound_to_exact_inverse(self):
        self.data['definition']['factored_inverse_numerators'][0] += 1
        with self.assertRaisesRegex(ValueError,'displayed eightfold CRT coefficients'):
            validate_filter(self.data)

    def test_coordinate_projector_has_correct_real_and_imaginary_normalization(self):
        r8,i8 = weil_forms(8)
        self.assertEqual(weil_filter({tuple(range(0,16,2)):Fraction(1)}),scale(r8,Fraction(1,128)))
        self.assertEqual(weil_filter({(1,2,4,6,8,10,12,14):Fraction(1)}),scale(i8,Fraction(1,128)))

    def test_opposite_Hodge_sector_refutes_filter_commutation_not_algebraicity(self):
        r6,i6 = weil_forms(6)
        opposite = combine(wedge(r6,R_B),wedge(i6,I_B))
        self.assertEqual(filtered_reverse(opposite),{})
        self.assertEqual(weil_filter(recover_stabilization(opposite),6),r6)
        self.assertFalse(self.data['cycle_policy']['nonzero_algebraic_W8_class_constructed'])

    def test_full_censuses_and_coarse_ranks_are_retained(self):
        result = eightfold_filter_core()
        self.assertEqual(result['full_coordinate_basis_count'],12870)
        self.assertEqual(result['source_intertwiner_basis_count'],924)
        self.assertEqual(result['rational_Weil_projector_rank'],2)
        self.assertEqual(result['coarse_1_plus_i_projector_rank'],4902)
        self.assertEqual(result['diagonal_i_invariant_projector_rank'],6470)

    def test_known_divisor_cube_is_not_a_filtered_Weil_witness(self):
        E = {(2*j,2*j+1):Fraction(d) for j,d in enumerate(DS)}
        cube = wedge(wedge(E,E),E)
        known_cycle = stabilize(cube)
        self.assertEqual(recover_stabilization(known_cycle),cube)
        self.assertEqual(filtered_reverse(known_cycle),{})


class HodgeEightfoldFullKernelTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(EIGHTFOLD_KERNEL_CONTRACT.read_text(encoding='utf-8'))

    def test_Hodge_dimension_does_not_decide_algebraic_dimension(self):
        self.data['algebraic_dimension_decided'] = True
        with self.assertRaisesRegex(ValueError,'not decided'):
            validate_eightfold_kernel(self.data)

    def test_full_Chow_image_cannot_be_called_rank_eight(self):
        self.data['dimensions']['full_H8_Chow_idempotent_image_rank'] = 8
        with self.assertRaisesRegex(ValueError,'rank scope'):
            validate_eightfold_kernel(self.data)

    def test_rank_eight_cohomology_formula_cannot_be_promoted_on_Chow(self):
        self.data['cycle_policy']['rank_eight_formula_Chow_idempotence_claimed'] = True
        with self.assertRaisesRegex(ValueError,'cycle promotion'):
            validate_eightfold_kernel(self.data)

    def test_nonzero_Chow_is_not_nonzero_exceptional_cohomology(self):
        self.data['cycle_policy']['nonzero_Chow_image_suffices'] = True
        with self.assertRaisesRegex(ValueError,'cycle promotion'):
            validate_eightfold_kernel(self.data)

    def test_formal_Hodge_tensor_blind_to_P8_is_not_an_algebraic_witness(self):
        r6,_ = weil_forms(6)
        v = insertion(r6,0)
        self.assertEqual(weil_filter(v,8),{})
        self.assertEqual(exceptional_projector(v),v)
        self.assertEqual(channels(v)[0],r6)
        self.assertFalse(self.data['cycle_policy']['nonzero_algebraic_exceptional_class_constructed'])

    def test_four_channels_have_correct_insertion_duality(self):
        for v in weil_forms(6):
            for i in range(4):
                for j in range(4):
                    self.assertEqual(contraction(insertion(v,j),i),v if i == j else {})

    def test_actual_divisor_cycle_is_not_an_exceptional_witness(self):
        E = {(2*j,2*j+1):Fraction(d) for j,d in enumerate(DS)}
        cube = wedge(wedge(E,E),E)
        for j in range(4):
            self.assertFalse(any(channels(insertion(cube,j))))

    def test_four_channel_reader_rejects_degree_six_input(self):
        r6,_ = weil_forms(6)
        with self.assertRaisesRegex(ValueError,'wrong degree'):
            channels(r6)

    def test_full_Hodge_table_is_bound(self):
        self.data['Hodge_table_by_codimension'][4] = 2
        with self.assertRaisesRegex(ValueError,'full Hodge table'):
            validate_eightfold_kernel(self.data)

    def test_Lie_and_full_projector_censuses(self):
        result = eightfold_hodge_core()
        self.assertEqual(result['Lie_rank_over_Q'],35)
        self.assertEqual(result['rational_Hdg4_dimension'],14)
        self.assertEqual(result['divisor_generated_Hdg4_dimension'],6)
        self.assertEqual(result['exceptional_Hdg4_dimension'],8)
        self.assertEqual(result['full_coordinate_basis_count'],12870)
        self.assertEqual(result['possible_algebraic_Hdg4_dimensions'],[6,14])

    def test_two_projectors_agree_only_on_the_Hodge_space(self):
        # A repeated native pair forces zero P6, but the anti-i image can be nonzero.
        v = insertion({(0,1,2,4,6,8):Fraction(1)},0)
        self.assertEqual(exceptional_projector(v),{})
        qv = chow_exceptional_action(v)
        self.assertTrue(qv)
        self.assertEqual(chow_exceptional_action(qv),qv)


class HodgeChernTransferTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(CHERN_TRANSFER_CONTRACT.read_text(encoding='utf-8'))

    def test_source_bundle_rank_two_is_not_a_third_Chern_route(self):
        self.data['rank_policy']['X_locally_free_kappa3_minimum_possible_rank'] = 2
        with self.assertRaisesRegex(ValueError,'rank policy'):
            validate_transfer(self.data)

    def test_target_bundle_rank_three_is_not_a_normalized_fourth_route(self):
        self.data['rank_policy']['A_locally_free_exceptional_kappa4_minimum_possible_rank'] = 3
        with self.assertRaisesRegex(ValueError,'rank policy'):
            validate_transfer(self.data)

    def test_locally_free_rank_bounds_cannot_be_imposed_on_reflexive_sheaves(self):
        self.data['rank_policy']['bounds_apply_to_arbitrary_reflexive_sheaves'] = True
        with self.assertRaisesRegex(ValueError,'rank policy'):
            validate_transfer(self.data)

    def test_normalization_cannot_be_declared_additive(self):
        self.data['rank_policy']['normalization_is_additive'] = True
        with self.assertRaisesRegex(ValueError,'rank policy'):
            validate_transfer(self.data)

    def test_tensor_twist_alone_is_not_the_transfer(self):
        self.data['transfer']['tensor_twist_alone_suffices'] = True
        with self.assertRaisesRegex(ValueError,'transfer scope'):
            validate_transfer(self.data)

    def test_transfer_denominator_is_n_plus_one_not_n(self):
        self.data['transfer']['exceptional_factor'] = '1/n'
        with self.assertRaisesRegex(ValueError,'transfer scope'):
            validate_transfer(self.data)

    def test_formal_source_is_not_a_supplied_bundle(self):
        self.data['transfer']['input_bundle_supplied'] = True
        with self.assertRaisesRegex(ValueError,'transfer scope'):
            validate_transfer(self.data)

    def test_rank_lower_bound_is_not_a_rank_four_existence_theorem(self):
        self.data['transfer']['rank_four_witness_guaranteed'] = True
        with self.assertRaisesRegex(ValueError,'transfer scope'):
            validate_transfer(self.data)

    def test_equivalence_does_not_choose_positive_branch(self):
        self.data['equivalence_branch_decided'] = True
        with self.assertRaisesRegex(ValueError,'branch not decided'):
            validate_transfer(self.data)

    def test_low_rank_polynomial_identities_and_singular_control_are_distinct(self):
        k3 = normalized_chern(2,3)
        self.assertEqual(k3.get((0,0,1,0)),Fraction(1,2))
        self.assertEqual(locally_free_restriction(k3,2),{})
        k2 = locally_free_restriction(normalized_chern(3,2),3)
        self.assertEqual(locally_free_restriction(normalized_chern(3,4),3),
                         chern_scale(chern_times(k2,k2),Fraction(1,12)))
        self.assertEqual(chern_transfer_core()['reflexive_control_normalized_third_coefficient'],'1/2')
        self.assertFalse(chern_transfer_core()['reflexive_control_Weil_projection_nonzero'])

    def test_all_transfer_probes_are_formal_and_old_filter_blind(self):
        records = chern_transfer_core()['conditional_transfer_controls']
        self.assertEqual(len(records),6)
        self.assertTrue(all(r['formal_input_only'] and not r['old_P8_image_nonzero'] for r in records))
        self.assertFalse(self.data['transfer']['input_bundle_supplied'])

    def test_zero_rank_normalization_rejected(self):
        with self.assertRaisesRegex(ValueError,'positive integral'):
            chern_character(0)

    def test_projected_fourth_Chern_formula_is_bound(self):
        self.data['projected_formulas']['A'] = 'Pi_exc kappa4=Pi_exc ch4'
        with self.assertRaisesRegex(ValueError,'formula binding'):
            validate_transfer(self.data)


class HodgeReflexiveReductionTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(REDUCTION_CONTRACT.read_text(encoding='utf-8'))

    def test_dimension_eight_does_not_exclude_the_second_stratum(self):
        self.data['geometry']['ambient_complex_dimension'] = 8
        with self.assertRaisesRegex(ValueError,'dimension scope'):
            validate_reduction(self.data)

    def test_only_projected_not_full_normalization_is_preserved(self):
        self.data['policy']['preserves_full_kappa3'] = True
        with self.assertRaisesRegex(ValueError,'scope promoted'):
            validate_reduction(self.data)

    def test_rank_two_quotient_is_not_a_bundle_at_D(self):
        self.data['policy']['quotient_is_locally_free_at_singular_locus'] = True
        with self.assertRaisesRegex(ValueError,'scope promoted'):
            validate_reduction(self.data)

    def test_arbitrary_prescribed_threefold_is_not_realized_by_the_reduction(self):
        self.data['policy']['arbitrary_prescribed_threefold_realized_as_singular_locus'] = True
        with self.assertRaisesRegex(ValueError,'scope promoted'):
            validate_reduction(self.data)

    def test_pure_effective_Weil_class_is_not_the_positive_search_target(self):
        self.data['policy']['pure_Weil_effective_threefold_required'] = True
        with self.assertRaisesRegex(ValueError,'scope promoted'):
            validate_reduction(self.data)

    def test_formal_source_is_not_a_supplied_bundle(self):
        self.data['policy']['source_bundle_supplied'] = True
        with self.assertRaisesRegex(ValueError,'scope promoted'):
            validate_reduction(self.data)

    def test_higher_codimension_singularities_do_not_supply_third_data(self):
        self.data['singularity_cycle']['singularities_only_in_codimension_at_least_four_suffice'] = True
        with self.assertRaisesRegex(ValueError,'Ext scope'):
            validate_reduction(self.data)

    def test_higher_Ext_is_not_silently_used_for_a_third_cycle(self):
        self.data['singularity_cycle']['higher_Ext_contributes_to_ch3'] = True
        with self.assertRaisesRegex(ValueError,'Ext scope'):
            validate_reduction(self.data)

    def test_existence_equivalence_does_not_choose_the_positive_branch(self):
        self.data['positive_branch_decided'] = True
        with self.assertRaisesRegex(ValueError,'branch not decided'):
            validate_reduction(self.data)

    def test_actual_split_control_and_duality_do_not_supply_a_Weil_witness(self):
        r = reduction_core()
        self.assertEqual(r['rank_two_singularity_cycle_identity'],
            'c3(F)=ch3(Ext1(F,O_X))=2*kappa3(F)')
        self.assertEqual(r['split_control_chern_coefficients'],[4,6,4])
        self.assertEqual(r['split_control_normalized_third_coefficient'],2)
        self.assertFalse(r['split_control_Weil_projection_nonzero'])
        self.assertEqual(r['polarization_sixth_power'],2160)

    def test_all_nonzero_Weil_rank_twist_probes_are_formal(self):
        records = reduction_core()['formal_rank_twist_controls']
        self.assertEqual(len(records),12)
        self.assertTrue(all(r['formal_input_only'] and r['projected_kappa3_preserved'] for r in records))
        self.assertFalse(self.data['policy']['source_bundle_supplied'])

    def test_rank_and_corank_dimension_boundaries(self):
        with self.assertRaisesRegex(ValueError,'rank at least three'):
            strata(2)
        self.assertIsNone(strata(3)['second_corank_codimension'])
        self.assertEqual(strata(4)['second_corank_codimension'],8)
        self.assertEqual(strata(4)['first_corank_codimension'],3)


class HodgeCyclicPrymTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(PRYM_CONTRACT.read_text(encoding='utf-8'))

    def test_unbalanced_signature_not_admitted(self):
        self.data['geometry']['signature'] = [4,2]
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_prym(self.data)

    def test_integral_deck_lattice_cannot_be_dropped(self):
        self.data['geometry']['integral_Gaussian_deck_action_retained'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_prym(self.data)

    def test_Prym_raw_norm_class_cannot_be_replaced_by_target_class(self):
        self.data['geometry']['raw_discriminant_norm_class'] = '-3'
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_prym(self.data)

    def test_printed_delta_one_is_not_automatically_raw_det_plus_one(self):
        self.data['source_policy']['source_delta_identified_with_our_raw_det_plus_one'] = True
        with self.assertRaisesRegex(ValueError,'convention scope'):
            validate_prym(self.data)

    def test_cyclic_Prym_exclusion_is_not_all_Pryms(self):
        self.data['scope_policy']['all_Prym_presentations_excluded'] = True
        with self.assertRaisesRegex(ValueError,'exclusion promoted'):
            validate_prym(self.data)

    def test_ramification_does_not_bypass_this_kernel_argument(self):
        self.data['geometry']['ramified_covers_included'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_prym(self.data)

    def test_sixfold_argument_does_not_exclude_auxiliary_eightfold(self):
        self.data['scope_policy']['eightfold_A_excluded'] = True
        with self.assertRaisesRegex(ValueError,'exclusion promoted'):
            validate_prym(self.data)

    def test_moduli_dimension_alone_does_not_exclude_fixed_period(self):
        self.data['scope_policy']['dimension_bound_alone_excludes_fixed_X'] = True
        with self.assertRaisesRegex(ValueError,'exclusion promoted'):
            validate_prym(self.data)

    def test_type_upper_bound_is_not_realization_theorem(self):
        self.data['scope_policy']['all_seven_polarization_types_realized'] = True
        with self.assertRaisesRegex(ValueError,'exclusion promoted'):
            validate_prym(self.data)

    def test_primary_source_hash_drift_rejected(self):
        data = load(PRYM_SNAPSHOT)
        data['files'][0]['sha256'] = '0'*64
        with patch('check_hodge_cyclic_prym_audit.load',return_value=data):
            with self.assertRaisesRegex(ValueError,'source drift'):
                validate_prym_sources()

    def test_primary_source_coverage_cannot_omit_PDF_or_images(self):
        data = load(PRYM_SNAPSHOT)
        data['files'][0] = data['files'][1]
        with patch('check_hodge_cyclic_prym_audit.load',return_value=data):
            with self.assertRaisesRegex(ValueError,'source coverage'):
                validate_prym_sources()

    def test_exact_type_bounds_and_lattice_control_are_scoped(self):
        r = prym_core()
        self.assertEqual(len(r['possible_elementary_divisor_type_bounds']),7)
        self.assertEqual(r['repolarization_basis_controls'],140)
        self.assertTrue(all(x['candidate_ratio_v3'] == 1 for x in r['possible_elementary_divisor_type_bounds']))
        self.assertEqual(r['PPAV_permutation_lattice_determinant'],-64)
        self.assertFalse(r['PPAV_lattice_control_is_a_curve_Jacobian'])


class HodgePrincipalIsogenyTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(PRINCIPAL_CONTRACT.read_text(encoding='utf-8'))

    def reject_policy(self,key):
        self.data['policy'][key] = True
        with self.assertRaisesRegex(ValueError,'quotient scope promoted'):
            validate_isogeny(self.data)

    def test_isogeny_degree_is_nine_not_three(self):
        self.data['geometry']['quotient_degree'] = 3
        with self.assertRaisesRegex(ValueError,'quotient geometry'):
            validate_isogeny(self.data)

    def test_Weil_pullback_factor_is_three_not_nine(self):
        self.data['transfer']['Weil_pullback_factor'] = 9
        with self.assertRaisesRegex(ValueError,'transfer normalization'):
            validate_isogeny(self.data)

    def test_normalized_reverse_is_not_unnormalized_reverse(self):
        self.data['transfer']['normalized_reverse_denominator'] = 1
        with self.assertRaisesRegex(ValueError,'transfer normalization'):
            validate_isogeny(self.data)

    def test_original_candidate_cannot_be_replaced(self):
        self.data['geometry']['original_candidate_X_changed'] = True
        with self.assertRaisesRegex(ValueError,'quotient geometry'):
            validate_isogeny(self.data)

    def test_marking_change_is_not_an_endomorphism(self):
        self.reject_policy('marking_matrix_is_an_endomorphism_of_A')

    def test_principal_split_eightfold_is_not_automatically_a_Prym(self):
        self.reject_policy('Prym_cover_constructed')

    def test_isogeny_does_not_make_Y_generic(self):
        self.reject_policy('generic_Weil_eightfold_claimed')

    def test_other_Chow_composition_not_proved_by_cohomology(self):
        self.reject_policy('q_pull_q_push_equals_9_on_Chow_claimed')

    def test_transferred_cohomology_retraction_not_promoted_to_Chow(self):
        self.reject_policy('transported_Chow_retraction_claimed')

    def test_transferred_filter_not_silently_a_Chow_idempotent(self):
        self.reject_policy('transported_rank_eight_formula_Chow_idempotence_claimed')

    def test_fixed_polarization_obstruction_does_not_exclude_other_B_polarizations(self):
        self.reject_policy('B_has_no_other_principal_polarization')

    def test_sixfold_theorem_cannot_be_applied_to_Y(self):
        self.reject_policy('sixfold_Koike_theorem_applied_to_Y')

    def test_exact_quotient_and_normalized_transfer_controls(self):
        r = principal_core()
        self.assertEqual(r['quotient_degree'],9)
        self.assertEqual(r['full_H8_inverse_basis_count'],12870)
        self.assertEqual(len(r['maximal_mixed_isotropic_Gaussian_lines_mod3']),4)
        r6,i6 = weil_forms(6)
        r8,i8 = weil_forms(8)
        for v,w in ((r6,r8),(i6,i8)):
            self.assertEqual(q_pull(w),scale(w,3))
            self.assertEqual(q_push(w),scale(w,3))
            self.assertEqual(forward_Y(v),w)
            self.assertEqual(reverse_Y(w),v)
            self.assertTrue(any(channels_Y(w)))

    def test_coordinate_escape_rejected(self):
        with self.assertRaisesRegex(ValueError,'invalid isogeny coordinates'):
            q_pull({(16,):Fraction(1)})

    def test_principal_quotient_is_not_a_nonzero_algebraic_Weil_source(self):
        self.data['boundary']['nonzero_algebraic_Weil_class_constructed'] = True
        with self.assertRaisesRegex(ValueError,'verdict promotion'):
            validate_isogeny(self.data)


class HodgePrincipalPrymMembershipTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(MEMBERSHIP_CONTRACT.read_text(encoding='utf-8'))

    def reject_scope(self,key):
        self.data['scope_policy'][key] = True
        with self.assertRaisesRegex(ValueError,'Prym exclusion promoted'):
            validate_membership(self.data)

    def test_canonical_principal_Prym_polarization_cannot_be_dropped(self):
        self.data['geometry']['canonical_principal_Prym_polarization'] = False
        with self.assertRaisesRegex(ValueError,'Prym geometry scope'):
            validate_membership(self.data)

    def test_elliptic_polarization_degree_is_three_not_isogeny_degree(self):
        self.data['geometry']['embedded_Eminus_degree'] = 9
        with self.assertRaisesRegex(ValueError,'Prym geometry scope'):
            validate_membership(self.data)

    def test_pullback_polarization_cannot_be_changed(self):
        self.data['geometry']['pullback_polarization'] = '2 E_A'
        with self.assertRaisesRegex(ValueError,'Prym geometry scope'):
            validate_membership(self.data)

    def test_other_polarizations_not_excluded(self):
        self.reject_scope('other_polarizations_excluded')

    def test_other_isogenous_principal_models_not_excluded(self):
        self.reject_scope('all_isogenous_principal_models_excluded')

    def test_ramified_covers_not_excluded(self):
        self.reject_scope('ramified_Pryms_excluded')

    def test_singular_admissible_covers_not_excluded(self):
        self.reject_scope('singular_admissible_covers_excluded')

    def test_unpolarized_isomorphism_not_sufficient(self):
        self.reject_scope('unpolarized_isomorphism_suffices')

    def test_moduli_dimension_not_a_membership_proof(self):
        self.reject_scope('moduli_dimension_alone_used')

    def test_Mumford_source_hash_drift_rejected(self):
        data = load(MEMBERSHIP_SNAPSHOT)
        data['files'][0]['sha256'] = '0'*64
        with patch('check_hodge_principal_prym_membership.load',return_value=data):
            with self.assertRaisesRegex(ValueError,'Mumford source drift'):
                validate_membership_sources()

    def test_Mumford_theorem_image_coverage_cannot_be_dropped(self):
        data = load(MEMBERSHIP_SNAPSHOT)
        data['files'][-1] = data['files'][0]
        with patch('check_hodge_principal_prym_membership.load',return_value=data):
            with self.assertRaisesRegex(ValueError,'Mumford source coverage'):
                validate_membership_sources()

    def test_four_quotients_not_just_one_are_audited(self):
        self.data['geometry']['quotient_count'] = 1
        with self.assertRaisesRegex(ValueError,'Prym geometry scope'):
            validate_membership(self.data)

    def test_exact_kernel_theta_and_genus_controls(self):
        r = membership_core()
        self.assertEqual(r['fixed_polarization_principal_quotient_count'],4)
        self.assertTrue(all(x['intersection_with_each_bad_factor_order'] == 1 for x in r['quotient_controls']))
        self.assertEqual((r['theta_product_crossing_dimension'],r['Mumford_nonhyperelliptic_upper_bound']),(6,4))
        self.assertEqual((r['hyperelliptic_genus_required'],r['coprime_elliptic_cover_genus_upper_bound']),(7,5))

    def test_coprime_birationality_shortcut_requires_coprimality(self):
        self.assertEqual(coprime_genus_bound(2,0,3,1),5)
        with self.assertRaisesRegex(ValueError,'coprime degrees required'):
            coprime_genus_bound(2,0,2,1)
        self.assertFalse(5 > coprime_genus_bound(2,0,3,1))

    def test_global_witness_search_cannot_be_declared_complete(self):
        self.data['boundary']['global_witness_search_completed'] = True
        with self.assertRaisesRegex(ValueError,'Prym verdict promotion'):
            validate_membership(self.data)

    def test_OCR_inequalities_need_rendered_theorem_check(self):
        self.data['source_policy']['theorem_inequalities_checked_against_rendered_images'] = False
        with self.assertRaisesRegex(ValueError,'Prym source policy'):
            validate_membership(self.data)

    def test_hypothetical_curve_not_a_supplied_geometric_source(self):
        self.reject_scope('actual_hyperelliptic_curve_constructed')


class HodgeIndecomposableModelTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(INDECOMPOSABLE_CONTRACT.read_text(encoding='utf-8'))

    def reject_policy(self,key):
        self.data['policy'][key] = True
        with self.assertRaisesRegex(ValueError,'successor scope promoted'):
            validate_model(self.data)

    def test_pullback_is_two_EA_not_the_excluded_fixed_EA(self):
        self.data['geometry']['pullback_polarization_multiplier'] = 1
        with self.assertRaisesRegex(ValueError,'successor model geometry'):
            validate_model(self.data)

    def test_two_primary_step_degree_is_256(self):
        self.data['geometry']['step_degree'] = 16
        with self.assertRaisesRegex(ValueError,'successor model geometry'):
            validate_model(self.data)

    def test_imaginary_Weil_determinant_not_its_absolute_value(self):
        self.data['transfer']['Gaussian_composite_determinant'] = [48,0]
        with self.assertRaisesRegex(ValueError,'successor transfer phase'):
            validate_model(self.data)

    def test_original_alpha_transfers_to_Inew_not_Rnew(self):
        self.data['transfer']['R6_forward_image'] = 'Rnew'
        with self.assertRaisesRegex(ValueError,'successor transfer phase'):
            validate_model(self.data)

    def test_transfer_denominator_not_isogeny_degree(self):
        self.data['transfer']['normalized_denominator'] = 2304
        with self.assertRaisesRegex(ValueError,'successor transfer phase'):
            validate_model(self.data)

    def test_factorized_certificate_is_not_an_explicit_global_census(self):
        self.data['transfer']['certificate'] = '12870_explicit_global_columns'
        with self.assertRaisesRegex(ValueError,'certificate scope'):
            validate_model(self.data)

    def test_lattice_marking_not_old_endomorphism(self):
        self.reject_policy('marking_change_is_endomorphism_of_A')

    def test_indecomposable_not_Prym_membership(self):
        self.reject_policy('Prym_cover_constructed')

    def test_new_Prym_membership_not_excluded_by_old_result(self):
        self.reject_policy('Prym_presentation_excluded')

    def test_old_product_crossing_not_reused(self):
        self.reject_policy('Mumford_product_crossing_argument_reused')

    def test_cohomological_retraction_not_Chow_retraction(self):
        self.reject_policy('Chow_retraction_claimed')

    def test_isogeny_model_not_generic_Weil_eightfold(self):
        self.reject_policy('generic_Weil_eightfold_claimed')

    def test_exact_certificate_phase_and_elliptic_axes(self):
        r = indecomposable_core()
        self.assertEqual(r['factorized_inverse_local_exterior_columns'],48)
        self.assertEqual(r['explicit_global_H8_sample_columns'],4)
        self.assertEqual(r['factorized_certificate_H8_dimension'],12870)
        self.assertEqual(r['elliptic_axis_isogeny_degrees'],[1,2])
        self.assertEqual(r['elliptic_axis_polarization_degrees'],[2,3])
        r6,i6 = weil_forms(6)
        r8,i8 = weil_forms(8)
        self.assertEqual(forward_new(r6),i8)
        self.assertEqual(forward_new(i6),scale(r8,-1))
        self.assertEqual(reverse_new(i8),r6)
        self.assertEqual(reverse_new(r8),scale(i6,-1))

    def test_successor_coordinate_escape_rejected(self):
        with self.assertRaisesRegex(ValueError,'invalid successor coordinates'):
            f_pull({(16,):Fraction(1)})

    def test_no_nonzero_algebraic_Weil_source_from_model_alone(self):
        self.data['boundary']['nonzero_algebraic_Weil_class_constructed'] = True
        with self.assertRaisesRegex(ValueError,'successor verdict promotion'):
            validate_model(self.data)

    def test_theta_singular_locus_dimension_not_computed_here(self):
        self.reject_policy('theta_singular_locus_dimension_computed')

    def test_original_sixfold_not_changed(self):
        self.data['geometry']['original_candidate_X_changed'] = True
        with self.assertRaisesRegex(ValueError,'successor model geometry'):
            validate_model(self.data)


class HodgeY2CurveAuditTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Y2_CURVE_CONTRACT.read_text(encoding='utf-8'))

    def reject_scope(self,key):
        self.data['scope_policy'][key] = True
        with self.assertRaisesRegex(ValueError,'Y2 curve exclusion promoted'):
            validate_y2_curve(self.data)

    def test_polarized_Jacobian_requirement_cannot_be_dropped(self):
        self.data['geometry']['fixed_principal_Y2'] = False
        with self.assertRaisesRegex(ValueError,'Y2 curve geometry scope'):
            validate_y2_curve(self.data)

    def test_elliptic_curve_degree_two_not_polarization_hom_degree_four(self):
        self.data['geometry']['elliptic_polarization_degree'] = 4
        with self.assertRaisesRegex(ValueError,'Y2 curve geometry scope'):
            validate_y2_curve(self.data)

    def test_Gaussian_square_minus_identity_required(self):
        self.data['geometry']['Gaussian_automorphism_square'] = 'identity'
        with self.assertRaisesRegex(ValueError,'Y2 curve geometry scope'):
            validate_y2_curve(self.data)

    def test_intermediate_genus_nine_not_bottom_genus_five(self):
        self.data['geometry']['etale_double_cover_base_genus'] = 5
        with self.assertRaisesRegex(ValueError,'Y2 curve geometry scope'):
            validate_y2_curve(self.data)

    def test_trigonal_free_involution_premise_cannot_be_dropped(self):
        self.data['geometry']['free_intermediate_involution_required_for_trigonal_exclusion'] = False
        with self.assertRaisesRegex(ValueError,'Y2 curve geometry scope'):
            validate_y2_curve(self.data)

    def test_weak_unpolarized_Torelli_not_enough(self):
        self.data['imports']['strong_polarized_Torelli'] = 'unpolarized isogeny'
        with self.assertRaisesRegex(ValueError,'Y2 curve theorem imports'):
            validate_y2_curve(self.data)

    def test_low_gonality_rejection_not_all_Pryms(self):
        self.reject_scope('all_smooth_etale_Prym_presentations_of_Y2_excluded')

    def test_conditional_bielliptic_requirement_not_unconditional(self):
        self.reject_scope('conditional_biellipticity_is_unconditional')

    def test_theta_dimension_not_computed(self):
        self.reject_scope('theta_singularity_dimension_computed')

    def test_genus_five_base_not_excluded_by_genus_nine_argument(self):
        self.reject_scope('genus5_base_excluded_by_this_argument')

    def test_reflection_anti_invariance_not_exceptional_test(self):
        self.reject_scope('reflection_anti_invariance_is_exceptional_test')

    def test_exact_reflection_and_nonzero_algebraic_anti_control(self):
        r = y2_curve_core()
        self.assertEqual(r['reflection_anti_full_H8_rank'],6864)
        self.assertTrue(r['reflection_anti_algebraic_divisor_control_nonzero'])
        self.assertTrue(r['reflection_anti_control_all_four_exceptional_channels_zero'])
        self.assertEqual(sum(x['involutions_checked'] for x in r['weighted_odd_fibre_controls']),6)
        self.assertIsNone(r['actual_theta_singularity_dimension'])

    def test_even_degree_bound_uses_new_independence_not_coprime_shortcut(self):
        self.assertEqual(hyperelliptic_elliptic_genus_bound(2),3)
        self.assertEqual(hyperelliptic_elliptic_genus_bound(3),5)
        with self.assertRaisesRegex(ValueError,'coprime degrees required'):
            coprime_genus_bound(2,0,2,1)

    def test_unique_trigonal_threshold_does_not_exclude_genus_four(self):
        self.assertFalse(trigonal_free_involution_obstruction(4))
        self.assertTrue(trigonal_free_involution_obstruction(5))
        self.assertTrue(trigonal_free_involution_obstruction(9))

    def test_conditional_theta_table_does_not_choose_unknown_branch(self):
        self.assertEqual(conditional_prym_gate(None),'undetermined_dimension_not_computed')
        self.assertEqual(conditional_prym_gate(4),'cyclic_quartic_realization_requires_bielliptic_genus9_intermediate')
        self.assertEqual(conditional_prym_gate(5),'excluded_as_smooth_etale_Prym_by_Mumford')
        self.assertIn('no_further',conditional_prym_gate(3))

    def test_Torelli_primary_file_hash_drift_rejected(self):
        d = load(Y2_CURVE_SNAPSHOT)
        d['files'][0]['sha256'] = '0'*64
        with patch('check_hodge_y2_curve_audit.load',return_value=d):
            with self.assertRaisesRegex(ValueError,'Torelli source drift'):
                validate_y2_curve_sources()

    def test_Torelli_rendered_theorem_page_must_be_pinned(self):
        d = load(Y2_CURVE_SNAPSHOT)
        d['files'][-1] = d['files'][0]
        with patch('check_hodge_y2_curve_audit.load',return_value=d):
            with self.assertRaisesRegex(ValueError,'Torelli source coverage'):
                validate_y2_curve_sources()


class HodgeHyperellipticBottomTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(BOTTOM_CONTRACT.read_text(encoding='utf-8'))

    def test_bottom_not_intermediate(self):
        self.data['geometry']['hyperelliptic_curve_in_unconditional_exclusion'] = 'genus9_intermediate'
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_bottom(self.data)

    def test_etale_cyclic_premise_required(self):
        self.data['geometry']['top_to_bottom'] = 'ramified_cyclic_quartic'
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_bottom(self.data)

    def test_based_lift_required(self):
        self.data['geometry']['pointed_lift_at_Weierstrass_point'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_bottom(self.data)

    def test_square_factor_is_fourfold_not_sixfold(self):
        self.data['geometry']['square_factor_dimension'] = 6
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_bottom(self.data)

    def test_scope_promotions_all_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'scope promoted'):
                    validate_bottom(d)

    def test_Hodge_verdict_promotion_rejected(self):
        self.data['boundary']['Hodge_proved'] = True
        with self.assertRaisesRegex(ValueError,'verdict promotion'):
            validate_bottom(self.data)

    def test_level_root_census_cannot_be_unmarked_count(self):
        self.data['level_data']['formal_root_count'] = 512
        with self.assertRaisesRegex(ValueError,'level data'):
            validate_bottom(self.data)

    def test_exact_dihedral_and_fourfold_controls(self):
        r = bottom_core()
        self.assertEqual(r['inverting_C4_fibre_lifts_checked'],4)
        self.assertEqual(r['lift_square'],'identity')
        self.assertEqual(r['square_factor_H1_dimensions'],[8,8])
        self.assertGreater(r['fixed_simple_factor_dimension'],r['hypothetical_square_factor_dimension'])
        self.assertTrue(r['all_fixed_A_isogeny_models_excluded_for_this_cover_family'])

    def test_complete_marked_root_set(self):
        roots = torsion_roots()
        self.assertEqual(len(set(roots)),1024)
        self.assertTrue(all(tuple(2*x%4 for x in v) == (2,)+(0,)*9 for v in roots))
        self.assertEqual(len({min(v,tuple(-x%4 for x in v)) for v in roots}),512)

    def test_genus_five_bielliptic_uniqueness_not_claimed(self):
        self.assertFalse(unique_bielliptic_involution_for_genus(5))
        self.assertTrue(unique_bielliptic_involution_for_genus(6))
        self.assertTrue(unique_bielliptic_involution_for_genus(9))

    def test_unknown_theta_does_not_select_bielliptic_bottom(self):
        self.assertEqual(conditional_family(None),'not_selected_theta_dimension_unknown')
        self.assertIn('necessary_bielliptic_C5',conditional_family(4))
        self.assertIn('no_bielliptic_family',conditional_family(3))
        self.assertIn('excluded',conditional_family(5))
        self.assertIsNone(bottom_core()['actual_theta_singularity_dimension'])


class HodgeBiellipticLiftTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(LIFT_CONTRACT.read_text(encoding='utf-8'))

    def test_connected_norm_kernel_not_optional(self):
        self.data['geometry']['norm_kernel_connected'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_lift(self.data)

    def test_pointed_lift_not_optional(self):
        self.data['geometry']['pointed_lift_used_for_inverting_case'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_lift(self.data)

    def test_ramified_top_not_included(self):
        self.data['geometry']['top_cover'] = 'ramified_cyclic_quartic'
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_lift(self.data)

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'scope promoted'):
                    validate_lift(d)

    def test_all_Hodge_boundary_promotions_rejected(self):
        for key in self.data['boundary']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['boundary'][key] = True
                with self.assertRaisesRegex(ValueError,'verdict promotion'):
                    validate_lift(d)

    def test_old_root_census_not_retained_after_norm_filter(self):
        self.data['level_data']['retained_roots'] = 1024
        with self.assertRaisesRegex(ValueError,'census scope'):
            validate_lift(self.data)

    def test_norm_strata_and_inverse_pairs(self):
        r = lift_core()
        self.assertEqual(set(r['norm_stratum_counts'].values()),{256})
        self.assertEqual(r['norm_zero_excluded_root_labels'],256)
        self.assertEqual(r['retained_necessary_condition_root_labels'],768)
        self.assertEqual(r['retained_inverse_pairs'],384)
        self.assertEqual(r['nonlifting_root_labels'],512)

    def test_commuting_lift_is_not_the_dihedral_case(self):
        v = (1,)+(0,)*9
        self.assertEqual(lift_norm(v),(2,0))
        self.assertEqual(lift_deck_action(v),v)
        self.assertEqual(lift_type(lift_norm(v)),'commuting_lift_not_excluded_here')

    def test_norm_zero_lift_reverses_character(self):
        v = (1,0,0,2)+(0,)*6
        self.assertEqual(lift_norm(v),(0,0))
        self.assertEqual(lift_deck_action(v),tuple(-x%4 for x in v))
        self.assertIn('excluded_up_to_A_isogeny',lift_type(lift_norm(v)))

    def test_nonlifting_example_is_neither_generator(self):
        v = (1,2,0,2)+(0,)*6
        self.assertNotIn(lift_deck_action(v),(v,tuple(-x%4 for x in v)))
        self.assertEqual(lift_deck_action(lift_deck_action(v)),v)
        self.assertIn('no_bielliptic_involution_lift',lift_type(lift_norm(v)))

    def test_non_two_torsion_norm_rejected(self):
        with self.assertRaisesRegex(ValueError,'elliptic two-torsion'):
            lift_type((1,0))

    def test_norm_pullback_and_unknown_target(self):
        self.assertEqual(lift_norm(lift_pullback((1,1))),(2,2))
        self.assertIsNone(lift_core()['actual_theta_singularity_dimension'])
        self.assertIsNone(lift_core()['actual_matching_root_label'])
        self.assertTrue(lift_core()['conditional_on_bielliptic_intermediate'])


class HodgeCommutingPrymTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(COMMUTING_CONTRACT.read_text(encoding='utf-8'))

    def test_rank_one_NS_required_for_unpolarized_isogeny_claim(self):
        self.data['geometry']['fixed_X_rational_NS_rank'] = 2
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_commuting(self.data)

    def test_commuting_not_inverting_lift(self):
        self.data['geometry']['lift_commutes_with_rho'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_commuting(self.data)

    def test_ramified_kernel_not_etale_principal_normalization(self):
        self.data['source_policy']['corollary'] = 2
        with self.assertRaisesRegex(ValueError,'source scope'):
            validate_commuting(self.data)

    def test_source_type_not_principal(self):
        r = commuting_core()
        self.assertEqual(r['ramified_sixfold_polarization_type'],[1,1,1,1,1,2])
        self.assertEqual(r['ramified_sixfold_polarization_kernel_order'],4)
        self.assertEqual(r['ramified_sixfold_branch_count'],12)
        self.assertEqual(r['ramified_sixfold_cover_genera'],[7,1])

    def test_odd_inertia_split_not_silently_accepted(self):
        for a in (1,3,5,7):
            with self.assertRaisesRegex(ValueError,'even inertia'):
                quotient_case(a)

    def test_all_quotient_cases_accounted_for(self):
        self.assertEqual([quotient_case(a)['Prym_factor_dimensions'] for a in (0,2,4,6,8)],
            [[0,8],[2,6],[4,4],[2,6],[0,8]])
        self.assertIn('remains',quotient_case(0)['result'])
        self.assertIn('inert_three',quotient_case(2)['result'])

    def test_inert_three_parity_and_even_rank_scalar(self):
        self.assertEqual(commuting_v3(Fraction(3,2))%2,1)
        for q in (Fraction(3),Fraction(1,3),Fraction(2,9)):
            self.assertEqual(commuting_v3(2*q**6)%2,0)
        self.assertEqual(commuting_core()['fixed_X_v3_parity'],1)

    def test_four_scalar_roots_not_full_commuting_exclusion(self):
        r = commuting_core()
        self.assertEqual(len(r['pulled_formal_root_labels']),4)
        self.assertEqual(r['mixed_commuting_root_labels_excluded'],252)
        self.assertEqual(r['conditional_total_remaining_root_labels'],516)
        self.assertEqual(r['conditional_total_remaining_inverse_pairs'],258)
        self.assertEqual(r['nonlifting_root_labels_not_tested_here'],512)
        self.assertIsNone(r['actual_matching_root_label'])
        self.assertIsNone(r['actual_theta_singularity_dimension'])

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_commuting(d)

    def test_old_retained_census_not_current(self):
        self.data['level_data']['all_conditional_roots_remaining'] = 768
        with self.assertRaisesRegex(ValueError,'census scope'):
            validate_commuting(self.data)

    def test_ramified_theorem_hash_drift_rejected(self):
        d = load(COMMUTING_SNAPSHOT)
        d['files'][0]['sha256'] = '0'*64
        with patch('check_hodge_commuting_prym_audit.load',return_value=d):
            with self.assertRaisesRegex(ValueError,'source drift'):
                validate_commuting_sources()

    def test_rendered_theorem_page_must_be_covered(self):
        d = load(COMMUTING_SNAPSHOT)
        d['files'][-1] = d['files'][0]
        with patch('check_hodge_commuting_prym_audit.load',return_value=d):
            with self.assertRaisesRegex(ValueError,'source coverage'):
                validate_commuting_sources()


class HodgeEvenScalarTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(EVEN_CONTRACT.read_text(encoding='utf-8'))

    def test_affine_model_not_normalization_rejected(self):
        self.data['geometry']['top_is_normalization'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_even(self.data)

    def test_actual_lift_square_required_not_branch_set_only(self):
        self.data['geometry']['inversion_lift_fixes_cover_coordinate'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_even(self.data)

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_even(d)

    def test_kernel_and_actual_tower(self):
        r = even_core()
        self.assertEqual(r['cyclic_four_kernel_generator'],[1,3])
        self.assertEqual(r['doubled_kernel_generator'],[0,0])
        self.assertEqual(r['actual_control_tower_genera'],[17,9,5])
        self.assertTrue(r['actual_control_tower_constructed'])
        self.assertTrue(r['Prym_isogenous_to_square_fourfold'])

    def test_explicit_fourfold_quotient(self):
        r = even_core()
        self.assertEqual(r['normalized_fourfold_quotient_genera'],[7,3])
        self.assertEqual(r['fourfold_double_cover_branch_count'],4)
        self.assertEqual(r['explicit_Prym_square_factor_dimension'],4)

    def test_squarefree_equations_not_finite_point_samples(self):
        for c in (2,3,16):
            n,d,f,g = even_models(c)
            self.assertEqual(polynomial_gcd(n,d),(1,))
            self.assertEqual(polynomial_gcd(f,polynomial_derivative(f)),(1,))
            self.assertEqual(polynomial_gcd(g,polynomial_derivative(g)),(1,))
            self.assertEqual((len(f)-1,len(g)-1),(16,8))

    def test_branch_collisions_rejected(self):
        for c in (0,1,25**4):
            with self.assertRaisesRegex(ValueError,'branch zeros'):
                even_models(c)

    def test_family_subcase_does_not_delete_root_labels(self):
        r = even_core()
        self.assertEqual(r['conditional_scalar_root_count_not_updated'],4)
        self.assertEqual(r['conditional_nonlifting_root_count_not_updated'],512)
        self.assertEqual(r['conditional_total_root_label_count_not_updated'],516)
        self.assertIsNone(r['actual_theta_singularity_dimension'])


class HodgeAsymmetricScalarTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(ASYMMETRIC_CONTRACT.read_text(encoding='utf-8'))

    def test_normalization_required(self):
        self.data['geometry']['top_is_normalization'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_asymmetric(self.data)

    def test_fixed_origin_not_every_inversion(self):
        self.data['geometry']['inversion_test'] = 'all_centers'
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_asymmetric(self.data)

    def test_n1_not_full_frobenius_polynomial(self):
        self.data['geometry']['point_counts'] = 'full_Weil_polynomial'
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_asymmetric(self.data)

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_asymmetric(d)

    def test_norm_and_modular_squarefree_certificate(self):
        _,_,_,_,_,f,fs = source_equations()
        self.assertEqual([int(v) for v in f],[4,-25,26,-1,-4,0,0,0,1])
        self.assertEqual((len(f)-1,len(fs)-1),(8,32))
        self.assertEqual(modgcd_degree(fs,polynomial_derivative(fs),7),0)
        self.assertTrue(good_reduction(7))

    def test_actual_tower_and_scoped_nonlift(self):
        r = asymmetric_core()
        self.assertEqual(r['actual_tower_genera'],[17,9,5])
        self.assertTrue(r['actual_asymmetric_control_tower_constructed'])
        self.assertTrue(r['fixed_origin_inversion_has_no_lift_to_top_double_cover'])
        self.assertFalse(r['old_fixed_origin_dihedral_square_argument_available'])
        self.assertIsNone(r['actual_target_isogeny'])
        self.assertIsNone(r['actual_theta_singularity_dimension'])

    def test_normalized_point_counts_include_split_pole_fibres(self):
        r = point_profile(7)
        self.assertEqual([r[k] for k in ('C5','C9','C17')],[10,8,16])
        self.assertEqual(r['pole_fibres_split_points'],[2,4,8])
        self.assertEqual(r['primitive_Prym_trace_n1'],-8)

    def test_five_good_profiles_are_only_n1_data(self):
        rows = asymmetric_core()['good_reduction_point_profiles']
        self.assertEqual([r['p'] for r in rows],[7,11,13,17,19])
        self.assertEqual([r['primitive_Prym_trace_n1'] for r in rows],[-8,-2,-4,4,-16])
        self.assertTrue(all(r['C17']%4 == 0 and r['C9']%2 == 0 for r in rows))
        self.assertEqual(asymmetric_core()['conditional_root_label_count_not_updated'],516)

    def test_unverified_prime_not_silently_used(self):
        with self.assertRaisesRegex(ValueError,'certified prime list'):
            point_profile(3)


class HodgeAsymmetricAutomorphismTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(AUT_CONTRACT.read_text(encoding='utf-8'))

    def test_prime_to_p_specialization_required(self):
        self.data['geometry']['torsion_order_prime_to_reduction'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_aut(self.data)

    def test_genus_seventeen_uniqueness_not_arbitrary_genus(self):
        self.data['geometry']['source_curve_genus'] = 4
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_aut(self.data)

    def test_non_special_j_required(self):
        self.data['geometry']['source_elliptic_j_not_0_or_1728'] = False
        with self.assertRaisesRegex(ValueError,'geometry scope'):
            validate_aut(self.data)

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_aut(d)

    def test_full_geometric_eight_torsion_not_a_rational_subset(self):
        pts = elliptic_points(409)
        self.assertEqual(len(pts),384)
        self.assertEqual(sum(eight(P,409) is None for P in pts),64)
        self.assertEqual(sum(double(double(P,409),409) is None for P in pts),16)
        self.assertEqual(sum(double(P,409) is None for P in pts),4)

    def test_branch_ring_inverse_and_nonunit_guard(self):
        ring = BranchRing(409,source_equations()[5])
        self.assertEqual(ring.mul((0,1),ring.inverse((0,1))),(1,))
        with self.assertRaisesRegex(ValueError,'nonunit'):
            ring.inverse((0,))

    def test_origin_and_nonorigin_residues(self):
        ring = BranchRing(409,source_equations()[5])
        self.assertEqual(reflection_residue(None,ring),(405,0,0,0,2))
        self.assertEqual(translation_residue(None,ring),(0,))
        self.assertNotEqual(reflection_residue((0,0),ring),(0,))
        self.assertNotEqual(translation_residue((0,0),ring),(0,))

    def test_all_sixty_four_centers_certified(self):
        rows = aut_core()['center_certificates']
        self.assertEqual(len(rows),64)
        self.assertTrue(all(r['nonzero_reflection_residue'] != [0] for r in rows))
        self.assertEqual([r['center'] for r in rows if r['translation_residue'] == [0]],[None])

    def test_full_curve_group_not_Prym_endomorphism_group(self):
        r = aut_core()
        self.assertEqual(r['full_geometric_curve_automorphism_group'],'C4 x C2')
        self.assertEqual(r['full_geometric_curve_automorphism_group_order'],8)
        self.assertTrue(r['no_dihedral_order_eight_curve_subgroup'])
        self.assertEqual(r['source_elliptic_c4_c6_discriminant'],[736,-19936,720])
        self.assertIsNone(r['actual_target_isogeny'])
        self.assertIsNone(r['actual_theta_singularity_dimension'])
        self.assertEqual(r['conditional_root_label_count_not_updated'],516)


class HodgeAsymmetricFrobeniusTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FROB_CONTRACT.read_text(encoding='utf-8'))
        self.counts = load(FROB_COUNTS)

    def test_full_recount_not_optional(self):
        self.data['arithmetic']['full_recount_required'] = False
        with self.assertRaisesRegex(ValueError,'arithmetic scope'):
            validate_frob(self.data)

    def test_base_field_simplicity_scope_not_absolute(self):
        self.data['arithmetic']['simplicity_scope'] = 'absolute'
        with self.assertRaisesRegex(ValueError,'arithmetic scope'):
            validate_frob(self.data)

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data)
                d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_frob(d)

    def test_independent_GF49_counts(self):
        self.assertEqual(small49_counts(),(96,112))

    def test_complete_polynomial_and_ordinary_coefficient(self):
        r = verify_frob_counts(self.counts)
        c = r['L_polynomial_coefficients_ascending']
        self.assertEqual(c[:9],[1,8,40,140,453,1444,4560,13360,36360])
        self.assertEqual(c[-1],7**8)
        self.assertEqual(c[8]%7,2)
        self.assertTrue(r['reduction_simple_over_F7'])
        self.assertTrue(r['reduction_ordinary_at_7'])
        self.assertEqual(c[9],7*c[7])
        self.assertIsNone(r['actual_target_isogeny'])

    def test_n1_only_not_accepted_for_full_polynomial(self):
        self.counts['rows'] = self.counts['rows'][:1]
        with self.assertRaisesRegex(ValueError,'coverage'):
            verify_frob_counts(self.counts)
        with self.assertRaisesRegex(ValueError,'eight exact traces'):
            newton_polynomial([-8])

    def test_field_cycle_must_be_verified(self):
        self.counts['rows'][7]['full_primitive_generator_cycle_verified'] = False
        with self.assertRaisesRegex(ValueError,'cycle coverage'):
            verify_frob_counts(self.counts)

    def test_count_difference_not_an_independent_trace_input(self):
        self.counts['rows'][3]['primitive_trace'] += 1
        with self.assertRaisesRegex(ValueError,'trace/deck'):
            verify_frob_counts(self.counts)

    def test_modular_degree_sets_are_incompatible(self):
        c = newton_polynomial([r['primitive_trace'] for r in self.counts['rows']])
        rows = factor_degree_certificate(c[::-1])
        self.assertEqual(set(rows[0]['possible_rational_factor_degrees']) &
            set(rows[1]['possible_rational_factor_degrees']),{0,16})

    def test_single_auxiliary_prime_not_enough(self):
        c = newton_polynomial([r['primitive_trace'] for r in self.counts['rows']])
        with patch('check_hodge_asymmetric_frobenius.FACTORS',{5:FROB_FACTORS[5]}):
            with self.assertRaisesRegex(ValueError,'factor-degree intersection'):
                factor_degree_certificate(c[::-1])

    def test_false_modular_factors_rejected(self):
        c = newton_polynomial([r['primitive_trace'] for r in self.counts['rows']])
        altered = copy.deepcopy(FROB_FACTORS)
        altered[5][0][0] = 2
        with patch('check_hodge_asymmetric_frobenius.FACTORS',altered):
            with self.assertRaisesRegex(ValueError,'modular factor product'):
                factor_degree_certificate(c[::-1])


class HodgeAsymmetricAbsoluteTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(ABS_CONTRACT.read_text(encoding='utf-8'))
        self.c = tuple(load('research/voevodsky/results/hodge-asymmetric-frobenius-v1.json')['L_polynomial_coefficients_ascending'])

    def test_complete_order_set_with_proven_bound(self):
        orders = possible_orders(256)
        self.assertEqual((len(orders),max(orders)),(504,1050))
        self.assertNotIn(1,orders)
        self.assertEqual(possible_orders(4),[2,3,4,5,6,8,10,12])

    def test_exact_cyclotomic_controls(self):
        self.assertEqual(cyclotomic(1),(-1,1))
        self.assertEqual(cyclotomic(3),(1,1,1))
        self.assertEqual(cyclotomic(12),(1,0,-1,0,1))

    def test_all_orders_excluded_but_first_prime_not_enough(self):
        r = root_ratio_certificate(self.c)
        a,b = r['modular_witnesses']
        self.assertEqual((a['prime'],b['prime']),(409,419))
        self.assertEqual(len(a['orders_excluded_by_gcd_one']),501)
        self.assertEqual(a['remaining_orders'],[41,136,408])
        self.assertEqual(b['orders_excluded_by_gcd_one'],[41,136,408])
        self.assertEqual(b['remaining_orders'],[])
        self.assertEqual((a['independent_Sylvester_evaluations'],b['independent_Sylvester_evaluations']),(257,257))
        self.assertEqual(len(set(a['orders_excluded_by_gcd_one']+b['orders_excluded_by_gcd_one'])),504)

    def test_diagonal_ratio_one_is_not_an_obstruction(self):
        r = ratio_polynomial(self.c,7,409)
        self.assertEqual(modgcd_degree(r,cyclotomic(1),409),1)

    def test_supersingular_quadratic_negative_control(self):
        r = ratio_polynomial((1,0,7),7,409)
        self.assertEqual(r,(1,0,407,0,1))
        self.assertEqual(modgcd_degree(r,cyclotomic(2),409),1)
        self.assertEqual(verify_ratio_resultants((1,0,7),409,r),5)

    def test_order_three_negative_control(self):
        r = ratio_polynomial((1,-7,49),49,409)
        self.assertEqual(r,(1,408,0,408,1))
        self.assertEqual(modgcd_degree(r,cyclotomic(3),409),2)

    def test_corrupted_Newton_polynomial_fails_independent_resultant(self):
        r = list(ratio_polynomial((1,0,7),7,409))
        r[0] += 1
        with self.assertRaisesRegex(ValueError,'Sylvester identity'):
            verify_ratio_resultants((1,0,7),409,r)

    def test_reciprocity_is_required_not_assumed(self):
        c = list(self.c);c[-2]+=1
        with self.assertRaisesRegex(ValueError,'reciprocal polynomial'):
            ratio_polynomial(c,7,409)

    def test_invalid_moduli_rejected(self):
        for ell in (2,7,441):
            with self.subTest(ell=ell),self.assertRaisesRegex(ValueError,'admissible prime'):
                ratio_polynomial((1,0,7),7,ell)

    def test_arbitrary_cyclotomic_cutoff_rejected(self):
        self.data['arithmetic']['totient_search_bound'] = 1000
        with self.assertRaisesRegex(ValueError,'arithmetic scope'):
            validate_absolute(self.data)

    def test_specialization_cannot_run_in_the_opposite_direction(self):
        self.data['arithmetic']['specialization_direction'] = 'simple_generic_implies_simple_reduction'
        with self.assertRaisesRegex(ValueError,'arithmetic scope'):
            validate_absolute(self.data)

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d = copy.deepcopy(self.data);d['scope_policy'][key] = True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_absolute(d)


class HodgeScalarFamilyLocalizationTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(FAMILY_CONTRACT.read_text(encoding='utf-8'))

    def test_seven_dimensional_family_and_pencil_ranks(self):
        g = family_geometry()
        self.assertEqual((g['H0_A_dimension'],g['H0_B_dimension']),(4,4))
        self.assertEqual((g['pencil_kernel_dimension'],g['pencil_cokernel_dimension']),(0,0))
        self.assertEqual(g['full_multiplication_rank'],8)
        self.assertEqual(g['fixed_elliptic_period_codifferential_rank'],7)
        self.assertEqual(g['ambient_unitary_period_dimension'],16)
        self.assertTrue(g['fixed_target_isogeny_locus_at_most_countable'])

    def test_nontrivial_character_square_required(self):
        with self.assertRaisesRegex(ValueError,'line-bundle input'):
            family_geometry(character_order=2,square_order=1)

    def test_base_norm_identity(self):
        self.assertEqual(family_norm(FAMILY_BASE),(4,-25,26,-1,-4,0,0,0,1))

    def test_general_norm_remains_monic_degree_eight(self):
        f = family_norm((1,2,3,4,5,6,7))
        self.assertEqual((len(f),f[-1]),(9,1))

    def test_every_coordinate_seven_shift_is_excluded(self):
        for i in range(7):
            v=list(FAMILY_BASE);v[i]+=21
            self.assertEqual(family_sieve(v),'excluded_from_A_Y2_by_absolute_simple_reduction')
            self.assertEqual(family_mod_seven(family_norm(v)),family_mod_seven(family_norm(FAMILY_BASE)))

    def test_fractional_residue_uses_inverse_not_truncation(self):
        v=list(FAMILY_BASE);v[0]+=Fraction(7,2)
        self.assertEqual(v[0],Fraction(3,2))
        self.assertEqual(family_residues(v),(5,0,0,0,1,0,0))
        self.assertEqual(family_sieve(v),'excluded_from_A_Y2_by_absolute_simple_reduction')
        self.assertEqual(family_mod_seven((Fraction(3,2),)),(5,))

    def test_seven_divisible_denominators_rejected(self):
        v=list(FAMILY_BASE);v[0]=Fraction(1,7)
        with self.assertRaisesRegex(ValueError,'integral at seven'):
            family_sieve(v)

    def test_outside_sieve_means_unknown_not_target(self):
        v=list(FAMILY_BASE);v[0]+=1
        self.assertEqual(family_sieve(v),'not_certified_by_this_sieve')

    def test_norm_squarefree_not_necessary_for_smooth_curve(self):
        c=family_controls()
        self.assertTrue(c['smooth_even_control_outside_chart'])
        self.assertTrue(c['norm_squarefree_chart_is_sufficient_not_necessary'])
        self.assertEqual(c['residue_controls_checked'],9)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_family(d)

    def test_chart_normalization_not_optional(self):
        self.data['family']['normalized_leading_x4_coefficient']=0
        with self.assertRaisesRegex(ValueError,'family scope'):
            validate_family(self.data)

    def test_exact_seven_coordinates_required(self):
        for v in ((1,2), (0.5,0,0,0,1,0,0)):
            with self.assertRaisesRegex(ValueError,'seven exact rational'):
                family_norm(v)


class HodgeScalarPolarizedObstructionTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SCALAR_POLARIZED_CONTRACT.read_text(encoding='utf-8'))

    def test_bielliptic_prym_minimum_elliptic_degree_four(self):
        self.assertEqual(minimum_elliptic_degree(17),4)
        self.assertEqual(minimum_elliptic_degree(13),3)

    def test_curve_degree_is_two_e_not_elliptic_isogeny_degree(self):
        self.assertEqual(curve_map_degree(2),4)
        self.assertEqual(curve_map_degree(3),6)
        self.assertNotEqual(curve_map_degree(2),16)

    def test_etale_restriction_cannot_be_replaced_by_principal(self):
        with self.assertRaisesRegex(ValueError,'twice principal'):
            curve_map_degree(2,jacobian_multiplier=1)

    def test_even_degrees_do_not_supply_coprimality(self):
        self.assertEqual(joint_degrees(2,4),[1,2])
        self.assertEqual(joint_degrees(4,4),[1,2,4])

    def test_degree_four_source_cannot_use_quadratic_independence(self):
        with self.assertRaisesRegex(ValueError,'quadratic source'):
            minimum_elliptic_degree(17,source_degree=4)
        self.assertEqual(independent_elliptic_genus_bound(4,4),17)

    def test_nonbirational_joint_map_not_given_genus_bound(self):
        with self.assertRaisesRegex(ValueError,'birational joint image'):
            independent_elliptic_genus_bound(2,4,joint_degree=2)

    def test_genus_equality_at_e_four_not_excluded(self):
        c = scalar_polarized_core()
        self.assertEqual(c['elliptic_degree_controls'][-1]['genus_upper_bound_after_independence'],17)
        self.assertFalse(c['elliptic_degree_controls'][-1]['excluded_at_genus17'])

    def test_low_degree_genus_bounds(self):
        self.assertEqual([independent_elliptic_genus_bound(2,curve_map_degree(e)) for e in (1,2,3)],[5,9,13])

    def test_correspondence_terms_do_not_raise_genus_bound(self):
        rows = scalar_polarized_core()['correspondence_intersection_controls']
        self.assertEqual([r['arithmetic_genus'] for r in rows],[9,8,8,7])

    def test_polarized_and_unpolarized_censuses_are_distinct(self):
        c = scalar_polarized_census()
        self.assertEqual((c['conditional_polarized_Y2_survivor_labels'],c['conditional_polarized_Y2_survivor_inverse_pairs']),(512,256))
        self.assertEqual((c['conditional_unpolarized_isogeny_survivor_labels'],c['conditional_unpolarized_isogeny_survivor_inverse_pairs']),(516,258))

    def test_unpolarized_comparison_not_substituted(self):
        self.data['geometry']['comparison'] = 'arbitrary_unpolarized_isogeny'
        with self.assertRaisesRegex(ValueError,'polarized scope'):
            validate_scalar_polarized(self.data)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_scalar_polarized(d)


class HodgeNonliftingPolarizedObstructionTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(NONLIFTING_CONTRACT.read_text(encoding='utf-8'))

    def test_all_three_joint_degrees_exhausted(self):
        c=nonlifting_core()
        self.assertEqual(c['joint_degrees_exhausted'],[1,2,4])
        self.assertTrue(all(v.startswith('excluded_') for v in c['joint_cases'].values()))

    def test_joint_degree_one_uses_smooth_image_fixed_points(self):
        self.assertEqual(joint_case(1),'excluded_by_smooth_image_reflection_fixed_points')
        self.assertEqual(nonlifting_core()['birational_image_normalization_defect'],0)

    def test_genus_below_equality_may_separate_fixed_image_branches(self):
        self.assertEqual(birational_case(15),'normalization_may_separate_branches_not_excluded')

    def test_free_involution_is_essential(self):
        self.assertEqual(birational_case(17,False),'fixed_points_permitted_no_etale_contradiction')

    def test_above_genus_bound_is_a_different_obstruction(self):
        self.assertEqual(birational_case(19),'excluded_by_genus_bound')

    def test_joint_degree_two_forces_lift_not_universal_lifting(self):
        self.assertEqual(joint_case(2),'excluded_by_forced_bielliptic_lift')
        self.assertEqual(joint_case(2,b_liftable=True),'involutive_lift_forced_no_nonlifting_contradiction')

    def test_quadratic_deck_involution_descends_nontrivially(self):
        c=v4_control()
        self.assertNotEqual(c['generic_fibre_h_permutation'],c['generic_fibre_sigma_permutation'])
        self.assertTrue(c['sigma_descends_nontrivially_on_h_quotient'])
        self.assertTrue(c['h_descends_nontrivially_on_sigma_quotient'])

    def test_joint_degree_four_is_invariant_factorization(self):
        self.assertEqual(joint_case(4),'excluded_by_invariant_vs_anti_invariant_factorization')

    def test_no_unlisted_joint_degree_admitted(self):
        for d in (0,3,8,True):
            with self.subTest(degree=d),self.assertRaisesRegex(ValueError,'joint degree coverage'):
                joint_case(d)

    def test_zero_polarized_survivors_not_zero_unpolarized(self):
        c=nonlifting_core()
        self.assertEqual((c['conditional_polarized_Y2_survivor_labels'],c['conditional_polarized_Y2_survivor_inverse_pairs']),(0,0))
        self.assertEqual((c['conditional_unpolarized_isogeny_survivor_labels'],c['conditional_unpolarized_isogeny_survivor_inverse_pairs']),(516,258))

    def test_theta_gate_not_actual_dimension(self):
        self.assertEqual(nonlifting_theta_gate(None),'undetermined_actual_dimension_not_computed')
        self.assertEqual(nonlifting_theta_gate(3),'no_exclusion_from_this_theta_gate')
        self.assertEqual(nonlifting_theta_gate(4),'excluded_fixed_Y2_smooth_etale_cyclic_quartic_realization')
        self.assertIsNone(nonlifting_core()['actual_theta_singularity_dimension'])

    def test_invalid_theta_dimensions_rejected(self):
        for d in (-2,8,True,'4'):
            with self.subTest(d=d),self.assertRaisesRegex(ValueError,'theta singularity dimension'):
                nonlifting_theta_gate(d)

    def test_contract_cannot_drop_freeness(self):
        self.data['geometry']['h_free']=False
        with self.assertRaisesRegex(ValueError,'nonlifting scope'):
            validate_nonlifting(self.data)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_nonlifting(d)


class HodgeEquivariantTetragonalGateTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TETRAGONAL_CONTRACT.read_text(encoding='utf-8'))

    def test_pencil_joint_degree_exhaustion(self):
        c=tetragonal_core()
        self.assertEqual(c['pencil_joint_degrees_exhausted'],[1,2,4])
        self.assertEqual(c['birational_4_4_P1_product_arithmetic_genus'],9)
        self.assertEqual(c['fixed_diagonal_intersection_degree'],8)
        self.assertEqual(c['necessary_C9_gonality'],4)

    def test_birational_fixed_diagonal_uses_freeness(self):
        self.assertEqual(tetragonal_joint_case(1),'excluded_by_smooth_4_4_image_and_fixed_diagonal')
        self.assertEqual(tetragonal_joint_case(1,free=False),'fixed_points_permitted')

    def test_below_genus_equality_normalization_escape_not_ignored(self):
        self.assertEqual(tetragonal_joint_case(1,genus=7),'singular_image_may_separate_fixed_branches')

    def test_quadratic_joint_factor_requires_both_curve_exclusions(self):
        self.assertEqual(tetragonal_joint_case(2),'excluded_by_rational_or_elliptic_quadratic_quotient')
        self.assertEqual(tetragonal_joint_case(2,nonhyperelliptic=False),'quadratic_quotient_not_excluded')
        self.assertEqual(tetragonal_joint_case(2,nonbielliptic=False),'quadratic_quotient_not_excluded')

    def test_degree_four_joint_factor_is_pencil_invariance(self):
        self.assertEqual(tetragonal_joint_case(4),'invariant_pencil')

    def test_only_two_even_degree_four_partitions(self):
        for p in ((4,),(2,2)):
            self.assertTrue(tetragonal_even_partition(p))
        for p in ((3,1),(2,1,1),(1,1,1,1)):
            self.assertFalse(tetragonal_even_partition(p))

    def test_odd_multiplicities_not_etale_pullback(self):
        with self.assertRaisesRegex(ValueError,'odd multiplicity'):
            tetragonal_budget(((4,),(4,),(4,),(3,1)),9)

    def test_top_ramification_budgets_total_thirty_two(self):
        rows=tetragonal_core()['top_ramification_budgets']
        self.assertEqual(len(rows),16)
        for r in rows:
            self.assertEqual(r['total_ramification'],24)
            self.assertEqual(r['C17_to_CM_elliptic_ramification_at_branch_values']+
                r['C17_to_CM_elliptic_ramification_elsewhere'],32)

    def test_bottom_ramification_budgets_total_twenty_four(self):
        rows=tetragonal_core()['bottom_ramification_budgets']
        self.assertEqual(len(rows),4)
        for r in rows:
            self.assertEqual(r['total_ramification'],16)
            self.assertEqual(r['C9_to_P1_ramification_at_branch_values']+
                r['C9_to_P1_ramification_elsewhere'],24)

    def test_harmonic_cross_ratios_exact_CM_j(self):
        for lam in (-1,2,Fraction(1,2)):
            self.assertEqual(tetragonal_j(lam),1728)
        self.assertNotEqual(tetragonal_j(3),1728)
        with self.assertRaisesRegex(ValueError,'distinct branch'):
            tetragonal_j(1)

    def test_norm_minus_one_not_plus_one_is_cyclic_four(self):
        self.assertEqual(tetragonal_lift_order(-1),4)
        self.assertEqual(tetragonal_lift_order(1),2)

    def test_invalid_lift_norm_not_admitted(self):
        for n in (0,2,True):
            with self.subTest(norm=n),self.assertRaisesRegex(ValueError,'plus or minus one'):
                tetragonal_lift_order(n)

    def test_even_fibre_parity_cannot_replace_connectedness(self):
        self.data['geometry']['connected_square_classes_required']=False
        with self.assertRaisesRegex(ValueError,'tetragonal scope'):
            validate_tetragonal(self.data)

    def test_cyclic_lift_norm_cannot_be_V4(self):
        self.data['geometry']['cyclic_lift_norm']=1
        with self.assertRaisesRegex(ValueError,'tetragonal scope'):
            validate_tetragonal(self.data)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'promotion'):
                    validate_tetragonal(d)


class HodgeEightfoldLiteratureAuditTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(EIGHTFOLD_LITERATURE_CONTRACT.read_text(encoding='utf-8'))

    def test_corrected_gaussian_character(self):
        self.assertEqual(secant_character(9,3),[Fraction(1),Fraction(3),Fraction(-9,2),Fraction(-9,2),Fraction(27,8)])
        self.assertTrue(in_secant_plane(secant_character(9,3),9))

    def test_displayed_twist_fails(self):
        self.assertEqual(secant_character(9,1)[2],Fraction(-17,2))
        self.assertFalse(in_secant_plane(secant_character(9,1),9))

    def test_normalization_points_are_essential(self):
        self.assertFalse(in_secant_plane(secant_character(9,3,False),9))
        self.assertEqual(secant_character(9,3,False)[4]-secant_character(9,3)[4],Fraction(306,24))

    def test_wrong_field_parameter_not_imported(self):
        self.data['geometry']['secant_d']=3
        with self.assertRaisesRegex(ValueError,'literature geometry'):
            validate_eightfold_literature(self.data)

    def test_reversing_K_class_fails_rank_one_plane_control(self):
        ch=secant_character(9,3);ch[0]=-ch[0]
        self.assertFalse(in_secant_plane(ch,9))

    def test_no_author_erratum_asserted(self):
        self.data['scope_policy']['author_confirmed_erratum']=True
        with self.assertRaisesRegex(ValueError,'literature promotion'):
            validate_eightfold_literature(self.data)

    def test_question_is_not_a_theorem(self):
        self.data['scope_policy']['question_11_4_used_as_theorem']=True
        with self.assertRaisesRegex(ValueError,'literature promotion'):
            validate_eightfold_literature(self.data)

    def test_all_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'literature promotion'):
                    validate_eightfold_literature(d)

    def test_pending_source_cannot_be_resolved(self):
        self.data['research_queue'][2]['status']='resolved'
        with self.assertRaisesRegex(ValueError,'research queue promotion'):
            validate_eightfold_literature(self.data)

    def test_ramified_tower_dimensions(self):
        self.assertEqual(cyclic_genera(4,[1,3]),[16,8,4])
        self.assertEqual(cyclic_genera(5,[1,3]),[20,10,5])

    def test_unpaired_monodromy_rejected(self):
        with self.assertRaisesRegex(ValueError,'paired fully ramified'):
            cyclic_genera(4,[1,1])

    def test_source_manifest_tampering_rejected(self):
        with patch('check_hodge_eightfold_literature_audit.SNAPSHOT') as source:
            source.read_bytes.return_value=b'tampered'
            with self.assertRaisesRegex(ValueError,'literature manifest drift'):
                validate_eightfold_literature_sources()


class HodgeSecantLocalExtGateTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(SECANT_LOCAL_CONTRACT.read_text(encoding='utf-8'))

    def test_nine_cycle_incidence(self):
        self.assertEqual(secant_incidence(9),{'double_curve_types':9,'triple_point_types':9,'isolated_node_types':18})

    def test_distance_two_intersections_not_isolated_nodes(self):
        r=secant_local_lengths(9,306)
        self.assertEqual(r['triple_points'],216)
        self.assertEqual(r['isolated_nodes'],432)
        self.assertNotEqual(r['isolated_nodes'],648)

    def test_exact_local_models(self):
        self.assertTrue(all(secant_local_checks().values()))

    def test_wrong_differential_rejected(self):
        models=copy.deepcopy(secant_local_models());models[1][0][0]=secant_variables()[0]
        with patch('check_hodge_secant_local_ext_gate.local_models',return_value=models):
            with self.assertRaisesRegex(ValueError,'local complex differential'):
                secant_local_checks()

    def test_normalizing_every_node_still_has_H1(self):
        r=secant_local_lengths(9,432)
        self.assertEqual((r['H1_length'],r['dual_sheaf_Ext3_length'],r['local_self_Ext2_length']),(432,0,864))

    def test_no_normalization_ideal_sheaf_control(self):
        r=secant_local_lengths(9,0)
        self.assertEqual((r['H1_length'],r['dual_sheaf_Ext3_length'],r['local_self_Ext2_length']),(0,432,1728))

    def test_partial_normalization_local_lengths(self):
        r=secant_local_lengths(9,306)
        self.assertEqual((r['remaining_nodes'],r['H1_length'],r['local_self_Ext2_length']),(126,306,1116))

    def test_cannot_normalize_more_than_isolated_nodes(self):
        with self.assertRaisesRegex(ValueError,'exceeds isolated nodes'):
            secant_local_lengths(9,433)

    def test_exact_count_types(self):
        for n in (True,5,9.0):
            with self.subTest(n=n),self.assertRaisesRegex(ValueError,'cycle length'):
                secant_incidence(n)
        with self.assertRaisesRegex(ValueError,'count types'):
            secant_local_lengths(9,True)

    def test_missing_variable_not_maximal_ideal(self):
        self.assertFalse(secant_generates_maximal(secant_variables()[:3]))

    def test_monomial_minimality_accepts_single_use_generator(self):
        self.assertEqual(secant_minimal(iter([(1,0,0,0),(2,0,0,0)])),[(1,0,0,0)])

    def test_transversality_cannot_be_omitted(self):
        self.data['geometry']['all_intersections_through_four_translates_transverse']=False
        with self.assertRaisesRegex(ValueError,'local Ext hypotheses'):
            validate_secant_local(self.data)

    def test_all_local_to_global_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'local Ext promotion'):
                    validate_secant_local(d)

    def test_complex_cannot_silently_be_placed_in_one_degree(self):
        self.data['geometry']['complex_degrees']=[0]
        with self.assertRaisesRegex(ValueError,'local Ext hypotheses'):
            validate_secant_local(self.data)


class HodgeSecantSourceSemiregularityTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(SOURCE_SEMI_CONTRACT.read_text(encoding='utf-8'))

    def test_hkr_rank_and_annihilator(self):
        r=source_semi_core()
        self.assertEqual((r['HKR_dimension'],r['character_action_rank'],r['character_annihilator_dimension']),(28,12,16))

    def test_all_compensated_bivectors_annihilate_character(self):
        for i in range(4):
            for j in range(i+1,4):
                self.assertEqual(annihilator_residual(9,i,j),{})

    def test_wrong_Bfield_coefficient_fails(self):
        self.assertTrue(annihilator_residual(9,0,1,8))

    def test_bivector_alone_does_not_annihilate(self):
        self.assertTrue(source_bivector(source_semi_character(),0,1))

    def test_local_first_plane_evaluation(self):
        self.assertEqual(local_at_square(0,1),[2,0])

    def test_local_second_plane_evaluation(self):
        self.assertEqual(local_at_square(2,3),[0,-2])

    def test_mixed_local_pairs_vanish(self):
        for i,j in ((0,2),(0,3),(1,2),(1,3)):
            self.assertEqual(local_at_square(i,j),[0,0])

    def test_Euler_is_not_sheaf_Ext_length(self):
        self.assertEqual(euler_pairing(),1296)
        self.assertNotEqual(euler_pairing(),1116)

    def test_Euler_polynomial_controls(self):
        for d in (3,5,9,13):
            self.assertEqual(euler_pairing(d),8*d*(d+9))

    def test_ordered_tangent_pair_required(self):
        with self.assertRaisesRegex(ValueError,'ordered local tangent'):
            local_at_square(1,0)

    def test_holomorphic_contractions_anticommute(self):
        p=source_wedge(source_theta(),source_theta())
        self.assertEqual(source_add(source_contract(source_contract(p,0),1),source_contract(source_contract(p,1),0)),{})

    def test_hkr_columns_have_full_domain_coverage(self):
        self.assertEqual(len(source_hkr_columns(source_semi_character())),6+16+6)

    def test_exact_rank_positive_control(self):
        self.assertEqual(source_hkr_rank([{1:Fraction(1)},{2:Fraction(1)},{1:Fraction(2)}]),2)

    def test_source_twist_frozen(self):
        self.data['hypotheses']['corrected_twist']=1
        with self.assertRaisesRegex(ValueError,'source semiregularity hypotheses'):
            validate_source_semi(self.data)

    def test_all_source_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'source semiregularity promotion'):
                    validate_source_semi(d)

    def test_nonzero_local_witness_cannot_be_dropped(self):
        models=copy.deepcopy(secant_local_models());models[0][0]=[{} for _ in range(4)]
        with patch('check_hodge_secant_source_semiregularity.local_models',return_value=models):
            with self.assertRaisesRegex(ValueError,'nonzero local Atiyah square'):
                source_semi_core()


class HodgeSecantCriterionPersistenceTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(persistence.CONTRACT.read_text(encoding='utf-8'))

    def test_four_independent_product_kernel_classes(self):
        r=persistence.exact_core()
        self.assertEqual(r['product_trace_kernel_lower_bound'],4)
        self.assertEqual(r['conditional_isogeny_descent_kernel_lower_bound'],4)

    def test_dual_character(self):
        self.assertEqual(persistence.exact_core()['dual_character_coefficients'],['1','-3','-9/2','9/2','27/8'])

    def test_dual_local_evaluations(self):
        for i in range(4):
            for j in range(i+1,4):
                self.assertEqual(persistence.dual_at_square(i,j),local_at_square(i,j))

    def test_zero_partner_not_admitted(self):
        with self.assertRaisesRegex(ValueError,'nonzero partner'):
            persistence.propagate_bound('external_product',2)

    def test_nonzero_external_partner(self):
        self.assertEqual(persistence.propagate_bound('external_product',2,other_nonzero=True),2)

    def test_equivalence_operations(self):
        for op in ('Fourier_Mukai_equivalence','line_twist','shift','derived_dual'):
            self.assertEqual(persistence.propagate_bound(op,4),4)

    def test_descent_requires_actual_object(self):
        with self.assertRaisesRegex(ValueError,'actual finite etale'):
            persistence.propagate_bound('isogeny_descent',4,finite_etale_isogeny=True)

    def test_descent_requires_etale_isogeny(self):
        with self.assertRaisesRegex(ValueError,'actual finite etale'):
            persistence.propagate_bound('isogeny_descent',4,actual_descent=True)

    def test_pushforward_requires_etale_isogeny(self):
        with self.assertRaisesRegex(ValueError,'finite etale abelian'):
            persistence.propagate_bound('isogeny_pushforward',4)

    def test_pushforward_with_hypotheses(self):
        self.assertEqual(persistence.propagate_bound('isogeny_pushforward',4,finite_etale_isogeny=True),4)

    def test_arbitrary_summand_not_admitted(self):
        for op in ('direct_summand','ramified_quotient','restricted_deformation'):
            with self.subTest(op=op),self.assertRaisesRegex(ValueError,'unsupported persistence'):
                persistence.propagate_bound(op,4)

    def test_eightfold_hkr_pullback_positive_control(self):
        diagonal=persistence.isogeny_hkr_diagonal(tuple(range(1,9)))
        self.assertEqual(len(diagonal),120)
        self.assertTrue(all(diagonal))

    def test_singular_differential_not_admitted(self):
        with self.assertRaisesRegex(ValueError,'invertible isogeny'):
            persistence.isogeny_hkr_diagonal((1,0,2,2))

    def test_descent_hypothesis_frozen(self):
        self.data['construction']['isogeny_descent_requires_actual_pullback_identification']=False
        with self.assertRaisesRegex(ValueError,'persistence construction'):
            persistence.validate_scope(self.data)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'persistence promotion'):
                    persistence.validate_scope(d)

    def test_product_Euler_control_not_Ext_dimension(self):
        self.assertEqual(persistence.exact_core()['product_Euler_pairing'],1296**2)


class HodgeRamifiedTrigonalFamilyTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(ramified_family.CONTRACT.read_text(encoding='utf-8'))

    def test_squarefree_degree_twelve_discriminant(self):
        b=[-2,3,0,0,0,0,1];d=ramified_family.add([4],ramified_family.mul(b,b),-1)
        self.assertEqual(len(d)-1,12)
        self.assertEqual(ramified_family.gcd(d,ramified_family.derivative(d)),[1])

    def test_irreducible_over_complex_function_field_certificate(self):
        self.assertTrue(ramified_family.cubic_irreducibility_control())

    def test_marked_branch_points_unramified_for_trigonal_map(self):
        for x,y in self.data['construction']['unramified_marked_points']:
            self.assertEqual(y**3-3*y+x**6+3*x-2,0)
            self.assertEqual(3*(y*y-1),9)

    def test_double_cover_line_divisor_identity(self):
        dn=(-1,0,1,1);f=(2,1,-2,-1)
        self.assertEqual(tuple(2*a+b for a,b in zip(dn,f)),(0,1,0,1))

    def test_two_actual_auxiliary_tower_genera(self):
        r=ramified_family.exact_core()
        self.assertEqual(r['ramified_tower_genera'],[16,8,4])
        self.assertEqual(r['etale_tetragonal_tower_genera'],[17,9,5])

    def test_naive_fourth_root_has_wrong_genus(self):
        self.assertEqual(ramified_family.exact_core()['naive_quartic_base_change_genus'],18)

    def test_square_root_torsor_size_not_cover_count(self):
        self.assertEqual(ramified_family.exact_core()['line_bundle_square_root_torsor_size'],2**8)
        self.assertFalse(self.data['scope_policy']['fully_coordinatized_quartic_cover'])

    def test_four_state_order_four_action(self):
        T=lambda s:(s[1],1-s[0]);s=(0,0);orbit=[]
        for _ in range(4):orbit.append(s);s=T(s)
        self.assertEqual(len(set(orbit)),4);self.assertEqual(s,(0,0))

    def test_balanced_eightfold_character_multiplicities(self):
        r=ramified_family.exact_core()
        self.assertEqual(r['holomorphic_K_multiplicities'],[4,4])
        self.assertEqual(r['primitive_H1_K_rank'],8)

    def assert_missing_transfer_hypothesis(self,k):
        flags=dict(preserves_trigonal_pencil=True,square_is_deck=True,branch_disjoint=True,branch_distinct_fibres=True)
        flags[k]=False
        with self.assertRaisesRegex(ValueError,'explicit equivariant'):
            ramified_family.transfer_allowed(**flags)

    def test_extra_action_requires_pencil_preservation(self):
        self.assert_missing_transfer_hypothesis('preserves_trigonal_pencil')

    def test_extra_action_square_must_be_deck(self):
        self.assert_missing_transfer_hypothesis('square_is_deck')

    def test_trigonal_ramification_must_avoid_branch(self):
        self.assert_missing_transfer_hypothesis('branch_disjoint')

    def test_general_case_requires_different_fibres(self):
        self.assert_missing_transfer_hypothesis('branch_distinct_fibres')

    def test_all_target_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'family promoted to target'):
                    ramified_family.validate_family(d)

    def test_marked_geometry_frozen(self):
        self.data['construction']['unramified_marked_points'][0]=[0,-1]
        with self.assertRaisesRegex(ValueError,'family geometry changed'):
            ramified_family.validate_family(self.data)

    def test_primary_source_hash_drift_rejected(self):
        data=json.loads(ramified_family.SOURCES.read_text(encoding='utf-8'))
        data['files'][0]['sha256']='0'*64
        with patch('check_hodge_ramified_trigonal_family.json.loads',return_value=data):
            with self.assertRaisesRegex(ValueError,'primary source drift'):
                ramified_family.validate_sources()


class HodgeTrigonalPrincipalMatchTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(principal_match.CONTRACT.read_text(encoding='utf-8'))

    def test_birational_rational_elliptic_genus_bound(self):
        self.assertEqual(principal_match.cs_bound(4,0,4,1),13)

    def test_quadratic_image_genus_bound(self):
        self.assertEqual(principal_match.cs_bound(2,0,2,1),3)

    def test_all_joint_degrees_exhausted(self):
        self.assertEqual(principal_match.quartic_joint_case(1),'excluded_genus_bound_13')
        self.assertEqual(principal_match.quartic_joint_case(2),'quadratic_quotient_genus_at_most_3')
        self.assertEqual(principal_match.quartic_joint_case(4),'excluded_degree_one_maps_to_P1_and_elliptic')

    def test_bad_common_degree_rejected(self):
        with self.assertRaisesRegex(ValueError,'common field degree'):
            principal_match.quartic_joint_case(3)

    def test_higher_elliptic_degree_is_not_excluded_by_same_bound(self):
        self.assertEqual(principal_match.cs_bound(4,0,6,1),21)
        with self.assertRaisesRegex(ValueError,'only degree-four'):
            principal_match.quartic_joint_case(1,elliptic_degree=6)

    def test_double_quotient_uniqueness_strict(self):
        self.assertTrue(principal_match.unique_double_quotient(17,3))
        self.assertFalse(principal_match.unique_double_quotient(13,3))
        self.assertFalse(principal_match.unique_double_quotient(17,4))

    def test_forced_genus_three(self):
        cases=principal_match.low_genus_cases()
        good=[c for c in cases if c['cyclic_monodromy_sum_zero'] and c['anti_involution_dimension_positive']]
        self.assertEqual([(c['v'],c['u'],c['q']) for c in good],[(3,1,1)])

    def test_genus_one_has_no_anti_elliptic_part(self):
        c=principal_match.low_genus_cases()[0]
        self.assertFalse(c['anti_involution_dimension_positive'])

    def test_genus_two_fails_cyclic_monodromy(self):
        c=principal_match.low_genus_cases()[1]
        self.assertEqual(c['index_two_branch_count'],1)
        self.assertFalse(c['cyclic_monodromy_sum_zero'])

    def test_Klein_four_genus_relation(self):
        r=principal_match.exact_core();g=r['forced_quotient_genera']
        self.assertEqual(17+2*g['U'],g['V']+9+g['W'])

    def test_forced_factor_dimensions(self):
        self.assertEqual(principal_match.exact_core()['forced_Prym_factor_dimensions'],[2,6])

    def test_forced_sixfold_cover_is_ramified(self):
        r=principal_match.exact_core()
        self.assertEqual(r['forced_W_double_branch_count'],12)
        self.assertEqual(r['forced_W_quartic_inertia_two_branch_count'],6)

    def test_all_two_primary_raw_types_have_odd_inert_valuation(self):
        for a in range(7):
            self.assertEqual(principal_match.sixfold.valuation3(Fraction(3,2**a)),1)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'principal obstruction promoted'):
                    principal_match.validate_contract(d)

    def test_principal_and_free_hypotheses_required(self):
        flags=dict(principal_comparison=True,top_pencil_degree=4,elliptic_map_degree=4,free_C4=True)
        for key,value in [('principal_comparison',False),('free_C4',False),('elliptic_map_degree',6)]:
            d=dict(flags);d[key]=value
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'exact principal comparison'):
                principal_match.matching_gate(**d)

    def test_fixed_elliptic_degree_not_replaced_by_isogeny_degree(self):
        self.data['geometry']['conditional_top_to_elliptic_degree']=6
        with self.assertRaisesRegex(ValueError,'principal comparison hypotheses'):
            principal_match.validate_contract(self.data)


class HodgeCyclicPrymOddAxisTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(odd_axis.CONTRACT.read_text(encoding='utf-8'))

    def test_joint_lattice_columns_are_integral_with_disjoint_units(self):
        r=odd_axis.exact_core();a,b=r['actual_surface_native_Gaussian_columns']
        self.assertEqual(a[0],['1','0']);self.assertEqual(b[7],['1','0'])
        self.assertEqual(b[5],['1','-1'])

    def test_physical_positive_CM_degrees_not_native_indefinite_form(self):
        self.assertEqual(self.data['geometry']['native_Gaussian_surface_Hermitian_diagonal'],[2,-3])
        self.assertEqual(odd_axis.exact_core()['physical_CM_product_polarization_degrees'],[2,3])

    def test_all_surface_unitaries_preserve_axes(self):
        u=odd_axis.unitary_restriction_controls((2,3));self.assertEqual(len(u),16)
        self.assertTrue(all(a[1]==(0,0) and b[0]==(0,0) for a,b in u))

    def test_square_minus_identity_restrictions(self):
        u=[m for m in odd_axis.unitary_restriction_controls((2,3)) if odd_axis.matrix_square_is_minus_identity(m)]
        self.assertEqual(len(u),4)

    def test_equal_weights_allow_axis_exchange(self):
        u=odd_axis.unitary_restriction_controls((2,2));self.assertEqual(len(u),32)
        self.assertTrue(any(a[1]!=(0,0) for a,b in u))

    def test_nonpositive_CM_weights_rejected(self):
        with self.assertRaisesRegex(ValueError,'positive integral CM'):
            odd_axis.unitary_restriction_controls((2,-3))

    def test_degree_six_not_divisible_by_free_orbit_length(self):
        self.assertFalse(odd_axis.invariant_fibre_divisibility(6))

    def test_degree_four_and_eight_not_excluded_by_same_parity(self):
        self.assertTrue(odd_axis.invariant_fibre_divisibility(4))
        self.assertTrue(odd_axis.invariant_fibre_divisibility(8))

    def test_ramified_action_not_admitted(self):
        with self.assertRaisesRegex(ValueError,'free C4'):
            odd_axis.invariant_fibre_divisibility(6,free_action=False)

    def test_axis_invariance_required(self):
        with self.assertRaisesRegex(ValueError,'invariant axis'):
            odd_axis.invariant_fibre_divisibility(6,axis_preserved=False)

    def test_order_four_linear_part_required(self):
        with self.assertRaisesRegex(ValueError,'order-four linear part'):
            odd_axis.invariant_fibre_divisibility(6,linear_part_square_minus_one=False)

    def test_conditional_source_theta_degree_parity(self):
        for d in range(1,25):
            self.assertEqual(odd_axis.invariant_fibre_divisibility(2*d),d%2==0)

    def test_conditional_auxiliary_lower_bound_does_not_construct_axes(self):
        self.assertEqual(odd_axis.exact_core()['conditional_auxiliary_K_isogeny_source_minimum_axis_theta_degree'],4)
        self.assertFalse(self.data['scope_policy']['actual_isogeny_source_axes_constructed'])

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'odd-axis exclusion promoted'):
                    odd_axis.validate_contract(d)

    def test_actual_axis_degree_frozen(self):
        self.data['geometry']['odd_axis_degree']=4
        with self.assertRaisesRegex(ValueError,'odd-axis comparison hypotheses'):
            odd_axis.validate_contract(self.data)

    def test_square_minus_identity_without_polarization_does_not_force_axes(self):
        rotation=(((0,0),(-1,0)),((1,0),(0,0)))
        self.assertTrue(odd_axis.matrix_square_is_minus_identity(rotation))
        self.assertNotIn(rotation,odd_axis.unitary_restriction_controls((2,3)))


class HodgeTwoBranchOddAxisTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(two_branch.CONTRACT.read_text(encoding='utf-8'))

    def test_generator_fixed_point_case(self):
        c=two_branch.branch_orbit_cases()[0]
        self.assertEqual((c['F'],c['T'],c['quotient_genus']),(2,0,'4'))
        self.assertTrue(c['integral_quotient_genus'])

    def test_swapped_branch_orbit_impossible_genus(self):
        c=two_branch.branch_orbit_cases()[1]
        self.assertEqual(c['quotient_genus'],'9/2')
        self.assertFalse(c['integral_quotient_genus'])

    def test_nonpaired_full_branch_characters_rejected(self):
        with self.assertRaisesRegex(ValueError,'primitive opposite tangent'):
            two_branch.residue_profiles(6,source_characters=(1,1))

    def test_degree_six_target_character_i_impossible(self):
        self.assertEqual(two_branch.residue_profiles(6,1),[])

    def test_degree_six_target_character_minus_i_impossible(self):
        self.assertEqual(two_branch.residue_profiles(6,3),[])

    def test_inverse_generator_same_exclusion(self):
        self.assertEqual(two_branch.residue_profiles(6,1,(3,1)),[])

    def test_omitting_tangent_characters_gives_spurious_profile(self):
        profiles=two_branch.residue_profiles(6,enforce_characters=False)
        self.assertTrue(any(p['ramification_indices']==[2,2] for p in profiles))

    def test_degree_four_local_control_not_actual_map(self):
        self.assertTrue(two_branch.residue_profiles(4))
        self.assertFalse(self.data['scope_policy']['degree_four_equivariant_curve_map_constructed'])

    def test_both_source_fixed_points_share_one_fixed_target(self):
        profiles=two_branch.residue_profiles(8)
        self.assertTrue(profiles)
        self.assertTrue(all(p['fixed_target_assignments'][0]==p['fixed_target_assignments'][1] for p in profiles))

    def test_primitive_tangent_congruences_in_positive_control(self):
        for p in two_branch.residue_profiles(12,3):
            ep,eq=p['ramification_indices']
            self.assertEqual(ep%4,3);self.assertEqual((3*eq)%4,3)

    def test_nonprimitive_target_tangent_rejected(self):
        with self.assertRaisesRegex(ValueError,'primitive opposite tangent'):
            two_branch.residue_profiles(6,2)

    def test_fresh_rendered_Mumford_normalization_source(self):
        two_branch.validate_sources()
        d=json.loads(two_branch.SOURCES.read_text(encoding='utf-8'))
        self.assertEqual((d['pdf_page'],d['printed_page']),(9,333))

    def test_principal_half_normalization_not_omitted(self):
        self.data['geometry']['principal_Prym_half_of_Jacobian_restriction']=False
        with self.assertRaisesRegex(ValueError,'two-branch comparison changed'):
            two_branch.validate_contract(self.data)

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'two-branch exclusion promoted'):
                    two_branch.validate_contract(d)

    def test_small_degree_residue_controls_not_curve_census(self):
        for degree in range(1,25):
            self.assertEqual(bool(two_branch.residue_profiles(degree)),degree%4==0)

    def test_new_primary_page_hash_drift_rejected(self):
        with patch('check_hodge_two_branch_odd_axis_obstruction.sha256') as h:
            h.return_value.hexdigest.return_value='0'*64
            with self.assertRaisesRegex(ValueError,'two-branch primary drift'):
                two_branch.validate_sources()


class HodgeEvenAxisPrincipalModelTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(even_axis.CONTRACT.read_text(encoding='utf-8'))

    def test_step_Gaussian_determinant_is_positive_real(self):
        self.assertEqual(even_axis.old.gdet(even_axis.gaussian_matrix()),(16,0))

    def test_composite_retains_quarter_turn(self):
        self.assertEqual(even_axis.exact_core()['Gaussian_composite_determinant'],[0,768])

    def test_principal_polarization_multiplier(self):
        form={(2*k,2*k+1):Fraction(d) for k,d in enumerate(even_axis.old.DY)}
        self.assertEqual(even_axis.q_pull(form),even_axis.old.scale(form,2))

    def test_axis_kernel_and_degree_data(self):
        r=even_axis.exact_core()
        self.assertEqual(r['elliptic_axis_step_kernel_orders'],[1,1])
        self.assertEqual(r['physical_elliptic_surface_polarization_degrees'],[4,6])

    def test_all_elliptic_degree_bound_and_parity(self):
        r=even_axis.exact_core()
        self.assertEqual(r['elliptic_theta_degree_lower_bound'],4)
        self.assertTrue(r['all_elliptic_theta_degrees_even'])
        self.assertFalse(self.data['scope_policy']['all_elliptic_curves_enumerated'])

    def test_bad_pairing_would_create_degree_one_axis(self):
        m=even_axis.gaussian_matrix(((0,6),(1,2),(3,4),(5,7)))
        bp=[even_axis.old.gaussian_matrix()[i][6] for i in range(8)]
        column=[tuple(sum(even_axis.old.cmul(m[i][k],bp[k])[j] for k in range(8)) for j in (0,1)) for i in range(8)]
        self.assertEqual(even_axis.axis_kernel_order(column),4)

    def test_opposite_sign_pairing_not_admitted(self):
        with self.assertRaisesRegex(ValueError,'same-sign pair partition'):
            even_axis.gaussian_matrix(((0,3),(1,2),(4,6),(5,7)))

    def test_marking_not_invented_old_endomorphism(self):
        self.assertFalse(self.data['scope_policy']['marking_matrix_is_endomorphism_of_Y2'])

    def test_local_exterior_inverse_coverage(self):
        self.assertEqual(even_axis.exact_core()['factorized_inverse_local_exterior_columns'],64)
        self.assertEqual(even_axis.exact_core()['explicit_global_H8_sample_columns'],4)

    def test_original_alpha_phase(self):
        r6,_=even_axis.old.generators(6);_,i8=even_axis.old.generators(8)
        self.assertEqual(even_axis.forward(r6),i8)

    def test_second_Weil_generator_phase(self):
        _,i6=even_axis.old.generators(6);r8,_=even_axis.old.generators(8)
        self.assertEqual(even_axis.forward(i6),even_axis.old.scale(r8,-1))

    def test_normalized_cohomological_roundtrip(self):
        r6,_=even_axis.old.generators(6)
        self.assertEqual(even_axis.reverse(even_axis.forward(r6)),r6)
        self.assertFalse(self.data['scope_policy']['Chow_retraction_claimed'])

    def test_divisor_cube_not_exceptional_cycle(self):
        e={(2*k,2*k+1):Fraction(d) for k,d in enumerate(even_axis.old.DS8[:6])}
        cube=even_axis.old.wedge(even_axis.old.wedge(e,e),e)
        self.assertFalse(any(even_axis.channels(even_axis.forward(cube))))

    def test_all_scope_promotions_rejected(self):
        for k in self.data['scope_policy']:
            with self.subTest(key=k):
                d=copy.deepcopy(self.data);d['scope_policy'][k]=True
                with self.assertRaisesRegex(ValueError,'Y3 promoted'):
                    even_axis.validate_contract(d)

    def test_new_denominator_not_old_48(self):
        self.data['transfer']['normalized_transfer_denominator']=48
        with self.assertRaisesRegex(ValueError,'Y3 geometry or transfer'):
            even_axis.validate_contract(self.data)

    def test_even_degrees_pass_local_filters_not_membership(self):
        self.assertTrue(odd_axis.invariant_fibre_divisibility(8))
        self.assertTrue(two_branch.residue_profiles(12))
        self.assertFalse(self.data['scope_policy']['Prym_membership_constructed'])


class HodgeCoupledKummerGateTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(coupled_kummer.CONTRACT.read_text(encoding='utf-8'))

    def test_elliptic_quotient_polynomial_identity(self):
        m=coupled_kummer.multiply_polynomials
        self.assertEqual(m({3:1,1:-1},{3:1,1:-1}),m({2:1},m({2:1,0:-1},{2:1,0:-1})))

    def test_elliptic_quotient_inertia_and_RH(self):
        self.assertEqual(coupled_kummer.exact_core()['elliptic_cyclic_quotient_inertia_orders'],[4,2,4])
        self.assertEqual(3+2+3,8)

    def test_product_not_ratio_descends(self):
        self.assertEqual((1+3)%4,0)
        self.assertNotEqual((1-3)%4,0)
        self.assertEqual(self.data['geometry']['coupled_equation'],'H(f8)*H(f12)=r^4')

    def test_degree_eight_profiles(self):
        ps=coupled_kummer.local_patterns(8)
        self.assertEqual(len(ps),20)
        self.assertTrue(all(p['RH_feasible'] for p in ps))

    def test_degree_twelve_profiles(self):
        ps=coupled_kummer.local_patterns(12)
        self.assertEqual(len(ps),99)
        self.assertEqual(sum(p['RH_feasible'] for p in ps),98)

    def test_triple_total_ramification_degree_twelve_is_impossible(self):
        p=coupled_kummer.fibre_pattern(12,(12,),(12,),(12,))
        self.assertFalse(p['RH_feasible'])
        self.assertEqual(p['remaining_ramification'],-1)

    def test_all_admitted_patterns_have_elliptic_RH_32(self):
        for n in (8,12):
            for p in coupled_kummer.local_patterns(n):
                if p['RH_feasible']:
                    self.assertEqual(p['elliptic_map_ramification_over_special_values']+p['elliptic_map_ramification_elsewhere'],32)

    def test_paired_profiles_are_not_covers(self):
        self.assertEqual(coupled_kummer.exact_core()['paired_local_profile_controls'],1960)
        self.assertFalse(self.data['scope_policy']['local_profiles_counted_as_actual_covers'])

    def test_exact_order_separates_split_quadratic_and_quartic(self):
        order=coupled_kummer.marked_torsion_order
        self.assertEqual([order((x,)+(0,)*9) for x in range(4)],[1,4,2,4])

    def test_no_unmarked_torsion_calculation_inferred(self):
        with self.assertRaisesRegex(ValueError,'marked genus-five'):
            coupled_kummer.marked_torsion_order((1,0))
        self.assertFalse(self.data['scope_policy']['actual_Picard_torsion_calculated'])

    def test_reconstruction_needs_exact_order_four(self):
        with self.assertRaisesRegex(ValueError,'exact order4'):
            coupled_kummer.require_reconstruction_hypotheses(smooth_connected_base=True,local_divisibility=True,
                exact_order_four=False,coupled_product_identity=True)

    def test_reconstruction_needs_global_product(self):
        with self.assertRaisesRegex(ValueError,'coupled product'):
            coupled_kummer.require_reconstruction_hypotheses(smooth_connected_base=True,local_divisibility=True,
                exact_order_four=True,coupled_product_identity=False)

    def test_reconstruction_needs_local_etaleness(self):
        with self.assertRaisesRegex(ValueError,'local divisibility'):
            coupled_kummer.require_reconstruction_hypotheses(smooth_connected_base=True,local_divisibility=False,
                exact_order_four=True,coupled_product_identity=True)

    def test_wrong_function_degrees_rejected(self):
        self.data['geometry']['base_function_degrees']=[4,6]
        with self.assertRaisesRegex(ValueError,'hypotheses changed'):
            coupled_kummer.validate_contract(self.data)

    def test_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d=copy.deepcopy(self.data);d['scope_policy'][key]=True
                with self.assertRaisesRegex(ValueError,'promoted to target'):
                    coupled_kummer.validate_contract(d)

    def test_joint_kernel_and_period_matching_not_erased(self):
        self.data['target_matching_requirements']=[]
        with self.assertRaisesRegex(ValueError,'hypotheses changed'):
            coupled_kummer.validate_contract(self.data)


class HodgeJointDegreeGateTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(joint_degree.CONTRACT.read_text(encoding='utf-8'))

    def test_all_joint_degree_divisors(self):
        self.assertEqual(joint_degree.common_degrees(),[1,2,4])

    def test_small_Prym_degree_four_cannot_match_Euler24(self):
        values=[joint_degree.small_prym_isogeny_degree(4,e) for e in (1,2,4)]
        self.assertEqual(values,[Fraction(1,6),Fraction(1,3),Fraction(2,3)])
        self.assertTrue(all(v.denominator>1 for v in values))

    def test_small_Prym_degree_two_cannot_match_Euler24(self):
        self.assertEqual([joint_degree.small_prym_isogeny_degree(2,e) for e in (1,2,4)],
            [Fraction(1,24),Fraction(1,12),Fraction(1,6)])

    def test_obstruction_needs_the_actual_target_Euler_characteristic(self):
        self.assertEqual(joint_degree.small_prym_isogeny_degree(4,1,4),1)
        self.assertFalse(self.data['scope_policy']['all_coupled_Kummer_covers_with_joint_degree4_excluded'])

    def test_obstruction_needs_two_primary_source(self):
        self.assertEqual(joint_degree.small_prym_isogeny_degree(4,6),1)

    def test_degree_four_RH_only_small_anti_Prym(self):
        cases=joint_degree.rh_anti_cases(4)
        self.assertEqual([r['gV'] for r in cases],[2,3,4,5])
        self.assertTrue(all(r['anti_dimension']==2 for r in cases))

    def test_degree_two_large_anti_Prym_alternatives(self):
        cases=[r for r in joint_degree.rh_anti_cases(2) if r['anti_dimension']==8]
        self.assertEqual([(r['gV'],r['gW'],r['branch_points_V_to_W'],r['ramification_C_to_V']) for r in cases],
            [(8,0,18,4),(9,1,16,0)])

    def test_Y3_Jacobian_bound_uses_degree_four_not_two(self):
        self.assertEqual(joint_degree.toreli.hyperelliptic_elliptic_genus_bound(4),7)
        self.assertLess(7,8)
        self.assertEqual(self.data['geometry']['Y3_hypothetical_Jacobian_elliptic_degree'],4)

    def test_sixteen_branch_source_is_not_principal_half(self):
        typ=joint_degree.exact_core()['degree2_ramified_Prym_induced_theta_type']
        self.assertEqual(typ,[1]*7+[2])
        self.assertEqual(sum(x==2 for x in typ),1)

    def test_ramified_source_polarized_isogeny_degree_two(self):
        self.assertEqual(joint_degree.exact_core()['degree2_ramified_Prym_isogeny_to_Y3_degree'],2)

    def test_third_involution_bielliptic_character_table(self):
        dims=joint_degree.v4_character_dimensions()
        self.assertEqual(list(dims.values()),[1,8,8,0])
        self.assertEqual(dims['h+sigma+']+dims['h-sigma-'],1)

    def test_bielliptic_branch_counts(self):
        self.assertEqual([2*g-2 for g in (17,5,9)],[32,8,16])

    def test_adjunction_defects_not_distinct_node_counts(self):
        self.assertEqual([joint_degree.image_arithmetic_genus(d) for d in (1,2)],[97,25])
        self.assertEqual(joint_degree.exact_core()['normalization_defect_sums_for_joint_degrees_1_2'],[80,16])
        self.assertFalse(self.data['scope_policy']['normalization_defects_counted_as_distinct_nodes'])

    def test_genus_five_base_can_cover_elliptic_image(self):
        self.assertEqual(joint_degree.exact_core()['quotient_surface_image_normalization_genera_for_joint_degrees_1_2'],[5,1])
        self.assertFalse(self.data['scope_policy']['all_scalar_sources_excluded_for_Y3'])

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d=copy.deepcopy(self.data);d['scope_policy'][key]=True
                with self.assertRaisesRegex(ValueError,'beyond fixed target'):
                    joint_degree.validate_contract(d)

    def test_principal_normalization_not_silently_substituted(self):
        self.data['geometry']['degree2_ramified_Prym_induced_theta_type']=[1]*8
        with self.assertRaisesRegex(ValueError,'geometry changed'):
            joint_degree.validate_contract(self.data)


class HodgeMinimalAxisScalarSourceTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(minimal_source.CONTRACT.read_text(encoding='utf-8'))

    def test_exact_special_fibre_polynomials(self):
        self.assertEqual(minimal_source.smoothness_certificate(),{
            '0':[-16,2,13,1,-4],'1':[-36,50,-7,-7,-1],'-1':[-4,-14,-7,25,-9]})

    def test_all_special_fibres_squarefree(self):
        for c in (0,1,-1):
            f=minimal_source.fibre_polynomial(c)
            self.assertEqual(minimal_source.gcd(f,minimal_source.derivative(f)),{0:1})

    def test_poles_genuine_and_simple(self):
        self.assertEqual(minimal_source.gcd(minimal_source.D,minimal_source.P),{0:1})
        self.assertEqual(minimal_source.gcd(minimal_source.D,minimal_source.fibre_polynomial(0)),{0:1})
        self.assertEqual(minimal_source.exact_core()['g_special_fibre_support_sizes'],[4,4,4,4])

    def test_anti_translation_numerator_and_denominator(self):
        transform=lambda a:{2-i:v*2**i for i,v in a.items()}
        self.assertEqual(transform(minimal_source.D),minimal_source.scaled(minimal_source.D,2))
        self.assertEqual(transform(minimal_source.N),minimal_source.scaled(minimal_source.N,-2))

    def test_explicit_degree_two_isogeny_certificate(self):
        self.assertEqual(minimal_source.exact_core()['g_degree'],4)
        self.assertEqual(self.data['geometry']['T_to_W'],'x=(t+2)^2/(4*t), y=v*(t^2-4)/(8*t^2)')

    def test_order_four_point_not_order_two(self):
        self.assertEqual((-2)**3+4*(-2),-16)
        self.assertEqual(self.data['geometry']['order_four_translation_on_T'],[-2,'4i'])
        self.assertNotEqual(-2,0)

    def test_ramified_V_genus_nine(self):
        r=minimal_source.exact_core()
        self.assertEqual((r['V_to_W_branch_points'],r['V_genus']),(16,9))

    def test_top_C_genus_seventeen(self):
        r=minimal_source.exact_core()
        self.assertEqual((r['C_to_T_branch_points'],r['C_genus']),(32,17))

    def test_free_scalar_tower_genera(self):
        r=minimal_source.exact_core()
        self.assertEqual([r[k] for k in ('C_genus','D_genus','B_genus')],[17,9,5])

    def test_nonprimitive_axis_would_violate_genus(self):
        self.assertEqual(minimal_source.exact_core()['hypothetical_nonprimitive_genus_bounds'],[9,5,3])
        self.assertTrue(all(b<17 for b in (9,5,3)))

    def test_primitive_elliptic_axis_theta_four(self):
        r=minimal_source.exact_core()
        self.assertEqual(r['primitive_curve_to_CM_elliptic_degree'],8)
        self.assertEqual(r['source_principal_Prym_elliptic_theta_degree'],4)

    def test_ramified_polarization_not_principal_half(self):
        self.assertEqual(minimal_source.exact_core()['ramified_auxiliary_induced_theta_type'],[1]*7+[2])

    def test_degree_two_isogeny_is_to_source_not_Y3(self):
        self.assertEqual(minimal_source.exact_core()['ramified_auxiliary_to_source_Prym_isogeny_degree'],2)
        self.assertFalse(self.data['scope_policy']['source_Prym_isogeny_to_Y3_constructed'])

    def test_second_axis_and_End_remain_unproved(self):
        for key in ('opposite_character_theta6_axis_constructed','degree2_joint_map_to_two_CM_elliptics_realized',
                    'source_Prym_End_computed','complementary_sevenfold_simple_proved'):
            self.assertFalse(self.data['scope_policy'][key])

    def test_all_scope_promotions_rejected(self):
        for key in self.data['scope_policy']:
            with self.subTest(key=key):
                d=copy.deepcopy(self.data);d['scope_policy'][key]=True
                with self.assertRaisesRegex(ValueError,'promoted to target'):
                    minimal_source.validate_contract(d)

    def test_untested_parameters_not_admitted_as_this_control(self):
        self.data['geometry']['parameters_lambda_a_b']=[2,3,2]
        with self.assertRaisesRegex(ValueError,'geometry changed'):
            minimal_source.validate_contract(self.data)


class HodgeScalar37CensusTests(unittest.TestCase):
    def setUp(self):
        self.data=load(census37.COUNTS);self.c=json.loads(census37.CONTRACT.read_text(encoding='utf-8'))
    def rows(self,a):return [r for r in self.data['rows'] if r['a']==a]
    def case(self,a):return census37.annotate(self.rows(a),a)
    def cases(self):return [self.case(a) for a in census37.REGULAR]
    def old221(self):return load(inert.OUT.relative_to(ROOT).as_posix())['CRT_partition']

    def test_all37_model_residues_partitioned(self):
        self.assertEqual([a for a in range(37) if joint_screen.good_model(a,37)],census37.REGULAR)
        self.assertEqual([a for a in range(37) if not joint_screen.good_model(a,37)],[3,11,17])

    def test_170_ordinary136_twisted_rows(self):
        self.assertEqual(len(self.data['rows']),170)
        self.assertEqual(sum('rho_Frobenius_fixed_V' in r for r in self.data['rows']),136)

    def test_a_dependent_poles_not_copied(self):
        for a in census37.REGULAR:
            r=self.rows(a);self.assertEqual(r[0]['rational_poles'],joint_screen.prime_poles(a,37))
            self.assertEqual(r[1]['rational_poles'],4)

    def test_independent_counts_every_case(self):
        d=census37.independent_counts()
        for a in census37.REGULAR:
            r=self.rows(a);self.assertEqual(d[a],[r[0]['V'],r[1]['V'],r[0]['rho_Frobenius_fixed_V']])

    def test_actual_a214_polynomial(self):
        self.assertEqual(self.case(29)['Frobenius_characteristic_coefficients_descending'],[1,4,56,62,-118,-6844,-87879,-285100,-3251523,-9369436,-5977054,116197982,3883261592,10262905636,94931877133])

    def test_every_unused_fifth_trace(self):
        for a in census37.REGULAR:self.assertEqual(len(census37.reconstruct(self.rows(a),a)['rational_power_traces_through_degree5']),5)

    def test_bad_fifth_trace_rejected(self):
        self.rows(29)[4]['V']+=1
        with self.assertRaisesRegex(ValueError,'unused fifth trace'):self.case(29)

    def test_shared_orbit_histograms_cover_every_field(self):
        for r in self.data['rows']:
            self.assertEqual(r['Frobenius_x_orbit_counts_by_length'],third.orbit_counts(r['n']))
            self.assertEqual(sum(i*v for i,v in enumerate(r['Frobenius_x_orbit_counts_by_length'])),r['q'])

    def test_fast_twist_power_audit_coverage_enforced(self):
        self.rows(0)[0]['twist_power_crosscheck']=False
        with self.assertRaisesRegex(ValueError,'power audits'):self.case(0)

    def test_exact28_CM_absent_residues(self):
        rs=[r for r in self.cases() if r['screen_verdict']=='CM_absent']
        self.assertEqual([r['a'] for r in rs],census37.CM_ABSENT)
        for r in rs:
            self.assertEqual(r['residual_modular_witnesses'][-1]['remaining_orders'],[])
            self.assertEqual(sum(len(t['orders_excluded']) for t in r['residual_modular_witnesses']),55)

    def test_a21_same_type_only_is_not_CM_absence(self):
        r=self.case(21);self.assertEqual(r['geometric_reduction_Ei_multiplicity_in_complement'],1)
        self.assertEqual(r['opposite_type_certificate']['degree'],0);self.assertEqual(r['screen_verdict'],'opposite_type_absent')

    def test_a16_finite_threefold_CM_multiplicity_is_only_upper_bound(self):
        r=self.case(16);self.assertEqual(r['geometric_reduction_Ei_multiplicity_in_complement'],2)
        self.assertEqual(r['same_type_certificate']['degree'],1);self.assertEqual(r['opposite_type_certificate']['degree'],1)
        self.assertEqual(r['screen_verdict'],'necessary_screen_survives')

    def test_native_GCD_handles_nonunit_quadratic_cyclotomic_factor(self):
        b=census37.bar(census37.BETA);f=(census37.pol.ONE,b,census37.zm(b,b))
        r=census37.native_factors(f,b,[3]);self.assertEqual(r['degree'],2)
        self.assertEqual(r['factors'][0]['degree_over_K'],2)

    def test_unit_complement_projectors_at2_8_13(self):
        for a in (2,8,13):
            r=self.case(a);self.assertTrue(r['known_axis_complement_projector']['integral_at3'])
            self.assertEqual(r['screen_verdict'],'inert3_degree_parity')

    def test_known_first_axis_split_improves_bounds(self):
        r=self.case(8);self.assertFalse(r['inert3_projector']['integral_at3'])
        self.assertTrue(r['known_axis_complement_projector']['integral_at3'])
        self.assertEqual([self.case(a)['conditional_primitive_axis_v3_upper_bound'] for a in (0,16)],[1,1])

    def test_conditional_target_degree_valuation_is1_not_full_degree6(self):
        for a in (0,16):self.assertEqual(self.case(a)['conditional_target_axis_v3_values'],[1])
        self.assertFalse(self.c['scope_policy']['primitive_theta6_axis_constructed'])

    def test_known_axis_nonunit_degree_cannot_be_split_at3(self):
        with self.assertRaisesRegex(ValueError,'degree must be a3-unit'):census37.known_axis_split_certificate(3)
        self.assertTrue(census37.known_axis_split_certificate(4)['orthogonal_complement_self_dual_at3'])

    def test_target_End_norm_hypotheses_remain_essential(self):
        with self.assertRaisesRegex(ValueError,'fixed End field'):inert.norm_parity_certificate(end0='unknown')
        with self.assertRaisesRegex(ValueError,'norm class'):inert.norm_parity_certificate(det=-1)

    def test_previous_slow37_control_recovered(self):
        old=load(third.COUNTS)
        for r,o in zip(self.rows(30),old['rows']):
            for key in ('W','V','E','rational_poles'):
                self.assertEqual(r[key],o[key])

    def test_final_CRT8077_2_98(self):
        r=census37.crt_partition(self.old221(),self.cases())
        self.assertEqual(r['excluded_count'],8077);self.assertEqual(r['joint_survivors'],[3087,6623])
        self.assertEqual(r['uncertified_count'],98)

    def test_uncertified_model_not_automatic_global_exclusion(self):
        r=census37.crt_partition(self.old221(),self.cases())
        self.assertIn(3,r['uncertified_residues'])
        self.assertFalse(self.c['scope_policy']['uncertified_model_residues_excluded_without_other_rule'])

    def test_next_actual_source_passes_three_necessary_screens_only(self):
        r=census37.next_control();self.assertEqual(r['parameters_lambda_a_b'],[2,-1554,2])
        self.assertEqual(r['good_prime_residues'],[6,10,0]);self.assertEqual(r['primitive_elliptic_theta_degree'],4)
        self.assertTrue(r['opposite_complex_axis_not_constructed'])

    def test_every_scope_promotion_rejected(self):
        for key in self.c['scope_policy']:
            changed=copy.deepcopy(self.c);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'scope promotion'):census37.validate_contract(changed)

    def test_native_quadratic_wrong_type_has_no_factor(self):
        b=census37.bar(census37.BETA);f=(census37.pol.ONE,b,census37.zm(b,b))
        self.assertEqual(census37.native_factors(f,census37.BETA,[3])['degree'],0)

    def test_arithmetic_chart_cannot_drop_a_case(self):
        self.c['arithmetic']['regular_residues'].remove(16)
        with self.assertRaisesRegex(ValueError,'arithmetic changed'):census37.validate_contract(self.c)


class HodgeOffReflectionThirdPrimeTests(unittest.TestCase):
    def setUp(self):
        self.data=load(third.COUNTS);self.c=json.loads(third.CONTRACT.read_text(encoding='utf-8'))
    def result(self):return third.reconstruct(self.data)
    def cert(self):return third.cm_certificate(tuple(self.result()['Frobenius_characteristic_coefficients_descending']))

    def test_beta37_orientation(self):
        self.assertEqual(third.zm(third.BETA,third.bar(third.BETA)),(37,0))
        self.assertEqual((third.BETA[0]+6*third.BETA[1])%37,0);self.assertEqual(self.data['rows'][0]['E'],40)

    def test_full_degree14_polynomial(self):
        self.assertEqual(self.result()['Frobenius_characteristic_coefficients_descending'],[1,8,16,34,378,-7728,-65743,-345364,-2432491,-10579632,19146834,63721474,1109503312,20525811272,94931877133])

    def test_fifth_trace_is43552(self):self.assertEqual(self.result()['rational_power_traces_through_degree5'],[-8,32,-230,88,43552])

    def test_degree5_full_orbit_coverage(self):
        r=self.data['rows'][4];self.assertEqual(r['q'],69343957)
        self.assertEqual(r['Frobenius_x_orbit_counts_by_length'],[0,37,0,0,0,13868784])

    def test_degree4_subfield_orbits(self):self.assertEqual(third.orbit_counts(4),[0,37,666,0,468198,0])

    def test_all_four_poles_rational_in_all_degrees(self):
        self.assertEqual([r['rational_poles'] for r in self.data['rows']],[4]*5)

    def test_independent_small_and_direct_twisted_counts(self):
        ordinary,twisted=third.independent_counts()
        self.assertEqual(ordinary,[[r['W'],r['V'],r['E']] for r in self.data['rows'][:2]])
        self.assertEqual(twisted,[40,self.data['rows'][0]['rho_Frobenius_fixed_V']])

    def test_all55_CM_orders_excluded(self):
        w=self.cert()['residual_modular_witnesses'];self.assertEqual(w[-1]['remaining_orders'],[])
        self.assertEqual(sum(len(r['orders_excluded']) for r in w),55)

    def test_no_extra_geometric_CM(self):
        self.assertEqual(self.cert()['cyclotomic_factors'],[])
        self.assertEqual(self.cert()['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_two_positive_primes_still_do_not_lift(self):
        d=load(joint_screen.OUT.relative_to(ROOT).as_posix())
        for p,a in ((13,6),(17,10)):
            r=next(r for r in d['finite_field_cases'] if (r['p'],r['a'])==(p,a))
            self.assertEqual(r['opposite_type_reduction_multiplicity'],1)
        self.assertEqual(self.cert()['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_bad_unused_fifth_trace_rejected(self):
        self.data['rows'][4]['V']+=1
        with self.assertRaisesRegex(ValueError,'unused fifth trace'):self.result()

    def test_missing_orbit_weight_rejected(self):
        self.data['rows'][4]['Frobenius_x_orbit_counts_by_length'][5]-=1
        with self.assertRaisesRegex(ValueError,'Frobenius x-orbits'):self.result()

    def test_fifth_count_not_mislabelled_direct(self):
        self.data['rows'][4]['direct_ordinary_crosscheck']=True
        with self.assertRaisesRegex(ValueError,'direct/orbit crosscheck'):self.result()

    def test_generic_ranks_squeezed_to2(self):
        r=third.generic_rank_certificate(1);self.assertEqual(r['geometric_generic_a_line_Hom_rank'],2)
        self.assertEqual(r['geometric_generic_three_parameter_Hom_rank'],2)
        self.assertTrue(r['transcendental_a_on_lambda2_b2_line_excluded'])

    def test_larger_special_rank_does_not_prove_generic_extra_factor(self):
        with self.assertRaisesRegex(ValueError,'one special-fibre CM factor'):third.generic_rank_certificate(2)

    def test_generic_fixed_line_cannot_silently_change(self):
        self.c['generic_argument']['fixed_line']['b']=3
        with self.assertRaisesRegex(ValueError,'generic hypotheses changed'):third.validate_contract(self.c)

    def test_independent_triples_not_all_transcendental_tuples(self):
        r=third.generic_rank_certificate(1);self.assertTrue(r['algebraically_independent_parameter_triples_excluded'])
        self.assertFalse(self.c['scope_policy']['all_transcendental_scalar_tuples_excluded'])
        self.assertFalse(self.c['scope_policy']['single_global_CM_jump_equation_constructed'])

    def test_CRT7457_excluded36_unchecked684_other(self):
        d=load(inert.OUT.relative_to(ROOT).as_posix());r=third.refined_crt(d['CRT_partition'])
        self.assertEqual(r['excluded_count'],7457);self.assertEqual(len(r['two_prime_survivors_not_counted_at37']),36)
        self.assertEqual(r['previously_uncertified_unexcluded_count'],684)
        self.assertEqual(len(r['newly_excluded_over_old_rule']),20)

    def test_next_actual_source_not_third_prime_CM_screened(self):
        r=third.next_control();self.assertEqual(r['parameters_lambda_a_b'],[2,214,2])
        self.assertEqual(r['primitive_elliptic_theta_degree'],4);self.assertEqual(r['CM_screened_primes'],[13,17])
        self.assertFalse(self.c['scope_policy']['new_control_counted_at37'])

    def test_every_scope_promotion_rejected(self):
        for key in self.c['scope_policy']:
            changed=copy.deepcopy(self.c);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'scope promotion'):third.validate_contract(changed)


class HodgeInertEllipticProjectorTests(unittest.TestCase):
    def setUp(self):
        self.old=load(joint_screen.OUT.relative_to(ROOT).as_posix())
        self.c=json.loads(inert.CONTRACT.read_text(encoding='utf-8'))
    def f(self,a):
        r=next(r for r in self.old['finite_field_cases'] if (r['p'],r['a'])==(13,a))
        return tuple(tuple(z) for z in r['Gaussian_characteristic_coefficients_descending'])
    def cert(self):return inert.spectral_certificate(self.f(2),(3,2),(-2,-3))

    def test_exact_projector_derivative(self):self.assertEqual(self.cert()['PV8_derivative_at_gamma'],[-14400,-73600])

    def test_derivative_is_unit_at_inert3(self):
        r=self.cert();self.assertEqual(r['derivative_norm'],5624320000)
        self.assertEqual(r['derivative_norm_valuation3'],0)

    def test_exact_idempotency(self):self.assertTrue(self.cert()['exact_idempotent'])

    def test_exact_Rosati_self_adjointness(self):self.assertTrue(self.cert()['exact_Rosati_self_adjoint'])

    def test_Gaussian_rank_one(self):self.assertEqual(self.cert()['Gaussian_rank'],1)

    def test_all_projector_coefficients_3_integral(self):
        self.assertTrue(self.cert()['integral_at3'])
        for z in self.cert()['projector_coefficients_ascending']:
            for num,den in z:self.assertNotEqual(den%3,0)

    def test_conjugate_orientation_has_same_unit_norm(self):
        r=inert.spectral_certificate(tuple(inert.bar(z) for z in self.f(2)),(3,-2),(-2,3))
        self.assertEqual(r['derivative_norm'],self.cert()['derivative_norm']);self.assertTrue(r['integral_at3'])

    def test_wrong_Rosati_similitude_rejected(self):
        with self.assertRaisesRegex(ValueError,'Rosati self-adjoint'):inert.spectral_certificate(self.f(2),(3,2),(-2,-3),17)

    def test_wrong_finite_eigenvalue_rejected(self):
        with self.assertRaisesRegex(ValueError,'actual opposite CM root'):inert.spectral_certificate(self.f(2),(3,2),(2,3))

    def test_nonunit_control_is_inconclusive_not_bad_degree(self):
        r=inert.spectral_certificate(self.f(6),(3,2),(3,-2))
        self.assertFalse(r['integral_at3']);self.assertFalse(r['conditional_unit_degree_implication_certified'])
        self.assertFalse(self.c['scope_policy']['nonunit_derivative_proves_a_bad_theta_degree'])

    def test_F9_nonzero_norms_do_not_vanish(self):
        r=inert.norm_parity_certificate();self.assertEqual(len(r['nonzero_F9_norm_residues']),8)
        self.assertTrue(all(row[2] for row in r['nonzero_F9_norm_residues']))

    def test_forced_and_target_determinant_parities_conflict(self):
        r=inert.norm_parity_certificate();self.assertEqual(r['forced_sixfold_determinant_valuation_parity'],0)
        self.assertEqual(r['fixed_X6_determinant_valuation_parity'],1)

    def test_exact_target_End_field_required(self):
        with self.assertRaisesRegex(ValueError,'fixed End field'):inert.norm_parity_certificate(end0='unknown')

    def test_exact_target_norm_class_required(self):
        with self.assertRaisesRegex(ValueError,'norm class'):inert.norm_parity_certificate(det=-1)

    def test_even_fixed_dimension_not_optional(self):
        with self.assertRaisesRegex(ValueError,'dimension'):inert.norm_parity_certificate(dimension=5)

    def test_primitive_first_axis_degree_required(self):
        with self.assertRaisesRegex(ValueError,'primitive degree'):inert.norm_parity_certificate(first_degree=3)

    def test_updated_CRT201_one_survivor19_uncertified(self):
        r=inert.updated_crt(self.old['CRT_partition']);self.assertEqual(len(r['excluded']),201)
        self.assertEqual(r['joint_survivors'],[214]);self.assertEqual(len(r['uncertified']),19)

    def test_four_new_CRT_exclusions(self):
        self.assertEqual(inert.updated_crt(self.old['CRT_partition'])['newly_excluded'],[54,80,158,197])

    def test_remaining_source_not_excluded_and37_model_good(self):
        self.assertFalse(joint_screen.good_model(-7,29));self.assertTrue(joint_screen.good_model(-7,37))
        self.assertFalse(self.c['scope_policy']['remaining_a_minus7_control_excluded'])
        self.assertFalse(self.c['scope_policy']['third_prime_Frobenius_computed'])

    def test_every_scope_promotion_rejected(self):
        for key in self.c['scope_policy']:
            changed=copy.deepcopy(self.c);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'scope promotion'):inert.validate_contract(changed)


class HodgeOffReflectionJointScreenTests(unittest.TestCase):
    def setUp(self):
        self.data=load(joint_screen.COUNTS);self.old=load(a_line.COUNTS)
        self.c=json.loads(joint_screen.CONTRACT.read_text(encoding='utf-8'))
    def rows(self,p,a):
        inherited=p==13 and a!=5
        return [r for r in (self.old if inherited else self.data)['rows'] if r['a']==a and (inherited or r['p']==p)]
    def case(self,p,a):return joint_screen.annotated_case(self.rows(p,a),a,p)
    def cases(self):return [self.case(p,a) for p in (13,17) for a in joint_screen.REG[p]]

    def test_extended_chart13(self):
        self.assertEqual([a for a in range(13) if joint_screen.good_model(a,13)],[0,2,5,6,7,8,10,11,12])

    def test_extended_chart17(self):
        self.assertEqual([a for a in range(17) if joint_screen.good_model(a,17)],[0,1,2,4,6,7,8,9,10,11,13,14,15,16])

    def test_four_transverse_Weierstrass_intersections(self):
        c=joint_screen.weierstrass_chart_certificate();self.assertEqual(len(c),4)
        self.assertTrue(all(r['branch_multiplicity']==1 and r['local_dg_dy'] for r in c))

    def test_old_sufficient_chart_was_not_a_bad_reduction_theorem(self):
        self.assertFalse(a_line.good_model(5));self.assertTrue(joint_screen.good_model(5,13))
        self.assertTrue(joint_screen.good_model(1,17))

    def test_seventy_five_new_ordinary_sixty_twisted_rows(self):
        self.assertEqual(len(self.data['rows']),75)
        self.assertEqual(sum('rho_Frobenius_fixed_V' in r for r in self.data['rows']),60)

    def test_independent_new_Weierstrass13_counts(self):
        rows=self.rows(13,5);self.assertEqual(joint_screen.independent_counts(13)[5],[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']])

    def test_independent_all_fourteen17_cases(self):
        d=joint_screen.independent_counts(17)
        for a in joint_screen.REG[17]:
            r=self.rows(17,a);self.assertEqual(d[a],[r[0]['V'],r[1]['V'],r[0]['rho_Frobenius_fixed_V']])

    def test_a6_full_polynomial_at17(self):
        self.assertEqual(self.case(17,6)['Frobenius_characteristic_coefficients_descending'],[1,-2,39,-140,741,-4446,12819,-88232,217923,-1284894,3640533,-11692940,55374423,-48275138,410338673])

    def test_a6_no_extra_geometric_CM_at17(self):
        r=self.case(17,6);self.assertEqual(r['cyclotomic_factors'],[])
        self.assertEqual(r['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_positive_at13_does_not_lift(self):
        self.assertEqual(self.case(13,6)['geometric_reduction_Ei_multiplicity_in_complement'],1)
        self.assertEqual(self.case(17,6)['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_a7_is_CM_positive_but_same_type_only(self):
        r=self.case(17,7);self.assertEqual(r['geometric_reduction_Ei_multiplicity_in_complement'],1)
        self.assertEqual(r['opposite_type_reduction_multiplicity'],0)
        self.assertEqual(r['CM_Gaussian_linear_roots'],[{'type':'beta','unit':[1,0],'multiplicity':1}])

    def test_a10_opposite_type_at17(self):
        self.assertEqual(self.case(17,10)['CM_Gaussian_linear_roots'],[{'type':'conjugate_beta','unit':[0,1],'multiplicity':1}])

    def test_beta_and_conjugate_beta_do_not_differ_by_root_of_unity(self):
        for p in (13,17):
            b=joint_screen.BETA[p];r=joint_screen.zd(b,joint_screen.bar(b))
            self.assertNotIn(r,((1,0),(-1,0),(0,1),(0,-1)))

    def test_End_field_signature_forces_balanced_elliptic_surface(self):
        r=joint_screen.signature_certificate(self.c['signature_argument'])
        self.assertEqual(r['allowed_Ei_squared_native_signatures'],[[1,1]])

    def test_native_veto_cannot_omit_exact_End_field(self):
        s=copy.deepcopy(self.c['signature_argument']);s['fixed_X6_End0']='unknown'
        with self.assertRaisesRegex(ValueError,'End field'):joint_screen.signature_certificate(s)

    def test_native_veto_cannot_change_source_signature(self):
        s=copy.deepcopy(self.c['signature_argument']);s['source_native_K_signature']=[5,3]
        with self.assertRaisesRegex(ValueError,'signatures'):joint_screen.signature_certificate(s)

    def test_unpolarized_veto_does_not_assume_K_linear_isogeny(self):
        self.assertTrue(joint_screen.signature_certificate(self.c['signature_argument'])['unpolarized_isogeny_need_not_be_K_linear'])
        self.assertFalse(self.c['scope_policy']['isogeny_assumed_K_linear_for_unpolarized_veto'])

    def test_all_twenty_three_CM_certificates_exhaust_orders(self):
        for r in self.cases():
            w=r['residual_modular_witnesses'];self.assertEqual(w[-1]['remaining_orders'],[])
            self.assertEqual(sum(len(t['orders_excluded']) for t in w),55)

    def test_raw_CM_partition_keeps_four_joint_survivors(self):
        r=joint_screen.crt_partition(self.cases());self.assertEqual(len(r['raw_CM_excluded']),191)
        self.assertEqual(r['CM_only_joint_survivors'],[41,58,197,214])

    def test_native_type_partition_excludes197_not219(self):
        r=joint_screen.crt_partition(self.cases());self.assertEqual(len(r['typed_excluded']),197)
        self.assertEqual(r['typed_joint_survivors'],[197,214]);self.assertEqual(len(r['uncertified']),22)

    def test_new_actual_source_a_minus7_is_least_only_in_certified_domain(self):
        r=joint_screen.actual_control();self.assertEqual(r['parameters_lambda_a_b'],[2,-7,2])
        self.assertEqual(r['regular_residues_at13_and17'],[6,10]);self.assertEqual(r['primitive_elliptic_theta_degree'],4)
        self.assertFalse(self.c['scope_policy']['least_absolute_two_good_prime_lift_is_global_minimum'])

    def test_uncertified_classes_disjoint_from_veto(self):
        r=joint_screen.crt_partition(self.cases());self.assertFalse(set(r['uncertified'])&set(r['typed_excluded']))
        self.assertIn(3,r['uncertified'])

    def test_unused_fifth_trace_at_new_prime(self):
        self.rows(17,6)[4]['V']+=1
        with self.assertRaisesRegex(ValueError,'unused fifth trace'):self.case(17,6)

    def test_every_scope_promotion_rejected(self):
        for key in self.c['scope_policy']:
            changed=copy.deepcopy(self.c);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'scope promotion'):joint_screen.validate_contract(changed)


class HodgeOffReflectionALineTests(unittest.TestCase):
    def setUp(self):
        self.data=load(a_line.COUNTS)
        self.c=json.loads(a_line.CONTRACT.read_text(encoding='utf-8'))
    def rows(self,a):return [r for r in self.data['rows'] if r['a']==a]
    def case(self,a):return a_line.reconstruct(self.rows(a),a)
    def cert(self,a):return a_line.cm_certificate(tuple(self.case(a)['Frobenius_characteristic_coefficients_descending']))

    def test_all_thirteen_residues_partitioned(self):
        self.assertEqual(len(a_line.REGULAR)+len(self.c['arithmetic']['failed_model_a_residues']),13)

    def test_exact_regular_chart(self):
        self.assertEqual([a for a in range(13) if a_line.good_model(a)],[0,2,6,7,8,10,11,12])

    def test_failed_chart_not_a_complex_exclusion(self):
        self.assertEqual([a for a in range(13) if not a_line.good_model(a)],[1,3,4,5,9])
        self.assertFalse(self.c['scope_policy']['failed_model_excludes_complex_source'])

    def test_generic_denominator_pole_identity(self):self.assertTrue(a_line.pole_certificate())

    def test_a_dependent_rational_poles(self):
        self.assertEqual(a_line.prime_poles(2),4)
        for a in (0,6,7,8,10,11,12):self.assertEqual(a_line.prime_poles(a),0)

    def test_forty_ordinary_thirty_two_twisted_rows(self):
        self.assertEqual(len(self.data['rows']),40)
        self.assertEqual(sum('rho_Frobenius_fixed_V' in r for r in self.data['rows']),32)

    def test_independent_counts_all_eight(self):
        d=a_line.independent_counts()
        for a in a_line.REGULAR:
            rows=self.rows(a);self.assertEqual(d[a],[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']])

    def test_a0_complete_polynomial(self):
        self.assertEqual(self.case(0)['Frobenius_characteristic_coefficients_descending'],[1,4,16,-2,134,-36,-1251,-17596,-16263,-6084,294398,-57122,5940688,19307236,62748517])

    def test_a0_no_extra_CM_over_any_finite_extension(self):
        self.assertEqual(self.cert(0)['cyclotomic_factors'],[])
        self.assertEqual(self.cert(0)['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_a6_single_opposite_type_in_reduction(self):
        self.assertEqual(self.cert(6)['geometric_reduction_Ei_multiplicity_in_complement'],1)
        self.assertEqual(b_line.linear_multiplicity(self.case(6)['Gaussian_characteristic_coefficients_descending'],(3,-2)),1)

    def test_a2_exact_positive_cyclotomic_factor(self):
        self.assertEqual(self.cert(2)['cyclotomic_factors'],[{'order':4,'multiplicity':1}])

    def test_unused_fifth_trace_not_a_fit_parameter(self):
        self.rows(0)[4]['V']+=1
        with self.assertRaisesRegex(ValueError,'unused fifth rational trace'):self.case(0)

    def test_consistent_generic_reconstruction_for_matching_pole_profile(self):
        case={'p':13,'b':2,'i_mod_p':5,'rows':self.rows(0)}
        self.assertEqual(self.case(0),second_prime.reconstruct(case,{'p':13,'b':2,'i_mod_p':5,'beta':[3,2]}))

    def test_all_residual_CM_order_exclusions_complete(self):
        for a in a_line.REGULAR:
            w=self.cert(a)['residual_modular_witnesses'];self.assertEqual(w[-1]['remaining_orders'],[])
            self.assertEqual(sum(len(r['orders_excluded']) for r in w),55)

    def test_new_actual_source_not_just_residue(self):
        d=a_line.actual_control();self.assertEqual(d['parameters_lambda_a_b'],[2,6,2])
        self.assertEqual(d['primitive_elliptic_theta_degree'],4)

    def test_finite_field_residual_degree_twelve(self):
        c=self.case(6)['Frobenius_characteristic_coefficients_descending']
        q=a_line.monic_quotient(tuple(reversed(c)),(13,-6,1));self.assertEqual(len(q)-1,12)
        self.assertFalse(self.c['scope_policy']['finite_field_degree12_factor_simple_proved'])

    def test_exact_reflection_does_not_exclude_whole_residue_class(self):
        self.assertTrue(a_line.good_model(15));self.assertNotIn(15,(2,4))
        self.assertFalse(self.c['scope_policy']['whole_a2_residue_class_excluded_by_exact_reflection'])

    def test_off_reflection_survival_not_target_compatibility(self):
        self.assertFalse(self.c['scope_policy']['off_reflection_implies_target_compatible'])
        self.assertFalse(self.c['scope_policy']['surviving_reduction_lifts_a_complex_CM_axis'])

    def test_every_scope_promotion_rejected(self):
        for key in self.c['scope_policy']:
            changed=copy.deepcopy(self.c);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'beyond scope'):a_line.validate_contract(changed)

    def test_wrong_a2_pole_normalization_rejected(self):
        self.rows(2)[0]['rational_poles']=0
        with self.assertRaisesRegex(ValueError,'a-dependent pole'):self.case(2)


class HodgeScalarReflectionTests(unittest.TestCase):
    def setUp(self):self.c=json.loads(reflection.CONTRACT.read_text(encoding='utf-8'))

    def test_all_generic_symbolic_certificates(self):
        self.assertEqual(reflection.symbolic_certificates(),['one_torsion','lambda_torsion','zero_torsion'])

    def test_three_loci_not_whole_family(self):
        self.assertEqual(self.c['geometry']['reflection_loci'],['a=2*lambda','a=2','b=0'])
        self.assertFalse(self.c['scope_policy']['all_scalar_parameters_excluded'])

    def test_differential_is_negative_identity(self):
        for _,_,_,_,_,c,(u,v,w,z) in reflection.reflection_data():
            self.assertEqual(reflection.sub(reflection.mul(u,z),reflection.mul(v,w)),reflection.scale(c,-1))

    def test_Moebius_matrices_square_to_scalar(self):
        for _,_,_,_,_,c,(u,v,w,z) in reflection.reflection_data():
            self.assertEqual(reflection.add(reflection.mul(u,u),reflection.mul(v,w)),c)
            self.assertFalse(reflection.add(reflection.mul(u,v),reflection.mul(v,z)))

    def test_actual_invariant_coordinate(self):
        for _,_,_,q,r,c,_ in reflection.reflection_data():
            root=reflection.sub(reflection.X,r)
            self.assertEqual(reflection.sub(q,reflection.mul(root,r)),c)

    def test_general_lambda_one_torsion_witness(self):
        self.assertEqual(reflection.witness(3,6,2,'one_torsion')['H3_genus'],3)

    def test_general_lambda_lambda_torsion_witness(self):
        self.assertEqual(reflection.witness(3,2,2,'lambda_torsion')['H5_genus'],5)

    def test_zero_torsion_witness_off_other_two_loci(self):
        self.assertTrue(reflection.witness(2,0,0,'zero_torsion')['infinity_branch'])

    def test_infinity_branch_strata_included(self):
        for b in (0,1,-1):
            w=reflection.witness(2,4,b,'one_torsion')
            self.assertEqual(len(w['H3_branch_polynomial_ascending'])-1,7)
            self.assertTrue(w['infinity_branch'])

    def test_remaining_b3_has_actual_quotients(self):
        w=reflection.witness(2,4,3,'one_torsion')
        self.assertEqual((w['H3_genus'],w['H5_genus']),(3,5))

    def test_H5_projective_branch_count(self):
        for b in (0,2,3):
            w=reflection.witness(2,4,b,'one_torsion');degree=len(w['H3_branch_polynomial_ascending'])-1+4
            self.assertEqual(degree+degree%2,12)

    def test_actual_polarized_source_isogeny_degrees(self):
        g=self.c['geometry'];self.assertEqual(g['principal_source_product_isogeny_degree'],2**8)
        self.assertEqual(2*g['ramified_Prym_product_isogeny_degree'],256)
        self.assertFalse(self.c['scope_policy']['source_principally_polarized_product_isomorphism_claimed'])

    def test_simple_sixfold_dimension_obstruction(self):
        self.assertLess(max(self.c['geometry']['quotient_genera']),self.c['geometry']['target_simple_factor_dimension'])

    def test_actual_new_off_locus_control(self):
        w=reflection.off_locus_control()
        self.assertEqual(w['parameters_lambda_a_b'],[2,0,2]);self.assertEqual(w['primitive_elliptic_theta_degree'],4)

    def test_off_locus_control_not_declared_target_compatible(self):
        self.assertFalse(self.c['scope_policy']['off_locus_target_compatibility_established'])
        self.assertFalse(self.c['scope_policy']['off_locus_sources_have_simple_complement'])

    def test_singular_lambda_rejected(self):
        for l in (0,1):
            with self.assertRaisesRegex(ValueError,'nonsingular elliptic'):reflection.witness(l,2*l,2,'one_torsion')

    def test_off_locus_not_pulled_into_exclusion(self):
        with self.assertRaisesRegex(ValueError,'specified reflection locus'):reflection.witness(2,0,2,'one_torsion')

    def test_degenerate_source_not_claimed_admissible(self):
        with self.assertRaisesRegex(ValueError,'admissible disjoint branch'):reflection.witness(2,3,0,'zero_torsion')

    def test_scope_promotions_rejected(self):
        for key in self.c['scope_policy']:
            changed=copy.deepcopy(self.c);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'scope promoted'):reflection.validate_contract(changed)

    def test_no_finite_field_lifting_or_specialization_used(self):
        self.assertFalse(self.c['scope_policy']['complex_factors_lifted_from_finite_fields'])
        self.assertFalse(self.c['scope_policy']['reflection_exclusion_uses_arithmetic_specialization'])


class HodgeSecondPrimeTests(unittest.TestCase):
    def setUp(self):
        self.data=load(second_prime.COUNTS)
        self.contract=json.loads(second_prime.CONTRACT.read_text(encoding='utf-8'))

    def case(self,k):return second_prime.reconstruct(self.data['cases'][k],second_prime.CONTROLS[k])
    def cert(self,k):return second_prime.cm_certificate(tuple(self.case(k)['Frobenius_characteristic_coefficients_descending']),tuple(second_prime.CONTROLS[k]['beta']))

    def test_both_good_primes(self):
        self.assertTrue(second_prime.good_reduction(3,13))
        self.assertTrue(second_prime.good_reduction(6,29))

    def test_bad_b6_prime13_not_used(self):
        with self.assertRaisesRegex(ValueError,'good prime'):second_prime.good_reduction(6,13)

    def test_generic_independent_fields(self):
        for p,poly in ((13,(2,1,1)),(29,(3,1,1))):
            f=second_prime.Field(p,poly)
            self.assertEqual(f.add(p-1,1),0)
            self.assertEqual(f.mul(2,f.inv(2)),1)
            self.assertEqual(len(f.exp),p*p-1)

    def test_ten_ordinary_eight_twisted_rows(self):
        rows=[r for c in self.data['cases'] for r in c['rows']]
        self.assertEqual(len(rows),10)
        self.assertEqual(sum('rho_Frobenius_fixed_V' in r for r in rows),8)

    def test_nonrational_poles_not_omitted(self):
        for c in self.data['cases']:self.assertEqual([r['rational_poles'] for r in c['rows']],[0,4,0,4,0])

    def test_CM_orientation_not_arbitrary(self):
        changed=copy.deepcopy(second_prime.CONTROLS[1]);changed['beta']=[-5,2]
        with self.assertRaisesRegex(ValueError,'oriented CM'):second_prime.reconstruct(self.data['cases'][1],changed)

    def test_unused_fifth_trace_both(self):
        self.assertEqual(self.case(0)['rational_power_traces_through_degree5'],[2,6,-70,126,-2638])
        self.assertEqual(self.case(1)['rational_power_traces_through_degree5'],[-18,-42,582,-5890,-29298])

    def test_Gaussian_constants(self):
        for k,p in enumerate((13,29)):
            a=self.case(k)['Gaussian_characteristic_coefficients_descending'][-1]
            self.assertEqual(sum(x*x for x in a),p**7)

    def test_reciprocal_full_degree14_polynomials(self):
        for k,p in enumerate((13,29)):
            f=self.case(k)['Frobenius_characteristic_coefficients_descending']
            self.assertEqual(len(f),15)
            for j in range(8):self.assertEqual(f[14-j],p**(7-j)*f[j])

    def test_b3_positive_factors_require_exact_division(self):
        self.assertEqual(self.cert(0)['cyclotomic_factors'],[{'order':1,'multiplicity':2},{'order':2,'multiplicity':2}])
        self.assertEqual(self.cert(0)['geometric_reduction_Ei_multiplicity_in_complement'],2)

    def test_b6_no_CM_roots_over_any_extension(self):
        self.assertEqual(self.cert(1)['cyclotomic_factors'],[])
        self.assertEqual(self.cert(1)['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_residual_exclusions_cover_all_fifty_five_orders(self):
        for k in (0,1):
            w=self.cert(k)['residual_modular_witnesses']
            self.assertEqual(w[-1]['remaining_orders'],[])
            self.assertEqual(sum(len(r['orders_excluded']) for r in w),55)

    def test_b3_opposite_type_only_in_reduction(self):
        a=self.case(0)['Gaussian_characteristic_coefficients_descending']
        self.assertEqual(b_line.linear_multiplicity(a,(-3,2)),1)
        self.assertFalse(self.contract['scope_policy']['b3_surviving_reductions_lift_a_complex_CM_axis'])

    def test_negative_b_congruence_chart(self):
        self.assertTrue(second_prime.good_reduction(23,29))
        self.assertEqual(self.contract['arithmetic']['b6_exclusion_congruences_mod29'],[6,23])

    def test_forged_rational_poles_rejected(self):
        self.data['cases'][0]['rows'][0]['rational_poles']=4
        with self.assertRaisesRegex(ValueError,'pole normalization'):self.case(0)

    def test_forged_unused_fifth_trace_rejected(self):
        self.data['cases'][1]['rows'][4]['V']+=1
        with self.assertRaisesRegex(ValueError,'fifth rational trace'):self.case(1)

    def test_incomplete_extensions_rejected(self):
        self.data['cases'][0]['rows'].pop()
        with self.assertRaisesRegex(ValueError,'count coverage'):self.case(0)

    def test_every_scope_promotion_rejected(self):
        for key in self.contract['scope_policy']:
            changed=copy.deepcopy(self.contract);changed['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'beyond scope'):second_prime.validate_contract(changed)

    def test_actual_b6_source_is_retained(self):
        self.assertFalse(self.contract['scope_policy']['b6_source_construction_invalidated'])
        self.assertEqual(b_line.exact_lift(6)['tower_genera'],[17,9,5])

    def test_independent_small_and_direct_twisted_counts(self):
        for c in self.data['cases']:
            small,twist=second_prime.independent_counts(c['p'],c['b'],c['i_mod_p'],tuple(tuple(r['modulus']) for r in c['rows']))
            self.assertEqual(small,[[r['W'],r['V'],r['E']] for r in c['rows'][:2]])
            self.assertEqual(twist,[c['rows'][0]['twisted_base'],c['rows'][0]['rho_Frobenius_fixed_V']])


class HodgeBLineTests(unittest.TestCase):
    def setUp(self):
        self.data=load(b_line.COUNTS)
        self.contract=json.loads(b_line.CONTRACT.read_text(encoding='utf-8'))

    def case(self,b):return b_line.reconstruct([r for r in self.data['rows'] if r['b']==b])

    def test_all_seventeen_residues_classified(self):
        self.assertEqual(sum(b_line.chart_class(b)=='regular_chart' for b in range(17)),6)
        self.assertEqual(len(self.contract['arithmetic']['regular_chart_b'])+len(self.contract['arithmetic']['infinity_branch_chart_not_analyzed_b'])+len(self.contract['arithmetic']['displayed_reduction_chart_fails_b']),17)

    def test_infinity_stratum_is_not_excluded(self):
        for b in (0,1,16):self.assertEqual(b_line.chart_class(b),'infinity_branch_chart_not_analyzed')

    def test_failed_chart_is_not_a_complex_exclusion(self):
        for b in (4,5,7,8,9,10,12,13):self.assertEqual(b_line.chart_class(b),'displayed_reduction_chart_fails')
        self.assertFalse(self.contract['scope_policy']['failed_reduction_chart_excludes_complex_source'])

    def test_regular_chart_exact_six(self):
        self.assertEqual([b for b in range(17) if b_line.chart_class(b)=='regular_chart'],[2,3,6,11,14,15])

    def test_actual_new_rational_lifts(self):
        for b in (3,6):self.assertEqual(b_line.exact_lift(b)['tower_genera'],[17,9,5])

    def test_actual_primitive_theta_four_not_theta_six(self):
        for b in (3,6):self.assertEqual(b_line.exact_lift(b)['actual_primitive_elliptic_theta_degree'],4)
        self.assertFalse(self.contract['scope_policy']['opposite_character_theta6_axis_constructed'])

    def test_sign_pair_profiles(self):
        for b in (2,3,6):self.assertEqual(self.case(b),self.case(17-b))

    def test_twenty_four_count_rows(self):
        self.assertEqual(len(self.data['rows']),24)
        self.assertTrue(all('rho_Frobenius_fixed_V' in r for r in self.data['rows']))

    def test_independent_small_counts(self):
        out=b_line.independent_counts()
        for b in (2,3,6):
            rows=[r for r in self.data['rows'] if r['b']==b]
            self.assertEqual(out[b],[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']])

    def test_complete_Gaussian_reciprocity(self):
        for b in (2,3,6):
            a,f=self.case(b);self.assertEqual(sum(x*x for x in a[-1]),17**7)
            self.assertEqual(f[-1],17**7)

    def test_old_control_not_resurrected(self):
        self.assertEqual(self.case(2)[1],minimal_frob.EXPECTED)
        self.assertEqual(b_line.cm_certificate(tuple(self.case(2)[1]))['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_b3_exact_cyclotomic_part(self):
        c=b_line.cm_certificate(tuple(self.case(3)[1]))
        self.assertEqual(c['cyclotomic_factors'],[{'order':2,'multiplicity':2},{'order':4,'multiplicity':1}])
        self.assertEqual(c['geometric_reduction_Ei_multiplicity_in_complement'],2)

    def test_b6_exact_cyclotomic_part(self):
        c=b_line.cm_certificate(tuple(self.case(6)[1]))
        self.assertEqual(c['cyclotomic_factors'],[{'order':1,'multiplicity':6}])
        self.assertEqual(c['geometric_reduction_Ei_multiplicity_in_complement'],3)

    def test_residual_certificates_exhaustive(self):
        for b in (2,3,6):
            c=b_line.cm_certificate(tuple(self.case(b)[1]))
            self.assertEqual(c['residual_modular_witnesses'][-1]['remaining_orders'],[])
            self.assertEqual(sum(len(w['orders_excluded']) for w in c['residual_modular_witnesses']),55)

    def test_opposite_type_roots_only_in_reduction(self):
        a,_=self.case(3);self.assertEqual(b_line.linear_multiplicity(a,(-1,4)),1)
        a,_=self.case(6);self.assertEqual(b_line.linear_multiplicity(a,(1,-4)),2)
        self.assertFalse(self.contract['scope_policy']['surviving_reduction_lifts_a_complex_CM_axis'])

    def test_forged_twisted_count_rejected(self):
        self.data['rows'][1]['rho_Frobenius_fixed_V']+=1
        with self.assertRaises(ValueError):self.case(3)

    def test_incomplete_moment_coverage_rejected(self):
        rows=[r for r in self.data['rows'] if r['b']==3][:-1]
        with self.assertRaisesRegex(ValueError,'four-moment coverage'):b_line.reconstruct(rows)

    def test_prime_cannot_be_changed(self):
        self.contract['arithmetic']['prime']=13
        with self.assertRaisesRegex(ValueError,'arithmetic changed'):b_line.validate_contract(self.contract)

    def test_scope_promotions_rejected(self):
        for key in self.contract['scope_policy']:
            d=copy.deepcopy(self.contract);d['scope_policy'][key]=True
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError,'promoted to complex matching'):b_line.validate_contract(d)

    def test_congruence_domain_is_algebraic_not_transcendental(self):
        self.assertEqual(self.contract['arithmetic']['congruence_exclusion_domain'],'algebraic_b_integral_at_a_place_over17_reducing_to_2_or15')
        self.assertFalse(self.contract['scope_policy']['transcendental_parameters_excluded'])


class HodgeMinimalFrobeniusTests(unittest.TestCase):
    def setUp(self):
        self.data=load(minimal_frob.COUNTS)
        self.contract=json.loads(minimal_frob.CONTRACT.read_text(encoding='utf-8'))

    def test_count_coverage_five_ordinary_four_twisted(self):
        self.assertEqual(len(self.data['rows']),5)
        self.assertEqual(sum('rho_Frobenius_fixed_V' in r for r in self.data['rows']),4)

    def test_good_prime_seventeen(self):
        self.assertTrue(minimal_frob.good_reduction())

    def test_independent_small_counts(self):
        self.assertEqual(minimal_frob.independent_small_counts()[0],[(16,8,16),(320,336,320)])

    def test_direct_twisted_count_over_fourth_extension(self):
        self.assertEqual(minimal_frob.independent_small_counts()[1],(16,16))

    def test_Gaussian_moments(self):
        self.assertEqual(minimal_frob.reconstruct(self.data)['Gaussian_power_traces'],[[3,-4],[7,-32],[51,-68],[391,176]])

    def test_full_sevenfold_polynomial(self):
        self.assertEqual(minimal_frob.reconstruct(self.data)['Frobenius_characteristic_coefficients_descending'],minimal_frob.EXPECTED)

    def test_unitary_reconstructed_constant(self):
        a=minimal_frob.reconstruct(self.data)['Gaussian_characteristic_coefficients_descending']
        self.assertEqual(a[-1],[-4913,19652])
        self.assertEqual(sum(x*x for x in a[-1]),17**7)

    def test_unused_fifth_trace(self):
        self.assertEqual(minimal_frob.reconstruct(self.data)['rational_power_traces_through_degree5'][-1],5126)

    def test_forged_fifth_count_rejected(self):
        self.data['rows'][4]['V']+=1
        with self.assertRaisesRegex(ValueError,'rational trace control'):minimal_frob.reconstruct(self.data)

    def test_forged_twisted_count_rejected(self):
        self.data['rows'][0]['rho_Frobenius_fixed_V']+=2
        with self.assertRaises(ValueError):minimal_frob.reconstruct(self.data)

    def test_reduction_is_not_asserted_simple(self):
        factors=minimal_frob.reconstruct(self.data)['reduction_factor_coefficients_descending']
        self.assertEqual([len(f)-1 for f in factors],[4,10])
        self.assertFalse(self.contract['scope_policy']['reduction_sevenfold_simple'])

    def test_complete_CM_order_coverage(self):
        c=minimal_frob.cm_ratio_certificate(minimal_frob.EXPECTED)
        self.assertEqual(c['cyclotomic_orders_checked_including_one'],55)
        self.assertEqual(c['CM_ratio_modular_witnesses'][0]['remaining_orders'],[50])
        self.assertEqual(c['CM_ratio_modular_witnesses'][1]['remaining_orders'],[])

    def test_norm_polynomial_exact_end_coefficients(self):
        f=minimal_frob.cm_ratio_certificate(minimal_frob.EXPECTED)['CM_ratio_norm_polynomial_coefficients_ascending']
        self.assertEqual(len(f),29)
        self.assertEqual((f[0],f[-1]),(17**14,17**14))

    def test_actual_CM_power_is_not_falsely_excluded(self):
        p={0:1}
        for _ in range(7):p=minimal_source.mul(p,{0:17,1:-2,2:1})
        with self.assertRaisesRegex(ValueError,'unexcluded CM elliptic'):minimal_frob.cm_ratio_certificate([p.get(i,0) for i in range(14,-1,-1)])

    def test_scope_promotions_rejected(self):
        for key in self.contract['scope_policy']:
            with self.subTest(key=key):
                d=copy.deepcopy(self.contract);d['scope_policy'][key]=True
                with self.assertRaisesRegex(ValueError,'beyond control'):minimal_frob.validate_contract(d)

    def test_bad_prime_not_substituted(self):
        self.contract['arithmetic']['prime']=5
        with self.assertRaisesRegex(ValueError,'arithmetic changed'):minimal_frob.validate_contract(self.contract)


if __name__ == '__main__':
    unittest.main(verbosity=2)
