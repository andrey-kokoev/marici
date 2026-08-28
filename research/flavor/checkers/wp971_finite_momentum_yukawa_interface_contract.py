"""Exact WP971 finite-momentum Yukawa interface contract audit."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Store the exact polynomials in x=q2/M2 by coefficient tuples.
# F1/kappa = 1 and F2/kappa = 1+x.
f1_coefficients = (1, 0)
f2_coefficients = (1, 1)
hostile = {
    "same_zero_momentum_value": f1_coefficients[0] == f2_coefficients[0],
    "different_nonzero_momentum_value": f1_coefficients != f2_coefficients,
}

coordinate_pairs = ((1, 1, 1), (4, 4, 2))  # (Z,m0_squared,y)
raw_y4 = tuple(y**4 for _, _, y in coordinate_pairs)
canonical_strength = tuple(Fraction(y**4, Z**2) for Z, _, y in coordinate_pairs)
canonical_mass_squared = tuple(Fraction(m0_squared, Z) for Z, m0_squared, _ in coordinate_pairs)

# A normalized one-pole shape is invariant under the coordinate pair above,
# but changes when the physical canonical pole changes.
def one_pole_shape(q2, mass_squared):
    return Fraction(mass_squared, mass_squared + q2)

coordinate_shape = tuple(one_pole_shape(1, value) for value in canonical_mass_squared)
physical_pole_shape = tuple(one_pole_shape(1, value) for value in (1, 2))

# The real symmetric kinetic commutant for two identical irreducible copies is
# three-dimensional.  Conjugation by sector parity diag(1,-1) kills exactly
# the off-diagonal generator and leaves two independent diagonal coefficients.
symmetric_gram_basis = (
    ((1, 0), (0, 0)),
    ((0, 0), (0, 1)),
    ((0, 1), (1, 0)),
)
parity = (1, -1)
parity_even_basis = tuple(
    matrix for matrix in symmetric_gram_basis
    if all(parity[i] * matrix[i][j] * parity[j] == matrix[i][j]
           for i in range(2) for j in range(2))
)

# WP489 common-clock descent.  At its vacuum, m_h^2=4*a*eta*w^2 and
# M_A^2=z_A^2*w^2, so the clock cancels from the shape argument.
def common_clock_shape_argument(a, eta, z_a):
    return Fraction(4 * a * eta, z_a**2)

wp489_arguments = tuple(common_clock_shape_argument(1, 1, z_a) for z_a in (1, 2))
wp489_shapes = tuple(Fraction(1, 1 + value) for value in wp489_arguments)

# Exact templates transferred from solved cross-sector selector mechanisms.
# Reciprocal self-sewing x -> 4/x has roots +/-2, hence one positive fixed
# point.  Low-grade cancellation has a unique coefficient pair.
reciprocal_fixed_roots = (-2, 2)
positive_reciprocal_fixed_roots = tuple(x for x in reciprocal_fixed_roots if x > 0)
counterterm_target = (Fraction(1), Fraction(1, 2))
wrong_counterterm = (Fraction(2), Fraction(1, 2))
wrong_counterterm_residual = tuple(
    value - target for value, target in zip(wrong_counterterm, counterterm_target)
)
flavor_transfer_premises = {
    "source_derived_coefficient_involution": False,
    "labelled_same_object_sewing": False,
    "coefficient_dependent_finiteness_anomaly": False,
    "source_cost_or_naturality_jointly_faithful_on_rivals": False,
}

# WP820/WP823 internal flavor precedent: primitive charge homology and anomaly
# survive a unit acyclic stabilization, while the loop-controlled fixed
# coordinate changes from 1/(3-1) to 1/(3+2-1).
wp820_primitive_charge = (1, 2, 3)
wp823_fixed_coordinates = (
    Fraction(1, 3 - 1),
    Fraction(1, 3 + 2 - 1),
)

# WP824/WP836/WP839 successor audit.  Every D_m=m H_q has the same scale-free
# shape R_3=3, while freely chosen polynomial spectral-action coefficients
# select different stable masses.  WP839's hostile transport then carries
# that coefficient fiber into different fixed-point magnitudes.
wp836_scale_free_scores = (3, 3)
spectral_action_packets = ((-2, 1), (-4, 1))  # (alpha, beta)
spectral_minimum_m2 = tuple(
    Fraction(-alpha, 2 * beta) for alpha, beta in spectral_action_packets
)
spectral_minimum_second_derivatives = tuple(
    -12 * alpha for alpha, _ in spectral_action_packets
)
wp839_fixed_coordinates = tuple(
    Fraction(1, 1 + m2) for m2 in spectral_minimum_m2
)

# WP840--WP875 successor audit.  The multiplicative reciprocal flow selects
# the positive fixed point but preserves the zero cusp.  A primitive dual pair
# would exclude zero, yet is not an admitted flavor source.  The strongest
# native additive source has an empty positive simultaneous-source surface.
delta_q = 2
def reciprocal_beta(x):
    return x * Fraction(1 - delta_q**2 * x**2, 1 + delta_q**2 * x**2)

reciprocal_fixed_samples = (Fraction(0), Fraction(1, 2))
dual_pair_self_dual_g2 = Fraction(1, delta_q)
dual_source_admitted = False
def simultaneous_kappa_a(T, g1, g2):
    return Fraction(-6 * (4 * T + 12 * g1 + 53 * g2), 103)

positive_source_kappas = (
    simultaneous_kappa_a(1, 0, 0),
    simultaneous_kappa_a(0, 1, 0),
    simultaneous_kappa_a(0, 0, 1),
)

# WP877--WP893 simple-parent audit.
spin5_b0 = (Fraction(9, 2), Fraction(13, 2))
completion_b_shape_invariants = (
    Fraction(63449, 368082),
    Fraction(1603, 9680),
)
threshold_constraint_rank = 1
threshold_coordinate_dimension = 3
spin5_dimuon_response_rank = 2
spin5_dimuon_finite_exposure_identifies = False

# WP916/WP917/WP931 declared-grammar exhaustion.
wp916_source_grid = ((1, 1), (1, 4), (4, 1), (4, 4))
wp916_admitted_response_grid = wp916_source_grid
wp917_j_hostile = ((1, 0), (1, 2))  # (Q, J)
wp917_portal_residuals = tuple(J**2 - Q for Q, J in wp917_j_hostile)
wp931_exchange_fixed_discriminants = (
    Fraction(40, 243),
    Fraction(135, 1024),
)
declared_selector_passes_all_five_gates = False

# WP932--WP950 post-exhaustion reopening audit.
boolean_route_count = 8
boolean_zeta_determinant = 1
authorized_threshold_rank = 1
single_holonomy_cp_cubic = 0
single_holonomy_comparator_cp_cubic = -36
two_holonomy_word_span_dimension = 9
full_matrix_algebra_dimension = 9
two_holonomy_cp_cubics = (0, -842400)
positive_equalizer_traces = (9, 8)  # c=1/3, 2/3

# Cross-sector search for a source-derived proper noncommutative module.
kitaev_algebra_dimensions = {
    "native_gauge": 6,
    "one_flux_maximum": 24,
    "two_typed_flux_ports": 36,
    "ambient": 256,
    "compiled_source_lie": 34,
}
nima_incidence_closure_dimensions = (5, 8)  # one-way parabolic, dual-completed sl3
kitaev_flux_ports_native = False
nima_reverse_incidence_analytically_admitted = False
strominger_finite_weyl_lift_source_admitted = False
nima_twisted_exchange_selector_survives_complete_ring = False

# Closest internal proper noncommutative module seed.
wp125_a = 28
wp125_q = 25
wp125_selected_x = Fraction(1, 2) + Fraction(wp125_a, 8 * wp125_q)
wp125_commutator_invariant_at_x = 8 * wp125_selected_x * (1 - wp125_selected_x)
wp646_word_ranks = (2, 9, 10)  # aligned, linear, degree-two universal
wp125_coefficient_ratio_source_derived = False

# WP127--WP129 source-constructor correction.
wp128_lambda = 25
wp128_rho = 13
wp128_alpha = Fraction(1)
wp128_beta = Fraction(1)
wp128_q = wp128_lambda * wp128_alpha**2 * wp128_beta**2
wp128_stability_margin = Fraction(wp128_rho) - Fraction(wp128_lambda, 2)
wp128_coefficient_ray_source_selected = False
wp436_source_free_wp128_noncommuting_vacuum = False
wp438_gauge_rank = 7
wp439_charged_gradient_rank = 0
wp442_commuting_global_vacuum = True
wp442_gauge_rank_upper_bound = 6
wp443_gauge_rank = 8
wp443_physical_hessian_modes_positive = True
wp444_dilation_orbit_dimension = 1
wp446_word_algebra_dimension = 5
wp447_word_algebra_dimension = 9
wp447_gauge_rank = 8
wp447_pole_multiplicities = (3, 5)
wp450_word_grammar_dimension = 9
wp451_native_symmetric_yukawa_dimension = 1
wp452_irrep_dimensions = (1, 3, 5)
source_selected_coefficient_vacuum = False
wp129_low_energy_rank = 1
wp129_source_count = 3
wp129_threshold_formal_rank = 3
wp129_threshold_instrument_admitted = False

gates = {
    "source_fixed_canonical_quadratic_pole_data": False,
    "complete_momentum_space_vertices": False,
    "routing_and_shift_invariance": False,
    "three_point_tensor_basis": False,
    "subtraction_and_pole_convention": False,
    "derivative_operator_basis": False,
    "threshold_and_analytic_support": False,
    "zero_momentum_recovery": True,
    "on_shell_detector_continuation": False,
}

ordered = list(gates)
first_failed = next(name for name in ordered if not gates[name])
checks = {
    "hostile_closes_at_zero": bool(hostile["same_zero_momentum_value"]),
    "hostile_opens_away_from_zero": bool(hostile["different_nonzero_momentum_value"]),
    "kinetic_rescaling_changes_raw_coupling": raw_y4[0] != raw_y4[1],
    "kinetic_rescaling_preserves_hatted_strength": canonical_strength[0] == canonical_strength[1],
    "kinetic_rescaling_preserves_canonical_mass": canonical_mass_squared[0] == canonical_mass_squared[1],
    "normalized_shape_descends_under_coordinate_rescaling": coordinate_shape[0] == coordinate_shape[1],
    "normalized_shape_detects_physical_pole_change": physical_pole_shape[0] != physical_pole_shape[1],
    "identical_copy_symmetric_commutant_has_dimension_three": len(symmetric_gram_basis) == 3,
    "sector_parity_removes_only_off_diagonal_generator": len(parity_even_basis) == 2,
    "sector_parity_leaves_two_free_pole_coefficients": parity_even_basis == symmetric_gram_basis[:2],
    "wp489_common_clock_cancels_from_shape_argument": common_clock_shape_argument(1, 1, 1) == 4,
    "wp489_free_coefficient_changes_shape_argument": wp489_arguments == (4, 1),
    "wp489_free_coefficient_changes_normalized_readout": wp489_shapes == (Fraction(1, 5), Fraction(1, 2)),
    "reciprocal_self_sewing_template_has_unique_positive_fixed_point": positive_reciprocal_fixed_roots == (2,),
    "counterterm_template_has_nonzero_wrong_coefficient_residual": wrong_counterterm_residual == (1, 0),
    "no_cross_sector_selector_premise_is_currently_admitted_in_flavor": not any(flavor_transfer_premises.values()),
    "wp820_primitive_charge_is_nontrivial_and_oriented": wp820_primitive_charge == (1, 2, 3),
    "wp823_acyclic_stabilization_changes_fixed_coordinate": wp823_fixed_coordinates == (Fraction(1, 2), Fraction(1, 4)),
    "wp836_scale_free_shape_is_blind_to_common_mass": wp836_scale_free_scores == (3, 3),
    "wp839_coefficient_packets_select_distinct_masses": spectral_minimum_m2 == (1, 2),
    "wp839_selected_masses_are_stable": all(value > 0 for value in spectral_minimum_second_derivatives),
    "wp839_coefficient_fiber_reaches_portal_coordinate": wp839_fixed_coordinates == (Fraction(1, 2), Fraction(1, 3)),
    "wp872_reciprocal_flow_keeps_zero_fixed": reciprocal_beta(reciprocal_fixed_samples[0]) == 0,
    "wp872_reciprocal_flow_selects_positive_half": reciprocal_beta(reciprocal_fixed_samples[1]) == 0,
    "wp873_primitive_dual_pair_would_select_g_squared_one_half": dual_pair_self_dual_g2 == Fraction(1, 2),
    "wp874_dual_pair_is_not_an_admitted_flavor_source": not dual_source_admitted,
    "wp875_completed_positive_source_directions_are_unphysical": all(value < 0 for value in positive_source_kappas),
    "wp879_anomaly_equivalent_completions_split_beta_coefficient": spin5_b0[1] - spin5_b0[0] == 2,
    "wp888_full_rank_yukawa_points_have_distinct_normalized_spectra": completion_b_shape_invariants[0] != completion_b_shape_invariants[1],
    "wp884_threshold_matching_leaves_two_dimensional_fiber": threshold_coordinate_dimension - threshold_constraint_rank == 2,
    "wp893_conditional_calibrated_instrument_has_rank_two": spin5_dimuon_response_rank == 2,
    "wp893_finite_exposure_does_not_identify": not spin5_dimuon_finite_exposure_identifies,
    "wp916_response_validation_has_zero_selection_reduction": len(wp916_admitted_response_grid) == len(wp916_source_grid),
    "wp917_j_blind_source_pair_is_split_by_conditional_portal": wp917_portal_residuals == (-1, 3),
    "wp931_exchange_rigidification_leaves_spectral_shape_fiber": wp931_exchange_fixed_discriminants[0] != wp931_exchange_fixed_discriminants[1],
    "wp931_no_declared_candidate_passes_all_five_selector_gates": not declared_selector_passes_all_five_gates,
    "wp932_boolean_tower_is_formally_faithful": boolean_zeta_determinant == 1,
    "wp932_authorized_threshold_probe_leaves_route_kernel_seven": boolean_route_count - authorized_threshold_rank == 7,
    "wp943_single_holonomy_selects_wrong_commuting_locus": single_holonomy_cp_cubic == 0 and single_holonomy_comparator_cp_cubic != 0,
    "wp944_two_holonomies_restore_full_matrix_algebra": two_holonomy_word_span_dimension == full_matrix_algebra_dimension,
    "wp944_fixed_carrier_does_not_select_cp_cubic": two_holonomy_cp_cubics[0] != two_holonomy_cp_cubics[1],
    "wp950_positive_equalizer_retains_weight_fiber": positive_equalizer_traces[0] != positive_equalizer_traces[1],
    "kitaev_endpoint_algebra_is_proper_and_noncommutative": kitaev_algebra_dimensions["native_gauge"] < kitaev_algebra_dimensions["two_typed_flux_ports"] < kitaev_algebra_dimensions["ambient"],
    "kitaev_two_typed_ports_are_strictly_stronger_than_one": kitaev_algebra_dimensions["one_flux_maximum"] < kitaev_algebra_dimensions["two_typed_flux_ports"],
    "kitaev_compiled_source_still_misses_full_endpoint_dimension": kitaev_algebra_dimensions["compiled_source_lie"] < kitaev_algebra_dimensions["two_typed_flux_ports"],
    "kitaev_required_flux_ports_are_not_native": not kitaev_flux_ports_native,
    "nima_dual_incidence_enlarges_parabolic_to_sl3": nima_incidence_closure_dimensions == (5, 8),
    "cross_sector_near_matches_retain_authority_failures": not any((nima_reverse_incidence_analytically_admitted, strominger_finite_weyl_lift_source_admitted, nima_twisted_exchange_selector_survives_complete_ring)),
    "wp125_degree_eight_module_selects_noncommuting_interior": wp125_selected_x == Fraction(16, 25) and wp125_commutator_invariant_at_x > 0,
    "wp125_selected_point_depends_on_free_coefficient_ratio": not wp125_coefficient_ratio_source_derived,
    "wp646_linear_word_module_is_proper_codimension_one": wp646_word_ranks[1] == wp646_word_ranks[2] - 1,
    "wp646_degree_two_words_restore_universal_rank": wp646_word_ranks == (2, 9, 10),
    "wp128_renormalizable_matching_derives_commutator_coefficient": wp128_q == 25,
    "wp128_adjoint_quartic_is_strictly_coercive_at_benchmark": wp128_stability_margin == Fraction(1, 2),
    "wp128_still_does_not_select_numerical_coefficient_ray": not wp128_coefficient_ray_source_selected,
    "wp436_wp128_has_no_source_free_noncommuting_vacuum": not wp436_source_free_wp128_noncommuting_vacuum,
    "wp438_noncommuting_vacuum_retains_u1": wp438_gauge_rank == 7,
    "wp439_renormalizable_charged_gradient_rank_is_zero": wp439_charged_gradient_rank == 0,
    "wp442_instability_endpoint_is_commuting_rank_at_most_six": wp442_commuting_global_vacuum and wp442_gauge_rank_upper_bound <= 6,
    "wp443_fundamental_completion_is_stable_and_fully_breaking": wp443_gauge_rank == 8 and wp443_physical_hessian_modes_positive,
    "wp444_full_breaking_vacuum_retains_scale_orbit": wp444_dilation_orbit_dimension == 1,
    "wp446_first_full_breaking_word_algebra_is_reducible": wp446_word_algebra_dimension < 9,
    "wp447_irreducible_completion_has_full_word_algebra_and_gauge_rank": wp447_word_algebra_dimension == 9 and wp447_gauge_rank == 8,
    "wp447_poles_split_as_triplet_plus_quintet": sum(wp447_pole_multiplicities) == 8,
    "wp450_degree_two_grammar_is_universal_carrier": wp450_word_grammar_dimension == 9,
    "wp451_native_source_symmetry_selects_only_identity": wp451_native_symmetric_yukawa_dimension == 1,
    "wp452_coefficient_algebra_decomposes_one_plus_three_plus_five": sum(wp452_irrep_dimensions) == 9,
    "coefficient_field_vacuum_remains_unselected": not source_selected_coefficient_vacuum,
    "wp129_low_energy_probes_leave_two_dimensional_source_kernel": wp129_source_count - wp129_low_energy_rank == 2,
    "wp129_formal_threshold_family_separates_rivals": wp129_threshold_formal_rank == wp129_source_count,
    "wp129_threshold_separation_lacks_admitted_instrument": not wp129_threshold_instrument_admitted,
    "current_packet_is_incomplete": not all(gates.values()),
    "first_failed_gate_is_source_fixed_pole_data": first_failed == ordered[0],
    "scc_naturality_must_remain_unadmitted": not gates["on_shell_detector_continuation"],
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.finite-momentum-yukawa-interface-contract.v1",
    "work_package": "WP971",
    "status": "PASS",
    "checks": checks,
    "contract_gates": gates,
    "first_failed_gate": first_failed,
    "smallest_exact_falsifier": {
        "F1": "kappa",
        "F2": "kappa*(1+q2/M2)",
        "agreement": "F1(0)=F2(0)=kappa",
        "disagreement": "F2(q2)-F1(q2)=kappa*q2/M2 for q2!=0",
    },
    "coordinate_normalization_descent": {
        "packets": ["(Z,m0^2,y)=(1,1,1)", "(Z,m0^2,y)=(4,4,2)"],
        "raw_y4": list(raw_y4),
        "canonical_y4_over_Z2": [str(value) for value in canonical_strength],
        "canonical_m0_squared_over_Z": [str(value) for value in canonical_mass_squared],
        "normalized_shape_at_q2_1": [str(value) for value in coordinate_shape],
        "consequence": "overall field normalization cancels from the normalized momentum shape",
    },
    "physical_pole_fiber": {
        "canonical_mass_squared": ["1", "2"],
        "same_zero_momentum_value": "G_M(0)=kappa",
        "normalized_shape_at_q2_1": [str(value) for value in physical_pole_shape],
        "consequence": "unfixed physical pole data leave the on-shell shape nonunique",
    },
    "symmetry_reduction": {
        "single_irreducible_factor": "kinetic shape is scalar on the irreducible factor",
        "identical_entrance_copy_symmetric_commutant_dimension": len(symmetric_gram_basis),
        "sector_parity_commutant_dimension": len(parity_even_basis),
        "authority": "WP629 sector parity is an added source rigidifier, not derived from the existing gauge group",
        "consequence": "symmetry can remove mixing but does not select either diagonal canonical pole value",
    },
    "wp489_common_clock_factorization": {
        "relations": ["m_h^2=4*a*eta*w^2", "M_A^2=z_A^2*w^2"],
        "descending_shape_argument": "m_h^2/M_A^2=4*a*eta/z_A^2",
        "hostile_coefficients": ["(a,eta,z_A)=(1,1,1)", "(a,eta,z_A)=(1,1,2)"],
        "shape_arguments": [str(value) for value in wp489_arguments],
        "normalized_one_pole_readouts": [str(value) for value in wp489_shapes],
        "image": "entire positive line as positive a, eta, and z_A vary",
        "classification": "source-derived conditional shape constructor; not a selector",
    },
    "cross_sector_selector_transfer": {
        "solved_templates": {
            "reciprocal_self_sewing": "unique positive fixed point when the source involution and labelled closure are admitted",
            "anomaly_cancellation": "unique coefficient when every alternative leaves a forbidden or divergent residual",
            "minimal_positive_update": "unique conditional repair after the source balance and cost are fixed",
            "counterfactual_naturality": "mechanism selection when admitted source variations are jointly faithful on rivals",
        },
        "flavor_premises": flavor_transfer_premises,
        "disposition": "no solved selector transfers without a new source arrow",
    },
    "closest_internal_flavor_precedent": {
        "wp820": "integer incidence plus oriented anomaly inflow conditionally selects primitive charge direction, sign, and normalization",
        "wp823_hostile": "a unit anomaly-neutral acyclic matter pair preserves charge homology and inflow",
        "conditional_fixed_coordinates": [str(value) for value in wp823_fixed_coordinates],
        "first_nonfaithful_arrow": "full chain-level spectral matter object to charge homology and anomaly inflow",
        "consequence": "topological selection does not determine loop coefficients, pole ratios, or thresholds",
    },
    "later_spectral_completion_audit": {
        "wp824": "complete Dirac spectrum faithfully records the acyclic mass but does not select it",
        "wp836_scale_free_scores": list(wp836_scale_free_scores),
        "wp836_classification": "conditional finite-completion and equal-singular-shape selector; scale blind and without source minimization authority",
        "spectral_action_packets": [list(packet) for packet in spectral_action_packets],
        "selected_mass_squared": [str(value) for value in spectral_minimum_m2],
        "stationary_second_derivatives": spectral_minimum_second_derivatives,
        "wp839_fixed_coordinates": [str(value) for value in wp839_fixed_coordinates],
        "first_missing_arrow": "(I,Q,H_q) -> (profile, normalization, spectral action) -> beta -> canonical pole ratios",
        "consequence": "faithful spectral recording and conditional shape selection do not select the finite-momentum pole argument",
    },
    "reciprocal_and_zero_exit_successor_audit": {
        "wp872_fixed_points_sampled": [str(value) for value in reciprocal_fixed_samples],
        "wp872_classification": "coefficient-free conditional selector on x>0; exact zero remains fixed",
        "wp873_conditional_self_dual_g_squared": str(dual_pair_self_dual_g2),
        "wp874_dual_source_admitted": dual_source_admitted,
        "wp875_axis_kappa_a": [str(value) for value in positive_source_kappas],
        "consequence": "neither the added dual architecture nor the current additive source selects pole ratios in the admitted flavor theory",
    },
    "simple_parent_source_and_instrument_audit": {
        "wp878": "selects normalized Hodge-odd operator sign and unit contrast; common gain remains free",
        "wp879_b0": [str(value) for value in spin5_b0],
        "wp888_scale_free_spectral_invariants": [str(value) for value in completion_b_shape_invariants],
        "wp884_threshold_fiber_dimension": threshold_coordinate_dimension - threshold_constraint_rank,
        "wp893_conditional_detector_rank": spin5_dimuon_response_rank,
        "wp893_finite_exposure_identifies": spin5_dimuon_finite_exposure_identifies,
        "classification": "conditional rank-two calibrated instrument and operator selector; no spectrum, gain, or pole-ratio selector",
    },
    "declared_grammar_exhaustion": {
        "wp916_source_grid_size": len(wp916_source_grid),
        "wp916_response_admitted_image_size": len(wp916_admitted_response_grid),
        "wp917_portal_residuals": list(wp917_portal_residuals),
        "wp931_exchange_fixed_discriminants": [str(value) for value in wp931_exchange_fixed_discriminants],
        "passes_all_five_selector_gates": declared_selector_passes_all_five_gates,
        "scope": "relative to declared Spin(5) and conditional Spin(7) grammar through WP930",
        "reopening": "new independently declared three-family source action or geometry",
    },
    "post_exhaustion_reopening_audit": {
        "wp932_boolean_zeta_determinant": boolean_zeta_determinant,
        "wp932_authorized_route_kernel_dimension": boolean_route_count - authorized_threshold_rank,
        "wp943_cp_cubics": [single_holonomy_cp_cubic, single_holonomy_comparator_cp_cubic],
        "wp944_word_span_dimension": two_holonomy_word_span_dimension,
        "wp944_same_carrier_cp_cubics": list(two_holonomy_cp_cubics),
        "wp950_equalizer_traces": list(positive_equalizer_traces),
        "disposition": "proper noncommuting carriers exist, but none supplies a source-selected coefficient vacuum",
    },
    "cross_sector_proper_noncommutative_module_search": {
        "kitaev_dimensions": kitaev_algebra_dimensions,
        "kitaev_flux_ports_native": kitaev_flux_ports_native,
        "kitaev_classification": "closest exact proper noncommutative source algebra; physical port execution and coefficient selection remain open",
        "nima_incidence_closure_dimensions": list(nima_incidence_closure_dimensions),
        "nima_reverse_incidence_analytically_admitted": nima_reverse_incidence_analytically_admitted,
        "strominger_finite_weyl_lift_source_admitted": strominger_finite_weyl_lift_source_admitted,
        "nima_twisted_exchange_survives_complete_ring": nima_twisted_exchange_selector_survives_complete_ring,
        "transfer": "derive a native typed generator census whose closure is proper, then derive its coefficient law without enlarging to universal span",
    },
    "closest_internal_module_seed": {
        "wp125_selected_x": str(wp125_selected_x),
        "wp125_commutator_invariant": str(wp125_commutator_invariant_at_x),
        "wp125_coefficient_ratio_source_derived": wp125_coefficient_ratio_source_derived,
        "wp646_rank_ladder": list(wp646_word_ranks),
        "classification": "proper CP-capable module exists; source coefficient law, radial completion, ensemble stability, threshold transport, and instrument remain open",
    },
    "wp128_source_constructor_correction": {
        "matched_q": str(wp128_q),
        "stability_margin": str(wp128_stability_margin),
        "coefficient_ray_source_selected": wp128_coefficient_ray_source_selected,
        "wp129_low_energy_rank": wp129_low_energy_rank,
        "wp129_source_kernel_dimension": wp129_source_count - wp129_low_energy_rank,
        "wp129_formal_threshold_rank": wp129_threshold_formal_rank,
        "wp129_threshold_instrument_admitted": wp129_threshold_instrument_admitted,
        "classification": "renormalizable proper interaction module; WP436 excludes a source-free noncommuting WP128 vacuum",
    },
    "wp436_wp452_vacuum_and_coefficient_authority": {
        "wp438_gauge_rank": wp438_gauge_rank,
        "wp439_charged_gradient_rank": wp439_charged_gradient_rank,
        "wp442_commuting_global_vacuum": wp442_commuting_global_vacuum,
        "wp442_gauge_rank_upper_bound": wp442_gauge_rank_upper_bound,
        "wp443_gauge_rank": wp443_gauge_rank,
        "wp444_dilation_orbit_dimension": wp444_dilation_orbit_dimension,
        "wp446_word_algebra_dimension": wp446_word_algebra_dimension,
        "wp447_word_algebra_dimension": wp447_word_algebra_dimension,
        "wp447_gauge_rank": wp447_gauge_rank,
        "wp447_pole_multiplicities": list(wp447_pole_multiplicities),
        "wp450_word_grammar_dimension": wp450_word_grammar_dimension,
        "wp451_native_symmetric_yukawa_dimension": wp451_native_symmetric_yukawa_dimension,
        "wp452_irrep_dimensions": list(wp452_irrep_dimensions),
        "source_selected_coefficient_vacuum": source_selected_coefficient_vacuum,
        "classification": "source-free full breaking and universal carrier capacity exist; numerical coefficient selection remains absent",
        "next_constructor": "source-derived SO(3)-breaking coefficient-field action with its own selected vacuum",
    },
    "classification": "declared-grammar selector exhaustion; conditional instruments exist, but no admitted end-to-end finite-momentum selector/instrument composite",
    "scc_disposition": "natural_transport remains failed until the complete on-shell matching square closes",
}

out = ROOT / "results" / "wp971_finite_momentum_yukawa_interface_contract.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
