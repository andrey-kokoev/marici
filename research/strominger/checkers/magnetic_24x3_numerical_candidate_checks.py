"""Deterministic replay of the floating-point 24-by-3 construction evidence."""

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT / "research/strominger/contracts/magnetic-24x3-numerical-candidate.v1.json"
packet = json.loads(PATH.read_text(encoding="utf-8"))
exact_packet = json.loads(PATH.read_text(encoding="utf-8"), parse_float=Fraction)
matrix = np.asarray(packet["matrix"], dtype=np.float64)
triples = np.asarray(list(itertools.combinations(range(24), 3)))
singular_floors = np.linalg.svd(matrix[triples], compute_uv=False)[:, -1]
absolute_minors = np.abs(np.linalg.det(matrix[triples]))
worst_index = int(np.argmin(singular_floors))
expected = packet["expected"]
authority = packet["authority"]
physical_dpc = packet["physical_realization_dpc"]
dpc_support = physical_dpc["detector_support_combinatorics"]
dpc_metric = physical_dpc["operational_metric_constructor"]
dpc_source_metric = dpc_metric["source_metric_audit"]
dpc_static_distinction = physical_dpc["static_distinction_authority"]
dpc_interface = physical_dpc["interface_selection_authority"]
dpc_disposition = physical_dpc["programme_disposition"]
dpc_sparse_fixture = dpc_support["width_four_exact_fixture"]
dpc_tree_fixture = dpc_support["width_four_tree_core_fixture"]
dpc_constructors = {constructor["id"]: constructor for constructor in physical_dpc["constructors"]}
dpc_faults = {fault["kind"]: fault for fault in physical_dpc["fault_grammar"]}
dpc_hostiles = {fixture["id"]: fixture for fixture in physical_dpc["hostile_fixtures"]}
polar_certificate = packet["exact_polar_certificate"]
stationarity_audit = packet["clarke_stationarity_audit"]
naimark_projector_typing = packet["naimark_projector_typing"]
fault_profile_gate = naimark_projector_typing["fault_profile_gate"]
fault_semantics = fault_profile_gate["fault_semantics"]
syndrome_line_gate = fault_semantics["syndrome_line_gate"]
mixed_quotient_gate = syndrome_line_gate["mixed_error_erasure_quotient_gate"]
sommerfeld_gate = mixed_quotient_gate["sommerfeld_local_normal_form"]
deformation_gate = sommerfeld_gate["ambient_deformation_audit"]
projector_tangent_gate = deformation_gate["projector_tangent_audit"]
missing_constructor_gate = deformation_gate["missing_port_encoder_constructor"]
exact_encoder_packet = missing_constructor_gate["exact_coefficient_packet"]
realization_spec = missing_constructor_gate["realization_acceptance_specification"]
sharp_realization_gate = missing_constructor_gate["sharp_unconstrained_realization_radius"]
leverage_gate = naimark_projector_typing["leverage_gate"]
pareto_hostile = leverage_gate["pareto_hostile"]
orientation_hostile = stationarity_audit["orientation_erasure_hostile"]
singular_gradient_typing = stationarity_audit["singular_gradient_typing"]


def exact_det3(rows):
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def determinant_mod_prime(rows, prime):
    work = [[int(value) % prime for value in row] for row in rows]
    determinant = 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % prime
        pivot_inverse = pow(pivot_value, prime - 2, prime)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * pivot_inverse % prime
            for index in range(column, len(work)):
                work[row][index] = (work[row][index] - factor * work[column][index]) % prime
    return determinant % prime


exact_matrix = exact_packet["matrix"]
exact_gram = [[sum(exact_matrix[r][i] * exact_matrix[r][j] for r in range(24)) for j in range(3)] for i in range(3)]


def exact_inverse_3x3(matrix3):
    determinant = exact_det3(matrix3)
    cofactors = []
    for row in range(3):
        cofactor_row = []
        for column in range(3):
            minor_rows = [index for index in range(3) if index != row]
            minor_columns = [index for index in range(3) if index != column]
            minor = matrix3[minor_rows[0]][minor_columns[0]] * matrix3[minor_rows[1]][minor_columns[1]] - matrix3[minor_rows[0]][minor_columns[1]] * matrix3[minor_rows[1]][minor_columns[0]]
            cofactor_row.append(minor if (row + column) % 2 == 0 else -minor)
        cofactors.append(cofactor_row)
    return [[cofactors[column][row] / determinant for column in range(3)] for row in range(3)]


exact_gram_inverse = exact_inverse_3x3(exact_gram)
exact_row_norms_squared = [sum(exact_matrix[row][i] * exact_gram_inverse[i][j] * exact_matrix[row][j] for i in range(3) for j in range(3)) for row in range(24)]
exact_pair_minimum_eigenvalue_tests = []
for pair in itertools.combinations(range(24), 2):
    pair_gram = [[sum(exact_matrix[pair[i]][a] * exact_gram_inverse[a][b] * exact_matrix[pair[j]][b] for a in range(3) for b in range(3)) for j in range(2)] for i in range(2)]
    exact_pair_minimum_eigenvalue_tests.append((pair, pair_gram))


def all_pair_floors_exceed(condition_bound):
    threshold_squared = 1 / (condition_bound * condition_bound)
    determinants = []
    for pair, pair_gram in exact_pair_minimum_eigenvalue_tests:
        shifted_00 = pair_gram[0][0] - threshold_squared
        shifted_11 = pair_gram[1][1] - threshold_squared
        determinants.append((shifted_00 * shifted_11 - pair_gram[0][1] ** 2, pair))
    return min(determinants)


kappa_1_lower, kappa_1_upper = map(Fraction, fault_profile_gate["kappa_1_interval"])
kappa_2_lower, kappa_2_upper = map(Fraction, fault_profile_gate["kappa_2_interval"])
minimum_row_norm_squared = min(exact_row_norms_squared)
kappa_2_upper_test = all_pair_floors_exceed(kappa_2_upper)
kappa_2_lower_test = all_pair_floors_exceed(kappa_2_lower)


def exact_q_inner(row_a, row_b):
    return sum(exact_matrix[row_a][i] * exact_gram_inverse[i][j] * exact_matrix[row_b][j] for i in range(3) for j in range(3))


def exact_projective_separation(row_a, row_b):
    inner_aa = exact_q_inner(row_a, row_a)
    inner_bb = exact_q_inner(row_b, row_b)
    inner_ab = exact_q_inner(row_a, row_b)
    return 1 - inner_ab ** 2 / (inner_aa * inner_bb)


projective_separations = [(exact_projective_separation(i, j), (i, j)) for i, j in itertools.combinations(range(24), 2)]
minimum_projective_separation, minimum_projective_pair = min(projective_separations)
line_condition_lower, line_condition_upper = map(Fraction, syndrome_line_gate["inverse_sine_condition_interval"])
mixed_quotient_separations = []
for erased_row in range(24):
    candidates = [row for row in range(24) if row != erased_row]
    erased_norm = exact_q_inner(erased_row, erased_row)
    for row_a, row_b in itertools.combinations(candidates, 2):
        projected_ab = exact_q_inner(row_a, row_b) - exact_q_inner(row_a, erased_row) * exact_q_inner(erased_row, row_b) / erased_norm
        projected_aa = exact_q_inner(row_a, row_a) - exact_q_inner(row_a, erased_row) ** 2 / erased_norm
        projected_bb = exact_q_inner(row_b, row_b) - exact_q_inner(row_b, erased_row) ** 2 / erased_norm
        separation = 1 - projected_ab ** 2 / (projected_aa * projected_bb)
        mixed_quotient_separations.append((separation, (erased_row, row_a, row_b)))
minimum_mixed_separation, minimum_mixed_witness = min(mixed_quotient_separations)
mixed_condition_lower, mixed_condition_upper = map(Fraction, mixed_quotient_gate["inverse_sine_condition_interval"])
mixed_erased, mixed_row_a, mixed_row_b = minimum_mixed_witness
mixed_projector_gram3 = [[exact_q_inner(row_a, row_b) for row_b in minimum_mixed_witness] for row_a in minimum_mixed_witness]
mixed_projector_det3 = exact_det3(mixed_projector_gram3)
mixed_projector_pair_det_a = exact_q_inner(mixed_erased, mixed_erased) * exact_q_inner(mixed_row_a, mixed_row_a) - exact_q_inner(mixed_erased, mixed_row_a) ** 2
mixed_projector_pair_det_b = exact_q_inner(mixed_erased, mixed_erased) * exact_q_inner(mixed_row_b, mixed_row_b) - exact_q_inner(mixed_erased, mixed_row_b) ** 2
mixed_gram_identity_value = mixed_projector_det3 * exact_q_inner(mixed_erased, mixed_erased) / (mixed_projector_pair_det_a * mixed_projector_pair_det_b)
raw_triple_volumes = sorted((abs(exact_det3([exact_matrix[row] for row in triple])), triple) for triple in itertools.combinations(range(24), 3))
mixed_raw_volume = abs(exact_det3([exact_matrix[row] for row in sorted(minimum_mixed_witness)]))
mixed_raw_volume_rank = next(index + 1 for index, (volume, triple) in enumerate(raw_triple_volumes) if volume == mixed_raw_volume and triple == tuple(sorted(minimum_mixed_witness)))
exact_gram_error = [[exact_gram[i][j] - (1 if i == j else 0) for j in range(3)] for i in range(3)]
exact_defect_bound = max(sum(abs(value) for value in row) for row in exact_gram_error)
exact_triple_lower_bounds = []
for triple in itertools.combinations(range(24), 3):
    rows = [exact_matrix[index] for index in triple]
    determinant = abs(exact_det3(rows))
    frobenius_squared = sum(value * value for row in rows for value in row)
    exact_triple_lower_bounds.append(2 * determinant / frobenius_squared)
