"""Exact compiler for quotients/completions preceding partial repairs."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb
from typing import Any


def rref(matrix: list[list[int | Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return a, []
    rows, cols, pivot_row = len(a), len(a[0]), 0
    pivots: list[int] = []
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return a, pivots


@lru_cache(maxsize=None)
def canonical_plucker_cover_counts(row_count: int) -> tuple[int, int, int, int]:
    """Return relation count, incidence count, incident minors, and max degree."""
    relation_count = comb(row_count, 5) if row_count >= 5 else 0
    incidences: dict[tuple[int, int, int], int] = {}
    for a, b, c, d, e in combinations(range(row_count), 5):
        relation_minors = {(a,b,c),(a,d,e),(a,b,d),(a,c,e),(a,b,e),(a,c,d)}
        for minor in relation_minors:
            incidences[minor] = incidences.get(minor, 0) + 1
    return relation_count, sum(incidences.values()), len(incidences), max(incidences.values(), default=0)


def nullspace(matrix: list[list[int | Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(matrix)
    cols = len(matrix[0]) if matrix else 0
    free = [j for j in range(cols) if j not in pivots]
    basis = []
    for j in free:
        vector = [Fraction(0) for _ in range(cols)]
        vector[j] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][j]
        basis.append(vector)
    return basis


def matvec(matrix: list[list[int | Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((Fraction(x) * y for x, y in zip(row, vector)), Fraction(0)) for row in matrix]


def rowmat(row: list[Fraction], matrix: list[list[int | Fraction]]) -> list[Fraction]:
    return [sum((row[i] * Fraction(matrix[i][j]) for i in range(len(row))), Fraction(0)) for j in range(len(matrix[0]))]


def normalize_constructor_words(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    valuations = dict(left.get("valuations", {}))
    conflict = any(prime in valuations and valuations[prime] != order for prime, order in right.get("valuations", {}).items())
    if not conflict:
        valuations.update(right.get("valuations", {}))
    mellin = Fraction(*left.get("mellin", [0, 1])) + Fraction(*right.get("mellin", [0, 1]))
    return {"zero": conflict, "valuations": {} if conflict else dict(sorted(valuations.items(), key=lambda item: int(item[0]))), "mellin": mellin}


def quadratic_form(matrix: list[list[int | Fraction]], vector: list[int | Fraction]) -> Fraction:
    v = [Fraction(value) for value in vector]
    return sum((v[i] * Fraction(matrix[i][j]) * v[j] for i in range(len(v)) for j in range(len(v))), Fraction(0))


def exact_descent_gate(quotient: list[list[int]], distinction: list[list[int]]) -> dict[str, Any]:
    killed = nullspace(quotient)
    witness = next((v for v in killed if any(matvec(distinction, v))), None)
    return {
        "descends": witness is None,
        "criterion": "ker(quotient) subseteq ker(required_distinction)",
        "killed_dimension": len(killed),
        "witness": [str(x) for x in witness] if witness else None,
        "distinction_image": [str(x) for x in matvec(distinction, witness)] if witness else None,
    }


def nonsurjective_integer_factorization_gate(fixture: dict[str, Any]) -> dict[str, Any]:
    q = int(fixture.get("quotient_multiplier", 0))
    observation = int(fixture.get("observation_multiplier", 0))
    required_factor = Fraction(observation, q) if q else None
    integer_factor_exists = required_factor is not None and required_factor.denominator == 1
    kernel_inclusion = q != 0 or observation == 0
    quotient_surjective = abs(q) == 1
    factor_through_image = q != 0
    errors = []
    if fixture.get("base_ring") != "Z" or kernel_inclusion != fixture.get("kernel_inclusion") or quotient_surjective != fixture.get("quotient_surjective"):
        errors.append("nonsurjective_integer_fixture_invalid")
    if integer_factor_exists != fixture.get("factor_through_declared_codomain") or factor_through_image != fixture.get("factor_through_image") or [required_factor.numerator, required_factor.denominator] != fixture.get("required_fractional_factor"):
        errors.append("nonsurjective_factorization_semantics_changed")
    return {
        "passed": not errors,
        "errors": errors,
        "kernel_inclusion": kernel_inclusion,
        "quotient_surjective": quotient_surjective,
        "integer_factor_exists": integer_factor_exists,
        "factor_through_image": factor_through_image,
        "required_fractional_factor": str(required_factor),
        "theorem": "kernel inclusion is sufficient through a canonical quotient or surjective presentation, but not through an arbitrary declared codomain over a general ring",
    }


def complex_pair(value: dict[str, list[int]]) -> tuple[Fraction, Fraction]:
    return Fraction(*value["re"]), Fraction(*value["im"])


def complex_mul(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def norm_squared(value: tuple[Fraction, Fraction]) -> Fraction:
    return value[0] ** 2 + value[1] ** 2


def compile_contract(contract: dict[str, Any]) -> dict[str, Any]:
    fixtures = {}
    errors: list[str] = []
    for fixture in contract.get("finite_fixtures", []):
        observed = exact_descent_gate(fixture["quotient_matrix"], fixture["required_distinction_matrix"])
        observed["expected_descends"] = fixture["expected_descends"]
        observed["passed"] = observed["descends"] == fixture["expected_descends"]
        fixtures[fixture["fixture_id"]] = observed
        if not observed["passed"]:
            errors.append("finite_fixture_mismatch:" + fixture["fixture_id"])
    nonsurjective_hostile = nonsurjective_integer_factorization_gate(contract.get("nonsurjective_factorization_hostile", {}))
    errors.extend(nonsurjective_hostile["errors"])

    theta = contract["theta_application"]
    finite_incidence = theta["finite_incidence"]
    if finite_incidence["P"]["formula"] != "p^(-1/2) delta_(log p)":
        errors.append("primitive_incidence_changed")
    if finite_incidence["Q"]["formula"] != "(1/2)p^(-1) delta_(2 log p)":
        errors.append("square_incidence_changed")
    if theta["completion_classes"]["P"] == theta["completion_classes"]["Q"]:
        errors.append("primitive_square_completion_types_conflated")
    if theta["completed_scalar_readout_authorized"]:
        errors.append("finite_incidence_laundered_to_scalar_completion")
    joint = theta.get("joint_global_completion", {})
    if not joint.get("source_authorized") or joint.get("gradewise_scalar_pushforward"):
        errors.append("global_tate_completion_mistyped")
    if theta.get("operator_lift", {}).get("source_authorized"):
        errors.append("scalar_tate_section_laundered_to_seam_operator")
    trace = theta.get("trace_obstruction", {})
    if trace.get("bounded_L2_restriction_exists") or not trace.get("source_test_space_restriction_exists"):
        errors.append("idelic_null_boundary_mistyped")
    line = theta.get("seam_line_system", {})
    transitions = [complex_pair(value) for value in line.get("unitary_transitions", [])]
    composite = complex_mul(transitions[1], transitions[0]) if len(transitions) == 2 else None
    seam_unitary = bool(transitions) and all(norm_squared(value) == 1 for value in transitions)
    off_seam = complex_pair(line["off_seam_transition"])
    off_seam_unitary = norm_squared(off_seam) == 1
    transported_metrics = [Fraction(1)]
    for _ in range(line.get("off_seam_repetitions", 0)):
        transported_metrics.append(transported_metrics[-1] / norm_squared(off_seam))
    raw_tensor = line.get("raw_reference_tensor", {})
    repair = theta.get("renormalization_trace_gate", {})
    metric_constructor = repair.get("metric_reference_constructor", {})
    trace_constructor = repair.get("rigged_trace_constructor", {})
    transition = Fraction(*metric_constructor["transition"])
    scales = [Fraction(*value) for value in metric_constructor["coordinate_scales"]]
    covectors = [Fraction(*value) for value in metric_constructor["original_pairing_covectors"]]
    normalized_transition = scales[1] * transition / scales[0]
    transported_covectors = [covectors[i] / scales[i] for i in range(2)]
    pairing_compatible_before = covectors[1] * transition == covectors[0]
    pairing_compatible_after = transported_covectors[1] * normalized_transition == transported_covectors[0]
    hostile_covectors = [Fraction(*value) for value in repair["hostile_scalar_only_covectors"]]
    hostile_pairing_compatible = hostile_covectors[1] * normalized_transition == hostile_covectors[0]
    induced = repair.get("pairing_induced_metric", {})
    nonzero_covectors = [Fraction(*value) for value in induced.get("nonzero_pairing_covectors", [])]
    zero_covectors = [Fraction(*value) for value in induced.get("zero_divisor_covectors", [])]
    original_metrics = [Fraction(1), Fraction(1, 4)]
    pairing_metric_ratios = [nonzero_covectors[i] ** 2 / original_metrics[i] for i in range(2)]
    pairing_induces_positive_metric = bool(nonzero_covectors) and all(value != 0 for value in nonzero_covectors)
    zero_pairing_induces_metric = bool(zero_covectors) and all(value != 0 for value in zero_covectors)
    jet_atlas = theta.get("jet_atlas", {})
    adaptive = jet_atlas.get("adaptive_constructor", {})
    reflection = theta.get("reflection_jet_gate", {})
    line_metric = theta.get("reflection_line_metric_gate", {})
    reflection_cell = theta.get("direct_limit_reflection_cell", {})
    off_uniform = theta.get("off_seam_uniform_comparison_gate", {})
    relative_trace = theta.get("relative_ambient_trace_gate", {})
    weighted_rigging = theta.get("weighted_source_rigging_gate", {})
    pro_gram = theta.get("pro_gram_endpoint_gate", {})
    endpoint_orbit = theta.get("endpoint_orbit_completion_gate", {})
    observability = theta.get("endpoint_observability_gate", {})
    doubled_green = theta.get("doubled_green_residual_gate", {})
    indexed_endpoint = theta.get("indexed_endpoint_capability_gate", {})
    constructor_normal = theta.get("constructor_normal_form_gate", {})
    mellin_saturation = theta.get("mellin_saturated_completion_gate", {})
    detector_clark = theta.get("relative_detector_poisson_clark_gate", {})
    poisson_lift = theta.get("poisson_matrix_lift_gate", {})
    poisson_gauge = theta.get("poisson_lift_gauge_gate", {})
    reflection_pairing = theta.get("reflection_pairing_nonuniqueness_gate", {})
    sector_normalization = theta.get("reflection_sector_normalization_gate", {})
    pairing_reconstruction = theta.get("reflection_pairing_reconstruction_gate", {})
    four_channel_reflection = theta.get("four_channel_reflection_multiplicity_gate", {})
    four_channel_source = theta.get("four_channel_source_action_gate", {})
    six_probe = theta.get("six_probe_pairing_reconstruction_gate", {})
    symmetric_observability = theta.get("symmetric_square_observability_gate", {})
    reflection_orbit_observability = theta.get("reflection_orbit_observability_gate", {})
    even_jet_observability = theta.get("even_jet_observability_gate", {})
    symmetric_square_gauge = theta.get("symmetric_square_gauge_character_gate", {})
    determinant_line = theta.get("observability_determinant_line_gate", {})
    observability_divisor = theta.get("observability_divisor_gate", {})
    local_smith = theta.get("local_smith_observability_gate", {})
    determinantal_divisors = theta.get("determinantal_divisor_reconstruction_gate", {})
    defect_barcode = theta.get("defect_module_barcode_gate", {})
    derived_specialization = theta.get("derived_specialization_kernel_gate", {})
    defect_variance = theta.get("observability_defect_variance_gate", {})
    kernel_cokernel_duality = theta.get("kernel_cokernel_duality_gate", {})
    green_adjointness = theta.get("green_adjointness_residual_gate", {})
    lagrangian_boundary = theta.get("lagrangian_boundary_condition_gate", {})
    boundary_kernel_dependence = theta.get("boundary_selection_kernel_dependence_gate", {})
    boundary_selector = theta.get("boundary_selector_insufficiency_gate", {})
    orbit_selector = theta.get("orbit_separating_selector_gate", {})
    selector_torsor = theta.get("selector_torsor_gate", {})
    selector_wall = theta.get("selector_wall_kernel_jump_gate", {})
    kernel_incidence = theta.get("lagrangian_kernel_incidence_gate", {})
    incidence_stratification = theta.get("lagrangian_incidence_stratification_gate", {})
    graph_smith = theta.get("lagrangian_graph_smith_barcode_gate", {})
    smith_chart = theta.get("boundary_smith_chart_invariance_gate", {})
    simultaneous_transport = theta.get("simultaneous_boundary_transport_gate", {})
    operator_transport = theta.get("operator_transport_square_gate", {})
    relative_injectivity = theta.get("relative_codomain_injectivity_gate", {})
    transport_residue = theta.get("kernel_transport_residue_sequence_gate", {})
    composite_residue = theta.get("composite_transport_residue_filtration_gate", {})
    factorization_flag = theta.get("factorization_dependent_residue_flag_gate", {})
    flag_comparison = theta.get("residue_flag_comparison_torsor_gate", {})
    flag_triangle = theta.get("residue_flag_triangle_holonomy_gate", {})
    holonomy_gauge = theta.get("triangle_holonomy_gauge_gate", {})
    holonomy_observability = theta.get("holonomy_observability_gate", {})
    unipotent_profile = theta.get("unipotent_holonomy_rank_profile_gate", {})
    rational_holonomy = theta.get("rational_canonical_holonomy_gate", {})
    non_pid_fitting = theta.get("non_pid_fitting_holonomy_gate", {})
    fitting_strata = theta.get("fitting_rank_stratification_gate", {})
    directional_slice = theta.get("directional_fitting_slice_gate", {})
    arc_closure = theta.get("arc_valuation_integral_closure_gate", {})
    closure_residue = theta.get("integral_closure_supported_residue_gate", {})
    ideal_filtration = theta.get("ideal_information_loss_filtration_gate", {})
    completion_comparison = theta.get("adic_versus_weakstar_completion_gate", {})
    weakstar_constructor = theta.get("weakstar_completion_constructor_gate", {})
    magnetic_ports = theta.get("magnetic_weakstar_low_mode_ports_gate", {})
    hard_flux = theta.get("magnetic_hard_flux_correspondence_gate", {})
    characteristic_separation = theta.get("characteristic_locus_completed_kernel_separation_gate", {})
    cross_sector_rank = theta.get("cross_sector_rank_provenance_gate", {})
    magnetic_composite = theta.get("magnetic_construction_observation_composition_gate", {})
    magnetic_stability = theta.get("magnetic_low_block_stability_gate", {})
    magnetic_margin = theta.get("magnetic_low_block_perturbation_margin_gate", {})
    magnetic_frame = theta.get("magnetic_redundant_observation_frame_gate", {})
    magnetic_erasure_frame = theta.get("magnetic_erasure_budget_frame_gate", {})
    magnetic_decoder = theta.get("magnetic_error_erasure_decoder_gate", {})
    magnetic_conditioning = theta.get("magnetic_frame_conditioning_gate", {})
    magnetic_naimark = theta.get("magnetic_naimark_deletion_duality_gate", {})
    magnetic_volume_budget = theta.get("magnetic_robustness_volume_budget_gate", {})
    magnetic_plucker = theta.get("magnetic_plucker_equal_volume_obstruction_gate", {})
    magnetic_plucker_gap = theta.get("magnetic_plucker_quantitative_gap_gate", {})
    magnetic_global_cover = theta.get("magnetic_global_plucker_cover_gate", {})
    magnetic_symmetric_cover = theta.get("magnetic_symmetrized_plucker_cover_gate", {})
    magnetic_energy_gap = theta.get("magnetic_plucker_energy_inequality_gate", {})
    magnetic_golden = theta.get("magnetic_five_row_golden_candidate_gate", {})
    magnetic_golden_kkt = theta.get("magnetic_golden_local_kkt_gate", {})
    magnetic_sign_reduction = theta.get("magnetic_rank_two_sign_chamber_reduction_gate", {})
    magnetic_coercivity = theta.get("magnetic_five_row_coercive_normalization_gate", {})
    magnetic_active_scout = theta.get("magnetic_five_row_active_set_scout_gate", {})
    magnetic_cycle_face = theta.get("magnetic_golden_five_cycle_face_gate", {})
    magnetic_graph_pruning = theta.get("magnetic_unit_minor_graph_pruning_gate", {})
    magnetic_minimal_faces = theta.get("magnetic_minimal_unit_graph_face_reduction_gate", {})
    magnetic_two_faces = theta.get("magnetic_two_base_face_exact_bounds_gate", {})
    magnetic_global_golden = theta.get("magnetic_global_golden_five_row_theorem_gate", {})
    magnetic_global_equality = theta.get("magnetic_global_golden_equality_obstruction_gate", {})
    jet_fixtures = {}
    for fixture in jet_atlas.get("fixtures", []):
        first = next((i for i, value in enumerate(fixture["jets"]) if value != 0), None)
        covered = first is not None and first <= jet_atlas.get("finite_executable_depth", -1)
        jet_fixtures[fixture["fixture_id"]] = {
            "first_nonzero_order": first,
            "expected_first_nonzero_order": fixture["expected_first_nonzero_order"],
            "covered_by_finite_executable_atlas": covered,
            "first_nonzero_jet_gauge_law": "j_m' = j_m/r when j_0=...=j_(m-1)=0",
        }
        if first != fixture["expected_first_nonzero_order"]:
            errors.append("jet_fixture_order_mismatch:" + fixture["fixture_id"])
    if line.get("expected_cocycle") is not True or composite is None:
        errors.append("seam_line_cocycle_missing")
    if seam_unitary != line.get("expected_seam_unitary"):
        errors.append("seam_line_unitarity_mismatch")
    if off_seam_unitary != line.get("expected_off_seam_unitary"):
        errors.append("off_seam_metric_gate_mismatch")
    if raw_tensor.get("fixed_nonzero_t_implementable") or not raw_tensor.get("t_zero_implementable"):
        errors.append("raw_reference_tensor_implementability_mistyped")
    if metric_constructor.get("source_authorized"):
        errors.append("metric_reference_authority_invented")
    if not trace_constructor.get("completed_closability_authorized") or not trace_constructor.get("does_not_authorize_full_doubled_green_identity"):
        errors.append("native_endpoint_closability_deleted_or_overstated")
    if repair.get("required_order") != ["R_metric", "T_trace"]:
        errors.append("renormalization_trace_order_changed")
    if induced.get("target_scalar_metric_source_authorized"):
        errors.append("target_scalar_metric_authority_invented")
    if not jet_atlas.get("source_derivative_family_authorized") or not jet_atlas.get("authorization_root"):
        errors.append("jet_family_source_authority_missing")
    if jet_atlas.get("target_jet_metric_source_authorized"):
        errors.append("target_jet_metric_authority_invented")
    if jet_atlas.get("finite_executable_depth") != 2:
        errors.append("theta_finite_jet_depth_fitted_to_observed_divisor")
    if not jet_atlas.get("section_nonidentity_certificate"):
        errors.append("analytic_jet_termination_certificate_missing")
    if adaptive.get("claims_uniform_bound") or adaptive.get("selection_rule") != "least m with j_m nonzero":
        errors.append("adaptive_jet_constructor_mistyped")
    fixed_jets = reflection.get("fixed_locus_jets", [])
    scalar_parity_valid = reflection.get("reflection_character") == 1 and all(value == 0 for i, value in enumerate(fixed_jets) if i % 2 == 1)
    fixed_first = next((i for i, value in enumerate(fixed_jets) if value != 0), None)
    paired_multiplicity = reflection.get("off_fixed_multiplicities", [])
    if not reflection.get("scalar_functional_equation_authorized") or not scalar_parity_valid:
        errors.append("scalar_reflection_jet_parity_failure")
    if len(paired_multiplicity) != 2 or paired_multiplicity[0] != paired_multiplicity[1]:
        errors.append("reflected_multiplicity_mismatch")
    if not reflection.get("boundary_line_comparison_cell_authorized"):
        errors.append("derived_boundary_line_comparison_cell_deleted")
    if reflection.get("scalar_jet_to_line_lift_authorized"):
        errors.append("scalar_jet_lift_authority_invented")
    if reflection.get("fixture_kind") != "synthetic_symmetric_germ_not_claim_about_actual_Xi_center_value":
        errors.append("synthetic_central_fixture_laundered_to_Xi_value_claim")
    candidates = line_metric.get("candidate_forms", [])
    coherent_candidates = [candidate for candidate in candidates if candidate.get("reflection_involutive")]
    positive_candidates = [candidate for candidate in coherent_candidates if candidate.get("coefficient", 0) > 0]
    negative_coherent = [candidate for candidate in coherent_candidates if candidate.get("coefficient", 0) < 0]
    source_admitted_candidates = [candidate for candidate in coherent_candidates if candidate.get("admitted_by_hilbert_metric")]
    if not line_metric.get("duality_cell_source_authorized") or not line_metric.get("real_structure_source_authorized"):
        errors.append("derived_boundary_line_reflection_cell_deleted")
    if not line_metric.get("finite_cutoff_hilbert_metric_source_authorized") or not line_metric.get("seam_positive_orientation_source_authorized"):
        errors.append("source_seam_hilbert_positivity_deleted")
    if line_metric.get("required_constructors") != ["existing_seam_hilbert_metric", "line_duality", "real_structure"]:
        errors.append("boundary_line_metric_constructor_inventory_changed")
    seam_u = complex_pair(reflection_cell["seam_transition"])
    seam_norm = norm_squared(seam_u)
    seam_inverse = (seam_u[0] / seam_norm, -seam_u[1] / seam_norm)
    seam_conjugate = (seam_u[0], -seam_u[1])
    dual_conjugate_residual = (seam_inverse[0] - seam_conjugate[0], seam_inverse[1] - seam_conjugate[1])
    real_phases = [complex_pair(value) for value in reflection_cell.get("real_structure_phases", [])]
    real_squares = [norm_squared(value) for value in real_phases]
    off_u = complex_pair(reflection_cell["off_seam_fixed_metric_transition"])
    off_norm = norm_squared(off_u)
    off_inverse = (off_u[0] / off_norm, -off_u[1] / off_norm)
    off_conjugate = (off_u[0], -off_u[1])
    off_residual = (off_inverse[0] - off_conjugate[0], off_inverse[1] - off_conjugate[1])
    if reflection_cell.get("expected_dual_conjugate_residual") != "zero_on_seam" or any(dual_conjugate_residual):
        errors.append("seam_dual_conjugate_cell_failure")
    if reflection_cell.get("expected_real_square") != "identity" or any(value != 1 for value in real_squares):
        errors.append("real_structure_involution_failure")
    if reflection_cell.get("global_phase_disposition") != "presentation_gauge_U(1)":
        errors.append("real_structure_phase_promoted_to_anomaly")
    if off_uniform.get("left_product_limit") != "0" or off_uniform.get("right_product_limit") != "infinity" or off_uniform.get("uniform_fixed_metric_comparison") is not False:
        errors.append("off_seam_uniform_no_go_weakened")
    synthetic = off_uniform.get("synthetic_reciprocal_fixture", {})
    factor = Fraction(*synthetic["transition_factor"])
    depth = synthetic.get("depth", 0)
    left_products = [factor ** (-n) for n in range(depth + 1)]
    right_products = [factor ** n for n in range(depth + 1)]
    left_metrics = [value ** (-2) for value in left_products]
    right_metrics = [value ** (-2) for value in right_products]
    reciprocal_metric_products = [left_metrics[i] * right_metrics[i] for i in range(depth + 1)]
    if synthetic.get("fixture_kind") != "exact_mechanism_not_fitted_theta_coefficients":
        errors.append("synthetic_off_seam_fixture_laundered_to_theta_coefficients")
    if relative_trace.get("ambient_kind") != "parameterized_isometric_direct_system_of_Hilbert_lines" or relative_trace.get("fixed_scalar_trivialization_required"):
        errors.append("relative_ambient_collapsed_to_fixed_trivialization")
    if relative_trace.get("projective_transport_claims_closability"):
        errors.append("projective_transport_laundered_to_trace_closability")
    if not relative_trace.get("source_graph_domination_authorized") or relative_trace.get("source_graph_identity") != "||A_s G||_2^2=||h'||_2^2+a^2||h||_2^2+a|h(0)|^2":
        errors.append("native_first_order_graph_control_deleted")
    if relative_trace.get("claims_full_doubled_green_identity"):
        errors.append("endpoint_graph_control_laundered_to_full_green_identity")
    nonclosable = relative_trace.get("nonclosable_fixture", {})
    coefficients = [Fraction(value) for value in nonclosable.get("functional_coefficients", [])]
    witness_indices = nonclosable.get("witness_indices", [])
    witness_amplitudes = [Fraction(*value) for value in nonclosable.get("witness_amplitudes", [])]
    witness_norms = witness_amplitudes
    witness_outputs = [coefficients[index - 1] * amplitude for index, amplitude in zip(witness_indices, witness_amplitudes)]
    nonclosable_detected = bool(witness_norms) and witness_norms[-1] < witness_norms[0] and all(value == 1 for value in witness_outputs)
    if nonclosable.get("expected_closable") is not False or not nonclosable_detected:
        errors.append("nonclosable_trace_hostile_invalid")
    alpha = weighted_rigging.get("functional_power_alpha")
    beta_candidates = weighted_rigging.get("weight_power_candidates", [])
    weighted_classification = {
        str(beta): {
            "dual_series_exponent": 2 * alpha - beta,
            "uniformly_bounded": beta - 2 * alpha > 1,
            "partial_dual_norm_squared": str(sum((Fraction(n) ** (2 * alpha - beta) for n in range(1, weighted_rigging.get("finite_evidence_cutoff", 0) + 1)), Fraction(0))),
        }
        for beta in beta_candidates
    }
    if weighted_rigging.get("summability_law") != "sum_n n^(2 alpha-beta) converges iff beta-2 alpha>1":
        errors.append("weighted_dual_summability_law_changed")
    if weighted_rigging.get("source_authorized_beta") is not None:
        errors.append("weighted_rigging_source_authority_invented")
    if weighted_rigging.get("trace_graph_norm_source_authorized"):
        errors.append("circular_trace_graph_norm_authorized")
    if not weighted_rigging.get("trace_graph_norm_is_circular_without_independent_constructor"):
        errors.append("trace_graph_norm_circularity_hidden")
    coordinate_fixture = pro_gram.get("coordinate_fixture", {})
    observed_indices = coordinate_fixture.get("finite_observation_indices", [])
    escaping_index = coordinate_fixture.get("escaping_witness_index")
    endpoint_coefficients = coordinate_fixture.get("endpoint_coefficients", [])
    escaping_seminorm_values = [Fraction(int(escaping_index == index)) for index in observed_indices]
    escaping_endpoint_value = Fraction(endpoint_coefficients[escaping_index - 1]) if escaping_index else Fraction(0)
    endpoint_not_finitely_dominated = not any(escaping_seminorm_values) and escaping_endpoint_value != 0
    if pro_gram.get("continuity_criterion") != "L continuous iff bounded by one finite maximum of generating seminorms":
        errors.append("pro_gram_continuity_criterion_changed")
    if not pro_gram.get("endpoint_port_source_identified"):
        errors.append("source_endpoint_port_deleted")
    if pro_gram.get("completed_green_incidence_authorized") or not pro_gram.get("endpoint_normalization_authorized"):
        errors.append("endpoint_completion_scope_mistyped")
    if not pro_gram.get("augmentation_must_precede_completion"):
        errors.append("endpoint_augmentation_order_weakened")
    if not endpoint_not_finitely_dominated or coordinate_fixture.get("expected_endpoint_continuity") is not False:
        errors.append("pro_gram_endpoint_hostile_invalid")
    single_port = endpoint_orbit.get("single_port_hostile", {})
    endpoint_before = [Fraction(value) for value in single_port.get("endpoint_before", [])]
    endpoint_after = [Fraction(value) for value in single_port.get("endpoint_after", [])]
    single_port_failure = bool(endpoint_before) and not any(endpoint_before) and all(value == 1 for value in endpoint_after)
    if not endpoint_orbit.get("source_monoid_authorized") or not endpoint_orbit.get("endpoint_source_authorized"):
        errors.append("endpoint_orbit_source_authority_deleted")
    if endpoint_orbit.get("generator_law") != "ell_C(Ac)=ell_(CA)(c)":
        errors.append("endpoint_orbit_reindexing_law_changed")
    if endpoint_orbit.get("claims_finite_endpoint_family_sufficient"):
        errors.append("finite_endpoint_orbit_claim_invented")
    if endpoint_orbit.get("claims_completed_green_identity"):
        errors.append("endpoint_orbit_laundered_to_green_identity")
    if not single_port_failure:
        errors.append("single_endpoint_port_hostile_invalid")
    observability_fixtures = {}
    for fixture in observability.get("fixtures", []):
        fixture_id = fixture["fixture_id"]
        if "matrix" in fixture:
            row = [Fraction(value) for value in fixture["endpoint_row"]]
            rows = []
            ranks = []
            for _ in range(fixture["depth"]):
                rows.append(row)
                ranks.append(len(rref(rows)[1]))
                row = rowmat(row, fixture["matrix"])
        else:
            ranks = []
            for dimension in fixture.get("generated_dimensions", []):
                backward_shift = [[int(j == i + 1) for j in range(dimension)] for i in range(dimension)]
                row = [Fraction(int(j == 0)) for j in range(dimension)]
                rows = []
                for _ in range(dimension):
                    rows.append(row)
                    row = rowmat(row, backward_shift)
                ranks.append(len(rref(rows)[1]))
        observability_fixtures[fixture_id] = {"ranks": ranks, "expected_ranks": fixture["expected_ranks"], "passed": ranks == fixture["expected_ranks"], "fixture_kind": fixture["fixture_kind"]}
        if ranks != fixture["expected_ranks"]:
            errors.append("endpoint_observability_fixture_mismatch:" + fixture_id)
    if observability.get("criterion") != "finite endpoint orbit iff the row span of L after constructor words stabilizes at finite rank":
        errors.append("endpoint_observability_criterion_changed")
    if observability.get("actual_theta_orbit_finite_rank_authorized"):
        errors.append("theta_endpoint_finite_rank_invented")
    theta_rank_premises = observability.get("theta_infinite_rank_premises", {})
    if not observability.get("actual_theta_orbit_infinite_rank_authorized") or not theta_rank_premises.get("valuation_projectors_separate_every_finite_label_set") or theta_rank_premises.get("endpoint_atoms_nonzero") != "L(e_n)=Phi(log n)>0":
        errors.append("theta_endpoint_infinite_rank_certificate_deleted")
    if any(item.get("fixture_kind") == "actual_theta_endpoint_orbit" for item in observability.get("fixtures", [])):
        errors.append("synthetic_observability_fixture_laundered_to_theta")
    cokernel_fixture = doubled_green.get("cokernel_fixture", {})
    current_matrix = cokernel_fixture.get("authorized_current_matrix", [])
    forcing_residual = cokernel_fixture.get("forcing_residual", [])
    current_rank = len(rref(current_matrix)[1]) if current_matrix else 0
    augmented_current = [row + [forcing_residual[i]] for i, row in enumerate(current_matrix)] if current_matrix else []
    augmented_rank = len(rref(augmented_current)[1]) if augmented_current else 0
    residual_in_image = current_rank == augmented_rank
    if doubled_green.get("exact_identity") != "2aN=-partial_q J-2F":
        errors.append("doubled_green_identity_changed")
    if doubled_green.get("direct_dual_forcing_relation_source_derived"):
        errors.append("direct_dual_forcing_relation_invented")
    if doubled_green.get("complete_boundary_derivative_authorized") or doubled_green.get("total_boundary_flux_vanishing_authorized"):
        errors.append("doubled_green_conditional_premise_invented")
    inventory = doubled_green.get("current_inventory", {})
    inventory_valid = (
        inventory.get("continuous_forcing_reservoir_current")
        and inventory.get("primitive_P_atomic_current")
        and not inventory.get("primitive_P_completed_green_attachment")
        and inventory.get("square_Q_atomic_current")
        and not inventory.get("square_Q_completed_green_attachment")
        and inventory.get("connected_prime_distribution")
        and not inventory.get("connected_prime_completed_green_attachment")
        and not inventory.get("archimedean_completed_green_attachment")
    )
    if not inventory_valid:
        errors.append("doubled_green_current_inventory_mistyped")
    if residual_in_image != cokernel_fixture.get("expected_in_authorized_image") or not cokernel_fixture.get("scalar_sum_zero"):
        errors.append("doubled_green_cokernel_hostile_invalid")
    if cokernel_fixture.get("fixture_kind") != "synthetic_exact_typed_current_image":
        errors.append("synthetic_green_cokernel_laundered_to_theta")
    if indexed_endpoint.get("orbit_module_generator") != "L" or indexed_endpoint.get("module_generator_count") != 1:
        errors.append("endpoint_cyclic_module_generator_changed")
    if indexed_endpoint.get("static_observation_rank") != "infinite" or indexed_endpoint.get("claims_finite_dimensional_readout"):
        errors.append("cyclic_endpoint_module_conflated_with_rank_one_readout")
    if indexed_endpoint.get("indexed_evaluator") != "Eval(C,c)=L(Cc)" or not indexed_endpoint.get("finite_packet_evaluator_source_authorized"):
        errors.append("indexed_endpoint_evaluator_deleted")
    if not indexed_endpoint.get("each_fixed_C_extends_continuously_in_orbit_topology"):
        errors.append("pointwise_endpoint_orbit_continuity_deleted")
    if indexed_endpoint.get("uniform_joint_bound_over_all_C_authorized"):
        errors.append("pointwise_constructor_continuity_laundered_to_uniform_joint_bound")
    if indexed_endpoint.get("constructor_index_kind") != "finite source-monoid word, logical index not time":
        errors.append("constructor_index_temporalized")
    if indexed_endpoint.get("claims_bounded_constructor_cost"):
        errors.append("unbounded_constructor_family_called_bounded_capability")
    normal_form_fixtures = {}
    for fixture in constructor_normal.get("fixtures", []):
        observed = normalize_constructor_words(fixture["left"], fixture["right"])
        passed = observed["zero"] == fixture["expected_zero"] and observed["valuations"] == fixture["expected_valuations"] and observed["mellin"] == Fraction(*fixture["expected_mellin"])
        normal_form_fixtures[fixture["fixture_id"]] = {"zero": observed["zero"], "valuations": observed["valuations"], "mellin": str(observed["mellin"]), "passed": passed}
        if not passed:
            errors.append("constructor_normal_form_fixture_mismatch:" + fixture["fixture_id"])
    required_relations = {"P_V P_W=P_(V union W) when consistent", "P_V P_W=0 when valuation constraints conflict", "M_t M_u=M_(t+u)", "P_V M_t=M_t P_V"}
    if set(constructor_normal.get("relations", [])) != required_relations or constructor_normal.get("normal_form") != "zero or P_V M_t with V finite and consistent":
        errors.append("constructor_normal_form_law_changed")
    if not constructor_normal.get("finite_packet_joint_continuity_authorized"):
        errors.append("finite_packet_constructor_continuity_deleted")
    if constructor_normal.get("completed_joint_strong_continuity_authorized"):
        errors.append("completed_joint_constructor_action_invented")
    if constructor_normal.get("index_space_compact"):
        errors.append("constructor_index_compactness_invented")
    mellin_fixture = mellin_saturation.get("exact_finite_fixture", {})
    mellin_coefficients = [Fraction(value) for value in mellin_fixture.get("coefficients", [])]
    mellin_frequencies = [Fraction(value) for value in mellin_fixture.get("frequencies", [])]
    value_at_zero = sum(mellin_coefficients, Fraction(0))
    first_frequency_moment = sum((coefficient * frequency for coefficient, frequency in zip(mellin_coefficients, mellin_frequencies)), Fraction(0))
    if not mellin_saturation.get("source_mellin_group_authorized") or not mellin_saturation.get("finite_packet_suprema_finite_by_exponential_polynomial_continuity"):
        errors.append("mellin_saturation_source_basis_deleted")
    if mellin_saturation.get("saturation_seminorms") != ["Q_(C,R)(c)=sup_|t|<=R q_C(M_t c)", "E_(C,R)(c)=sup_|t|<=R |L(C M_t c)|"]:
        errors.append("mellin_saturation_seminorms_changed")
    if not mellin_saturation.get("saturated_completion_strong_action_authorized"):
        errors.append("saturated_mellin_action_deleted")
    if mellin_saturation.get("claims_same_topology_as_pointwise_pro_gram") or mellin_saturation.get("claims_uniform_global_t_bound") or mellin_saturation.get("claims_green_identity_extension"):
        errors.append("mellin_saturation_scope_laundered")
    if mellin_saturation.get("parameter_kind") != "spectral group coordinate, not time or epoch":
        errors.append("mellin_parameter_temporalized")
    if value_at_zero != mellin_fixture.get("expected_value_at_zero") or first_frequency_moment != mellin_fixture.get("expected_first_frequency_moment"):
        errors.append("mellin_saturation_finite_fixture_mismatch")
    if detector_clark.get("normalized_fock_state_threshold") != "Re(s)>1/2" or detector_clark.get("raw_euler_detector_threshold") != "Re(s)>1" or detector_clark.get("common_mellin_hilbert_level_iff") != "Re(s)>1":
        errors.append("state_detector_thresholds_changed")
    if not detector_clark.get("finite_fock_detector_nonzero") or not detector_clark.get("relative_heat_detector_constructed") or detector_clark.get("relative_detector_value") != "zeta(s)":
        errors.append("relative_detector_construction_deleted")
    if not detector_clark.get("regulator_universal") or detector_clark.get("normalized_regulator_class") != "smooth rapid decay with rho(0)=1" or detector_clark.get("finite_counterterms_authorized"):
        errors.append("relative_detector_regulator_coherence_mistyped")
    if detector_clark.get("finite_part_positive") or detector_clark.get("finite_part_multiplicative") or detector_clark.get("boundary_quotient_cone_pointed"):
        errors.append("finite_part_order_or_algebra_laundered")
    if detector_clark.get("theta_germ_finite_dimensional_realization") or not detector_clark.get("theta_germ_shift_realization") or not detector_clark.get("clark_shift_graph_equivalence"):
        errors.append("theta_shift_clark_graph_theorem_mistyped")
    if [Fraction(*value) for value in detector_clark.get("clark_constants_at_a_half", [])] != [Fraction(1, 4), Fraction(3, 2)]:
        errors.append("clark_graph_constants_changed")
    if not detector_clark.get("four_channel_poisson_incidence_supplied") or detector_clark.get("common_finite_poisson_clark_matrix_supplied") or detector_clark.get("uniform_generalized_eigenvalue_bounds_proved") or detector_clark.get("determinant_kernel_bridge_supplied") or detector_clark.get("relative_detector_nonvanishing_proved"):
        errors.append("poisson_clark_frontier_mistyped")
    finite_part_hostile = detector_clark.get("finite_part_square_hostile", {})
    finite_part_value = Fraction(finite_part_hostile.get("laurent_coefficients", {}).get("0", 0))
    if finite_part_value != finite_part_hostile.get("expected_finite_part") or not finite_part_hostile.get("pointwise_nonnegative") or finite_part_value >= 0:
        errors.append("finite_part_positive_square_hostile_invalid")
    lift_hostile = poisson_lift.get("hostile_same_readout_lifts", {})
    distinguished = lift_hostile.get("distinguished_state", [])
    positive_lift = lift_hostile.get("positive_lift", [])
    indefinite_lift = lift_hostile.get("indefinite_lift", [])
    positive_readout = quadratic_form(positive_lift, distinguished)
    indefinite_readout = quadratic_form(indefinite_lift, distinguished)
    positive_min_rayleigh = min(Fraction(positive_lift[i][i]) for i in range(len(positive_lift)))
    indefinite_min_rayleigh = min(Fraction(indefinite_lift[i][i]) for i in range(len(indefinite_lift)))
    if not poisson_lift.get("scalar_four_channel_incidence_authorized") or poisson_lift.get("channel_feature_map_on_common_clark_module_authorized") or poisson_lift.get("channel_pairing_signature_authorized") or poisson_lift.get("cutoff_covariance_authorized"):
        errors.append("poisson_matrix_lift_inventory_mistyped")
    if poisson_lift.get("claims_scalar_incidence_determines_energy"):
        errors.append("scalar_poisson_incidence_laundered_to_energy_form")
    if poisson_lift.get("lift_formula") != "E_X=W_X^* J_X W_X":
        errors.append("poisson_energy_lift_formula_changed")
    if positive_readout != indefinite_readout or positive_readout != lift_hostile.get("expected_common_scalar_readout") or positive_min_rayleigh != lift_hostile.get("expected_positive_lift_min_rayleigh") or indefinite_min_rayleigh != lift_hostile.get("expected_indefinite_lift_min_rayleigh"):
        errors.append("same_readout_inequivalent_energy_hostile_invalid")
    scale = Fraction(*poisson_gauge.get("channel_rescaling", [1, 1]))
    coefficient = Fraction(*poisson_gauge.get("original_coefficient", [0, 1]))
    feature = Fraction(*poisson_gauge.get("original_feature", [0, 1]))
    transformed_coefficient = Fraction(*poisson_gauge.get("transformed_coefficient", [0, 1]))
    transformed_feature = Fraction(*poisson_gauge.get("transformed_feature", [0, 1]))
    pairing = Fraction(*poisson_gauge.get("original_pairing", [0, 1]))
    transported_pairing = Fraction(*poisson_gauge.get("transported_pairing", [0, 1]))
    scalar_before = coefficient * feature
    scalar_after = transformed_coefficient * transformed_feature
    naive_energy_before = feature * feature
    naive_energy_after = transformed_feature * transformed_feature
    invariant_energy_before = feature * pairing * feature
    invariant_energy_after = transformed_feature * transported_pairing * transformed_feature
    if transformed_coefficient != coefficient / scale or transformed_feature != scale * feature or scalar_before != scalar_after:
        errors.append("poisson_scalar_gauge_fixture_invalid")
    if poisson_gauge.get("pairing_transport_law") != "J'=S^(-*) J S^(-1)" or transported_pairing != pairing / (scale * scale) or invariant_energy_before != invariant_energy_after:
        errors.append("poisson_pairing_gauge_law_changed")
    if naive_energy_before == naive_energy_after:
        errors.append("naive_channel_gram_gauge_hostile_invalid")
    if poisson_gauge.get("source_pairing_selected") or poisson_gauge.get("claims_identity_pairing_canonical"):
        errors.append("poisson_channel_pairing_authority_invented")
    reflection_matrix = reflection_pairing.get("reflection_matrix", [])
    pairing_0 = reflection_pairing.get("pairing_0", [])
    pairing_1 = reflection_pairing.get("pairing_1", [])
    test_feature = reflection_pairing.get("test_feature", [])
    def swap_invariant(matrix):
        return reflection_matrix == [[0, 1], [1, 0]] and len(matrix) == 2 and matrix[0][0] == matrix[1][1] and matrix[0][1] == matrix[1][0]
    def symmetric_two_by_two_positive(matrix):
        return len(matrix) == 2 and matrix[0][0] > 0 and matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] > 0
    reflection_energy_0 = quadratic_form(pairing_0, test_feature)
    reflection_energy_1 = quadratic_form(pairing_1, test_feature)
    if reflection_pairing.get("pairing_family_law") != "J(alpha,beta)=[[alpha,beta],[beta,alpha]]" or not swap_invariant(pairing_0) or not swap_invariant(pairing_1):
        errors.append("reflection_pairing_commutant_fixture_invalid")
    if not reflection_pairing.get("requires_positive_definite") or not symmetric_two_by_two_positive(pairing_0) or not symmetric_two_by_two_positive(pairing_1) or reflection_energy_0 == reflection_energy_1:
        errors.append("reflection_positive_pairing_nonuniqueness_fixture_invalid")
    if reflection_pairing.get("claims_reflection_and_positivity_select_unique_pairing") or reflection_pairing.get("source_flux_normalization_authorized"):
        errors.append("reflection_symmetry_laundered_to_pairing_authority")
    even_vector = sector_normalization.get("even_sector_vector", [])
    odd_vector = sector_normalization.get("odd_sector_vector", [])
    sector_candidate_0 = sector_normalization.get("candidate_0", [])
    sector_candidate_1 = sector_normalization.get("candidate_1", [])
    even_energy_0 = quadratic_form(sector_candidate_0, even_vector)
    even_energy_1 = quadratic_form(sector_candidate_1, even_vector)
    odd_energy_0 = quadratic_form(sector_candidate_0, odd_vector)
    odd_energy_1 = quadratic_form(sector_candidate_1, odd_vector)
    if even_vector != [1, 1] or odd_vector != [1, -1] or not swap_invariant(sector_candidate_0) or not swap_invariant(sector_candidate_1):
        errors.append("reflection_sector_fixture_invalid")
    if even_energy_0 != even_energy_1 or even_energy_0 != sector_normalization.get("expected_common_even_energy") or [odd_energy_0, odd_energy_1] != sector_normalization.get("expected_odd_energies"):
        errors.append("single_sector_normalization_hostile_invalid")
    if sector_normalization.get("minimal_independent_sector_normalizations") != 2:
        errors.append("reflection_sector_normalization_count_changed")
    if sector_normalization.get("claims_one_sector_normalization_is_jointly_faithful") or sector_normalization.get("even_flux_normalization_authorized") or sector_normalization.get("odd_flux_normalization_authorized"):
        errors.append("reflection_sector_flux_authority_invented")
    even_flux = Fraction(pairing_reconstruction.get("even_flux", 0))
    odd_flux = Fraction(pairing_reconstruction.get("odd_flux", 0))
    reconstructed_alpha = (even_flux + odd_flux) / 4
    reconstructed_beta = (even_flux - odd_flux) / 4
    reconstructed_pairing = [[reconstructed_alpha, reconstructed_beta], [reconstructed_beta, reconstructed_alpha]]
    expected_pairing = [[Fraction(x) for x in row] for row in pairing_reconstruction.get("expected_pairing", [])]
    if pairing_reconstruction.get("reconstruction_law") != {"alpha": "(E_plus+E_minus)/4", "beta": "(E_plus-E_minus)/4"} or reconstructed_alpha != pairing_reconstruction.get("expected_alpha") or reconstructed_beta != pairing_reconstruction.get("expected_beta") or reconstructed_pairing != expected_pairing:
        errors.append("reflection_pairing_reconstruction_changed")
    if pairing_reconstruction.get("positivity_law") != "E_plus>0 and E_minus>0" or even_flux <= 0 or odd_flux <= 0 or not symmetric_two_by_two_positive(reconstructed_pairing):
        errors.append("reflection_pairing_reconstruction_not_positive")
    if pairing_reconstruction.get("scalar_incidence_authorizes_flux_values") or pairing_reconstruction.get("claims_reconstruction_before_flux_authority"):
        errors.append("reflection_flux_values_laundered_from_scalar_incidence")
    four_perm = four_channel_reflection.get("reflection_permutation", [])
    four_candidate_0 = four_channel_reflection.get("candidate_0", [])
    four_candidate_1 = four_channel_reflection.get("candidate_1", [])
    def permutation_invariant(matrix, permutation):
        return len(matrix) == len(permutation) and all(matrix[i][j] == matrix[permutation[i]][permutation[j]] for i in range(len(permutation)) for j in range(len(permutation)))
    first_even = four_channel_reflection.get("first_pair_even_probe", [])
    first_odd = four_channel_reflection.get("first_pair_odd_probe", [])
    second_even = four_channel_reflection.get("second_pair_even_probe", [])
    first_pair_energies = [quadratic_form(four_candidate_0, first_even), quadratic_form(four_candidate_1, first_even), quadratic_form(four_candidate_0, first_odd), quadratic_form(four_candidate_1, first_odd)]
    second_pair_even_energies = [quadratic_form(four_candidate_0, second_even), quadratic_form(four_candidate_1, second_even)]
    if four_perm != [1, 0, 3, 2] or not permutation_invariant(four_candidate_0, four_perm) or not permutation_invariant(four_candidate_1, four_perm):
        errors.append("four_channel_reflection_fixture_invalid")
    if four_channel_reflection.get("even_multiplicity") != 2 or four_channel_reflection.get("odd_multiplicity") != 2 or four_channel_reflection.get("real_symmetric_commutant_dimension") != 6:
        errors.append("four_channel_reflection_commutant_dimension_changed")
    expected_first = four_channel_reflection.get("expected_first_pair_energies", [])
    if first_pair_energies != [expected_first[0], expected_first[0], expected_first[1], expected_first[1]] or second_pair_even_energies != four_channel_reflection.get("expected_second_pair_even_energies"):
        errors.append("four_channel_two_flux_hostile_invalid")
    if four_channel_reflection.get("claims_two_scalar_fluxes_reconstruct_four_channel_pairing") or four_channel_reflection.get("additional_channel_symmetry_authorized"):
        errors.append("four_channel_pairing_authority_laundered")
    expected_channels = ["A_f(s)", "A_fhat(1-s)", "fhat(0)/(s-1)", "-f(0)/s"]
    source_reflection_matches = four_channel_source.get("reciprocal_reflection_permutation") == four_perm
    if four_channel_source.get("ordered_channels") != expected_channels or not four_channel_source.get("self_dual_source") or not four_channel_source.get("boundary_sign_included_in_fourth_channel") or not source_reflection_matches:
        errors.append("four_channel_source_action_mistyped")
    if four_channel_source.get("larger_channel_action_source_authorized") or four_channel_source.get("claims_bulk_boundary_exchange_symmetry"):
        errors.append("four_channel_extra_symmetry_invented")
    even_block = six_probe.get("even_block", [])
    odd_block = six_probe.get("odd_block", [])
    probe_vectors = six_probe.get("probe_vectors", [])
    even_probe_energies = [quadratic_form(even_block, vector) for vector in probe_vectors]
    odd_probe_energies = [quadratic_form(odd_block, vector) for vector in probe_vectors]
    def reconstruct_symmetric_block(energies):
        return [[energies[0], (energies[2] - energies[0] - energies[1]) / 2], [(energies[2] - energies[0] - energies[1]) / 2, energies[1]]]
    reconstructed_even_block = reconstruct_symmetric_block(even_probe_energies)
    reconstructed_odd_block = reconstruct_symmetric_block(odd_probe_energies)
    hostile_even_blocks = six_probe.get("hostile_same_five_probes_even_blocks", [])
    hostile_diagonal_data_equal = len(hostile_even_blocks) == 2 and [hostile_even_blocks[0][0][0], hostile_even_blocks[0][1][1]] == [hostile_even_blocks[1][0][0], hostile_even_blocks[1][1][1]] and hostile_even_blocks[0] != hostile_even_blocks[1] and all(symmetric_two_by_two_positive(block) for block in hostile_even_blocks)
    if probe_vectors != [[1, 0], [0, 1], [1, 1]] or even_probe_energies != six_probe.get("expected_even_energies") or odd_probe_energies != six_probe.get("expected_odd_energies") or reconstructed_even_block != even_block or reconstructed_odd_block != odd_block:
        errors.append("six_probe_polarization_fixture_invalid")
    if six_probe.get("polarization_law") != "offdiag=(E_12-E_1-E_2)/2" or six_probe.get("expected_parameter_count") != 6:
        errors.append("six_probe_reconstruction_law_changed")
    if not hostile_diagonal_data_equal:
        errors.append("five_probe_pairing_hostile_invalid")
    if six_probe.get("six_flux_ports_source_authorized") or six_probe.get("claims_five_linear_probes_can_be_jointly_faithful"):
        errors.append("six_probe_capability_authority_invented")
    design_matrix = symmetric_observability.get("design_matrix", [])
    hostile_design = symmetric_observability.get("hostile_rank_deficient_design", [])
    design_reduced, design_pivots = rref(design_matrix)
    hostile_reduced, hostile_pivots = rref(hostile_design)
    design_rank = len(design_pivots)
    hostile_design_rank = len(hostile_pivots)
    design_determinant = Fraction(1)
    determinant_matrix = [[Fraction(x) for x in row] for row in design_matrix]
    determinant_sign = 1
    for col in range(len(determinant_matrix)):
        pivot = next((row for row in range(col, len(determinant_matrix)) if determinant_matrix[row][col]), None)
        if pivot is None:
            design_determinant = Fraction(0)
            break
        if pivot != col:
            determinant_matrix[col], determinant_matrix[pivot] = determinant_matrix[pivot], determinant_matrix[col]
            determinant_sign *= -1
        pivot_value = determinant_matrix[col][col]
        design_determinant *= pivot_value
        for row in range(col + 1, len(determinant_matrix)):
            scale = determinant_matrix[row][col] / pivot_value
            determinant_matrix[row] = [x - scale * y for x, y in zip(determinant_matrix[row], determinant_matrix[col])]
    design_determinant *= determinant_sign
    if symmetric_observability.get("parameter_order") != ["J+11", "J+22", "J+12", "J-11", "J-22", "J-12"] or design_rank != symmetric_observability.get("expected_rank") or design_determinant != symmetric_observability.get("expected_determinant"):
        errors.append("symmetric_square_observability_fixture_invalid")
    if hostile_design_rank != symmetric_observability.get("expected_hostile_rank") or hostile_design_rank >= design_rank:
        errors.append("rank_deficient_six_port_hostile_invalid")
    if symmetric_observability.get("source_feature_family_authorized") or symmetric_observability.get("claims_port_count_alone_implies_faithfulness"):
        errors.append("symmetric_square_observability_authority_invented")
    orbit_probe = reflection_orbit_observability.get("parity_coordinate_probe", [])
    reflected_probe = reflection_orbit_observability.get("reflected_probe", [])
    def invariant_design_row(vector):
        x1, x2, y1, y2 = vector
        return [x1 * x1, x2 * x2, 2 * x1 * x2, y1 * y1, y2 * y2, 2 * y1 * y2]
    orbit_rows = [invariant_design_row(orbit_probe), invariant_design_row(reflected_probe)] if len(orbit_probe) == len(reflected_probe) == 4 else []
    _, orbit_pivots = rref(orbit_rows)
    orbit_rank = len(orbit_pivots)
    if reflected_probe != orbit_probe[:2] + [-value for value in orbit_probe[2:]] or not orbit_rows or orbit_rows[0] != reflection_orbit_observability.get("expected_invariant_design_row") or orbit_rows[0] != orbit_rows[1]:
        errors.append("reflection_orbit_observability_fixture_invalid")
    if orbit_rank != reflection_orbit_observability.get("expected_two_port_rank"):
        errors.append("reflection_orbit_observability_rank_changed")
    if reflection_orbit_observability.get("claims_reflection_orbit_adds_independent_observation") or reflection_orbit_observability.get("additional_seed_family_source_authorized"):
        errors.append("reflection_orbit_observability_authority_invented")
    even_jet_matrix = even_jet_observability.get("normalized_even_jet_matrix", [])
    truncated_even_jet_matrix = even_jet_observability.get("hostile_truncated_even_jet_matrix", [])
    _, even_jet_pivots = rref(even_jet_matrix)
    _, truncated_even_jet_pivots = rref(truncated_even_jet_matrix)
    even_jet_rank = len(even_jet_pivots)
    truncated_even_jet_rank = len(truncated_even_jet_pivots)
    if even_jet_observability.get("seam_coordinate") != "t=s-1/2" or even_jet_observability.get("reciprocity_law") != "Phi(-t)=Phi(t)" or even_jet_observability.get("normalized_even_jet_orders") != [0, 2, 4, 6, 8, 10] or not even_jet_observability.get("odd_jets_vanish"):
        errors.append("even_jet_reciprocity_fixture_invalid")
    if even_jet_rank != even_jet_observability.get("expected_rank") or truncated_even_jet_rank != even_jet_observability.get("expected_hostile_rank"):
        errors.append("even_jet_observability_rank_changed")
    if even_jet_observability.get("source_feature_germ_authorized") or even_jet_observability.get("claims_scalar_section_jets_are_feature_jets"):
        errors.append("even_jet_feature_authority_invented")
    even_gauge_det = int(symmetric_square_gauge.get("even_gauge_determinant", 0))
    odd_gauge_det = int(symmetric_square_gauge.get("odd_gauge_determinant", 0))
    sym_square_exponent = int(symmetric_square_gauge.get("symmetric_square_exponent", 0))
    total_gauge_character = (even_gauge_det * odd_gauge_det) ** sym_square_exponent
    transformed_design_determinant = int(symmetric_square_gauge.get("original_design_determinant", 0)) * total_gauge_character
    if sym_square_exponent != 3 or total_gauge_character != symmetric_square_gauge.get("expected_total_character") or transformed_design_determinant != symmetric_square_gauge.get("expected_transformed_design_determinant"):
        errors.append("symmetric_square_gauge_character_changed")
    if symmetric_square_gauge.get("claims_determinant_value_is_gauge_invariant") or symmetric_square_gauge.get("claims_nonvanishing_selects_pairing"):
        errors.append("symmetric_square_gauge_invariance_overclaimed")
    orientation_gauge_dets = determinant_line.get("orientation_reversing_gauge_determinants", [])
    orientation_character = (orientation_gauge_dets[0] * orientation_gauge_dets[1]) ** 3 if len(orientation_gauge_dets) == 2 else 0
    transformed_local_coordinate = determinant_line.get("original_local_coordinate", 0) * orientation_character
    nonvanishing_preserved = transformed_local_coordinate != 0 and determinant_line.get("original_local_coordinate", 0) != 0
    sign_preserved = transformed_local_coordinate * determinant_line.get("original_local_coordinate", 0) > 0
    if determinant_line.get("line_type") != "(det V_plus)^3 tensor (det V_minus)^3" or transformed_local_coordinate != determinant_line.get("expected_transformed_local_coordinate") or nonvanishing_preserved != determinant_line.get("nonvanishing_preserved") or sign_preserved != determinant_line.get("sign_preserved"):
        errors.append("observability_determinant_line_fixture_invalid")
    if determinant_line.get("source_orientation_authorized") or determinant_line.get("claims_positive_determinant_intrinsic"):
        errors.append("observability_orientation_authority_invented")
    determinant_coefficients = observability_divisor.get("local_determinant_coefficients", [])
    regular_character_coefficients = observability_divisor.get("regular_gauge_character_coefficients", [])
    singular_character_coefficients = observability_divisor.get("singular_gauge_character_coefficients", [])
    def polynomial_product(left, right):
        product = [0] * (len(left) + len(right) - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                product[i + j] += x * y
        return product
    def vanishing_order(coefficients):
        return next((i for i, value in enumerate(coefficients) if value != 0), None)
    original_vanishing_order = vanishing_order(determinant_coefficients)
    regular_transform_order = vanishing_order(polynomial_product(determinant_coefficients, regular_character_coefficients))
    singular_transform_order = vanishing_order(polynomial_product(determinant_coefficients, singular_character_coefficients))
    if original_vanishing_order != observability_divisor.get("expected_original_vanishing_order") or regular_transform_order != observability_divisor.get("expected_regular_transform_vanishing_order") or singular_transform_order != observability_divisor.get("expected_singular_transform_vanishing_order"):
        errors.append("observability_divisor_fixture_invalid")
    if not observability_divisor.get("admissible_chart_requires_nonzero_constant_character") or not regular_character_coefficients or regular_character_coefficients[0] == 0 or not singular_character_coefficients or singular_character_coefficients[0] != 0:
        errors.append("observability_chart_admissibility_mistyped")
    if observability_divisor.get("claims_singular_gauge_preserves_divisor"):
        errors.append("singular_gauge_laundered_to_divisor_equivalence")
    smith_profiles = [local_smith.get("fixture_a_invariant_orders", []), local_smith.get("fixture_b_invariant_orders", [])]
    smith_determinant_orders = [sum(profile) for profile in smith_profiles]
    smith_cokernel_lengths = list(smith_determinant_orders)
    smith_special_coranks = [sum(order > 0 for order in profile) for profile in smith_profiles]
    smith_generator_counts = list(smith_special_coranks)
    if smith_determinant_orders != [local_smith.get("expected_common_determinant_order")] * 2 or smith_cokernel_lengths != local_smith.get("expected_cokernel_lengths") or smith_special_coranks != local_smith.get("expected_special_coranks") or smith_generator_counts != local_smith.get("expected_minimal_generator_counts"):
        errors.append("local_smith_observability_fixture_invalid")
    if not local_smith.get("regular_left_right_equivalence_preserves_profile"):
        errors.append("local_smith_regular_equivalence_mistyped")
    if local_smith.get("claims_determinant_order_classifies_failure") or local_smith.get("source_analytic_observability_matrix_authorized"):
        errors.append("local_smith_observability_authority_invented")
    fixture_a_deltas = determinantal_divisors.get("fixture_a_determinantal_valuations", [])
    fixture_b_deltas = determinantal_divisors.get("fixture_b_determinantal_valuations", [])
    def smith_profile_from_deltas(deltas):
        previous = 0
        profile = []
        for delta in deltas:
            profile.append(delta - previous)
            previous = delta
        return profile
    recovered_fixture_a_profile = smith_profile_from_deltas(fixture_a_deltas)
    recovered_fixture_b_profile = smith_profile_from_deltas(fixture_b_deltas)
    if determinantal_divisors.get("reconstruction_law") != "nu_k=delta_k-delta_(k-1), delta_0=0" or recovered_fixture_a_profile != determinantal_divisors.get("expected_fixture_a_profile") or recovered_fixture_b_profile != determinantal_divisors.get("expected_fixture_b_profile"):
        errors.append("determinantal_divisor_reconstruction_changed")
    if not determinantal_divisors.get("determinantal_ideals_regular_equivalence_invariant"):
        errors.append("determinantal_ideal_invariance_mistyped")
    if determinantal_divisors.get("claims_top_determinant_valuation_is_complete") or determinantal_divisors.get("source_minor_ideals_authorized"):
        errors.append("determinantal_divisor_authority_invented")
    barcode_profiles = [defect_barcode.get("fixture_a_profile", []), defect_barcode.get("fixture_b_profile", [])]
    barcode_summands = [[order for order in profile if order > 0] for profile in barcode_profiles]
    def depth_layers(profile):
        maximum = max(profile, default=0)
        return [sum(order >= depth for order in profile) for depth in range(1, maximum + 1)]
    barcode_layers = [depth_layers(profile) for profile in barcode_profiles]
    barcode_lengths = [sum(profile) for profile in barcode_profiles]
    if defect_barcode.get("module_law") != "coker M_torsion = direct_sum_i O/(t^nu_i) for nu_i>0" or barcode_summands != [defect_barcode.get("expected_fixture_a_summands"), defect_barcode.get("expected_fixture_b_summands")] or barcode_layers != [defect_barcode.get("expected_fixture_a_depth_layers"), defect_barcode.get("expected_fixture_b_depth_layers")] or barcode_lengths != [defect_barcode.get("expected_common_total_length")] * 2:
        errors.append("defect_module_barcode_fixture_invalid")
    if defect_barcode.get("claims_equal_length_implies_equivalent_defect_module") or defect_barcode.get("source_residue_module_authorized"):
        errors.append("defect_module_barcode_authority_invented")
    derived_profiles = derived_specialization.get("fixture_profiles", [])
    derived_special_kernel_dimensions = [sum(order > 0 for order in profile) for profile in derived_profiles]
    derived_tor1_dimensions = list(derived_special_kernel_dimensions)
    if derived_specialization.get("generic_kernel_dimensions") != [0, 0] or derived_special_kernel_dimensions != derived_specialization.get("expected_special_kernel_dimensions") or derived_tor1_dimensions != derived_specialization.get("expected_tor1_dimensions"):
        errors.append("derived_specialization_kernel_fixture_invalid")
    if derived_specialization.get("exact_sequence_law") != "Tor_1^O(coker M,k) isomorphic to ker(M tensor_O k) when M is generically injective between free modules" or not derived_specialization.get("tor1_detects_generator_count_not_depth") or not derived_specialization.get("full_torsion_cokernel_retains_depth"):
        errors.append("derived_specialization_exact_sequence_mistyped")
    if derived_specialization.get("claims_ordinary_generic_kernel_detects_specialization_birth") or derived_specialization.get("source_derived_kernel_authorized"):
        errors.append("derived_specialization_kernel_authority_invented")
    variance_profiles = defect_variance.get("fixture_profiles", [])
    variance_kernel_dimensions = [sum(order > 0 for order in profile) for profile in variance_profiles]
    variance_cokernel_dimensions = list(variance_kernel_dimensions)
    if defect_variance.get("map_type") != "pairing_parameter_module -> flux_observation_module" or defect_variance.get("kernel_meaning") != "invisible pairing-parameter combinations" or defect_variance.get("cokernel_meaning") != "unreachable flux-observation syndromes" or defect_variance.get("tor1_meaning") != "specialization-born invisible parameter directions":
        errors.append("observability_defect_variance_mistyped")
    if variance_kernel_dimensions != defect_variance.get("expected_special_kernel_dimensions") or variance_cokernel_dimensions != defect_variance.get("expected_special_cokernel_dimensions"):
        errors.append("observability_defect_variance_fixture_invalid")
    if defect_variance.get("claims_equal_dimensions_canonically_identify_kernel_and_cokernel") or defect_variance.get("source_kernel_cokernel_duality_authorized"):
        errors.append("observability_defect_duality_invented")
    duality_matrix = kernel_cokernel_duality.get("finite_matrix", [])
    duality_kernel_witness = [Fraction(x) for x in kernel_cokernel_duality.get("kernel_witness", [])]
    adjoint_kernel_witness = [Fraction(x) for x in kernel_cokernel_duality.get("adjoint_kernel_witness", [])]
    transpose_matrix = [list(row) for row in zip(*duality_matrix)] if duality_matrix else []
    if not duality_matrix or any(matvec(duality_matrix, duality_kernel_witness)) or any(matvec(transpose_matrix, adjoint_kernel_witness)) or duality_kernel_witness == adjoint_kernel_witness:
        errors.append("kernel_cokernel_duality_fixture_invalid")
    if kernel_cokernel_duality.get("duality_law") != "(coker M)^* isomorphic to ker(M^*)" or kernel_cokernel_duality.get("kernel_cokernel_identification_requires") != ["perfect parameter-observation duality", "adjointness cell identifying M^* with M"]:
        errors.append("kernel_cokernel_duality_law_mistyped")
    if kernel_cokernel_duality.get("perfect_parameter_observation_duality_authorized") or kernel_cokernel_duality.get("adjointness_cell_authorized") or kernel_cokernel_duality.get("claims_square_matrix_supplies_self_duality"):
        errors.append("kernel_cokernel_self_duality_authority_invented")
    green_matrix = green_adjointness.get("finite_matrix", [])
    parameter_pairing = green_adjointness.get("parameter_pairing", [])
    observation_pairing = green_adjointness.get("observation_pairing", [])
    def matrix_product(left, right):
        return [[sum(Fraction(left[i][k]) * Fraction(right[k][j]) for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]
    green_transpose = [list(row) for row in zip(*green_matrix)] if green_matrix else []
    left_green = matrix_product(observation_pairing, green_matrix) if green_matrix else []
    right_green = matrix_product(green_transpose, parameter_pairing) if green_matrix else []
    green_residual = [[left_green[i][j] - right_green[i][j] for j in range(len(left_green[0]))] for i in range(len(left_green))] if left_green else []
    expected_green_residual = [[Fraction(x) for x in row] for row in green_adjointness.get("expected_boundary_residual", [])]
    if green_adjointness.get("residual_law") != "B=J_observation M-M^T J_parameter" or green_residual != expected_green_residual or not green_adjointness.get("boundary_residual_is_typed"):
        errors.append("green_adjointness_residual_fixture_invalid")
    if green_adjointness.get("source_boundary_condition_annihilates_residual") or green_adjointness.get("claims_retaining_residual_makes_operator_self_adjoint") or green_adjointness.get("source_green_matrix_authorized"):
        errors.append("green_adjointness_authority_invented")
    boundary_form = lagrangian_boundary.get("boundary_form", [])
    candidate_lines = [lagrangian_boundary.get("candidate_line_0", []), lagrangian_boundary.get("candidate_line_1", [])]
    line_pairings = [quadratic_form(boundary_form, line) for line in candidate_lines] if boundary_form else []
    boundary_form_skew = boundary_form == [[0, 1], [-1, 0]]
    boundary_form_nondegenerate = boundary_form_skew
    candidates_distinct = candidate_lines[0] != candidate_lines[1]
    both_candidates_isotropic = line_pairings == [0, 0]
    if lagrangian_boundary.get("expected_boundary_dimension") != 2 or lagrangian_boundary.get("expected_lagrangian_dimension") != 1 or not boundary_form_nondegenerate or both_candidates_isotropic != lagrangian_boundary.get("both_candidates_isotropic") or candidates_distinct != lagrangian_boundary.get("candidates_distinct"):
        errors.append("lagrangian_boundary_condition_fixture_invalid")
    if lagrangian_boundary.get("source_lagrangian_selected") or lagrangian_boundary.get("claims_adjointness_selects_unique_boundary_domain"):
        errors.append("lagrangian_boundary_selection_authority_invented")
    extension_operator = boundary_kernel_dependence.get("operator_matrix", [])
    extension_boundary_form = boundary_kernel_dependence.get("boundary_form", [])
    extension_generators = [boundary_kernel_dependence.get("regular_lagrangian_generator", []), boundary_kernel_dependence.get("kernel_lagrangian_generator", [])]
    extension_isotropic = [quadratic_form(extension_boundary_form, generator) == 0 for generator in extension_generators]
    extension_images = [matvec(extension_operator, [Fraction(x) for x in generator]) for generator in extension_generators]
    restricted_kernel_dimensions = [1 if not any(image) else 0 for image in extension_images]
    if extension_boundary_form != [[0, 1], [-1, 0]] or not all(extension_isotropic) or not boundary_kernel_dependence.get("both_domains_lagrangian") or restricted_kernel_dimensions != boundary_kernel_dependence.get("expected_restricted_kernel_dimensions"):
        errors.append("boundary_selection_kernel_dependence_fixture_invalid")
    if boundary_kernel_dependence.get("claims_kernel_independent_of_lagrangian_selection") or boundary_kernel_dependence.get("source_extension_selection_authorized"):
        errors.append("boundary_extension_selection_authority_invented")
    selector_boundary_form = boundary_selector.get("boundary_form", [])
    selector_reflection = boundary_selector.get("reflection_matrix", [])
    selector_energy = boundary_selector.get("positive_boundary_energy", [])
    selector_lines = boundary_selector.get("candidate_reflection_invariant_lines", [])
    reflected_lines = [matvec(selector_reflection, [Fraction(x) for x in line]) for line in selector_lines]
    selector_line_invariant = [reflected == [Fraction(x) for x in line] or reflected == [-Fraction(x) for x in line] for reflected, line in zip(reflected_lines, selector_lines)]
    selector_energies = [quadratic_form(selector_energy, line) for line in selector_lines]
    selector_isotropic = [quadratic_form(selector_boundary_form, line) == 0 for line in selector_lines]
    reflected_boundary_form = matrix_product([list(row) for row in zip(*selector_reflection)], matrix_product(selector_boundary_form, selector_reflection))
    reflection_anti_symplectic = reflected_boundary_form == [[-Fraction(x) for x in row] for row in selector_boundary_form]
    if not all(selector_line_invariant) or not all(selector_isotropic) or selector_energies != boundary_selector.get("expected_candidate_energies") or reflection_anti_symplectic != boundary_selector.get("reflection_is_anti_symplectic") or not boundary_selector.get("both_candidates_lagrangian"):
        errors.append("boundary_selector_insufficiency_fixture_invalid")
    if boundary_selector.get("claims_reflection_and_positivity_select_unique_domain") or boundary_selector.get("additional_selector_source_authorized"):
        errors.append("boundary_selector_authority_invented")
    exchange = boundary_selector.get("symmetry_exchange_matrix", [])
    exchanged_lines = [matvec(exchange, [Fraction(x) for x in line]) for line in selector_lines]
    candidate_orbit = []
    for exchanged in exchanged_lines:
        candidate_orbit.append(next((i for i, line in enumerate(selector_lines) if exchanged == [Fraction(x) for x in line] or exchanged == [-Fraction(x) for x in line]), None))
    exchange_transpose = [list(row) for row in zip(*exchange)]
    exchange_boundary_form = matrix_product(exchange_transpose, matrix_product(selector_boundary_form, exchange))
    exchange_energy = matrix_product(exchange_transpose, matrix_product(selector_energy, exchange))
    exchange_anti_symplectic = exchange_boundary_form == [[-Fraction(x) for x in row] for row in selector_boundary_form]
    exchange_preserves_energy = exchange_energy == [[Fraction(x) for x in row] for row in selector_energy]
    if candidate_orbit != boundary_selector.get("expected_candidate_orbit") or exchange_anti_symplectic != boundary_selector.get("exchange_is_anti_symplectic") or exchange_preserves_energy != boundary_selector.get("exchange_preserves_energy"):
        errors.append("boundary_selector_orbit_fixture_invalid")
    if boundary_selector.get("claims_invariant_selector_distinguishes_one_orbit"):
        errors.append("invariant_selector_orbit_laundering")
    orbit_lines = orbit_selector.get("candidate_lines", [])
    orbit_form = orbit_selector.get("candidate_selector_form", [])
    orbit_scores = [quadratic_form(orbit_form, line) for line in orbit_lines]
    selected_candidate = orbit_scores.index(min(orbit_scores)) if orbit_scores and orbit_scores.count(min(orbit_scores)) == 1 else None
    orbit_exchange = orbit_selector.get("exchange_matrix", [])
    orbit_exchange_transpose = [list(row) for row in zip(*orbit_exchange)]
    transported_selector_form = matrix_product(orbit_exchange_transpose, matrix_product(orbit_form, orbit_exchange))
    selector_exchange_invariant = transported_selector_form == [[Fraction(x) for x in row] for row in orbit_form]
    if orbit_scores != orbit_selector.get("expected_scores") or selected_candidate != orbit_selector.get("expected_selected_candidate") or selector_exchange_invariant != orbit_selector.get("selector_exchange_invariant") or not orbit_selector.get("orbit_separation_is_mathematically_sufficient"):
        errors.append("orbit_separating_selector_fixture_invalid")
    if orbit_selector.get("selector_form_source_authorized") or orbit_selector.get("selector_executable") or orbit_selector.get("claims_mathematical_sufficiency_implies_source_authority"):
        errors.append("orbit_selector_authority_laundered")
    torsor_exchange = selector_torsor.get("exchange_matrix", [])
    torsor_generator = selector_torsor.get("anti_invariant_generator", [])
    torsor_exchange_transpose = [list(row) for row in zip(*torsor_exchange)]
    transported_torsor_generator = matrix_product(torsor_exchange_transpose, matrix_product(torsor_generator, torsor_exchange))
    torsor_character = None
    if transported_torsor_generator == [[Fraction(x) for x in row] for row in torsor_generator]:
        torsor_character = 1
    elif transported_torsor_generator == [[-Fraction(x) for x in row] for row in torsor_generator]:
        torsor_character = -1
    torsor_lines = selector_torsor.get("candidate_lines", [])
    positive_torsor_scores = [quadratic_form(torsor_generator, line) for line in torsor_lines]
    negative_torsor_scores = [-score for score in positive_torsor_scores]
    positive_choice = positive_torsor_scores.index(min(positive_torsor_scores)) if positive_torsor_scores.count(min(positive_torsor_scores)) == 1 else None
    negative_choice = negative_torsor_scores.index(min(negative_torsor_scores)) if negative_torsor_scores.count(min(negative_torsor_scores)) == 1 else None
    if torsor_character != selector_torsor.get("expected_exchange_character") or positive_torsor_scores != selector_torsor.get("expected_positive_generator_scores") or negative_torsor_scores != selector_torsor.get("expected_negative_generator_scores") or positive_choice != selector_torsor.get("expected_positive_choice") or negative_choice != selector_torsor.get("expected_negative_choice") or selector_torsor.get("zero_section_selects_uniquely") or not selector_torsor.get("selector_space_is_two_orientation_torsor"):
        errors.append("selector_torsor_fixture_invalid")
    if selector_torsor.get("source_coorientation_authorized") or selector_torsor.get("claims_torsor_has_canonical_element"):
        errors.append("selector_torsor_authority_laundered")
    wall_operator = selector_wall.get("operator_matrix", [])
    wall_boundary_form = selector_wall.get("boundary_form", [])
    wall_lines = selector_wall.get("candidate_lines", [])
    wall_exchange = selector_wall.get("exchange_matrix", [])
    wall_energy = selector_wall.get("invariant_positive_energy", [])
    wall_selector = selector_wall.get("anti_invariant_selector", [])
    wall_exchange_transpose = [list(row) for row in zip(*wall_exchange)]
    wall_exchange_lines = [matvec(wall_exchange, [Fraction(x) for x in line]) for line in wall_lines]
    wall_orbit = [next((i for i, line in enumerate(wall_lines) if image == [Fraction(x) for x in line] or image == [-Fraction(x) for x in line]), None) for image in wall_exchange_lines]
    wall_energy_transport = matrix_product(wall_exchange_transpose, matrix_product(wall_energy, wall_exchange))
    wall_selector_transport = matrix_product(wall_exchange_transpose, matrix_product(wall_selector, wall_exchange))
    wall_energy_invariant = wall_energy_transport == [[Fraction(x) for x in row] for row in wall_energy]
    wall_selector_anti_invariant = wall_selector_transport == [[-Fraction(x) for x in row] for row in wall_selector]
    wall_energies = [quadratic_form(wall_energy, line) for line in wall_lines]
    wall_base_scores = [quadratic_form(wall_selector, line) for line in wall_lines]
    wall_kernel_dimensions = [1 if not any(matvec(wall_operator, [Fraction(x) for x in line])) else 0 for line in wall_lines]
    wall_selected_candidates = []
    for parameter in selector_wall.get("selector_parameters", []):
        scores = [Fraction(parameter) * score for score in wall_base_scores]
        wall_selected_candidates.append(scores.index(min(scores)) if scores.count(min(scores)) == 1 else None)
    wall_selected_kernel_dimensions = [wall_kernel_dimensions[index] if index is not None else None for index in wall_selected_candidates]
    if wall_orbit != [1, 0] or not wall_energy_invariant or not wall_selector_anti_invariant or wall_energies != [3, 3] or wall_base_scores != [-1, 1] or wall_selected_candidates != selector_wall.get("expected_selected_candidates") or wall_selected_kernel_dimensions != selector_wall.get("expected_selected_kernel_dimensions") or not selector_wall.get("bulk_operator_constant"):
        errors.append("selector_wall_kernel_jump_fixture_invalid")
    if selector_wall.get("claims_wall_is_bulk_rank_failure") or selector_wall.get("source_path_through_selector_space_authorized"):
        errors.append("selector_wall_kernel_jump_authority_laundered")
    incidence_operator = kernel_incidence.get("operator_matrix", [])
    incidence_kernel = [Fraction(x) for x in kernel_incidence.get("bulk_kernel_generator", [])]
    incidence_lines = [[Fraction(x) for x in line] for line in kernel_incidence.get("candidate_lagrangian_generators", [])]
    bulk_kernel_witness_valid = not any(matvec(incidence_operator, incidence_kernel))
    incidence_dimensions = [1 if len(line) == 2 and len(incidence_kernel) == 2 and line[0] * incidence_kernel[1] - line[1] * incidence_kernel[0] == 0 else 0 for line in incidence_lines]
    incidence_restricted_kernel_dimensions = [1 if not any(matvec(incidence_operator, line)) else 0 for line in incidence_lines]
    if not bulk_kernel_witness_valid or incidence_dimensions != kernel_incidence.get("expected_intersection_dimensions") or incidence_restricted_kernel_dimensions != kernel_incidence.get("expected_restricted_kernel_dimensions") or incidence_dimensions != incidence_restricted_kernel_dimensions:
        errors.append("lagrangian_kernel_incidence_fixture_invalid")
    if kernel_incidence.get("claims_incidence_count_is_spectral_flow") or kernel_incidence.get("claims_incidence_count_is_maslov_index") or kernel_incidence.get("continuous_lagrangian_family_source_authorized") or kernel_incidence.get("gap_continuity_authorized") or kernel_incidence.get("self_adjoint_family_authorized"):
        errors.append("lagrangian_incidence_index_authority_laundered")
    strata_boundary_form = incidence_stratification.get("boundary_form", [])
    strata_operator = incidence_stratification.get("operator_matrix", [])
    strata_kernel_basis = incidence_stratification.get("bulk_kernel_basis", [])
    strata_domains = incidence_stratification.get("candidate_domain_bases", [])
    strata_kernel_valid = all(not any(matvec(strata_operator, [Fraction(x) for x in vector])) for vector in strata_kernel_basis)
    strata_domains_isotropic = []
    strata_intersections = []
    strata_restricted_kernels = []
    for basis in strata_domains:
        pairings = [sum((Fraction(left[i]) * Fraction(strata_boundary_form[i][j]) * Fraction(right[j]) for i in range(4) for j in range(4)), Fraction(0)) for left in basis for right in basis]
        strata_domains_isotropic.append(not any(pairings) and len(basis) == 2)
        combined_columns = strata_kernel_basis + basis
        combined_rows = [[combined_columns[col][row] for col in range(len(combined_columns))] for row in range(4)]
        combined_rank = len(rref(combined_rows)[1])
        strata_intersections.append(len(strata_kernel_basis) + len(basis) - combined_rank)
        restricted_image_columns = [matvec(strata_operator, [Fraction(x) for x in vector]) for vector in basis]
        restricted_image_rows = [[restricted_image_columns[col][row] for col in range(len(restricted_image_columns))] for row in range(4)]
        restricted_rank = len(rref(restricted_image_rows)[1])
        strata_restricted_kernels.append(len(basis) - restricted_rank)
    nested_strata_counts = {"at_least_1": sum(value >= 1 for value in strata_intersections), "at_least_2": sum(value >= 2 for value in strata_intersections)}
    if not strata_kernel_valid or not all(strata_domains_isotropic) or strata_intersections != incidence_stratification.get("expected_intersection_dimensions") or strata_restricted_kernels != incidence_stratification.get("expected_restricted_kernel_dimensions") or nested_strata_counts != incidence_stratification.get("expected_nested_strata_counts"):
        errors.append("lagrangian_incidence_stratification_fixture_invalid")
    if incidence_stratification.get("claims_finite_fixture_proves_global_schubert_geometry") or incidence_stratification.get("source_lagrangian_family_authorized"):
        errors.append("lagrangian_incidence_stratification_authority_laundered")
    graph_exponents = sorted(int(value) for value in graph_smith.get("diagonal_parameter_exponents", []))
    graph_determinantal_valuations = [sum(graph_exponents[:index]) for index in range(1, len(graph_exponents) + 1)]
    graph_smith_profile = [graph_determinantal_valuations[0]] + [graph_determinantal_valuations[index] - graph_determinantal_valuations[index - 1] for index in range(1, len(graph_determinantal_valuations))] if graph_determinantal_valuations else []
    graph_generic_intersection = sum(exponent < 0 for exponent in graph_exponents)
    graph_special_intersection = sum(exponent > 0 for exponent in graph_exponents)
    graph_total_defect_length = sum(graph_smith_profile)
    if graph_determinantal_valuations != graph_smith.get("expected_determinantal_valuations") or graph_smith_profile != graph_smith.get("expected_smith_profile") or graph_generic_intersection != graph_smith.get("expected_generic_intersection_dimension") or graph_special_intersection != graph_smith.get("expected_special_intersection_dimension") or graph_total_defect_length != graph_smith.get("expected_total_defect_length") or not graph_smith.get("regular_graph_chart_required"):
        errors.append("lagrangian_graph_smith_barcode_fixture_invalid")
    if graph_smith.get("claims_top_determinant_order_determines_special_corank") or graph_smith.get("source_analytic_boundary_graph_authorized"):
        errors.append("lagrangian_graph_smith_authority_laundered")
    chart_base_exponents = [int(value) for value in smith_chart.get("base_diagonal_exponents", [])]
    chart_transform = smith_chart.get("regular_constant_transform", [])
    chart_transform_det = chart_transform[0][0] * chart_transform[1][1] - chart_transform[0][1] * chart_transform[1][0]
    regular_entry_polynomials = [[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k, exponent in enumerate(chart_base_exponents):
                coefficient = chart_transform[k][i] * chart_transform[k][j]
                if coefficient:
                    regular_entry_polynomials[i][j][exponent] = regular_entry_polynomials[i][j].get(exponent, 0) + coefficient
    regular_entry_valuations = [[min(poly) if poly else None for poly in row] for row in regular_entry_polynomials]
    regular_determinant_valuation = sum(chart_base_exponents) + 2 * 0 if abs(chart_transform_det) == 1 else None
    regular_delta_1 = min(value for row in regular_entry_valuations for value in row if value is not None)
    regular_smith_profile = [regular_delta_1, regular_determinant_valuation - regular_delta_1]
    singular_shifts = [int(value) for value in smith_chart.get("singular_diagonal_transform_exponents", [])]
    singular_diagonal_exponents = [exponent + 2 * shift for exponent, shift in zip(chart_base_exponents, singular_shifts)]
    singular_smith_profile = sorted(singular_diagonal_exponents)
    if abs(chart_transform_det) != 1 or regular_entry_valuations != smith_chart.get("expected_regular_entry_valuations") or regular_determinant_valuation != smith_chart.get("expected_regular_determinant_valuation") or regular_smith_profile != smith_chart.get("expected_regular_smith_profile") or singular_diagonal_exponents != smith_chart.get("expected_singular_diagonal_exponents") or singular_smith_profile != smith_chart.get("expected_singular_smith_profile"):
        errors.append("boundary_smith_chart_invariance_fixture_invalid")
    if smith_chart.get("claims_singular_transform_is_admissible_chart") or smith_chart.get("claims_singular_profile_is_intrinsic"):
        errors.append("singular_boundary_chart_laundered")
    simultaneous_boundary_form = simultaneous_transport.get("boundary_form", [])
    simultaneous_map = simultaneous_transport.get("symplectic_transport", [])
    simultaneous_map_transpose = [list(row) for row in zip(*simultaneous_map)]
    transported_boundary_form = matrix_product(simultaneous_map_transpose, matrix_product(simultaneous_boundary_form, simultaneous_map))
    simultaneous_is_symplectic = transported_boundary_form == [[Fraction(x) for x in row] for row in simultaneous_boundary_form]
    simultaneous_domain = [Fraction(x) for x in simultaneous_transport.get("domain_generator", [])]
    simultaneous_kernel = [Fraction(x) for x in simultaneous_transport.get("kernel_generator", [])]
    transported_domain = matvec(simultaneous_map, simultaneous_domain)
    transported_kernel = matvec(simultaneous_map, simultaneous_kernel)
    def line_intersection_dimension(left: list[Fraction], right: list[Fraction]) -> int:
        return 1 if len(left) == 2 and len(right) == 2 and left[0] * right[1] - left[1] * right[0] == 0 else 0
    original_pair_intersection = line_intersection_dimension(simultaneous_domain, simultaneous_kernel)
    simultaneous_pair_intersection = line_intersection_dimension(transported_domain, transported_kernel)
    one_sided_pair_intersection = line_intersection_dimension(transported_domain, simultaneous_kernel)
    if not simultaneous_is_symplectic or original_pair_intersection != simultaneous_transport.get("expected_original_intersection_dimension") or simultaneous_pair_intersection != simultaneous_transport.get("expected_simultaneous_intersection_dimension") or one_sided_pair_intersection != simultaneous_transport.get("expected_one_sided_intersection_dimension"):
        errors.append("simultaneous_boundary_transport_fixture_invalid")
    if simultaneous_transport.get("claims_one_sided_transport_is_coordinate_change") or simultaneous_transport.get("source_bulk_kernel_transport_cell_authorized"):
        errors.append("boundary_transport_authority_laundered")
    source_operator = operator_transport.get("source_operator", [])
    domain_transport = operator_transport.get("domain_transport", [])
    codomain_transport = operator_transport.get("codomain_transport", [])
    transported_operator = operator_transport.get("transported_operator", [])
    transport_square_left = matrix_product(transported_operator, domain_transport)
    transport_square_right = matrix_product(codomain_transport, source_operator)
    transport_square_commutes = transport_square_left == transport_square_right
    source_domain_generator = [Fraction(x) for x in operator_transport.get("source_domain_generator", [])]
    source_kernel_generator = [Fraction(x) for x in operator_transport.get("source_kernel_generator", [])]
    transported_domain_generator = matvec(domain_transport, source_domain_generator)
    transported_kernel_generator = matvec(domain_transport, source_kernel_generator)
    source_kernel_valid = not any(matvec(source_operator, source_kernel_generator))
    transported_kernel_valid = not any(matvec(transported_operator, transported_kernel_generator))
    transported_domain_kernel_intersection = line_intersection_dimension(transported_domain_generator, transported_kernel_generator)
    one_sided_restricted_kernel_dimension = 1 if not any(matvec(source_operator, transported_domain_generator)) else 0
    if not source_kernel_valid or not transported_kernel_valid or transported_domain_generator != [Fraction(x) for x in operator_transport.get("expected_transported_domain_generator", [])] or transported_kernel_generator != [Fraction(x) for x in operator_transport.get("expected_transported_kernel_generator", [])] or transport_square_commutes != operator_transport.get("expected_square_commutes") or not operator_transport.get("codomain_transport_injective") or transported_domain_kernel_intersection != 1 or one_sided_restricted_kernel_dimension != 0:
        errors.append("operator_transport_square_fixture_invalid")
    if operator_transport.get("source_transport_square_authorized") or operator_transport.get("claims_domain_transport_alone_transports_kernel"):
        errors.append("operator_transport_square_authority_laundered")
    relative_source_operator = relative_injectivity.get("source_operator", [])
    relative_domain_transport = relative_injectivity.get("domain_transport", [])
    relative_good_transport = relative_injectivity.get("good_noninjective_codomain_transport", [])
    relative_bad_transport = relative_injectivity.get("bad_noninjective_codomain_transport", [])
    relative_good_operator = matrix_product(relative_good_transport, relative_source_operator)
    relative_bad_operator = matrix_product(relative_bad_transport, relative_source_operator)
    relative_source_rank = len(rref(relative_source_operator)[1])
    relative_good_rank = len(rref(relative_good_operator)[1])
    relative_bad_rank = len(rref(relative_bad_operator)[1])
    relative_source_kernel_dimension = len(relative_source_operator[0]) - relative_source_rank
    relative_good_kernel_dimension = len(relative_good_operator[0]) - relative_good_rank
    relative_bad_kernel_dimension = len(relative_bad_operator[0]) - relative_bad_rank
    good_injective_on_image = relative_good_rank == relative_source_rank
    bad_injective_on_image = relative_bad_rank == relative_source_rank
    good_square_commutes = matrix_product(relative_good_operator, relative_domain_transport) == matrix_product(relative_good_transport, relative_source_operator)
    bad_square_commutes = matrix_product(relative_bad_operator, relative_domain_transport) == matrix_product(relative_bad_transport, relative_source_operator)
    if not good_square_commutes or not bad_square_commutes or relative_source_kernel_dimension != relative_injectivity.get("expected_source_kernel_dimension") or relative_good_kernel_dimension != relative_injectivity.get("expected_good_transported_kernel_dimension") or relative_bad_kernel_dimension != relative_injectivity.get("expected_bad_transported_kernel_dimension") or good_injective_on_image != relative_injectivity.get("good_transport_injective_on_operator_image") or bad_injective_on_image != relative_injectivity.get("bad_transport_injective_on_operator_image"):
        errors.append("relative_codomain_injectivity_fixture_invalid")
    if relative_injectivity.get("claims_commuting_square_alone_preserves_kernel") or relative_injectivity.get("source_relative_injectivity_authorized"):
        errors.append("relative_codomain_injectivity_authority_laundered")
    _, relative_source_pivot_columns = rref(relative_source_operator)
    relative_image_basis = [[Fraction(relative_source_operator[row][column]) for row in range(len(relative_source_operator))] for column in relative_source_pivot_columns]
    def subspace_intersection_dimension(left_basis: list[list[Fraction]], right_basis: list[list[Fraction]], ambient_dimension: int) -> int:
        combined = left_basis + right_basis
        combined_rows = [[combined[column][row] for column in range(len(combined))] for row in range(ambient_dimension)] if combined else [[] for _ in range(ambient_dimension)]
        return len(left_basis) + len(right_basis) - len(rref(combined_rows)[1])
    good_transport_kernel_basis = nullspace(relative_good_transport)
    bad_transport_kernel_basis = nullspace(relative_bad_transport)
    good_overlap_dimension = subspace_intersection_dimension(relative_image_basis, good_transport_kernel_basis, len(relative_source_operator))
    bad_overlap_dimension = subspace_intersection_dimension(relative_image_basis, bad_transport_kernel_basis, len(relative_source_operator))
    good_excess_kernel_dimension = relative_good_kernel_dimension - relative_source_kernel_dimension
    bad_excess_kernel_dimension = relative_bad_kernel_dimension - relative_source_kernel_dimension
    if good_overlap_dimension != transport_residue.get("expected_good_overlap_dimension") or bad_overlap_dimension != transport_residue.get("expected_bad_overlap_dimension") or good_excess_kernel_dimension != transport_residue.get("expected_good_excess_kernel_dimension") or bad_excess_kernel_dimension != transport_residue.get("expected_bad_excess_kernel_dimension") or good_overlap_dimension != good_excess_kernel_dimension or bad_overlap_dimension != bad_excess_kernel_dimension or transport_residue.get("residue_kind") != "ordinary linear overlap quotient":
        errors.append("kernel_transport_residue_sequence_fixture_invalid")
    if transport_residue.get("claims_residue_is_tor_or_derived_kernel") or transport_residue.get("source_residue_readout_authorized"):
        errors.append("kernel_transport_residue_authority_laundered")
    composite_source_operator = composite_residue.get("source_operator", [])
    composite_first_transport = composite_residue.get("first_codomain_transport", [])
    composite_second_transport = composite_residue.get("second_codomain_transport", [])
    composite_first_operator = matrix_product(composite_first_transport, composite_source_operator)
    composite_final_operator = matrix_product(composite_second_transport, composite_first_operator)
    composite_width = len(composite_source_operator[0])
    composite_source_kernel_dimension = composite_width - len(rref(composite_source_operator)[1])
    composite_first_kernel_dimension = composite_width - len(rref(composite_first_operator)[1])
    composite_final_kernel_dimension = composite_width - len(rref(composite_final_operator)[1])
    composite_first_residue_dimension = composite_first_kernel_dimension - composite_source_kernel_dimension
    composite_second_residue_dimension = composite_final_kernel_dimension - composite_first_kernel_dimension
    composite_total_residue_dimension = composite_final_kernel_dimension - composite_source_kernel_dimension
    composite_residue_additive = composite_first_residue_dimension + composite_second_residue_dimension == composite_total_residue_dimension
    _, composite_first_image_pivots = rref(composite_first_operator)
    composite_first_image_basis = [[Fraction(composite_first_operator[row][column]) for row in range(len(composite_first_operator))] for column in composite_first_image_pivots]
    composite_second_kernel_basis = nullspace(composite_second_transport)
    composite_second_overlap_dimension = subspace_intersection_dimension(composite_first_image_basis, composite_second_kernel_basis, len(composite_first_operator))
    if composite_source_kernel_dimension != composite_residue.get("expected_source_kernel_dimension") or composite_first_kernel_dimension != composite_residue.get("expected_first_kernel_dimension") or composite_final_kernel_dimension != composite_residue.get("expected_composite_kernel_dimension") or composite_first_residue_dimension != composite_residue.get("expected_first_residue_dimension") or composite_second_residue_dimension != composite_residue.get("expected_second_residue_dimension") or composite_total_residue_dimension != composite_residue.get("expected_composite_residue_dimension") or composite_second_overlap_dimension != composite_second_residue_dimension or not composite_residue_additive or not composite_residue.get("residue_layers_are_logical_factorization_not_time"):
        errors.append("composite_transport_residue_filtration_fixture_invalid")
    if composite_residue.get("claims_final_nullity_forgets_residue_filtration") or composite_residue.get("source_composite_transport_authorized"):
        errors.append("composite_transport_residue_authority_laundered")
    factorization_source = factorization_flag.get("source_operator", [])
    factorization_a = factorization_flag.get("factorization_a", [])
    factorization_b = factorization_flag.get("factorization_b", [])
    composite_a = matrix_product(factorization_a[1], factorization_a[0])
    composite_b = matrix_product(factorization_b[1], factorization_b[0])
    first_operator_a = matrix_product(factorization_a[0], factorization_source)
    first_operator_b = matrix_product(factorization_b[0], factorization_source)
    final_operator_a = matrix_product(composite_a, factorization_source)
    final_operator_b = matrix_product(composite_b, factorization_source)
    first_kernel_a = nullspace(first_operator_a)
    first_kernel_b = nullspace(first_operator_b)
    final_kernel_a = nullspace(final_operator_a)
    final_kernel_b = nullspace(final_operator_b)
    common_composite = composite_a == composite_b == factorization_flag.get("expected_common_composite")
    distinct_first_flags = first_kernel_a != first_kernel_b
    same_final_kernel = final_kernel_a == final_kernel_b
    if not common_composite or [[int(x) for x in vector] for vector in first_kernel_a] != factorization_flag.get("expected_first_kernel_a") or [[int(x) for x in vector] for vector in first_kernel_b] != factorization_flag.get("expected_first_kernel_b") or len(final_kernel_a) != factorization_flag.get("expected_common_final_kernel_dimension") or not distinct_first_flags or not same_final_kernel:
        errors.append("factorization_dependent_residue_flag_fixture_invalid")
    if factorization_flag.get("claims_composite_map_canonically_determines_residue_flag") or factorization_flag.get("factorization_comparison_cell_authorized"):
        errors.append("factorization_residue_flag_authority_laundered")
    comparison_endpoint = flag_comparison.get("endpoint_operator", [])
    comparison_source_flag = [Fraction(x) for x in flag_comparison.get("source_flag_generator", [])]
    comparison_target_flag = [Fraction(x) for x in flag_comparison.get("target_flag_generator", [])]
    comparison_candidates = flag_comparison.get("comparison_candidates", [])
    comparison_invertible = [len(rref(candidate)[1]) == len(candidate) for candidate in comparison_candidates]
    comparison_commutes = [matrix_product(candidate, comparison_endpoint) == matrix_product(comparison_endpoint, candidate) for candidate in comparison_candidates]
    comparison_maps_flag = [matvec(candidate, comparison_source_flag) == comparison_target_flag for candidate in comparison_candidates]
    comparison_candidates_distinct = len(comparison_candidates) == 2 and comparison_candidates[0] != comparison_candidates[1]
    if len(comparison_candidates) != flag_comparison.get("expected_candidate_count") or all(comparison_invertible) != flag_comparison.get("all_candidates_invertible") or all(comparison_commutes) != flag_comparison.get("all_candidates_commute_with_endpoint") or all(comparison_maps_flag) != flag_comparison.get("all_candidates_map_source_flag_to_target") or not comparison_candidates_distinct or not flag_comparison.get("comparison_space_has_nontrivial_stabilizer"):
        errors.append("residue_flag_comparison_torsor_fixture_invalid")
    if flag_comparison.get("claims_existence_implies_canonical_comparison") or flag_comparison.get("source_comparison_choice_authorized"):
        errors.append("residue_flag_comparison_authority_laundered")
    triangle_endpoint = flag_triangle.get("endpoint_operator", [])
    triangle_flags = [[Fraction(x) for x in flag] for flag in flag_triangle.get("flag_generators", [])]
    triangle_maps = [flag_triangle.get("comparison_12", []), flag_triangle.get("comparison_23", []), flag_triangle.get("comparison_31", [])]
    triangle_pairwise_valid = [matvec(triangle_maps[0], triangle_flags[0]) == triangle_flags[1], matvec(triangle_maps[1], triangle_flags[1]) == triangle_flags[2], matvec(triangle_maps[2], triangle_flags[2]) == triangle_flags[0]]
    triangle_maps_invertible = [len(rref(comparison)[1]) == 2 for comparison in triangle_maps]
    triangle_maps_commute = [matrix_product(comparison, triangle_endpoint) == matrix_product(triangle_endpoint, comparison) for comparison in triangle_maps]
    triangle_holonomy = matrix_product(triangle_maps[2], matrix_product(triangle_maps[1], triangle_maps[0]))
    triangle_identity = flag_triangle.get("expected_identity", [])
    triangle_holonomy_stabilizes_source = matvec(triangle_holonomy, triangle_flags[0]) == triangle_flags[0]
    triangle_coherent = triangle_holonomy == triangle_identity
    if not all(triangle_pairwise_valid) or not all(triangle_maps_invertible) or not all(triangle_maps_commute) or triangle_holonomy != flag_triangle.get("expected_holonomy") or not triangle_holonomy_stabilizes_source or triangle_coherent or not flag_triangle.get("all_pairwise_comparisons_valid") or flag_triangle.get("holonomy_kind") != "nonidentity target-flag stabilizer automorphism":
        errors.append("residue_flag_triangle_holonomy_fixture_invalid")
    if flag_triangle.get("source_triangle_coherence_cell_authorized") or flag_triangle.get("claims_pairwise_validity_implies_triangle_coherence"):
        errors.append("residue_flag_triangle_coherence_laundered")
    def inverse_2x2(matrix: list[list[int | Fraction]]) -> list[list[Fraction]]:
        determinant = Fraction(matrix[0][0]) * Fraction(matrix[1][1]) - Fraction(matrix[0][1]) * Fraction(matrix[1][0])
        return [[Fraction(matrix[1][1]) / determinant, -Fraction(matrix[0][1]) / determinant], [-Fraction(matrix[1][0]) / determinant, Fraction(matrix[0][0]) / determinant]]
    vertex_gauges = holonomy_gauge.get("vertex_gauges", [])
    gauged_triangle_maps = [
        matrix_product(vertex_gauges[1], matrix_product(triangle_maps[0], inverse_2x2(vertex_gauges[0]))),
        matrix_product(vertex_gauges[2], matrix_product(triangle_maps[1], inverse_2x2(vertex_gauges[1]))),
        matrix_product(vertex_gauges[0], matrix_product(triangle_maps[2], inverse_2x2(vertex_gauges[2]))),
    ]
    gauged_holonomy = matrix_product(gauged_triangle_maps[2], matrix_product(gauged_triangle_maps[1], gauged_triangle_maps[0]))
    expected_gauged_holonomy = [[Fraction(x) for x in row] for row in holonomy_gauge.get("expected_gauged_holonomy", [])]
    holonomy_trace = triangle_holonomy[0][0] + triangle_holonomy[1][1]
    gauged_holonomy_trace = gauged_holonomy[0][0] + gauged_holonomy[1][1]
    holonomy_determinant = triangle_holonomy[0][0] * triangle_holonomy[1][1] - triangle_holonomy[0][1] * triangle_holonomy[1][0]
    gauged_holonomy_determinant = gauged_holonomy[0][0] * gauged_holonomy[1][1] - gauged_holonomy[0][1] * gauged_holonomy[1][0]
    holonomy_identity_status_preserved = (triangle_holonomy == triangle_identity) == (gauged_holonomy == triangle_identity)
    if triangle_holonomy != [[Fraction(x) for x in row] for row in holonomy_gauge.get("expected_original_holonomy", [])] or gauged_holonomy != expected_gauged_holonomy or holonomy_trace != gauged_holonomy_trace or holonomy_trace != holonomy_gauge.get("expected_trace") or holonomy_determinant != gauged_holonomy_determinant or holonomy_determinant != holonomy_gauge.get("expected_determinant") or holonomy_identity_status_preserved != holonomy_gauge.get("identity_status_gauge_invariant"):
        errors.append("triangle_holonomy_gauge_fixture_invalid")
    if holonomy_gauge.get("claims_raw_holonomy_matrix_is_gauge_invariant") or holonomy_gauge.get("source_stabilizer_trivialization_authorized"):
        errors.append("triangle_holonomy_gauge_authority_laundered")
    identity_holonomy = holonomy_observability.get("identity_holonomy", [])
    unipotent_holonomy = holonomy_observability.get("unipotent_holonomy", [])
    identity_trace = identity_holonomy[0][0] + identity_holonomy[1][1]
    unipotent_trace = unipotent_holonomy[0][0] + unipotent_holonomy[1][1]
    identity_determinant = identity_holonomy[0][0] * identity_holonomy[1][1] - identity_holonomy[0][1] * identity_holonomy[1][0]
    unipotent_determinant = unipotent_holonomy[0][0] * unipotent_holonomy[1][1] - unipotent_holonomy[0][1] * unipotent_holonomy[1][0]
    identity_displacement = [[identity_holonomy[i][j] - (1 if i == j else 0) for j in range(2)] for i in range(2)]
    unipotent_displacement = [[unipotent_holonomy[i][j] - (1 if i == j else 0) for j in range(2)] for i in range(2)]
    identity_displacement_rank = len(rref(identity_displacement)[1])
    unipotent_displacement_rank = len(rref(unipotent_displacement)[1])
    scalar_ports_collide = identity_trace == unipotent_trace and identity_determinant == unipotent_determinant
    if identity_trace != holonomy_observability.get("expected_common_trace") or unipotent_trace != holonomy_observability.get("expected_common_trace") or identity_determinant != holonomy_observability.get("expected_common_determinant") or unipotent_determinant != holonomy_observability.get("expected_common_determinant") or identity_displacement_rank != holonomy_observability.get("expected_identity_displacement_rank") or unipotent_displacement_rank != holonomy_observability.get("expected_unipotent_displacement_rank") or not scalar_ports_collide or holonomy_observability.get("trace_determinant_ports_jointly_faithful") or not holonomy_observability.get("displacement_rank_conjugacy_invariant"):
        errors.append("holonomy_observability_fixture_invalid")
    if holonomy_observability.get("source_displacement_rank_port_authorized") or holonomy_observability.get("claims_scalar_character_detects_all_holonomy"):
        errors.append("holonomy_observability_authority_laundered")
    unipotent_matrices = [unipotent_profile.get("unipotent_partition_31", []), unipotent_profile.get("unipotent_partition_22", [])]
    unipotent_traces = [sum(matrix[index][index] for index in range(4)) for matrix in unipotent_matrices]
    unipotent_displacements = [[[matrix[i][j] - (1 if i == j else 0) for j in range(4)] for i in range(4)] for matrix in unipotent_matrices]
    unipotent_rank_profiles = []
    for displacement in unipotent_displacements:
        power = displacement
        ranks = []
        for _ in range(3):
            ranks.append(len(rref(power)[1]))
            power = matrix_product(power, displacement)
        unipotent_rank_profiles.append(ranks)
    unipotent_determinants = [1 if all(matrix[i][i] == 1 for i in range(4)) and all(matrix[i][j] == 0 for i in range(4) for j in range(i)) else None for matrix in unipotent_matrices]
    if unipotent_traces != [unipotent_profile.get("expected_common_trace")] * 2 or unipotent_determinants != [unipotent_profile.get("expected_common_determinant")] * 2 or [profile[0] for profile in unipotent_rank_profiles] != [unipotent_profile.get("expected_common_first_displacement_rank")] * 2 or unipotent_rank_profiles[0] != unipotent_profile.get("expected_rank_profile_31") or unipotent_rank_profiles[1] != unipotent_profile.get("expected_rank_profile_22") or not unipotent_profile.get("rank_profile_determines_unipotent_jordan_partition") or unipotent_profile.get("single_displacement_rank_jointly_faithful"):
        errors.append("unipotent_holonomy_rank_profile_fixture_invalid")
    if unipotent_profile.get("source_rank_profile_ports_authorized") or unipotent_profile.get("claims_finite_rank_profile_is_full_general_holonomy_classifier"):
        errors.append("unipotent_rank_profile_authority_laundered")
    rational_identity = rational_holonomy.get("identity_matrix", [])
    rational_unipotent = rational_holonomy.get("unipotent_matrix", [])
    rational_traces = [matrix[0][0] + matrix[1][1] for matrix in [rational_identity, rational_unipotent]]
    rational_determinants = [matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] for matrix in [rational_identity, rational_unipotent]]
    rational_characteristic_polynomials_equal = rational_traces[0] == rational_traces[1] and rational_determinants[0] == rational_determinants[1]
    identity_pencil_has_unit_entry = any(rational_identity[i][j] != 0 for i in range(2) for j in range(2) if i != j)
    unipotent_pencil_has_unit_entry = any(rational_unipotent[i][j] != 0 for i in range(2) for j in range(2) if i != j)
    identity_pencil_factors = ["1", "(x-1)^2"] if identity_pencil_has_unit_entry else ["x-1", "x-1"]
    unipotent_pencil_factors = ["1", "(x-1)^2"] if unipotent_pencil_has_unit_entry else ["x-1", "x-1"]
    if rational_holonomy.get("base_field") != "Q" or not rational_characteristic_polynomials_equal or rational_holonomy.get("expected_common_characteristic_polynomial") != "(x-1)^2" or identity_pencil_factors != rational_holonomy.get("expected_identity_pencil_invariant_factors") or unipotent_pencil_factors != rational_holonomy.get("expected_unipotent_pencil_invariant_factors") or not rational_holonomy.get("polynomial_pencil_smith_data_classifies_similarity"):
        errors.append("rational_canonical_holonomy_fixture_invalid")
    if rational_holonomy.get("claims_characteristic_polynomial_classifies_similarity") or rational_holonomy.get("source_polynomial_pencil_ports_authorized") or rational_holonomy.get("claims_field_classifier_applies_unchanged_over_completion_ring"):
        errors.append("rational_canonical_holonomy_authority_laundered")
    fitting_matrix_a = non_pid_fitting.get("matrix_a", [])
    fitting_matrix_b = non_pid_fitting.get("matrix_b", [])
    fitting_fixture_exact = fitting_matrix_a == [["u", "0"], ["0", "v"]] and fitting_matrix_b == [["1", "0"], ["0", "uv"]]
    fitting_common_determinant_ideal = "(uv)" if fitting_fixture_exact else None
    fitting_first_ideal_a = "(u,v)" if fitting_fixture_exact else None
    fitting_first_ideal_b = "(1)" if fitting_fixture_exact else None
    fitting_ideals_distinct = fitting_first_ideal_a != fitting_first_ideal_b
    if non_pid_fitting.get("coefficient_ring") != "Q[u,v]" or non_pid_fitting.get("ring_is_pid") or not fitting_fixture_exact or fitting_common_determinant_ideal != non_pid_fitting.get("expected_common_determinant_ideal") or fitting_first_ideal_a != non_pid_fitting.get("expected_first_determinantal_ideal_a") or fitting_first_ideal_b != non_pid_fitting.get("expected_first_determinantal_ideal_b") or non_pid_fitting.get("first_ideal_a_principal") or not non_pid_fitting.get("fitting_ideals_preserved_under_module_presentation_change"):
        errors.append("non_pid_fitting_holonomy_fixture_invalid")
    if non_pid_fitting.get("claims_smith_normal_form_exists_over_ring") or non_pid_fitting.get("claims_equal_determinant_ideal_implies_equal_cokernel_module") or non_pid_fitting.get("source_completion_coefficient_ring_authorized"):
        errors.append("non_pid_fitting_holonomy_authority_laundered")
    def evaluate_fitting_token(token: str, u_value: int, v_value: int) -> int:
        return {"0": 0, "1": 1, "u": u_value, "v": v_value, "uv": u_value * v_value}[token]
    fitting_sample_points = fitting_strata.get("sample_points", [])
    fitting_ranks_a = []
    fitting_ranks_b = []
    fitting_determinant_zero_a = []
    fitting_determinant_zero_b = []
    for u_value, v_value in fitting_sample_points:
        evaluated_a = [[evaluate_fitting_token(token, u_value, v_value) for token in row] for row in fitting_matrix_a]
        evaluated_b = [[evaluate_fitting_token(token, u_value, v_value) for token in row] for row in fitting_matrix_b]
        fitting_ranks_a.append(len(rref(evaluated_a)[1]))
        fitting_ranks_b.append(len(rref(evaluated_b)[1]))
        fitting_determinant_zero_a.append(evaluated_a[0][0] * evaluated_a[1][1] - evaluated_a[0][1] * evaluated_a[1][0] == 0)
        fitting_determinant_zero_b.append(evaluated_b[0][0] * evaluated_b[1][1] - evaluated_b[0][1] * evaluated_b[1][0] == 0)
    if fitting_ranks_a != fitting_strata.get("expected_ranks_a") or fitting_ranks_b != fitting_strata.get("expected_ranks_b") or fitting_determinant_zero_a != fitting_strata.get("expected_common_determinant_zero_pattern") or fitting_determinant_zero_b != fitting_strata.get("expected_common_determinant_zero_pattern") or fitting_strata.get("rank_at_most_1_locus") != "V(uv) for both presentations" or fitting_strata.get("rank_at_most_0_locus_a") != "V(u,v)" or fitting_strata.get("rank_at_most_0_locus_b") != "empty":
        errors.append("fitting_rank_stratification_fixture_invalid")
    if fitting_strata.get("claims_common_determinant_divisor_implies_common_rank_stratification") or fitting_strata.get("source_geometric_family_authorized"):
        errors.append("fitting_rank_stratification_authority_laundered")
    slice_exponents = [int(value) for value in directional_slice.get("slice_exponents", [])]
    slice_determinant_orders = [1 + exponent for exponent in slice_exponents]
    slice_profiles_a = [[1, exponent] if exponent >= 1 else [exponent, 1] for exponent in slice_exponents]
    slice_profiles_b = [[0, 1 + exponent] for exponent in slice_exponents]
    slice_special_coranks_a = [sum(order > 0 for order in profile) for profile in slice_profiles_a]
    slice_special_coranks_b = [sum(order > 0 for order in profile) for profile in slice_profiles_b]
    if slice_determinant_orders != directional_slice.get("expected_determinant_orders") or slice_profiles_a != directional_slice.get("expected_profiles_a") or slice_profiles_b != directional_slice.get("expected_profiles_b") or slice_special_coranks_a != directional_slice.get("expected_special_coranks_a") or slice_special_coranks_b != directional_slice.get("expected_special_coranks_b") or directional_slice.get("parameter_kind") != "local algebraic coordinate, not time or epoch":
        errors.append("directional_fitting_slice_fixture_invalid")
    if directional_slice.get("claims_single_slice_recovers_multivariable_fitting_object") or directional_slice.get("source_slice_selection_authorized"):
        errors.append("directional_fitting_slice_authority_laundered")
    arc_exponents = arc_closure.get("monomial_arc_exponents", [])
    arc_orders_i = [min(2 * int(a), 2 * int(b)) for a, b in arc_exponents]
    arc_orders_j = [min(2 * int(a), int(a) + int(b), 2 * int(b)) for a, b in arc_exponents]
    arc_orders_collide = arc_orders_i == arc_orders_j
    if arc_closure.get("coefficient_ring") != "Q[u,v]" or arc_closure.get("ideal_i_generators") != ["u^2", "v^2"] or arc_closure.get("ideal_j_generators") != ["u^2", "uv", "v^2"] or arc_orders_i != arc_closure.get("expected_orders_i") or arc_orders_j != arc_closure.get("expected_orders_j") or not arc_orders_collide or arc_closure.get("ideals_equal") or arc_closure.get("uv_belongs_to_i") or not arc_closure.get("uv_belongs_to_j") or not arc_closure.get("integral_closures_equal") or arc_closure.get("valuative_reconstruction_target") != "integral closure under the stated Noetherian-domain hypotheses":
        errors.append("arc_valuation_integral_closure_fixture_invalid")
    if arc_closure.get("claims_all_arc_orders_recover_exact_ideal") or arc_closure.get("source_complete_arc_family_authorized"):
        errors.append("arc_valuation_reconstruction_authority_laundered")
    closure_residue_relations_valid = closure_residue.get("u_times_generator_in_i") and closure_residue.get("v_times_generator_in_i") and not closure_residue.get("generator_in_i")
    closure_residue_supported_at_origin = closure_residue.get("expected_annihilator") == "(u,v)" and closure_residue.get("expected_support") == "origin V(u,v)"
    if closure_residue.get("inclusion") != "I=(u^2,v^2) subset J=(u^2,uv,v^2)" or closure_residue.get("quotient") != "J/I" or closure_residue.get("primitive_quotient_generator") != "class of uv" or not closure_residue_relations_valid or not closure_residue_supported_at_origin or closure_residue.get("expected_local_length") != 1 or closure_residue.get("arc_order_readout_detects_residue") or not closure_residue.get("exact_ideal_or_rees_data_detects_residue"):
        errors.append("integral_closure_supported_residue_fixture_invalid")
    if closure_residue.get("source_scheme_sensitive_port_authorized") or closure_residue.get("claims_integral_closure_preserves_supported_residue"):
        errors.append("integral_closure_supported_residue_authority_laundered")
    ideal_closure_length = len(ideal_filtration.get("closure_residue_basis", []))
    ideal_radicalization_length = len(ideal_filtration.get("radicalization_residue_basis", []))
    ideal_total_residue_length = ideal_closure_length + ideal_radicalization_length
    ideal_layers_typed = ideal_filtration.get("valuative_readout_retains") == "integral closure" and ideal_filtration.get("support_readout_retains") == "radical"
    if ideal_filtration.get("exact_ideal") != "I=(u^2,v^2)" or ideal_filtration.get("integral_closure") != "Ibar=(u,v)^2" or ideal_filtration.get("radical") != "sqrt(I)=(u,v)" or ideal_filtration.get("closure_residue_basis") != ["uv"] or ideal_filtration.get("radicalization_residue_basis") != ["u", "v"] or ideal_closure_length != ideal_filtration.get("expected_closure_residue_length") or ideal_radicalization_length != ideal_filtration.get("expected_radicalization_residue_length") or ideal_total_residue_length != ideal_filtration.get("expected_total_residue_length") or ideal_filtration.get("exact_sequence") != "0 -> Ibar/I -> sqrt(I)/I -> sqrt(I)/Ibar -> 0" or not ideal_layers_typed:
        errors.append("ideal_information_loss_filtration_fixture_invalid")
    if ideal_filtration.get("claims_closure_and_radical_residues_are_interchangeable") or ideal_filtration.get("source_full_ideal_filtration_port_authorized"):
        errors.append("ideal_information_loss_filtration_authority_laundered")
    completed_residue_lengths = list(completion_comparison.get("input_residue_lengths", [])) if completion_comparison.get("ring_noetherian") and completion_comparison.get("adic_completion_flat") and completion_comparison.get("adic_completion_faithfully_flat_on_finite_modules") else []
    if completion_comparison.get("local_ring") != "Q[u,v]_(u,v)" or completion_comparison.get("adic_completion") != "Q[[u,v]]" or completion_comparison.get("completion_ideal") != "(u,v)" or not completion_comparison.get("ring_noetherian") or not completion_comparison.get("adic_completion_flat") or not completion_comparison.get("adic_completion_faithfully_flat_on_finite_modules") or completed_residue_lengths != completion_comparison.get("expected_completed_residue_lengths") or completion_comparison.get("weakstar_completion_kind") != "topological dual completion against declared source tests" or completion_comparison.get("weakstar_is_ordinary_adic_base_change") or completion_comparison.get("weakstar_exactness_authorized"):
        errors.append("adic_versus_weakstar_completion_fixture_invalid")
    if completion_comparison.get("claims_adic_flatness_proves_weakstar_exactness") or completion_comparison.get("source_weakstar_comparison_cell_authorized"):
        errors.append("weakstar_completion_authority_laundered")
    weakstar_basis_values = weakstar_constructor.get("sum_port_values_on_basis", [])
    weakstar_sum_discontinuous_witness = weakstar_constructor.get("basis_sequence_weakstar_limit") == "0" and all(value == 1 for value in weakstar_basis_values)
    weakstar_constructor_typed = weakstar_constructor.get("source_space") == "c00" and weakstar_constructor.get("declared_predual") == "ell1" and weakstar_constructor.get("ambient_dual") == "ell_infinity" and weakstar_constructor.get("completion") == "weak-star closure of c00 in ell_infinity" and weakstar_constructor.get("expected_completion") == "ell_infinity"
    if not weakstar_constructor_typed or weakstar_constructor.get("coordinate_port_predual_vector") != "e_1 in ell1" or not weakstar_constructor.get("coordinate_port_extends") or weakstar_constructor.get("sum_port_coefficient") != "(1,1,...) not in ell1" or not weakstar_sum_discontinuous_witness or weakstar_constructor.get("sum_port_extends_weakstar_continuously") or weakstar_constructor.get("required_map_gate") != "map is adjoint of a continuous predual map" or weakstar_constructor.get("required_exactness_gates") != ["predual exactness", "weak-star closed image", "dual separation"]:
        errors.append("weakstar_completion_constructor_fixture_invalid")
    if weakstar_constructor.get("theta_dual_pair_source_authorized") or weakstar_constructor.get("claims_algebraic_functional_extends_to_weakstar_completion"):
        errors.append("weakstar_completion_constructor_authority_laundered")
    magnetic_degrees = [int(value) for value in magnetic_ports.get("kernel_harmonic_degrees", [])]
    magnetic_multiplicities = [2 * degree + 1 for degree in magnetic_degrees]
    magnetic_labels = [(degree, order) for degree in magnetic_degrees for order in range(-degree, degree + 1)]
    magnetic_kernel_dimension = len(magnetic_labels)
    magnetic_observation_matrix = [[1 if row == column else 0 for column in range(magnetic_kernel_dimension)] for row in range(magnetic_kernel_dimension)]
    magnetic_observation_rank = len(rref(magnetic_observation_matrix)[1])
    magnetic_deleted_rank = len(rref(magnetic_observation_matrix[:-1])[1])
    magnetic_joint_faithful = magnetic_observation_rank == magnetic_kernel_dimension and magnetic_ports.get("joint_map_with_A3_faithful")
    if magnetic_ports.get("sector") != "grade-three magnetic parity" or magnetic_ports.get("source_artifact") != "research/strominger/functional-completion-extension-master-theorem.md" or magnetic_ports.get("declared_predual") != "C(S^2)" or magnetic_ports.get("ambient_dual") != "M(S^2)=C(S^2)^*" or magnetic_multiplicities != magnetic_ports.get("expected_multiplicities") or magnetic_kernel_dimension != magnetic_ports.get("expected_kernel_dimension") or not magnetic_ports.get("port_tests_are_continuous") or magnetic_observation_rank != magnetic_ports.get("expected_observation_rank") or magnetic_deleted_rank != magnetic_ports.get("expected_deleted_port_rank") or not magnetic_joint_faithful or magnetic_ports.get("fewer_than_21_ports_can_be_faithful") or not magnetic_ports.get("ports_executable_as_finite_integrals") or not magnetic_ports.get("source_dual_pair_authorized"):
        errors.append("magnetic_weakstar_low_mode_ports_fixture_invalid")
    if magnetic_ports.get("claims_ports_follow_from_geometric_support_alone"):
        errors.append("magnetic_low_mode_port_authority_laundered")
    hard_flux_degrees = [int(value) for value in hard_flux.get("harmonic_degrees", [])]
    hard_flux_multiplicities = [2 * degree + 1 for degree in hard_flux_degrees]
    hard_flux_rank = sum(multiplicity for multiplicity, nonzero in zip(hard_flux_multiplicities, hard_flux.get("source_multipliers_nonzero", [])) if nonzero)
    hard_flux_variance_typed = hard_flux.get("variance") == {"states": "covariant source-to-shear", "tests": "contravariant target-test pullback"}
    hard_flux_support_typed = hard_flux.get("angular_support") == "compact sphere S^2" and hard_flux.get("retarded_support_requirement") == "compact support or declared integrability for pushforward" and hard_flux.get("angular_projection_proper") and not hard_flux.get("retarded_pushforward_proper_without_support")
    if hard_flux.get("source_artifacts") != ["research/strominger/functional-completion-extension-master-theorem.md", "research/strominger/functional-completion-extension-correction-audit.md"] or hard_flux.get("source_object") != "weak-star smooth coexact angular-flux channel" or hard_flux.get("target_object") != "magnetic low-harmonic shear block H_2 direct_sum H_3 direct_sum H_4" or not hard_flux_variance_typed or hard_flux_multiplicities != hard_flux.get("multiplicities") or not all(hard_flux.get("source_multipliers_nonzero", [])) or hard_flux_rank != hard_flux.get("expected_correspondence_rank") or not hard_flux_support_typed or not hard_flux.get("linear_constructibility_authorized") or hard_flux.get("nonlinear_dominant_energy_realizability_authorized") or hard_flux.get("construction_supplies_observation_ports"):
        errors.append("magnetic_hard_flux_correspondence_fixture_invalid")
    if hard_flux.get("claims_geometric_support_implies_constructibility"):
        errors.append("magnetic_hard_flux_correspondence_authority_laundered")
    characteristic_factorization_valid = characteristic_separation.get("local_symbol") == "p^4-q^4" and characteristic_separation.get("factorization") == ["p-q", "p+q", "p-iq", "p+iq"]
    compact_support_kernel_dimension = 0 if characteristic_separation.get("compact_support_fourier_transform_type") == "entire function" and characteristic_separation.get("symbol_nonzero_on_dense_open") else None
    planar_l2_kernel_dimension = 0 if characteristic_separation.get("real_characteristic_set_measure_zero") else None
    characteristic_completed_degrees = [int(value) for value in characteristic_separation.get("completed_kernel_degrees", [])]
    characteristic_completed_dimension = sum(2 * degree + 1 for degree in characteristic_completed_degrees)
    characteristic_objects_distinct = characteristic_separation.get("characteristic_object_type") != characteristic_separation.get("completed_kernel_object_type") and compact_support_kernel_dimension == 0 and planar_l2_kernel_dimension == 0 and characteristic_completed_dimension > 0
    if not characteristic_factorization_valid or characteristic_separation.get("characteristic_object_type") != "local cotangent support variety" or compact_support_kernel_dimension != characteristic_separation.get("expected_compactly_supported_homogeneous_kernel_dimension") or planar_l2_kernel_dimension != characteristic_separation.get("expected_planar_L2_homogeneous_kernel_dimension") or characteristic_separation.get("completed_kernel_object_type") != "global smooth spherical spectral block" or characteristic_completed_dimension != characteristic_separation.get("expected_completed_kernel_dimension") or characteristic_separation.get("completed_kernel_source") != "zeros of global multiplier lambda_l" or not characteristic_objects_distinct:
        errors.append("characteristic_locus_completed_kernel_separation_fixture_invalid")
    if characteristic_separation.get("claims_characteristic_locus_equals_completed_kernel") or characteristic_separation.get("claims_characteristic_support_constructs_global_state"):
        errors.append("characteristic_locus_kernel_authority_laundered")
    cross_sector_ranks_equal = cross_sector_rank.get("left_rank") == cross_sector_rank.get("right_rank")
    cross_sector_provenance_typed = bool(cross_sector_rank.get("left_source_artifact")) and bool(cross_sector_rank.get("left_source_sha256")) and bool(cross_sector_rank.get("right_source_artifact")) and bool(cross_sector_rank.get("right_source_sha256"))
    if cross_sector_rank.get("left_rank") != 21 or cross_sector_rank.get("right_rank") != 26 or cross_sector_rank.get("historical_right_rank") != 21 or cross_sector_rank.get("historical_status") != "cutoff-five plateau superseded by geometric stabilization" or cross_sector_rank.get("current_same_rank") != cross_sector_ranks_equal or not cross_sector_provenance_typed or cross_sector_rank.get("disposition") != "no_current_rank_coincidence" or not cross_sector_rank.get("requires_digest_refresh_on_source_change"):
        errors.append("cross_sector_rank_provenance_fixture_invalid")
    if cross_sector_rank.get("comparison_map") is not None or cross_sector_rank.get("identified"):
        errors.append("cross_sector_rank_identification_laundered")
    composite_degrees = [int(value) for value in magnetic_composite.get("harmonic_degrees", [])]
    composite_multiplicities = [2 * degree + 1 for degree in composite_degrees]
    composite_nonzero_flags = magnetic_composite.get("source_multipliers_nonzero", [])
    construction_rank = sum(multiplicity for multiplicity, nonzero in zip(composite_multiplicities, composite_nonzero_flags) if nonzero)
    observation_rank = magnetic_kernel_dimension
    composite_label_count = len([(degree, order) for degree in composite_degrees for order in range(-degree, degree + 1)])
    composite_coherence_authorized = magnetic_composite.get("label_normalization_coherence_cell") == "same normalized real magnetic harmonic basis" and magnetic_composite.get("label_normalization_coherence_source_authorized")
    magnetic_composite_rank = min(construction_rank, observation_rank, composite_label_count) if composite_coherence_authorized else 0
    magnetic_composite_faithful = magnetic_composite_rank == composite_label_count and all(composite_nonzero_flags)
    if magnetic_composite.get("source_multiplier_symbols") != ["mu_2", "mu_3", "mu_4"] or construction_rank != magnetic_composite.get("construction_rank") or observation_rank != magnetic_composite.get("observation_rank") or not composite_coherence_authorized or magnetic_composite_rank != magnetic_composite.get("expected_composite_rank") or magnetic_composite_faithful != magnetic_composite.get("composite_faithful_on_low_source_block") or not magnetic_composite.get("algebraic_low_block_inverse_exists") or magnetic_composite.get("nonlinear_source_controller_authorized"):
        errors.append("magnetic_construction_observation_composition_fixture_invalid")
    if magnetic_composite.get("claims_equal_ranks_imply_composable_capabilities"):
        errors.append("magnetic_capability_composition_authority_laundered")
    stability_multipliers = [Fraction(value) for value in magnetic_stability.get("magnetic_hodge_multipliers", [])]
    stability_singular_values = [abs(value) for value in stability_multipliers]
    stability_minimum = min(stability_singular_values) if stability_singular_values else None
    stability_maximum = max(stability_singular_values) if stability_singular_values else None
    stability_inverse_norm = Fraction(1, stability_minimum) if stability_minimum else None
    stability_condition_number = stability_maximum / stability_minimum if stability_minimum else None
    if magnetic_stability.get("source_artifact") != "research/strominger/results/hard_flux_low_kernel_constructibility.json" or magnetic_stability.get("normalized_harmonic_degrees") != [2, 3, 4] or stability_multipliers != [Fraction(-6), Fraction(-12), Fraction(-20)] or stability_minimum != magnetic_stability.get("expected_minimum_singular_value") or stability_maximum != magnetic_stability.get("expected_maximum_singular_value") or stability_inverse_norm != Fraction(*magnetic_stability.get("expected_inverse_norm", [0, 1])) or stability_condition_number != Fraction(*magnetic_stability.get("expected_condition_number", [0, 1])) or not magnetic_stability.get("observation_map_isometry_on_normalized_low_block") or not magnetic_stability.get("quantitative_low_block_reconstruction_authorized"):
        errors.append("magnetic_low_block_stability_fixture_invalid")
    if magnetic_stability.get("claims_bound_is_uniform_outside_low_block") or magnetic_stability.get("claims_linear_stability_implies_nonlinear_control"):
        errors.append("magnetic_low_block_stability_authority_laundered")
    margin_sigma = Fraction(magnetic_margin.get("unperturbed_minimum_singular_value", 0))
    margin_perturbations = [Fraction(value) for value in magnetic_margin.get("operator_norm_perturbations", [])]
    margin_lower_bounds = [max(Fraction(0), margin_sigma - delta) for delta in margin_perturbations]
    margin_inverse_norms = [Fraction(1, bound) if bound > 0 else None for bound in margin_lower_bounds]
    expected_margin_inverse_norms = [Fraction(*value) if value is not None else None for value in magnetic_margin.get("expected_certified_inverse_norms", [])]
    margin_boundary_index = margin_perturbations.index(Fraction(magnetic_margin.get("boundary_delta"))) if Fraction(magnetic_margin.get("boundary_delta")) in margin_perturbations else None
    margin_boundary_guaranteed = margin_boundary_index is not None and margin_lower_bounds[margin_boundary_index] > 0
    if margin_sigma != 6 or margin_lower_bounds != magnetic_margin.get("expected_weyl_lower_bounds") or margin_inverse_norms != expected_margin_inverse_norms or magnetic_margin.get("strict_faithfulness_margin") != "delta<6" or margin_boundary_guaranteed != magnetic_margin.get("faithfulness_guaranteed_at_boundary") or magnetic_margin.get("parameter_kind") != "operator norm radius, not time or epoch":
        errors.append("magnetic_low_block_perturbation_margin_fixture_invalid")
    if magnetic_margin.get("physical_noise_model_source_authorized") or magnetic_margin.get("claims_mathematical_margin_is_physical_tolerance"):
        errors.append("magnetic_perturbation_margin_authority_laundered")
    frame_dimension = int(magnetic_frame.get("kernel_dimension", 0))
    frame_matrix = [[1 if row == column else 0 for column in range(frame_dimension)] for row in range(frame_dimension)] + [[1 for _ in range(frame_dimension)]]
    frame_full_rank = len(rref(frame_matrix)[1])
    frame_deletion_ranks = [len(rref(frame_matrix[:index] + frame_matrix[index + 1:])[1]) for index in range(len(frame_matrix))]
    frame_minimum_deletion_rank = min(frame_deletion_ranks) if frame_deletion_ranks else 0
    hostile_deleted_indices = set(magnetic_frame.get("hostile_two_port_deletion", []))
    hostile_two_port_matrix = [row for index, row in enumerate(frame_matrix) if index not in hostile_deleted_indices]
    hostile_two_port_rank = len(rref(hostile_two_port_matrix)[1])
    if magnetic_frame.get("base_ports") != "21 coordinate harmonic coefficient tests" or magnetic_frame.get("redundant_port") != "sum of all 21 normalized harmonic tests" or len(frame_matrix) != magnetic_frame.get("total_port_count") or frame_full_rank != magnetic_frame.get("expected_full_rank") or frame_minimum_deletion_rank != magnetic_frame.get("expected_minimum_one_port_deletion_rank") or not magnetic_frame.get("one_port_deletion_tolerant") or hostile_two_port_rank != magnetic_frame.get("expected_hostile_two_port_rank") or magnetic_frame.get("two_port_deletion_tolerant") or not magnetic_frame.get("redundant_test_is_continuous_predual_element") or not magnetic_frame.get("redundant_port_source_authorized"):
        errors.append("magnetic_redundant_observation_frame_fixture_invalid")
    if magnetic_frame.get("claims_minimal_faithful_fiber_is_deletion_tolerant"):
        errors.append("magnetic_observation_redundancy_authority_laundered")
    erasure_dimension = int(magnetic_erasure_frame.get("kernel_dimension", 0))
    erasure_budget = int(magnetic_erasure_frame.get("redundancy_budget", -1))
    erasure_nodes = list(range(erasure_dimension + erasure_budget))
    surviving_node_sets = list(combinations(erasure_nodes, erasure_dimension)) if erasure_dimension > 0 and erasure_budget >= 0 else []
    surviving_determinants_nonzero = all(
        all(right != left for index, left in enumerate(nodes) for right in nodes[index + 1:])
        for nodes in surviving_node_sets
    )
    four_deletion_rank = min(erasure_dimension, max(0, len(erasure_nodes) - erasure_budget - 1))
    bounded_replay = {}
    for dimension in magnetic_erasure_frame.get("bounded_replay_dimensions", []):
        for budget in magnetic_erasure_frame.get("bounded_replay_budgets", []):
            nodes = list(range(dimension + budget))
            determinants = [
                all(right != left for index, left in enumerate(kept) for right in kept[index + 1:])
                for kept in combinations(nodes, dimension)
            ]
            bounded_replay[f"n={dimension},s={budget}"] = bool(determinants) and all(determinants)
    if erasure_dimension != 21 or erasure_budget != 3 or len(erasure_nodes) != magnetic_erasure_frame.get("expected_total_port_count") or not surviving_determinants_nonzero or magnetic_erasure_frame.get("expected_surviving_rank_after_any_three_deletions") != 21 or four_deletion_rank != magnetic_erasure_frame.get("expected_rank_after_four_deletions") or not all(bounded_replay.values()):
        errors.append("magnetic_erasure_budget_frame_fixture_invalid")
    if not magnetic_erasure_frame.get("finite_linear_aggregation_of_authorized_ports") or not magnetic_erasure_frame.get("source_authorizes_finite_linear_aggregation") or magnetic_erasure_frame.get("claims_algebraic_full_spark_implies_executable_without_aggregation_authority"):
        errors.append("magnetic_erasure_frame_authority_laundered")
    if magnetic_erasure_frame.get("claims_three_erasure_budget_tolerates_four_deletions"):
        errors.append("magnetic_erasure_budget_overclaimed")
    decoder_length = int(magnetic_decoder.get("code_length", 0))
    decoder_dimension = int(magnetic_decoder.get("message_dimension", 0))
    decoder_distance = decoder_length - decoder_dimension + 1
    decoder_errors = int(magnetic_decoder.get("correctable_error_count", -1))
    decoder_erasures = int(magnetic_decoder.get("correctable_erasure_count", -1))
    decoder_correctable = 2 * decoder_errors + decoder_erasures < decoder_distance
    hostile_errors = int(magnetic_decoder.get("hostile_uncorrectable_error_count", -1))
    hostile_erasures = int(magnetic_decoder.get("hostile_uncorrectable_erasure_count", -1))
    hostile_correctable = 2 * hostile_errors + hostile_erasures < decoder_distance
    decoder_region = {
        f"e={errors_count},s={erasures_count}": 2 * errors_count + erasures_count < decoder_distance
        for errors_count in range(3)
        for erasures_count in range(5)
    }
    if decoder_length != 24 or decoder_dimension != 21 or decoder_distance != magnetic_decoder.get("expected_minimum_distance") or magnetic_decoder.get("expected_decoding_inequality") != "2e+s<d" or not decoder_correctable or hostile_correctable or magnetic_decoder.get("claims_boundary_case_is_uniquely_decodable"):
        errors.append("magnetic_error_erasure_decoder_fixture_invalid")
    if not magnetic_decoder.get("algebraic_decoder_is_finite_executable_algorithm") or magnetic_decoder.get("physical_fault_model_source_authorized") or magnetic_decoder.get("fault_location_semantics_source_authorized") or magnetic_decoder.get("claims_algebraic_decoder_supplies_physical_fault_diagnosis"):
        errors.append("magnetic_decoder_authority_laundered")
    conditioning_shape = magnetic_conditioning.get("frame_shape", [])
    integer_condition = float(magnetic_conditioning.get("integer_monomial_condition_estimate", 0))
    scaled_condition = float(magnetic_conditioning.get("scaled_monomial_condition_estimate", 0))
    chebyshev_condition_squared = magnetic_conditioning.get("chebyshev_gauss_exact_full_condition_squared")
    deletion_condition = float(magnetic_conditioning.get("chebyshev_gauss_worst_three_deletion_condition_estimate", 0))
    conditioning_separation = integer_condition > 1e20 and scaled_condition > 1e8 and chebyshev_condition_squared == 2 and deletion_condition > 1e5
    if conditioning_shape != [24, 21] or magnetic_conditioning.get("domain_norm") != "Euclidean norm in normalized real harmonic basis" or not conditioning_separation or magnetic_conditioning.get("worst_three_deleted_rows") != [0, 1, 2] or magnetic_conditioning.get("numerical_evidence_backend") != "numpy 2.5.2 float64 SVD" or not magnetic_conditioning.get("exact_full_orthogonality_identity") or not magnetic_conditioning.get("all_three_deletion_submatrices_injective") or magnetic_conditioning.get("uniform_three_deletion_stability_certified"):
        errors.append("magnetic_frame_conditioning_fixture_invalid")
    if not magnetic_conditioning.get("chebyshev_tests_are_continuous") or magnetic_conditioning.get("chebyshev_coefficients_fit_exact_rational_record_schema") or magnetic_conditioning.get("approximate_instrument_realization_source_authorized") or magnetic_conditioning.get("claims_full_spark_implies_uniform_stability") or magnetic_conditioning.get("claims_continuity_implies_exact_executability"):
        errors.append("magnetic_frame_conditioning_authority_laundered")
    naimark_ports = int(magnetic_naimark.get("ambient_port_count", 0))
    naimark_signal = int(magnetic_naimark.get("signal_dimension", 0))
    naimark_complement = int(magnetic_naimark.get("complement_dimension", 0))
    hadamard = [[Fraction(value, 2) for value in row] for row in [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]]
    fixture_a = [row[:3] for row in hadamard]
    fixture_b = [row[3:] for row in hadamard]
    deleted_index = 0
    retained_a = [row for index, row in enumerate(fixture_a) if index != deleted_index]
    retained_gram = [[sum(row[i] * row[j] for row in retained_a) for j in range(3)] for i in range(3)]
    deleted_row = fixture_a[deleted_index]
    expected_retained_gram = [[Fraction(int(i == j)) - deleted_row[i] * deleted_row[j] for j in range(3)] for i in range(3)]
    fixture_complement_square = fixture_b[deleted_index][0] ** 2
    fixture_lower_bound = Fraction(*magnetic_naimark.get("expected_fixture_retained_lower_bound", [0,1]))
    naimark_dimensions_close = naimark_ports - naimark_signal == naimark_complement == magnetic_naimark.get("deleted_port_count")
    if not naimark_dimensions_close or not magnetic_naimark.get("parseval_hypothesis_required") or magnetic_naimark.get("retained_lower_frame_bound") != "sigma_min(B_S)^2" or magnetic_naimark.get("retained_condition_number") != "1/sigma_min(B_S)" or not magnetic_naimark.get("injective_iff_complement_minor_invertible") or retained_gram != expected_retained_gram or fixture_complement_square != fixture_lower_bound or magnetic_naimark.get("expected_fixture_condition_number") != 2 or not magnetic_naimark.get("small_complement_reduction_is_exact"):
        errors.append("magnetic_naimark_deletion_duality_fixture_invalid")
    if magnetic_naimark.get("optimized_24_port_parseval_frame_source_authorized") or magnetic_naimark.get("claims_complement_reduction_constructs_optimized_frame") or magnetic_naimark.get("claims_full_frame_tightness_implies_deletion_tightness"):
        errors.append("magnetic_naimark_deletion_authority_laundered")
    volume_ports = int(magnetic_volume_budget.get("ambient_port_count", 0))
    volume_dimension = int(magnetic_volume_budget.get("complement_dimension", 0))
    volume_minor_count = comb(volume_ports, volume_dimension) if volume_ports >= volume_dimension >= 0 else 0
    average_squared_minor = Fraction(1, volume_minor_count) if volume_minor_count else None
    hadamard_squared_minors = [row[0] ** 2 for row in fixture_b]
    hadamard_cauchy_binet_sum = sum(hadamard_squared_minors)
    condition_lower_decimal = volume_minor_count ** (Fraction(1, 6)) if volume_minor_count else 0
    if volume_minor_count != magnetic_volume_budget.get("expected_minor_count") or magnetic_volume_budget.get("parseval_complement_gram_determinant") != 1 or magnetic_volume_budget.get("cauchy_binet_squared_minor_sum") != 1 or average_squared_minor != Fraction(*magnetic_volume_budget.get("expected_average_squared_minor", [0,1])) or average_squared_minor != Fraction(*magnetic_volume_budget.get("worst_squared_minor_upper_bound", [0,1])) or magnetic_volume_budget.get("worst_sigma_min_upper_bound") != "2024^(-1/6)" or magnetic_volume_budget.get("worst_condition_lower_bound") != "2024^(1/6)" or abs(float(condition_lower_decimal) - float(magnetic_volume_budget.get("worst_condition_lower_bound_decimal", 0))) > 1e-12 or hadamard_cauchy_binet_sum != 1 or hadamard_squared_minors != [Fraction(*value) for value in magnetic_volume_budget.get("exact_hadamard_fixture_squared_minors", [])]:
        errors.append("magnetic_robustness_volume_budget_fixture_invalid")
    if magnetic_volume_budget.get("equal_minor_energy_design_exists_source_authorized") or magnetic_volume_budget.get("claims_average_bound_is_attainable") or magnetic_volume_budget.get("claims_determinant_bound_classifies_conditioning"):
        errors.append("magnetic_robustness_volume_budget_authority_laundered")
    plucker_signed_sums = sorted(set(sum(signs) for signs in product([-1, 1], repeat=3)))
    plucker_zero_possible = 0 in plucker_signed_sums
    plucker_equal_volume_exists = plucker_zero_possible
    strict_bound_follows = not plucker_equal_volume_exists and magnetic_plucker.get("compact_parseval_frame_space") and magnetic_plucker.get("minimum_minor_objective_continuous")
    if magnetic_plucker.get("field") != "R" or magnetic_plucker.get("rank") != 3 or magnetic_plucker.get("minimum_row_count") != 5 or magnetic_plucker.get("relation") != "p123*p145-p124*p135+p125*p134=0" or magnetic_plucker.get("normalized_product_terms") != [-1, 1] or plucker_signed_sums != magnetic_plucker.get("expected_possible_signed_three_term_sums") or plucker_zero_possible != magnetic_plucker.get("zero_sum_possible") or plucker_equal_volume_exists != magnetic_plucker.get("equal_volume_real_frame_exists") or not strict_bound_follows or magnetic_plucker.get("strict_worst_condition_bound") != "kappa_worst>2024^(1/6)":
        errors.append("magnetic_plucker_equal_volume_obstruction_fixture_invalid")
    if magnetic_plucker.get("quantitative_strict_gap_computed") or magnetic_plucker.get("optimal_frame_constructed") or magnetic_plucker.get("claims_plucker_obstruction_supplies_gap_value"):
        errors.append("magnetic_plucker_obstruction_authority_laundered")
    quantitative_minor_count = int(magnetic_plucker_gap.get("minor_count", 0))
    quantitative_denominator = quantitative_minor_count + 1
    quantitative_minor_bound = Fraction(1, quantitative_denominator) if quantitative_denominator else None
    quantitative_condition_bound = quantitative_denominator ** (Fraction(1, 6)) if quantitative_denominator else 0
    if quantitative_minor_count != volume_minor_count or magnetic_plucker_gap.get("minimum_squared_minor_symbol") != "m" or magnetic_plucker_gap.get("three_term_product_lower_bound") != "m" or magnetic_plucker_gap.get("forced_large_product_lower_bound") != "2m" or magnetic_plucker_gap.get("forced_large_squared_minor_lower_bound") != "2m" or magnetic_plucker_gap.get("cauchy_binet_total") != 1 or magnetic_plucker_gap.get("derived_total_lower_bound") != "2025m" or quantitative_minor_bound != Fraction(*magnetic_plucker_gap.get("derived_minimum_squared_minor_upper_bound", [0,1])) or magnetic_plucker_gap.get("derived_worst_condition_lower_bound") != "2025^(1/6)" or abs(float(quantitative_condition_bound) - float(magnetic_plucker_gap.get("derived_worst_condition_lower_bound_decimal", 0))) > 1e-12 or not magnetic_plucker_gap.get("improves_average_bound") or not magnetic_plucker_gap.get("uses_one_local_five_row_relation"):
        errors.append("magnetic_plucker_quantitative_gap_fixture_invalid")
    if magnetic_plucker_gap.get("global_overlap_counting_applied") or magnetic_plucker_gap.get("bound_claimed_optimal") or magnetic_plucker_gap.get("optimized_frame_constructed"):
        errors.append("magnetic_plucker_quantitative_gap_overclaimed")
    cover_rows = int(magnetic_global_cover.get("row_count", 0))
    cover_relation_count, cover_total_incidences, cover_incident_minor_count, cover_max_degree = canonical_plucker_cover_counts(cover_rows)
    cover_minimum_witnesses = (cover_relation_count + cover_max_degree - 1) // cover_max_degree if cover_max_degree else 0
    cover_energy_denominator = volume_minor_count + cover_minimum_witnesses
    cover_minor_bound = Fraction(1, cover_energy_denominator) if cover_energy_denominator else None
    cover_condition_bound = cover_energy_denominator ** (Fraction(1, 6)) if cover_energy_denominator else 0
    if not magnetic_global_cover.get("canonical_relation_per_five_subset") or cover_relation_count != magnetic_global_cover.get("expected_relation_count") or magnetic_global_cover.get("minors_per_relation") != 6 or cover_total_incidences != magnetic_global_cover.get("expected_total_relation_minor_incidences") or cover_max_degree != magnetic_global_cover.get("expected_max_relations_witnessed_by_one_minor") or cover_minimum_witnesses != magnetic_global_cover.get("expected_minimum_distinct_large_minors") or magnetic_global_cover.get("large_minor_squared_lower_bound") != "2m" or magnetic_global_cover.get("expected_global_energy_lower_bound") != "2227m" or cover_minor_bound != Fraction(*magnetic_global_cover.get("derived_minimum_squared_minor_upper_bound", [0,1])) or magnetic_global_cover.get("derived_worst_condition_lower_bound") != "2227^(1/6)" or abs(float(cover_condition_bound) - float(magnetic_global_cover.get("derived_worst_condition_lower_bound_decimal", 0))) > 1e-12 or not magnetic_global_cover.get("cover_bound_is_exact_for_incidence_hypergraph"):
        errors.append("magnetic_global_plucker_cover_fixture_invalid")
    if magnetic_global_cover.get("simultaneous_plucker_feasibility_solved") or magnetic_global_cover.get("bound_claimed_optimal_for_frames") or magnetic_global_cover.get("optimized_frame_constructed"):
        errors.append("magnetic_global_plucker_cover_overclaimed")
    symmetric_rows = int(magnetic_symmetric_cover.get("row_count", 0))
    symmetric_five_sets = comb(symmetric_rows, 5) if symmetric_rows >= 5 else 0
    symmetric_relation_count = symmetric_five_sets * 5
    symmetric_containing_sets = comb(symmetric_rows - 3, 2) if symmetric_rows >= 5 else 0
    symmetric_minor_degree = symmetric_containing_sets * 3
    symmetric_witnesses = (symmetric_relation_count + symmetric_minor_degree - 1) // symmetric_minor_degree if symmetric_minor_degree else 0
    symmetric_energy_denominator = volume_minor_count + symmetric_witnesses
    symmetric_minor_bound = Fraction(1, symmetric_energy_denominator) if symmetric_energy_denominator else None
    symmetric_condition_bound = symmetric_energy_denominator ** (Fraction(1, 6)) if symmetric_energy_denominator else 0
    symmetric_incidence_left = symmetric_relation_count * int(magnetic_symmetric_cover.get("minors_per_relation", 0))
    symmetric_incidence_right = volume_minor_count * symmetric_minor_degree
    if symmetric_five_sets != magnetic_symmetric_cover.get("five_subset_count") or magnetic_symmetric_cover.get("pivot_relations_per_five_subset") != 5 or symmetric_relation_count != magnetic_symmetric_cover.get("expected_relation_count") or magnetic_symmetric_cover.get("minors_per_relation") != 6 or magnetic_symmetric_cover.get("minor_appearances_per_containing_five_subset") != 3 or symmetric_containing_sets != magnetic_symmetric_cover.get("five_subsets_containing_one_minor") or symmetric_minor_degree != magnetic_symmetric_cover.get("expected_uniform_minor_degree") or symmetric_witnesses != magnetic_symmetric_cover.get("expected_minimum_distinct_large_minors") or magnetic_symmetric_cover.get("large_minor_squared_lower_bound") != "2m" or magnetic_symmetric_cover.get("expected_global_energy_lower_bound") != "2362m" or symmetric_minor_bound != Fraction(*magnetic_symmetric_cover.get("derived_minimum_squared_minor_upper_bound", [0,1])) or magnetic_symmetric_cover.get("derived_worst_condition_lower_bound") != "2362^(1/6)" or abs(float(symmetric_condition_bound) - float(magnetic_symmetric_cover.get("derived_worst_condition_lower_bound_decimal", 0))) > 1e-12 or symmetric_incidence_left != symmetric_incidence_right or not magnetic_symmetric_cover.get("incidence_double_count_exact"):
        errors.append("magnetic_symmetrized_plucker_cover_fixture_invalid")
    if magnetic_symmetric_cover.get("cover_lower_bound_attainability_established") or magnetic_symmetric_cover.get("simultaneous_relation_witness_assignment_solved") or magnetic_symmetric_cover.get("bound_claimed_optimal_for_frames"):
        errors.append("magnetic_symmetrized_plucker_cover_overclaimed")
    energy_relation_count = int(magnetic_energy_gap.get("relation_count", 0))
    energy_minor_degree = int(magnetic_energy_gap.get("uniform_minor_degree", 0))
    energy_local_coefficient = 8
    energy_global_coefficient = energy_relation_count * energy_local_coefficient
    energy_minor_bound = Fraction(energy_minor_degree, energy_global_coefficient) if energy_global_coefficient else None
    energy_condition_bound = (1 / energy_minor_bound) ** (Fraction(1, 6)) if energy_minor_bound else 0
    if energy_relation_count != symmetric_relation_count or energy_minor_degree != symmetric_minor_degree or magnetic_energy_gap.get("local_product_law") != "w=u+v" or magnetic_energy_gap.get("pair_square_inequality") != "a^2+b^2>=2ab" or magnetic_energy_gap.get("product_lower_bounds") != "u>=m and v>=m" or magnetic_energy_gap.get("local_six_minor_energy_lower_bound") != "8m" or magnetic_energy_gap.get("global_counted_energy") != "630" or magnetic_energy_gap.get("global_relation_energy_lower_bound") != "1700160m" or energy_minor_bound != Fraction(*magnetic_energy_gap.get("derived_minimum_squared_minor_upper_bound", [0,1])) or magnetic_energy_gap.get("derived_worst_condition_lower_bound") != "(8096/3)^(1/6)" or abs(float(energy_condition_bound) - float(magnetic_energy_gap.get("derived_worst_condition_lower_bound_decimal", 0))) > 1e-12 or not magnetic_energy_gap.get("strictly_improves_cover_bound") or not magnetic_energy_gap.get("local_energy_bound_sharp"):
        errors.append("magnetic_plucker_energy_inequality_fixture_invalid")
    if magnetic_energy_gap.get("global_simultaneous_equality_feasibility_established") or magnetic_energy_gap.get("bound_claimed_optimal_for_frames"):
        errors.append("magnetic_plucker_energy_inequality_overclaimed")
    def qadd(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return x[0] + y[0], x[1] + y[1]
    def qneg(x: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return -x[0], -x[1]
    def qmul(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return x[0] * y[0] + x[1] * y[1], x[0] * y[1] + x[1] * y[0] + x[1] * y[1]
    one, phi = (Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))
    a, b, c, d, e, f = phi, phi, one, phi, phi, one
    golden_coordinates = [one,b,d,f,qneg(a),qneg(c),qneg(e),qadd(qmul(a,d),qneg(qmul(b,c))),qadd(qmul(a,f),qneg(qmul(b,e))),qadd(qmul(c,f),qneg(qmul(d,e)))]
    golden_expected = [one,phi,phi,one,qneg(phi),qneg(one),qneg(phi),one,qneg(one),qneg(phi)]
    golden_energy = (Fraction(0), Fraction(0))
    for coordinate in golden_coordinates:
        golden_energy = qadd(golden_energy, qmul(coordinate, coordinate))
    golden_energy_decimal = float(golden_energy[0]) + float(golden_energy[1]) * ((1 + 5 ** 0.5) / 2)
    golden_unit_count = sum(coordinate in (one, qneg(one)) for coordinate in golden_coordinates)
    golden_phi_count = sum(coordinate in (phi, qneg(phi)) for coordinate in golden_coordinates)
    if magnetic_golden.get("quadratic_field") != "Q(phi), phi^2=phi+1" or golden_coordinates != golden_expected or golden_unit_count != magnetic_golden.get("expected_unit_magnitude_count") or golden_phi_count != magnetic_golden.get("expected_phi_magnitude_count") or golden_energy != (Fraction(10), Fraction(5)) or magnetic_golden.get("expected_total_squared_energy") != "10+5phi" or abs(golden_energy_decimal - float(magnetic_golden.get("expected_total_squared_energy_decimal", 0))) > 1e-12 or not magnetic_golden.get("candidate_satisfies_all_plucker_relations_exactly"):
        errors.append("magnetic_five_row_golden_candidate_fixture_invalid")
    if magnetic_golden.get("candidate_alone_proves_local_minimum") or magnetic_golden.get("candidate_alone_proves_global_lower_bound") or magnetic_golden.get("claims_numerical_search_certifies_optimality"):
        errors.append("magnetic_five_row_golden_candidate_overclaimed")
    kkt_active_count = len(magnetic_golden_kkt.get("active_nonconstant_constraints", []))
    kkt_chart_dimension = int(magnetic_golden_kkt.get("expected_chart_dimension", 0))
    kkt_tangent_dimension = kkt_chart_dimension - kkt_active_count
    kkt_licq_minor = qmul(phi, phi)
    kkt_multiplier = (Fraction(4), Fraction(2))
    kkt_small_eigenvalue = Fraction(6)
    kkt_large_eigenvalue = 30 + 12 * (5 ** 0.5)
    kkt_positive = kkt_small_eigenvalue > 0 and kkt_large_eigenvalue > 0 and (float(kkt_multiplier[0]) + float(kkt_multiplier[1]) * ((1 + 5 ** 0.5) / 2)) > 0
    if magnetic_golden_kkt.get("sign_chamber") != "signed coordinates of golden candidate" or kkt_active_count != magnetic_golden_kkt.get("expected_active_constraint_count") or kkt_tangent_dimension != magnetic_golden_kkt.get("expected_critical_tangent_dimension") or kkt_licq_minor != (Fraction(1), Fraction(1)) or magnetic_golden_kkt.get("expected_licq_minor") != "phi^2" or kkt_multiplier != (Fraction(4), Fraction(2)) or magnetic_golden_kkt.get("expected_common_kkt_multiplier") != "5+sqrt5" or magnetic_golden_kkt.get("expected_restricted_hessian") != [["18+6sqrt5","12+6sqrt5"],["12+6sqrt5","18+6sqrt5"]] or magnetic_golden_kkt.get("expected_restricted_hessian_eigenvalues") != ["6","30+12sqrt5"] or not kkt_positive or not magnetic_golden_kkt.get("all_active_multipliers_strictly_positive") or not magnetic_golden_kkt.get("second_order_sufficient_condition") or not magnetic_golden_kkt.get("strict_local_minimum_in_sign_chamber"):
        errors.append("magnetic_golden_local_kkt_fixture_invalid")
    if magnetic_golden_kkt.get("global_minimum_proved") or magnetic_golden_kkt.get("other_sign_chambers_exhausted") or magnetic_golden_kkt.get("claims_local_kkt_implies_global_minimum"):
        errors.append("magnetic_golden_local_kkt_overclaimed")
    sign_operations = magnetic_sign_reduction.get("allowed_column_operations", [])
    sign_reduction_valid = magnetic_sign_reduction.get("field") == "R" and magnetic_sign_reduction.get("rank") == 2 and magnetic_sign_reduction.get("column_count") == 5 and magnetic_sign_reduction.get("uniform_configuration_from_minor_floor") and magnetic_sign_reduction.get("separating_functional_chosen_off_finite_annihilator_union") and sign_operations == ["sign reorientation", "permutation"] and not magnetic_sign_reduction.get("positive_rescaling_used") and not magnetic_sign_reduction.get("general_linear_rescaling_used") and magnetic_sign_reduction.get("all_reoriented_columns_in_one_open_halfplane") and magnetic_sign_reduction.get("slope_order_makes_all_ordered_minors_positive") and magnetic_sign_reduction.get("absolute_minor_multiset_preserved") and magnetic_sign_reduction.get("squared_energy_preserved") and magnetic_sign_reduction.get("all_realizable_uniform_sign_chambers_equivalent")
    if not sign_reduction_valid:
        errors.append("magnetic_rank_two_sign_chamber_reduction_fixture_invalid")
    if magnetic_sign_reduction.get("active_constraint_patterns_classified") or magnetic_sign_reduction.get("global_minimum_proved") or magnetic_sign_reduction.get("claims_sign_reduction_proves_golden_optimum"):
        errors.append("magnetic_rank_two_sign_chamber_reduction_overclaimed")
    coercive_variables = magnetic_coercivity.get("chart_variables", [])
    coercive_homogeneous = magnetic_coercivity.get("homogeneous_energy_degree") == magnetic_coercivity.get("homogeneous_minimum_squared_minor_degree") == 2
    coercive_chart_valid = magnetic_coercivity.get("minimum_minor_nonzero") and magnetic_coercivity.get("normalized_minimum_squared_minor") == 1 and magnetic_coercivity.get("minimum_minor_relabelled_to") == "p12" and magnetic_coercivity.get("chart_denominator_nonzero") and coercive_variables == ["a","b","c","d","e","f"]
    coercive_attainment = coercive_homogeneous and coercive_chart_valid and magnetic_coercivity.get("energy_contains_chart_coordinate_squares_with_unit_coefficients") and magnetic_coercivity.get("coercive_lower_bound") == "E>=1+a^2+b^2+c^2+d^2+e^2+f^2" and magnetic_coercivity.get("feasible_minor_inequalities_closed") and magnetic_coercivity.get("bounded_energy_sublevels_bounded") and magnetic_coercivity.get("normalized_feasible_sublevels_compact") and magnetic_coercivity.get("global_minimum_attained")
    if magnetic_coercivity.get("scale_invariant_objective") != "sum_I p_I^2 / min_I p_I^2" or not coercive_attainment or not magnetic_coercivity.get("normalization_is_proof_gauge_not_port_constructor"):
        errors.append("magnetic_five_row_coercive_normalization_fixture_invalid")
    if magnetic_coercivity.get("active_constraint_patterns_classified") or magnetic_coercivity.get("golden_global_minimum_proved") or magnetic_coercivity.get("claims_attainment_identifies_minimizer"):
        errors.append("magnetic_five_row_coercive_normalization_overclaimed")
    active_labels = magnetic_active_scout.get("nonconstant_constraint_labels", [])
    formal_active_patterns = 2 ** len(active_labels)
    golden_active_labels = magnetic_active_scout.get("golden_active_labels", [])
    golden_inactive_labels = magnetic_active_scout.get("golden_inactive_labels", [])
    scout_attempts = int(magnetic_active_scout.get("attempt_count", 0))
    scout_successes = int(magnetic_active_scout.get("successful_feasible_convergences", 0))
    scout_failures = int(magnetic_active_scout.get("failed_or_infeasible_attempts", 0))
    if active_labels != ["a","b","c","d","e","f","ad-bc","be-af","de-cf"] or formal_active_patterns != magnetic_active_scout.get("formal_active_pattern_count") or sorted(golden_active_labels + golden_inactive_labels) != sorted(active_labels) or golden_active_labels != ["c","f","ad-bc","be-af"] or magnetic_active_scout.get("golden_inactive_common_value") != "phi" or magnetic_active_scout.get("deterministic_seed") != 2707 or scout_attempts != scout_successes + scout_failures or scout_successes != 97 or magnetic_active_scout.get("distinct_successful_active_patterns") != 1 or magnetic_active_scout.get("distinct_successful_energy_levels") != 1 or magnetic_active_scout.get("successful_energy") != "10+5phi" or magnetic_active_scout.get("numerical_backend") != "scipy 1.18.1 SLSQP" or magnetic_active_scout.get("constraint_activity_tolerance") != 0.00002:
        errors.append("magnetic_five_row_active_set_scout_fixture_invalid")
    if magnetic_active_scout.get("numerical_scout_exhausts_active_patterns") or magnetic_active_scout.get("failed_runs_are_evidence_of_other_minima") or magnetic_active_scout.get("claims_scout_proves_global_minimum"):
        errors.append("magnetic_five_row_active_set_scout_overclaimed")
    cycle_solution = magnetic_cycle_face.get("positive_plucker_solution", {})
    cycle_factorization_valid = magnetic_cycle_face.get("derivative_factorization") == "4(t^2-t-1)(t^2(t-1)^2+t^2-t+1)/(t-1)^3"
    cycle_cofactor_positive = magnetic_cycle_face.get("positive_cofactor_on_interval") and magnetic_cycle_face.get("one_variable_interval") == "sqrt(2)<=t<=2"
    cycle_unique = cycle_factorization_valid and cycle_cofactor_positive and magnetic_cycle_face.get("unique_critical_point") == "t=phi" and magnetic_cycle_face.get("unique_face_minimum_energy") == "10+5phi"
    if magnetic_cycle_face.get("unit_minor_graph") != "C5" or magnetic_cycle_face.get("unit_cycle_edge_count") != 5 or magnetic_cycle_face.get("diagonal_variables") != ["x","y","z","u","v"] or cycle_solution != {"v":"yz-1","u":"(y+1)/(yz-1)","x":"(z+1)/(yz-1)"} or magnetic_cycle_face.get("feasible_product_interval") != "2<=p<=4" or not magnetic_cycle_face.get("energy_strictly_increasing_in_s_at_fixed_p") or magnetic_cycle_face.get("fixed_product_minimizer") != "y=z=sqrt(p)" or magnetic_cycle_face.get("diagonal_energy") != "2t^2+(t^2-1)^2+2/(t-1)^2" or not cycle_unique or not magnetic_cycle_face.get("golden_is_global_minimum_on_five_cycle_face"):
        errors.append("magnetic_golden_five_cycle_face_fixture_invalid")
    if magnetic_cycle_face.get("all_other_active_graphs_excluded") or magnetic_cycle_face.get("claims_face_minimum_is_global_minimum"):
        errors.append("magnetic_golden_five_cycle_face_overclaimed")
    graph_vertex_count = int(magnetic_graph_pruning.get("vertex_count", 0))
    graph_edges = list(combinations(range(graph_vertex_count), 2))
    def cyclic_between(left: int, right: int, point: int) -> bool:
        return (point - left) % graph_vertex_count < (right - left) % graph_vertex_count
    def edges_cross(first: tuple[int, int], second: tuple[int, int]) -> bool:
        a, b = first
        c, d = second
        return len({a,b,c,d}) == 4 and cyclic_between(a,b,c) != cyclic_between(a,b,d) and cyclic_between(c,d,a) != cyclic_between(c,d,b)
    crossing_pairs = [(first, second) for first, second in combinations(graph_edges, 2) if edges_cross(first, second)]
    def dihedral_graph_key(edge_set: set[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
        representatives = []
        for reflected in (False, True):
            for shift in range(graph_vertex_count):
                transformed = []
                for left, right in edge_set:
                    new_left = ((-left if reflected else left) + shift) % graph_vertex_count
                    new_right = ((-right if reflected else right) + shift) % graph_vertex_count
                    transformed.append(tuple(sorted((new_left, new_right))))
                representatives.append(tuple(sorted(transformed)))
        return min(representatives)
    admitted_graphs = []
    for mask in range(1 << len(graph_edges)):
        edge_set = {edge for index, edge in enumerate(graph_edges) if mask & (1 << index)}
        if any(first in edge_set and second in edge_set for first, second in crossing_pairs):
            continue
        if {vertex for edge in edge_set for vertex in edge} != set(range(graph_vertex_count)):
            continue
        admitted_graphs.append(edge_set)
    graph_count_by_size = {str(size): sum(len(graph) == size for graph in admitted_graphs) for size in range(3, 8)}
    graph_orbits = {dihedral_graph_key(graph) for graph in admitted_graphs}
    orbit_count_by_size = {str(size): sum(len(graph) == size for graph in graph_orbits) for size in range(3, 8)}
    if graph_vertex_count != 5 or len(graph_edges) != magnetic_graph_pruning.get("complete_graph_edge_count") or 1 << len(graph_edges) != magnetic_graph_pruning.get("labeled_graph_count") or len(crossing_pairs) != magnetic_graph_pruning.get("positive_plucker_crossing_pair_count") or not magnetic_graph_pruning.get("crossing_unit_edges_forbidden") or not magnetic_graph_pruning.get("column_scaling_stationarity_forbids_isolated_vertices") or len(admitted_graphs) != magnetic_graph_pruning.get("expected_noncrossing_vertex_cover_graph_count") or graph_count_by_size != magnetic_graph_pruning.get("expected_labeled_count_by_edge_count") or magnetic_graph_pruning.get("symmetry_group") != "D5" or len(graph_orbits) != magnetic_graph_pruning.get("expected_dihedral_orbit_count") or orbit_count_by_size != magnetic_graph_pruning.get("expected_orbit_count_by_edge_count") or not magnetic_graph_pruning.get("golden_cycle_is_one_five_edge_orbit"):
        errors.append("magnetic_unit_minor_graph_pruning_fixture_invalid")
    if magnetic_graph_pruning.get("all_23_non_golden_orbits_excluded") or magnetic_graph_pruning.get("claims_graph_pruning_proves_global_minimum"):
        errors.append("magnetic_unit_minor_graph_pruning_overclaimed")
    minimal_graphs = [
        graph for graph in admitted_graphs
        if all({vertex for edge in graph - {removed} for vertex in edge} != set(range(graph_vertex_count)) for removed in graph)
    ]
    minimal_graph_count_by_size = {str(size): sum(len(graph) == size for graph in minimal_graphs) for size in (3, 4)}
    minimal_graph_orbits = sorted({dihedral_graph_key(graph) for graph in minimal_graphs}, key=lambda graph: (len(graph), graph))
    expected_minimal_representatives = [tuple(tuple(edge) for edge in graph) for graph in magnetic_minimal_faces.get("expected_minimal_orbit_representatives", [])]
    every_graph_contains_minimal = all(any(minimal <= graph for minimal in minimal_graphs) for graph in admitted_graphs)
    if magnetic_minimal_faces.get("admitted_graph_order") != "edge inclusion" or len(minimal_graphs) != magnetic_minimal_faces.get("expected_inclusion_minimal_labeled_graph_count") or minimal_graph_count_by_size != magnetic_minimal_faces.get("expected_minimal_labeled_count_by_edge_count") or len(minimal_graph_orbits) != magnetic_minimal_faces.get("expected_inclusion_minimal_dihedral_orbit_count") or minimal_graph_orbits != expected_minimal_representatives or magnetic_minimal_faces.get("minimal_orbit_types") != ["adjacent-wedge plus disjoint edge","boundary-wedge plus separated edge","four-edge star"] or not every_graph_contains_minimal or not magnetic_minimal_faces.get("every_admitted_graph_contains_minimal_graph") or not magnetic_minimal_faces.get("adding_unit_edges_shrinks_feasible_face") or not magnetic_minimal_faces.get("face_minimum_monotone_under_edge_inclusion"):
        errors.append("magnetic_minimal_unit_graph_face_reduction_fixture_invalid")
    if magnetic_minimal_faces.get("three_base_face_lower_bounds_proved") or magnetic_minimal_faces.get("claims_combinatorial_reduction_proves_global_minimum"):
        errors.append("magnetic_minimal_unit_graph_face_reduction_overclaimed")
    adjacent_wedge_energy = 16 + 4 * (2 ** 0.5)
    golden_energy_value = 10 + 5 * ((1 + 5 ** 0.5) / 2)
    two_face_separation = magnetic_two_faces.get("star_exact_minimum_energy") == 24 and adjacent_wedge_energy > golden_energy_value and 24 > golden_energy_value
    if magnetic_two_faces.get("star_active_coordinates") != ["p12","p13","p14","p15"] or magnetic_two_faces.get("star_remaining_chain") != "D>=1, F-D>=1, G-F>=1" or magnetic_two_faces.get("star_exact_minimizer") != ["D=1","F=2","G=3"] or magnetic_two_faces.get("adjacent_wedge_active_coordinates") != ["p12","p13","p45"] or magnetic_two_faces.get("adjacent_wedge_plucker_substitution") != ["F=BD+x","G=CD+y","By-Cx=1"] or magnetic_two_faces.get("adjacent_wedge_lower_bound_saturations") != ["D=1","C=1","x=1"] or magnetic_two_faces.get("adjacent_wedge_product_floor") != "By>=2" or magnetic_two_faces.get("adjacent_wedge_exact_minimizer") != ["B=sqrt2","y=sqrt2"] or magnetic_two_faces.get("adjacent_wedge_exact_minimum_energy") != "16+4sqrt2" or abs(adjacent_wedge_energy - float(magnetic_two_faces.get("adjacent_wedge_exact_minimum_energy_decimal", 0))) > 1e-12 or not two_face_separation or not magnetic_two_faces.get("both_bounds_strictly_above_golden"):
        errors.append("magnetic_two_base_face_exact_bounds_fixture_invalid")
    if magnetic_two_faces.get("separated_wedge_bound_proved") or magnetic_two_faces.get("all_three_base_faces_proved") or magnetic_two_faces.get("claims_two_faces_finish_global_theorem"):
        errors.append("magnetic_two_base_face_exact_bounds_overclaimed")
    global_five_subset_count = comb(24, 5)
    global_minor_appearances = comb(21, 2)
    global_effective_denominator = 1012 * (2 + ((1 + 5 ** 0.5) / 2))
    global_minor_upper_bound = 1 / global_effective_denominator
    global_condition_lower_bound = global_effective_denominator ** (1 / 6)
    if magnetic_global_golden.get("separated_wedge_active_coordinates") != ["p12","p15","p34"] or magnetic_global_golden.get("separated_wedge_variables_relation") != "By=1+Az" or magnetic_global_golden.get("D_descent_boundaries") != ["D=1","F=1","G=1"] or not magnetic_global_golden.get("exceptional_D_boundaries_contain_adjacent_wedge_face") or magnetic_global_golden.get("D_equals_one_z_descent_boundaries") != ["z=1","y=1","G=1"] or not magnetic_global_golden.get("z_equals_one_boundary_is_five_cycle_face") or not magnetic_global_golden.get("other_z_descent_boundaries_contain_adjacent_wedge_face") or magnetic_global_golden.get("separated_wedge_exact_minimum_energy") != "10+5phi" or not magnetic_global_golden.get("all_three_base_face_bounds_proved") or magnetic_global_golden.get("global_five_row_energy_inequality") != "sum_10 p_I^2 >= (10+5phi)m" or magnetic_global_golden.get("equality_packet") != "five unit minors and five phi minors on C5" or global_five_subset_count != magnetic_global_golden.get("five_subset_count") or global_minor_appearances != magnetic_global_golden.get("global_minor_appearances_in_five_subsets") or magnetic_global_golden.get("global_cauchy_binet_energy") != 1 or magnetic_global_golden.get("derived_global_minimum_squared_minor_upper_bound") != "1/(1012(2+phi))" or abs(global_minor_upper_bound - float(magnetic_global_golden.get("derived_global_minimum_squared_minor_upper_bound_decimal", 0))) > 1e-15 or magnetic_global_golden.get("derived_worst_condition_lower_bound") != "(1012(2+phi))^(1/6)" or abs(global_condition_lower_bound - float(magnetic_global_golden.get("derived_worst_condition_lower_bound_decimal", 0))) > 1e-12:
        errors.append("magnetic_global_golden_five_row_theorem_fixture_invalid")
    if magnetic_global_golden.get("global_bound_claimed_optimal_for_24_row_frames") or magnetic_global_golden.get("optimized_24_row_frame_constructed"):
        errors.append("magnetic_global_golden_five_row_theorem_overclaimed")
    inclusion_gram_eigenvalues = [comb(24 - 3 - index, 5 - 3) * comb(5 - index, 3 - index) for index in range(4)]
    inclusion_gram_multiplicities = [1] + [comb(24, index) - comb(24, index - 1) for index in range(1, 4)]
    inclusion_full_rank = all(value > 0 for value in inclusion_gram_eigenvalues) and sum(inclusion_gram_multiplicities) == comb(24, 3)
    equality_real_constant = Fraction(5, comb(5, 3))
    equality_impossible = inclusion_full_rank and equality_real_constant == Fraction(1, 2)
    if magnetic_global_equality.get("triple_count") != comb(24, 3) or magnetic_global_equality.get("five_subset_count") != comb(24, 5) or magnetic_global_equality.get("equality_requires_floor_triples_per_five_set") != 5 or magnetic_global_equality.get("floor_indicator_type") != "0/1 function on 3-subsets" or magnetic_global_equality.get("inclusion_map") != "W_3,5 from triple functions to five-set sums" or inclusion_gram_eigenvalues != magnetic_global_equality.get("gram_eigenvalues") or inclusion_gram_multiplicities != magnetic_global_equality.get("gram_eigenvalue_multiplicities") or not inclusion_full_rank or not magnetic_global_equality.get("all_gram_eigenvalues_positive") or not magnetic_global_equality.get("inclusion_map_full_column_rank") or magnetic_global_equality.get("unique_real_solution_to_constant_five_sum") != "indicator identically 1/2" or not magnetic_global_equality.get("solution_is_not_zero_one") or magnetic_global_equality.get("global_equality_packet_exists") or magnetic_global_equality.get("strict_global_condition_bound") != ">(1012(2+phi))^(1/6)":
        errors.append("magnetic_global_golden_equality_obstruction_fixture_invalid")
    if magnetic_global_equality.get("quantitative_strict_gap_computed") or magnetic_global_equality.get("optimal_24_row_frame_constructed") or magnetic_global_equality.get("claims_rank_obstruction_supplies_gap_value"):
        errors.append("magnetic_global_golden_equality_obstruction_overclaimed")

    sequence_witnesses = {}
    for witness in theta["sequential_hostiles"]:
        valid = witness["quotient_norm_limit"] == "0" and witness["required_distinction_limit"] != "0"
        sequence_witnesses[witness["witness_id"]] = {
            "rejects_continuous_descent": valid,
            "code": "required_distinction_not_continuous_in_quotient_topology" if valid else None,
        }
        if not valid:
            errors.append("invalid_sequential_hostile:" + witness["witness_id"])

    return {
        "schema": "marici.distinction-preserving-completion-result.v1",
        "passed": not errors,
        "errors": errors,
        "theorem": {
            "algebraic_necessary": "R factors through Q implies ker(Q) subseteq ker(R)",
            "algebraic_sufficient_scope": "kernel inclusion is sufficient when Q is surjective, or after replacing its codomain by im(Q) / the canonical quotient",
            "topological_necessary": "Q(v_n)->0 implies R(v_n)->0",
            "uniform_continuity": "R_N^*R_N <= C^2 Q_N for one cutoff-independent C",
        },
        "finite_fixtures": fixtures,
        "nonsurjective_factorization_hostile": nonsurjective_hostile,
        "theta": {
            "L_factorization": ["L_finite_incidence", "L_typed_completion", "L_scalar_readout"],
            "finite_incidence_authorized": True,
            "completion_classes": theta["completion_classes"],
            "completed_scalar_readout_authorized": False,
            "joint_global_completion_authorized": True,
            "operator_lift_authorized": False,
            "trace_correspondence": {
                "bounded_additive_L2_trace": False,
                "source_test_space_trace": True,
                "reason": "idelic locus is additive-Haar null",
            },
            "seam_line_system": {
                "finite_cocycle_exact": composite is not None,
                "composite_transition": [str(x) for x in composite] if composite else None,
                "all_bonding_maps_unitary": seam_unitary,
                "direct_limit_line_exists": seam_unitary,
                "global_scalar_trivialization_required": False,
                "line_itself_can_vanish": False,
                "off_seam_unitary_in_seam_metric": off_seam_unitary,
                "transported_off_seam_metrics": [str(x) for x in transported_metrics],
                "finite_metric_transport_isometric": all(transported_metrics[i + 1] * norm_squared(off_seam) == transported_metrics[i] for i in range(len(transported_metrics) - 1)),
                "uniformly_equivalent_to_fixed_metric": len(set(transported_metrics)) == 1,
                "raw_reference_tensor_implementable_at_t_zero": raw_tensor.get("t_zero_implementable"),
                "raw_reference_tensor_implementable_at_fixed_nonzero_t": raw_tensor.get("fixed_nonzero_t_implementable"),
            },
            "renormalization_trace_gate": {
                "constructors_separate": True,
                "metric_reference_source_authorized": metric_constructor.get("source_authorized"),
                "rigged_trace_source_test_space_authorized": trace_constructor.get("source_test_space_authorized"),
                "rigged_trace_completed_closability_authorized": trace_constructor.get("completed_closability_authorized"),
                "required_order": repair.get("required_order"),
                "normalized_transition": str(normalized_transition),
                "pairing_compatible_before": pairing_compatible_before,
                "contragredient_pairing_compatible_after": pairing_compatible_after,
                "scalar_only_pairing_compatible_after": hostile_pairing_compatible,
                "pairing_metric_invariant_values": [str(value) for value in pairing_metric_ratios],
                "pairing_metric_invariant_constant": len(set(pairing_metric_ratios)) == 1,
                "pairing_induces_positive_metric_off_divisor": pairing_induces_positive_metric,
                "pairing_induces_metric_on_zero_divisor": zero_pairing_induces_metric,
                "pairing_metric_scope": "complement_of_pairing_zero_divisor",
                "zero_divisor_disposition": "metric_chart_boundary_not_line_failure",
                "target_scalar_metric_source_authorized": induced.get("target_scalar_metric_source_authorized"),
                "composite_authorized": bool(metric_constructor.get("source_authorized") and trace_constructor.get("completed_closability_authorized") and pairing_compatible_after),
            },
            "jet_atlas": {
                "source_derivative_family_authorized": jet_atlas.get("source_derivative_family_authorized"),
                "target_jet_metric_source_authorized": jet_atlas.get("target_jet_metric_source_authorized"),
                "finite_executable_depth": jet_atlas.get("finite_executable_depth"),
                "fixtures": jet_fixtures,
                "finite_atlas_globally_complete": all(item["covered_by_finite_executable_atlas"] for item in jet_fixtures.values()),
                "infinite_analytic_jet_jointly_faithful_condition": "section analytic and not identically zero",
                "infinite_jet_tower_is_finite_executable_capability": False,
                "adaptive_constructor_predeclared": bool(adaptive.get("family")),
                "adaptive_selection_rule": adaptive.get("selection_rule"),
                "adaptive_selection_is_logical_not_temporal": adaptive.get("selection_kind") == "logical dependent sum, not chronological execution",
                "adaptive_pointwise_termination": bool(jet_atlas.get("section_nonidentity_certificate")),
                "adaptive_uniform_depth_bound": adaptive.get("claims_uniform_bound"),
                "identically_zero_germ_rejected": jet_fixtures.get("identically_zero_germ", {}).get("first_nonzero_order") is None,
                "multiplicity_stratum_object": "ord_s(section)=least m with j_m nonzero",
            },
            "reflection_jet_gate": {
                "scalar_functional_equation_authorized": reflection.get("scalar_functional_equation_authorized"),
                "fixture_kind": reflection.get("fixture_kind"),
                "claims_actual_Xi_center_zero": False,
                "off_fixed_multiplicity_preserved": len(paired_multiplicity) == 2 and paired_multiplicity[0] == paired_multiplicity[1],
                "fixed_locus_odd_jets_vanish": scalar_parity_valid,
                "fixed_locus_first_nonzero_order": fixed_first,
                "fixed_locus_zero_multiplicity_even": fixed_first is not None and fixed_first % 2 == 0,
                "boundary_line_comparison_cell_authorized": reflection.get("boundary_line_comparison_cell_authorized"),
                "scalar_jet_to_line_lift_authorized": reflection.get("scalar_jet_to_line_lift_authorized"),
                "scalar_parity_transports_to_boundary_line": bool(reflection.get("boundary_line_comparison_cell_authorized") and reflection.get("scalar_jet_to_line_lift_authorized") and scalar_parity_valid),
                "unresolved_line_choice": reflection.get("boundary_line_comparison_choice"),
            },
            "reflection_line_metric_gate": {
                "coherent_candidate_count": len(coherent_candidates),
                "positive_candidate_count": len(positive_candidates),
                "negative_coherent_candidate_count": len(negative_coherent),
                "reflection_coherence_implies_positivity": not negative_coherent,
                "source_admitted_candidate_count": len(source_admitted_candidates),
                "source_hilbert_packet_rejects_negative_form": bool(negative_coherent) and all(not candidate.get("admitted_by_hilbert_metric") for candidate in negative_coherent),
                "required_constructors": line_metric.get("required_constructors"),
                "finite_cutoff_hilbert_metric_source_authorized": line_metric.get("finite_cutoff_hilbert_metric_source_authorized"),
                "seam_positive_orientation_source_authorized": line_metric.get("seam_positive_orientation_source_authorized"),
                "duality_cell_source_authorized": line_metric.get("duality_cell_source_authorized"),
                "real_structure_source_authorized": line_metric.get("real_structure_source_authorized"),
                "metric_construction_authorized": bool(line_metric.get("finite_cutoff_hilbert_metric_source_authorized") and line_metric.get("seam_positive_orientation_source_authorized")),
                "reflection_compatible_metric_authorized": bool(line_metric.get("seam_positive_orientation_source_authorized") and line_metric.get("duality_cell_source_authorized") and line_metric.get("real_structure_source_authorized")),
                "residual": "zero_on_seam",
            },
            "direct_limit_reflection_cell": {
                "seam_transition_norm_squared": str(seam_norm),
                "dual_transition": [str(value) for value in seam_inverse],
                "conjugate_transition": [str(value) for value in seam_conjugate],
                "dual_conjugate_residual": [str(value) for value in dual_conjugate_residual],
                "comparison_cell_natural_on_seam": not any(dual_conjugate_residual),
                "real_structure_phase_norms_squared": [str(value) for value in real_squares],
                "real_structure_squares_to_identity": all(value == 1 for value in real_squares),
                "global_phase_disposition": reflection_cell.get("global_phase_disposition"),
                "off_seam_fixed_metric_dual_conjugate_residual": [str(value) for value in off_residual],
                "off_seam_fixed_metric_cell_exists": not any(off_residual),
            },
            "off_seam_uniform_comparison_gate": {
                "source_formula": off_uniform.get("source_formula"),
                "left_product_limit": off_uniform.get("left_product_limit"),
                "right_product_limit": off_uniform.get("right_product_limit"),
                "reflected_sector_limits_reciprocal": off_uniform.get("left_product_limit") == "0" and off_uniform.get("right_product_limit") == "infinity",
                "uniform_fixed_metric_comparison": off_uniform.get("uniform_fixed_metric_comparison"),
                "global_uniform_comparison_falsified_by_real_slice": off_uniform.get("uniform_fixed_metric_comparison") is False,
                "synthetic_left_products": [str(value) for value in left_products],
                "synthetic_right_products": [str(value) for value in right_products],
                "synthetic_left_metrics": [str(value) for value in left_metrics],
                "synthetic_right_metrics": [str(value) for value in right_metrics],
                "reciprocal_metric_product_invariant": all(value == 1 for value in reciprocal_metric_products),
                "synthetic_fixture_kind": synthetic.get("fixture_kind"),
                "remaining_options": ["cutoff-dependent transported metrics", "source-derived renormalized reference representation", "relative/projective ambient object"],
            },
            "relative_ambient_trace_gate": {
                "ambient_kind": relative_trace.get("ambient_kind"),
                "relative_line_system_exists": relative_trace.get("ambient_kind") == "parameterized_isometric_direct_system_of_Hilbert_lines",
                "fixed_scalar_trivialization_required": relative_trace.get("fixed_scalar_trivialization_required"),
                "finite_trace_compatibility_required": relative_trace.get("finite_trace_compatibility_required"),
                "projective_transport_repairs_closability": relative_trace.get("projective_transport_claims_closability"),
                "source_graph_domination_authorized": relative_trace.get("source_graph_domination_authorized"),
                "source_graph_identity": relative_trace.get("source_graph_identity"),
                "source_graph_scope": relative_trace.get("source_graph_scope"),
                "native_endpoint_trace_closable": bool(relative_trace.get("source_graph_domination_authorized") and trace_constructor.get("completed_closability_authorized")),
                "full_doubled_green_identity_authorized": relative_trace.get("claims_full_doubled_green_identity"),
                "nonclosable_witness_input_norms": [str(value) for value in witness_norms],
                "nonclosable_witness_outputs": [str(value) for value in witness_outputs],
                "nonclosable_witness_detected": nonclosable_detected,
                "theorem": "isometric target transport preserves, rather than repairs, the zero-sequence criterion for closability",
                "first_missing_constructor": "completed doubled Green-current comparison with no undeclared cross-sector residual",
            },
            "weighted_source_rigging_gate": {
                "criterion": "sup_N ||T_N||_(H_w)^2 = sum_n |c_n|^2/w_n < infinity",
                "power_family_classification": weighted_classification,
                "critical_power": 2 * alpha + 1,
                "strict_threshold": "beta > 2 alpha + 1",
                "integer_minimum_beta_conditional_on_integer_power_grammar": 2 * alpha + 2,
                "integer_power_grammar_authorized": weighted_rigging.get("integer_power_grammar_authorized"),
                "source_authorized_beta": weighted_rigging.get("source_authorized_beta"),
                "mathematically_sufficient_candidate_exists": any(item["uniformly_bounded"] for item in weighted_classification.values()),
                "source_authorized_candidate_exists": weighted_rigging.get("source_authorized_beta") is not None,
                "trace_graph_norm_source_authorized": weighted_rigging.get("trace_graph_norm_source_authorized"),
                "circular_graph_norm_rejected": weighted_rigging.get("trace_graph_norm_is_circular_without_independent_constructor") and not weighted_rigging.get("trace_graph_norm_source_authorized"),
                "explanation": "the target-line problem reduces to membership of the coefficient sequence in the weighted source dual; choosing that dual remains source data",
            },
            "pro_gram_endpoint_gate": {
                "continuity_criterion": pro_gram.get("continuity_criterion"),
                "finite_packet_separation": coordinate_fixture.get("expected_finite_packet_separation"),
                "finite_observation_indices": observed_indices,
                "escaping_witness_index": escaping_index,
                "escaping_witness_observation_values": [str(value) for value in escaping_seminorm_values],
                "escaping_witness_endpoint_value": str(escaping_endpoint_value),
                "endpoint_continuous_in_bare_coordinate_pro_gram": not endpoint_not_finitely_dominated,
                "endpoint_port_source_identified": pro_gram.get("endpoint_port_source_identified"),
                "endpoint_port_may_be_retained_before_completion": bool(pro_gram.get("endpoint_port_source_identified") and pro_gram.get("augmentation_must_precede_completion")),
                "completed_green_incidence_authorized": pro_gram.get("completed_green_incidence_authorized"),
                "endpoint_normalization_authorized": pro_gram.get("endpoint_normalization_authorized"),
                "augmented_completion_fully_authorized": bool(pro_gram.get("endpoint_port_source_identified") and pro_gram.get("completed_green_incidence_authorized") and pro_gram.get("endpoint_normalization_authorized")),
                "theorem": "finite-packet Hausdorff faithfulness does not imply continuity of a global endpoint functional; continuity requires finite seminorm domination",
            },
            "endpoint_orbit_completion_gate": {
                "source_monoid_authorized": endpoint_orbit.get("source_monoid_authorized"),
                "endpoint_source_authorized": endpoint_orbit.get("endpoint_source_authorized"),
                "augmented_family": endpoint_orbit.get("augmented_family"),
                "constructor_reindexing_law": endpoint_orbit.get("generator_law"),
                "all_source_constructors_continuous_by_reindexing": endpoint_orbit.get("generator_law") == "ell_C(Ac)=ell_(CA)(c)",
                "single_endpoint_port_is_constructor_stable": not single_port_failure,
                "single_port_hostile_endpoint_before": [str(value) for value in endpoint_before],
                "single_port_hostile_endpoint_after_constructor": [str(value) for value in endpoint_after],
                "minimal_stable_augmentation": "all q_C and all ell_C for C in the source monoid",
                "universal_property": "weakest locally convex topology making every U after C and every L after C continuous",
                "completion_realization": "closure of the diagonal evaluation map into product_C(H_C x scalar_C)",
                "finite_endpoint_family_sufficient": endpoint_orbit.get("claims_finite_endpoint_family_sufficient"),
                "completed_green_identity_authorized": endpoint_orbit.get("claims_completed_green_identity"),
                "theorem": "one source endpoint port closes under constructors only after adjoining its full source-monoid orbit",
            },
            "endpoint_observability_gate": {
                "criterion": observability.get("criterion"),
                "fixtures": observability_fixtures,
                "finite_rank_equivalent_data": ["finite endpoint presentation", "finite linear recurrence among L after constructor words", "finite-dimensional cyclic dual module"],
                "backward_shift_rank_unbounded_in_fixture_family": observability_fixtures.get("backward_shift_growth", {}).get("ranks") == observability.get("fixtures", [{}, {}])[1].get("expected_ranks"),
                "actual_theta_orbit_finite_rank_authorized": observability.get("actual_theta_orbit_finite_rank_authorized"),
                "actual_theta_orbit_infinite_rank_authorized": observability.get("actual_theta_orbit_infinite_rank_authorized"),
                "theta_infinite_rank_premises": theta_rank_premises,
                "finite_endpoint_packet_stable_under_full_valuation_algebra": not observability.get("actual_theta_orbit_infinite_rank_authorized"),
                "theorem_theta": "valuation separation plus nonzero theta endpoint atoms gives arbitrarily large diagonal endpoint-observability minors",
            },
            "doubled_green_residual_gate": {
                "exact_identity": doubled_green.get("exact_identity"),
                "forcing_difference": doubled_green.get("forcing_difference"),
                "obstruction_object": "class of 2F in bulk forcing densities modulo derivatives of source-authorized boundary currents",
                "direct_dual_forcing_relation_source_derived": doubled_green.get("direct_dual_forcing_relation_source_derived"),
                "complete_boundary_derivative_authorized": doubled_green.get("complete_boundary_derivative_authorized"),
                "total_boundary_flux_vanishing_authorized": doubled_green.get("total_boundary_flux_vanishing_authorized"),
                "current_inventory": inventory,
                "cokernel_fixture_current_rank": current_rank,
                "cokernel_fixture_augmented_rank": augmented_rank,
                "cokernel_fixture_residual_in_authorized_image": residual_in_image,
                "cokernel_fixture_scalar_sum_zero": cokernel_fixture.get("scalar_sum_zero"),
                "cokernel_fixture_kind": cokernel_fixture.get("fixture_kind"),
                "scalar_cancellation_implies_typed_boundary_derivative": cokernel_fixture.get("scalar_sum_zero") and residual_in_image,
                "conditional_critical_line_implication": bool(doubled_green.get("complete_boundary_derivative_authorized") and doubled_green.get("total_boundary_flux_vanishing_authorized") and doubled_green.get("nonzero_completed_tail_state_authorized")),
                "first_missing_constructor": "source-derived comparison f_- versus Fourier-Tate transform of f_+, followed by P,Q,connected-tail,archimedean incidence into one boundary-current complex",
            },
            "indexed_endpoint_capability_gate": {
                "orbit_is_cyclic_module": indexed_endpoint.get("module_generator_count") == 1,
                "module_generator": indexed_endpoint.get("orbit_module_generator"),
                "static_observation_rank": indexed_endpoint.get("static_observation_rank"),
                "indexed_evaluator": indexed_endpoint.get("indexed_evaluator"),
                "finite_interface_schema": True,
                "finite_dimensional_observation_fiber": indexed_endpoint.get("claims_finite_dimensional_readout"),
                "finite_packet_evaluator_source_authorized": indexed_endpoint.get("finite_packet_evaluator_source_authorized"),
                "pointwise_completed_evaluation_authorized": indexed_endpoint.get("each_fixed_C_extends_continuously_in_orbit_topology"),
                "uniform_joint_bound_over_constructor_family_authorized": indexed_endpoint.get("uniform_joint_bound_over_all_C_authorized"),
                "constructor_index_kind": indexed_endpoint.get("constructor_index_kind"),
                "bounded_executable_capability": indexed_endpoint.get("claims_bounded_constructor_cost"),
                "theorem": "one cyclic generator can present an infinite-rank observation module only as an indexed higher-order capability, not as a finite static readout",
            },
            "constructor_normal_form_gate": {
                "relations": constructor_normal.get("relations"),
                "normal_form": constructor_normal.get("normal_form"),
                "fixtures": normal_form_fixtures,
                "finite_packet_joint_continuity_authorized": constructor_normal.get("finite_packet_joint_continuity_authorized"),
                "completed_joint_strong_continuity_authorized": constructor_normal.get("completed_joint_strong_continuity_authorized"),
                "index_space_compact": constructor_normal.get("index_space_compact"),
                "normalized_index_type": "finite valuation cylinder times real Mellin character, plus zero",
                "theorem": "commuting diagonal source constructors compress every finite word to a valuation-cylinder/Mellin normal form",
            },
            "mellin_saturated_completion_gate": {
                "saturation_seminorms": mellin_saturation.get("saturation_seminorms"),
                "compact_parameter_sets": mellin_saturation.get("compact_parameter_sets"),
                "finite_packet_suprema_finite": mellin_saturation.get("finite_packet_suprema_finite_by_exponential_polynomial_continuity"),
                "saturated_completion_strong_mellin_action": mellin_saturation.get("saturated_completion_strong_action_authorized"),
                "same_as_pointwise_pro_gram_claimed": mellin_saturation.get("claims_same_topology_as_pointwise_pro_gram"),
                "uniform_global_parameter_bound_claimed": mellin_saturation.get("claims_uniform_global_t_bound"),
                "green_identity_extension_claimed": mellin_saturation.get("claims_green_identity_extension"),
                "parameter_kind": mellin_saturation.get("parameter_kind"),
                "finite_fixture_value_at_zero": str(value_at_zero),
                "finite_fixture_first_frequency_moment": str(first_frequency_moment),
                "universal_property": "weakest refinement of the endpoint-orbit topology making the Mellin action locally equicontinuous on compact parameter sets",
                "theorem": "compact-uniform saturation extends the source Mellin group strongly to its own completion, without identifying that completion with the pointwise pro-Gram completion",
            },
            "relative_detector_poisson_clark_gate": {
                "normalized_fock_state_threshold": detector_clark.get("normalized_fock_state_threshold"),
                "raw_euler_detector_threshold": detector_clark.get("raw_euler_detector_threshold"),
                "common_mellin_hilbert_level_iff": detector_clark.get("common_mellin_hilbert_level_iff"),
                "finite_fock_detector_nonzero": detector_clark.get("finite_fock_detector_nonzero"),
                "relative_heat_detector_constructed": detector_clark.get("relative_heat_detector_constructed"),
                "relative_detector_value": detector_clark.get("relative_detector_value"),
                "regulator_universal": detector_clark.get("regulator_universal"),
                "finite_counterterms_authorized": detector_clark.get("finite_counterterms_authorized"),
                "finite_part_positive": detector_clark.get("finite_part_positive"),
                "finite_part_multiplicative": detector_clark.get("finite_part_multiplicative"),
                "boundary_quotient_cone_pointed": detector_clark.get("boundary_quotient_cone_pointed"),
                "finite_part_square_hostile_value": str(finite_part_value),
                "finite_part_square_hostile_pointwise_nonnegative": finite_part_hostile.get("pointwise_nonnegative"),
                "theta_germ_requires_infinite_shift": not detector_clark.get("theta_germ_finite_dimensional_realization") and detector_clark.get("theta_germ_shift_realization"),
                "clark_shift_graph_equivalence": detector_clark.get("clark_shift_graph_equivalence"),
                "clark_constants_at_a_half": [str(Fraction(*value)) for value in detector_clark.get("clark_constants_at_a_half", [])],
                "four_channel_poisson_incidence_supplied": detector_clark.get("four_channel_poisson_incidence_supplied"),
                "common_finite_poisson_clark_matrix_supplied": detector_clark.get("common_finite_poisson_clark_matrix_supplied"),
                "actual_theta_generalized_eigenvalue_interval": "undefined" if not detector_clark.get("common_finite_poisson_clark_matrix_supplied") else "requires computation",
                "uniform_generalized_eigenvalue_bounds_proved": detector_clark.get("uniform_generalized_eigenvalue_bounds_proved"),
                "determinant_kernel_bridge_supplied": detector_clark.get("determinant_kernel_bridge_supplied"),
                "relative_detector_nonvanishing_proved": detector_clark.get("relative_detector_nonvanishing_proved"),
                "first_missing_constructor": "typed finite Poisson/Green matrix E_X on the Clark shift module with residual blocks and cutoff covariance",
            },
            "poisson_matrix_lift_gate": {
                "scalar_four_channel_incidence_authorized": poisson_lift.get("scalar_four_channel_incidence_authorized"),
                "channel_feature_map_on_common_clark_module_authorized": poisson_lift.get("channel_feature_map_on_common_clark_module_authorized"),
                "channel_pairing_signature_authorized": poisson_lift.get("channel_pairing_signature_authorized"),
                "cutoff_covariance_authorized": poisson_lift.get("cutoff_covariance_authorized"),
                "lift_formula": poisson_lift.get("lift_formula"),
                "positive_lift_scalar_readout": str(positive_readout),
                "indefinite_lift_scalar_readout": str(indefinite_readout),
                "positive_lift_min_generalized_rayleigh": str(positive_min_rayleigh),
                "indefinite_lift_min_generalized_rayleigh": str(indefinite_min_rayleigh),
                "same_scalar_readout_determines_energy": positive_readout != indefinite_readout,
                "minimal_missing_packet": ["common Clark shift state module", "four channel feature rows W_X", "source pairing/signature J_X", "typed residual decomposition", "cutoff intertwining law"],
                "theorem": "four-channel scalar incidence does not determine a Poisson/Green energy; a source pairing on channel features is additional data",
            },
            "poisson_lift_gauge_gate": {
                "scalar_incidence_before": str(scalar_before),
                "scalar_incidence_after": str(scalar_after),
                "scalar_incidence_gauge_invariant": scalar_before == scalar_after,
                "naive_identity_gram_before": str(naive_energy_before),
                "naive_identity_gram_after": str(naive_energy_after),
                "naive_identity_gram_gauge_invariant": naive_energy_before == naive_energy_after,
                "transported_pairing_energy_before": str(invariant_energy_before),
                "transported_pairing_energy_after": str(invariant_energy_after),
                "transported_pairing_energy_gauge_invariant": invariant_energy_before == invariant_energy_after,
                "pairing_transport_law": poisson_gauge.get("pairing_transport_law"),
                "source_pairing_selected": poisson_gauge.get("source_pairing_selected"),
                "identity_pairing_canonical": poisson_gauge.get("claims_identity_pairing_canonical"),
                "theorem": "a scalar incidence has contragredient channel gauge, so a quadratic lift is natural only with a transported source pairing",
            },
            "reflection_pairing_nonuniqueness_gate": {
                "both_pairings_reflection_invariant": swap_invariant(pairing_0) and swap_invariant(pairing_1),
                "both_pairings_positive_definite": symmetric_two_by_two_positive(pairing_0) and symmetric_two_by_two_positive(pairing_1),
                "test_energy_0": str(reflection_energy_0),
                "test_energy_1": str(reflection_energy_1),
                "pairings_distinguished_by_energy": reflection_energy_0 != reflection_energy_1,
                "reflection_and_positivity_select_unique_pairing": reflection_pairing.get("claims_reflection_and_positivity_select_unique_pairing"),
                "source_flux_normalization_authorized": reflection_pairing.get("source_flux_normalization_authorized"),
                "theorem": "reflection invariance and positivity leave a nontrivial commutant cone, so a source flux normalization is still required",
            },
            "reflection_sector_normalization_gate": {
                "candidate_even_energies": [str(even_energy_0), str(even_energy_1)],
                "candidate_odd_energies": [str(odd_energy_0), str(odd_energy_1)],
                "one_even_normalization_jointly_faithful": even_energy_0 != even_energy_1 or odd_energy_0 == odd_energy_1,
                "minimal_independent_sector_normalizations": sector_normalization.get("minimal_independent_sector_normalizations"),
                "even_flux_normalization_authorized": sector_normalization.get("even_flux_normalization_authorized"),
                "odd_flux_normalization_authorized": sector_normalization.get("odd_flux_normalization_authorized"),
                "theorem": "the reflection representation splits into even and odd lines, and an invariant positive pairing carries one independent weight on each line",
            },
            "reflection_pairing_reconstruction_gate": {
                "reconstructed_alpha": str(reconstructed_alpha),
                "reconstructed_beta": str(reconstructed_beta),
                "reconstructed_pairing": [[str(x) for x in row] for row in reconstructed_pairing],
                "positive_definite": symmetric_two_by_two_positive(reconstructed_pairing),
                "two_flux_values_reconstruct_pairing": reconstructed_pairing == expected_pairing,
                "scalar_incidence_authorizes_flux_values": pairing_reconstruction.get("scalar_incidence_authorizes_flux_values"),
                "theorem": "authorized even and odd flux values are sufficient to reconstruct the unique reflection-invariant positive pairing",
            },
            "four_channel_reflection_multiplicity_gate": {
                "even_multiplicity": four_channel_reflection.get("even_multiplicity"),
                "odd_multiplicity": four_channel_reflection.get("odd_multiplicity"),
                "real_symmetric_commutant_dimension": four_channel_reflection.get("real_symmetric_commutant_dimension"),
                "both_candidates_reflection_invariant": permutation_invariant(four_candidate_0, four_perm) and permutation_invariant(four_candidate_1, four_perm),
                "first_pair_probe_energies": [str(x) for x in first_pair_energies],
                "second_pair_even_energies": [str(x) for x in second_pair_even_energies],
                "two_scalar_fluxes_reconstruct_four_channel_pairing": four_channel_reflection.get("claims_two_scalar_fluxes_reconstruct_four_channel_pairing"),
                "additional_channel_symmetry_authorized": four_channel_reflection.get("additional_channel_symmetry_authorized"),
                "theorem": "four channels with pairwise reflection have multiplicity two in each parity sector, leaving a six-parameter real symmetric invariant pairing",
            },
            "four_channel_source_action_gate": {
                "ordered_channels": four_channel_source.get("ordered_channels"),
                "reciprocal_reflection_permutation": four_channel_source.get("reciprocal_reflection_permutation"),
                "source_reflection_matches_multiplicity_fixture": source_reflection_matches,
                "larger_channel_action_source_authorized": four_channel_source.get("larger_channel_action_source_authorized"),
                "bulk_boundary_exchange_symmetry_claimed": four_channel_source.get("claims_bulk_boundary_exchange_symmetry"),
                "theorem": "Tate-Poisson reciprocity authorizes two reflected channel pairs but no bulk-boundary exchange action",
            },
            "six_probe_pairing_reconstruction_gate": {
                "even_probe_energies": [str(x) for x in even_probe_energies],
                "odd_probe_energies": [str(x) for x in odd_probe_energies],
                "reconstructed_even_block": [[str(x) for x in row] for row in reconstructed_even_block],
                "reconstructed_odd_block": [[str(x) for x in row] for row in reconstructed_odd_block],
                "six_probes_reconstruct_pairing": reconstructed_even_block == even_block and reconstructed_odd_block == odd_block,
                "five_probe_hostile_has_unseen_direction": hostile_diagonal_data_equal,
                "minimal_linear_probe_count": six_probe.get("expected_parameter_count"),
                "six_flux_ports_source_authorized": six_probe.get("six_flux_ports_source_authorized"),
                "theorem": "three polarized quadratic probes in each parity multiplicity space reconstruct the six-parameter invariant pairing, and fewer than six linear measurements cannot be faithful",
            },
            "symmetric_square_observability_gate": {
                "design_rank": design_rank,
                "design_determinant": str(design_determinant),
                "hostile_design_rank": hostile_design_rank,
                "full_rank_design_is_faithful": design_rank == 6,
                "six_ports_alone_are_sufficient": hostile_design_rank == 6,
                "source_feature_family_authorized": symmetric_observability.get("source_feature_family_authorized"),
                "theorem": "pairing observability is rank of the source-generated symmetric-square design, not the raw number of ports",
            },
            "reflection_orbit_observability_gate": {
                "probe_design_row": orbit_rows[0] if orbit_rows else None,
                "reflected_design_row": orbit_rows[1] if orbit_rows else None,
                "two_port_rank": orbit_rank,
                "reflection_orbit_adds_independent_observation": orbit_rank > 1,
                "additional_seed_family_source_authorized": reflection_orbit_observability.get("additional_seed_family_source_authorized"),
                "theorem": "a symmetry orbit does not increase observability rank on an invariant pairing because orbit-related probes induce the same restricted functional",
            },
            "even_jet_observability_gate": {
                "normalized_even_jet_orders": even_jet_observability.get("normalized_even_jet_orders"),
                "even_jet_rank": even_jet_rank,
                "truncated_even_jet_rank": truncated_even_jet_rank,
                "odd_jets_vanish": even_jet_observability.get("odd_jets_vanish"),
                "six_even_jets_can_be_faithful": even_jet_rank == 6,
                "source_feature_germ_authorized": even_jet_observability.get("source_feature_germ_authorized"),
                "scalar_section_jets_are_feature_jets": even_jet_observability.get("claims_scalar_section_jets_are_feature_jets"),
                "theorem": "reciprocity kills odd seam jets, while six independent normalized even jets can span the invariant pairing dual",
            },
            "symmetric_square_gauge_character_gate": {
                "total_gauge_character": total_gauge_character,
                "original_design_determinant": symmetric_square_gauge.get("original_design_determinant"),
                "transformed_design_determinant": transformed_design_determinant,
                "determinant_value_gauge_invariant": transformed_design_determinant == symmetric_square_gauge.get("original_design_determinant"),
                "determinant_nonvanishing_gauge_invariant": total_gauge_character != 0,
                "nonvanishing_selects_pairing": symmetric_square_gauge.get("claims_nonvanishing_selects_pairing"),
                "theorem": "the symmetric-square observability determinant is a relative invariant, so its value changes by a nonzero character while its vanishing locus is gauge invariant",
            },
            "observability_determinant_line_gate": {
                "line_type": determinant_line.get("line_type"),
                "orientation_character": orientation_character,
                "original_local_coordinate": determinant_line.get("original_local_coordinate"),
                "transformed_local_coordinate": transformed_local_coordinate,
                "nonvanishing_preserved": nonvanishing_preserved,
                "sign_preserved": sign_preserved,
                "source_orientation_authorized": determinant_line.get("source_orientation_authorized"),
                "positive_determinant_intrinsic": determinant_line.get("claims_positive_determinant_intrinsic"),
                "theorem": "the observability determinant is a section of a character line; without a source orientation only its zero locus, not its sign, is intrinsic",
            },
            "observability_divisor_gate": {
                "original_vanishing_order": original_vanishing_order,
                "regular_transform_vanishing_order": regular_transform_order,
                "singular_transform_vanishing_order": singular_transform_order,
                "regular_chart_preserves_divisor_multiplicity": original_vanishing_order == regular_transform_order,
                "singular_chart_preserves_divisor_multiplicity": original_vanishing_order == singular_transform_order,
                "admissible_chart_requires_nonzero_constant_character": observability_divisor.get("admissible_chart_requires_nonzero_constant_character"),
                "theorem": "analytic invertible gauges preserve the observability divisor and its multiplicity, while a singular gauge can create spurious vanishing order",
            },
            "local_smith_observability_gate": {
                "invariant_order_profiles": smith_profiles,
                "determinant_orders": smith_determinant_orders,
                "cokernel_lengths": smith_cokernel_lengths,
                "special_coranks": smith_special_coranks,
                "minimal_generator_counts": smith_generator_counts,
                "same_divisor_order_different_failure_type": smith_determinant_orders[0] == smith_determinant_orders[1] and smith_special_coranks[0] != smith_special_coranks[1],
                "regular_left_right_equivalence_preserves_profile": local_smith.get("regular_left_right_equivalence_preserves_profile"),
                "source_analytic_observability_matrix_authorized": local_smith.get("source_analytic_observability_matrix_authorized"),
                "theorem": "the local Smith profile classifies the number and depth of lost observation directions, while determinant order records only their total length",
            },
            "determinantal_divisor_reconstruction_gate": {
                "fixture_a_determinantal_valuations": fixture_a_deltas,
                "fixture_b_determinantal_valuations": fixture_b_deltas,
                "recovered_fixture_a_profile": recovered_fixture_a_profile,
                "recovered_fixture_b_profile": recovered_fixture_b_profile,
                "same_top_valuation": fixture_a_deltas[-1] == fixture_b_deltas[-1],
                "lower_determinantal_valuation_separates_profiles": fixture_a_deltas[:-1] != fixture_b_deltas[:-1],
                "determinantal_ideals_regular_equivalence_invariant": determinantal_divisors.get("determinantal_ideals_regular_equivalence_invariant"),
                "source_minor_ideals_authorized": determinantal_divisors.get("source_minor_ideals_authorized"),
                "theorem": "valuations of all determinantal ideals reconstruct the local Smith profile by successive differences",
            },
            "defect_module_barcode_gate": {
                "torsion_summand_depths": barcode_summands,
                "depth_layer_dimensions": barcode_layers,
                "total_lengths": barcode_lengths,
                "equal_length_different_barcodes": barcode_lengths[0] == barcode_lengths[1] and barcode_layers[0] != barcode_layers[1],
                "source_residue_module_authorized": defect_barcode.get("source_residue_module_authorized"),
                "theorem": "positive Smith orders are persistence lengths of hidden observation directions, and their depth-layer dimensions form the defect barcode",
            },
            "derived_specialization_kernel_gate": {
                "generic_kernel_dimensions": derived_specialization.get("generic_kernel_dimensions"),
                "special_kernel_dimensions": derived_special_kernel_dimensions,
                "tor1_dimensions": derived_tor1_dimensions,
                "tor1_matches_special_kernel": derived_tor1_dimensions == derived_special_kernel_dimensions,
                "tor1_detects_generator_count_not_depth": derived_specialization.get("tor1_detects_generator_count_not_depth"),
                "full_torsion_cokernel_retains_depth": derived_specialization.get("full_torsion_cokernel_retains_depth"),
                "source_derived_kernel_authorized": derived_specialization.get("source_derived_kernel_authorized"),
                "theorem": "specialization-born kernel directions are the Tor_1 shadow of the torsion defect module, while their persistence depths live in the full cokernel",
            },
            "observability_defect_variance_gate": {
                "map_type": defect_variance.get("map_type"),
                "kernel_meaning": defect_variance.get("kernel_meaning"),
                "cokernel_meaning": defect_variance.get("cokernel_meaning"),
                "tor1_meaning": defect_variance.get("tor1_meaning"),
                "special_kernel_dimensions": variance_kernel_dimensions,
                "special_cokernel_dimensions": variance_cokernel_dimensions,
                "equal_dimensions_canonically_identify_kernel_and_cokernel": defect_variance.get("claims_equal_dimensions_canonically_identify_kernel_and_cokernel"),
                "source_kernel_cokernel_duality_authorized": defect_variance.get("source_kernel_cokernel_duality_authorized"),
                "theorem": "kernel and cokernel have opposite observational variance; equal dimensions in a square fixture do not identify their elements",
            },
            "kernel_cokernel_duality_gate": {
                "kernel_witness": [str(x) for x in duality_kernel_witness],
                "adjoint_kernel_witness": [str(x) for x in adjoint_kernel_witness],
                "kernel_and_adjoint_kernel_distinct": duality_kernel_witness != adjoint_kernel_witness,
                "duality_law": kernel_cokernel_duality.get("duality_law"),
                "perfect_parameter_observation_duality_authorized": kernel_cokernel_duality.get("perfect_parameter_observation_duality_authorized"),
                "adjointness_cell_authorized": kernel_cokernel_duality.get("adjointness_cell_authorized"),
                "square_matrix_supplies_self_duality": kernel_cokernel_duality.get("claims_square_matrix_supplies_self_duality"),
                "theorem": "duality identifies the dual cokernel with the adjoint kernel; identifying it with the original kernel additionally requires source adjointness",
            },
            "green_adjointness_residual_gate": {
                "boundary_residual": [[str(x) for x in row] for row in green_residual],
                "boundary_residual_nonzero": any(value for row in green_residual for value in row),
                "boundary_residual_is_typed": green_adjointness.get("boundary_residual_is_typed"),
                "source_boundary_condition_annihilates_residual": green_adjointness.get("source_boundary_condition_annihilates_residual"),
                "retaining_residual_makes_operator_self_adjoint": green_adjointness.get("claims_retaining_residual_makes_operator_self_adjoint"),
                "source_green_matrix_authorized": green_adjointness.get("source_green_matrix_authorized"),
                "theorem": "the Green boundary current is the typed adjointness residual; retaining it accounts for non-self-adjointness but does not annihilate it",
            },
            "lagrangian_boundary_condition_gate": {
                "boundary_form_skew_nondegenerate": boundary_form_skew and boundary_form_nondegenerate,
                "candidate_line_pairings": [str(x) for x in line_pairings],
                "both_candidates_lagrangian": both_candidates_isotropic and lagrangian_boundary.get("expected_lagrangian_dimension") * 2 == lagrangian_boundary.get("expected_boundary_dimension"),
                "candidates_distinct": candidates_distinct,
                "source_lagrangian_selected": lagrangian_boundary.get("source_lagrangian_selected"),
                "adjointness_selects_unique_boundary_domain": lagrangian_boundary.get("claims_adjointness_selects_unique_boundary_domain"),
                "theorem": "annihilating a symplectic Green residual requires a Lagrangian boundary domain, but adjointness alone does not select one among the Lagrangian family",
            },
            "boundary_selection_kernel_dependence_gate": {
                "both_domains_lagrangian": all(extension_isotropic),
                "restricted_operator_images": [[str(x) for x in image] for image in extension_images],
                "restricted_kernel_dimensions": restricted_kernel_dimensions,
                "kernel_depends_on_lagrangian_selection": len(set(restricted_kernel_dimensions)) > 1,
                "source_extension_selection_authorized": boundary_kernel_dependence.get("source_extension_selection_authorized"),
                "theorem": "distinct Lagrangian boundary domains can define adjoint extensions with different kernels, so extension selection is kernel data",
            },
            "boundary_selector_insufficiency_gate": {
                "reflection_anti_symplectic": reflection_anti_symplectic,
                "candidate_lines_reflection_invariant": selector_line_invariant,
                "candidate_lines_lagrangian": selector_isotropic,
                "candidate_boundary_energies": [str(x) for x in selector_energies],
                "reflection_and_positivity_select_unique_domain": boundary_selector.get("claims_reflection_and_positivity_select_unique_domain"),
                "additional_selector_source_authorized": boundary_selector.get("additional_selector_source_authorized"),
                "theorem": "reflection invariance and positive boundary energy can leave multiple Lagrangian extensions, so they do not by themselves select the physical domain",
                "candidate_orbit_under_exchange": candidate_orbit,
                "exchange_anti_symplectic": exchange_anti_symplectic,
                "exchange_preserves_energy": exchange_preserves_energy,
                "invariant_selector_distinguishes_one_orbit": boundary_selector.get("claims_invariant_selector_distinguishes_one_orbit"),
                "orbit_obstruction_theorem": "an invariant selector is constant on every symmetry orbit, so it cannot choose between symmetry-related Lagrangian domains",
            },
            "orbit_separating_selector_gate": {
                "candidate_scores": [str(x) for x in orbit_scores],
                "selected_candidate": selected_candidate,
                "unique_selection": selected_candidate is not None,
                "selector_exchange_invariant": selector_exchange_invariant,
                "orbit_separation_is_mathematically_sufficient": orbit_selector.get("orbit_separation_is_mathematically_sufficient"),
                "selector_form_source_authorized": orbit_selector.get("selector_form_source_authorized"),
                "selector_executable": orbit_selector.get("selector_executable"),
                "mathematical_sufficiency_implies_source_authority": orbit_selector.get("claims_mathematical_sufficiency_implies_source_authority"),
                "theorem": "a function selects a unique candidate from a finite admissible family exactly when its extremal fiber is a singleton; separating one symmetry orbit requires symmetry-breaking data",
            },
            "selector_torsor_gate": {
                "exchange_character": torsor_character,
                "positive_generator_scores": [str(x) for x in positive_torsor_scores],
                "negative_generator_scores": [str(x) for x in negative_torsor_scores],
                "positive_generator_choice": positive_choice,
                "negative_generator_choice": negative_choice,
                "opposite_orientations_select_opposite_domains": {positive_choice, negative_choice} == {0, 1},
                "zero_section_selects_uniquely": selector_torsor.get("zero_section_selects_uniquely"),
                "selector_space_is_two_orientation_torsor": selector_torsor.get("selector_space_is_two_orientation_torsor"),
                "source_coorientation_authorized": selector_torsor.get("source_coorientation_authorized"),
                "torsor_has_canonical_element": selector_torsor.get("claims_torsor_has_canonical_element"),
                "theorem": "the minimal binary-domain selector is a nonzero section of the exchange sign line; its two orientations select opposite domains and no orientation is canonical without source coorientation",
            },
            "selector_wall_kernel_jump_gate": {
                "candidate_orbit_under_exchange": wall_orbit,
                "invariant_boundary_energies": [str(x) for x in wall_energies],
                "selector_anti_invariant": wall_selector_anti_invariant,
                "selector_base_scores": [str(x) for x in wall_base_scores],
                "candidate_restricted_kernel_dimensions": wall_kernel_dimensions,
                "selected_candidates_by_parameter": wall_selected_candidates,
                "selected_kernel_dimensions_by_parameter": wall_selected_kernel_dimensions,
                "zero_parameter_is_selector_wall": wall_selected_candidates[1] is None,
                "bulk_operator_constant": selector_wall.get("bulk_operator_constant"),
                "wall_is_bulk_rank_failure": selector_wall.get("claims_wall_is_bulk_rank_failure"),
                "source_path_through_selector_space_authorized": selector_wall.get("source_path_through_selector_space_authorized"),
                "theorem": "crossing the zero section of a boundary-selector sign line can switch between extension domains with different restricted kernels while the bulk operator remains constant",
            },
            "lagrangian_kernel_incidence_gate": {
                "bulk_kernel_witness_valid": bulk_kernel_witness_valid,
                "intersection_dimensions": incidence_dimensions,
                "restricted_kernel_dimensions": incidence_restricted_kernel_dimensions,
                "restricted_kernel_equals_boundary_intersection": incidence_dimensions == incidence_restricted_kernel_dimensions,
                "kernel_incidence_locus": kernel_incidence.get("kernel_incidence_locus_name"),
                "continuous_lagrangian_family_source_authorized": kernel_incidence.get("continuous_lagrangian_family_source_authorized"),
                "gap_continuity_authorized": kernel_incidence.get("gap_continuity_authorized"),
                "self_adjoint_family_authorized": kernel_incidence.get("self_adjoint_family_authorized"),
                "incidence_count_is_spectral_flow": kernel_incidence.get("claims_incidence_count_is_spectral_flow"),
                "incidence_count_is_maslov_index": kernel_incidence.get("claims_incidence_count_is_maslov_index"),
                "theorem": "for a fixed bulk operator M restricted to a boundary domain L, ker(M restricted to L) equals L intersection ker(M); the jump locus is therefore a Lagrangian incidence locus",
            },
            "lagrangian_incidence_stratification_gate": {
                "bulk_kernel_basis_valid": strata_kernel_valid,
                "candidate_domains_lagrangian": strata_domains_isotropic,
                "intersection_dimensions": strata_intersections,
                "restricted_kernel_dimensions": strata_restricted_kernels,
                "nested_strata_counts": nested_strata_counts,
                "incidence_equals_restricted_kernel_dimension": strata_intersections == strata_restricted_kernels,
                "finite_fixture_proves_global_schubert_geometry": incidence_stratification.get("claims_finite_fixture_proves_global_schubert_geometry"),
                "source_lagrangian_family_authorized": incidence_stratification.get("source_lagrangian_family_authorized"),
                "theorem": "the loci dim(L intersection ker M) at least r form a nested determinantal stratification of the admissible Lagrangian family; the finite fixture realizes depths zero, one, and two",
            },
            "lagrangian_graph_smith_barcode_gate": {
                "determinantal_valuations": graph_determinantal_valuations,
                "smith_profile": graph_smith_profile,
                "generic_intersection_dimension": graph_generic_intersection,
                "special_intersection_dimension": graph_special_intersection,
                "total_defect_length": graph_total_defect_length,
                "regular_graph_chart_required": graph_smith.get("regular_graph_chart_required"),
                "top_determinant_order_determines_special_corank": graph_smith.get("claims_top_determinant_order_determines_special_corank"),
                "source_analytic_boundary_graph_authorized": graph_smith.get("source_analytic_boundary_graph_authorized"),
                "theorem": "in a regular Lagrangian graph chart L_A, boundary-kernel incidence equals ker A and the local Smith profile of A records the persistence depths of the incident kernel directions",
            },
            "boundary_smith_chart_invariance_gate": {
                "regular_transform_determinant": chart_transform_det,
                "regular_entry_valuations": regular_entry_valuations,
                "regular_determinant_valuation": regular_determinant_valuation,
                "regular_smith_profile": regular_smith_profile,
                "singular_diagonal_exponents": singular_diagonal_exponents,
                "singular_smith_profile": singular_smith_profile,
                "regular_chart_preserves_profile": regular_smith_profile == graph_smith_profile,
                "singular_transform_changes_profile": singular_smith_profile != graph_smith_profile,
                "singular_transform_is_admissible_chart": smith_chart.get("claims_singular_transform_is_admissible_chart"),
                "singular_profile_is_intrinsic": smith_chart.get("claims_singular_profile_is_intrinsic"),
                "theorem": "regular unimodular graph-coordinate congruence preserves the boundary Smith profile, while a singular coordinate transform can counterfeit incidence depth",
            },
            "simultaneous_boundary_transport_gate": {
                "transport_is_symplectic": simultaneous_is_symplectic,
                "original_intersection_dimension": original_pair_intersection,
                "simultaneous_intersection_dimension": simultaneous_pair_intersection,
                "one_sided_intersection_dimension": one_sided_pair_intersection,
                "simultaneous_transport_preserves_incidence": original_pair_intersection == simultaneous_pair_intersection,
                "one_sided_transport_is_coordinate_change": simultaneous_transport.get("claims_one_sided_transport_is_coordinate_change"),
                "source_bulk_kernel_transport_cell_authorized": simultaneous_transport.get("source_bulk_kernel_transport_cell_authorized"),
                "theorem": "boundary incidence and its barcode belong to the pair (L,ker M); an invertible symplectic coordinate change preserves them only when both members are transported",
            },
            "operator_transport_square_gate": {
                "square_commutes": transport_square_commutes,
                "source_kernel_witness_valid": source_kernel_valid,
                "transported_kernel_witness_valid": transported_kernel_valid,
                "transported_domain_generator": [str(x) for x in transported_domain_generator],
                "transported_kernel_generator": [str(x) for x in transported_kernel_generator],
                "transported_domain_kernel_intersection_dimension": transported_domain_kernel_intersection,
                "one_sided_restricted_kernel_dimension": one_sided_restricted_kernel_dimension,
                "codomain_transport_injective": operator_transport.get("codomain_transport_injective"),
                "source_transport_square_authorized": operator_transport.get("source_transport_square_authorized"),
                "domain_transport_alone_transports_kernel": operator_transport.get("claims_domain_transport_alone_transports_kernel"),
                "theorem": "a commuting square M' S = T M with invertible S and injective T transports ker M to ker M'; domain transport alone supplies no such identification",
            },
            "relative_codomain_injectivity_gate": {
                "good_square_commutes": good_square_commutes,
                "bad_square_commutes": bad_square_commutes,
                "source_kernel_dimension": relative_source_kernel_dimension,
                "good_transported_kernel_dimension": relative_good_kernel_dimension,
                "bad_transported_kernel_dimension": relative_bad_kernel_dimension,
                "good_transport_injective_on_operator_image": good_injective_on_image,
                "bad_transport_injective_on_operator_image": bad_injective_on_image,
                "commuting_square_alone_preserves_kernel": relative_injectivity.get("claims_commuting_square_alone_preserves_kernel"),
                "source_relative_injectivity_authorized": relative_injectivity.get("source_relative_injectivity_authorized"),
                "theorem": "for M' S = T M with invertible S, exact kernel transport holds iff ker T intersects im M trivially; global injectivity of T is sufficient but unnecessary",
            },
            "kernel_transport_residue_sequence_gate": {
                "exact_sequence": transport_residue.get("exact_sequence"),
                "good_overlap_dimension": good_overlap_dimension,
                "bad_overlap_dimension": bad_overlap_dimension,
                "good_excess_kernel_dimension": good_excess_kernel_dimension,
                "bad_excess_kernel_dimension": bad_excess_kernel_dimension,
                "overlap_equals_excess_kernel": good_overlap_dimension == good_excess_kernel_dimension and bad_overlap_dimension == bad_excess_kernel_dimension,
                "residue_kind": transport_residue.get("residue_kind"),
                "residue_is_tor_or_derived_kernel": transport_residue.get("claims_residue_is_tor_or_derived_kernel"),
                "source_residue_readout_authorized": transport_residue.get("source_residue_readout_authorized"),
                "theorem": "the excess transported kernel is canonically the overlap ker T intersection im M via the short exact sequence 0 -> ker M -> M^(-1)(ker T) -> ker T intersection im M -> 0",
            },
            "composite_transport_residue_filtration_gate": {
                "source_kernel_dimension": composite_source_kernel_dimension,
                "first_kernel_dimension": composite_first_kernel_dimension,
                "composite_kernel_dimension": composite_final_kernel_dimension,
                "first_residue_dimension": composite_first_residue_dimension,
                "second_residue_dimension": composite_second_residue_dimension,
                "second_overlap_dimension": composite_second_overlap_dimension,
                "composite_residue_dimension": composite_total_residue_dimension,
                "residue_dimensions_add": composite_residue_additive,
                "residue_layers_are_logical_factorization_not_time": composite_residue.get("residue_layers_are_logical_factorization_not_time"),
                "final_nullity_forgets_residue_filtration": composite_residue.get("claims_final_nullity_forgets_residue_filtration"),
                "source_composite_transport_authorized": composite_residue.get("source_composite_transport_authorized"),
                "theorem": "a factored codomain transport gives the excess kernel a filtration whose successive quotients are the image-overlap residues created by each factor",
            },
            "factorization_dependent_residue_flag_gate": {
                "common_composite": common_composite,
                "first_kernel_a": [[str(x) for x in vector] for vector in first_kernel_a],
                "first_kernel_b": [[str(x) for x in vector] for vector in first_kernel_b],
                "distinct_first_flags": distinct_first_flags,
                "same_final_kernel": same_final_kernel,
                "common_final_kernel_dimension": len(final_kernel_a),
                "composite_map_canonically_determines_residue_flag": factorization_flag.get("claims_composite_map_canonically_determines_residue_flag"),
                "factorization_comparison_cell_authorized": factorization_flag.get("factorization_comparison_cell_authorized"),
                "theorem": "equal composite transport maps can induce different residue flags; the flag belongs to the factorization unless a source comparison cell identifies the filtered objects",
            },
            "residue_flag_comparison_torsor_gate": {
                "candidate_count": len(comparison_candidates),
                "candidate_invertibility": comparison_invertible,
                "candidates_commute_with_endpoint": comparison_commutes,
                "candidates_map_source_flag_to_target": comparison_maps_flag,
                "candidates_distinct": comparison_candidates_distinct,
                "comparison_space_has_nontrivial_stabilizer": flag_comparison.get("comparison_space_has_nontrivial_stabilizer"),
                "existence_implies_canonical_comparison": flag_comparison.get("claims_existence_implies_canonical_comparison"),
                "source_comparison_choice_authorized": flag_comparison.get("source_comparison_choice_authorized"),
                "theorem": "comparison cells between residue flags form a torsor under endpoint automorphisms stabilizing the target flag; existence of a comparison does not select a canonical one",
            },
            "residue_flag_triangle_holonomy_gate": {
                "pairwise_comparisons_valid": triangle_pairwise_valid,
                "comparison_maps_invertible": triangle_maps_invertible,
                "comparison_maps_commute_with_endpoint": triangle_maps_commute,
                "holonomy": [[int(x) if x.denominator == 1 else str(x) for x in row] for row in triangle_holonomy],
                "holonomy_stabilizes_source_flag": triangle_holonomy_stabilizes_source,
                "triangle_coherent": triangle_coherent,
                "holonomy_kind": flag_triangle.get("holonomy_kind"),
                "source_triangle_coherence_cell_authorized": flag_triangle.get("source_triangle_coherence_cell_authorized"),
                "pairwise_validity_implies_triangle_coherence": flag_triangle.get("claims_pairwise_validity_implies_triangle_coherence"),
                "theorem": "pairwise valid residue-flag comparisons descend coherently only when their cycle holonomy is identity or is killed by a source-authorized higher coherence cell",
            },
            "triangle_holonomy_gauge_gate": {
                "original_holonomy": [[int(x) for x in row] for row in triangle_holonomy],
                "gauged_holonomy": [[int(x) for x in row] for row in gauged_holonomy],
                "raw_matrix_changed": triangle_holonomy != gauged_holonomy,
                "trace_before_after": [int(holonomy_trace), int(gauged_holonomy_trace)],
                "determinant_before_after": [int(holonomy_determinant), int(gauged_holonomy_determinant)],
                "identity_status_gauge_invariant": holonomy_identity_status_preserved,
                "raw_holonomy_matrix_is_gauge_invariant": holonomy_gauge.get("claims_raw_holonomy_matrix_is_gauge_invariant"),
                "source_stabilizer_trivialization_authorized": holonomy_gauge.get("source_stabilizer_trivialization_authorized"),
                "theorem": "vertex presentation changes conjugate cycle holonomy; its raw matrix is gauge-dependent while its identity status and conjugacy invariants are intrinsic",
            },
            "holonomy_observability_gate": {
                "identity_trace_determinant": [identity_trace, identity_determinant],
                "unipotent_trace_determinant": [unipotent_trace, unipotent_determinant],
                "scalar_ports_collide": scalar_ports_collide,
                "identity_displacement_rank": identity_displacement_rank,
                "unipotent_displacement_rank": unipotent_displacement_rank,
                "trace_determinant_ports_jointly_faithful": holonomy_observability.get("trace_determinant_ports_jointly_faithful"),
                "displacement_rank_conjugacy_invariant": holonomy_observability.get("displacement_rank_conjugacy_invariant"),
                "source_displacement_rank_port_authorized": holonomy_observability.get("source_displacement_rank_port_authorized"),
                "scalar_character_detects_all_holonomy": holonomy_observability.get("claims_scalar_character_detects_all_holonomy"),
                "theorem": "trace and determinant do not detect all nonidentity holonomy; identity and nontrivial unipotent classes collide there, while rank(H-I) separates this hostile pair",
            },
            "unipotent_holonomy_rank_profile_gate": {
                "traces": unipotent_traces,
                "determinants": unipotent_determinants,
                "rank_profile_31": unipotent_rank_profiles[0],
                "rank_profile_22": unipotent_rank_profiles[1],
                "first_displacement_ranks_collide": unipotent_rank_profiles[0][0] == unipotent_rank_profiles[1][0],
                "higher_rank_profiles_separate": unipotent_rank_profiles[0] != unipotent_rank_profiles[1],
                "rank_profile_determines_unipotent_jordan_partition": unipotent_profile.get("rank_profile_determines_unipotent_jordan_partition"),
                "single_displacement_rank_jointly_faithful": unipotent_profile.get("single_displacement_rank_jointly_faithful"),
                "source_rank_profile_ports_authorized": unipotent_profile.get("source_rank_profile_ports_authorized"),
                "finite_rank_profile_is_full_general_holonomy_classifier": unipotent_profile.get("claims_finite_rank_profile_is_full_general_holonomy_classifier"),
                "theorem": "for unipotent holonomy in finite dimension, the ranks of successive powers of H-I recover the nilpotent Jordan partition; the first displacement rank alone does not",
            },
            "rational_canonical_holonomy_gate": {
                "base_field": rational_holonomy.get("base_field"),
                "characteristic_polynomials_equal": rational_characteristic_polynomials_equal,
                "common_characteristic_polynomial": rational_holonomy.get("expected_common_characteristic_polynomial"),
                "identity_pencil_invariant_factors": identity_pencil_factors,
                "unipotent_pencil_invariant_factors": unipotent_pencil_factors,
                "pencil_smith_data_separate": identity_pencil_factors != unipotent_pencil_factors,
                "polynomial_pencil_smith_data_classifies_similarity": rational_holonomy.get("polynomial_pencil_smith_data_classifies_similarity"),
                "characteristic_polynomial_classifies_similarity": rational_holonomy.get("claims_characteristic_polynomial_classifies_similarity"),
                "source_polynomial_pencil_ports_authorized": rational_holonomy.get("source_polynomial_pencil_ports_authorized"),
                "field_classifier_applies_unchanged_over_completion_ring": rational_holonomy.get("claims_field_classifier_applies_unchanged_over_completion_ring"),
                "theorem": "over a field, the invariant factors of xI-H classify finite-dimensional holonomy up to similarity; the characteristic polynomial alone is only their product",
            },
            "non_pid_fitting_holonomy_gate": {
                "coefficient_ring": non_pid_fitting.get("coefficient_ring"),
                "ring_is_pid": non_pid_fitting.get("ring_is_pid"),
                "common_determinant_ideal": fitting_common_determinant_ideal,
                "first_determinantal_ideal_a": fitting_first_ideal_a,
                "first_determinantal_ideal_b": fitting_first_ideal_b,
                "first_determinantal_ideals_distinct": fitting_ideals_distinct,
                "first_ideal_a_principal": non_pid_fitting.get("first_ideal_a_principal"),
                "fitting_ideals_preserved_under_module_presentation_change": non_pid_fitting.get("fitting_ideals_preserved_under_module_presentation_change"),
                "smith_normal_form_exists_over_ring": non_pid_fitting.get("claims_smith_normal_form_exists_over_ring"),
                "equal_determinant_ideal_implies_equal_cokernel_module": non_pid_fitting.get("claims_equal_determinant_ideal_implies_equal_cokernel_module"),
                "source_completion_coefficient_ring_authorized": non_pid_fitting.get("source_completion_coefficient_ring_authorized"),
                "theorem": "over a non-PID coefficient ring, determinantal and Fitting ideals remain presentation invariants even when Smith invariant factors do not exist",
            },
            "fitting_rank_stratification_gate": {
                "sample_points": fitting_sample_points,
                "ranks_a": fitting_ranks_a,
                "ranks_b": fitting_ranks_b,
                "determinant_zero_pattern_a": fitting_determinant_zero_a,
                "determinant_zero_pattern_b": fitting_determinant_zero_b,
                "common_determinant_zero_pattern": fitting_determinant_zero_a == fitting_determinant_zero_b,
                "rank_at_most_1_locus": fitting_strata.get("rank_at_most_1_locus"),
                "rank_at_most_0_locus_a": fitting_strata.get("rank_at_most_0_locus_a"),
                "rank_at_most_0_locus_b": fitting_strata.get("rank_at_most_0_locus_b"),
                "common_determinant_divisor_implies_common_rank_stratification": fitting_strata.get("claims_common_determinant_divisor_implies_common_rank_stratification"),
                "source_geometric_family_authorized": fitting_strata.get("source_geometric_family_authorized"),
                "theorem": "the full determinantal ideal hierarchy defines nested rank-drop loci; equal top determinant divisors can conceal different deeper kernel-multiplicity strata",
            },
            "directional_fitting_slice_gate": {
                "slice_exponents": slice_exponents,
                "determinant_orders": slice_determinant_orders,
                "profiles_a": slice_profiles_a,
                "profiles_b": slice_profiles_b,
                "special_coranks_a": slice_special_coranks_a,
                "special_coranks_b": slice_special_coranks_b,
                "equal_determinant_orders_but_distinct_profiles": all(sum(left) == sum(right) for left, right in zip(slice_profiles_a, slice_profiles_b)) and slice_profiles_a != slice_profiles_b,
                "parameter_kind": directional_slice.get("parameter_kind"),
                "single_slice_recovers_multivariable_fitting_object": directional_slice.get("claims_single_slice_recovers_multivariable_fitting_object"),
                "source_slice_selection_authorized": directional_slice.get("source_slice_selection_authorized"),
                "theorem": "one-parameter pullbacks turn multivariable Fitting data into directional Smith barcodes, but no single slice recovers the whole multivariable defect object",
            },
            "arc_valuation_integral_closure_gate": {
                "monomial_arc_exponents": arc_exponents,
                "orders_i": arc_orders_i,
                "orders_j": arc_orders_j,
                "arc_orders_collide": arc_orders_collide,
                "ideals_equal": arc_closure.get("ideals_equal"),
                "uv_membership_i_j": [arc_closure.get("uv_belongs_to_i"), arc_closure.get("uv_belongs_to_j")],
                "integral_closures_equal": arc_closure.get("integral_closures_equal"),
                "valuative_reconstruction_target": arc_closure.get("valuative_reconstruction_target"),
                "all_arc_orders_recover_exact_ideal": arc_closure.get("claims_all_arc_orders_recover_exact_ideal"),
                "source_complete_arc_family_authorized": arc_closure.get("source_complete_arc_family_authorized"),
                "theorem": "valuations along a complete admissible arc family determine the integral closure of an ideal under suitable hypotheses, not necessarily the ideal or its scheme structure",
            },
            "integral_closure_supported_residue_gate": {
                "quotient": closure_residue.get("quotient"),
                "primitive_generator": closure_residue.get("primitive_quotient_generator"),
                "annihilator_relations_valid": closure_residue_relations_valid,
                "annihilator": closure_residue.get("expected_annihilator"),
                "support": closure_residue.get("expected_support"),
                "local_length": closure_residue.get("expected_local_length"),
                "arc_order_readout_detects_residue": closure_residue.get("arc_order_readout_detects_residue"),
                "exact_ideal_or_rees_data_detects_residue": closure_residue.get("exact_ideal_or_rees_data_detects_residue"),
                "source_scheme_sensitive_port_authorized": closure_residue.get("source_scheme_sensitive_port_authorized"),
                "integral_closure_preserves_supported_residue": closure_residue.get("claims_integral_closure_preserves_supported_residue"),
                "theorem": "the closure defect J/I is a finite module supported at the deeper stratum; for I=(u^2,v^2) inside J=(u,v)^2 it is the one-dimensional origin residue generated by uv",
            },
            "ideal_information_loss_filtration_gate": {
                "exact_sequence": ideal_filtration.get("exact_sequence"),
                "closure_residue_basis": ideal_filtration.get("closure_residue_basis"),
                "radicalization_residue_basis": ideal_filtration.get("radicalization_residue_basis"),
                "closure_residue_length": ideal_closure_length,
                "radicalization_residue_length": ideal_radicalization_length,
                "total_residue_length": ideal_total_residue_length,
                "lengths_add": ideal_total_residue_length == ideal_closure_length + ideal_radicalization_length,
                "valuative_readout_retains": ideal_filtration.get("valuative_readout_retains"),
                "support_readout_retains": ideal_filtration.get("support_readout_retains"),
                "closure_and_radical_residues_are_interchangeable": ideal_filtration.get("claims_closure_and_radical_residues_are_interchangeable"),
                "source_full_ideal_filtration_port_authorized": ideal_filtration.get("source_full_ideal_filtration_port_authorized"),
                "theorem": "exact ideal, integral closure, and radical form a typed information-loss filtration whose successive supported quotients record closure and infinitesimal-neighborhood data",
            },
            "adic_versus_weakstar_completion_gate": {
                "local_ring": completion_comparison.get("local_ring"),
                "adic_completion": completion_comparison.get("adic_completion"),
                "adic_completion_flat": completion_comparison.get("adic_completion_flat"),
                "adic_completion_faithfully_flat_on_finite_modules": completion_comparison.get("adic_completion_faithfully_flat_on_finite_modules"),
                "input_residue_lengths": completion_comparison.get("input_residue_lengths"),
                "completed_residue_lengths": completed_residue_lengths,
                "finite_supported_residue_lengths_preserved": completed_residue_lengths == completion_comparison.get("input_residue_lengths"),
                "weakstar_completion_kind": completion_comparison.get("weakstar_completion_kind"),
                "weakstar_is_ordinary_adic_base_change": completion_comparison.get("weakstar_is_ordinary_adic_base_change"),
                "weakstar_exactness_authorized": completion_comparison.get("weakstar_exactness_authorized"),
                "adic_flatness_proves_weakstar_exactness": completion_comparison.get("claims_adic_flatness_proves_weakstar_exactness"),
                "source_weakstar_comparison_cell_authorized": completion_comparison.get("source_weakstar_comparison_cell_authorized"),
                "theorem": "Noetherian adic completion preserves finite supported residue sequences by faithful flatness, while weak-star completion requires its own topological exactness constructor and comparison cell",
            },
            "weakstar_completion_constructor_gate": {
                "source_space": weakstar_constructor.get("source_space"),
                "declared_predual": weakstar_constructor.get("declared_predual"),
                "ambient_dual": weakstar_constructor.get("ambient_dual"),
                "completion": weakstar_constructor.get("expected_completion"),
                "basis_sequence_weakstar_limit": weakstar_constructor.get("basis_sequence_weakstar_limit"),
                "coordinate_port_extends": weakstar_constructor.get("coordinate_port_extends"),
                "sum_port_values_on_basis": weakstar_basis_values,
                "sum_port_discontinuous_witness": weakstar_sum_discontinuous_witness,
                "sum_port_extends_weakstar_continuously": weakstar_constructor.get("sum_port_extends_weakstar_continuously"),
                "required_map_gate": weakstar_constructor.get("required_map_gate"),
                "required_exactness_gates": weakstar_constructor.get("required_exactness_gates"),
                "theta_dual_pair_source_authorized": weakstar_constructor.get("theta_dual_pair_source_authorized"),
                "algebraic_functional_extends_to_weakstar_completion": weakstar_constructor.get("claims_algebraic_functional_extends_to_weakstar_completion"),
                "theorem": "weak-star completion is typed by a declared dual pair; a functional extends exactly when represented by the predual, and algebraic definition on the dense source is insufficient",
            },
            "magnetic_weakstar_low_mode_ports_gate": {
                "sector": magnetic_ports.get("sector"),
                "source_artifact": magnetic_ports.get("source_artifact"),
                "declared_predual": magnetic_ports.get("declared_predual"),
                "ambient_dual": magnetic_ports.get("ambient_dual"),
                "completion": magnetic_ports.get("completion"),
                "harmonic_multiplicities": magnetic_multiplicities,
                "kernel_dimension": magnetic_kernel_dimension,
                "port_labels": [[degree, order] for degree, order in magnetic_labels],
                "ports_weakstar_continuous": magnetic_ports.get("port_tests_are_continuous"),
                "observation_rank": magnetic_observation_rank,
                "joint_map_with_A3_faithful": magnetic_joint_faithful,
                "deleted_port_rank": magnetic_deleted_rank,
                "fewer_than_21_ports_can_be_faithful": magnetic_ports.get("fewer_than_21_ports_can_be_faithful"),
                "ports_executable_as_finite_integrals": magnetic_ports.get("ports_executable_as_finite_integrals"),
                "source_dual_pair_authorized": magnetic_ports.get("source_dual_pair_authorized"),
                "ports_follow_from_geometric_support_alone": magnetic_ports.get("claims_ports_follow_from_geometric_support_alone"),
                "theorem": "the 21 low-harmonic coefficient ports are weak-star continuous predual evaluations, jointly faithful on the completed magnetic kernel, and minimal by rank-nullity",
            },
            "magnetic_hard_flux_correspondence_gate": {
                "source_object": hard_flux.get("source_object"),
                "target_object": hard_flux.get("target_object"),
                "relation": hard_flux.get("relation"),
                "variance": hard_flux.get("variance"),
                "variance_typed": hard_flux_variance_typed,
                "harmonic_multiplicities": hard_flux_multiplicities,
                "correspondence_rank": hard_flux_rank,
                "all_low_multipliers_nonzero": all(hard_flux.get("source_multipliers_nonzero", [])),
                "angular_support": hard_flux.get("angular_support"),
                "retarded_support_requirement": hard_flux.get("retarded_support_requirement"),
                "support_and_properness_typed": hard_flux_support_typed,
                "linear_constructibility_authorized": hard_flux.get("linear_constructibility_authorized"),
                "nonlinear_dominant_energy_realizability_authorized": hard_flux.get("nonlinear_dominant_energy_realizability_authorized"),
                "construction_supplies_observation_ports": hard_flux.get("construction_supplies_observation_ports"),
                "geometric_support_implies_constructibility": hard_flux.get("claims_geometric_support_implies_constructibility"),
                "theorem": "the linear coexact hard-flux relation is rank 21 on the low block with covariant state transport and contravariant test pullback; support conditions type its pushforward, but construction and observation remain distinct capabilities",
            },
            "characteristic_locus_completed_kernel_separation_gate": {
                "local_symbol": characteristic_separation.get("local_symbol"),
                "factorization_valid": characteristic_factorization_valid,
                "characteristic_object_type": characteristic_separation.get("characteristic_object_type"),
                "compactly_supported_homogeneous_kernel_dimension": compact_support_kernel_dimension,
                "planar_L2_homogeneous_kernel_dimension": planar_l2_kernel_dimension,
                "completed_kernel_object_type": characteristic_separation.get("completed_kernel_object_type"),
                "completed_kernel_degrees": characteristic_completed_degrees,
                "completed_kernel_dimension": characteristic_completed_dimension,
                "completed_kernel_source": characteristic_separation.get("completed_kernel_source"),
                "characteristic_and_completed_kernel_objects_distinct": characteristic_objects_distinct,
                "characteristic_locus_equals_completed_kernel": characteristic_separation.get("claims_characteristic_locus_equals_completed_kernel"),
                "characteristic_support_constructs_global_state": characteristic_separation.get("claims_characteristic_support_constructs_global_state"),
                "theorem": "the local characteristic variety supports neither compactly supported nor planar L2 homogeneous states, while the completed 21-dimensional kernel is a global smooth spherical spectral block",
            },
            "cross_sector_rank_provenance_gate": {
                "left_object": cross_sector_rank.get("left_object"),
                "left_rank": cross_sector_rank.get("left_rank"),
                "left_source_artifact": cross_sector_rank.get("left_source_artifact"),
                "left_source_sha256": cross_sector_rank.get("left_source_sha256"),
                "right_object": cross_sector_rank.get("right_object"),
                "right_rank": cross_sector_rank.get("right_rank"),
                "right_source_artifact": cross_sector_rank.get("right_source_artifact"),
                "right_source_sha256": cross_sector_rank.get("right_source_sha256"),
                "historical_right_rank": cross_sector_rank.get("historical_right_rank"),
                "historical_status": cross_sector_rank.get("historical_status"),
                "current_same_rank": cross_sector_ranks_equal,
                "provenance_typed": cross_sector_provenance_typed,
                "comparison_map": cross_sector_rank.get("comparison_map"),
                "identified": cross_sector_rank.get("identified"),
                "disposition": cross_sector_rank.get("disposition"),
                "requires_digest_refresh_on_source_change": cross_sector_rank.get("requires_digest_refresh_on_source_change"),
                "theorem": "cross-sector rank comparisons are versioned provenance records; the magnetic rank is 21, the current cosmology rank is 26, and the former cosmology rank 21 is only a superseded cutoff plateau",
            },
            "magnetic_construction_observation_composition_gate": {
                "source_low_block": magnetic_composite.get("source_low_block"),
                "constructed_kernel_block": magnetic_composite.get("constructed_kernel_block"),
                "observation_block": magnetic_composite.get("observation_block"),
                "harmonic_multiplicities": composite_multiplicities,
                "construction_rank": construction_rank,
                "observation_rank": observation_rank,
                "label_count": composite_label_count,
                "label_normalization_coherence_cell": magnetic_composite.get("label_normalization_coherence_cell"),
                "label_normalization_coherence_source_authorized": composite_coherence_authorized,
                "composite_rank": magnetic_composite_rank,
                "composite_faithful_on_low_source_block": magnetic_composite_faithful,
                "algebraic_low_block_inverse_exists": magnetic_composite.get("algebraic_low_block_inverse_exists"),
                "nonlinear_source_controller_authorized": magnetic_composite.get("nonlinear_source_controller_authorized"),
                "equal_ranks_imply_composable_capabilities": magnetic_composite.get("claims_equal_ranks_imply_composable_capabilities"),
                "theorem": "hard-flux construction followed by low-harmonic observation is faithful on the 21-dimensional source block only after a source-derived harmonic label and normalization coherence cell",
            },
            "magnetic_low_block_stability_gate": {
                "source_artifact": magnetic_stability.get("source_artifact"),
                "singular_values": [str(value) for value in stability_singular_values],
                "minimum_singular_value": str(stability_minimum),
                "maximum_singular_value": str(stability_maximum),
                "inverse_norm": str(stability_inverse_norm),
                "condition_number": str(stability_condition_number),
                "observation_map_isometry_on_normalized_low_block": magnetic_stability.get("observation_map_isometry_on_normalized_low_block"),
                "quantitative_low_block_reconstruction_authorized": magnetic_stability.get("quantitative_low_block_reconstruction_authorized"),
                "bound_is_uniform_outside_low_block": magnetic_stability.get("claims_bound_is_uniform_outside_low_block"),
                "linear_stability_implies_nonlinear_control": magnetic_stability.get("claims_linear_stability_implies_nonlinear_control"),
                "theorem": "the normalized magnetic low-block construction-observation composite has singular values 6, 12, and 20, inverse norm 1/6, and condition number 10/3",
            },
            "magnetic_low_block_perturbation_margin_gate": {
                "operator_norm_perturbations": [str(value) for value in margin_perturbations],
                "weyl_lower_bounds": [str(value) for value in margin_lower_bounds],
                "certified_inverse_norms": [str(value) if value is not None else None for value in margin_inverse_norms],
                "strict_faithfulness_margin": magnetic_margin.get("strict_faithfulness_margin"),
                "boundary_delta": str(magnetic_margin.get("boundary_delta")),
                "faithfulness_guaranteed_at_boundary": margin_boundary_guaranteed,
                "parameter_kind": magnetic_margin.get("parameter_kind"),
                "physical_noise_model_source_authorized": magnetic_margin.get("physical_noise_model_source_authorized"),
                "mathematical_margin_is_physical_tolerance": magnetic_margin.get("claims_mathematical_margin_is_physical_tolerance"),
                "theorem": "an operator-norm perturbation delta below 6 preserves faithfulness with inverse norm at most 1/(6-delta); at delta 6 the bound no longer guarantees injectivity",
            },
            "magnetic_redundant_observation_frame_gate": {
                "kernel_dimension": frame_dimension,
                "total_port_count": len(frame_matrix),
                "full_rank": frame_full_rank,
                "one_port_deletion_ranks": frame_deletion_ranks,
                "minimum_one_port_deletion_rank": frame_minimum_deletion_rank,
                "one_port_deletion_tolerant": frame_minimum_deletion_rank == frame_dimension,
                "hostile_two_port_deletion": sorted(hostile_deleted_indices),
                "hostile_two_port_rank": hostile_two_port_rank,
                "two_port_deletion_tolerant": magnetic_frame.get("two_port_deletion_tolerant"),
                "redundant_test_is_continuous_predual_element": magnetic_frame.get("redundant_test_is_continuous_predual_element"),
                "redundant_port_source_authorized": magnetic_frame.get("redundant_port_source_authorized"),
                "minimal_faithful_fiber_is_deletion_tolerant": magnetic_frame.get("claims_minimal_faithful_fiber_is_deletion_tolerant"),
                "theorem": "the 21-port coordinate fiber is minimally faithful but not deletion-tolerant; one continuous checksum port yields a rank-21 frame tolerating every single-port deletion but not arbitrary double deletion",
            },
            "magnetic_erasure_budget_frame_gate": {
                "kernel_dimension": erasure_dimension,
                "redundancy_budget": erasure_budget,
                "total_port_count": len(erasure_nodes),
                "surviving_submatrix_count": len(surviving_node_sets),
                "all_surviving_vandermonde_determinants_nonzero": surviving_determinants_nonzero,
                "minimum_rank_after_any_three_deletions": erasure_dimension if surviving_determinants_nonzero else None,
                "rank_after_four_deletions": four_deletion_rank,
                "bounded_replay": bounded_replay,
                "finite_linear_aggregation_of_authorized_ports": magnetic_erasure_frame.get("finite_linear_aggregation_of_authorized_ports"),
                "source_authorizes_finite_linear_aggregation": magnetic_erasure_frame.get("source_authorizes_finite_linear_aggregation"),
                "algebraic_full_spark_implies_executable_without_aggregation_authority": magnetic_erasure_frame.get("claims_algebraic_full_spark_implies_executable_without_aggregation_authority"),
                "three_erasure_budget_tolerates_four_deletions": magnetic_erasure_frame.get("claims_three_erasure_budget_tolerates_four_deletions"),
                "theorem": "over the rational coefficient field, the 24-by-21 Vandermonde observation frame tolerates any three missing ports; executability additionally requires source authority for finite linear aggregation of the harmonic tests",
            },
            "magnetic_error_erasure_decoder_gate": {
                "code_length": decoder_length,
                "message_dimension": decoder_dimension,
                "minimum_distance": decoder_distance,
                "correctable_error_count": decoder_errors,
                "correctable_erasure_count": decoder_erasures,
                "requested_pattern_is_uniquely_decodable": decoder_correctable,
                "decoding_region": decoder_region,
                "hostile_error_count": hostile_errors,
                "hostile_erasure_count": hostile_erasures,
                "hostile_pattern_is_uniquely_decodable": hostile_correctable,
                "algebraic_decoder_is_finite_executable_algorithm": magnetic_decoder.get("algebraic_decoder_is_finite_executable_algorithm"),
                "physical_fault_model_source_authorized": magnetic_decoder.get("physical_fault_model_source_authorized"),
                "fault_location_semantics_source_authorized": magnetic_decoder.get("fault_location_semantics_source_authorized"),
                "algebraic_decoder_supplies_physical_fault_diagnosis": magnetic_decoder.get("claims_algebraic_decoder_supplies_physical_fault_diagnosis"),
                "boundary_case_is_uniquely_decodable": magnetic_decoder.get("claims_boundary_case_is_uniquely_decodable"),
                "theorem": "the exact 24-port rational Reed-Solomon frame uniquely corrects e erroneous values and s erasures precisely in the certified region 2e+s<4; this algebraic decoder does not type discrepancies as physical faults",
            },
            "magnetic_frame_conditioning_gate": {
                "frame_shape": conditioning_shape,
                "domain_norm": magnetic_conditioning.get("domain_norm"),
                "integer_monomial_condition_estimate": integer_condition,
                "scaled_monomial_condition_estimate": scaled_condition,
                "chebyshev_gauss_exact_full_condition_squared": chebyshev_condition_squared,
                "chebyshev_gauss_worst_three_deletion_condition_estimate": deletion_condition,
                "worst_three_deleted_rows": magnetic_conditioning.get("worst_three_deleted_rows"),
                "conditioning_separation_detected": conditioning_separation,
                "numerical_evidence_backend": magnetic_conditioning.get("numerical_evidence_backend"),
                "exact_full_orthogonality_identity": magnetic_conditioning.get("exact_full_orthogonality_identity"),
                "all_three_deletion_submatrices_injective": magnetic_conditioning.get("all_three_deletion_submatrices_injective"),
                "uniform_three_deletion_stability_certified": magnetic_conditioning.get("uniform_three_deletion_stability_certified"),
                "chebyshev_tests_are_continuous": magnetic_conditioning.get("chebyshev_tests_are_continuous"),
                "chebyshev_coefficients_fit_exact_rational_record_schema": magnetic_conditioning.get("chebyshev_coefficients_fit_exact_rational_record_schema"),
                "approximate_instrument_realization_source_authorized": magnetic_conditioning.get("approximate_instrument_realization_source_authorized"),
                "full_spark_implies_uniform_stability": magnetic_conditioning.get("claims_full_spark_implies_uniform_stability"),
                "continuity_implies_exact_executability": magnetic_conditioning.get("claims_continuity_implies_exact_executability"),
                "theorem": "full-spark erasure recovery and norm-stable observation are separate properties; Chebyshev-Gauss orientation stabilizes the full frame but does not certify a uniform three-deletion bound or an executable physical realization",
            },
            "magnetic_naimark_deletion_duality_gate": {
                "ambient_port_count": naimark_ports,
                "signal_dimension": naimark_signal,
                "complement_dimension": naimark_complement,
                "deleted_port_count": magnetic_naimark.get("deleted_port_count"),
                "dimensions_close": naimark_dimensions_close,
                "parseval_hypothesis_required": magnetic_naimark.get("parseval_hypothesis_required"),
                "retained_lower_frame_bound": magnetic_naimark.get("retained_lower_frame_bound"),
                "retained_condition_number": magnetic_naimark.get("retained_condition_number"),
                "injective_iff_complement_minor_invertible": magnetic_naimark.get("injective_iff_complement_minor_invertible"),
                "fixture_retained_gram_matches_parseval_deletion_identity": retained_gram == expected_retained_gram,
                "fixture_complement_minor_squared": str(fixture_complement_square),
                "fixture_retained_lower_bound": str(fixture_lower_bound),
                "fixture_condition_number": magnetic_naimark.get("expected_fixture_condition_number"),
                "small_complement_reduction_is_exact": magnetic_naimark.get("small_complement_reduction_is_exact"),
                "optimized_24_port_parseval_frame_source_authorized": magnetic_naimark.get("optimized_24_port_parseval_frame_source_authorized"),
                "complement_reduction_constructs_optimized_frame": magnetic_naimark.get("claims_complement_reduction_constructs_optimized_frame"),
                "full_frame_tightness_implies_deletion_tightness": magnetic_naimark.get("claims_full_frame_tightness_implies_deletion_tightness"),
                "theorem": "for a Parseval 24-by-21 frame, three-port deletion stability is exactly the least singular value problem for the corresponding 3-by-3 Naimark-complement minor",
            },
            "magnetic_robustness_volume_budget_gate": {
                "ambient_port_count": volume_ports,
                "complement_dimension": volume_dimension,
                "minor_count": volume_minor_count,
                "cauchy_binet_squared_minor_sum": magnetic_volume_budget.get("cauchy_binet_squared_minor_sum"),
                "average_squared_minor": str(average_squared_minor),
                "worst_squared_minor_upper_bound": str(average_squared_minor),
                "worst_sigma_min_upper_bound": magnetic_volume_budget.get("worst_sigma_min_upper_bound"),
                "worst_condition_lower_bound": magnetic_volume_budget.get("worst_condition_lower_bound"),
                "worst_condition_lower_bound_decimal": float(condition_lower_decimal),
                "hadamard_fixture_squared_minors": [str(value) for value in hadamard_squared_minors],
                "hadamard_fixture_cauchy_binet_sum": str(hadamard_cauchy_binet_sum),
                "equal_minor_energy_design_exists_source_authorized": magnetic_volume_budget.get("equal_minor_energy_design_exists_source_authorized"),
                "average_bound_is_attainable": magnetic_volume_budget.get("claims_average_bound_is_attainable"),
                "determinant_bound_classifies_conditioning": magnetic_volume_budget.get("claims_determinant_bound_classifies_conditioning"),
                "theorem": "Cauchy-Binet fixes the total squared complementary-minor volume at one, so some three-port deletion has condition number at least 2024^(1/6); this conservation bound neither constructs an optimizer nor classifies its singular spectrum",
            },
            "magnetic_plucker_equal_volume_obstruction_gate": {
                "field": magnetic_plucker.get("field"),
                "rank": magnetic_plucker.get("rank"),
                "minimum_row_count": magnetic_plucker.get("minimum_row_count"),
                "relation": magnetic_plucker.get("relation"),
                "possible_signed_three_term_sums": plucker_signed_sums,
                "zero_sum_possible": plucker_zero_possible,
                "equal_volume_real_frame_exists": plucker_equal_volume_exists,
                "compact_parseval_frame_space": magnetic_plucker.get("compact_parseval_frame_space"),
                "minimum_minor_objective_continuous": magnetic_plucker.get("minimum_minor_objective_continuous"),
                "strict_bound_follows": strict_bound_follows,
                "strict_worst_condition_bound": magnetic_plucker.get("strict_worst_condition_bound"),
                "quantitative_strict_gap_computed": magnetic_plucker.get("quantitative_strict_gap_computed"),
                "optimal_frame_constructed": magnetic_plucker.get("optimal_frame_constructed"),
                "plucker_obstruction_supplies_gap_value": magnetic_plucker.get("claims_plucker_obstruction_supplies_gap_value"),
                "theorem": "the real three-term Plucker relation forbids equal nonzero absolute 3-by-3 minors once five rows are present; compactness therefore makes the universal worst-condition bound strict, without determining the gap",
            },
            "magnetic_plucker_quantitative_gap_gate": {
                "minor_count": quantitative_minor_count,
                "minimum_squared_minor_symbol": magnetic_plucker_gap.get("minimum_squared_minor_symbol"),
                "three_term_product_lower_bound": magnetic_plucker_gap.get("three_term_product_lower_bound"),
                "forced_large_product_lower_bound": magnetic_plucker_gap.get("forced_large_product_lower_bound"),
                "forced_large_squared_minor_lower_bound": magnetic_plucker_gap.get("forced_large_squared_minor_lower_bound"),
                "cauchy_binet_total": magnetic_plucker_gap.get("cauchy_binet_total"),
                "derived_total_lower_bound": magnetic_plucker_gap.get("derived_total_lower_bound"),
                "derived_minimum_squared_minor_upper_bound": str(quantitative_minor_bound),
                "derived_worst_condition_lower_bound": magnetic_plucker_gap.get("derived_worst_condition_lower_bound"),
                "derived_worst_condition_lower_bound_decimal": float(quantitative_condition_bound),
                "improves_average_bound": quantitative_minor_bound < average_squared_minor,
                "uses_one_local_five_row_relation": magnetic_plucker_gap.get("uses_one_local_five_row_relation"),
                "global_overlap_counting_applied": magnetic_plucker_gap.get("global_overlap_counting_applied"),
                "bound_claimed_optimal": magnetic_plucker_gap.get("bound_claimed_optimal"),
                "optimized_frame_constructed": magnetic_plucker_gap.get("optimized_frame_constructed"),
                "theorem": "one five-row Plucker relation forces one squared minor to carry at least twice the minimum energy, improving the universal bound to min det(B_S)^2 <= 1/2025 and worst condition at least 2025^(1/6)",
            },
            "magnetic_global_plucker_cover_gate": {
                "row_count": cover_rows,
                "relation_count": cover_relation_count,
                "minors_per_relation": magnetic_global_cover.get("minors_per_relation"),
                "total_relation_minor_incidences": cover_total_incidences,
                "distinct_incident_minors": cover_incident_minor_count,
                "maximum_relations_witnessed_by_one_minor": cover_max_degree,
                "minimum_distinct_large_minors": cover_minimum_witnesses,
                "large_minor_squared_lower_bound": magnetic_global_cover.get("large_minor_squared_lower_bound"),
                "global_energy_lower_bound": magnetic_global_cover.get("expected_global_energy_lower_bound"),
                "derived_minimum_squared_minor_upper_bound": str(cover_minor_bound),
                "derived_worst_condition_lower_bound": magnetic_global_cover.get("derived_worst_condition_lower_bound"),
                "derived_worst_condition_lower_bound_decimal": float(cover_condition_bound),
                "cover_bound_is_exact_for_incidence_hypergraph": magnetic_global_cover.get("cover_bound_is_exact_for_incidence_hypergraph"),
                "simultaneous_plucker_feasibility_solved": magnetic_global_cover.get("simultaneous_plucker_feasibility_solved"),
                "bound_claimed_optimal_for_frames": magnetic_global_cover.get("bound_claimed_optimal_for_frames"),
                "optimized_frame_constructed": magnetic_global_cover.get("optimized_frame_constructed"),
                "theorem": "covering all 42504 canonical five-row Plucker relations requires at least 203 distinct doubled-energy minors, improving the universal squared-volume bound to 1/2227 and worst condition to at least 2227^(1/6)",
            },
            "magnetic_symmetrized_plucker_cover_gate": {
                "row_count": symmetric_rows,
                "five_subset_count": symmetric_five_sets,
                "pivot_relations_per_five_subset": magnetic_symmetric_cover.get("pivot_relations_per_five_subset"),
                "relation_count": symmetric_relation_count,
                "minors_per_relation": magnetic_symmetric_cover.get("minors_per_relation"),
                "minor_appearances_per_containing_five_subset": magnetic_symmetric_cover.get("minor_appearances_per_containing_five_subset"),
                "five_subsets_containing_one_minor": symmetric_containing_sets,
                "uniform_minor_degree": symmetric_minor_degree,
                "incidence_double_count_left": symmetric_incidence_left,
                "incidence_double_count_right": symmetric_incidence_right,
                "minimum_distinct_large_minors": symmetric_witnesses,
                "large_minor_squared_lower_bound": magnetic_symmetric_cover.get("large_minor_squared_lower_bound"),
                "global_energy_lower_bound": magnetic_symmetric_cover.get("expected_global_energy_lower_bound"),
                "derived_minimum_squared_minor_upper_bound": str(symmetric_minor_bound),
                "derived_worst_condition_lower_bound": magnetic_symmetric_cover.get("derived_worst_condition_lower_bound"),
                "derived_worst_condition_lower_bound_decimal": float(symmetric_condition_bound),
                "incidence_double_count_exact": symmetric_incidence_left == symmetric_incidence_right,
                "cover_lower_bound_attainability_established": magnetic_symmetric_cover.get("cover_lower_bound_attainability_established"),
                "simultaneous_relation_witness_assignment_solved": magnetic_symmetric_cover.get("simultaneous_relation_witness_assignment_solved"),
                "bound_claimed_optimal_for_frames": magnetic_symmetric_cover.get("bound_claimed_optimal_for_frames"),
                "theorem": "using all five pivoted Plucker relations on every five-set yields a uniform degree-630 incidence system and forces at least 338 doubled-energy minors, improving the bound to 1/2362 and worst condition to at least 2362^(1/6)",
            },
            "magnetic_plucker_energy_inequality_gate": {
                "relation_count": energy_relation_count,
                "uniform_minor_degree": energy_minor_degree,
                "local_product_law": magnetic_energy_gap.get("local_product_law"),
                "pair_square_inequality": magnetic_energy_gap.get("pair_square_inequality"),
                "product_lower_bounds": magnetic_energy_gap.get("product_lower_bounds"),
                "local_six_minor_energy_lower_bound": magnetic_energy_gap.get("local_six_minor_energy_lower_bound"),
                "global_counted_energy": magnetic_energy_gap.get("global_counted_energy"),
                "global_relation_energy_lower_bound": magnetic_energy_gap.get("global_relation_energy_lower_bound"),
                "derived_minimum_squared_minor_upper_bound": str(energy_minor_bound),
                "derived_worst_condition_lower_bound": magnetic_energy_gap.get("derived_worst_condition_lower_bound"),
                "derived_worst_condition_lower_bound_decimal": float(energy_condition_bound),
                "strictly_improves_cover_bound": energy_minor_bound < symmetric_minor_bound,
                "local_energy_bound_sharp": magnetic_energy_gap.get("local_energy_bound_sharp"),
                "global_simultaneous_equality_feasibility_established": magnetic_energy_gap.get("global_simultaneous_equality_feasibility_established"),
                "bound_claimed_optimal_for_frames": magnetic_energy_gap.get("bound_claimed_optimal_for_frames"),
                "theorem": "AM-GM upgrades each three-term Plucker relation to an eight-m local squared-energy inequality; uniform double counting yields min det(B_S)^2 <= 3/8096 and worst condition at least (8096/3)^(1/6)",
            },
            "magnetic_five_row_golden_candidate_gate": {
                "chart": magnetic_golden.get("chart"),
                "quadratic_field": magnetic_golden.get("quadratic_field"),
                "signed_plucker_coordinates_verified": golden_coordinates == golden_expected,
                "unit_magnitude_count": golden_unit_count,
                "phi_magnitude_count": golden_phi_count,
                "total_squared_energy": "10+5phi" if golden_energy == (Fraction(10), Fraction(5)) else str(golden_energy),
                "total_squared_energy_decimal": golden_energy_decimal,
                "numerical_search_best_energy_approx": magnetic_golden.get("numerical_search_best_energy_approx"),
                "numerical_search_constraint_defect_approx": magnetic_golden.get("numerical_search_constraint_defect_approx"),
                "candidate_satisfies_all_plucker_relations_exactly": magnetic_golden.get("candidate_satisfies_all_plucker_relations_exactly"),
                "candidate_alone_proves_local_minimum": magnetic_golden.get("candidate_alone_proves_local_minimum"),
                "candidate_alone_proves_global_lower_bound": magnetic_golden.get("candidate_alone_proves_global_lower_bound"),
                "numerical_search_certifies_optimality": magnetic_golden.get("claims_numerical_search_certifies_optimality"),
                "theorem": "the exact golden-ratio five-row chart supplies a feasible Plucker packet with energy 10+5phi and matches numerical minimization evidence, but it is only an upper-bound candidate for the local minimum until a proof is supplied",
            },
            "magnetic_golden_local_kkt_gate": {
                "sign_chamber": magnetic_golden_kkt.get("sign_chamber"),
                "active_nonconstant_constraints": magnetic_golden_kkt.get("active_nonconstant_constraints"),
                "active_constraint_count": kkt_active_count,
                "chart_dimension": kkt_chart_dimension,
                "critical_tangent_dimension": kkt_tangent_dimension,
                "licq_minor": "phi^2" if kkt_licq_minor == (Fraction(1), Fraction(1)) else str(kkt_licq_minor),
                "common_kkt_multiplier": magnetic_golden_kkt.get("expected_common_kkt_multiplier"),
                "all_active_multipliers_strictly_positive": kkt_positive,
                "restricted_hessian": magnetic_golden_kkt.get("expected_restricted_hessian"),
                "restricted_hessian_eigenvalues": magnetic_golden_kkt.get("expected_restricted_hessian_eigenvalues"),
                "second_order_sufficient_condition": magnetic_golden_kkt.get("second_order_sufficient_condition"),
                "strict_local_minimum_in_sign_chamber": magnetic_golden_kkt.get("strict_local_minimum_in_sign_chamber"),
                "global_minimum_proved": magnetic_golden_kkt.get("global_minimum_proved"),
                "other_sign_chambers_exhausted": magnetic_golden_kkt.get("other_sign_chambers_exhausted"),
                "local_kkt_implies_global_minimum": magnetic_golden_kkt.get("claims_local_kkt_implies_global_minimum"),
                "theorem": "the golden packet satisfies LICQ, strict complementarity, and a positive-definite critical Hessian, hence is a strict constrained local minimum in its sign chamber; the certificate alone supplies no global conclusion",
            },
            "magnetic_rank_two_sign_chamber_reduction_gate": {
                "field": magnetic_sign_reduction.get("field"),
                "rank": magnetic_sign_reduction.get("rank"),
                "column_count": magnetic_sign_reduction.get("column_count"),
                "uniform_configuration_from_minor_floor": magnetic_sign_reduction.get("uniform_configuration_from_minor_floor"),
                "separating_functional_chosen_off_finite_annihilator_union": magnetic_sign_reduction.get("separating_functional_chosen_off_finite_annihilator_union"),
                "allowed_column_operations": sign_operations,
                "positive_rescaling_used": magnetic_sign_reduction.get("positive_rescaling_used"),
                "general_linear_rescaling_used": magnetic_sign_reduction.get("general_linear_rescaling_used"),
                "all_reoriented_columns_in_one_open_halfplane": magnetic_sign_reduction.get("all_reoriented_columns_in_one_open_halfplane"),
                "slope_order_makes_all_ordered_minors_positive": magnetic_sign_reduction.get("slope_order_makes_all_ordered_minors_positive"),
                "absolute_minor_multiset_preserved": magnetic_sign_reduction.get("absolute_minor_multiset_preserved"),
                "squared_energy_preserved": magnetic_sign_reduction.get("squared_energy_preserved"),
                "all_realizable_uniform_sign_chambers_equivalent": magnetic_sign_reduction.get("all_realizable_uniform_sign_chambers_equivalent"),
                "active_constraint_patterns_classified": magnetic_sign_reduction.get("active_constraint_patterns_classified"),
                "global_minimum_proved": magnetic_sign_reduction.get("global_minimum_proved"),
                "sign_reduction_proves_golden_optimum": magnetic_sign_reduction.get("claims_sign_reduction_proves_golden_optimum"),
                "theorem": "every uniform real rank-two sign chamber is equivalent under column reorientation and permutation to the positive cyclic chamber, preserving all absolute minors and energy; active-set classification remains separate",
            },
            "magnetic_five_row_coercive_normalization_gate": {
                "homogeneous_energy_degree": magnetic_coercivity.get("homogeneous_energy_degree"),
                "homogeneous_minimum_squared_minor_degree": magnetic_coercivity.get("homogeneous_minimum_squared_minor_degree"),
                "degrees_match": coercive_homogeneous,
                "scale_invariant_objective": magnetic_coercivity.get("scale_invariant_objective"),
                "minimum_minor_nonzero": magnetic_coercivity.get("minimum_minor_nonzero"),
                "normalized_minimum_squared_minor": magnetic_coercivity.get("normalized_minimum_squared_minor"),
                "minimum_minor_relabelled_to": magnetic_coercivity.get("minimum_minor_relabelled_to"),
                "chart_denominator_nonzero": magnetic_coercivity.get("chart_denominator_nonzero"),
                "chart_variables": coercive_variables,
                "coercive_lower_bound": magnetic_coercivity.get("coercive_lower_bound"),
                "feasible_minor_inequalities_closed": magnetic_coercivity.get("feasible_minor_inequalities_closed"),
                "bounded_energy_sublevels_bounded": magnetic_coercivity.get("bounded_energy_sublevels_bounded"),
                "normalized_feasible_sublevels_compact": magnetic_coercivity.get("normalized_feasible_sublevels_compact"),
                "global_minimum_attained": magnetic_coercivity.get("global_minimum_attained"),
                "normalization_is_proof_gauge_not_port_constructor": magnetic_coercivity.get("normalization_is_proof_gauge_not_port_constructor"),
                "active_constraint_patterns_classified": magnetic_coercivity.get("active_constraint_patterns_classified"),
                "golden_global_minimum_proved": magnetic_coercivity.get("golden_global_minimum_proved"),
                "attainment_identifies_minimizer": magnetic_coercivity.get("claims_attainment_identifies_minimizer"),
                "theorem": "normalizing a nonzero minimum minor to p12=1 makes the scale-invariant five-row problem coercive with compact feasible sublevels, so a global minimizer exists; attainment alone does not identify it",
            },
            "magnetic_five_row_active_set_scout_gate": {
                "nonconstant_constraint_labels": active_labels,
                "formal_active_pattern_count": formal_active_patterns,
                "golden_active_labels": golden_active_labels,
                "golden_inactive_labels": golden_inactive_labels,
                "golden_inactive_common_value": magnetic_active_scout.get("golden_inactive_common_value"),
                "deterministic_seed": magnetic_active_scout.get("deterministic_seed"),
                "attempt_count": scout_attempts,
                "successful_feasible_convergences": scout_successes,
                "failed_or_infeasible_attempts": scout_failures,
                "attempt_accounting_closes": scout_attempts == scout_successes + scout_failures,
                "distinct_successful_active_patterns": magnetic_active_scout.get("distinct_successful_active_patterns"),
                "distinct_successful_energy_levels": magnetic_active_scout.get("distinct_successful_energy_levels"),
                "successful_energy": magnetic_active_scout.get("successful_energy"),
                "numerical_backend": magnetic_active_scout.get("numerical_backend"),
                "constraint_activity_tolerance": magnetic_active_scout.get("constraint_activity_tolerance"),
                "numerical_scout_exhausts_active_patterns": magnetic_active_scout.get("numerical_scout_exhausts_active_patterns"),
                "failed_runs_are_evidence_of_other_minima": magnetic_active_scout.get("failed_runs_are_evidence_of_other_minima"),
                "scout_proves_global_minimum": magnetic_active_scout.get("claims_scout_proves_global_minimum"),
                "theorem": "the positive chart has 512 formal active sets; a deterministic numerical scout found only the exact golden active set among 97 feasible convergences, but this is routing evidence for symbolic classification rather than an exhaustive proof",
            },
            "magnetic_golden_five_cycle_face_gate": {
                "unit_minor_graph": magnetic_cycle_face.get("unit_minor_graph"),
                "unit_cycle_edge_count": magnetic_cycle_face.get("unit_cycle_edge_count"),
                "diagonal_variables": magnetic_cycle_face.get("diagonal_variables"),
                "positive_plucker_solution": cycle_solution,
                "product_variable": magnetic_cycle_face.get("product_variable"),
                "sum_variable": magnetic_cycle_face.get("sum_variable"),
                "feasible_product_interval": magnetic_cycle_face.get("feasible_product_interval"),
                "energy_strictly_increasing_in_s_at_fixed_p": magnetic_cycle_face.get("energy_strictly_increasing_in_s_at_fixed_p"),
                "fixed_product_minimizer": magnetic_cycle_face.get("fixed_product_minimizer"),
                "one_variable": magnetic_cycle_face.get("one_variable"),
                "one_variable_interval": magnetic_cycle_face.get("one_variable_interval"),
                "diagonal_energy": magnetic_cycle_face.get("diagonal_energy"),
                "derivative_factorization": magnetic_cycle_face.get("derivative_factorization"),
                "positive_cofactor_on_interval": cycle_cofactor_positive,
                "unique_critical_point": magnetic_cycle_face.get("unique_critical_point"),
                "unique_face_minimum_energy": magnetic_cycle_face.get("unique_face_minimum_energy"),
                "golden_is_global_minimum_on_five_cycle_face": cycle_unique and magnetic_cycle_face.get("golden_is_global_minimum_on_five_cycle_face"),
                "all_other_active_graphs_excluded": magnetic_cycle_face.get("all_other_active_graphs_excluded"),
                "face_minimum_is_global_minimum": magnetic_cycle_face.get("claims_face_minimum_is_global_minimum"),
                "theorem": "on the positive five-cycle unit-minor face, Plucker relations reduce the energy to one variable whose derivative has unique zero t=phi, proving the golden packet is the unique global minimum of that face",
            },
            "magnetic_unit_minor_graph_pruning_gate": {
                "vertex_count": graph_vertex_count,
                "complete_graph_edge_count": len(graph_edges),
                "labeled_graph_count": 1 << len(graph_edges),
                "positive_plucker_crossing_pair_count": len(crossing_pairs),
                "crossing_unit_edges_forbidden": magnetic_graph_pruning.get("crossing_unit_edges_forbidden"),
                "column_scaling_stationarity_forbids_isolated_vertices": magnetic_graph_pruning.get("column_scaling_stationarity_forbids_isolated_vertices"),
                "noncrossing_vertex_cover_graph_count": len(admitted_graphs),
                "labeled_count_by_edge_count": graph_count_by_size,
                "symmetry_group": magnetic_graph_pruning.get("symmetry_group"),
                "dihedral_orbit_count": len(graph_orbits),
                "orbit_count_by_edge_count": orbit_count_by_size,
                "golden_cycle_is_one_five_edge_orbit": magnetic_graph_pruning.get("golden_cycle_is_one_five_edge_orbit"),
                "non_golden_orbit_count": len(graph_orbits) - 1,
                "all_non_golden_orbits_excluded": magnetic_graph_pruning.get("all_23_non_golden_orbits_excluded"),
                "graph_pruning_proves_global_minimum": magnetic_graph_pruning.get("claims_graph_pruning_proves_global_minimum"),
                "theorem": "positive Plucker relations forbid crossing unit edges and column-rescaling descent forbids isolated vertices, reducing 1024 labeled unit graphs to 176 and then to 24 dihedral types; 23 non-golden types remain",
            },
            "magnetic_minimal_unit_graph_face_reduction_gate": {
                "admitted_graph_order": magnetic_minimal_faces.get("admitted_graph_order"),
                "inclusion_minimal_labeled_graph_count": len(minimal_graphs),
                "minimal_labeled_count_by_edge_count": minimal_graph_count_by_size,
                "inclusion_minimal_dihedral_orbit_count": len(minimal_graph_orbits),
                "minimal_orbit_representatives": [[list(edge) for edge in graph] for graph in minimal_graph_orbits],
                "minimal_orbit_types": magnetic_minimal_faces.get("minimal_orbit_types"),
                "every_admitted_graph_contains_minimal_graph": every_graph_contains_minimal,
                "adding_unit_edges_shrinks_feasible_face": magnetic_minimal_faces.get("adding_unit_edges_shrinks_feasible_face"),
                "face_minimum_monotone_under_edge_inclusion": magnetic_minimal_faces.get("face_minimum_monotone_under_edge_inclusion"),
                "three_base_face_lower_bounds_proved": magnetic_minimal_faces.get("three_base_face_lower_bounds_proved"),
                "combinatorial_reduction_proves_global_minimum": magnetic_minimal_faces.get("claims_combinatorial_reduction_proves_global_minimum"),
                "theorem": "the 24 unit-graph types are upward closures of only three minimal dihedral faces; proving the golden lower bound on those three faces suffices for every admitted graph, but those analytic bounds remain separate",
            },
            "magnetic_two_base_face_exact_bounds_gate": {
                "star_active_coordinates": magnetic_two_faces.get("star_active_coordinates"),
                "star_remaining_chain": magnetic_two_faces.get("star_remaining_chain"),
                "star_exact_minimizer": magnetic_two_faces.get("star_exact_minimizer"),
                "star_exact_minimum_energy": magnetic_two_faces.get("star_exact_minimum_energy"),
                "adjacent_wedge_active_coordinates": magnetic_two_faces.get("adjacent_wedge_active_coordinates"),
                "adjacent_wedge_plucker_substitution": magnetic_two_faces.get("adjacent_wedge_plucker_substitution"),
                "adjacent_wedge_lower_bound_saturations": magnetic_two_faces.get("adjacent_wedge_lower_bound_saturations"),
                "adjacent_wedge_product_floor": magnetic_two_faces.get("adjacent_wedge_product_floor"),
                "adjacent_wedge_exact_minimizer": magnetic_two_faces.get("adjacent_wedge_exact_minimizer"),
                "adjacent_wedge_exact_minimum_energy": magnetic_two_faces.get("adjacent_wedge_exact_minimum_energy"),
                "adjacent_wedge_exact_minimum_energy_decimal": adjacent_wedge_energy,
                "golden_energy_decimal": golden_energy_value,
                "both_bounds_strictly_above_golden": two_face_separation,
                "separated_wedge_bound_proved": magnetic_two_faces.get("separated_wedge_bound_proved"),
                "all_three_base_faces_proved": magnetic_two_faces.get("all_three_base_faces_proved"),
                "two_faces_finish_global_theorem": magnetic_two_faces.get("claims_two_faces_finish_global_theorem"),
                "theorem": "the four-edge star has exact face minimum 24 and the adjacent-wedge plus disjoint-edge face has exact minimum 16+4sqrt2; both exceed the golden energy, leaving only the separated-wedge face",
            },
            "magnetic_global_golden_five_row_theorem_gate": {
                "separated_wedge_active_coordinates": magnetic_global_golden.get("separated_wedge_active_coordinates"),
                "separated_wedge_variables_relation": magnetic_global_golden.get("separated_wedge_variables_relation"),
                "D_descent_boundaries": magnetic_global_golden.get("D_descent_boundaries"),
                "exceptional_D_boundaries_contain_adjacent_wedge_face": magnetic_global_golden.get("exceptional_D_boundaries_contain_adjacent_wedge_face"),
                "D_equals_one_z_descent_boundaries": magnetic_global_golden.get("D_equals_one_z_descent_boundaries"),
                "z_equals_one_boundary_is_five_cycle_face": magnetic_global_golden.get("z_equals_one_boundary_is_five_cycle_face"),
                "other_z_descent_boundaries_contain_adjacent_wedge_face": magnetic_global_golden.get("other_z_descent_boundaries_contain_adjacent_wedge_face"),
                "separated_wedge_exact_minimum_energy": magnetic_global_golden.get("separated_wedge_exact_minimum_energy"),
                "all_three_base_face_bounds_proved": magnetic_global_golden.get("all_three_base_face_bounds_proved"),
                "global_five_row_energy_inequality": magnetic_global_golden.get("global_five_row_energy_inequality"),
                "equality_packet": magnetic_global_golden.get("equality_packet"),
                "five_subset_count": global_five_subset_count,
                "global_minor_appearances_in_five_subsets": global_minor_appearances,
                "global_cauchy_binet_energy": magnetic_global_golden.get("global_cauchy_binet_energy"),
                "derived_global_minimum_squared_minor_upper_bound": magnetic_global_golden.get("derived_global_minimum_squared_minor_upper_bound"),
                "derived_global_minimum_squared_minor_upper_bound_decimal": global_minor_upper_bound,
                "derived_worst_condition_lower_bound": magnetic_global_golden.get("derived_worst_condition_lower_bound"),
                "derived_worst_condition_lower_bound_decimal": global_condition_lower_bound,
                "global_bound_claimed_optimal_for_24_row_frames": magnetic_global_golden.get("global_bound_claimed_optimal_for_24_row_frames"),
                "optimized_24_row_frame_constructed": magnetic_global_golden.get("optimized_24_row_frame_constructed"),
                "theorem": "all three minimal unit-graph faces satisfy the golden five-row inequality; double counting over all five-subsets improves the universal 24-row squared-minor bound to 1/(1012(2+phi)) and worst deletion condition to at least (1012(2+phi))^(1/6)",
            },
            "magnetic_global_golden_equality_obstruction_gate": {
                "triple_count": comb(24, 3),
                "five_subset_count": comb(24, 5),
                "equality_requires_floor_triples_per_five_set": magnetic_global_equality.get("equality_requires_floor_triples_per_five_set"),
                "floor_indicator_type": magnetic_global_equality.get("floor_indicator_type"),
                "inclusion_map": magnetic_global_equality.get("inclusion_map"),
                "gram_eigenvalues": inclusion_gram_eigenvalues,
                "gram_eigenvalue_multiplicities": inclusion_gram_multiplicities,
                "all_gram_eigenvalues_positive": all(value > 0 for value in inclusion_gram_eigenvalues),
                "inclusion_map_full_column_rank": inclusion_full_rank,
                "unique_real_solution_to_constant_five_sum": magnetic_global_equality.get("unique_real_solution_to_constant_five_sum"),
                "solution_is_not_zero_one": equality_real_constant not in (0, 1),
                "global_equality_packet_exists": not equality_impossible,
                "strict_global_condition_bound": magnetic_global_equality.get("strict_global_condition_bound"),
                "quantitative_strict_gap_computed": magnetic_global_equality.get("quantitative_strict_gap_computed"),
                "optimal_24_row_frame_constructed": magnetic_global_equality.get("optimal_24_row_frame_constructed"),
                "rank_obstruction_supplies_gap_value": magnetic_global_equality.get("claims_rank_obstruction_supplies_gap_value"),
                "theorem": "global equality would require a zero-one triple coloring with five marked triples in every five-set; full column rank of W_3,5 forces the unique real solution to be the impossible constant 1/2, so the condition bound is strict without a computed gap",
            },
            "sequential_hostiles": sequence_witnesses,
            "first_missing_constructor": "source-canonical metric/reference renormalization and a closable rigged trace correspondence coupling the line to tail-seam incidence maps (B_s,C_s)",
        },
    }
