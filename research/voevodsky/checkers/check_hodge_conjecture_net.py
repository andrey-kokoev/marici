"""Validate Hodge work gates and by-reference foundational wiring, not Hodge truth.
Uses the shared MetricGraph DAG validator. --pin creates, never overwrites, the
explicit source snapshot. --check verifies an existing result without writing.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph
from check_hodge_obstruction_controls import report as control_report
from check_hodge_cycle_map_scope import report as cycle_scope_report
from check_hodge_cycle_packet_dictionary import report as dictionary_report
from check_hodge_literature_boundary_audit import report as audit_report, source_paths as audit_source_paths
from check_hodge_explicit_sixfold_candidate import report as candidate_report
from check_hodge_weil_projector import report as projector_report
from check_hodge_tautological_witness_search import report as search_report
from check_hodge_middle_hodge_kernel import report as kernel_report
from check_hodge_secant_sheaf_transplant import report as transplant_report, source_paths as transplant_source_paths
from check_hodge_split_eightfold_stabilization import report as stabilization_report
from check_hodge_eightfold_weil_filter import report as eightfold_filter_report
from check_hodge_eightfold_hodge_kernel import report as eightfold_kernel_report
from check_hodge_chern_witness_transfer import report as chern_transfer_report
from check_hodge_reflexive_rank_reduction import report as reduction_report
from check_hodge_cyclic_prym_audit import report as prym_report, source_paths as prym_source_paths
from check_hodge_gaussian_principal_isogeny import report as principal_isogeny_report
from check_hodge_principal_prym_membership import report as principal_prym_report, source_paths as principal_prym_sources
from check_hodge_indecomposable_principal_model import report as indecomposable_report
from check_hodge_y2_curve_audit import report as y2_curve_report, source_paths as y2_curve_sources
from check_hodge_hyperelliptic_bottom_audit import report as bottom_report
from check_hodge_bielliptic_lift_audit import report as lift_report, POLICY as LIFT_POLICY
from check_hodge_commuting_prym_audit import report as commuting_report, POLICY as COMMUTING_POLICY, source_paths as commuting_sources
from check_hodge_even_scalar_cover import report as even_scalar_report, POLICY as EVEN_SCALAR_POLICY
from check_hodge_asymmetric_scalar_cover import report as asymmetric_report, POLICY as ASYMMETRIC_POLICY
from check_hodge_asymmetric_reflections import report as automorphism_report, POLICY as AUTOMORPHISM_POLICY
from check_hodge_asymmetric_frobenius import report as frobenius_report, POLICY as FROBENIUS_POLICY, source_paths as frobenius_sources
from check_hodge_asymmetric_absolute import report as absolute_report, POLICY as ABSOLUTE_POLICY
from check_hodge_scalar_family_localization import report as scalar_family_report, POLICY as SCALAR_FAMILY_POLICY
from check_hodge_scalar_polarized_obstruction import report as scalar_polarized_report, POLICY as SCALAR_POLARIZED_POLICY, source_paths as scalar_polarized_sources
from check_hodge_nonlifting_polarized_obstruction import report as nonlifting_report, POLICY as NONLIFTING_POLICY
from check_hodge_secant_local_ext_gate import report as local_ext_report, POLICY as LOCAL_EXT_POLICY
from check_hodge_secant_source_semiregularity import report as source_semireg_report, POLICY as SOURCE_SEMIREG_POLICY
from check_hodge_secant_criterion_persistence import report as persistence_report, POLICY as PERSISTENCE_POLICY
from check_hodge_ramified_trigonal_family import report as ramified_family_report, POLICY as RAMIFIED_FAMILY_POLICY, source_paths as ramified_family_sources
from check_hodge_trigonal_principal_match_obstruction import report as principal_match_report, POLICY as PRINCIPAL_MATCH_POLICY
from check_hodge_cyclic_prym_odd_axis_obstruction import report as odd_axis_report, POLICY as ODD_AXIS_POLICY
from check_hodge_two_branch_odd_axis_obstruction import report as two_branch_report, POLICY as TWO_BRANCH_POLICY, source_paths as two_branch_sources
from check_hodge_even_axis_principal_model import report as even_axis_report, POLICY as EVEN_AXIS_POLICY
from check_hodge_even_axis_coupled_kummer_gate import report as coupled_kummer_report, POLICY as COUPLED_KUMMER_POLICY
from check_hodge_even_axis_joint_degree_gate import report as joint_degree_report, POLICY as JOINT_DEGREE_POLICY
from check_hodge_minimal_axis_scalar_source import report as minimal_source_report, POLICY as MINIMAL_SOURCE_POLICY
from check_hodge_minimal_axis_frobenius_obstruction import report as minimal_frob_report, POLICY as MINIMAL_FROB_POLICY, source_paths as minimal_frob_sources
from check_hodge_minimal_axis_b_line import report as b_line_report, POLICY as B_LINE_POLICY, source_paths as b_line_sources
from check_hodge_minimal_axis_second_prime import report as second_prime_report, POLICY as SECOND_PRIME_POLICY, source_paths as second_prime_sources
from check_hodge_scalar_reflection_decomposition import report as reflection_report, POLICY as REFLECTION_POLICY
from check_hodge_off_reflection_a_line import report as a_line_report, POLICY as A_LINE_POLICY, source_paths as a_line_sources
from check_hodge_off_reflection_joint_screen import report as joint_screen_report, POLICY as JOINT_SCREEN_POLICY, source_paths as joint_screen_sources
from check_hodge_inert_elliptic_projector import report as inert_report, POLICY as INERT_POLICY
from check_hodge_off_reflection_third_prime import report as third_report, POLICY as THIRD_POLICY, source_paths as third_sources
from check_hodge_scalar_37_census import report as census37_report, POLICY as CENSUS37_POLICY, source_paths as census37_sources
from check_hodge_refutation_direction import validate_direction, source_paths as direction_sources
from check_hodge_equivariant_tetragonal_gate import report as tetragonal_report, POLICY as TETRAGONAL_POLICY
from check_hodge_eightfold_literature_audit import report as eightfold_literature_report, POLICY as EIGHTFOLD_LITERATURE_POLICY, source_paths as eightfold_literature_sources

HOME = 'research/conjecture_net/'
CONTRACT = HOME + 'contracts/hodge-conjecture-net.v1.json'
ATTACHMENTS = HOME + 'contracts/hodge-foundational-attachments.v1.json'
OUT = ROOT / 'research/voevodsky/results/hodge-conjecture-net-v1.json'
EXPECTED_NODES = {
    'fixed-candidate-nonalgebraicity', 'higher-coherence-counterexample-existence',
    'scalar-37-full-screen', 'scalar-37-typed-polarized-target-transplant', 'off-reflection-third-prime-generic-gate', 'third-prime-and-generic-target-transplant', 'inert-elliptic-projector-gate', 'inert-degree-parity-target-transplant', 'off-reflection-two-prime-screen', 'off-reflection-two-prime-target-transplant', 'off-reflection-a-line-screen', 'off-reflection-a-line-target-transplant', 'scalar-reflection-quotient-decomposition', 'reflection-symmetric-scalar-target-transplant', 'minimal-axis-second-prime-screen', 'minimal-axis-b6-target-transplant', 'minimal-axis-b-line-screen', 'minimal-axis-scalar-target-transplant', 'minimal-axis-scalar-source', 'even-axis-joint-degree-gate', 'even-axis-coupled-kummer-gate', 'even-axis-principal-model', 'y2-two-branch-cyclic-quartic-transplant', 'y2-etale-cyclic-quartic-polarized-transplant', 'ramified-trigonal-principal-target-transplant', 'ramified-trigonal-auxiliary-family', 'eightfold-secant-weak-criterion-transplant', 'secant-source-weak-semiregularity-transplant', 'secant-local-ext-gate', 'eightfold-literature-and-secant-audit',
    'scope-and-cycle-map', 'literature-boundary-audit', 'positive-and-rational-controls',
    'candidate-variety-and-class', 'packet-coherence-dictionary', 'obstruction-construction',
    'cohomology-descent', 'rational-survival', 'all-algebraic-cycles-annihilation',
    'candidate-hodge-membership', 'candidate-obstruction-nonzero',
    'counterexample-assembly', 'algebraic-witness-search', 'bare-chain-closure-obstruction',
    'uniform-weil-projector-annihilation', 'tautological-power-witness-search', 'generic-middle-hodge-kernel', 'secant-sheaf-transplant', 'split-eightfold-stabilization', 'eightfold-weil-filter', 'eightfold-full-hodge-kernel', 'higher-chern-witness-transfer', 'reflexive-rank-reduction', 'cyclic-quartic-prym-transplant', 'gaussian-principal-isogeny', 'principal-prym-membership-audit', 'indecomposable-principal-model', 'y2-jacobian-low-gonality-transplant', 'hyperelliptic-bottom-prym-transplant', 'bielliptic-involution-lift-transplant', 'commuting-prym-factor-transplant', 'inversion-symmetric-scalar-transplant', 'asymmetric-scalar-cover-control', 'asymmetric-cover-automorphisms', 'asymmetric-prym-frobenius7', 'asymmetric-scalar-target-transplant', 'scalar-family-localization', 'scalar-polarized-prym-transplant', 'nonlifting-polarized-prym-transplant', 'equivariant-tetragonal-gate',
}
SCOPED_REJECTION_INPUTS = {
    'minimal-axis-b-line-screen': {'minimal-axis-scalar-source':'constructed','minimal-axis-scalar-target-transplant':'rejected'},
    'even-axis-principal-model': {'indecomposable-principal-model':'constructed',
        'y2-etale-cyclic-quartic-polarized-transplant':'rejected','y2-two-branch-cyclic-quartic-transplant':'rejected'},
    'y2-two-branch-cyclic-quartic-transplant': {'y2-etale-cyclic-quartic-polarized-transplant':'rejected',
        'indecomposable-principal-model':'constructed','ramified-trigonal-auxiliary-family':'constructed'},
    'y2-etale-cyclic-quartic-polarized-transplant': {'indecomposable-principal-model':'constructed',
        'equivariant-tetragonal-gate':'constructed','ramified-trigonal-principal-target-transplant':'rejected'},
    'ramified-trigonal-principal-target-transplant': {'ramified-trigonal-auxiliary-family':'constructed',
        'equivariant-tetragonal-gate':'constructed','cyclic-quartic-prym-transplant':'rejected'},
    'eightfold-secant-weak-criterion-transplant': {'secant-source-weak-semiregularity-transplant':'rejected',
        'secant-local-ext-gate':'constructed'},
    'scalar-family-localization': {'asymmetric-scalar-target-transplant':'rejected'},
    'nonlifting-polarized-prym-transplant': {'scalar-polarized-prym-transplant':'rejected',
        'indecomposable-principal-model':'constructed','y2-jacobian-low-gonality-transplant':'rejected'},
    'equivariant-tetragonal-gate': {'nonlifting-polarized-prym-transplant':'rejected',
        'indecomposable-principal-model':'constructed','y2-jacobian-low-gonality-transplant':'rejected',
        'hyperelliptic-bottom-prym-transplant':'rejected'},
}
EXPECTED_LINKS = {
    'parent-to-hodge-scope': ('parent', 'mathematical-realization', 'hodge', 'scope-and-cycle-map', 'common-foundations-context'),
    'identity-to-hodge-scope': ('identity', 'scope', 'hodge', 'scope-and-cycle-map', 'identity-scope-context'),
    'math-to-hodge-dictionary': ('math', 'stagewise-mathematical-interface', 'hodge', 'packet-coherence-dictionary', 'stagewise-interface-context'),
    'identity-to-hodge-coherence': ('identity', 'higher-coherence', 'hodge', 'packet-coherence-dictionary', 'higher-coherence-context'),
    'hodge-dictionary-to-identity-review': ('hodge', 'packet-coherence-dictionary', 'identity', 'continuation-and-composition', 'hodge-dictionary-review'),
    'hodge-rational-boundary-to-identity-review': ('hodge', 'rational-survival', 'identity', 'higher-coherence', 'rational-obstruction-review'),
    'hodge-to-mathematical-parent-review': ('hodge', 'counterexample-assembly', 'parent', 'mathematical-realization', 'hodge-example-review'),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def path(name):
    p = (ROOT / name).resolve()
    require(p.is_relative_to(ROOT), 'path escapes repository')
    return p


def load(name):
    return json.loads(path(name).read_text(encoding='utf-8'))


def digest(name):
    return sha256(path(name).read_bytes()).hexdigest()


def node_ids(c):
    result = {n['id'] for n in c.get('conjectures', []) + c.get('obligations', [])}
    if isinstance(c.get('root'), dict):
        result.add(c['root']['id'])
    return result


def load_bundle():
    c, a = load(CONTRACT), load(ATTACHMENTS)
    refs = {alias: c if alias == 'hodge' else load(file) for alias, file in a['contracts'].items()}
    controls = load('research/voevodsky/results/hodge-obstruction-controls-v1.json')
    return c, a, refs, controls, load(HOME + 'registry.json')


def predecessors(c):
    while c.get('predecessor'):
        previous = c['predecessor']
        prior = load(previous['contract_snapshot'])
        require(prior.get('iteration', 0) == c['iteration'] - 1, 'predecessor iteration order')
        require(prior['source_pins'] == previous['source_pins'], 'predecessor pin identity')
        yield previous, prior
        c = prior


def validate(c, a, refs, controls, registry):
    require(c['id'] == 'marici.hodge-coherence-obstruction-work.v1', 'work net identity')
    h = c['classical_conjecture']
    require(h['status'] == 'open' and h['outcome'] is None and c['objective']['outcome'] is None,
            'unreviewed Hodge outcome')
    require(h['coefficients'] == 'Q' and h['base_field'] == 'C' and h['smooth'] is True and h['projective'] is True, 'classical scope/coefficients')
    require(h['quantifiers'] == {'varieties': 'all_smooth_projective_complex_varieties',
            'codimensions': 'every_integer_0_le_p_le_dimX',
            'cycles': 'all_codimension_p_algebraic_cycles_with_rational_coefficients'}, 'classical quantifier restriction')
    require(c['research_hypothesis']['status'] == 'open' and c['research_hypothesis']['outcome'] is None, 'intuition promoted to theorem')
    require(all(v is False for v in c['boundary'].values()) and not c.get('imports', []), 'proof or physical promotion')
    require(c['scope']['cycle_map_is_equivalence'] is False, 'cycle-class surjectivity is not equivalence')
    candidate_id = 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1'
    require(c['scope']['candidate_status'] == 'selected_explicit_marked_period_integral_Hodge_class_algebraicity_open' and
            (c['scope']['candidate_X'], c['scope']['candidate_p'], c['scope']['candidate_alpha']) ==
            (candidate_id + ':X', 3, candidate_id + ':alpha'), 'unreviewed candidate selection')
    obstruction = c['obstruction_contract']
    require(obstruction['status'] == 'candidate_defined_all_cycle_annihilation_open' and
            obstruction['definition_artifact'] == 'weil-projector' and
            obstruction['validated_hodge_obstruction'] is False and
            obstruction['target_coefficients'] == 'Q', 'unreviewed obstruction')
    require(obstruction['required_domain'] == 'rational_cohomology_classes_not_chosen_cocycles_or_packet_presentations', 'representative-level obstruction')
    require(obstruction['required_annihilation'] == 'image_of_cycle_class_on_ALL_rational_algebraic_cycles', 'divisor-only/finite-cycle annihilation')
    require(set(obstruction['required_properties']) == {'Q_linearity', 'cohomology_class_invariance',
            'independence_of_charts_and_auxiliary_choices', 'non_torsion_rational_detection',
            'vanishing_on_all_algebraic_cycle_classes'}, 'obstruction gate bypass')
    require(controls == control_report() and controls['passed'], 'control receipt stale or altered')
    require(not any(controls['results'][k] for k in ('Hodge_proved', 'Hodge_refuted', 'general_algebraic_cycle_annihilation_proved')), 'controls promoted')
    by = {n['id']: n for n in c['conjectures']}
    require(set(by) == EXPECTED_NODES and len(by) == len(c['conjectures']), 'work node census')
    MetricGraph(tuple(MetricAction(n['id'], frozenset(n['depends_on']), frozenset(n['requires']),
                status='resolved' if n['status'] == 'resolved' else 'active',
                terminal=n['id'] == c['objective']['target']) for n in c['conjectures'])).validate()
    require(c['objective']['target'] == 'counterexample-assembly', 'objective target')
    for n in c['conjectures']:
        require(n['outcome'] is None, 'unreviewed node proof outcome')
        require(n['statement'] and n['acceptance'] and n['falsifier'], 'missing scientific gate')
        # Only these exact scoped proof/census imports may consume rejections.
        # Negative outcomes never become constructed cycle/assembly witnesses.
        scoped_anchor = n['required_verdicts'] == SCOPED_REJECTION_INPUTS.get(n['id'])
        require(len(n['depends_on']) == len(set(n['depends_on'])) and
                set(n['required_verdicts']) == set(n['depends_on']) and
                (scoped_anchor or all(v == 'constructed' for v in n['required_verdicts'].values())), 'required constructed-witness gate')
        if n['id'] == 'positive-and-rational-controls':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['control-bundle'], 'control binding')
        elif n['id'] == 'scope-and-cycle-map':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['cycle-map-scope'] and
                    n['resolution_kind'] == 'typed_scope_definition_and_linear_descent_lemma', 'scope result binding')
        elif n['id'] == 'literature-boundary-audit':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['literature-boundary-audit'] and
                    n['resolution_kind'] == 'dated_source_specific_boundary_audit_with_discriminant_controls', 'literature audit binding')
        elif n['id'] in ('candidate-variety-and-class', 'candidate-hodge-membership'):
            kind = {'candidate-variety-and-class': 'explicit_marked_polarized_torus_and_integral_weil_class',
                    'candidate-hodge-membership': 'balanced_weil_determinant_Hodge_membership'}[n['id']]
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['explicit-sixfold-candidate'] and n['resolution_kind'] == kind,
                    'candidate construction/membership binding')
        elif n['id'] in ('obstruction-construction', 'cohomology-descent', 'rational-survival', 'candidate-obstruction-nonzero'):
            kind = {'obstruction-construction': 'explicit_candidate_weil_isotypic_projector_without_annihilation',
                    'cohomology-descent': 'functorial_cohomology_projector_independent_of_presentations',
                    'rational-survival': 'nonzero_rational_rank_two_projector_target',
                    'candidate-obstruction-nonzero': 'fixed_alpha_is_fixed_by_candidate_projector'}[n['id']]
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['weil-projector'] and n['resolution_kind'] == kind, 'candidate projector gate binding')
        elif n['id'] == 'uniform-weil-projector-annihilation':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and n['evidence'] == ['weil-projector'] and
                    n['resolution_kind'] == 'special_fiber_algebraic_weil_classes_refute_uniform_annihilation', 'uniform rejection binding')
        elif n['id'] == 'tautological-power-witness-search':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['tautological-witness-search'] and
                    n['resolution_kind'] == 'central_i_symmetry_excludes_divisorial_power_correspondence_library', 'bounded witness rejection binding')
        elif n['id'] == 'generic-middle-hodge-kernel':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['middle-hodge-kernel'] and
                    n['resolution_kind'] == 'generic_degree_six_Hodge_kernel_and_finite_order_cycle_projector', 'middle Hodge kernel binding')
        elif n['id'] == 'secant-sheaf-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['secant-sheaf-transplant'] and
                    n['resolution_kind'] == 'fixed_isogeny_class_discriminant_rigidity_blocks_retained_split_secant_theorem', 'secant transplant rejection binding')
        elif n['id'] == 'split-eightfold-stabilization':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['split-eightfold-stabilization'] and
                    n['resolution_kind'] == 'explicit_split_eightfold_and_algebraic_Weil_transfer_retraction', 'stabilization node binding')
        elif n['id'] == 'eightfold-weil-filter':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['eightfold-weil-filter'] and
                    n['resolution_kind'] == 'rank_two_eightfold_CRT_projector_and_typed_cycle_filter', 'eightfold filter node binding')
        elif n['id'] == 'eightfold-full-hodge-kernel':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['eightfold-hodge-kernel'] and
                    n['resolution_kind'] == 'full_product_Hodge_space_and_complete_exceptional_cycle_test', 'eightfold Hodge node binding')
        elif n['id'] == 'higher-chern-witness-transfer':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['chern-witness-transfer'] and
                    n['resolution_kind'] == 'rank_sensitive_normalized_Chern_audit_and_conditional_bundle_transfer', 'Chern transfer node binding')
        elif n['id'] == 'reflexive-rank-reduction':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['reflexive-rank-reduction'] and
                    n['resolution_kind'] == 'generic_determinantal_smoothing_and_rank_two_reflexive_witness_equivalence', 'reflexive reduction node binding')
        elif n['id'] == 'cyclic-quartic-prym-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['cyclic-quartic-prym-audit'] and
                    n['resolution_kind'] == 'cyclic_quartic_Prym_polarization_and_discriminant_exclude_fixed_isogeny_class', 'cyclic Prym node binding')
        elif n['id'] == 'gaussian-principal-isogeny':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['gaussian-principal-isogeny'] and
                    n['resolution_kind'] == 'explicit_mixed_three_torsion_Gaussian_principal_quotient_and_cycle_transfer', 'principal isogeny node binding')
        elif n['id'] == 'principal-prym-membership-audit':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['principal-prym-membership-audit'] and
                    n['resolution_kind'] == 'fixed_polarization_product_factor_and_Mumford_hyperelliptic_cover_exclusion', 'principal Prym node binding')
        elif n['id'] == 'indecomposable-principal-model':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['indecomposable-principal-model'] and
                    n['resolution_kind'] == 'two_primary_repolarized_Gaussian_gluing_indecomposable_model_with_phase_correct_transfer', 'indecomposable model node binding')
        elif n['id'] == 'y2-jacobian-low-gonality-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['y2-curve-audit'] and
                    n['resolution_kind'] == 'polarized_Torelli_elliptic_degree_two_and_free_involution_low_gonality_exclusion', 'Y2 curve node binding')
        elif n['id'] == 'hyperelliptic-bottom-prym-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['hyperelliptic-bottom-audit'] and
                    n['resolution_kind'] == 'pointed_dihedral_lift_square_fourfold_obstruction_and_conditional_bielliptic_descent', 'bottom-cover node binding')
        elif n['id'] == 'bielliptic-involution-lift-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['bielliptic-lift-audit'] and
                    n['resolution_kind'] == 'norm_strata_dihedral_quarter_exclusion_and_nonlifting_half_control', 'bielliptic-lift node binding')
        elif n['id'] == 'commuting-prym-factor-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['commuting-prym-audit'] and
                    n['resolution_kind'] == 'commuting_quotient_genus_ramified_polarization_and_inert_three_parity_exclusion', 'commuting Prym node binding')
        elif n['id'] == 'inversion-symmetric-scalar-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['even-scalar-cover'] and
                    n['resolution_kind'] == 'explicit_cyclic_four_isogeny_even_branch_involutive_lift_and_fourfold_square', 'even scalar node binding')
        elif n['id'] == 'asymmetric-scalar-cover-control':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['asymmetric-scalar-cover'] and
                    n['resolution_kind'] == 'explicit_smooth_asymmetric_tower_fixed_origin_nonlift_and_good_reduction_profiles', 'asymmetric node binding')
        elif n['id'] == 'asymmetric-cover-automorphisms':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['asymmetric-reflections'] and
                    n['resolution_kind'] == 'branch_sum_full_eight_torsion_stabilizer_and_unique_bielliptic_automorphism_certificate', 'automorphism node binding')
        elif n['id'] == 'asymmetric-prym-frobenius7':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['asymmetric-frobenius'] and
                    n['resolution_kind'] == 'fresh_extension_counts_Newton_reconstruction_and_modular_degree_irreducibility', 'Frobenius node binding')
        elif n['id'] == 'asymmetric-scalar-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['asymmetric-absolute'] and
                    n['depends_on'] == ['asymmetric-prym-frobenius7','indecomposable-principal-model'] and
                    n['resolution_kind'] == 'cyclotomic_ratio_exclusion_absolute_simple_reduction_and_specialization', 'absolute node binding')
        elif n['id'] == 'scalar-family-localization':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['scalar-family-localization'] and
                    n['depends_on'] == ['asymmetric-scalar-target-transplant'] and
                    n['required_verdicts'] == {'asymmetric-scalar-target-transplant':'rejected'} and
                    n['resolution_kind'] == 'elliptic_pencil_period_immersion_generic_simplicity_and_seven_adic_exclusion', 'scalar family node binding')
        elif n['id'] == 'scalar-polarized-prym-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['scalar-polarized-obstruction'] and
                    n['depends_on'] == ['indecomposable-principal-model','scalar-family-localization'] and
                    n['resolution_kind'] == 'anti_invariant_elliptic_map_quadratic_independence_and_genus_bound', 'scalar polarized node binding')
        elif n['id'] == 'nonlifting-polarized-prym-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['nonlifting-polarized-obstruction'] and
                    n['depends_on'] == ['scalar-polarized-prym-transplant','indecomposable-principal-model','y2-jacobian-low-gonality-transplant'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'joint_degree_exhaustion_genus_equality_free_involution_and_forced_lift', 'nonlifting node binding')
        elif n['id'] == 'equivariant-tetragonal-gate':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['equivariant-tetragonal-gate'] and
                    n['depends_on'] == ['nonlifting-polarized-prym-transplant','indecomposable-principal-model','y2-jacobian-low-gonality-transplant','hyperelliptic-bottom-prym-transplant'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'elliptic_axis_quotient_free_involution_pencil_and_even_fibre_cyclic_lift_gate', 'tetragonal node binding')
        elif n['id'] == 'scalar-37-full-screen':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['scalar-37-census'] and
                    n['depends_on'] == ['off-reflection-third-prime-generic-gate','inert-elliptic-projector-gate'] and
                    n['required_verdicts'] == {'off-reflection-third-prime-generic-gate':'constructed','inert-elliptic-projector-gate':'constructed'} and
                    n['resolution_kind'] == 'complete_regular37_CM_native_type_and_projector_census', 'full37 census node binding')
        elif n['id'] == 'scalar-37-typed-polarized-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['scalar-37-census'] and
                    n['depends_on'] == ['scalar-37-full-screen','even-axis-principal-model'] and
                    n['required_verdicts'] == {'scalar-37-full-screen':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'CM_type_and_inert_degree_vetoes_with_scoped_three_prime_CRT', 'full37 target veto node binding')
        elif n['id'] == 'off-reflection-third-prime-generic-gate':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['off-reflection-third-prime'] and
                    n['depends_on'] == ['inert-elliptic-projector-gate','scalar-reflection-quotient-decomposition'] and
                    n['required_verdicts'] == {'inert-elliptic-projector-gate':'constructed','scalar-reflection-quotient-decomposition':'constructed'} and
                    n['resolution_kind'] == 'prime37_exhaustive_CM_certificate_and_generic_Hom_rank_squeeze', 'third-prime generic node binding')
        elif n['id'] == 'third-prime-and-generic-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['off-reflection-third-prime'] and
                    n['depends_on'] == ['off-reflection-third-prime-generic-gate','even-axis-principal-model'] and
                    n['required_verdicts'] == {'off-reflection-third-prime-generic-gate':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'literal_residue_and_geometric_generic_CM_multiplicity_veto', 'third-prime generic target veto node binding')
        elif n['id'] == 'inert-elliptic-projector-gate':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['inert-elliptic-projector'] and
                    n['depends_on'] == ['off-reflection-two-prime-screen','even-axis-principal-model'] and
                    n['required_verdicts'] == {'off-reflection-two-prime-screen':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'integral_self_adjoint_inert_prime_elliptic_projector', 'inert projector node binding')
        elif n['id'] == 'inert-degree-parity-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['inert-elliptic-projector'] and
                    n['depends_on'] == ['inert-elliptic-projector-gate','indecomposable-principal-model'] and
                    n['required_verdicts'] == {'inert-elliptic-projector-gate':'constructed','indecomposable-principal-model':'constructed'} and
                    n['resolution_kind'] == 'conditional_axis_degree_and_fixed_sixfold_norm_parity_contradiction', 'inert norm veto node binding')
        elif n['id'] == 'off-reflection-two-prime-screen':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['off-reflection-joint-screen'] and
                    n['depends_on'] == ['off-reflection-a-line-screen','even-axis-principal-model'] and
                    n['required_verdicts'] == {'off-reflection-a-line-screen':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'two_prime_native_type_census_with_transverse_Weierstrass_chart', 'two-prime screen node binding')
        elif n['id'] == 'off-reflection-two-prime-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['off-reflection-joint-screen'] and
                    n['depends_on'] == ['off-reflection-two-prime-screen','indecomposable-principal-model'] and
                    n['required_verdicts'] == {'off-reflection-two-prime-screen':'constructed','indecomposable-principal-model':'constructed'} and
                    n['resolution_kind'] == 'CM_absence_and_End_field_signature_veto_with_scoped_CRT', 'two-prime target veto node binding')
        elif n['id'] == 'off-reflection-a-line-screen':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['off-reflection-a-line'] and
                    n['depends_on'] == ['scalar-reflection-quotient-decomposition','minimal-axis-second-prime-screen'] and
                    n['required_verdicts'] == {'scalar-reflection-quotient-decomposition':'constructed','minimal-axis-second-prime-screen':'constructed'} and
                    n['resolution_kind'] == 'complete_regular_a_line_CM_census_and_actual_a6_source', 'off-reflection a-line node binding')
        elif n['id'] == 'off-reflection-a-line-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['off-reflection-a-line'] and
                    n['depends_on'] == ['off-reflection-a-line-screen','even-axis-principal-model'] and
                    n['required_verdicts'] == {'off-reflection-a-line-screen':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'six_F13_CM_vetoes_and_twelve_algebraic_congruence_boxes', 'off-reflection target exclusion node binding')
        elif n['id'] == 'scalar-reflection-quotient-decomposition':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['scalar-reflection-decomposition'] and
                    n['depends_on'] == ['minimal-axis-scalar-source','even-axis-joint-degree-gate'] and
                    n['required_verdicts'] == {'minimal-axis-scalar-source':'constructed','even-axis-joint-degree-gate':'constructed'} and
                    n['resolution_kind'] == 'actual_reflection_quotient_Jacobians_and_degree256_source_isogeny', 'reflection decomposition node binding')
        elif n['id'] == 'reflection-symmetric-scalar-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['scalar-reflection-decomposition'] and
                    n['depends_on'] == ['scalar-reflection-quotient-decomposition','even-axis-principal-model'] and
                    n['required_verdicts'] == {'scalar-reflection-quotient-decomposition':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'complex_source_factor_dimensions_3_5_exclude_simple_target_sixfold', 'reflection target exclusion node binding')
        elif n['id'] == 'minimal-axis-second-prime-screen':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['minimal-axis-second-prime'] and
                    n['depends_on'] == ['minimal-axis-b-line-screen'] and
                    n['required_verdicts'] == {'minimal-axis-b-line-screen':'constructed'} and
                    n['resolution_kind'] == 'two_split_prime_Gaussian_reconstructions_with_unused_fifth_trace_controls', 'second-prime node binding')
        elif n['id'] == 'minimal-axis-b6-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['minimal-axis-second-prime'] and
                    n['depends_on'] == ['minimal-axis-second-prime-screen','even-axis-principal-model'] and
                    n['required_verdicts'] == {'minimal-axis-second-prime-screen':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'prime29_complete_CM_ratio_veto_and_faithful_Hom_specialization', 'b6 target exclusion node binding')
        elif n['id'] == 'minimal-axis-b-line-screen':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['minimal-axis-b-line'] and
                    n['depends_on'] == ['minimal-axis-scalar-source','minimal-axis-scalar-target-transplant'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'complete_regular_chart_b_line_CM_screen_congruence_exclusion_and_actual_rational_sources', 'b-line node binding')
        elif n['id'] == 'minimal-axis-scalar-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['minimal-axis-frobenius-obstruction'] and
                    n['depends_on'] == ['minimal-axis-scalar-source','even-axis-principal-model'] and
                    n['required_verdicts'] == {'minimal-axis-scalar-source':'constructed','even-axis-principal-model':'constructed'} and
                    n['resolution_kind'] == 'twisted_Frobenius_Gaussian_reconstruction_and_second_CM_factor_specialization_exclusion', 'minimal Frobenius node binding')
        elif n['id'] == 'minimal-axis-scalar-source':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['minimal-axis-scalar-source'] and
                    n['depends_on'] == ['even-axis-joint-degree-gate','eightfold-literature-and-secant-audit'] and
                    n['required_verdicts'] == {'even-axis-joint-degree-gate':'constructed','eightfold-literature-and-secant-audit':'constructed'} and
                    n['resolution_kind'] == 'explicit_anti_translation_elliptic_function_scalar_tower_and_primitive_theta4_axis', 'minimal source node binding')
        elif n['id'] == 'even-axis-joint-degree-gate':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['even-axis-joint-degree-gate'] and
                    n['depends_on'] == ['even-axis-principal-model','even-axis-coupled-kummer-gate'] and
                    n['required_verdicts'] == {'even-axis-principal-model':'constructed','even-axis-coupled-kummer-gate':'constructed'} and
                    n['resolution_kind'] == 'joint_map_Euler_obstruction_Torelli_and_degree_two_scalar_pullback_classification', 'joint-degree node binding')
        elif n['id'] == 'even-axis-coupled-kummer-gate':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['even-axis-coupled-kummer-gate'] and
                    n['depends_on'] == ['even-axis-principal-model','eightfold-literature-and-secant-audit'] and
                    n['required_verdicts'] == {'even-axis-principal-model':'constructed','eightfold-literature-and-secant-audit':'constructed'} and
                    n['resolution_kind'] == 'opposite_axis_common_cover_Kummer_product_and_conditional_reconstruction', 'coupled Kummer node binding')
        elif n['id'] == 'even-axis-principal-model':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['even-axis-principal-model'] and
                    n['depends_on'] == ['indecomposable-principal-model','y2-etale-cyclic-quartic-polarized-transplant','y2-two-branch-cyclic-quartic-transplant'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'four_Hadamard_blocks_even_elliptic_surface_and_phase_correct_cycle_transfer', 'even-axis node binding')
        elif n['id'] == 'y2-two-branch-cyclic-quartic-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['two-branch-odd-axis-obstruction'] and
                    n['depends_on'] == ['y2-etale-cyclic-quartic-polarized-transplant','indecomposable-principal-model','ramified-trigonal-auxiliary-family'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'two_fixed_points_and_local_tangent_characters_exclude_degree_six', 'two-branch node binding')
        elif n['id'] == 'y2-etale-cyclic-quartic-polarized-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['cyclic-prym-odd-axis-obstruction'] and
                    n['depends_on'] == ['indecomposable-principal-model','equivariant-tetragonal-gate','ramified-trigonal-principal-target-transplant'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'intrinsic_elliptic_axes_and_free_C4_fixed_fibre_degree_obstruction', 'odd-axis node binding')
        elif n['id'] == 'ramified-trigonal-principal-target-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['trigonal-principal-match-obstruction'] and
                    n['depends_on'] == ['ramified-trigonal-auxiliary-family','equivariant-tetragonal-gate','cyclic-quartic-prym-transplant'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'CS_unique_low_genus_quotient_forces_excluded_primitive_sixfold', 'principal match node binding')
        elif n['id'] == 'ramified-trigonal-auxiliary-family':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['ramified-trigonal-family'] and
                    n['depends_on'] == ['eightfold-literature-and-secant-audit','equivariant-tetragonal-gate'] and
                    n['required_verdicts'] == {'eightfold-literature-and-secant-audit':'constructed','equivariant-tetragonal-gate':'constructed'} and
                    n['resolution_kind'] == 'geometric_auxiliary_cover_existence_and_explicit_C4_equivariant_trigonal_construction', 'ramified family node binding')
        elif n['id'] == 'eightfold-secant-weak-criterion-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['secant-criterion-persistence'] and
                    n['depends_on'] == ['secant-source-weak-semiregularity-transplant','secant-local-ext-gate'] and
                    n['required_verdicts'] == SCOPED_REJECTION_INPUTS[n['id']] and
                    n['resolution_kind'] == 'Kunneth_Hochschild_naturality_and_finite_etale_isogeny_persistence', 'persistence node binding')
        elif n['id'] == 'secant-source-weak-semiregularity-transplant':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['secant-source-semiregularity'] and
                    n['depends_on'] == ['secant-local-ext-gate','eightfold-literature-and-secant-audit'] and
                    n['required_verdicts'] == {'secant-local-ext-gate':'constructed','eightfold-literature-and-secant-audit':'constructed'} and
                    n['resolution_kind'] == 'compensated_bivector_annihilator_and_nonzero_local_Atiyah_evaluation', 'source semiregularity node binding')
        elif n['id'] == 'secant-local-ext-gate':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['secant-local-ext-gate'] and
                    n['depends_on'] == ['eightfold-literature-and-secant-audit'] and
                    n['required_verdicts'] == {'eightfold-literature-and-secant-audit':'constructed'} and
                    n['resolution_kind'] == 'conditional_incidence_normalization_cohomology_and_local_Ext_modules', 'local Ext node binding')
        elif n['id'] == 'eightfold-literature-and-secant-audit':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['eightfold-literature-audit'] and
                    n['depends_on'] == ['split-eightfold-stabilization','indecomposable-principal-model'] and
                    n['required_verdicts'] == {'split-eightfold-stabilization':'constructed','indecomposable-principal-model':'constructed'} and
                    n['resolution_kind'] == 'primary_source_scope_and_corrected_secant_character_audit', 'eightfold literature node binding')
        elif n['id'] == 'packet-coherence-dictionary':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and
                    n['evidence'] == ['cycle-packet-dictionary'] and
                    n['resolution_kind'] == 'cycle_supplied_fundamental_chain_dictionary_and_necessity_lemma', 'dictionary result binding')
        elif n['id'] == 'bare-chain-closure-obstruction':
            require(n['status'] == 'resolved' and n['verdict'] == 'rejected' and
                    n['evidence'] == ['cycle-packet-dictionary'] and
                    n['resolution_kind'] == 'topological_chain_closure_is_universal_not_algebraicity_detector', 'closure-only rejection binding')
        else:
            require(n['status'] == n['verdict'] == 'open' and n['evidence'] == [], 'unreviewed research resolution')
            require(n['next_action'] and n['deliverable'], 'empty research task')
    expected_assembly = {'candidate-hodge-membership', 'cohomology-descent', 'rational-survival',
                         'all-algebraic-cycles-annihilation', 'candidate-obstruction-nonzero'}
    require(set(by['counterexample-assembly']['depends_on']) == expected_assembly and
            by['counterexample-assembly']['requires'] == ['independent-counterexample-review'], 'counterexample assembly bypass')
    require(by['obstruction-construction']['rejected_candidate_controls'] ==
            ['bare-chain-closure-obstruction', 'uniform-weil-projector-annihilation'], 'rejected candidate history lost')
    require(by['algebraic-witness-search']['bounded_attempts'] == ['tautological-power-witness-search', 'secant-sheaf-transplant', 'cyclic-quartic-prym-transplant', 'principal-prym-membership-audit', 'y2-jacobian-low-gonality-transplant', 'hyperelliptic-bottom-prym-transplant', 'bielliptic-involution-lift-transplant', 'commuting-prym-factor-transplant', 'inversion-symmetric-scalar-transplant', 'asymmetric-scalar-target-transplant', 'scalar-polarized-prym-transplant', 'nonlifting-polarized-prym-transplant', 'secant-source-weak-semiregularity-transplant', 'eightfold-secant-weak-criterion-transplant', 'ramified-trigonal-principal-target-transplant', 'y2-etale-cyclic-quartic-polarized-transplant', 'y2-two-branch-cyclic-quartic-transplant', 'minimal-axis-scalar-target-transplant', 'minimal-axis-b6-target-transplant', 'reflection-symmetric-scalar-target-transplant', 'off-reflection-a-line-target-transplant', 'off-reflection-two-prime-target-transplant', 'inert-degree-parity-target-transplant', 'third-prime-and-generic-target-transplant', 'scalar-37-typed-polarized-target-transplant'], 'bounded witness history lost')
    require(by['algebraic-witness-search']['structural_progress'] == ['secant-local-ext-gate', 'eightfold-literature-and-secant-audit', 'generic-middle-hodge-kernel', 'split-eightfold-stabilization', 'eightfold-weil-filter', 'eightfold-full-hodge-kernel', 'higher-chern-witness-transfer', 'reflexive-rank-reduction', 'gaussian-principal-isogeny', 'indecomposable-principal-model', 'asymmetric-scalar-cover-control', 'asymmetric-cover-automorphisms', 'asymmetric-prym-frobenius7', 'scalar-family-localization', 'equivariant-tetragonal-gate', 'ramified-trigonal-auxiliary-family', 'even-axis-principal-model', 'even-axis-coupled-kummer-gate', 'even-axis-joint-degree-gate', 'minimal-axis-scalar-source', 'minimal-axis-b-line-screen', 'minimal-axis-second-prime-screen', 'scalar-reflection-quotient-decomposition', 'off-reflection-a-line-screen', 'off-reflection-two-prime-screen', 'inert-elliptic-projector-gate', 'off-reflection-third-prime-generic-gate', 'scalar-37-full-screen'], 'middle Hodge progress lost')
    require(c['available_external_witnesses'] == [], 'unreviewed external witness')
    direction_policy = validate_direction(c)
    frontier = [n['id'] for n in c['conjectures'] if n['status'] == 'open' and n['id'] in direction_policy['active_refutation_nodes'] and
                all(by[d]['status'] == 'resolved' and by[d]['verdict'] == n['required_verdicts'][d] for d in n['depends_on']) and
                set(n['requires']) <= set(c['available_external_witnesses'])]
    require(frontier == c['frontier']['entry_nodes'] and c['frontier']['recommended_start'] in frontier,
            'stale or blocked frontier')
    require(c['frontier']['parent_formulation_is_not_a_blocker'] is True, 'parent improperly blocks local research')

    require(a['schema'] == 'marici.hodge-foundational-attachments.v1' and a['work_net'] == CONTRACT and
            c['attachment_model'] == ATTACHMENTS, 'attachment identity')
    require(a['contracts'] == {'hodge': CONTRACT, 'parent': HOME + 'contracts/common-foundations-conjecture-net.v1.json',
            'math': HOME + 'contracts/mathematical-realization-conjecture-net.v1.json',
            'identity': HOME + 'contracts/witnessed-constructive-identity.proposed.v1.json'}, 'main contract references')
    require(all(v is False for v in a['boundary'].values()), 'cross-net implication promotion')
    require(c['main_net']['contract'] == a['contracts']['identity'] and
            c['main_net']['node'] == refs['identity']['root']['id'], 'wrong main conjecture net')
    index = a['reciprocal_index']
    require(index == {'contract': a['contracts']['identity'], 'field': 'research_branches', 'id': 'hodge-coherence-obstruction'}, 'reciprocal index')
    back = [b for b in refs['identity'].get(index['field'], []) if b['id'] == index['id']]
    require(len(back) == 1 and back[0]['contract'] == CONTRACT and back[0]['node'] == 'packet-coherence-dictionary' and
            back[0]['attachment_model'] == ATTACHMENTS and back[0]['proof_bearing'] is False and
            back[0]['discharges_parent'] is False and back[0]['outcome'] is None, 'missing/promoted main-net backlink')
    require(any(entry['contract'] == CONTRACT and entry['id'] == c['id'] for entry in registry['nets']), 'net not registered')
    require(any(entry['contract'] == ATTACHMENTS for entry in registry['nets']), 'attachment not registered')
    artifact = {item['id']: item for item in c['artifacts']}
    require(len(artifact) == len(c['artifacts']) == 52 and set(artifact) == {'scalar-37-census', 'off-reflection-third-prime', 'inert-elliptic-projector', 'off-reflection-joint-screen', 'off-reflection-a-line', 'scalar-reflection-decomposition', 'minimal-axis-second-prime', 'minimal-axis-b-line', 'minimal-axis-frobenius-obstruction', 'minimal-axis-scalar-source', 'even-axis-joint-degree-gate', 'even-axis-coupled-kummer-gate', 'even-axis-principal-model', 'two-branch-odd-axis-obstruction', 'cyclic-prym-odd-axis-obstruction', 'trigonal-principal-match-obstruction', 'ramified-trigonal-family', 'secant-criterion-persistence', 'secant-source-semiregularity', 'secant-local-ext-gate', 'eightfold-literature-audit', 'control-bundle', 'cycle-map-scope', 'cycle-packet-dictionary', 'literature-boundary-audit', 'explicit-sixfold-candidate', 'weil-projector', 'tautological-witness-search', 'middle-hodge-kernel', 'secant-sheaf-transplant', 'split-eightfold-stabilization', 'eightfold-weil-filter', 'eightfold-hodge-kernel', 'chern-witness-transfer', 'reflexive-rank-reduction', 'cyclic-quartic-prym-audit', 'gaussian-principal-isogeny', 'principal-prym-membership-audit', 'indecomposable-principal-model', 'y2-curve-audit', 'hyperelliptic-bottom-audit', 'bielliptic-lift-audit', 'commuting-prym-audit', 'even-scalar-cover', 'asymmetric-scalar-cover', 'asymmetric-reflections', 'asymmetric-frobenius', 'asymmetric-absolute', 'scalar-family-localization', 'scalar-polarized-obstruction', 'nonlifting-polarized-obstruction', 'equivariant-tetragonal-gate'}, 'artifact census')
    control = artifact['control-bundle']
    require(control['contract'] == HOME + 'contracts/hodge-control-fixtures.v1.json' and
            control['checker'] == 'research/voevodsky/checkers/check_hodge_obstruction_controls.py' and
            control['receipt'] == 'research/voevodsky/results/hodge-obstruction-controls-v1.json', 'control artifact binding')
    scope = artifact['cycle-map-scope']
    require(scope['contract'] == HOME + 'contracts/hodge-cycle-map-scope.v1.json' and
            scope['note'] == 'research/voevodsky/hodge-cycle-map-scope-v1.md' and
            scope['checker'] == 'research/voevodsky/checkers/check_hodge_cycle_map_scope.py' and
            scope['receipt'] == 'research/voevodsky/results/hodge-cycle-map-scope-v1.json', 'scope artifact binding')
    dictionary = artifact['cycle-packet-dictionary']
    require(dictionary['contract'] == HOME + 'contracts/hodge-cycle-packet-dictionary.v1.json' and
            dictionary['note'] == 'research/voevodsky/hodge-cycle-packet-dictionary-v1.md' and
            dictionary['checker'] == 'research/voevodsky/checkers/check_hodge_cycle_packet_dictionary.py' and
            dictionary['receipt'] == 'research/voevodsky/results/hodge-cycle-packet-dictionary-v1.json', 'dictionary artifact binding')
    checked_dictionary = load(dictionary['receipt'])
    require(checked_dictionary == dictionary_report() and checked_dictionary['passed'] and
            all(checked_dictionary['checks'].values()), 'dictionary receipt stale or altered')
    require(checked_dictionary['bare_chain_closure_candidate_verdict'] == 'rejected' and
            not any(checked_dictionary[k] for k in ('full_algebraic_packet_source_generated',
            'general_higher_coherence_constructed', 'specific_hodge_obstruction_constructed', 'Hodge_proved', 'Hodge_refuted')), 'dictionary theorem promoted')
    audit = artifact['literature-boundary-audit']
    require(audit['contract'] == HOME + 'contracts/hodge-literature-boundary-audit.v1.json' and
            audit['note'] == 'research/voevodsky/hodge-literature-boundary-audit-v1.md' and
            audit['checker'] == 'research/voevodsky/checkers/check_hodge_literature_boundary_audit.py' and
            audit['receipt'] == 'research/voevodsky/results/hodge-literature-boundary-audit-v1.json', 'literature artifact binding')
    checked_audit = load(audit['receipt'])
    require(checked_audit == audit_report() and checked_audit['passed'] and
            all(checked_audit['checks'].values()), 'literature receipt stale or altered')
    require(not any(checked_audit[k] for k in ('specific_candidate_selected', 'specific_alpha_selected',
            'Hodge_proved', 'Hodge_refuted', 'nonalgebraicity_established',
            'global_exhaustive_literature_status_certified')), 'literature audit promoted')
    require(c['scope']['audit_recommended_window'] == {'dimension': 6, 'codimension': 3,
            'family': checked_audit['recommended_family'], 'status': 'shortlist_only_not_selected_target'}, 'shortlist promoted to target')
    candidate = artifact['explicit-sixfold-candidate']
    require(candidate['contract'] == HOME + 'contracts/hodge-explicit-sixfold-candidate.v1.json' and
            candidate['note'] == 'research/voevodsky/hodge-explicit-sixfold-candidate-v1.md' and
            candidate['checker'] == 'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py' and
            candidate['receipt'] == 'research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json', 'candidate artifact binding')
    checked_candidate = load(candidate['receipt'])
    require(checked_candidate == candidate_report() and checked_candidate['passed'] and
            all(checked_candidate['checks'].values()), 'candidate receipt stale or altered')
    require(checked_candidate['candidate_id'] == candidate_id and
            all(checked_candidate[k] is True for k in ('specific_candidate_selected', 'specific_alpha_selected',
            'alpha_rational_hodge_membership_proved', 'divisor_product_nonmembership_proved')) and
            not any(checked_candidate[k] for k in ('Hodge_proved', 'Hodge_refuted',
            'alpha_nonalgebraic_proved', 'class_obstruction_constructed')), 'candidate result promoted or unbound')
    projector = artifact['weil-projector']
    require(projector['contract'] == HOME + 'contracts/hodge-weil-projector.v1.json' and
            projector['note'] == 'research/voevodsky/hodge-weil-projector-v1.md' and
            projector['checker'] == 'research/voevodsky/checkers/check_hodge_weil_projector.py' and
            projector['receipt'] == 'research/voevodsky/results/hodge-weil-projector-v1.json', 'projector artifact binding')
    checked_projector = load(projector['receipt'])
    require(checked_projector == projector_report() and checked_projector['passed'] and
            all(checked_projector['checks'].values()), 'projector receipt stale or altered')
    require(checked_projector['candidate_id'] == candidate_id and
            all(checked_projector[k] is True for k in ('candidate_map_constructed', 'cohomology_descent_proved',
            'rational_survival_proved', 'candidate_value_nonzero_proved', 'preserves_algebraic_cycle_classes')) and
            not any(checked_projector[k] for k in ('validated_hodge_obstruction', 'all_cycle_annihilation_proved',
            'alpha_nonalgebraic_proved', 'algebraic_representative_of_alpha_constructed', 'Hodge_proved', 'Hodge_refuted')),
            'candidate projector promoted to annihilator')
    require(checked_projector['uniform_annihilation_candidate_verdict'] == 'rejected', 'uniform failure lost')
    search = artifact['tautological-witness-search']
    require(search['contract'] == HOME + 'contracts/hodge-tautological-witness-search.v1.json' and
            search['note'] == 'research/voevodsky/hodge-tautological-witness-search-v1.md' and
            search['checker'] == 'research/voevodsky/checkers/check_hodge_tautological_witness_search.py' and
            search['receipt'] == 'research/voevodsky/results/hodge-tautological-witness-search-v1.json', 'witness search artifact binding')
    checked_search = load(search['receipt'])
    require(checked_search == search_report() and checked_search['passed'] and
            all(checked_search['checks'].values()), 'witness search receipt stale or altered')
    require(checked_search['candidate_id'] == candidate_id and checked_search['verdict'] == 'rejected' and
            checked_search['node'] == 'tautological-power-witness-search' and
            checked_search['bounded_library_excluded'] is True and
            checked_search['End0_dimension_from_written_genericity_proof'] == 2 and
            checked_search['finite_search_count'] == 43 and checked_search['nonzero_Weil_projection_count'] == 0 and
            not any(checked_search[k] for k in ('global_algebraic_witness_search_completed',
            'all_cycle_annihilation_proved', 'alpha_nonalgebraic_proved',
            'algebraic_representative_of_alpha_constructed', 'Hodge_proved', 'Hodge_refuted')), 'bounded search promoted')
    kernel = artifact['middle-hodge-kernel']
    require(kernel['contract'] == HOME + 'contracts/hodge-middle-hodge-kernel.v1.json' and
            kernel['note'] == 'research/voevodsky/hodge-middle-hodge-kernel-v1.md' and
            kernel['checker'] == 'research/voevodsky/checkers/check_hodge_middle_hodge_kernel.py' and
            kernel['receipt'] == 'research/voevodsky/results/hodge-middle-hodge-kernel-v1.json', 'kernel artifact binding')
    checked_kernel = load(kernel['receipt'])
    require(checked_kernel == kernel_report() and checked_kernel['passed'] and
            all(checked_kernel['checks'].values()), 'Hodge kernel receipt stale or altered')
    require(checked_kernel['candidate_id'] == candidate_id and checked_kernel['verdict'] == 'constructed' and
            checked_kernel['node'] == 'generic-middle-hodge-kernel' and
            checked_kernel['rational_Hodge_dimension_from_written_genericity_proof'] == 3 and
            checked_kernel['Chow_idempotent_constructed'] is True and
            checked_kernel['full_H6_anti_i_projector_rank'] == 452 and
            not any(checked_kernel[k] for k in ('nonzero_homological_anti_i_cycle_constructed',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'alpha_nonalgebraic_proved', 'Hodge_proved', 'Hodge_refuted')), 'Hodge kernel promoted to cycle theorem')
    transplant = artifact['secant-sheaf-transplant']
    require(transplant['contract'] == HOME + 'contracts/hodge-secant-sheaf-transplant.v1.json' and
            transplant['note'] == 'research/voevodsky/hodge-secant-sheaf-transplant-v1.md' and
            transplant['checker'] == 'research/voevodsky/checkers/check_hodge_secant_sheaf_transplant.py' and
            transplant['receipt'] == 'research/voevodsky/results/hodge-secant-sheaf-transplant-v1.json', 'transplant artifact binding')
    checked_transplant = load(transplant['receipt'])
    require(checked_transplant == transplant_report() and checked_transplant['passed'] and
            all(checked_transplant['checks'].values()), 'secant transplant receipt stale or altered')
    require(checked_transplant['candidate_id'] == candidate_id and checked_transplant['verdict'] == 'rejected' and
            checked_transplant['node'] == 'secant-sheaf-transplant' and
            checked_transplant['retained_split_theorem_excluded_on_all_repolarized_Qi_isogeny_models'] is True and
            not any(checked_transplant[k] for k in ('retained_theorem_applicable_to_fixed_isogeny_class',
            'algebraic_representative_of_alpha_constructed', 'alpha_nonalgebraic_proved',
            'all_cycle_annihilation_proved', 'all_sheaf_routes_excluded', 'global_witness_search_completed',
            'Hodge_proved', 'Hodge_refuted')), 'transplant rejection promoted')
    stabilization = artifact['split-eightfold-stabilization']
    require(stabilization['contract'] == HOME + 'contracts/hodge-split-eightfold-stabilization.v1.json' and
            stabilization['note'] == 'research/voevodsky/hodge-split-eightfold-stabilization-v1.md' and
            stabilization['checker'] == 'research/voevodsky/checkers/check_hodge_split_eightfold_stabilization.py' and
            stabilization['receipt'] == 'research/voevodsky/results/hodge-split-eightfold-stabilization-v1.json', 'stabilization artifact binding')
    checked_stabilization = load(stabilization['receipt'])
    require(checked_stabilization == stabilization_report() and checked_stabilization['passed'] and
            all(checked_stabilization['checks'].values()), 'stabilization receipt stale or altered')
    require(checked_stabilization['candidate_id'] == candidate_id and checked_stabilization['verdict'] == 'constructed' and
            checked_stabilization['node'] == 'split-eightfold-stabilization' and
            checked_stabilization['specified_W8_algebraicity_equivalent_to_alpha_algebraicity'] is True and
            checked_stabilization['full_H8_retraction_image_projector_rank'] == 924 and
            not any(checked_stabilization[k] for k in ('nonzero_algebraic_W8_class_constructed',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'alpha_nonalgebraic_proved', 'sixfold_theorem_applied_to_A', 'Hodge_proved', 'Hodge_refuted')), 'stabilization reduction promoted')
    eightfold_filter = artifact['eightfold-weil-filter']
    require(eightfold_filter['contract'] == HOME + 'contracts/hodge-eightfold-weil-filter.v1.json' and
            eightfold_filter['note'] == 'research/voevodsky/hodge-eightfold-weil-filter-v1.md' and
            eightfold_filter['checker'] == 'research/voevodsky/checkers/check_hodge_eightfold_weil_filter.py' and
            eightfold_filter['receipt'] == 'research/voevodsky/results/hodge-eightfold-weil-filter-v1.json', 'eightfold filter artifact binding')
    checked_filter = load(eightfold_filter['receipt'])
    require(checked_filter == eightfold_filter_report() and checked_filter['passed'] and
            all(checked_filter['checks'].values()), 'eightfold filter receipt stale or altered')
    require(checked_filter['candidate_id'] == candidate_id and checked_filter['verdict'] == 'constructed' and
            checked_filter['node'] == 'eightfold-weil-filter' and
            checked_filter['cycle_preserving_filtered_reverse_constructed'] is True and
            checked_filter['rational_Weil_projector_rank'] == 2 and
            checked_filter['source_intertwiner_basis_count'] == 924 and
            not any(checked_filter[k] for k in ('nonzero_algebraic_W8_class_constructed',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'alpha_nonalgebraic_proved', 'Chow_idempotence_claimed', 'Hodge_proved', 'Hodge_refuted')), 'eightfold filter promoted')
    eightfold_kernel = artifact['eightfold-hodge-kernel']
    require(eightfold_kernel['contract'] == HOME + 'contracts/hodge-eightfold-hodge-kernel.v1.json' and
            eightfold_kernel['note'] == 'research/voevodsky/hodge-eightfold-hodge-kernel-v1.md' and
            eightfold_kernel['checker'] == 'research/voevodsky/checkers/check_hodge_eightfold_hodge_kernel.py' and
            eightfold_kernel['receipt'] == 'research/voevodsky/results/hodge-eightfold-hodge-kernel-v1.json', 'eightfold Hodge artifact binding')
    checked_eightfold = load(eightfold_kernel['receipt'])
    require(checked_eightfold == eightfold_kernel_report() and checked_eightfold['passed'] and
            all(checked_eightfold['checks'].values()), 'eightfold Hodge receipt stale or altered')
    require(checked_eightfold['candidate_id'] == candidate_id and checked_eightfold['verdict'] == 'constructed' and
            checked_eightfold['node'] == 'eightfold-full-hodge-kernel' and
            checked_eightfold['complete_exceptional_cycle_test_constructed'] is True and
            checked_eightfold['Chow_idempotent_constructed'] is True and
            checked_eightfold['rational_Hdg4_dimension'] == 14 and
            checked_eightfold['full_H8_Chow_idempotent_image_rank'] == 1808 and
            checked_eightfold['full_H8_exceptional_projector_rank'] == 8 and
            not any(checked_eightfold[k] for k in ('nonzero_algebraic_exceptional_class_constructed',
            'algebraic_dimension_decided', 'algebraic_representative_of_alpha_constructed',
            'all_cycle_annihilation_proved', 'alpha_nonalgebraic_proved', 'Hodge_proved', 'Hodge_refuted')), 'eightfold Hodge result promoted')
    chern_transfer = artifact['chern-witness-transfer']
    require(chern_transfer['contract'] == HOME + 'contracts/hodge-chern-witness-transfer.v1.json' and
            chern_transfer['note'] == 'research/voevodsky/hodge-chern-witness-transfer-v1.md' and
            chern_transfer['checker'] == 'research/voevodsky/checkers/check_hodge_chern_witness_transfer.py' and
            chern_transfer['receipt'] == 'research/voevodsky/results/hodge-chern-witness-transfer-v1.json', 'Chern transfer artifact binding')
    checked_chern = load(chern_transfer['receipt'])
    require(checked_chern == chern_transfer_report() and checked_chern['passed'] and
            all(checked_chern['checks'].values()), 'Chern transfer receipt stale or altered')
    require(checked_chern['candidate_id'] == candidate_id and checked_chern['verdict'] == 'constructed' and
            checked_chern['node'] == 'higher-chern-witness-transfer' and
            checked_chern['conditional_bundle_transfer_constructed'] is True and
            checked_chern['normalized_fourth_existence_equivalent_to_alpha_algebraicity'] is True and
            not any(checked_chern[k] for k in ('nonzero_Weil_bundle_constructed',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'alpha_nonalgebraic_proved', 'equivalence_branch_decided', 'all_reflexive_sheaf_routes_excluded',
            'Hodge_proved', 'Hodge_refuted')), 'Chern transfer result promoted')
    reduction = artifact['reflexive-rank-reduction']
    require(reduction['contract'] == HOME + 'contracts/hodge-reflexive-rank-reduction.v1.json' and
            reduction['note'] == 'research/voevodsky/hodge-reflexive-rank-reduction-v1.md' and
            reduction['checker'] == 'research/voevodsky/checkers/check_hodge_reflexive_rank_reduction.py' and
            reduction['receipt'] == 'research/voevodsky/results/hodge-reflexive-rank-reduction-v1.json', 'reflexive reduction artifact binding')
    checked_reduction = load(reduction['receipt'])
    require(checked_reduction == reduction_report() and checked_reduction['passed'] and
            all(checked_reduction['checks'].values()), 'reflexive reduction receipt stale or altered')
    require(checked_reduction['candidate_id'] == candidate_id and checked_reduction['verdict'] == 'constructed' and
            checked_reduction['node'] == 'reflexive-rank-reduction' and
            checked_reduction['conditional_rank_reduction_constructed'] is True and
            checked_reduction['rank_two_reflexive_witness_existence_equivalent_to_alpha_algebraicity'] is True and
            checked_reduction['smooth_threefold_witness_existence_equivalent_to_alpha_algebraicity'] is True and
            not any(checked_reduction[k] for k in ('nonzero_Weil_reflexive_sheaf_constructed',
            'nonzero_Weil_smooth_threefold_constructed', 'algebraic_representative_of_alpha_constructed',
            'all_cycle_annihilation_proved', 'alpha_nonalgebraic_proved', 'positive_branch_decided',
            'Hodge_proved', 'Hodge_refuted')), 'reflexive reduction result promoted')
    prym = artifact['cyclic-quartic-prym-audit']
    require(prym['contract'] == HOME + 'contracts/hodge-cyclic-prym-audit.v1.json' and
            prym['note'] == 'research/voevodsky/hodge-cyclic-prym-audit-v1.md' and
            prym['checker'] == 'research/voevodsky/checkers/check_hodge_cyclic_prym_audit.py' and
            prym['receipt'] == 'research/voevodsky/results/hodge-cyclic-prym-audit-v1.json', 'cyclic Prym artifact binding')
    checked_prym = load(prym['receipt'])
    require(checked_prym == prym_report() and checked_prym['passed'] and all(checked_prym['checks'].values()),
            'cyclic Prym receipt stale or altered')
    require(checked_prym['candidate_id'] == candidate_id and checked_prym['verdict'] == 'rejected' and
            checked_prym['node'] == 'cyclic-quartic-prym-transplant' and
            checked_prym['cyclic_quartic_primitive_Prym_presentation_excluded_on_fixed_Qi_isogeny_class'] is True and
            not any(checked_prym[k] for k in ('all_Prym_presentations_excluded', 'eightfold_A_excluded',
            'global_witness_search_completed', 'all_cycle_annihilation_proved',
            'algebraic_representative_of_alpha_constructed', 'alpha_nonalgebraic_proved',
            'Hodge_proved', 'Hodge_refuted')), 'cyclic Prym result promoted')
    principal = artifact['gaussian-principal-isogeny']
    require(principal['contract'] == HOME + 'contracts/hodge-gaussian-principal-isogeny.v1.json' and
            principal['note'] == 'research/voevodsky/hodge-gaussian-principal-isogeny-v1.md' and
            principal['checker'] == 'research/voevodsky/checkers/check_hodge_gaussian_principal_isogeny.py' and
            principal['receipt'] == 'research/voevodsky/results/hodge-gaussian-principal-isogeny-v1.json', 'principal isogeny artifact binding')
    checked_principal = load(principal['receipt'])
    require(checked_principal == principal_isogeny_report() and checked_principal['passed'] and
            all(checked_principal['checks'].values()), 'principal isogeny receipt stale or altered')
    require(checked_principal['candidate_id'] == candidate_id and checked_principal['verdict'] == 'constructed' and
            checked_principal['node'] == 'gaussian-principal-isogeny' and
            checked_principal['actual_principal_Gaussian_eightfold_constructed'] is True and
            checked_principal['algebraicity_test_transported_by_actual_isogeny'] is True and
            checked_principal['quotient_degree'] == 9 and checked_principal['Weil_pullback_factor'] == 3 and
            not any(checked_principal[k] for k in ('Prym_cover_constructed', 'nonzero_algebraic_Weil_class_constructed',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'alpha_nonalgebraic_proved', 'Hodge_proved', 'Hodge_refuted')), 'principal isogeny result promoted')
    membership = artifact['principal-prym-membership-audit']
    require(membership['contract'] == HOME + 'contracts/hodge-principal-prym-membership.v1.json' and
            membership['note'] == 'research/voevodsky/hodge-principal-prym-membership-v1.md' and
            membership['checker'] == 'research/voevodsky/checkers/check_hodge_principal_prym_membership.py' and
            membership['receipt'] == 'research/voevodsky/results/hodge-principal-prym-membership-v1.json', 'principal Prym artifact binding')
    checked_membership = load(membership['receipt'])
    require(checked_membership == principal_prym_report() and checked_membership['passed'] and
            all(checked_membership['checks'].values()), 'principal Prym receipt stale or altered')
    require(checked_membership['candidate_id'] == candidate_id and checked_membership['verdict'] == 'rejected' and
            checked_membership['node'] == 'principal-prym-membership-audit' and
            checked_membership['fixed_theta_Y_smooth_etale_Prym_presentation_excluded'] is True and
            checked_membership['all_four_fixed_polarization_Gaussian_principal_quotients_excluded_as_smooth_etale_Pryms'] is True and
            not any(checked_membership[k] for k in ('all_Prym_presentations_excluded', 'ramified_Pryms_excluded',
            'singular_admissible_covers_excluded', 'all_isogenous_principal_models_excluded',
            'other_polarizations_excluded', 'other_Gaussian_embeddings_excluded',
            'Hodge_proved', 'Hodge_refuted', 'alpha_nonalgebraic_proved',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'global_witness_search_completed')), 'principal Prym result promoted')
    indecomposable = artifact['indecomposable-principal-model']
    require(indecomposable['contract'] == HOME + 'contracts/hodge-indecomposable-principal-model.v1.json' and
            indecomposable['note'] == 'research/voevodsky/hodge-indecomposable-principal-model-v1.md' and
            indecomposable['checker'] == 'research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py' and
            indecomposable['receipt'] == 'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json', 'indecomposable model artifact binding')
    checked_indecomposable = load(indecomposable['receipt'])
    require(checked_indecomposable == indecomposable_report() and checked_indecomposable['passed'] and
            all(checked_indecomposable['checks'].values()), 'indecomposable model receipt stale or altered')
    require(checked_indecomposable['candidate_id'] == candidate_id and checked_indecomposable['verdict'] == 'constructed' and
            checked_indecomposable['node'] == 'indecomposable-principal-model' and
            checked_indecomposable['actual_principal_Gaussian_model_constructed'] is True and
            checked_indecomposable['principal_polarization_indecomposable'] is True and
            checked_indecomposable['Gaussian_composite_determinant'] == [0,48] and
            checked_indecomposable['elliptic_axis_polarization_degrees'] == [2,3] and
            not any(checked_indecomposable[k] for k in ('Prym_cover_constructed', 'Prym_presentation_excluded',
            'Mumford_product_crossing_argument_reused', 'theta_singular_locus_dimension_computed',
            'Chow_retraction_claimed', 'transported_filter_Chow_idempotence_claimed',
            'Hodge_proved', 'Hodge_refuted', 'alpha_nonalgebraic_proved',
            'algebraic_representative_of_alpha_constructed', 'nonzero_algebraic_Weil_class_constructed',
            'all_cycle_annihilation_proved')), 'indecomposable model result promoted')
    curve = artifact['y2-curve-audit']
    require(curve['contract'] == HOME + 'contracts/hodge-y2-curve-audit.v1.json' and
            curve['note'] == 'research/voevodsky/hodge-y2-curve-audit-v1.md' and
            curve['checker'] == 'research/voevodsky/checkers/check_hodge_y2_curve_audit.py' and
            curve['receipt'] == 'research/voevodsky/results/hodge-y2-curve-audit-v1.json', 'Y2 curve artifact binding')
    checked_curve = load(curve['receipt'])
    require(checked_curve == y2_curve_report() and checked_curve['passed'] and
            all(checked_curve['checks'].values()), 'Y2 curve receipt stale or altered')
    require(checked_curve['candidate_id'] == candidate_id and checked_curve['verdict'] == 'rejected' and
            checked_curve['node'] == 'y2-jacobian-low-gonality-transplant' and
            checked_curve['fixed_principal_Y2_Jacobian_presentation_excluded'] is True and
            checked_curve['hyperelliptic_genus9_smooth_etale_Prym_base_excluded'] is True and
            checked_curve['trigonal_genus9_intermediate_cyclic_quartic_tower_excluded'] is True and
            checked_curve['actual_theta_singularity_dimension'] is None and
            not any(checked_curve[k] for k in ('all_smooth_etale_Prym_presentations_of_Y2_excluded',
            'all_isogenous_Jacobians_excluded', 'other_polarizations_excluded', 'ramified_Pryms_excluded',
            'singular_admissible_covers_excluded', 'genus5_base_excluded_by_this_argument',
            'theta_singularity_dimension_computed', 'conditional_biellipticity_is_unconditional',
            'all_cycles_reflection_invariant', 'reflection_anti_invariance_is_exceptional_test',
            'Hodge_proved', 'Hodge_refuted', 'alpha_nonalgebraic_proved',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'global_witness_search_completed')), 'Y2 curve result promoted')
    bottom = artifact['hyperelliptic-bottom-audit']
    require(bottom['contract'] == HOME + 'contracts/hodge-hyperelliptic-bottom-audit.v1.json' and
            bottom['note'] == 'research/voevodsky/hodge-hyperelliptic-bottom-audit-v1.md' and
            bottom['checker'] == 'research/voevodsky/checkers/check_hodge_hyperelliptic_bottom_audit.py' and
            bottom['receipt'] == 'research/voevodsky/results/hodge-hyperelliptic-bottom-audit-v1.json', 'bottom-cover artifact binding')
    checked_bottom = load(bottom['receipt'])
    require(checked_bottom == bottom_report() and checked_bottom['passed'] and
            all(checked_bottom['checks'].values()), 'bottom-cover receipt stale or altered')
    require(checked_bottom['candidate_id'] == candidate_id and checked_bottom['verdict'] == 'rejected' and
            checked_bottom['node'] == 'hyperelliptic-bottom-prym-transplant' and
            checked_bottom['hyperelliptic_genus5_bottom_excluded_up_to_isogeny_to_fixed_A'] is True and
            checked_bottom['all_fixed_A_isogeny_models_excluded_for_this_cover_family'] is True and
            checked_bottom['actual_theta_singularity_dimension'] is None and
            not any(checked_bottom[k] for k in ('nonhyperelliptic_bottoms_excluded', 'ramified_covers_excluded',
            'singular_admissible_covers_excluded', 'all_Prym_presentations_excluded',
            'square_is_a_principal_product_claimed', 'actual_fourfold_for_target_constructed',
            'actual_cover_matching_Y2_constructed', 'theta_dimension_computed',
            'bielliptic_branch_is_unconditional', 'formal_root_pairs_are_unmarked_moduli_count',
            'Hodge_proved', 'Hodge_refuted', 'alpha_nonalgebraic_proved',
            'algebraic_representative_of_alpha_constructed', 'all_cycle_annihilation_proved',
            'global_witness_search_completed')), 'bottom-cover result promoted')
    lift = artifact['bielliptic-lift-audit']
    require(lift['contract'] == HOME + 'contracts/hodge-bielliptic-lift-audit.v1.json' and
            lift['note'] == 'research/voevodsky/hodge-bielliptic-lift-audit-v1.md' and
            lift['checker'] == 'research/voevodsky/checkers/check_hodge_bielliptic_lift_audit.py' and
            lift['receipt'] == 'research/voevodsky/results/hodge-bielliptic-lift-audit-v1.json', 'bielliptic-lift artifact binding')
    checked_lift = load(lift['receipt'])
    require(checked_lift == lift_report() and checked_lift['passed'] and
            all(checked_lift['checks'].values()), 'bielliptic-lift receipt stale or altered')
    require(checked_lift['candidate_id'] == candidate_id and checked_lift['verdict'] == 'rejected' and
            checked_lift['node'] == 'bielliptic-involution-lift-transplant' and
            checked_lift['conditional_on_bielliptic_intermediate'] is True and
            checked_lift['norm_zero_roots_excluded_up_to_fixed_A_isogeny'] is True and
            checked_lift['universal_bielliptic_lifting_claim_refuted'] is True and
            checked_lift['actual_theta_singularity_dimension'] is None and
            checked_lift['actual_matching_root_label'] is None and
            not any(checked_lift[k] for k in LIFT_POLICY + ['Hodge_proved', 'Hodge_refuted',
            'alpha_nonalgebraic_proved', 'algebraic_representative_of_alpha_constructed',
            'all_cycle_annihilation_proved', 'global_witness_search_completed']), 'bielliptic-lift result promoted')
    commuting = artifact['commuting-prym-audit']
    require(commuting['contract'] == HOME + 'contracts/hodge-commuting-prym-audit.v1.json' and
            commuting['note'] == 'research/voevodsky/hodge-commuting-prym-audit-v1.md' and
            commuting['checker'] == 'research/voevodsky/checkers/check_hodge_commuting_prym_audit.py' and
            commuting['receipt'] == 'research/voevodsky/results/hodge-commuting-prym-audit-v1.json', 'commuting Prym artifact binding')
    checked_commuting = load(commuting['receipt'])
    require(checked_commuting == commuting_report() and checked_commuting['passed'] and
            all(checked_commuting['checks'].values()), 'commuting Prym receipt stale or altered')
    require(checked_commuting['candidate_id'] == candidate_id and checked_commuting['verdict'] == 'rejected' and
            checked_commuting['node'] == 'commuting-prym-factor-transplant' and
            checked_commuting['conditional_on_bielliptic_intermediate'] is True and
            checked_commuting['mixed_commuting_factor_presentations_excluded_up_to_A_isogeny'] is True and
            checked_commuting['actual_theta_singularity_dimension'] is None and
            checked_commuting['actual_matching_root_label'] is None and
            not any(checked_commuting[k] for k in COMMUTING_POLICY), 'commuting Prym result promoted')
    even = artifact['even-scalar-cover']
    require(even['contract'] == HOME + 'contracts/hodge-even-scalar-cover.v1.json' and
            even['note'] == 'research/voevodsky/hodge-even-scalar-cover-v1.md' and
            even['checker'] == 'research/voevodsky/checkers/check_hodge_even_scalar_cover.py' and
            even['receipt'] == 'research/voevodsky/results/hodge-even-scalar-cover-v1.json', 'even scalar artifact binding')
    checked_even = load(even['receipt'])
    require(checked_even == even_scalar_report() and checked_even['passed'] and
            all(checked_even['checks'].values()), 'even scalar receipt stale or altered')
    require(checked_even['candidate_id'] == candidate_id and checked_even['verdict'] == 'rejected' and
            checked_even['node'] == 'inversion-symmetric-scalar-transplant' and
            checked_even['actual_control_tower_constructed'] is True and
            checked_even['even_scalar_subfamily_excluded_up_to_fixed_A_isogeny'] is True and
            checked_even['actual_theta_singularity_dimension'] is None and
            not any(checked_even[k] for k in EVEN_SCALAR_POLICY), 'even scalar result promoted')
    asymmetric = artifact['asymmetric-scalar-cover']
    require(asymmetric['contract'] == HOME + 'contracts/hodge-asymmetric-scalar-cover.v1.json' and
            asymmetric['note'] == 'research/voevodsky/hodge-asymmetric-scalar-cover-v1.md' and
            asymmetric['checker'] == 'research/voevodsky/checkers/check_hodge_asymmetric_scalar_cover.py' and
            asymmetric['receipt'] == 'research/voevodsky/results/hodge-asymmetric-scalar-cover-v1.json', 'asymmetric artifact binding')
    checked_asymmetric = load(asymmetric['receipt'])
    require(checked_asymmetric == asymmetric_report() and checked_asymmetric['passed'] and
            all(checked_asymmetric['checks'].values()), 'asymmetric receipt stale or altered')
    require(checked_asymmetric['candidate_id'] == candidate_id and checked_asymmetric['verdict'] == 'constructed' and
            checked_asymmetric['node'] == 'asymmetric-scalar-cover-control' and
            checked_asymmetric['actual_asymmetric_control_tower_constructed'] is True and
            checked_asymmetric['fixed_origin_inversion_has_no_lift_to_top_double_cover'] is True and
            checked_asymmetric['actual_theta_singularity_dimension'] is None and
            checked_asymmetric['actual_target_isogeny'] is None and
            not any(checked_asymmetric[k] for k in ASYMMETRIC_POLICY), 'asymmetric result promoted')
    automorphism = artifact['asymmetric-reflections']
    require(automorphism['contract'] == HOME + 'contracts/hodge-asymmetric-reflections.v1.json' and
            automorphism['note'] == 'research/voevodsky/hodge-asymmetric-reflections-v1.md' and
            automorphism['checker'] == 'research/voevodsky/checkers/check_hodge_asymmetric_reflections.py' and
            automorphism['receipt'] == 'research/voevodsky/results/hodge-asymmetric-reflections-v1.json', 'automorphism artifact binding')
    checked_aut = load(automorphism['receipt'])
    require(checked_aut == automorphism_report() and checked_aut['passed'] and
            all(checked_aut['checks'].values()), 'automorphism receipt stale or altered')
    require(checked_aut['candidate_id'] == candidate_id and checked_aut['verdict'] == 'constructed' and
            checked_aut['node'] == 'asymmetric-cover-automorphisms' and
            checked_aut['full_geometric_curve_automorphism_group'] == 'C4 x C2' and
            checked_aut['full_geometric_curve_automorphism_group_order'] == 8 and
            checked_aut['all_64_reflection_residues_nonzero'] is True and
            checked_aut['actual_theta_singularity_dimension'] is None and
            checked_aut['actual_target_isogeny'] is None and
            not any(checked_aut[k] for k in AUTOMORPHISM_POLICY), 'automorphism result promoted')
    frobenius = artifact['asymmetric-frobenius']
    require(frobenius['contract'] == HOME + 'contracts/hodge-asymmetric-frobenius.v1.json' and
            frobenius['note'] == 'research/voevodsky/hodge-asymmetric-frobenius-v1.md' and
            frobenius['checker'] == 'research/voevodsky/checkers/check_hodge_asymmetric_frobenius.py' and
            frobenius['receipt'] == 'research/voevodsky/results/hodge-asymmetric-frobenius-v1.json', 'Frobenius artifact binding')
    checked_frob = load(frobenius['receipt'])
    require(checked_frob == frobenius_report() and checked_frob['passed'] and
            all(checked_frob['checks'].values()), 'Frobenius receipt stale or altered')
    require(checked_frob['candidate_id'] == candidate_id and checked_frob['verdict'] == 'constructed' and
            checked_frob['node'] == 'asymmetric-prym-frobenius7' and
            checked_frob['reduction_simple_over_F7'] is True and checked_frob['reduction_ordinary_at_7'] is True and
            checked_frob['full_extension_counts_reexecuted'] is True and
            checked_frob['actual_theta_singularity_dimension'] is None and checked_frob['actual_target_isogeny'] is None and
            not any(checked_frob[k] for k in FROBENIUS_POLICY), 'Frobenius result promoted')
    absolute = artifact['asymmetric-absolute']
    require(absolute['contract'] == HOME + 'contracts/hodge-asymmetric-absolute.v1.json' and
            absolute['note'] == 'research/voevodsky/hodge-asymmetric-absolute-v1.md' and
            absolute['checker'] == 'research/voevodsky/checkers/check_hodge_asymmetric_absolute.py' and
            absolute['receipt'] == 'research/voevodsky/results/hodge-asymmetric-absolute-v1.json', 'absolute artifact binding')
    checked_abs = load(absolute['receipt'])
    require(checked_abs == absolute_report() and checked_abs['passed'] and
            all(checked_abs['checks'].values()), 'absolute receipt stale or altered')
    require(checked_abs['candidate_id'] == candidate_id and checked_abs['verdict'] == 'rejected' and
            checked_abs['node'] == 'asymmetric-scalar-target-transplant' and
            checked_abs['reduction_absolutely_simple'] is True and
            checked_abs['complex_auxiliary_Prym_absolutely_simple'] is True and
            checked_abs['this_auxiliary_Prym_isogenous_to_X6_times_B2'] is False and
            checked_abs['this_auxiliary_Prym_square_isogeny_excluded'] is True and
            checked_abs['nontrivial_cyclotomic_orders_checked'] == 504 and
            checked_abs['actual_theta_singularity_dimension'] is None and
            not any(checked_abs[k] for k in ABSOLUTE_POLICY), 'absolute result promoted')
    family = artifact['scalar-family-localization']
    require(family['contract'] == HOME + 'contracts/hodge-scalar-family-localization.v1.json' and
            family['note'] == 'research/voevodsky/hodge-scalar-family-localization-v1.md' and
            family['checker'] == 'research/voevodsky/checkers/check_hodge_scalar_family_localization.py' and
            family['receipt'] == 'research/voevodsky/results/hodge-scalar-family-localization-v1.json', 'scalar family artifact binding')
    checked_family = load(family['receipt'])
    require(checked_family == scalar_family_report() and checked_family['passed'] and
            all(checked_family['checks'].values()), 'scalar family receipt stale or altered')
    require(checked_family['candidate_id'] == candidate_id and checked_family['verdict'] == 'constructed' and
            checked_family['node'] == 'scalar-family-localization' and
            checked_family['fixed_elliptic_period_codifferential_rank'] == 7 and
            checked_family['Prym_map_quasifinite_on_norm_simple_chart'] is True and
            checked_family['geometric_generic_Prym_simple'] is True and
            checked_family['fixed_target_isogeny_locus_at_most_countable'] is True and
            checked_family['excluded_residue_vector_mod_7'] == [5,0,0,0,1,0,0] and
            not any(checked_family[k] for k in SCALAR_FAMILY_POLICY), 'scalar family result promoted')
    scalar_polarized = artifact['scalar-polarized-obstruction']
    require(scalar_polarized['contract'] == HOME + 'contracts/hodge-scalar-polarized-obstruction.v1.json' and
            scalar_polarized['note'] == 'research/voevodsky/hodge-scalar-polarized-obstruction-v1.md' and
            scalar_polarized['checker'] == 'research/voevodsky/checkers/check_hodge_scalar_polarized_obstruction.py' and
            scalar_polarized['receipt'] == 'research/voevodsky/results/hodge-scalar-polarized-obstruction-v1.json', 'scalar polarized artifact binding')
    checked_sp = load(scalar_polarized['receipt'])
    require(checked_sp == scalar_polarized_report() and checked_sp['passed'] and
            all(checked_sp['checks'].values()), 'scalar polarized receipt stale or altered')
    require(checked_sp['candidate_id'] == candidate_id and checked_sp['verdict'] == 'rejected' and
            checked_sp['node'] == 'scalar-polarized-prym-transplant' and
            checked_sp['canonical_polarized_Y2_scalar_realizations_excluded'] is True and
            checked_sp['minimum_elliptic_Prym_polarization_degree'] == 4 and
            checked_sp['conditional_polarized_Y2_survivor_labels'] == 512 and
            checked_sp['conditional_polarized_Y2_survivor_inverse_pairs'] == 256 and
            checked_sp['conditional_unpolarized_isogeny_survivor_labels'] == 516 and
            checked_sp['conditional_unpolarized_isogeny_survivor_inverse_pairs'] == 258 and
            checked_sp['actual_theta_singularity_dimension'] is None and
            not any(checked_sp[k] for k in SCALAR_POLARIZED_POLICY), 'scalar polarized result promoted')
    nonlifting = artifact['nonlifting-polarized-obstruction']
    require(nonlifting['contract'] == HOME + 'contracts/hodge-nonlifting-polarized-obstruction.v1.json' and
            nonlifting['note'] == 'research/voevodsky/hodge-nonlifting-polarized-obstruction-v1.md' and
            nonlifting['checker'] == 'research/voevodsky/checkers/check_hodge_nonlifting_polarized_obstruction.py' and
            nonlifting['receipt'] == 'research/voevodsky/results/hodge-nonlifting-polarized-obstruction-v1.json', 'nonlifting artifact binding')
    checked_nl = load(nonlifting['receipt'])
    require(checked_nl == nonlifting_report() and checked_nl['passed'] and
            all(checked_nl['checks'].values()), 'nonlifting receipt stale or altered')
    require(checked_nl['candidate_id'] == candidate_id and checked_nl['verdict'] == 'rejected' and
            checked_nl['node'] == 'nonlifting-polarized-prym-transplant' and
            checked_nl['joint_degrees_exhausted'] == [1,2,4] and
            checked_nl['fixed_Y2_bielliptic_intermediate_cyclic_realizations_excluded'] is True and
            checked_nl['conditional_polarized_Y2_survivor_labels'] == 0 and
            checked_nl['conditional_polarized_Y2_survivor_inverse_pairs'] == 0 and
            checked_nl['conditional_unpolarized_isogeny_survivor_labels'] == 516 and
            checked_nl['conditional_unpolarized_isogeny_survivor_inverse_pairs'] == 258 and
            checked_nl['necessary_theta_dimension_upper_bound_if_cyclic_realization_exists'] == 3 and
            checked_nl['actual_theta_singularity_dimension'] is None and
            not any(checked_nl[k] for k in NONLIFTING_POLICY), 'nonlifting result promoted')
    cs = artifact['scalar-37-census']
    require(cs['contract'] == HOME + 'contracts/hodge-scalar-37-census.v1.json' and
            cs['note'] == 'research/voevodsky/hodge-scalar-37-census-v1.md' and
            cs['checker'] == 'research/voevodsky/checkers/check_hodge_scalar_37_census.py' and
            cs['receipt'] == 'research/voevodsky/results/hodge-scalar-37-census-v1.json', 'full37 artifact binding')
    checked_cs = load(cs['receipt'])
    require(checked_cs == census37_report() and checked_cs['passed'] and all(checked_cs['checks'].values()), 'full37 receipt stale or altered')
    require(checked_cs['candidate_id'] == candidate_id and checked_cs['node'] == 'scalar-37-full-screen' and
            checked_cs['excluded_control_node'] == 'scalar-37-typed-polarized-target-transplant' and checked_cs['target_transplant_verdict'] == 'rejected' and
            checked_cs['verdicts_by_a_residue']['necessary_screen_survives'] == [0,16] and
            checked_cs['verdicts_by_a_residue']['opposite_type_absent'] == [21] and checked_cs['verdicts_by_a_residue']['inert3_degree_parity'] == [2,8,13] and
            checked_cs['known_axis_split_certificate']['actual_axis_theta_degree'] == 4 and checked_cs['known_axis_split_certificate']['integral_at3'] is True and
            checked_cs['literal_2_214_2_excluded_even_up_to_Y3_isogeny'] is True and checked_cs['CRT_partition']['excluded_count'] == 8077 and
            checked_cs['CRT_partition']['joint_survivors'] == [3087,6623] and checked_cs['CRT_partition']['uncertified_count'] == 98 and
            checked_cs['next_actual_control']['parameters_lambda_a_b'] == [2,-1554,2] and not any(checked_cs[k] for k in CENSUS37_POLICY), 'full37 result promoted beyond scope')
    tp = artifact['off-reflection-third-prime']
    require(tp['contract'] == HOME + 'contracts/hodge-off-reflection-third-prime.v1.json' and
            tp['note'] == 'research/voevodsky/hodge-off-reflection-third-prime-v1.md' and
            tp['checker'] == 'research/voevodsky/checkers/check_hodge_off_reflection_third_prime.py' and
            tp['receipt'] == 'research/voevodsky/results/hodge-off-reflection-third-prime-v1.json', 'third-prime artifact binding')
    checked_tp = load(tp['receipt'])
    require(checked_tp == third_report() and checked_tp['passed'] and all(checked_tp['checks'].values()), 'third-prime receipt stale or altered')
    require(checked_tp['candidate_id'] == candidate_id and checked_tp['node'] == 'off-reflection-third-prime-generic-gate' and
            checked_tp['excluded_control_node'] == 'third-prime-and-generic-target-transplant' and checked_tp['target_transplant_verdict'] == 'rejected' and
            checked_tp['prime37_result']['cyclotomic_factors'] == [] and checked_tp['literal_2_minus7_2_excluded_even_up_to_Y3_isogeny'] is True and
            checked_tp['generic_rank_certificate']['geometric_generic_a_line_Hom_rank'] == 2 and
            checked_tp['generic_rank_certificate']['geometric_generic_three_parameter_Hom_rank'] == 2 and
            checked_tp['generic_rank_certificate']['transcendental_a_on_lambda2_b2_line_excluded'] is True and
            checked_tp['generic_rank_certificate']['algebraically_independent_parameter_triples_excluded'] is True and
            checked_tp['CRT_partition']['excluded_count'] == 7457 and len(checked_tp['CRT_partition']['two_prime_survivors_not_counted_at37']) == 36 and
            checked_tp['next_actual_control']['parameters_lambda_a_b'] == [2,214,2] and not any(checked_tp[k] for k in THIRD_POLICY), 'third-prime/generic result promoted beyond scope')
    ip = artifact['inert-elliptic-projector']
    require(ip['contract'] == HOME + 'contracts/hodge-inert-elliptic-projector.v1.json' and
            ip['note'] == 'research/voevodsky/hodge-inert-elliptic-projector-v1.md' and
            ip['checker'] == 'research/voevodsky/checkers/check_hodge_inert_elliptic_projector.py' and
            ip['receipt'] == 'research/voevodsky/results/hodge-inert-elliptic-projector-v1.json', 'inert projector artifact binding')
    checked_ip = load(ip['receipt'])
    require(checked_ip == inert_report() and checked_ip['passed'] and all(checked_ip['checks'].values()), 'inert projector receipt stale or altered')
    require(checked_ip['candidate_id'] == candidate_id and checked_ip['node'] == 'inert-elliptic-projector-gate' and
            checked_ip['excluded_control_node'] == 'inert-degree-parity-target-transplant' and checked_ip['target_transplant_verdict'] == 'rejected' and
            checked_ip['projector_certificate']['integral_at3'] is True and checked_ip['nonunit_a6_control']['integral_at3'] is False and
            checked_ip['literal_2_minus24_2_excluded_even_up_to_Y3_isogeny'] is True and
            len(checked_ip['CRT_partition']['excluded']) == 201 and checked_ip['CRT_partition']['joint_survivors'] == [214] and
            len(checked_ip['CRT_partition']['uncertified']) == 19 and not any(checked_ip[k] for k in INERT_POLICY), 'inert projector promoted beyond scope')
    js = artifact['off-reflection-joint-screen']
    require(js['contract'] == HOME + 'contracts/hodge-off-reflection-joint-screen.v1.json' and
            js['note'] == 'research/voevodsky/hodge-off-reflection-joint-screen-v1.md' and
            js['checker'] == 'research/voevodsky/checkers/check_hodge_off_reflection_joint_screen.py' and
            js['receipt'] == 'research/voevodsky/results/hodge-off-reflection-joint-screen-v1.json', 'two-prime artifact binding')
    checked_js = load(js['receipt'])
    require(checked_js == joint_screen_report() and checked_js['passed'] and all(checked_js['checks'].values()), 'two-prime receipt stale or altered')
    require(checked_js['candidate_id'] == candidate_id and checked_js['node'] == 'off-reflection-two-prime-screen' and
            checked_js['excluded_control_node'] == 'off-reflection-two-prime-target-transplant' and
            checked_js['target_transplant_verdict'] == 'rejected' and checked_js['typed_excluded_count_mod221'] == 197 and
            checked_js['CRT_partition']['typed_joint_survivors'] == [197,214] and len(checked_js['CRT_partition']['uncertified']) == 22 and
            checked_js['signature_certificate']['unpolarized_isogeny_need_not_be_K_linear'] is True and
            checked_js['literal_2_6_2_excluded_even_up_to_Y3_isogeny'] is True and
            checked_js['same_type_only_special_fibre_is_not_declared_CM_free'] is True and
            checked_js['actual_next_control']['parameters_lambda_a_b'] == [2,-7,2] and
            not any(checked_js[k] for k in JOINT_SCREEN_POLICY), 'two-prime screen promoted beyond scope')
    al = artifact['off-reflection-a-line']
    require(al['contract'] == HOME + 'contracts/hodge-off-reflection-a-line.v1.json' and
            al['note'] == 'research/voevodsky/hodge-off-reflection-a-line-v1.md' and
            al['checker'] == 'research/voevodsky/checkers/check_hodge_off_reflection_a_line.py' and
            al['receipt'] == 'research/voevodsky/results/hodge-off-reflection-a-line-v1.json', 'a-line artifact binding')
    checked_al = load(al['receipt'])
    require(checked_al == a_line_report() and checked_al['passed'] and all(checked_al['checks'].values()), 'a-line receipt stale or altered')
    require(checked_al['candidate_id'] == candidate_id and checked_al['node'] == 'off-reflection-a-line-screen' and
            checked_al['excluded_control_node'] == 'off-reflection-a-line-target-transplant' and
            checked_al['target_transplant_verdict'] == 'rejected' and checked_al['excluded_a_residues'] == [0,7,8,10,11,12] and
            checked_al['surviving_a_residues'] == [2,6] and len(checked_al['algebraic_congruence_boxes_excluded']) == 12 and
            checked_al['off_reflection_control_2_0_2_excluded_even_up_to_Y3_isogeny'] is True and
            checked_al['actual_next_control']['parameters_lambda_a_b'] == [2,6,2] and
            not any(checked_al[k] for k in A_LINE_POLICY), 'a-line reduction promoted beyond scope')
    rf = artifact['scalar-reflection-decomposition']
    require(rf['contract'] == HOME + 'contracts/hodge-scalar-reflection-decomposition.v1.json' and
            rf['note'] == 'research/voevodsky/hodge-scalar-reflection-decomposition-v1.md' and
            rf['checker'] == 'research/voevodsky/checkers/check_hodge_scalar_reflection_decomposition.py' and
            rf['receipt'] == 'research/voevodsky/results/hodge-scalar-reflection-decomposition-v1.json', 'reflection artifact binding')
    checked_rf = load(rf['receipt'])
    require(checked_rf == reflection_report() and checked_rf['passed'] and all(checked_rf['checks'].values()), 'reflection receipt stale or altered')
    require(checked_rf['candidate_id'] == candidate_id and checked_rf['node'] == 'scalar-reflection-quotient-decomposition' and
            checked_rf['excluded_control_node'] == 'reflection-symmetric-scalar-target-transplant' and
            checked_rf['target_transplant_verdict'] == 'rejected' and checked_rf['source_isogeny_factor_dimensions'] == [3,5] and
            checked_rf['source_isogeny_degree'] == 256 and checked_rf['source_principal_polarization_pullback_multiple'] == 2 and
            checked_rf['all_admissible_reflection_loci_excluded_even_up_to_complex_Y3_isogeny'] is True and
            checked_rf['literal_b3_source_isogenous_to_Y3'] is False and
            checked_rf['actual_off_locus_control']['parameters_lambda_a_b'] == [2,0,2] and
            not any(checked_rf[k] for k in REFLECTION_POLICY), 'reflection result promoted beyond scope')
    sp = artifact['minimal-axis-second-prime']
    require(sp['contract'] == HOME + 'contracts/hodge-minimal-axis-second-prime.v1.json' and
            sp['note'] == 'research/voevodsky/hodge-minimal-axis-second-prime-v1.md' and
            sp['checker'] == 'research/voevodsky/checkers/check_hodge_minimal_axis_second_prime.py' and
            sp['receipt'] == 'research/voevodsky/results/hodge-minimal-axis-second-prime-v1.json', 'second-prime artifact binding')
    checked_sp = load(sp['receipt'])
    require(checked_sp == second_prime_report() and checked_sp['passed'] and all(checked_sp['checks'].values()), 'second-prime receipt stale or altered')
    require(checked_sp['candidate_id'] == candidate_id and checked_sp['node'] == 'minimal-axis-second-prime-screen' and
            checked_sp['excluded_control_node'] == 'minimal-axis-b6-target-transplant' and
            checked_sp['b6_control_verdict'] == 'rejected' and checked_sp['b3_necessary_prime_screens_survived'] == [13,17] and
            checked_sp['b6_complex_complement_has_no_Ei_factor'] is True and
            checked_sp['b6_source_Ei_isogeny_multiplicity'] == 1 and checked_sp['fixed_Y3_Ei_isogeny_multiplicity'] == 2 and
            checked_sp['b6_source_isogenous_to_fixed_Y3'] is False and
            checked_sp['algebraic_b_congruence_classes_6_and23_mod29_excluded'] is True and
            not any(checked_sp[k] for k in SECOND_PRIME_POLICY), 'second-prime result promoted beyond scope')
    bl = artifact['minimal-axis-b-line']
    require(bl['contract'] == HOME + 'contracts/hodge-minimal-axis-b-line.v1.json' and
            bl['note'] == 'research/voevodsky/hodge-minimal-axis-b-line-v1.md' and
            bl['checker'] == 'research/voevodsky/checkers/check_hodge_minimal_axis_b_line.py' and
            bl['receipt'] == 'research/voevodsky/results/hodge-minimal-axis-b-line-v1.json', 'b-line artifact binding')
    checked_bl = load(bl['receipt'])
    require(checked_bl == b_line_report() and checked_bl['passed'] and all(checked_bl['checks'].values()), 'b-line receipt stale or altered')
    require(checked_bl['candidate_id'] == candidate_id and checked_bl['node'] == 'minimal-axis-b-line-screen' and
            checked_bl['verdict'] == 'constructed' and checked_bl['CM_ratio_excluded_residues'] == [2,15] and
            checked_bl['CM_ratio_surviving_residues'] == [3,6,11,14] and
            checked_bl['algebraic_b_congruence_classes_2_and15_excluded_even_up_to_Y3_isogeny'] is True and
            checked_bl['new_rational_sources_with_one_primitive_theta4_axis_constructed'] is True and
            not any(checked_bl[k] for k in B_LINE_POLICY), 'b-line reduction promoted to target')
    mf = artifact['minimal-axis-frobenius-obstruction']
    require(mf['contract'] == HOME + 'contracts/hodge-minimal-axis-frobenius-obstruction.v1.json' and
            mf['note'] == 'research/voevodsky/hodge-minimal-axis-frobenius-obstruction-v1.md' and
            mf['checker'] == 'research/voevodsky/checkers/check_hodge_minimal_axis_frobenius_obstruction.py' and
            mf['receipt'] == 'research/voevodsky/results/hodge-minimal-axis-frobenius-obstruction-v1.json', 'minimal Frobenius artifact binding')
    checked_mf = load(mf['receipt'])
    require(checked_mf == minimal_frob_report() and checked_mf['passed'] and
            all(checked_mf['checks'].values()), 'minimal Frobenius receipt stale or altered')
    require(checked_mf['candidate_id'] == candidate_id and checked_mf['node'] == 'minimal-axis-scalar-target-transplant' and
            checked_mf['verdict'] == 'rejected' and checked_mf['reduction_ordinary_at17'] is True and
            checked_mf['complex_complement_has_no_square_lattice_elliptic_factor'] is True and
            checked_mf['source_square_lattice_elliptic_isogeny_multiplicity'] == 1 and
            checked_mf['fixed_Y3_square_lattice_elliptic_isogeny_multiplicity'] == 2 and
            checked_mf['this_source_isogenous_to_fixed_Y3'] is False and
            checked_mf['cyclotomic_orders_checked_including_one'] == 55 and
            not any(checked_mf[k] for k in MINIMAL_FROB_POLICY), 'minimal Frobenius exclusion promoted')
    minimal = artifact['minimal-axis-scalar-source']
    require(minimal['contract'] == HOME + 'contracts/hodge-minimal-axis-scalar-source.v1.json' and
            minimal['note'] == 'research/voevodsky/hodge-minimal-axis-scalar-source-v1.md' and
            minimal['checker'] == 'research/voevodsky/checkers/check_hodge_minimal_axis_scalar_source.py' and
            minimal['receipt'] == 'research/voevodsky/results/hodge-minimal-axis-scalar-source-v1.json', 'minimal source artifact binding')
    checked_minimal = load(minimal['receipt'])
    require(checked_minimal == minimal_source_report() and checked_minimal['passed'] and
            all(checked_minimal['checks'].values()), 'minimal source receipt stale or altered')
    require(checked_minimal['candidate_id'] == candidate_id and checked_minimal['node'] == 'minimal-axis-scalar-source' and
            checked_minimal['verdict'] == 'constructed' and checked_minimal['actual_scalar_curve_tower_constructed'] is True and
            checked_minimal['actual_primitive_theta4_axis_constructed'] is True and
            checked_minimal['actual_ramified9_1_to_source_principal_Prym_degree2_isogeny_constructed'] is True and
            checked_minimal['auxiliary_determinant_classes_algebraic_by_retained_theorem'] is True and
            checked_minimal['source_principal_Prym_elliptic_theta_degree'] == 4 and
            checked_minimal['primitive_curve_to_CM_elliptic_degree'] == 8 and
            [checked_minimal[k] for k in ('C_genus','D_genus','B_genus')] == [17,9,5] and
            not any(checked_minimal[k] for k in MINIMAL_SOURCE_POLICY), 'minimal source promoted to target')
    joint = artifact['even-axis-joint-degree-gate']
    require(joint['contract'] == HOME + 'contracts/hodge-even-axis-joint-degree-gate.v1.json' and
            joint['note'] == 'research/voevodsky/hodge-even-axis-joint-degree-gate-v1.md' and
            joint['checker'] == 'research/voevodsky/checkers/check_hodge_even_axis_joint_degree_gate.py' and
            joint['receipt'] == 'research/voevodsky/results/hodge-even-axis-joint-degree-gate-v1.json', 'joint-degree artifact binding')
    checked_joint = load(joint['receipt'])
    require(checked_joint == joint_degree_report() and checked_joint['passed'] and
            all(checked_joint['checks'].values()), 'joint-degree receipt stale or altered')
    require(checked_joint['candidate_id'] == candidate_id and checked_joint['node'] == 'even-axis-joint-degree-gate' and
            checked_joint['verdict'] == 'constructed' and checked_joint['fixed_principal_Y3_Jacobian_presentation_excluded'] is True and
            checked_joint['joint_degree4_excluded_for_fixed_Y3'] is True and
            checked_joint['remaining_conditional_joint_degrees'] == [1,2] and
            checked_joint['degree2_requires_scalar_elliptic_isogeny_pullback'] is True and
            checked_joint['degree2_ramified_Prym_genus_pair'] == [9,1] and
            checked_joint['degree2_ramified_Prym_branch_points'] == 16 and
            checked_joint['degree2_ramified_Prym_isogeny_to_Y3_degree'] == 2 and
            checked_joint['normalization_defect_sums_for_joint_degrees_1_2'] == [80,16] and
            not any(checked_joint[k] for k in JOINT_DEGREE_POLICY), 'joint-degree gate promoted')
    coupled = artifact['even-axis-coupled-kummer-gate']
    require(coupled['contract'] == HOME + 'contracts/hodge-even-axis-coupled-kummer-gate.v1.json' and
            coupled['note'] == 'research/voevodsky/hodge-even-axis-coupled-kummer-gate-v1.md' and
            coupled['checker'] == 'research/voevodsky/checkers/check_hodge_even_axis_coupled_kummer_gate.py' and
            coupled['receipt'] == 'research/voevodsky/results/hodge-even-axis-coupled-kummer-gate-v1.json', 'coupled Kummer artifact binding')
    checked_coupled = load(coupled['receipt'])
    require(checked_coupled == coupled_kummer_report() and checked_coupled['passed'] and
            all(checked_coupled['checks'].values()), 'coupled Kummer receipt stale or altered')
    require(checked_coupled['candidate_id'] == candidate_id and checked_coupled['node'] == 'even-axis-coupled-kummer-gate' and
            checked_coupled['verdict'] == 'constructed' and checked_coupled['conditional_geometric_cover_reconstruction_proved'] is True and
            checked_coupled['base_function_degrees'] == [8,12] and
            checked_coupled['quotient_surface_equation'] == 'r^4=H(s)*H(t)' and
            checked_coupled['opposite_Kummer_characters'] == [1,3] and
            checked_coupled['paired_local_profile_controls'] == 1960 and
            checked_coupled['conditional_reconstructed_tower_genera'] == [17,9,5] and
            not any(checked_coupled[k] for k in COUPLED_KUMMER_POLICY), 'coupled Kummer gate promoted')
    even = artifact['even-axis-principal-model']
    require(even['contract'] == HOME + 'contracts/hodge-even-axis-principal-model.v1.json' and
            even['note'] == 'research/voevodsky/hodge-even-axis-principal-model-v1.md' and
            even['checker'] == 'research/voevodsky/checkers/check_hodge_even_axis_principal_model.py' and
            even['receipt'] == 'research/voevodsky/results/hodge-even-axis-principal-model-v1.json', 'even-axis artifact binding')
    checked_even = load(even['receipt'])
    require(checked_even == even_axis_report() and checked_even['passed'] and
            all(checked_even['checks'].values()), 'even-axis receipt stale or altered')
    require(checked_even['candidate_id'] == candidate_id and checked_even['node'] == 'even-axis-principal-model' and
            checked_even['verdict'] == 'constructed' and checked_even['actual_principal_Gaussian_model_Y3_constructed'] is True and
            checked_even['principal_polarization_indecomposable'] is True and
            checked_even['four_exceptional_cycle_channels_transported'] is True and
            checked_even['physical_elliptic_surface_polarization_degrees'] == [4,6] and
            checked_even['elliptic_theta_degree_lower_bound'] == 4 and
            checked_even['all_elliptic_theta_degrees_even'] is True and
            checked_even['Gaussian_composite_determinant'] == [0,768] and
            checked_even['normalized_transfer_denominator'] == 768 and
            not any(checked_even[k] for k in EVEN_AXIS_POLICY), 'even-axis model promoted')
    two = artifact['two-branch-odd-axis-obstruction']
    require(two['contract'] == HOME + 'contracts/hodge-two-branch-odd-axis-obstruction.v1.json' and
            two['note'] == 'research/voevodsky/hodge-two-branch-odd-axis-obstruction-v1.md' and
            two['checker'] == 'research/voevodsky/checkers/check_hodge_two_branch_odd_axis_obstruction.py' and
            two['receipt'] == 'research/voevodsky/results/hodge-two-branch-odd-axis-obstruction-v1.json', 'two-branch artifact binding')
    checked_two = load(two['receipt'])
    require(checked_two == two_branch_report() and checked_two['passed'] and
            all(checked_two['checks'].values()), 'two-branch receipt stale or altered')
    require(checked_two['candidate_id'] == candidate_id and
            checked_two['node'] == 'y2-two-branch-cyclic-quartic-transplant' and checked_two['verdict'] == 'rejected' and
            checked_two['fixed_Y2_natural_principal_two_branch_cyclic_quartic_presentations_excluded'] is True and
            checked_two['fixed_Y2_standard_zero_or_two_branch_principal_cyclic_quartic_presentations_excluded'] is True and
            checked_two['generator_fixed_point_count'] == 2 and
            checked_two['degree_six_tangent_compatible_profile_count'] == 0 and
            checked_two['conditional_equivariant_elliptic_map_degree_divisor'] == 4 and
            checked_two['conditional_two_branch_K_isogeny_source_axis_theta_degrees_even'] is True and
            not any(checked_two[k] for k in TWO_BRANCH_POLICY), 'two-branch exclusion promoted')
    odd = artifact['cyclic-prym-odd-axis-obstruction']
    require(odd['contract'] == HOME + 'contracts/hodge-cyclic-prym-odd-axis-obstruction.v1.json' and
            odd['note'] == 'research/voevodsky/hodge-cyclic-prym-odd-axis-obstruction-v1.md' and
            odd['checker'] == 'research/voevodsky/checkers/check_hodge_cyclic_prym_odd_axis_obstruction.py' and
            odd['receipt'] == 'research/voevodsky/results/hodge-cyclic-prym-odd-axis-obstruction-v1.json', 'odd-axis artifact binding')
    checked_odd = load(odd['receipt'])
    require(checked_odd == odd_axis_report() and checked_odd['passed'] and
            all(checked_odd['checks'].values()), 'odd-axis receipt stale or altered')
    require(checked_odd['candidate_id'] == candidate_id and
            checked_odd['node'] == 'y2-etale-cyclic-quartic-polarized-transplant' and checked_odd['verdict'] == 'rejected' and
            checked_odd['fixed_Y2_smooth_etale_cyclic_quartic_principal_presentations_excluded'] is True and
            checked_odd['physical_CM_product_polarization_degrees'] == [2,3] and
            checked_odd['surface_unitary_restriction_upper_bound'] == 16 and
            checked_odd['forced_elliptic_curve_map_degree'] == 6 and
            checked_odd['required_free_C4_fibre_degree_divisor'] == 4 and
            checked_odd['conditional_K_isogeny_source_axis_theta_degrees_even'] is True and
            checked_odd['conditional_auxiliary_K_isogeny_source_minimum_axis_theta_degree'] == 4 and
            not any(checked_odd[k] for k in ODD_AXIS_POLICY), 'odd-axis exclusion promoted')
    match = artifact['trigonal-principal-match-obstruction']
    require(match['contract'] == HOME + 'contracts/hodge-trigonal-principal-match-obstruction.v1.json' and
            match['note'] == 'research/voevodsky/hodge-trigonal-principal-match-obstruction-v1.md' and
            match['checker'] == 'research/voevodsky/checkers/check_hodge_trigonal_principal_match_obstruction.py' and
            match['receipt'] == 'research/voevodsky/results/hodge-trigonal-principal-match-obstruction-v1.json', 'principal match artifact binding')
    checked_match = load(match['receipt'])
    require(checked_match == principal_match_report() and checked_match['passed'] and
            all(checked_match['checks'].values()), 'principal match receipt stale or altered')
    require(checked_match['candidate_id'] == candidate_id and
            checked_match['node'] == 'ramified-trigonal-principal-target-transplant' and checked_match['verdict'] == 'rejected' and
            checked_match['fixed_Y2_natural_principal_match_for_auxiliary_family_excluded'] is True and
            checked_match['forced_quotient_genera'] == {'V':3,'U':1,'Q':1,'W':7} and
            checked_match['forced_Prym_factor_dimensions'] == [2,6] and
            checked_match['forced_sixfold_raw_norm_class'] == '-1' and
            checked_match['fixed_X_raw_norm_class'] == '-3' and
            not any(checked_match[k] for k in PRINCIPAL_MATCH_POLICY), 'principal match exclusion promoted')
    family = artifact['ramified-trigonal-family']
    require(family['contract'] == HOME + 'contracts/hodge-ramified-trigonal-family.v1.json' and
            family['note'] == 'research/voevodsky/hodge-ramified-trigonal-family-v1.md' and
            family['checker'] == 'research/voevodsky/checkers/check_hodge_ramified_trigonal_family.py' and
            family['receipt'] == 'research/voevodsky/results/hodge-ramified-trigonal-family-v1.json', 'ramified family artifact binding')
    checked_family = load(family['receipt'])
    require(checked_family == ramified_family_report() and checked_family['passed'] and
            all(checked_family['checks'].values()), 'ramified family receipt stale or altered')
    require(checked_family['candidate_id'] == candidate_id and
            checked_family['node'] == 'ramified-trigonal-auxiliary-family' and checked_family['verdict'] == 'constructed' and
            checked_family['ramified_tower_genera'] == [16,8,4] and
            checked_family['etale_tetragonal_tower_genera'] == [17,9,5] and
            checked_family['auxiliary_smooth_connected_cover_existence'] is True and
            checked_family['auxiliary_K_equivariant_ppav_isomorphism'] is True and
            checked_family['auxiliary_free_C4_etale_tower'] is True and
            checked_family['auxiliary_determinant_algebraicity_by_primary_theorem'] is True and
            not any(checked_family[k] for k in RAMIFIED_FAMILY_POLICY), 'ramified family promoted to target')
    persistence = artifact['secant-criterion-persistence']
    require(persistence['contract'] == HOME + 'contracts/hodge-secant-criterion-persistence.v1.json' and
            persistence['note'] == 'research/voevodsky/hodge-secant-criterion-persistence-v1.md' and
            persistence['checker'] == 'research/voevodsky/checkers/check_hodge_secant_criterion_persistence.py' and
            persistence['receipt'] == 'research/voevodsky/results/hodge-secant-criterion-persistence-v1.json', 'persistence artifact binding')
    checked_persist = load(persistence['receipt'])
    require(checked_persist == persistence_report() and checked_persist['passed'] and
            all(checked_persist['checks'].values()), 'persistence receipt stale or altered')
    require(checked_persist['candidate_id'] == candidate_id and
            checked_persist['node'] == 'eightfold-secant-weak-criterion-transplant' and
            checked_persist['verdict'] == 'rejected' and
            checked_persist['standard_corrected_pair_full_HH2_criterion_fails'] is True and
            checked_persist['product_trace_kernel_lower_bound'] == 4 and
            checked_persist['equivalence_trace_kernel_lower_bound'] == 4 and
            checked_persist['conditional_isogeny_descent_kernel_lower_bound'] == 4 and
            checked_persist['finite_etale_pushforward_kernel_lower_bound'] == 4 and
            not any(checked_persist[k] for k in PERSISTENCE_POLICY), 'persistence result promoted')
    source_semi = artifact['secant-source-semiregularity']
    require(source_semi['contract'] == HOME + 'contracts/hodge-secant-source-semiregularity.v1.json' and
            source_semi['note'] == 'research/voevodsky/hodge-secant-source-semiregularity-v1.md' and
            source_semi['checker'] == 'research/voevodsky/checkers/check_hodge_secant_source_semiregularity.py' and
            source_semi['receipt'] == 'research/voevodsky/results/hodge-secant-source-semiregularity-v1.json', 'source semiregularity artifact binding')
    checked_semi = load(source_semi['receipt'])
    require(checked_semi == source_semireg_report() and checked_semi['passed'] and
            all(checked_semi['checks'].values()), 'source semiregularity receipt stale or altered')
    require(checked_semi['candidate_id'] == candidate_id and
            checked_semi['node'] == 'secant-source-weak-semiregularity-transplant' and
            checked_semi['verdict'] == 'rejected' and checked_semi['source_weak_criterion_fails'] is True and
            checked_semi['character_action_rank'] == 12 and
            checked_semi['trace_kernel_on_evaluation_image_lower_bound'] == 2 and
            checked_semi['evaluation_rank_lower_bound'] == 14 and
            not any(checked_semi[k] for k in SOURCE_SEMIREG_POLICY), 'source semiregularity result promoted')
    local_ext = artifact['secant-local-ext-gate']
    require(local_ext['contract'] == HOME + 'contracts/hodge-secant-local-ext-gate.v1.json' and
            local_ext['note'] == 'research/voevodsky/hodge-secant-local-ext-gate-v1.md' and
            local_ext['checker'] == 'research/voevodsky/checkers/check_hodge_secant_local_ext_gate.py' and
            local_ext['receipt'] == 'research/voevodsky/results/hodge-secant-local-ext-gate-v1.json', 'local Ext artifact binding')
    checked_ext = load(local_ext['receipt'])
    require(checked_ext == local_ext_report() and checked_ext['passed'] and
            all(checked_ext['checks'].values()), 'local Ext receipt stale or altered')
    require(checked_ext['candidate_id'] == candidate_id and checked_ext['node'] == 'secant-local-ext-gate' and
            checked_ext['verdict'] == 'constructed' and checked_ext['isolated_nodes'] == 432 and
            checked_ext['triple_points'] == 216 and checked_ext['H1_length'] == 306 and
            checked_ext['dual_sheaf_Ext3_length'] == 126 and checked_ext['local_self_Ext2_length'] == 1116 and
            not any(checked_ext[k] for k in LOCAL_EXT_POLICY), 'local Ext result promoted')
    literature = artifact['eightfold-literature-audit']
    require(literature['contract'] == HOME + 'contracts/hodge-eightfold-literature-audit.v1.json' and
            literature['note'] == 'research/voevodsky/hodge-eightfold-literature-audit-v1.md' and
            literature['checker'] == 'research/voevodsky/checkers/check_hodge_eightfold_literature_audit.py' and
            literature['receipt'] == 'research/voevodsky/results/hodge-eightfold-literature-audit-v1.json', 'eightfold literature artifact binding')
    checked_lit = load(literature['receipt'])
    require(checked_lit == eightfold_literature_report() and checked_lit['passed'] and
            all(checked_lit['checks'].values()), 'eightfold literature receipt stale or altered')
    require(checked_lit['candidate_id'] == candidate_id and
            checked_lit['node'] == 'eightfold-literature-and-secant-audit' and
            checked_lit['verdict'] == 'constructed' and
            checked_lit['Schoen_eightfold_cycle_mechanism_conditional_on_realization'] is True and
            checked_lit['d9_corrected_character'] == ['1','3','-9/2','-9/2','27/8'] and
            checked_lit['d9_normalized_nodes'] == 306 and
            checked_lit['ramified_tower_genera'] == [16,8,4] and
            checked_lit['primitive_Prym_dimension'] == 8 and
            not any(checked_lit[k] for k in EIGHTFOLD_LITERATURE_POLICY), 'eightfold literature result promoted')
    tetragonal = artifact['equivariant-tetragonal-gate']
    require(tetragonal['contract'] == HOME + 'contracts/hodge-equivariant-tetragonal-gate.v1.json' and
            tetragonal['note'] == 'research/voevodsky/hodge-equivariant-tetragonal-gate-v1.md' and
            tetragonal['checker'] == 'research/voevodsky/checkers/check_hodge_equivariant_tetragonal_gate.py' and
            tetragonal['receipt'] == 'research/voevodsky/results/hodge-equivariant-tetragonal-gate-v1.json', 'tetragonal artifact binding')
    checked_tg = load(tetragonal['receipt'])
    require(checked_tg == tetragonal_report() and checked_tg['passed'] and
            all(checked_tg['checks'].values()), 'tetragonal receipt stale or altered')
    require(checked_tg['candidate_id'] == candidate_id and checked_tg['verdict'] == 'constructed' and
            checked_tg['node'] == 'equivariant-tetragonal-gate' and
            checked_tg['necessary_C9_gonality'] == 4 and
            checked_tg['free_intermediate_involution_preserves_pencil'] is True and
            checked_tg['induced_P1_involution_nontrivial'] is True and
            checked_tg['bottom_required_even_fibres'] == 2 and
            checked_tg['top_required_harmonic_even_fibres'] == 4 and
            checked_tg['CM_elliptic_j_invariant'] == 1728 and
            checked_tg['connected_quadratic_square_classes_required_nontrivial'] is True and
            checked_tg['actual_theta_singularity_dimension'] is None and
            not any(checked_tg[k] for k in TETRAGONAL_POLICY), 'tetragonal result promoted')
    for item in artifact.values():
        for key in ('contract', 'checker', 'receipt'):
            require(path(item[key]).is_file(), 'missing bound artifact')
    scoped = load(scope['receipt'])
    require(scoped == cycle_scope_report() and scoped['passed'] and all(scoped['checks'].values()), 'scope receipt stale or altered')
    require(not any(scoped[k] for k in ('packet_bridge_constructed', 'specific_obstruction_constructed', 'Hodge_proved', 'Hodge_refuted')), 'scope theorem promoted')
    require(c['iteration'] == 52 and c['predecessor']['source_pins'] == 'research/voevodsky/inputs/hodge-net-source-pins.v54.json', 'iteration provenance')
    for previous, prior in predecessors(c):
        old_pins = load(previous['source_pins'])
        require(digest(previous['contract_snapshot']) == old_pins['source_sha256'][CONTRACT], 'predecessor contract drift')
        require(load(previous['validation_snapshot'])['source_sha256'] == old_pins['source_sha256'], 'predecessor receipt drift')

    # Materialize every local prerequisite port and every explicit cross-net port.
    connections, driven, input_ports = [], set(), set()
    for n in c['conjectures']:
        for d in n['depends_on']:
            port = ('hodge', n['id'], 'requires:' + d)
            input_ports.add(port); driven.add(port)
            connections.append({'source': 'hodge:' + d, 'source_port': 'constructed-witness',
                                'target': 'hodge:' + n['id'], 'target_port': port[2],
                                'type': 'constructed_witness', 'available': by[d]['verdict'] == 'constructed',
                                'logical_implication_asserted': False})
        input_ports.update(('hodge', n['id'], port) for port in n['external_inputs'])
        input_ports.update(('hodge', n['id'], 'requires:' + port) for port in n['requires'])
    links = {link['id']: link for link in a['connections']}
    require(set(links) == set(EXPECTED_LINKS) and len(links) == len(a['connections']), 'cross-net link coverage')
    for identifier, link in links.items():
        require((link['source_net'], link['source_node'], link['target_net'], link['target_node'], link['target_port']) == EXPECTED_LINKS[identifier], 'cross-net endpoint changed')
        for direction in ('source', 'target'):
            alias, node = link[direction + '_net'], link[direction + '_node']
            require(alias in refs and node in node_ids(refs[alias]), 'dangling external node')
        require(link['proof_bearing'] is link['discharges_target'] is link['blocks_local_research'] is False, 'reference promoted or blocking')
        target = (link['target_net'], link['target_node'], link['target_port'])
        require(target not in driven, 'duplicate input driver')
        driven.add(target)
        if link['target_net'] != 'hodge':
            input_ports.add(target)  # Supplemental typed review slot, not a core DAG edit.
        if link['source_net'] == 'hodge':
            require(link['type'] == 'candidate_review' and link['source_port'] == 'candidate-contribution', 'candidate port type')
            available = by[link['source_node']]['verdict'] == 'constructed'
        else:
            require(link['type'] == 'research_reference' and link['source_port'] == 'research-context', 'reference port type')
            available = True  # Referenced node exists, not proof availability.
        connections.append(dict(link, available=available, logical_implication_asserted=False))
    require(a['external_obligations'] == [{'target_net': 'hodge', 'target_node': 'counterexample-assembly',
            'target_port': 'requires:independent-counterexample-review', 'type': 'reviewed_external_witness',
            'status': 'open', 'available': False}], 'independent review gate')
    for external in a['external_obligations']:
        key = (external['target_net'], external['target_node'], external['target_port'])
        require(key not in driven, 'external input already driven')
        driven.add(key)
    require(input_ports == driven, 'unwired or undeclared input port')
    return {'node_count': len(by), 'resolved_finite_control_nodes': 1, 'resolved_scope_nodes': 1,
            'resolved_dictionary_nodes': 1, 'resolved_literature_audits': 1, 'rejected_candidate_nodes': 27,
            'constructed_full37_CM_type_polarization_censuses': 1,
            'full37_CRT_excluded_classes': 8077,
            'full37_CRT_joint_necessary_survivors': 2,
            'full37_CRT_uncertified_classes': 98,
            'constructed_third_prime_and_generic_Hom_gates': 1,
            'three_prime_CRT_excluded_classes': 7457,
            'two_prime_classes_uncounted_at37': 36,
            'constructed_inert_elliptic_projector_gates': 1,
            'polarization_refined_CRT_excluded_classes': 201,
            'polarization_refined_CRT_uncertified_classes': 19,
            'constructed_off_reflection_two_prime_screens': 1,
            'two_prime_typed_CRT_excluded_classes': 197,
            'two_prime_CRT_uncertified_classes': 22,
            'constructed_off_reflection_a_line_screens': 1,
            'arithmetic_excluded_off_reflection_congruence_boxes': 12,
            'actual_next_off_reflection_control': None,
            'historical_last_off_reflection_control': [2,-1554,2],
            'active_refutation_nodes': direction_policy['active_refutation_nodes'],
            'active_refutation_count': direction_policy['active_refutation_count'],
            'dismissed_construction_count': direction_policy['dismissed_construction_count'],
            'constructed_actual_source_quotient_Jacobian_isogenies': 1,
            'rejected_reflection_symmetric_scalar_loci': 3,
            'source_quotient_isogeny_factor_dimensions': [3,5],
            'new_off_locus_scalar_source_controls': 1,
            'rejected_minimal_axis_scalar_controls_by_missing_second_CM_factor': 2,
            'constructed_minimal_axis_second_prime_screen': 1,
            'rejected_b6_source_by_prime29_CM_absence': 1,
            'b3_good_prime_CM_screens_survived': 2,
            'constructed_minimal_axis_b_line_screen': 1,
            'algebraic_b_congruence_classes_excluded_by_CM_ratio': 2,
            'new_rational_source_lifts_without_complex_second_axis': 2, 'rejected_secant_theorem_transplants': 1,
            'rejected_even_scalar_cover_transplants': 1,
            'resolved_asymmetric_scalar_cover_controls': 1,
            'resolved_asymmetric_curve_automorphism_certificates': 1,
            'resolved_asymmetric_Frobenius_certificates': 1,
            'rejected_asymmetric_target_transplants_by_absolute_simplicity': 1,
            'resolved_scalar_family_localizations': 1,
            'rejected_scalar_fixed_polarized_Y2_presentations': 1,
            'rejected_nonlifting_fixed_polarized_Y2_presentations': 1,
            'resolved_equivariant_tetragonal_gates': 1,
            'resolved_eightfold_literature_and_secant_audits': 1,
            'resolved_secant_local_Ext_gates': 1,
            'rejected_source_weak_semiregularity_transplants': 1,
            'rejected_eightfold_weak_criterion_repairs': 1,
            'constructed_auxiliary_ramified_trigonal_families': 1,
            'rejected_trigonal_principal_target_matches': 1,
            'rejected_Y2_etale_cyclic_quartic_principal_presentations': 1,
            'rejected_Y2_two_branch_cyclic_quartic_principal_presentations': 1,
            'constructed_even_axis_principal_models': 1,
            'constructed_common_cover_Kummer_reductions': 1,
            'constructed_joint_elliptic_degree_gates': 1,
            'constructed_scalar_sources_with_primitive_theta4_axis': 1,
            'excluded_Y3_principal_Jacobian_presentations': 1,
            'necessary_C9_gonality_if_fixed_cyclic_realization_exists': 4,
            'conditional_polarized_Y2_root_labels': 0,
            'conditional_unpolarized_isogeny_root_labels': 516,
            'rejected_mixed_commuting_Prym_factor_transplants': 1,
            'rejected_universal_bielliptic_lift_transplants': 1,
            'rejected_hyperelliptic_bottom_cover_families': 1,
            'rejected_Y2_Jacobian_low_gonality_transplants': 1,
            'rejected_fixed_polarization_Prym_membership_routes': 1,
            'rejected_cyclic_quartic_Prym_transplants': 1,
            'rejected_witness_libraries': 1,
            'resolved_candidate_constructions': 1, 'resolved_candidate_memberships': 1,
            'resolved_candidate_projector_gates': 4, 'resolved_full_Hodge_kernel_nodes': 1,
            'resolved_auxiliary_stabilizations': 1, 'resolved_eightfold_Weil_filters': 1,
            'resolved_full_eightfold_Hodge_kernel_nodes': 1, 'resolved_Chern_witness_transfers': 1,
            'resolved_reflexive_rank_reductions': 1, 'resolved_principal_Gaussian_isogenies': 1, 'resolved_indecomposable_principal_models': 1,
            'open_research_nodes': sum(n['status'] == 'open' for n in by.values()),
            'frontier': frontier, 'cross_net_connections': len(links), 'input_port_count': len(input_ports),
            'connections': connections, 'external_obligations': a['external_obligations']}


def source_paths(c, a):
    return set(a['contracts'].values()) | {ATTACHMENTS, c['guide'],
        'research/conjecture_net/graph_metrics.py',
        'research/conjecture_net/contracts/hodge-control-fixtures.v1.json',
        'research/voevodsky/checkers/check_hodge_obstruction_controls.py',
        'research/voevodsky/results/hodge-obstruction-controls-v1.json',
        Path(__file__).relative_to(ROOT).as_posix(),
        'research/voevodsky/checkers/test_hodge_conjecture_net.py'} | {
        item[key] for item in c['artifacts'] for key in ('contract', 'note', 'checker', 'receipt') if key in item
    } | audit_source_paths() | transplant_source_paths() | prym_source_paths() | principal_prym_sources() | y2_curve_sources() | commuting_sources() | frobenius_sources() | scalar_polarized_sources() | eightfold_literature_sources() | ramified_family_sources() | two_branch_sources() | minimal_frob_sources() | b_line_sources() | second_prime_sources() | a_line_sources() | joint_screen_sources() | third_sources() | census37_sources() | direction_sources() | {previous[key] for previous, prior in predecessors(c)
         for key in ('contract_snapshot', 'validation_snapshot', 'source_pins')}


def validate_pins(c, a, pins):
    require(pins['schema'] == 'marici.hodge-net-source-pins.v1' and
            set(pins['source_sha256']) == source_paths(c, a), 'source-pin coverage')
    for name, expected in pins['source_sha256'].items():
        require(digest(name) == expected, 'source drift: ' + name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    require(not (args.pin and args.check), 'choose pin or check')
    c, a, refs, controls, registry = load_bundle()
    pinpath = path(c['source_pins'])
    if args.pin:
        require(not pinpath.exists(), 'refusing to overwrite immutable pins; use a reviewed successor filename')
    wiring = validate(c, a, refs, controls, registry)
    if args.pin:
        require(not pinpath.exists(), 'refusing to overwrite immutable pins; use a reviewed successor filename')
        pins = {'schema': 'marici.hodge-net-source-pins.v1',
                'source_sha256': {name: digest(name) for name in sorted(source_paths(c, a))}}
        with pinpath.open('x', encoding='utf-8') as stream:
            stream.write(json.dumps(pins, indent=2) + '\n')
    pins = load(c['source_pins'])
    validate_pins(c, a, pins)
    result = {'schema': 'marici.hodge-conjecture-net-validation.v1', 'passed': True,
              'verification_level': 'Structural wiring, frozen scope, source freshness and finite control algebra; no Hodge or foundational proof.',
              'wiring': wiring, 'control_results': controls['results'],
              'Hodge_proved': False, 'Hodge_refuted': False, 'main_net_discharged': False,
              'source_sha256': pins['source_sha256']}
    if args.check:
        require(load(OUT.relative_to(ROOT).as_posix()) == result, 'validation receipt drift')
    else:
        OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('wiring', 'source_sha256', 'control_results')} |
                     {k: v for k, v in wiring.items() if k not in ('connections', 'external_obligations')}, indent=2))


if __name__ == '__main__':
    main()