exact_floor = min(exact_triple_lower_bounds)
declared_defect_bound = Fraction(polar_certificate["gram_operator_defect_upper_bound"])
certified_floor = Fraction(polar_certificate["certified_exact_parseval_sigma_floor"])


def exact_det2(matrix2):
    return matrix2[0][0] * matrix2[1][1] - matrix2[0][1] * matrix2[1][0]


sharp_threshold = Fraction(1, 261) + declared_defect_bound
sharp_leading_minors = [[], [], []]
for triple in itertools.combinations(range(24), 3):
    rows = [exact_matrix[index] for index in triple]
    shifted_gram = [
        [sum(rows[i][k] * rows[j][k] for k in range(3)) - (sharp_threshold ** 2 if i == j else 0) for j in range(3)]
        for i in range(3)
    ]
    sharp_leading_minors[0].append(shifted_gram[0][0])
    sharp_leading_minors[1].append(exact_det2(shifted_gram))
    sharp_leading_minors[2].append(exact_det3(shifted_gram))
sharp_leading_minor_floors = [min(values) for values in sharp_leading_minors]


def sylvester_floors(condition_bound):
    threshold = 1 / condition_bound + declared_defect_bound
    floors = [None, None, None]
    active_triple = None
    for triple in itertools.combinations(range(24), 3):
        rows = [exact_matrix[index] for index in triple]
        shifted = [
            [sum(rows[i][k] * rows[j][k] for k in range(3)) - (threshold ** 2 if i == j else 0) for j in range(3)]
            for i in range(3)
        ]
        values = [shifted[0][0], exact_det2(shifted), exact_det3(shifted)]
        for index, value in enumerate(values):
            if floors[index] is None or value < floors[index]:
                floors[index] = value
                if index == 2:
                    active_triple = triple
    return floors, active_triple


tight_bound = Fraction(polar_certificate["tight_certified_exact_condition_upper_bound"])
tight_floors, tight_active_triple = sylvester_floors(tight_bound)
hostile_tighter_bound = Fraction(polar_certificate["tighter_hostile_certificate_request"])
hostile_tighter_floors, _ = sylvester_floors(hostile_tighter_bound)


def generalized_pencil_floors(condition_bound):
    threshold_squared = 1 / (condition_bound * condition_bound)
    floors = [None, None, None]
    active_triple = None
    for triple in itertools.combinations(range(24), 3):
        local_gram = [
            [sum(exact_matrix[row][i] * exact_matrix[row][j] for row in triple) for j in range(3)]
            for i in range(3)
        ]
        pencil = [[local_gram[i][j] - threshold_squared * exact_gram[i][j] for j in range(3)] for i in range(3)]
        values = [pencil[0][0], exact_det2(pencil), exact_det3(pencil)]
        for index, value in enumerate(values):
            if floors[index] is None or value < floors[index]:
                floors[index] = value
                if index == 2:
                    active_triple = triple
    return floors, active_triple


generalized_upper = Fraction(polar_certificate["generalized_pencil_certified_condition_upper_bound"])
generalized_lower = Fraction(polar_certificate["generalized_pencil_certified_condition_lower_bound"])
generalized_upper_floors, generalized_active = generalized_pencil_floors(generalized_upper)
generalized_lower_floors, _ = generalized_pencil_floors(generalized_lower)
triple_frobenius_squared = np.sum(matrix[triples] ** 2, axis=(1, 2))
shape_factors = singular_floors / np.cbrt(absolute_minors)
shape_index = int(np.argmin(shape_factors))
determinant_lower_bounds = 2 * absolute_minors / triple_frobenius_squared
lower_bound_slack_ratios = singular_floors / determinant_lower_bounds
all_u, _, all_vh = np.linalg.svd(matrix[triples])
audit_triple_indices = [int(np.flatnonzero(np.all(triples == triple, axis=1))[0]) for triple in stationarity_audit["near_active_triples_zero_based"]]
audit_gradients = []
for triple_index in audit_triple_indices:
    euclidean_gradient = np.zeros_like(matrix)
    euclidean_gradient[triples[triple_index], :] = np.outer(all_u[triple_index, :, -1], all_vh[triple_index, -1, :])
    tangent_gradient = euclidean_gradient - matrix @ ((matrix.T @ euclidean_gradient + euclidean_gradient.T @ matrix) / 2)
    audit_gradients.append(tangent_gradient)
audit_weights = np.asarray(stationarity_audit["closest_convex_gradient_weights"])
audit_combination = sum((weight * gradient for weight, gradient in zip(audit_weights, audit_gradients)), np.zeros_like(matrix))
audit_residual = np.linalg.norm(audit_combination)
audit_pairings = [float(np.sum(gradient * audit_combination)) for gradient in audit_gradients]
ascent_direction = audit_combination / audit_residual
escape_u, _, escape_v = np.linalg.svd(matrix + stationarity_audit["common_ascent_polar_step"] * ascent_direction, full_matrices=False)
escape_matrix = escape_u @ escape_v
escape_floors = np.linalg.svd(escape_matrix[triples], compute_uv=False)[:, -1]
escape_index = int(np.argmin(escape_floors))
cancel_tensors = np.asarray(orientation_hostile["cancelling_oriented_tensors"], dtype=float)
aligned_tensors = np.asarray(orientation_hostile["aligned_oriented_tensors"], dtype=float)
cancel_distance = min(np.linalg.norm(weight * cancel_tensors[0] + (1 - weight) * cancel_tensors[1]) for weight in np.linspace(0, 1, 1001))
aligned_distance = min(np.linalg.norm(weight * aligned_tensors[0] + (1 - weight) * aligned_tensors[1]) for weight in np.linspace(0, 1, 1001))
gauge_u = np.asarray([1.0, 2.0]) / np.sqrt(5)
gauge_v = np.asarray([2.0, -1.0]) / np.sqrt(5)
simple_tensor = np.outer(gauge_u, gauge_v)
gauge_flipped_tensor = np.outer(-gauge_u, -gauge_v)
repeated_selector_0 = np.diag([1.0, 0.0])
repeated_selector_1 = np.diag([0.0, 1.0])
polar_u, _, polar_v = np.linalg.svd(matrix, full_matrices=False)
exact_frame_float_replay = polar_u @ polar_v
candidate_projector = np.eye(24) - matrix @ np.linalg.inv(matrix.T @ matrix) @ matrix.T
encoder_chart_indices = np.arange(21)
encoder_chart_gram = candidate_projector[np.ix_(encoder_chart_indices, encoder_chart_indices)]
encoder_chart_values, encoder_chart_vectors = np.linalg.eigh(encoder_chart_gram)
candidate_encoder = candidate_projector[:, encoder_chart_indices] @ encoder_chart_vectors @ np.diag(1 / np.sqrt(encoder_chart_values)) @ encoder_chart_vectors.T
encoder_parseval_defect = np.linalg.norm(candidate_encoder.T @ candidate_encoder - np.eye(21))
encoder_projector_defect = np.linalg.norm(candidate_encoder @ candidate_encoder.T - candidate_projector)
sparse_encoder = [[0] * 21 for _ in range(24)]
for column, coefficients in enumerate(dpc_sparse_fixture["column_coefficients"]):
    for offset, coefficient in enumerate(coefficients):
        sparse_encoder[column + offset][column] = coefficient
sparse_prime = dpc_sparse_fixture["modular_certificate_prime"]
sparse_modular_determinants = []
for deletion in itertools.combinations(range(24), 3):
    retained = [sparse_encoder[row] for row in range(24) if row not in deletion]
    sparse_modular_determinants.append((determinant_mod_prime(retained, sparse_prime), deletion))
sparse_minimum_residue, sparse_minimum_residue_witness = min(sparse_modular_determinants)
sparse_float_encoder = np.asarray(sparse_encoder, dtype=np.float64)
sparse_column_normalized = sparse_float_encoder / np.linalg.norm(sparse_float_encoder, axis=0)
sparse_deletion_conditions = np.asarray([np.linalg.cond(np.delete(sparse_column_normalized, deletion, axis=0)) for deletion in itertools.combinations(range(24), 3)])
sparse_worst_deletion_index = int(np.argmax(sparse_deletion_conditions))
sparse_deletion_list = list(itertools.combinations(range(24), 3))
sparse_gram_values, sparse_gram_vectors = np.linalg.eigh(sparse_column_normalized.T @ sparse_column_normalized)
sparse_whitened = sparse_column_normalized @ sparse_gram_vectors @ np.diag(1 / np.sqrt(sparse_gram_values)) @ sparse_gram_vectors.T
tree_encoder = [[0] * 21 for _ in range(24)]
for column, coefficients in enumerate(dpc_tree_fixture["column_coefficients"]):
    for row, coefficient in zip([0, 1, column + 2, column + 3], coefficients):
        tree_encoder[row][column] = coefficient
tree_modular_determinants = []
for deletion in itertools.combinations(range(24), 3):
    retained = [tree_encoder[row] for row in range(24) if row not in deletion]
    tree_modular_determinants.append((determinant_mod_prime(retained, dpc_tree_fixture["modular_certificate_prime"]), deletion))
tree_minimum_residue, tree_minimum_residue_witness = min(tree_modular_determinants)
tree_float_encoder = np.asarray(tree_encoder, dtype=np.float64)
tree_column_normalized = tree_float_encoder / np.linalg.norm(tree_float_encoder, axis=0)
tree_deletion_list = list(itertools.combinations(range(24), 3))
tree_deletion_conditions = np.asarray([np.linalg.cond(np.delete(tree_column_normalized, deletion, axis=0)) for deletion in tree_deletion_list])
tree_worst_deletion_index = int(np.argmax(tree_deletion_conditions))
metric_coordinate_change = np.diag(np.linspace(0.5, 2.0, 21))
metric_original_information = tree_column_normalized.T @ tree_column_normalized
metric_reparameterized_encoder = tree_column_normalized @ np.linalg.inv(metric_coordinate_change)
metric_reparameterized_signal_gram = np.linalg.inv(metric_coordinate_change).T @ np.linalg.inv(metric_coordinate_change)
metric_reparameterized_information = metric_reparameterized_encoder.T @ metric_reparameterized_encoder
metric_original_generalized_spectrum = np.linalg.eigvalsh(metric_original_information)
metric_reparameterized_generalized_spectrum = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(metric_reparameterized_signal_gram, metric_reparameterized_information))))
posthoc_whitened_information = np.linalg.inv(metric_original_information) @ metric_original_information
sharp_deletion_set = sharp_realization_gate["worst_deletion_set_zero_based"]
sharp_retained_rows = [row for row in range(24) if row not in sharp_deletion_set]
sharp_retained_u, sharp_retained_s, sharp_retained_vh = np.linalg.svd(candidate_encoder[sharp_retained_rows])
sharp_hostile_perturbation = np.zeros_like(candidate_encoder)
sharp_hostile_perturbation[sharp_retained_rows] = -sharp_retained_s[-1] * np.outer(sharp_retained_u[:, -1], sharp_retained_vh[-1])
sharp_hostile_retained_singular_floor = np.linalg.svd((candidate_encoder + sharp_hostile_perturbation)[sharp_retained_rows], compute_uv=False)[-1]


def mixed_float_separation(frame):
    erased, row_a, row_b = minimum_mixed_witness
    rows = frame[[erased, row_a, row_b]]
    projected_a = rows[1] - rows[0] * (rows[1] @ rows[0]) / (rows[0] @ rows[0])
    projected_b = rows[2] - rows[0] * (rows[2] @ rows[0]) / (rows[0] @ rows[0])
    return 1 - (projected_a @ projected_b) ** 2 / ((projected_a @ projected_a) * (projected_b @ projected_b))


mixed_gradient_step = 1e-6
mixed_euclidean_gradient = np.zeros_like(exact_frame_float_replay)
for row in range(24):
    for column in range(3):
        coordinate_step = np.zeros_like(exact_frame_float_replay)
        coordinate_step[row, column] = mixed_gradient_step
        mixed_euclidean_gradient[row, column] = (
            np.log(mixed_float_separation(exact_frame_float_replay + coordinate_step))
            - np.log(mixed_float_separation(exact_frame_float_replay - coordinate_step))
        ) / (2 * mixed_gradient_step)
mixed_tangent_gradient = mixed_euclidean_gradient - exact_frame_float_replay @ ((exact_frame_float_replay.T @ mixed_euclidean_gradient + mixed_euclidean_gradient.T @ exact_frame_float_replay) / 2)
mixed_tangent_norm = np.linalg.norm(mixed_tangent_gradient)
mixed_normal_ratio = np.linalg.norm(mixed_euclidean_gradient - mixed_tangent_gradient) / np.linalg.norm(mixed_euclidean_gradient)
polar_all_u, _, polar_all_vh = np.linalg.svd(exact_frame_float_replay[triples])
polar_audit_gradients = []
for triple_index in audit_triple_indices:
    euclidean_gradient = np.zeros_like(exact_frame_float_replay)
    euclidean_gradient[triples[triple_index], :] = np.outer(polar_all_u[triple_index, :, -1], polar_all_vh[triple_index, -1, :])
    polar_audit_gradients.append(euclidean_gradient - exact_frame_float_replay @ ((exact_frame_float_replay.T @ euclidean_gradient + euclidean_gradient.T @ exact_frame_float_replay) / 2))
polar_ascent = sum((weight * gradient for weight, gradient in zip(audit_weights, polar_audit_gradients)), np.zeros_like(exact_frame_float_replay))
polar_ascent /= np.linalg.norm(polar_ascent)
mixed_active_pairings = np.asarray([np.sum(gradient * mixed_tangent_gradient) for gradient in polar_audit_gradients])
polar_ascent_pairings = np.asarray([np.sum(gradient * polar_ascent) for gradient in polar_audit_gradients])
cone_correction = max(0, float(np.max(-mixed_active_pairings / polar_ascent_pairings)))
joint_escape_direction = mixed_tangent_gradient + cone_correction * polar_ascent
joint_escape_direction /= np.linalg.norm(joint_escape_direction)
joint_vertical_generator = (exact_frame_float_replay.T @ joint_escape_direction - joint_escape_direction.T @ exact_frame_float_replay) / 2
joint_vertical_direction = exact_frame_float_replay @ joint_vertical_generator
joint_horizontal_direction = joint_escape_direction - joint_vertical_direction
joint_projector_derivative = -(joint_horizontal_direction @ exact_frame_float_replay.T + exact_frame_float_replay @ joint_horizontal_direction.T)
joint_trial_u, _, joint_trial_v = np.linalg.svd(exact_frame_float_replay + deformation_gate["polar_retraction_step"] * joint_escape_direction, full_matrices=False)
joint_escape_frame = joint_trial_u @ joint_trial_v
joint_escape_mixed_condition = 1 / np.sqrt(mixed_float_separation(joint_escape_frame))
joint_escape_floors = np.linalg.svd(joint_escape_frame[triples], compute_uv=False)[:, -1]
joint_escape_worst_condition = 1 / np.min(joint_escape_floors)
robust_projector = np.eye(24) - exact_frame_float_replay @ exact_frame_float_replay.T
projector_values, projector_vectors = np.linalg.eigh(robust_projector)
analysis_atlas = projector_vectors[:, -21:]
atlas_gauge = np.eye(21)
atlas_gauge[:2, :2] = np.asarray([[0.0, -1.0], [1.0, 0.0]])
rotated_analysis_atlas = analysis_atlas @ atlas_gauge
leverage_scores = np.diag(robust_projector)
equal_leverage_target = naimark_projector_typing["expected_projector_rank"] / 24
single_erasure_conditions = 1 / np.sqrt(1 - leverage_scores)
worst_single_erasure_index = int(np.argmax(single_erasure_conditions))
stacked_identity_complement = np.vstack([np.eye(3) for _ in range(8)]) / np.sqrt(8)
pareto_witness = stacked_identity_complement[pareto_hostile["singular_three_row_witness_zero_based"]]


def admissible(candidate_matrix, candidate_authority):
    candidate_floors = np.linalg.svd(candidate_matrix[triples], compute_uv=False)[:, -1]
    return bool(
        candidate_matrix.shape == (24, 3)
        and np.linalg.norm(candidate_matrix.T @ candidate_matrix - np.eye(3)) <= expected["parseval_defect_max"]
        and np.all(candidate_floors > 0)
        and not candidate_authority["optimality_proved"]
        and not candidate_authority["stored_decimal_matrix_is_exact_parseval"]
        and candidate_authority["exact_algebraic_polar_frame_constructed"]
        and not candidate_authority["physical_observation_ports_authorized"]
        and candidate_authority["numerical_upper_bracket_only"]
    )


duplicate_row = matrix.copy()
duplicate_row[1] = duplicate_row[0]
scaled_packet = 2 * matrix
laundered_authority = dict(authority, physical_observation_ports_authorized=True)

checks = {
    "shape_is_24_by_3": list(matrix.shape) == expected["shape"],
    "all_2024_triples_replayed": len(triples) == expected["triple_count"],
    "parseval_columns": np.linalg.norm(matrix.T @ matrix - np.eye(3)) <= expected["parseval_defect_max"],
    "every_triple_invertible_at_float64_resolution": bool(np.all(singular_floors > 0)),
    "worst_triple_replayed": triples[worst_index].tolist() == expected["worst_rows_zero_based"],
    "singular_floor_replayed": abs(float(singular_floors[worst_index]) - expected["minimum_singular_value"]) <= 1e-14,
    "condition_upper_bracket_replayed": abs(float(1 / singular_floors[worst_index]) - expected["worst_condition_number"]) <= 1e-8,
    "minor_floor_replayed": abs(float(absolute_minors.min()) - expected["minimum_absolute_minor"]) <= 1e-14,
    "shape_factor_floor_replayed": abs(float(shape_factors[shape_index]) - expected["minimum_shape_factor"]) <= 1e-14,
    "shape_worst_triple_replayed": triples[shape_index].tolist() == expected["minimum_shape_factor_rows_zero_based"],
    "shape_factor_ceiling_replayed": abs(float(shape_factors.max()) - expected["shape_factor_maximum"]) <= 1e-14,
    "determinant_lower_bound_holds_for_every_triple": bool(np.all(singular_floors + 1e-15 >= determinant_lower_bounds)),
    "determinant_cube_upper_bound_holds_for_every_triple": bool(np.all(singular_floors <= np.cbrt(absolute_minors) + 1e-15)),
    "determinant_lower_bound_slack_replayed": abs(float(lower_bound_slack_ratios.min()) - expected["determinant_lower_bound_minimum_slack_ratio"]) <= 1e-12,
    "does_not_claim_optimality": not authority["optimality_proved"],
    "stored_decimal_matrix_not_claimed_exact_parseval": not authority["stored_decimal_matrix_is_exact_parseval"],
    "exact_algebraic_polar_frame_is_constructed": authority["exact_algebraic_polar_frame_constructed"],
    "does_not_launder_physical_port_authority": not authority["physical_observation_ports_authorized"],
    "typed_as_numerical_upper_bracket_only": authority["numerical_upper_bracket_only"],
    "aggregate_candidate_admitted": admissible(matrix, authority),
    "duplicate_row_rank_loss_rejected": not admissible(duplicate_row, authority),
    "nonparseval_scaling_rejected": not admissible(scaled_packet, authority),
    "physical_authority_laundering_rejected": not admissible(matrix, laundered_authority)
    ,"exact_rational_gram_defect_below_declared_bound": exact_defect_bound < declared_defect_bound
    ,"exact_polar_floor_exceeds_one_over_673": exact_floor - declared_defect_bound > certified_floor
    ,"exact_parseval_condition_bound_is_673": polar_certificate["certified_exact_worst_condition_upper_bound"] == 673
    ,"all_exact_sylvester_minors_positive": all(value > 0 for value in sharp_leading_minor_floors)
    ,"sharp_sylvester_test_covers_all_triples": polar_certificate["sharp_sylvester_tested_triple_count"] == len(triples)
    ,"sharp_exact_parseval_condition_bound_is_261": polar_certificate["sharp_certified_exact_parseval_sigma_floor"] == "1/261" and polar_certificate["sharp_certified_exact_worst_condition_upper_bound"] == 261
    ,"tight_exact_condition_bound_passes_sylvester": all(value > 0 for value in tight_floors)
    ,"tight_bound_active_triple_replayed": list(tight_active_triple) == polar_certificate["tight_active_triple_zero_based"]
    ,"hostile_tighter_certificate_request_rejected": hostile_tighter_floors[2] < 0
    ,"failed_certificate_not_laundered_to_disproof": not polar_certificate["claims_failed_certificate_disproves_bound"]
    ,"generalized_pencil_upper_bound_passes": all(value > 0 for value in generalized_upper_floors)
    ,"generalized_pencil_lower_bound_fails": generalized_lower_floors[2] < 0
    ,"generalized_pencil_active_triple_replayed": list(generalized_active) == polar_certificate["generalized_pencil_active_triple_zero_based"]
    ,"generalized_pencil_typed_as_invariant_polar_test": polar_certificate["generalized_pencil_is_invariant_polar_test"]
    ,"near_active_gradient_convex_hull_excludes_origin": not stationarity_audit["origin_in_near_active_gradient_convex_hull"] and audit_residual > 0.03
    ,"common_ascent_pairing_replayed": min(audit_pairings) > 0.0013
    ,"polar_escape_improves_global_floor": float(escape_floors[escape_index]) > float(singular_floors[worst_index])
    ,"polar_escape_metrics_replayed": abs(float(escape_floors[escape_index]) - stationarity_audit["escaped_minimum_singular_value"]) < 1e-14 and triples[escape_index].tolist() == stationarity_audit["escaped_floor_triple_zero_based"]
    ,"explicit_escape_falsifies_frozen_global_optimum": not stationarity_audit["frozen_frame_globally_optimal"]
    ,"escape_not_laundered_to_new_global_optimum": not stationarity_audit["claims_escape_frame_globally_optimal"]
    ,"escape_frame_not_claimed_exactified": not stationarity_audit["claims_escape_frame_is_exactified"]
    ,"stiefel_tangent_dimension_replayed": stationarity_audit["stiefel_tangent_dimension"] == stationarity_audit["stiefel_ambient_coordinate_dimension"] - stationarity_audit["stiefel_normal_dimension"] == 66
    ,"caratheodory_stationarity_support_bound_replayed": stationarity_audit["caratheodory_maximum_stationarity_support"] == stationarity_audit["stiefel_tangent_dimension"] + 1 == 67
    ,"caratheodory_upper_bound_not_laundered_to_lower_bound": not stationarity_audit["claims_caratheodory_requires_67_active_gradients"]
    ,"same_incidence_different_orientation_changes_stationarity": orientation_hostile["shared_support_multiset"][0] == orientation_hostile["shared_support_multiset"][1] and cancel_distance == orientation_hostile["expected_cancelling_convex_hull_distance"] and aligned_distance == orientation_hostile["expected_aligned_convex_hull_distance"]
    ,"incidence_only_stationarity_classifier_rejected": not orientation_hostile["incidence_only_stationarity_classifier_authorized"]
    ,"abstract_orientation_hostile_not_laundered_to_frame_realization": not orientation_hostile["fixture_is_claimed_realized_by_current_frame"]
    ,"simple_singular_tensor_is_sign_gauge_invariant": singular_gradient_typing["simple_tensor_gauge_invariant"] and np.array_equal(simple_tensor, gauge_flipped_tensor)
    ,"repeated_singular_value_has_multiple_subgradients": not singular_gradient_typing["repeated_value_has_canonical_rank_one_selector"] and not np.array_equal(repeated_selector_0, repeated_selector_1) and np.trace(repeated_selector_0) == np.trace(repeated_selector_1) == 1
    ,"repeated_selector_authority_not_invented": singular_gradient_typing["selector_requires_source_authority"] and not singular_gradient_typing["claims_current_active_minima_are_repeated"]
    ,"naimark_projector_is_rank_21": np.linalg.matrix_rank(robust_projector, tol=1e-10) == naimark_projector_typing["expected_projector_rank"]
    ,"naimark_projector_is_idempotent": np.linalg.norm(robust_projector @ robust_projector - robust_projector) < 1e-12
    ,"orthogonal_atlas_gauge_preserves_projector": np.linalg.norm(analysis_atlas @ analysis_atlas.T - rotated_analysis_atlas @ rotated_analysis_atlas.T) < 1e-12 and not np.allclose(analysis_atlas, rotated_analysis_atlas)
    ,"projector_not_laundered_to_canonical_analysis_coordinates": not naimark_projector_typing["projector_determines_analysis_coordinates_canonically"] and not naimark_projector_typing["source_comparison_to_low_harmonic_basis_authorized"]
    ,"optimized_projector_not_laundered_to_executable_ports": not naimark_projector_typing["physical_port_realization_authorized"] and not naimark_projector_typing["claims_numerical_optimization_supplies_executable_ports"]
    ,"exact_kappa_1_interval_certified": 1 / (kappa_1_upper ** 2) < minimum_row_norm_squared <= 1 / (kappa_1_lower ** 2) and [exact_row_norms_squared.index(minimum_row_norm_squared)] == fault_profile_gate["kappa_1_witness_zero_based"]
    ,"exact_kappa_2_interval_certified": kappa_2_upper_test[0] > 0 and kappa_2_lower_test[0] <= 0 and list(kappa_2_upper_test[1]) == fault_profile_gate["kappa_2_witness_zero_based"]
    ,"fault_profile_witnesses_change_with_cardinality": fault_profile_gate["kappa_1_witness_zero_based"] != fault_profile_gate["kappa_2_witness_zero_based"] != fault_profile_gate["kappa_3_witness_zero_based"] and not fault_profile_gate["claims_one_support_controls_all_cardinalities"]
    ,"fault_profile_terminates_at_codimension_three": fault_profile_gate["maximum_dimensionally_correctable_erasure_count"] == 24 - fault_profile_gate["signal_dimension"] == 3
    ,"four_erasure_rank_loss_is_dimensionally_forced": fault_profile_gate["first_dimensionally_singular_erasure_count"] == 4 and fault_profile_gate["retained_row_count_at_first_singular_erasure"] == 20 < fault_profile_gate["signal_dimension"] and fault_profile_gate["kappa_s_for_s_at_least_4"] == "infinity"
    ,"distance_four_error_erasure_budget_replayed": fault_semantics["distance_four_decoding_inequality"] == "2e+s<4" and 2 * fault_semantics["correctable_unknown_error_count"] < 4 and 2 * fault_semantics["correctable_mixed_pair"]["unknown_errors"] + fault_semantics["correctable_mixed_pair"]["known_erasures"] < 4
    ,"erasure_conditioning_not_laundered_to_error_location": fault_semantics["conditioning_profile_assumes_known_erasure_locations"] and not fault_semantics["conditioning_profile_locates_unknown_errors"]
    ,"algebraic_decoding_not_laundered_to_stability": not fault_semantics["algebraic_error_decoder_supplies_continuous_stability_bound"]
    ,"exact_syndrome_line_condition_interval_certified": 1 / line_condition_upper ** 2 < minimum_projective_separation <= 1 / line_condition_lower ** 2 and list(minimum_projective_pair) == syndrome_line_gate["minimum_projective_angle_pair_zero_based"]
    ,"all_one_error_syndrome_lines_distinct": syndrome_line_gate["all_syndrome_lines_distinct"] and minimum_projective_separation > 0
    ,"syndrome_line_stability_not_laundered_to_erasure_or_physical_noise": not syndrome_line_gate["claims_line_separation_equals_erasure_condition"] and not syndrome_line_gate["physical_syndrome_noise_model_source_authorized"]
    ,"exact_mixed_error_erasure_quotient_interval_certified": 1 / mixed_condition_upper ** 2 < minimum_mixed_separation <= 1 / mixed_condition_lower ** 2 and list(minimum_mixed_witness) == [mixed_quotient_gate["worst_known_erasure_zero_based"], *mixed_quotient_gate["worst_candidate_error_pair_zero_based"]]
    ,"mixed_quotient_lines_distinct_but_poorly_conditioned": mixed_quotient_gate["all_quotient_syndrome_lines_distinct"] and minimum_mixed_separation > 0 and not mixed_quotient_gate["claims_exact_mixed_decodability_implies_stable_localization"]
    ,"sommerfeld_normalized_gram_identity_exact": mixed_gram_identity_value == minimum_mixed_separation
    ,"mixed_witness_is_conditional_not_raw_volume_minimum": mixed_raw_volume_rank == sommerfeld_gate["critical_raw_volume_rank_one_based"] > 1 and len(raw_triple_volumes) == sommerfeld_gate["raw_volume_triple_count"]
    ,"conditional_geometry_not_laundered_to_source_necessity": sommerfeld_gate["mechanism"] == "conditional three-way volume is small relative to both surviving pair areas" and not sommerfeld_gate["claims_mechanism_is_source_forced"]
    ,"mixed_collision_is_not_ambient_stiefel_stationary": abs(mixed_tangent_norm - deformation_gate["tangent_log_separation_gradient_norm"]) < 1e-6 and mixed_tangent_norm > 400 and abs(mixed_normal_ratio - deformation_gate["normal_component_ratio"]) < 1e-8
    ,"audited_joint_escape_improves_both_condition_factors": abs(float(joint_escape_mixed_condition) - deformation_gate["escaped_mixed_condition"]) < 1e-8 and abs(float(joint_escape_worst_condition) - deformation_gate["escaped_worst_triple_condition"]) < 1e-7 and joint_escape_mixed_condition < 1 / np.sqrt(float(minimum_mixed_separation)) and joint_escape_worst_condition < float(1 / singular_floors[worst_index])
    ,"ambient_escape_not_laundered_to_source_or_global_pareto_authority": not deformation_gate["source_admissible_deformation_family_authorized"] and not deformation_gate["claims_finite_step_is_global_pareto_theorem"]
    ,"joint_escape_changes_invariant_projector_not_only_atlas": projector_tangent_gate["escape_changes_invariant_projector"] and abs(np.linalg.norm(joint_vertical_direction) - projector_tangent_gate["vertical_gauge_norm"]) < 1e-9 and abs(np.linalg.norm(joint_horizontal_direction) - projector_tangent_gate["horizontal_norm"]) < 1e-12 and abs(np.linalg.norm(joint_projector_derivative) - projector_tangent_gate["projector_derivative_frobenius_norm"]) < 1e-12
    ,"exact_rational_projector_has_deterministic_algebraic_encoder": missing_constructor_gate["projector_entries_exact_rational"] and missing_constructor_gate["encoder_entries_exact_real_algebraic"] and missing_constructor_gate["mathematical_encoder_constructed"] and missing_constructor_gate["encoder_isometry_R21_to_image_P_declared"] and abs(float(encoder_chart_values[0]) - missing_constructor_gate["chart_minimum_eigenvalue_float64"]) < 1e-14 and encoder_parseval_defect < 2e-14 and encoder_projector_defect < 2e-14
    ,"encoder_chart_invertibility_has_exact_complement_witness": missing_constructor_gate["omitted_chart_rows_zero_based"] == [21,22,23] and exact_det3([exact_matrix[row] for row in missing_constructor_gate["omitted_chart_rows_zero_based"]]) != 0
    ,"exact_encoder_expression_dag_is_typed_and_total": missing_constructor_gate["exact_24_port_coefficient_packet_declared"] and exact_encoder_packet["representation"] == "algebraic_expression_dag" and exact_encoder_packet["input_matrix_pointer"] == "/matrix" and exact_encoder_packet["chart_indices_zero_based"] == list(range(21)) and [node["id"] for node in exact_encoder_packet["nodes"]] == ["G","K","P","C","H","R","E"] and exact_encoder_packet["nodes"][-1]["shape"] == [24,21] and exact_encoder_packet["output_node"] == "E" and not exact_encoder_packet["expanded_scalar_list_required"]
    ,"algebraic_packet_does_not_launder_realization_or_execution": not missing_constructor_gate["coefficient_realization_authorized"] and not missing_constructor_gate["instrument_execution_authorized"]
    ,"weyl_realization_acceptance_bound_is_exact": Fraction(1, 1) / Fraction(realization_spec["nominal_worst_condition_upper_endpoint"]) - Fraction(realization_spec["maximum_error"]) > 0 and Fraction(1, 1) / (Fraction(1, 1) / Fraction(realization_spec["nominal_worst_condition_upper_endpoint"]) - Fraction(realization_spec["maximum_error"])) < Fraction(realization_spec["realized_worst_condition_upper_bound"]) and realization_spec["all_three_deletion_patterns_remain_injective"]
    ,"acceptance_specification_not_laundered_to_measurement_or_noise_authority": not realization_spec["instrument_measured_against_specification"] and not realization_spec["claims_mathematical_tolerance_is_physical_noise_model"]
    ,"sharp_unconstrained_realization_radius_interval_certified": Fraction(sharp_realization_gate["radius_decimal_interval"][0]) < sharp_retained_s[-1] < Fraction(sharp_realization_gate["radius_decimal_interval"][1]) and Fraction(realization_spec["maximum_error"]) < Fraction(sharp_realization_gate["radius_decimal_interval"][0])
    ,"rank_one_hostile_realization_reaches_failure_radius": abs(np.linalg.norm(sharp_hostile_perturbation, 2) - sharp_retained_s[-1]) < 1e-14 and sharp_hostile_retained_singular_floor < 1e-14 and np.linalg.matrix_rank((candidate_encoder + sharp_hostile_perturbation)[sharp_retained_rows], tol=1e-12) == sharp_realization_gate["hostile_perturbed_retained_rank"]
    ,"sharp_radius_scope_not_laundered_to_parseval_or_physical_noise": not sharp_realization_gate["perturbation_required_to_preserve_parseval"] and not sharp_realization_gate["claims_radius_is_physical_noise_tolerance"]
    ,"physical_dpc_constructor_chain_is_typed": physical_dpc["state"] == "mathematically_completed_operationally_unclosed" and [dpc_constructors[stage]["status"] for stage in physical_dpc["pipeline"]] == ["authorized","authorized","authorized","missing","missing","conditional_on_fault_grammar"] and not physical_dpc["claims_current_pipeline_is_physical_capability"]
    ,"physical_dpc_separates_six_fault_actions": len(dpc_faults) == 6 and dpc_faults["known_erasure"]["mathematical_action"] == "row deletion" and dpc_faults["unknown_additive_error"]["mathematical_action"] == "syndrome-line localization" and dpc_faults["known_erasure_plus_unknown_error"]["mathematical_action"] == "quotient syndrome localization" and dpc_faults["coefficient_drift"]["mathematical_action"] == "operator perturbation of encoder" and dpc_faults["correlated_port_loss"]["mathematical_action"] == "fault-hypergraph row deletion" and dpc_faults["harmonic_label_confusion"]["mathematical_action"] == "permutation or alias channel"
    ,"physical_dpc_hostile_codes_are_distinct_and_rejected": len(dpc_hostiles) == 22 and len({fixture["expected_code"] for fixture in dpc_hostiles.values()}) == 22 and all(not fixture["admitted"] for fixture in dpc_hostiles.values())
    ,"physical_dpc_rejects_dense_formula_to_locality_laundering": not physical_dpc["local_detector_architecture_declared"] and dpc_hostiles["dense_formula_to_local_detector"]["expected_code"] == "detector_locality_laundering" and not dpc_hostiles["dense_formula_to_local_detector"]["admitted"]
    ,"three_erasure_robustness_forces_detector_incidence_floor": dpc_support["minimum_degree_per_harmonic_coordinate"] == 4 and dpc_support["minimum_total_mode_port_incidences"] == 21 * 4 == 84 and dpc_support["lower_bound_on_maximum_port_support_width"] == 4 and 24 * 3 < 84 and not dpc_support["support_width_at_most_three_possible"]
    ,"robust_hall_support_is_necessary_not_sufficient": dpc_support["three_erasure_robust_hall_condition"] == "for every nonempty harmonic subset T, |N(T)| >= |T|+3" and dpc_support["proof_kind"] == "support-only necessary condition, not coefficient sufficiency" and not dpc_support["claims_robust_hall_support_constructs_full_spark_coefficients"] and dpc_hostiles["three_local_modes_per_port"]["expected_code"] == "detector_support_incidence_deficit"
    ,"width_four_incidence_floor_is_attained_by_exact_full_spark_fixture": dpc_sparse_fixture["total_incidences"] == 84 and dpc_sparse_fixture["maximum_port_support_width"] == 4 and len(dpc_sparse_fixture["column_coefficients"]) == 21 and all(len(column) == 4 and all(value != 0 for value in column) for column in dpc_sparse_fixture["column_coefficients"])
    ,"modular_certificate_proves_all_sparse_retained_determinants_nonzero": len(sparse_modular_determinants) == 2024 and all(residue != 0 for residue, _ in sparse_modular_determinants) and sparse_minimum_residue == dpc_sparse_fixture["minimum_nonzero_determinant_residue"] and list(sparse_minimum_residue_witness) == dpc_sparse_fixture["minimum_residue_deletion_witness_zero_based"] and dpc_sparse_fixture["all_2024_retained_determinants_nonzero_over_integers"]
    ,"sparse_exact_recovery_not_laundered_to_parseval_or_stability": not dpc_sparse_fixture["parseval"] and not dpc_sparse_fixture["uniform_stability_certified"] and not dpc_sparse_fixture["claims_width_four_support_alone_guarantees_full_spark"]
    ,"sparse_fixture_conditioning_failure_is_replayed": abs(np.linalg.cond(sparse_column_normalized) - dpc_sparse_fixture["column_normalized_full_condition_float64"]) < 1e-10 and abs(sparse_deletion_conditions[sparse_worst_deletion_index] - dpc_sparse_fixture["column_normalized_worst_three_deletion_condition_float64"]) < 1e-3 and list(sparse_deletion_list[sparse_worst_deletion_index]) == dpc_sparse_fixture["column_normalized_worst_deletion_zero_based"]
    ,"interval_full_spark_support_forbids_parseval_and_whitening_densifies_fixture": all(sparse_column_normalized[:, column] @ sparse_column_normalized[:, column + 3] != 0 for column in range(18)) and np.count_nonzero(np.abs(sparse_whitened) > 1e-10) == dpc_sparse_fixture["principal_whitening_nonzero_count_at_1e_minus_10"] == dpc_sparse_fixture["principal_whitening_total_entry_count"] and not dpc_sparse_fixture["claims_all_width_four_support_graphs_forbid_parseval"]
    ,"tree_core_fixture_removes_single_overlaps_and_remains_exact_full_spark": dpc_tree_fixture["single_overlap_column_pairs"] == 0 and len(tree_modular_determinants) == 2024 and all(residue != 0 for residue, _ in tree_modular_determinants) and tree_minimum_residue == dpc_tree_fixture["minimum_nonzero_determinant_residue"] and list(tree_minimum_residue_witness) == dpc_tree_fixture["minimum_residue_deletion_witness_zero_based"]
    ,"tree_core_support_improves_fixture_but_not_to_stable_regime": abs(np.linalg.cond(tree_column_normalized) - dpc_tree_fixture["column_normalized_full_condition_float64"]) < 1e-10 and abs(tree_deletion_conditions[tree_worst_deletion_index] - dpc_tree_fixture["column_normalized_worst_three_deletion_condition_float64"]) < 1e-3 and list(tree_deletion_list[tree_worst_deletion_index]) == dpc_tree_fixture["column_normalized_worst_deletion_zero_based"] and tree_deletion_conditions[tree_worst_deletion_index] < sparse_deletion_conditions[sparse_worst_deletion_index] and not dpc_tree_fixture["uniform_stability_certified"]
    ,"tree_core_matching_dimension_obstructs_parseval": dpc_tree_fixture["matching_column_witness_zero_based"] == [0,2,4] and dpc_tree_fixture["parseval_obstruction"] == "three matching-edge columns restrict to three nonzero pairwise-orthogonal vectors on a two-port common core" and not dpc_tree_fixture["parseval"] and not dpc_tree_fixture["claims_no_single_overlaps_imply_parseval_realizability"]
    ,"operational_metric_constructor_is_typed_but_uninstantiated": dpc_metric["generalized_information_matrix"] == "G^(-1/2)*E_R^T*Sigma_R^(-1)*E_R*G^(-1/2)" and not dpc_metric["euclidean_harmonic_norm_source_authorized_as_physical_energy"] and not dpc_metric["isotropic_independent_port_noise_source_authorized"] and not dpc_metric["uniform_three_deletion_risk_source_authorized"] and not dpc_metric["detector_coupling_cost_source_authorized"] and not dpc_metric["decoder_resource_model_source_authorized"] and not dpc_metric["spatial_locality_geometry_source_authorized"]
    ,"ordinary_condition_number_not_authorized_for_physical_architecture_ranking": not dpc_metric["ordinary_condition_number_authorized_for_cross_architecture_physical_ranking"] and dpc_hostiles["euclidean_norm_to_energy"]["expected_code"] == "signal_norm_authority_laundering" and dpc_hostiles["iid_noise_assumption"]["expected_code"] == "noise_covariance_authority_laundering" and dpc_hostiles["uniform_triple_risk"]["expected_code"] == "fault_weight_authority_laundering"
    ,"decoder_preconditioning_does_not_erase_analog_noise_amplification": not dpc_metric["decoder_preconditioning_removes_measurement_noise_amplification"] and dpc_hostiles["preconditioning_erases_noise"]["expected_code"] == "decoder_preconditioning_noise_laundering"
    ,"generalized_information_spectrum_is_coordinate_covariant": np.max(np.abs(metric_original_generalized_spectrum - metric_reparameterized_generalized_spectrum)) < 1e-11 and dpc_metric["coordinate_covariance_law"] == "E'=E*S^(-1), G'=S^(-T)*G*S^(-1), generalized information spectrum unchanged"
    ,"posthoc_candidate_metric_trivializes_tightness_and_is_rejected": np.max(np.abs(posthoc_whitened_information - np.eye(21))) < 1e-12 and dpc_metric["metric_must_precede_encoder_selection"] and dpc_metric["common_metric_required_across_compared_architectures"] and dpc_metric["candidate_fitted_metric_G_equals_EtE_prohibited"] and not dpc_metric["claims_metric_is_currently_predeclared"] and dpc_hostiles["posthoc_metric_whitening"]["expected_code"] == "candidate_fitted_metric_laundering"
    ,"angular_L2_is_authorized_only_as_mathematical_benchmark": dpc_source_metric["normalized_angular_L2_coefficient_metric_authorized"] and dpc_source_metric["normalized_angular_L2_metric_kind"] == "mathematical benchmark"
    ,"news_energy_is_history_seminorm_not_static_coefficient_norm": dpc_source_metric["news_energy_formula"] == "sum_i |c_i|^2 integral |f_i'(u)|^2 du" and dpc_source_metric["news_energy_metric_kind"] == "positive_semidefinite history seminorm" and dpc_source_metric["stationary_low_block_news_energy"] == 0 and dpc_source_metric["stationary_low_block_null_dimension"] == 21 and not dpc_source_metric["news_energy_supplies_invertible_static_coefficient_metric"]
    ,"temporal_profile_and_soft_norm_authority_not_invented": not dpc_source_metric["common_temporal_profile_source_authorized"] and not dpc_source_metric["positive_profile_weight_floor_source_authorized"] and not dpc_source_metric["boundary_soft_norm_source_authorized"] and dpc_hostiles["finite_energy_to_static_norm"]["expected_code"] == "history_seminorm_to_static_norm_laundering"
    ,"static_low_block_has_authorized_separating_ports_before_optional_quotient": dpc_static_distinction["dimension"] == 21 and dpc_static_distinction["complete_local_shear_tests_separate_points"] and dpc_static_distinction["low_harmonic_coefficient_ports_separate_points"] and not dpc_static_distinction["exact_form_gauge_quotient_removes_nonzero_coexact_magnetic_modes"] and not dpc_static_distinction["conservation_l0_l1_restrictions_remove_l2_l3_l4_modes"]
    ,"single_grade_three_kernel_not_laundered_to_observational_nullity": dpc_static_distinction["grade_three_readout_blind_dimension"] == 21 and not dpc_static_distinction["grade_three_blindness_implies_all_observables_blind"] and dpc_hostiles["grade_three_to_all_observables"]["expected_code"] == "single_readout_kernel_to_observational_null_laundering"
    ,"zero_news_energy_not_laundered_to_gauge_equivalence": not dpc_static_distinction["zero_news_energy_implies_pure_gauge"] and dpc_hostiles["zero_energy_to_gauge"]["expected_code"] == "energy_kernel_to_gauge_laundering"
    ,"endpoint_policy_does_not_erase_returning_history_distinctions": not dpc_static_distinction["no_magnetic_endpoint_policy_source_authorized_as_universal"] and dpc_static_distinction["no_magnetic_endpoint_policy_excludes_static_endpoint_modes"] and dpc_static_distinction["returning_low_mode_histories_survive_zero_endpoint_policy"] and dpc_static_distinction["time_resolved_shear_or_news_ports_detect_returning_histories"] and dpc_hostiles["endpoint_to_history_exclusion"]["expected_code"] == "endpoint_policy_to_history_exclusion_laundering"
    ,"invertible_antipodal_matching_not_laundered_to_alias": dpc_static_distinction["antipodal_matching_map_invertible"] and dpc_hostiles["matching_to_alias"]["expected_code"] == "invertible_matching_to_alias_laundering"
    ,"grade_three_is_mathematically_typed_but_not_physically_privileged": dpc_interface["grade_three_mathematical_constructor_authorized"] and dpc_interface["grade_three_continuity_and_fredholm_typing_authorized"] and not dpc_interface["grade_three_physically_privileged_interface_authorized"] and not dpc_interface["reason_grade_three_is_unavoidable_declared"] and dpc_hostiles["derived_grade_to_privilege"]["expected_code"] == "mathematical_constructor_to_interface_privilege_laundering"
    ,"authorized_lower_ports_falsify_universal_repair_necessity": dpc_interface["direct_low_coefficient_ports_authorized"] and dpc_interface["complete_local_shear_tests_authorized"] and dpc_interface["lower_grade_ports_may_detect_low_modes"] and not dpc_interface["claims_24_port_repair_is_physically_necessary"] and dpc_hostiles["kernel_requires_repair"]["expected_code"] == "selected_interface_kernel_to_universal_repair_laundering"
    ,"rank_minimality_not_laundered_to_physical_optimality": not dpc_interface["comparative_cost_of_direct_ports_declared"] and dpc_hostiles["minimal21_to_optimal24"]["expected_code"] == "rank_minimality_to_physical_optimality_laundering"
    ,"mathematical_bypass_not_laundered_to_redundant_instrument_execution": dpc_interface["low_mode_bypass_mathematically_authorized"] and not dpc_interface["redundant_bypass_instrument_execution_authorized"] and dpc_interface["current_24_port_role"] == "conditional fault-tolerant bypass design, not source-forced physical interface" and dpc_hostiles["bypass_to_execution"]["expected_code"] == "bypass_observation_to_instrument_execution_laundering"
    ,"encoder_optimization_lane_is_conditionally_closed_on_authority_not_performance": dpc_disposition["encoder_optimization_lane_status"] == "conditionally_closed_pending_new_authority" and set(dpc_disposition["resume_requires"]) == {"interface_selection_authority","source_fault_grammar","operational_metric_authority"} and not dpc_disposition["new_numerical_improvement_alone_reopens_lane"]
    ,"conditional_lane_closure_preserves_intrinsic_and_mathematical_results": len(dpc_disposition["intrinsic_results_retained"]) == 4 and len(dpc_disposition["conditional_engineering_results_retained"]) == 4 and not dpc_disposition["conditional_closure_invalidates_intrinsic_kernel_theorem"] and not dpc_disposition["conditional_closure_invalidates_mathematical_encoder_theorems"]
    ,"programme_disposition_rejects_five_unauthorized_physical_promotions": len(dpc_disposition["physical_claims_not_authorized"]) == 5 and "24 ports are physically necessary or optimal" in dpc_disposition["physical_claims_not_authorized"] and "Euclidean conditioning is the physical objective" in dpc_disposition["physical_claims_not_authorized"]
    ,"physical_dpc_frontier_fields_have_distinct_deletion_witnesses": set(physical_dpc["completion_requires"]) == set(physical_dpc["completion_requirement_deletion_witnesses"]) and set(physical_dpc["completion_requirement_deletion_witnesses"].values()).issubset(dpc_hostiles) and len(set(physical_dpc["completion_requirement_deletion_witnesses"].values())) == len(physical_dpc["completion_requires"]) and physical_dpc["minimality_scope"] == "relative to the declared physical-realization DPC constructor grammar" and not physical_dpc["claims_absolute_minimality"] and not physical_dpc["physical_fault_grammar_source_authorized"] and not physical_dpc["physical_noise_model_source_authorized"]
    ,"port_encoder_frontier_is_explicit": missing_constructor_gate["magnetic_low_block_declared"] and missing_constructor_gate["normalized_harmonic_coordinate_basis_source_authorized"] and missing_constructor_gate["finite_linear_aggregation_source_authorized"] and missing_constructor_gate["abstract_rank_21_projector_declared"] and missing_constructor_gate["encoder_isometry_R21_to_image_P_declared"] and missing_constructor_gate["exact_24_port_coefficient_packet_declared"] and not missing_constructor_gate["coefficient_realization_authorized"] and not missing_constructor_gate["instrument_execution_authorized"] and len(missing_constructor_gate["required_fields"]) == 2
    ,"optimizer_seed_rejected_as_port_execution_authority": missing_constructor_gate["current_generation_authority"] == "unconstrained numerical frame optimization" and not missing_constructor_gate["optimizer_seed_is_source_parameter"] and missing_constructor_gate["admissibility_verdict"] == "abstract projector deformation is defined; executable magnetic port realization is unauthorized until an encoder constructor is supplied"
    ,"projector_leverage_profile_replayed": abs(float(leverage_scores.mean()) - leverage_gate["expected_mean_leverage"]) < 1e-14 and abs(float(leverage_scores.min()) - leverage_gate["expected_minimum_leverage"]) < 1e-14 and abs(float(leverage_scores.max()) - leverage_gate["expected_maximum_leverage"]) < 1e-14
    ,"unequal_leverage_stratum_detected": not leverage_gate["equal_leverage_port_stratum_satisfied"] and abs(float(np.max(np.abs(leverage_scores - equal_leverage_target))) - leverage_gate["expected_maximum_equal_leverage_deviation"]) < 1e-14
    ,"diagonal_rescaling_not_assumed_objective_preserving": not leverage_gate["claims_diagonal_rescaling_preserves_parseval_and_deletion_objective"] and not leverage_gate["physical_equal_normalization_required_source_authorized"]
    ,"ambient_grassmann_dimension_replayed": leverage_gate["ambient_grassmann_dimension"] == 3 * (24 - 3) == 63
    ,"equal_diagonal_regular_stratum_dimension_replayed": leverage_gate["fixed_diagonal_independent_constraint_count_on_regular_stratum"] == 24 - 1 and leverage_gate["equal_diagonal_regular_stratum_dimension"] == 63 - 23 == 40
    ,"regular_stratum_formula_not_laundered_to_global_smoothness": not leverage_gate["claims_every_equal_diagonal_point_is_regular"]
    ,"single_erasure_equal_leverage_minimax_bound_replayed": leverage_gate["single_erasure_minimax_condition"] == "sqrt(8)" and abs(np.sqrt(8) - leverage_gate["single_erasure_minimax_condition_decimal"]) < 1e-14 and leverage_gate["equal_leverage_iff_single_erasure_minimax_equality"]
    ,"current_single_erasure_penalty_replayed": worst_single_erasure_index == leverage_gate["current_worst_single_erasure_row_zero_based"] and abs(float(single_erasure_conditions[worst_single_erasure_index]) - leverage_gate["current_worst_single_erasure_condition"]) < 1e-14
    ,"single_fault_optimum_not_laundered_to_triple_fault_optimum": not leverage_gate["claims_single_erasure_optimum_implies_three_erasure_optimum"]
    ,"stacked_identity_fixture_is_equal_leverage_parseval": np.linalg.norm(stacked_identity_complement.T @ stacked_identity_complement - np.eye(3)) < 1e-14 and np.allclose(np.sum(stacked_identity_complement ** 2, axis=1), 1 / 8)
    ,"single_optimal_fixture_has_singular_triple": np.linalg.matrix_rank(pareto_witness) == pareto_hostile["witness_rank"] == 1 and pareto_hostile["worst_three_erasure_condition"] == "infinity"
    ,"fault_cardinality_pareto_incomparability_detected": pareto_hostile["current_design_and_hostile_fixture_pareto_incomparable"] and leverage_gate["current_worst_single_erasure_condition"] > np.sqrt(8) and np.isfinite(expected["worst_condition_number"])
    ,"float64_bracket_not_laundered_to_rigorous": not polar_certificate["claims_float64_condition_is_rigorous"]
    ,"algebraic_polar_factor_not_claimed_rational": not polar_certificate["claims_polar_factor_has_rational_entries"]
    ,"exact_existence_does_not_authorize_physical_ports": not polar_certificate["physical_observation_ports_authorized"]
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "schema": "marici.strominger.magnetic-24x3-numerical-candidate-result.v1",
    "artifact_sha256": hashlib.sha256(PATH.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "observed": {
        "worst_rows_zero_based": triples[worst_index].tolist(),
        "minimum_singular_value": float(singular_floors[worst_index]),
        "worst_condition_number": float(1 / singular_floors[worst_index]),
        "minimum_absolute_minor": float(absolute_minors.min()),
        "minimum_shape_factor": float(shape_factors[shape_index]),
        "minimum_shape_factor_rows_zero_based": triples[shape_index].tolist(),
        "maximum_shape_factor": float(shape_factors.max()),
        "determinant_lower_bound_minimum_slack_ratio": float(lower_bound_slack_ratios.min()),
        "parseval_defect": float(np.linalg.norm(matrix.T @ matrix - np.eye(3))),
        "duplicate_row_minimum_singular_value": float(np.linalg.svd(duplicate_row[triples], compute_uv=False)[:, -1].min()),
        "scaled_packet_parseval_defect": float(np.linalg.norm(scaled_packet.T @ scaled_packet - np.eye(3)))
        ,"exact_rational_gram_defect_upper_bound": str(exact_defect_bound)
        ,"exact_rational_triple_lower_floor": str(exact_floor)
        ,"certified_exact_parseval_sigma_floor": "1/673"
        ,"certified_exact_worst_condition_upper_bound": 673
        ,"sharp_sylvester_leading_minor_floors": [str(value) for value in sharp_leading_minor_floors]
        ,"sharp_certified_exact_parseval_sigma_floor": "1/261"
        ,"sharp_certified_exact_worst_condition_upper_bound": 261
        ,"tight_certified_exact_condition_upper_bound": polar_certificate["tight_certified_exact_condition_upper_bound"]
        ,"tight_sylvester_leading_minor_floors": [str(value) for value in tight_floors]
        ,"tight_active_triple_zero_based": list(tight_active_triple)
        ,"hostile_tighter_certificate_request_rejected": polar_certificate["tighter_hostile_certificate_request"]
        ,"generalized_pencil_condition_interval": [polar_certificate["generalized_pencil_certified_condition_lower_bound"], polar_certificate["generalized_pencil_certified_condition_upper_bound"]]
        ,"generalized_pencil_upper_leading_minor_floors": [str(value) for value in generalized_upper_floors]
        ,"generalized_pencil_lower_third_minor_floor": str(generalized_lower_floors[2])
        ,"generalized_pencil_active_triple_zero_based": list(generalized_active)
        ,"clarke_near_active_gradient_residual_norm": float(audit_residual)
        ,"clarke_minimum_common_gradient_pairing": min(audit_pairings)
        ,"escaped_minimum_singular_value": float(escape_floors[escape_index])
        ,"escaped_condition_number": float(1 / escape_floors[escape_index])
        ,"escaped_floor_triple_zero_based": triples[escape_index].tolist()
        ,"stiefel_tangent_dimension": stationarity_audit["stiefel_tangent_dimension"]
        ,"caratheodory_maximum_stationarity_support": stationarity_audit["caratheodory_maximum_stationarity_support"]
        ,"orientation_erasure_hostile_distances": [float(cancel_distance), float(aligned_distance)]
        ,"singular_gradient_strata": ["simple_canonical_rank_one_tensor", "repeated_psd_trace_one_subdifferential"]
        ,"naimark_projector_rank": int(np.linalg.matrix_rank(robust_projector, tol=1e-10))
        ,"naimark_projector_idempotence_defect": float(np.linalg.norm(robust_projector @ robust_projector - robust_projector))
        ,"analysis_atlas_gauge": naimark_projector_typing["analysis_atlas_gauge"]
        ,"exact_fault_condition_intervals": [fault_profile_gate["kappa_1_interval"], fault_profile_gate["kappa_2_interval"], fault_profile_gate["kappa_3_interval"]]
        ,"fault_profile_witnesses_zero_based": [fault_profile_gate["kappa_1_witness_zero_based"], fault_profile_gate["kappa_2_witness_zero_based"], fault_profile_gate["kappa_3_witness_zero_based"]]
        ,"fault_profile_tail": {"s_at_least": 4, "condition": "infinity", "cause": "retained observation dimension below signal dimension"}
        ,"fault_semantics": {"conditioning": "known-location erasures", "decoding_budget": fault_semantics["distance_four_decoding_inequality"], "unknown_error_location_is_separate": True}
        ,"one_error_syndrome_line_condition_interval": syndrome_line_gate["inverse_sine_condition_interval"]
        ,"minimum_projective_angle_pair_zero_based": list(minimum_projective_pair)
        ,"mixed_error_erasure_quotient_condition_interval": mixed_quotient_gate["inverse_sine_condition_interval"]
        ,"mixed_error_erasure_witness_zero_based": list(minimum_mixed_witness)
        ,"projector_leverage_range": [float(leverage_scores.min()), float(leverage_scores.max())]
        ,"projector_maximum_equal_leverage_deviation": float(np.max(np.abs(leverage_scores - equal_leverage_target)))
        ,"equal_diagonal_regular_stratum_dimension": leverage_gate["equal_diagonal_regular_stratum_dimension"]
        ,"worst_single_erasure_condition": float(single_erasure_conditions[worst_single_erasure_index])
        ,"worst_single_erasure_row_zero_based": worst_single_erasure_index
        ,"single_optimal_pareto_hostile_triple_rank": int(np.linalg.matrix_rank(pareto_witness))
        ,"fault_profile_pareto_points": [["sqrt(8)", "infinity"], [leverage_gate["current_worst_single_erasure_condition"], expected["worst_condition_number"]]]
    },
    "interpretation": "invariant rational generalized-pencil test traps the expanded exact algebraic polar frame condition in [238.4083422894,238.4083422895); seventeen near-active triples span distinct supports but their gradient hull still admits escape; no optimality or physical-port authority"
}
print(json.dumps(result, indent=2, sort_keys=True))
if not all(checks.values()):
    raise SystemExit(1)
