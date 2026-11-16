// Structural audit only: no proof-outcome or source-admissibility inference.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {normalizeNet} from '../../../src/conjecture-nets/model.js';
import {normalizeImplications} from '../../../src/conjecture-nets/ports.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const contractPath = 'research/strominger/contracts/persistent-seam-pe-conjecture-net.v1.json';
const load = async p => JSON.parse(await fs.readFile(path.join(root, p), 'utf8'));
const raw = await load(contractPath);
const checks = [];
const inputs = new Set([contractPath, 'src/conjecture-nets/catalog.json', 'src/conjecture-nets/model.js', 'src/conjecture-nets/ports.js', 'research/strominger/checkers/check_persistent_seam_pe_net.mjs']);
function check(name, f) { f(); checks.push(name); }
function boundaries(r) {
  const n = normalizeNet(r, contractPath);
  const by = new Map(n.nodes.map(x => [x.id, x]));
  assert.equal(by.get('persistent-seam-pe').status, 'open');
  assert.ok(n.nodes.every(x => x.outcome === null));
  assert.equal(normalizeImplications(n).rules.length, 0);
  assert.equal(r.boundary.conjecture_proved, false);
  assert.equal(r.boundary.operator_confirmation_is_evidence, false);
  assert.equal(r.boundary.parent_outcomes_changed, false);
  assert.equal(r.boundary.physical_particle_identity_established, false);
  assert.equal(r.boundary.protocol_selected, false);
  assert.ok(!by.get('persistent-seam-pe').depends_on.includes('polarity-cover-audit'));
  assert.equal(by.get('persistent-seam-observability').status, 'verified_conditional');
  assert.equal(by.get('serial-shared-coordinate-rival').status, 'verified_alternative');
  assert.deepEqual(by.get('persistent-seam-pe').raw.rivals, ['serial-shared-coordinate-rival', 'counteroriented-synchronous-rival']);
  assert.equal(by.get('counteroriented-synchronous-rival').status, 'verified_alternative');
  assert.equal(by.get('counteroriented-synchronous-rival').raw.source_binding_status, 'rejected_under_unchanged_native_forward_interface');
  assert.equal(by.get('counteroriented-native-realization').status, 'refuted_bounded_claim');
  assert.equal(by.get('seam-invariants-select-same-orientation').status, 'refuted_bounded_claim');
  assert.equal(by.get('persistent-seam-pe').raw.actionable, false);
  assert.equal(by.get('global-28-stage-pe-fibration').status, 'open');
  assert.equal(by.get('rung4-double-observation-readout').status, 'open');
  assert.equal(by.get('rung4-double-observation-readout').raw.rung_assignment_established, false);
  assert.equal(by.get('rung4-double-observation-readout').raw.physical_reality_established, false);
  assert.equal(by.get('nested-double-observation-certificate').status, 'verified_conditional');
  assert.equal(by.get('nested-double-observation-certificate').raw.serial_work, 28);
  assert.equal(by.get('nested-double-observation-certificate').raw.sequential_observation_parallel_span, 12);
  assert.equal(by.get('nested-double-observation-certificate').raw.global_28_stages_established, false);
  assert.deepEqual(by.get('rung4-double-observation-readout').depends_on, ['nested-double-observation-certificate']);
  assert.equal(r.revision, 73);
  assert.equal(r.typing_review.revision, r.revision);
  assert.equal(r.typing_review.reviewed_node_count, n.nodes.length);
  for (const key of ['scalar_to_cell_reconstruction_required', 'additive_chain_model_assumed', 'signed_parent_cell_is_finite_cutoff_operator_cell', 'native_realization_established']) assert.equal(r.typing_review[key], false);
  assert.ok(r.typing_review.transport_signature.includes('--kappa-->'));
  assert.deepEqual(r.frontier, ['f736-boundary-witness-record-graph-lift', 'f736-source-retaining-common-target-comparison', 'f736-response-cutoff-joint-graph-instantiation', 'f736-physical-spectral-diagonal-pv-normalization', 'pb208-retained-native-construction', 'f736-observer-closure-audit', 'esd7-channel-attachment-construction']);
  assert.equal(r.recommended_start, r.frontier[0]);
  assert.ok(r.frontier_reason);
  assert.equal(r.maintenance.research_target, 'assembler-as-global-evolution');
  assert.ok(r.maintenance.recommendation_origin.includes('Maintainer-proposed'));
  for (const id of r.frontier) {
    const task = by.get(id);
    assert.equal(task.status, 'open'); assert.equal(task.raw.actionable, true);
    assert.ok(task.raw.next_action && task.raw.acceptance && task.raw.deliverable);
    assert.ok(task.depends_on.every(p => ['source_located', 'verified_conditional'].includes(by.get(p).status)));
  }
  for (const node of by.values()) {
    assert.ok((node.raw.related_nodes ?? []).every(id => by.has(id)));
  }
  for (const id of ['native-intrinsic-selector-audit', 'native-task-selector-audit', 'scalar-global-fcc-candidate']) {
    assert.equal(by.get(id).status, 'refuted_bounded_claim');
    assert.equal(by.get(id).raw.actionable, false);
    assert.ok(!by.get('channel-contract-and-first-assembly-step').depends_on.includes(id));
  }
  assert.equal(by.get('scalar-global-fcc-candidate').raw.native_endpoint_match, false);
  assert.equal(by.get('scalar-global-fcc-candidate').raw.global_conjecture_refuted, false);
  const sewing = by.get('native-joint-field-assembly-sewing');
  assert.equal(sewing.status, 'verified_conditional');
  assert.equal(sewing.raw.all_assemblies_established, false);
  assert.equal(sewing.raw.global_clock_established, false);
  const assembly = by.get('single-channel-esd7-assembly');
  assert.equal(assembly.status, 'open'); assert.equal(assembly.raw.proposal_origin, 'operator');
  assert.equal(assembly.raw.reconstruction_established, false);
  const channel = by.get('channel-contract-and-first-assembly-step');
  assert.equal(channel.status, 'verified_conditional');
  assert.equal(channel.raw.actionable, false);
  assert.equal(channel.raw.record_count, 23);
  assert.equal(channel.raw.channel_checks, 20);
  assert.equal(channel.raw.reconstructed_field_checks, 18);
  assert.equal(channel.raw.full114_channel_established, false);
  assert.equal(channel.raw.full_esd7_established, false);
  const geometry = by.get('esd7-generated-geometric-channel');
  assert.equal(geometry.status, 'verified_conditional');
  assert.equal(geometry.raw.geometric_reconstruction_established, true);
  assert.equal(geometry.raw.record_count, 345);
  for (const key of ['full114_channel_established', 'analytical_coherence_discharged', 'global_field_transport_established']) assert.equal(geometry.raw[key], false);
  const bridge = by.get('esd7-analytical-prototype-bridge');
  assert.equal(bridge.status, 'verified_conditional');
  assert.equal(bridge.raw.registry_bridge_established, true);
  assert.equal(bridge.raw.mixed_role_shared_faces, 294);
  for (const key of ['full114_channel_established', 'analytical_coherence_discharged', 'global_field_transport_established']) assert.equal(bridge.raw[key], false);
  const gate = by.get('esd7-retained-face-comparison-gate');
  assert.equal(gate.status, 'verified_conditional');
  assert.equal(gate.raw.implementation_checks, 12);
  assert.equal(gate.raw.actual_face_comparison_established, false);
  assert.equal(gate.raw.actual_face_status, 'blocked_missing_source_bound_payload');
  assert.equal(gate.raw.synthetic_controls_only, true);
  assert.equal(gate.raw.analytical_coherence_discharged, false);
  assert.equal(gate.raw.global_field_transport_established, false);
  const shortcut = by.get('esd7-bare-parent-chart-substitution');
  assert.equal(shortcut.status, 'refuted_bounded_claim');
  assert.equal(shortcut.raw.conflicting_vertices, 116);
  assert.equal(shortcut.raw.refinement_impossible, false);
  assert.equal(shortcut.raw.actual_face_comparison_established, false);
  for (const id of r.frontier) assert.ok(!by.get(id).depends_on.includes(shortcut.id));
  const refinement = by.get('esd7-simplicial-fine-vertex-refinement');
  assert.equal(refinement.status, 'verified_conditional');
  assert.equal(refinement.raw.structural_refinement_established, true);
  assert.equal(refinement.raw.cell_count, 1807);
  assert.equal(refinement.raw.implementation_checks, 20);
  for (const key of ['analytical_realization_established', 'actual_face_comparison_established', 'full114_channel_established']) assert.equal(refinement.raw[key], false);
  const evaluation = by.get('esd7-strict-parent-evaluation');
  assert.equal(evaluation.status, 'verified_conditional');
  assert.equal(evaluation.raw.conditional_strict_evaluation_established, true);
  assert.equal(evaluation.raw.implementation_checks, 21);
  for (const key of ['source_identities_freshly_proved', 'intended_witness_binding_established', 'native44_transport_binding_established', 'completion_extension_established', 'full114_channel_established']) assert.equal(evaluation.raw[key], false);
  const comparison = by.get('strict-native-witness-comparison');
  assert.equal(comparison.status, 'verified_conditional');
  assert.equal(comparison.raw.implementation_checks, 14);
  assert.equal(comparison.raw.native_pairwise_comparisons, 196);
  for (const key of ['encoder_supplied', 'intended_witness_binding_established', 'full_esd7_native_transport_established', 'full114_channel_established']) assert.equal(comparison.raw[key], false);
  const encoder = by.get('finite-observer-encoder-candidate');
  assert.equal(encoder.status, 'verified_conditional');
  assert.equal(encoder.raw.explicit_finite_packet_encoder_constructed, true);
  assert.equal(encoder.raw.packet_dimension, 5); assert.equal(encoder.raw.implementation_checks, 17);
  for (const key of ['source_forced_or_unique', 'full_observer_domain_encoded', 'specific_analytical_residual_evaluated', 'intended_witness_binding_established', 'physical_preparation_established', 'full114_channel_established']) assert.equal(encoder.raw[key], false);
  const endpoint = by.get('finite-packet-signed-endpoint-form');
  assert.equal(endpoint.status, 'verified_conditional');
  assert.equal(endpoint.raw.specific_endpoint_term_evaluated, true);
  assert.equal(endpoint.raw.implementation_checks, 18); assert.deepEqual(endpoint.raw.signature, [1,1,3]);
  for (const key of ['full_regulated_residual_evaluated', 'analytical_face_homotopy_established', 'positivity_established', 'physical_readout_established', 'full114_channel_established']) assert.equal(endpoint.raw[key], false);
  const trace = by.get('finite-packet-green-trace-subproblem');
  assert.equal(trace.status, 'verified_conditional');
  assert.equal(trace.raw.source_trace_subproblem_evaluated, true); assert.equal(trace.raw.implementation_checks, 17);
  for (const key of ['full_physical_mixed_polarization_identified', 'physical_cutoff_residual_evaluated', 'analytical_face_homotopy_established', 'physical_probe_protocol_established', 'full114_channel_established']) assert.equal(trace.raw[key], false);
  const placement = by.get('corrected-cutoff-observer-legs');
  assert.equal(placement.status, 'verified_conditional'); assert.equal(placement.raw.implementation_checks, 12);
  assert.equal(placement.raw.corrected_finite_identity_verified, true);
  assert.equal(placement.raw.full_physical_cutoff_evaluated, false); assert.equal(placement.raw.packet_cutoff_residual_evaluated, false);
  const rewrite = by.get('cutoff-leg-cyclicity-shortcut');
  assert.equal(rewrite.status, 'refuted_bounded_claim');
  assert.equal(rewrite.raw.source_unitary_transport_refuted, false); assert.equal(rewrite.raw.global_conjecture_refuted, false);
  for (const id of r.frontier) assert.ok(!by.get(id).depends_on.includes('cutoff-leg-cyclicity-shortcut'));
  const cutoff = by.get('archimedean-physical-cutoff-enclosures');
  assert.equal(cutoff.status, 'verified_conditional'); assert.equal(cutoff.raw.implementation_checks, 23);
  assert.equal(cutoff.raw.physical_off_diagonal_entries_enclosed, true);
  assert.equal(cutoff.raw.off_diagonal_entries, 20); assert.equal(cutoff.raw.finite_enclosures, 60);
  for (const key of ['complete_packet_matrix_evaluated', 'diagonal_finite_part_evaluated', 'all_semilocal_sectors_established', 'full_analytical_filler_established', 'full114_channel_established']) assert.equal(cutoff.raw[key], false);
  const centered = by.get('archimedean-centered-packet-limit');
  assert.equal(centered.status, 'verified_conditional'); assert.equal(centered.raw.implementation_checks, 19);
  assert.equal(centered.raw.diagonal_finite_part_represented, true); assert.equal(centered.raw.centered_packet_matrix_limit_controlled, true);
  for (const key of ['numerical_finite_part_value_computed', 'positivity_established', 'all_semilocal_sectors_established', 'analytical_higher_witness_established', 'full114_channel_established']) assert.equal(centered.raw[key], false);
  const batch = by.get('native-retained-joint-attachment-attempt');
  assert.equal(batch.status, 'verified_conditional'); assert.equal(batch.raw.implementation_checks, 15);
  assert.equal(batch.raw.concrete_native_attempt, true); assert.equal(batch.raw.minimal_joint_conflict_recorded, true);
  for (const key of ['full_pb_construction_established', 'physical_selection_established', 'whole_assembly_presentation_refuted']) assert.equal(batch.raw[key], false);
  const readerComparison = by.get('native-ne-nn-reader-comparison');
  assert.equal(readerComparison.status, 'verified_conditional'); assert.equal(readerComparison.raw.implementation_checks, 12);
  assert.equal(readerComparison.raw.full_coefficient_comparison_established, true);
  for (const key of ['native_cross_species_arrow_established', 'current_composition_readout_preserved', 'active_reader_only_factorization', 'whole_assembly_interpretation_refuted', 'full_pb_construction_established']) assert.equal(readerComparison.raw[key], false);
  const inventoryAttempt = by.get('pb208-inventory-fibration-attempt');
  assert.equal(inventoryAttempt.status, 'refuted_bounded_claim'); assert.equal(inventoryAttempt.raw.registration_before_execution, true);
  assert.equal(inventoryAttempt.raw.inventory_bridge_established, false); assert.equal(inventoryAttempt.raw.actionable, false);
  assert.equal(inventoryAttempt.raw.criterion_disposition, 'candidate-insufficient-for-inventory-bridge'); assert.equal(inventoryAttempt.raw.implementation_checks, 22);
  for (const key of ['generic_fibration_refuted', 'all_whole_assembly_models_refuted', 'full_pb_construction_established']) assert.equal(inventoryAttempt.raw[key], false);
  const wholeAttempt = by.get('pb208-native-whole-fixture-attempt');
  assert.equal(wholeAttempt.status, 'refuted_bounded_claim'); assert.equal(wholeAttempt.raw.registration_before_execution, true);
  assert.equal(wholeAttempt.raw.pair_binding_established, false); assert.equal(wholeAttempt.raw.actionable, false);
  assert.equal(wholeAttempt.raw.inventory_criterion_passed, true); assert.equal(wholeAttempt.raw.implementation_checks, 9);
  assert.equal(wholeAttempt.raw.criterion_disposition, 'inventory-grounded-but-pair-not-admitted');
  assert.equal(wholeAttempt.raw.root_frames_checked, 7); assert.equal(wholeAttempt.raw.prefix_bindings, 5);
  assert.equal(wholeAttempt.raw.electron_bindings, 2); assert.equal(wholeAttempt.raw.neutron_bindings, 0);
  for (const key of ['full_pb_construction_established', 'all_whole_assembly_models_refuted']) assert.equal(wholeAttempt.raw[key], false);
  const atlasAttempt = by.get('pb208-octahedral-reader-atlas-attempt');
  assert.equal(atlasAttempt.status, 'refuted_bounded_claim'); assert.equal(atlasAttempt.raw.registration_before_execution, true); assert.equal(atlasAttempt.raw.external_port_established, false);
  assert.equal(atlasAttempt.raw.actionable, false); assert.equal(atlasAttempt.raw.implementation_checks, 9);
  assert.equal(atlasAttempt.raw.reader_states, 8); assert.equal(atlasAttempt.raw.native_transitions, 16);
  assert.equal(atlasAttempt.raw.source_invariant_established, true);
  assert.equal(atlasAttempt.raw.criterion_disposition, 'no-external-port-under-fixed-root-N-only-rules');
  for (const key of ['all_native_routes_excluded', 'whole_neutron_admission_established', 'absolute_histories_identified']) assert.equal(atlasAttempt.raw[key], false);
  const screwAttempt = by.get('pb208-screw-field-attempt');
  assert.equal(screwAttempt.status, 'verified_conditional'); assert.equal(screwAttempt.raw.registration_before_execution, true); assert.equal(screwAttempt.raw.screw_field_sewing_established, true);
  assert.equal(screwAttempt.raw.actionable, false); assert.equal(screwAttempt.raw.implementation_checks, 19);
  assert.equal(screwAttempt.raw.packet_count, 66); assert.equal(screwAttempt.raw.interface_count, 95); assert.equal(screwAttempt.raw.body_count, 24);
  for (const key of ['actual_esd7_face_binding_established', 'full_pb_construction_established', 'infinite_retained_extension_established']) assert.equal(screwAttempt.raw[key], false);
  const attachment = by.get('screw-esd7-geometric-attachment-attempt');
  assert.equal(attachment.status, 'refuted_bounded_claim'); assert.equal(attachment.raw.registration_before_execution, true); assert.equal(attachment.raw.geometric_attachment_established, false);
  assert.equal(attachment.raw.actionable, false); assert.equal(attachment.raw.implementation_checks, 11);
  assert.equal(attachment.raw.occupied_primitive_embeddings, 40); assert.equal(attachment.raw.minimum_external_reference_vertices, 1);
  for (const key of ['all_geometric_embeddings_excluded', 'coherence_presentation_interpretation_refuted', 'actual_analytical_face_binding_established', 'full_pb_construction_established']) assert.equal(attachment.raw[key], false);
  const relative = by.get('screw-esd7-relative-attachment-attempt');
  assert.equal(relative.status, 'verified_conditional'); assert.equal(relative.raw.registration_before_execution, true); assert.equal(relative.raw.relative_native_attachment_established, true); assert.equal(relative.raw.actionable, false);
  assert.equal(relative.raw.implementation_checks, 10); assert.equal(relative.raw.occupied_cells, 24); assert.equal(relative.raw.retained_packets, 66); assert.equal(relative.raw.validated_interfaces, 95);
  assert.equal(relative.raw.external_reference_vertices, 1); assert.equal(relative.raw.generated_reference_only_cells, 1);
  for (const key of ['analytical_domain_extension_established', 'actual_f006_binding_established', 'full_pb_construction_established']) assert.equal(relative.raw[key], false);
  const c0trace = by.get('external-c0-finite-trace-attempt');
  assert.equal(c0trace.status, 'verified_conditional'); assert.equal(c0trace.raw.registration_before_execution, true); assert.equal(c0trace.raw.finite_c0_trace_binding_established, true); assert.equal(c0trace.raw.actionable, false);
  assert.equal(c0trace.raw.implementation_checks, 109); assert.equal(c0trace.raw.encoded_presentations, 66); assert.equal(c0trace.raw.native_interfaces, 95); assert.deepEqual(c0trace.raw.matching_calibrated_flux_indices, [1]);
  for (const key of ['endpoint_only_sufficient', 'encoder_refitted', 'analytical_domain_extension_established', 'actual_f006_binding_established', 'full_pb_construction_established']) assert.equal(c0trace.raw[key], false);
  const fineFace = by.get('native-ne-fine-face-attempt');
  assert.equal(fineFace.status, 'verified_conditional'); assert.equal(fineFace.raw.registration_before_execution, true); assert.equal(fineFace.raw.native_fine_face_identity_established, true); assert.equal(fineFace.raw.actionable, false);
  assert.equal(fineFace.raw.implementation_checks, 13); assert.equal(fineFace.raw.primitive_matches, 343); assert.equal(fineFace.raw.face, 'F736');
  assert.deepEqual(fineFace.raw.incident_tetrahedra, ['T325','T324']); assert.deepEqual(fineFace.raw.local_roles, ['H134','H134']); assert.deepEqual(fineFace.raw.shared_edge_route, ['E514','E539']); assert.equal(fineFace.raw.direct_edge, 'E515');
  for (const key of ['analytical_face_comparison_established', 'analytical_homotopy_established', 'full_pb_construction_established']) assert.equal(fineFace.raw[key], false);
  const physicalF736 = by.get('f736-physical-readout-attempt');
  assert.equal(physicalF736.status, 'verified_conditional'); assert.equal(physicalF736.raw.registration_before_execution, true); assert.equal(physicalF736.raw.physical_readout_comparison_established, true); assert.equal(physicalF736.raw.actionable, false);
  assert.equal(physicalF736.raw.implementation_checks, 47); assert.equal(physicalF736.raw.enclosed_physical_entries, 75); assert.equal(physicalF736.raw.native_matrix_unit_squares, 25); assert.deepEqual(physicalF736.raw.cutoffs, [2,4,8]);
  for (const key of ['fine_edge_operators_supplied', 'hardy_reference_identification_established', 'analytical_face_filler_established', 'all_semilocal_sectors_established', 'full_pb_construction_established']) assert.equal(physicalF736.raw[key], false);
  const wordEdges = by.get('f736-correlated-word-edges-attempt');
  assert.equal(wordEdges.status, 'verified_conditional'); assert.equal(wordEdges.raw.registration_before_execution, true); assert.equal(wordEdges.raw.conditional_fine_edge_realization_established, true); assert.equal(wordEdges.raw.actionable, false);
  assert.equal(wordEdges.raw.implementation_checks, 31); assert.equal(wordEdges.raw.oriented_component_maps, 42); assert.equal(wordEdges.raw.route_squares, 14); assert.equal(wordEdges.raw.adjacent_occurrence_squares, 36);
  assert.equal(wordEdges.raw.flattened_program_composition_rejected, true); assert.equal(wordEdges.raw.nondegenerate_component_role, 'H234'); assert.equal(wordEdges.raw.nondegenerate_occurrence, 5);
  for (const key of ['intended_homotopy_binding_established', 'completion_extension_established', 'full_pb_construction_established']) assert.equal(wordEdges.raw[key], false);
  for (const id of ['prior-local-logarithmic-operator-lift', 'prior-observer-faithful-h234-recovery', 'prior-signed-asymptotic-h234-filler', 'prior-signed-esd7-analytical-propagation', 'prior-signed-mixed-horn-naturality', 'prior-internal-positive-h134-derived-face', 'prior-represented-spectral-reverse-constructors', 'prior-faithful-response-reverse-constructors', 'prior-complete-response-retract-and-endpoints', 'prior-exact-physical-hardy-regulator-transport', 'prior-eight-leg-ordered-placement-witness', 'prior-corrected-hardy-placement-limit', 'prior-residual-augmented-interchange-prototypes', 'prior-coupled-h134-h234-signed-horn', 'prior-internal-common-face-gram-construction', 'prior-hadamard-physical-cross-feature', 'prior-combined-endpoint-schur-douglas-criterion', 'prior-common-bulk-polarity-successor-coherence', 'prior-paired-path-horn-bottom-constructor', 'prior-retained-tetrahedral-package-recovery', 'prior-supplied-bottom-dependent-pair-agreement', 'prior-forced-signed-completion-structured-lift-reduction', 'prior-fixed-boundary-tetrahedron-presentation-equivalence', 'prior-paired-completion-presentation-transport', 'prior-common-strip-core-polarized-green-comparison', 'prior-compact-support-weil-form-closure', 'prior-complete-hermitian-presentation-endpoint-isometry', 'prior-source-backed-segmentwise-h123-triangulations', 'prior-observer-valued-c14-analytical-path', 'prior-source-reached-augmented-graph-universal-property', 'prior-complete-chart-form-operator-feature-transport', 'prior-rank-two-endpoint-preserving-core-approximation', 'prior-rapid-remainder-bounded-packet-pullback', 'prior-source-rooted-cech-form-tetrahedron', 'prior-joint-source-graph-successor-equivariance', 'prior-source-star-generated-kernel-dagger', 'prior-joint-source-polarity-relation-and-promotion-criterion', 'prior-generated-dagger-ambient-extension-criterion', 'prior-reciprocal-adjoint-mate-cone-cell', 'prior-inverse-right-adjoint-compositor-mate', 'prior-relative-feature-target-and-boundary-evaluation', 'prior-plancherel-volume-cutoff-cocycle', 'prior-labelled-continuous-joint-graph-complementation', 'prior-cfp-bounded-response-faithful-graph-example', 'prior-archimedean-fixed-cutoff-trace-continuity', 'prior-regular-schwartz-kernel-trace-class-continuity', 'prior-trace-class-transported-regulator-removal', 'prior-bounded-polarized-response-trace-class-linearization', 'prior-intrinsic-four-function-response-continuity', 'prior-weighted-second-order-complete-trace-domain', 'prior-exact-four-function-fourier-response-action', 'prior-trivial-sector-finite-prime-tate-compression', 'prior-corrected-unitary-gamma-fourier-scale', 'prior-subtracted-gamma-shift-graph-construction', 'derived-frozen-diagonal-even-tate-normalization-match', 'derived-one-sector-compact-test-tate-comparison', 'derived-one-sector-rapid-scalar-cutoff-family', 'prior-convolution-observation-common-graph-domain', 'derived-one-sector-retained-carrier-and-word-diagram', 'prior-typed-tetrahedral-presentation-defect-identity', 'prior-rigged-residual-attachment-witness-graph-lift', 'prior-prepared-euler-endpoint-residual-output-equivalence', 'prior-relative-tower-universal-stable-cone-enhancement', 'derived-centered-cutoff-relative-reference-calibration', 'prior-regulated-h124-cutoff-volume-feature', 'prior-signed-defect-augmented-hermitian-comparison', 'prior-relative-rigged-source-successor-square', 'prior-exact-recentered-relative-difference-feature', 'prior-semilocal-fourier-canonical-dual-cutoff-square', 'derived-finite-cutoff-step-left-placement-defect', 'derived-one-sector-label-dilation-response-square', 'derived-f736-finite-packet-native-word-retained-grid', 'derived-retained-rapid-readout-comparison-on-grid']) {
    const imported = by.get(id);
    assert.equal(imported.status, 'verified_conditional'); assert.equal(imported.outcome, null);
    assert.ok(imported.raw.hypotheses.length); assert.ok(imported.raw.evidence.length); assert.ok(imported.raw.verification_basis);
    assert.equal(imported.raw.f736_binding_established, false); assert.equal(imported.raw.actionable, false);
  }
  assert.equal(by.get('prior-signed-asymptotic-h234-filler').raw.analytical_representative_available, true);
  assert.equal(by.get('prior-signed-asymptotic-h234-filler').raw.finite_cutoff_equality_established, false);
  const parentFace = by.get('prior-signed-asymptotic-h234-filler').raw;
  assert.deepEqual(parentFace.parent_signature, {objects: ['Q2:Obs_S->Herm', 'Q3:Obs_S->Herm', 'Q4:Obs_S->Herm'], arrows: ['eta23:Q2=>Q3', 'eta34:Q3=>Q4', 'eta24:Q2=>Q4'], modification: 'H234:eta34 eta23==>eta24'});
  assert.equal(parentFace.finite_representative_is_automatically_an_operator_2_cell, false);
  assert.equal(by.get('prior-complete-hermitian-presentation-endpoint-isometry').raw.representative_bearing_modification_enhancement_automatic, false);
  assert.equal(by.get('prior-source-backed-segmentwise-h123-triangulations').raw.stagewise_cell_signature, 'H123[r]:C23[r] C12[r]==>C13[r]');
  assert.equal(by.get('prior-internal-positive-h134-derived-face').raw.external_green_identification_established, false);
  for (const key of ['scalar_trace_inverse_established', 'augmented_hilbert_inverse_established']) assert.equal(by.get('prior-faithful-response-reverse-constructors').raw[key], false);
  assert.equal(by.get('prior-eight-leg-ordered-placement-witness').raw.finite_skew_erased, false);
  for (const key of ['rapid_decay_rate_established_by_this_argument', 'all_path_simultaneous_limit_established']) assert.equal(by.get('prior-corrected-hardy-placement-limit').raw[key], false);
  assert.equal(by.get('prior-exact-physical-hardy-regulator-transport').raw.native_reference_identification_established, false);
  assert.equal(by.get('prior-internal-common-face-gram-construction').raw.internal_common_gram_identity_established, true);
  assert.equal(by.get('prior-internal-common-face-gram-construction').raw.external_physical_identification_established, false);
  assert.equal(by.get('prior-hadamard-physical-cross-feature').raw.external_volume_row_identification_established, false);
  assert.equal(by.get('prior-hadamard-physical-cross-feature').raw.finite_skew_erased, false);
  assert.equal(by.get('prior-combined-endpoint-schur-douglas-criterion').raw.physical_schur_bound_established, false);
  assert.equal(by.get('prior-common-bulk-polarity-successor-coherence').raw.dyadic_positive_accretion_established, false);
  assert.equal(by.get('prior-paired-path-horn-bottom-constructor').raw.paired_bottom_and_filler_constructor_available, true);
  assert.equal(by.get('prior-paired-path-horn-bottom-constructor').raw.arbitrary_fixed_surface_fillability_established, false);
  assert.equal(by.get('prior-retained-tetrahedral-package-recovery').raw.scalar_shadow_recovery_established, false);
  assert.equal(by.get('prior-supplied-bottom-dependent-pair-agreement').raw.independently_fixed_faces_automatically_compatible, false);
  assert.equal(by.get('prior-forced-signed-completion-structured-lift-reduction').raw.remaining_structured_fiber_inhabited, false);
  assert.equal(by.get('prior-fixed-boundary-tetrahedron-presentation-equivalence').raw.fixed_boundary_filler_equivalence_available, true);
  assert.equal(by.get('prior-fixed-boundary-tetrahedron-presentation-equivalence').raw.independent_pentagon_comparison_established, false);
  assert.equal(by.get('prior-paired-completion-presentation-transport').raw.paired_completion_translation_available, true);
  for (const id of ['prior-fixed-boundary-tetrahedron-presentation-equivalence', 'prior-paired-completion-presentation-transport']) assert.equal(by.get(id).raw.analytical_realization_comparison_established, false);
  assert.equal(by.get('prior-common-strip-core-polarized-green-comparison').raw.unaugmented_endpoint_bound_established, false);
  assert.equal(by.get('prior-compact-support-weil-form-closure').raw.external_source_verification_established, false);
  for (const key of ['canonical_nondegenerate_seven_stage_alignment_established', 'graph_sets_are_certified_c13_segments']) assert.equal(by.get('prior-complete-hermitian-presentation-endpoint-isometry').raw[key], false);
  for (const id of ['prior-source-backed-segmentwise-h123-triangulations', 'prior-observer-valued-c14-analytical-path']) assert.equal(by.get(id).raw.canonical_fine_stage_identification_established, false);
  assert.equal(by.get('prior-source-reached-augmented-graph-universal-property').raw.endpoint_factored_through_regular_response, false);
  for (const key of ['external_topology_identification_established', 'absolute_value_commutes_with_compression']) assert.equal(by.get('prior-complete-chart-form-operator-feature-transport').raw[key], false);
  assert.equal(by.get('prior-rank-two-endpoint-preserving-core-approximation').raw.regular_compact_spectral_core_used_for_endpoint_evaluation, false);
  assert.equal(by.get('prior-rapid-remainder-bounded-packet-pullback').raw.conditional_remainder_pullback_formula_available, true);
  assert.equal(by.get('prior-rapid-remainder-bounded-packet-pullback').raw.native_triangle_boundary_identification_established, false);
  assert.equal(by.get('prior-source-rooted-cech-form-tetrahedron').raw.unanchored_cutoff_operator_equivalence_established, false);
  assert.equal(by.get('prior-joint-source-graph-successor-equivariance').raw.independent_physical_successor_identification_established, false);
  for (const key of ['automatic_augmented_feature_promotion_established', 'mellin_convention_reconciliation_established']) assert.equal(by.get('prior-source-star-generated-kernel-dagger').raw[key], false);
  assert.equal(by.get('prior-joint-source-polarity-relation-and-promotion-criterion').raw.unconditional_augmented_antiunitary_promotion_established, false);
  assert.equal(by.get('prior-generated-dagger-ambient-extension-criterion').raw.canonical_ambient_extension_selected, false);
  assert.equal(by.get('prior-reciprocal-adjoint-mate-cone-cell').raw.actual_green_return_adjoint_identification_established, false);
  assert.equal(by.get('prior-inverse-right-adjoint-compositor-mate').raw.conditional_inverse_mate_direction_available, true);
  for (const key of ['same_analytical_target_identification_established', 'finite_representative_identification_established']) assert.equal(by.get('prior-inverse-right-adjoint-compositor-mate').raw[key], false);
  for (const key of ['boundary_evaluation_inverse_established', 'observational_equality_implies_positive_isometry']) assert.equal(by.get('prior-relative-feature-target-and-boundary-evaluation').raw[key], false);
  assert.equal(by.get('prior-plancherel-volume-cutoff-cocycle').raw.relative_finite_part_positivity_established, false);
  const targetComparison = by.get('f736-source-retaining-common-target-comparison');
  assert.equal(targetComparison.status, 'open'); assert.equal(targetComparison.raw.actionable, true);
  assert.deepEqual(targetComparison.raw.admissible_realization_routes, ['transport_existing_parent_modification']);
  assert.equal(targetComparison.raw.chosen_realization_route, 'transport_existing_parent_modification');
  assert.equal(targetComparison.raw.scalar_to_cell_reconstruction_required, false);
  assert.equal(targetComparison.raw.optional_additive_model_requires_parent_comparison, true);
  assert.ok(targetComparison.depends_on.includes('prior-signed-asymptotic-h234-filler'));
  for (const id of ['prior-typed-tetrahedral-presentation-defect-identity', 'prior-relative-feature-target-and-boundary-evaluation']) {
    assert.ok(!targetComparison.depends_on.includes(id));
    assert.ok(targetComparison.raw.related_nodes.includes(id));
  }
  for (const key of ['scalar_to_operator_defect_identification_established', 'closed_defect_boundary_discharges_higher_filler']) assert.equal(targetComparison.raw[key], false);
  const defectIdentity = by.get('prior-typed-tetrahedral-presentation-defect-identity');
  assert.deepEqual(defectIdentity.raw.f736_patch_equations, ['Omega736-Omega732+D539 Omega731-Omega745 D511=0', 'Omega736-Omega735+D539 Omega734-Omega760 D513=0']);
  for (const key of ['closed_boundary_implies_higher_filler', 'scalar_remainder_identified_with_operator_defect', 'parent_modification_to_additive_defect_model_supplied', 'additive_defect_model_required_for_K']) assert.equal(defectIdentity.raw[key], false);
  for (const key of ['analytical_comparison_established', 'scalar_readout_inverse_allowed', 'native_triangle_boundary_identification_established', 'paired_f736_completion_established']) assert.equal(targetComparison.raw[key], false);
  for (const key of ['output_only_closed_range_inferred', 'modification_comparison_supplied_by_graph_closedness']) assert.equal(by.get('prior-labelled-continuous-joint-graph-complementation').raw[key], false);
  for (const key of ['owner_cfp_g4_identification_established', 'carrier_identified_with_f736']) assert.equal(by.get('prior-cfp-bounded-response-faithful-graph-example').raw[key], false);
  const carrierTask = by.get('f736-response-cutoff-joint-graph-instantiation');
  assert.equal(carrierTask.status, 'open'); assert.equal(carrierTask.raw.actionable, true);
  assert.equal(carrierTask.raw.one_sector_scalar_family_continuity_established, true);
  for (const key of ['conditional_one_sector_carrier_assembly_available', 'candidate_word_round_trips_established']) assert.equal(carrierTask.raw[key], true);
  const wordAssembly = by.get('derived-one-sector-retained-carrier-and-word-diagram');
  for (const key of ['conditional_one_sector_carrier_assembly_available', 'candidate_word_round_trips_established']) assert.equal(wordAssembly.raw[key], true);
  for (const key of ['native_spectral_domain_identification_established', 'uniform_operator_family_bound_established', 'modification_comparison_established']) assert.equal(wordAssembly.raw[key], false);
  for (const key of ['uniform_observer_family_bound_established', 'external_arithmetic_incidence_established']) assert.equal(by.get('prior-convolution-observation-common-graph-domain').raw[key], false);
  for (const key of ['carrier_instantiation_established', 'required_external_family_topology_identified', 'uniform_operator_family_continuity_established', 'modification_comparison_established', 'scalar_readout_inverse_allowed']) assert.equal(carrierTask.raw[key], false);
  assert.ok(carrierTask.depends_on.includes('derived-one-sector-retained-carrier-and-word-diagram'));
  for (const key of ['all_sector_extension_established', 'regulator_family_bound_from_nuclear_estimate_established']) assert.equal(by.get('prior-archimedean-fixed-cutoff-trace-continuity').raw[key], false);
  for (const key of ['ordered_trace_evaluated_by_uncompressed_diagonal', 'uniform_cutoff_trace_norm_bound_established']) assert.equal(by.get('prior-regular-schwartz-kernel-trace-class-continuity').raw[key], false);
  for (const key of ['all_path_simultaneous_limit_established', 'trace_value_identification_established_by_removal']) assert.equal(by.get('prior-trace-class-transported-regulator-removal').raw[key], false);
  assert.equal(by.get('prior-bounded-polarized-response-trace-class-linearization').raw.global_hilbert_source_bound_established, false);
  for (const key of ['general_semilocal_normalization_match_established', 'unaugmented_endpoint_bound_established']) assert.equal(by.get('prior-intrinsic-four-function-response-continuity').raw[key], false);
  for (const key of ['first_order_graph_flux_bound_established', 'external_arithmetic_transpose_membership_established']) assert.equal(by.get('prior-weighted-second-order-complete-trace-domain').raw[key], false);
  assert.equal(by.get('prior-exact-four-function-fourier-response-action').raw.additive_fourier_identified_with_unmodified_log_mellin, false);
  for (const key of ['invariant_subspace_intertwining_established', 'all_prime_full_line_limit_established']) assert.equal(by.get('prior-trivial-sector-finite-prime-tate-compression').raw[key], false);
  for (const key of ['cross_family_normalization_automatically_identified', 'physical_pv_constant_identified']) assert.equal(by.get('prior-corrected-unitary-gamma-fourier-scale').raw[key], false);
  const normalizationTask = by.get('f736-physical-spectral-diagonal-pv-normalization');
  assert.equal(normalizationTask.status, 'open'); assert.equal(normalizationTask.raw.actionable, true);
  assert.equal(normalizationTask.raw.frozen_packet_diagonal_constant_match_established, true);
  assert.equal(normalizationTask.raw.one_sector_general_polarized_distribution_match_established, true);
  const sectorMatch = by.get('derived-one-sector-compact-test-tate-comparison');
  assert.equal(sectorMatch.raw.one_sector_general_polarized_distribution_match_established, true);
  for (const key of ['all_sector_operator_equivalence_established', 'finite_remainder_erased']) assert.equal(sectorMatch.raw[key], false);
  const scalarFamily = by.get('derived-one-sector-rapid-scalar-cutoff-family');
  assert.equal(scalarFamily.raw.one_sector_rapid_scalar_family_continuity_established, true);
  for (const key of ['uniform_operator_trace_norm_family_bound_established', 'all_path_outer_angular_limit_established']) assert.equal(scalarFamily.raw[key], false);
  const diagonalMatch = by.get('derived-frozen-diagonal-even-tate-normalization-match');
  assert.equal(diagonalMatch.raw.frozen_packet_diagonal_constant_match_established, true);
  for (const key of ['additional_identity_delta_correction_required_for_this_match', 'general_polarized_distribution_match_established', 'finite_remainder_erased']) assert.equal(diagonalMatch.raw[key], false);
  assert.equal(normalizationTask.raw.one_sector_diagonal_pv_normalization_match_established, true);
  for (const key of ['full_target_diagonal_pv_normalization_match_established', 'additional_sector_required_by_restricted_K', 'finite_remainder_erased', 'all_sector_operator_equivalence_established']) assert.equal(normalizationTask.raw[key], false);
  for (const id of ['derived-one-sector-compact-test-tate-comparison', 'derived-one-sector-rapid-scalar-cutoff-family']) assert.ok(normalizationTask.depends_on.includes(id));
  assert.equal(by.get('prior-rigged-residual-attachment-witness-graph-lift').raw.actual_source_differential_and_witness_transport_available, true);
  assert.equal(by.get('prior-rigged-residual-attachment-witness-graph-lift').raw.f736_source_sector_identification_established, false);
  for (const key of ['unrestricted_output_inverse_established', 'f736_scalar_trace_inverse_established']) assert.equal(by.get('prior-prepared-euler-endpoint-residual-output-equivalence').raw[key], false);
  for (const key of ['global_closed_operator_realization_established', 'physical_coherent_nullhomotopy_established']) assert.equal(by.get('prior-relative-tower-universal-stable-cone-enhancement').raw[key], false);
  const witnessLift = by.get('f736-boundary-witness-record-graph-lift');
  assert.equal(witnessLift.status, 'open'); assert.equal(witnessLift.raw.actionable, true);
  assert.equal(witnessLift.raw.parent_signature_and_representative_available, true);
  const mechanismIds = ['f736-polarized-kernel-witness-lift-conjecture', 'f736-cutoff-current-transgression-witness-conjecture'];
  assert.deepEqual(witnessLift.raw.candidate_mechanisms, []);
  assert.deepEqual(witnessLift.raw.deferred_auxiliary_models, mechanismIds);
  assert.equal(witnessLift.raw.candidate_mechanisms_are_joint_prerequisites, false);
  assert.equal(witnessLift.raw.parent_signed_cell_available, true);
  assert.equal(witnessLift.raw.scalar_to_cell_reconstruction_required, false);
  assert.equal(witnessLift.raw.compositor_and_native_boundary_comparisons_required, true);
  assert.equal(witnessLift.raw.quotient_only_recovery_of_finite_representative_allowed, false);
  assert.ok(!witnessLift.depends_on.includes('derived-retained-rapid-readout-comparison-on-grid'));
  assert.ok(witnessLift.raw.related_nodes.includes('derived-retained-rapid-readout-comparison-on-grid'));
  const parentCell = by.get('prior-signed-asymptotic-h234-filler').raw;
  assert.equal(parentCell.parent_signed_cell_available, true);
  assert.equal(parentCell.parent_cell_reconstruction_from_scalar_required, false);
  assert.equal(parentCell.finite_representative_recoverable_from_quotient_class_alone, false);
  for (const id of mechanismIds) {
    const mechanism = by.get(id);
    assert.equal(mechanism.status, 'deferred_missing_operation'); assert.equal(mechanism.outcome, null);
    assert.equal(mechanism.kind, 'conjecture');
    assert.equal(mechanism.raw.proposal_origin, 'assistant_synthesis');
    assert.equal(mechanism.raw.actionable, false);
    assert.equal(mechanism.raw.typed_parent_model_supplied, false);
    assert.equal(mechanism.raw.scalar_to_cell_reconstruction_required, false);
    assert.equal(mechanism.raw.disposition, 'withdrawn_scalar_reconstruction_route_pending_typed_parent_model');
    assert.ok(mechanism.raw.missing_operation);
    assert.ok(mechanism.depends_on.includes('prior-signed-asymptotic-h234-filler'));
    assert.ok(!r.frontier.includes(id));
    assert.equal(mechanism.raw.f736_binding_established, false);
    assert.equal(mechanism.raw.positive_feature_lift_established, false);
    assert.ok(mechanism.raw.first_test && mechanism.raw.falsifier);
    assert.ok(!witnessLift.depends_on.includes(id));
    assert.ok(!mechanism.depends_on.some(dep => mechanismIds.includes(dep)));
  }
  assert.equal(by.get(mechanismIds[0]).raw.kernel_to_witness_realization_established, false);
  for (const key of ['geometric_current_constructed', 'witness_valued_tail_integrability_established']) assert.equal(by.get(mechanismIds[1]).raw[key], false);
  assert.equal(witnessLift.raw.finite_packet_retained_comparison_grid_available, true);
  assert.equal(witnessLift.raw.retained_scalar_readout_comparison_on_grid_available, true);
  for (const key of ['response_chart_identified_with_parent_cutoff_arrow', 'parent_modification_observation_interpretation_established']) assert.equal(witnessLift.raw[key], false);
  const readoutComparison = by.get('derived-retained-rapid-readout-comparison-on-grid').raw;
  assert.equal(readoutComparison.retains_actual_spectral_and_cutoff_boundary_families, true);
  assert.equal(readoutComparison.readout_boundary_identity, 't_(c,w)-v_(c,w)=E composed with p_(c,w)');
  assert.equal(readoutComparison.comparison_groupoid.cutoff_spectral_arrow, 'V --E--> T');
  assert.equal(readoutComparison.comparison_groupoid.components, 'Fam/N');
  for (const key of ['new_source_ideal_or_differential_introduced', 'native_modification_target_identification_established', 'scalar_inverse_is_automatically_compositor_mate_representative', 'operator_defect_or_feature_isometry_identification_established', 'scalar_groupoid_is_parent_modification_category', 'scalar_groupoid_is_required_intermediate_target_for_K']) assert.equal(readoutComparison[key], false);
  for (const key of ['parent_natural_arrow_comparison_on_grid_established', 'representative_bearing_modification_on_grid_identified']) assert.equal(witnessLift.raw[key], false);
  assert.ok(witnessLift.raw.depends_on.includes('derived-f736-finite-packet-native-word-retained-grid'));
  const retainedGrid = by.get('derived-f736-finite-packet-native-word-retained-grid').raw;
  assert.deepEqual(retainedGrid.grid_indices, {native_contexts: [5,15], fine_vertices: ['V104','V111','V113'], tagged_object_count: 6});
  assert.equal(retainedGrid.map_formulas.mixed_square, 'N_v H_(5,e)=H_(15,e) N_u');
  for (const key of ['retains_full_native_field_separately', 'mixed_squares_on_declared_grid_established']) assert.equal(retainedGrid[key], true);
  for (const key of ['all_observer_word_image_surjectivity_established', 'independent_presentation_modification_identification_established', 'positive_physical_metric_identification_established']) assert.equal(retainedGrid[key], false);
  assert.deepEqual(witnessLift.raw.auxiliary_constructor_action_types, ['fixed_observer_cutoff_frame_change', 'retained_log_amplitude_translation', 'simultaneous_polarized_pair_translation']);
  assert.equal(witnessLift.raw.chosen_native_constructor_action_type, 'decoded_source_preserving_native_NE_transfer');
  assert.equal(witnessLift.raw.native_constructor_generator_identification_established, true);
  assert.equal(witnessLift.raw.fixed_cutoff_finite_packet_covariance_available, true);
  const nativeReadout = by.get('f736-physical-readout-attempt').raw;
  assert.deepEqual(nativeReadout.native_constructor, {operation: 15, kind: 'NE', source_packet: 5, target_packet: 15, permutation: [0,4,2,3,1], phase_delta: 0});
  assert.equal(nativeReadout.decoded_packet_source_action_identified, true);
  assert.equal(nativeReadout.nonzero_log_label_translation_is_decoded_NE_action, false);
  assert.equal(nativeReadout.crossing_identified_with_fine_edge_or_filler, false);
  assert.equal(nativeReadout.decoded_source_equation, 'D15 U_NE=D5; hence E D15 U_NE=E D5 for the actual five-packet synthesis E');
  assert.equal(witnessLift.raw.one_sector_explicit_response_action_available, true);
  const dilationSquare = by.get('derived-one-sector-label-dilation-response-square').raw;
  assert.deepEqual(dilationSquare.response_action, {B: 'exp(-s/2) B(exp(-s)a)', Q: 'exp(s/2) Q(exp(s)a)', A: 'exp(s/2) A(exp(-s)a)', C: 'exp(-s/2) C(exp(s)a)'});
  assert.equal(dilationSquare.source_coordinate_laws.identity_density, '(sigma_s h)(0)=h(-s)');
  for (const key of ['uniform_all_translation_parameter_bound_established', 'label_translation_identified_with_fixed_observer_frame_change', 'native_constructor_action_identification_established', 'full_ordered_cutoff_intertwining_established']) assert.equal(dilationSquare[key], false);
  assert.equal(witnessLift.raw.native_full_centered_record_intertwining_established, false);
  for (const key of ['all_successor_arrows_invertible', 'full_physical_centered_boundary_naturality_established']) assert.equal(by.get('prior-relative-rigged-source-successor-square').raw[key], false);
  for (const key of ['common_row_hilbert_schmidt_established', 'full_ordered_boundary_stationarity_established']) assert.equal(by.get('prior-exact-recentered-relative-difference-feature').raw[key], false);
  assert.equal(by.get('prior-semilocal-fourier-canonical-dual-cutoff-square').raw.complete_differentiated_form_invariance_established_by_this_result, false);
  for (const key of ['placement_defect_vanishing_established', 'placement_defect_nonvanishing_established', 'native_target_regulator_identified_with_transported_candidate']) assert.equal(by.get('derived-finite-cutoff-step-left-placement-defect').raw[key], false);
  for (const key of ['eta24_finite_reference_calibration_accounted_for_natively', 'eta24_native_naturality_square_established']) assert.equal(witnessLift.raw[key], false);
  for (const key of ['calibration_zero_at_finite_regulator_established', 'separate_summands_rapid_decay_established', 'trace_norm_null_quotient_identified_with_rapid_scalar_quotient']) assert.equal(by.get('derived-centered-cutoff-relative-reference-calibration').raw[key], false);
  for (const key of ['centered_form_positivity_established', 'native_eta24_naturality_established']) assert.equal(by.get('prior-regulated-h124-cutoff-volume-feature').raw[key], false);
  for (const key of ['pure_positive_comparison_established', 'canonical_vertex_replacement_allowed']) assert.equal(by.get('prior-signed-defect-augmented-hermitian-comparison').raw[key], false);
  for (const key of ['graph_presentation_functor_identification_established', 'parent_arrow_native_boundary_identification_established', 'higher_realization_comparison_K_established', 'whole_record_lift_established', 'boundary_intertwining_established', 'whole_record_recovery_established', 'native_f736_completion_established']) assert.equal(witnessLift.raw[key], false);
  for (const id of ['prior-complete-hermitian-presentation-endpoint-isometry', 'prior-source-backed-segmentwise-h123-triangulations']) assert.ok(witnessLift.raw.depends_on.includes(id));
  const pb = by.get('pb208-retained-native-construction');
  assert.equal(pb.status, 'open'); assert.equal(pb.raw.proposal_origin, 'operator_requested_research_direction');
  for (const key of ['construction_established', 'isotope_counts_derived', 'geometric_fill_sufficient', 'completed_target_input_allowed']) assert.equal(pb.raw[key], false);
  const substitution = by.get('pb208-process-substitution-criticism');
  assert.equal(substitution.status, 'open'); assert.equal(substitution.raw.substitutes_discharge_task, false); assert.equal(substitution.raw.construction_impossible, false);
  assert.ok(!pb.depends_on.includes(substitution.id));
  const synthesis = by.get('assembler-as-global-evolution');
  assert.equal(synthesis.status, 'open'); assert.equal(synthesis.raw.proposal_origin, 'assistant_synthesis');
  assert.equal(synthesis.raw.evolution_binding_established, false);
  assert.deepEqual(synthesis.depends_on, ['single-channel-esd7-assembly', 'global-28-stage-pe-fibration']);
  assert.ok(r.connections.every(x => !x.proof_bearing && !x.discharges_parent_obligation));
  return by;
}
let by;
check('DAG and no-promotion boundaries', () => { by = boundaries(raw); });
check('operator modality retained', () => assert.equal(raw.operator_stimulus.confidence_modality, 'seems'));
const prior = await load(raw.previous_revision); inputs.add(raw.previous_revision);
check('previous revision retained without silently upgrading its nodes', () => {
  assert.equal(prior.revision, 72);
  assert.deepEqual(prior.frontier, ['f736-cutoff-current-transgression-witness-conjecture', 'f736-polarized-kernel-witness-lift-conjecture', ...raw.frontier]);
  const deferred = new Set(['f736-polarized-kernel-witness-lift-conjecture', 'f736-cutoff-current-transgression-witness-conjecture']);
  for (const old of prior.conjectures) {
    if (deferred.has(old.id)) assert.equal(old.status, 'open');
    assert.equal(by.get(old.id).status, deferred.has(old.id) ? 'deferred_missing_operation' : old.status);
    assert.equal(by.get(old.id).outcome, old.outcome);
  }
});
const reviewPath = raw.typing_review.all_node_dispositions;
inputs.add(reviewPath);
const reviewText = await fs.readFile(path.join(root, reviewPath), 'utf8');
function checkReview(text) {
  const rows = [...text.matchAll(/^\| `([^`]+)` \| (retain|revise|defer) \| (.+) \|$/gm)];
  assert.equal(rows.length, raw.conjectures.length);
  assert.equal(new Set(rows.map(row => row[1])).size, rows.length);
  const oldBy = new Map(prior.conjectures.map(node => [node.id, node]));
  assert.deepEqual(rows.map(row => row[1]).sort(), raw.conjectures.map(node => node.id).sort());
  for (const [, id, disposition, reason] of rows) {
    assert.ok(reason.length > 20);
    const changed = JSON.stringify(oldBy.get(id)) !== JSON.stringify(by.get(id).raw);
    assert.equal(changed, disposition !== 'retain', id);
    if (disposition === 'defer') assert.equal(by.get(id).status, 'deferred_missing_operation');
  }
}
check('all-node review covers exact live node set and changed-node dispositions', () => checkReview(reviewText));
check('review rejects missing node disposition', () => assert.throws(() => checkReview(reviewText.replace(/^\| `existing-seed-context`.*\n/m, ''))));
for (const [nodeId, receiptPath, validate] of [
  ['native-intrinsic-selector-audit', 'research/strominger/results/intrinsic-retained-selector.json', r => {
    assert.equal(r.conjectureOutcome, 'native-contract uniqueness falsified'); assert.equal(r.sourceCount, 96); assert.equal(r.certifiedContinuations, 192);
  }],
  ['native-task-selector-audit', 'research/strominger/results/retained-transport-task-selection.json', r => {
    assert.equal(r.counts.sources, 48); assert.equal(r.counts.fixedTaskCounterexamples, 8); assert.equal(r.counts.certifiedContinuations, 40);
  }],
  ['scalar-global-fcc-candidate', 'research/strominger/results/global-fcc-evolution.json', r => {
    assert.equal(r.native_E_match_at28, false); assert.ok(r.candidate_outcome.startsWith('rejected'));
  }],
  ['f736-correlated-word-edges-attempt', 'research/strominger/results/f736-correlated-word-edges/verification.json', r => {
    assert.equal(r.check_count, 31); assert.equal(r.conditionalFineEdgeRealizationEstablished, true); assert.equal(r.face, 'F736');
    assert.equal(r.orientedComponentMaps, 42); assert.equal(r.routeSquares, 14); assert.equal(r.adjacentOccurrenceSquares, 36); assert.equal(r.faceOccurrences, 21);
    assert.equal(r.flattenedProgramCompositionRejected, true); assert.equal(r.nondegenerateParentRole, 'H234'); assert.equal(r.nondegenerateOccurrence, 5);
    for (const key of ['intendedHomotopyBindingEstablished', 'completionExtensionEstablished', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['f736-physical-readout-attempt', 'research/strominger/results/f736-physical-readout/verification.json', r => {
    assert.equal(r.check_count, 47); assert.equal(r.physicalReadoutComparisonEstablished, true); assert.equal(r.face, 'F736');
    assert.equal(r.enclosedPhysicalEntries, 75); assert.equal(r.nativeMatrixUnitSquares, 25); assert.equal(r.nativeFieldDimension, 44); assert.deepEqual(r.cutoffs, [2,4,8]);
    for (const key of ['analyticalFaceFillerEstablished', 'fineEdgeOperatorsSupplied', 'hardyReferenceIdentificationEstablished', 'allSemilocalSectorsEstablished', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['native-ne-fine-face-attempt', 'research/strominger/results/native-ne-fine-face/verification.json', r => {
    assert.equal(r.check_count, 13); assert.equal(r.nativeFineFaceIdentityEstablished, true); assert.equal(r.primitiveMatches, 343); assert.equal(r.face, 'F736');
    assert.deepEqual(r.vertices, ['V104','V111','V113']); assert.deepEqual(r.sharedEdgeRoute, ['E514','E539']); assert.equal(r.directEdge, 'E515');
    assert.deepEqual(r.incidentPackets.map(p=>p.analyticalContext.role), ['H134','H134']);
    for (const key of ['analyticalFaceComparisonEstablished', 'analyticalHomotopyEstablished', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['external-c0-finite-trace-attempt', 'research/strominger/results/external-c0-finite-trace/verification.json', r => {
    assert.equal(r.check_count, 109); assert.equal(r.finiteC0TraceBindingEstablished, true);
    assert.equal(r.encodedPresentations, 66); assert.equal(r.nativeInterfaces, 95); assert.deepEqual(r.matchingCalibratedFluxIndices, [1]); assert.equal(r.endpointInvisibleWitnessCount, 2);
    for (const key of ['endpointOnlySufficient', 'encoderRefitted', 'analyticalDomainExtensionEstablished', 'actualF006BindingEstablished', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['screw-esd7-relative-attachment-attempt', 'research/strominger/results/screw-esd7-relative-attachment/verification.json', r => {
    assert.equal(r.check_count, 10); assert.equal(r.relativeNativeAttachmentEstablished, true);
    assert.equal(r.occupiedCells, 24); assert.equal(r.packets, 66); assert.equal(r.validatedInterfaces, 95);
    assert.equal(r.externalReferenceVertices, 1); assert.equal(r.generatedReferenceCells, 1); assert.deepEqual(r.failures, []);
    for (const key of ['analyticalDomainExtensionEstablished', 'actualF006BindingEstablished', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['screw-esd7-geometric-attachment-attempt', 'research/strominger/results/screw-esd7-geometric-attachment/verification.json', r => {
    assert.equal(r.check_count, 11); assert.deepEqual(r.occupiedMinimumResolutions, [7,6]); assert.deepEqual(r.fullMinimumResolutions, [8,8]);
    assert.equal(r.excludedOrientations, 48); assert.equal(r.acceptedPlacements, 0); assert.equal(r.occupiedOnlyPlacements, 40); assert.equal(r.minimumOutsideReferences, 1);
    for (const key of ['geometricAttachmentEstablished', 'actualAnalyticalFaceBindingEstablished', 'coherencePresentationInterpretationRefuted', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
    const w=r.minimalExternalWitness; assert.equal(w.sign, -1); assert.deepEqual(w.translation, [-3,2,2,1]);
    assert.deepEqual(w.references[0].target, [-3,1,3,0]); assert.equal(w.references.length, 1);
    assert.ok(w.references[0].incidentInterfaces.some(e=>e.kind==='NE'&&e.source===5&&e.target===15));
  }],
  ['pb208-screw-field-attempt', 'research/strominger/results/screw-field-sewing.json', r => {
    assert.equal(r.check_count, 19); assert.equal(r.screwFieldSewingEstablished, true);
    assert.equal(r.counts.packets, 66); assert.equal(r.counts.interfaces, 95); assert.equal(r.counts.rootFieldDimension, 44);
    assert.deepEqual(r.counts.bodies, {proton:9,neutron:13,electron:2});
    assert.equal(r.exitSplits.length, 4); assert.equal(r.fixedBindingFailurePackets.length, 57);
    for (const key of ['actualEsd7FaceBindingEstablished', 'fullPbConstructionEstablished', 'infiniteRetainedExtensionEstablished']) assert.equal(r[key], false);
  }],
  ['pb208-octahedral-reader-atlas-attempt', 'research/strominger/results/octahedral-reader-atlas/verification.json', r => {
    assert.equal(r.check_count, 9); assert.equal(r.readerStates, 8); assert.equal(r.nativeTransitions, 16);
    assert.equal(r.exitPorts, 8); assert.equal(r.externalPorts, 0); assert.equal(r.referenceOnlyReaders, 7);
    assert.equal(r.criterionDisposition, 'no-external-port-under-fixed-root-N-only-rules'); assert.equal(r.sourceInvariantEstablished, true);
    for (const key of ['externalPortEstablished', 'absoluteHistoriesIdentified', 'wholeNeutronAdmissionEstablished', 'allNativeRoutesExcluded']) assert.equal(r[key], false);
  }],
  ['pb208-native-whole-fixture-attempt', 'research/strominger/results/native-whole-inventory-fixture/verification.json', r => {
    assert.equal(r.check_count, 9); assert.equal(r.criterionDisposition, 'inventory-grounded-but-pair-not-admitted');
    assert.equal(r.inventoryCriterionPassed, true); assert.equal(r.packetCount, 14); assert.equal(r.interfacesChecked, 18);
    assert.equal(r.rootFramesChecked, 7); assert.equal(r.prefixBindings, 5); assert.equal(r.electronBindings, 2); assert.equal(r.neutronBindings, 0);
    for (const key of ['pairBindingEstablished', 'fullPbConstructionEstablished', 'allWholeAssemblyModelsRefuted']) assert.equal(r[key], false);
  }],
  ['pb208-inventory-fibration-attempt', 'research/strominger/results/pb208-inventory-fibration/verification.json', r => {
    assert.equal(r.check_count, 22); assert.equal(r.criterionDisposition, 'candidate-insufficient-for-inventory-bridge');
    assert.equal(r.retainedTotalRecoveryPassed, true);
    for (const key of ['inventoryBridgeEstablished', 'genericFibrationRefuted', 'allWholeAssemblyModelsRefuted', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['native-ne-nn-reader-comparison', 'research/strominger/results/native-reader-comparison/verification.json', r => {
    assert.equal(r.check_count, 12); assert.equal(r.fullCoefficientComparisonEstablished, true);
    for (const key of ['nativeCrossSpeciesArrowEstablished', 'currentCompositionReadoutPreserved', 'activeReaderOnlyFactorization', 'wholeAssemblyReaderInterpretationRefuted', 'fullPbConstructionEstablished']) assert.equal(r[key], false);
  }],
  ['native-retained-joint-attachment-attempt', 'research/strominger/results/native-retained-batch-attempt/verification.json', r => {
    assert.equal(r.check_count, 15); assert.equal(r.concreteNativeAttempt, true);
    assert.equal(r.exploredRounds, 3); assert.equal(r.exploredSnapshots, 4); assert.equal(r.terminalRoundConfigurations, 10);
    for (const key of ['targetQuotaUsed', 'completedPbInputUsed', 'fullPbConstructionEstablished', 'physicalSelectionEstablished']) assert.equal(r[key], false);
  }],
  ['archimedean-centered-packet-limit', 'research/strominger/results/archimedean-diagonal-limit-verification.json', r => {
    assert.equal(r.check_count, 19); assert.equal(r.packetDimension, 5);
    assert.equal(r.diagonalFinitePartRepresented, true); assert.equal(r.centeredPacketMatrixLimitControlled, true);
    assert.equal(r.diagonalErrorAt1024, '361735/226492416');
    for (const key of ['numericalFinitePartValueComputed', 'positivityEstablished', 'allSemilocalSectorsEstablished', 'analyticalHigherWitnessEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['archimedean-physical-cutoff-enclosures', 'research/strominger/results/archimedean-cutoff-entry-verification.json', r => {
    assert.equal(r.check_count, 23); assert.equal(r.offDiagonalEntries, 20); assert.equal(r.finiteEnclosures, 60);
    assert.equal(r.physicalCutoffEntriesEnclosed, true); assert.deepEqual(r.cutoffs, [2,4,8]);
    for (const key of ['completePacketMatrixEvaluated', 'diagonalFinitePartEvaluated', 'fullAnalyticalFillerEstablished', 'allSemilocalSectorsEstablished', 'full114ChannelEstablished', 'numericalQuadraturePerformed']) assert.equal(r[key], false);
  }],
  ['corrected-cutoff-observer-legs', 'research/strominger/results/cutoff-regulator-placement-verification.json', r => {
    assert.equal(r.check_count, 12); assert.equal(r.correctedControlCases, 24);
    assert.equal(r.correctedFiniteTraceIdentityVerified, true); assert.equal(r.claimedFactorizationValidWithoutExtraCommutation, false);
    assert.equal(r.counterexampleDefect, '-1/4');
    for (const key of ['fullPhysicalCutoffEvaluated', 'packetCutoffResidualEvaluated', 'sourceUnitaryTransportRefuted', 'globalConjectureRefuted']) assert.equal(r[key], false);
    assert.ok(by.get('cutoff-leg-cyclicity-shortcut').raw.evidence.includes('research/strominger/results/cutoff-regulator-placement-verification.json'));
  }],
  ['finite-packet-green-trace-subproblem', 'research/strominger/results/finite-packet-green-trace-verification.json', r => {
    assert.equal(r.check_count, 17); assert.equal(r.seamMatrices, 5); assert.equal(r.polarizedEntries, 125);
    assert.equal(r.nativePresentationSeamChecks, 70); assert.equal(r.endpointInvisiblePairing, -10);
    assert.equal(r.sourceTraceSubproblemEvaluated, true);
    for (const key of ['fullPhysicalMixedPolarizationIdentified', 'physicalCutoffResidualEvaluated', 'analyticalFaceHomotopyEstablished', 'physicalProbeProtocolEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['finite-packet-signed-endpoint-form', 'research/strominger/results/finite-packet-endpoint-form-verification.json', r => {
    assert.equal(r.check_count, 18); assert.equal(r.polarizedEntries, 25);
    assert.equal(r.transportedPresentations, 14); assert.equal(r.matchedFull44EReaders, 2);
    assert.equal(r.specificEndpointTermEvaluated, true); assert.deepEqual(r.signature, [1,1,3]);
    for (const key of ['fullRegulatedResidualEvaluated', 'analyticalFaceHomotopyEstablished', 'positivityEstablished', 'physicalReadoutEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['finite-observer-encoder-candidate', 'research/strominger/results/finite-observer-encoder-verification.json', r => {
    assert.equal(r.check_count, 17); assert.equal(r.packetDimension, 5);
    assert.equal(r.encodedPresentations, 14); assert.equal(r.nativeInterfaces, 18); assert.equal(r.matchedEExits, 2);
    assert.equal(r.observationDeterminant, '-3/2'); assert.equal(r.explicitFinitePacketEncoderConstructed, true);
    for (const key of ['sourceForcedOrUnique', 'fullObserverDomainEncoded', 'specificAnalyticalResidualEvaluated', 'intendedAnalyticalWitnessBindingEstablished', 'physicalPreparationEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['strict-native-witness-comparison', 'research/strominger/results/strict-native-comparison-verification.json', r => {
    assert.equal(r.check_count, 14); assert.equal(r.pairwiseComparisons, 196);
    assert.equal(r.nativeCocycleTriangles, 2744); assert.equal(r.conditionalMixedSquares, 3136);
    assert.equal(r.retainedOrderFiveWitness.coefficientOrder, 5);
    assert.deepEqual(r.retainedOrderFiveWitness.fieldFactorWord, []);
    assert.equal(r.retainedOrderFiveWitness.readoutsDifferent, true);
    for (const key of ['encoderSupplied', 'intendedAnalyticalWitnessBindingEstablished', 'fullEsd7NativeTransportEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['esd7-strict-parent-evaluation', 'research/strominger/results/esd7-strict-parent-evaluation-verification.json', r => {
    assert.equal(r.check_count, 21); assert.equal(r.counts.cells, 1807);
    assert.equal(r.counts.restrictionAdjacencies, 64736); assert.equal(r.counts.readoutSquares, 5421);
    assert.equal(r.conditionalStrictDiagramEvaluationEstablished, true);
    assert.equal(r.F006.parentOccurrences.length, 21);
    for (const key of ['sourceAnalyticIdentitiesFreshlyProved', 'intendedAnalyticalWitnessBindingEstablished', 'native44TransportBindingEstablished', 'full114ChannelEstablished', 'completionExtensionEstablished']) assert.equal(r[key], false);
  }],
  ['esd7-simplicial-fine-vertex-refinement', 'research/strominger/results/esd7-simplicial-refinement-verification.json', r => {
    assert.equal(r.check_count, 20); assert.equal(r.cellCount, 1807);
    assert.equal(r.structuralRefinementEstablished, true);
    assert.deepEqual(r.parentNerveDimensions, {vertex:6,edge:13,face:20,tetrahedron:27});
    assert.deepEqual(r.F006.parentSupport, [1,2,3,4]);
    for (const key of ['actualF006AnalyticalComparisonEstablished', 'analyticalRealizationEstablished', 'globalFieldTransportEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['esd7-bare-parent-chart-substitution', 'research/strominger/results/esd7-parent-chart-binding-verification.json', r => {
    assert.equal(r.check_count, 12); assert.equal(r.conflictingVertices, 116);
    assert.equal(r.singleTransferEdges, 504); assert.equal(r.compoundTransferEdges, 56);
    assert.equal(r.candidateDisposition, 'rejected_context_free_substitution');
    assert.equal(r.actualF006ComparisonEstablished, false); assert.equal(r.refinementImpossible, false);
    assert.equal(r.parentFaceReduction.fineVertexIdentificationEstablished, false);
  }],
  ['esd7-retained-face-comparison-gate', 'research/strominger/results/esd7-retained-face-comparison.json', r => {
    assert.equal(r.check_count, 12); assert.equal(r.face.face, 'F006');
    assert.equal(r.actualFaceStatus, 'blocked_missing_source_bound_payload');
    assert.equal(r.actualFaceComparisonEstablished, false);
    assert.equal(r.analyticalCoherenceDischarged, false); assert.equal(r.globalFieldTransportEstablished, false);
    assert.equal(r.implementationControl.positive.passed, true);
    assert.equal(r.implementationControl.endpointMutation.passed, false);
    assert.equal(r.missingSourceBindings.length, 4);
  }],
  ['esd7-analytical-prototype-bridge', 'research/strominger/results/esd7-analytical-binding-verification.json', r => {
    assert.equal(r.check_count, 24); assert.equal(r.registryBridgeEstablished, true);
    assert.equal(r.boundTetrahedra, 343); assert.equal(r.boundFaces, 784);
    assert.equal(r.sharedFaceComparisons, 588); assert.equal(r.distinctRoleSharedFaces, 294);
    assert.deepEqual(r.sharedRolePairs, {'H123/H234':294, 'H124/H124':147, 'H134/H134':147});
    for (const key of ['analyticalCoherenceDischarged', 'globalFieldTransportEstablished', 'full114ChannelEstablished']) assert.equal(r[key], false);
  }],
  ['esd7-generated-geometric-channel', 'research/strominger/results/esd7-attachment-channel-verification.json', r => {
    assert.equal(r.recordCount, 345); assert.equal(r.check_count, 25);
    assert.deepEqual(r.counts, {vertices:120, edges:560, triangles:784, tetrahedra:343});
    assert.equal(r.geometricReconstructionEstablished, true);
    for (const key of ['targetUsedByDecoder', 'full114ChannelEstablished', 'analyticalCoherenceDischarged', 'globalFieldTransportEstablished']) assert.equal(r[key], false);
    assert.deepEqual(r.pendingObligations, {faceHomotopies:784, tetrahedralCoherences:343});
  }],
  ['channel-contract-and-first-assembly-step', 'research/strominger/results/native-retained-channel-verification.json', r => {
    assert.equal(r.recordCount, 23); assert.equal(r.check_count, 20);
    assert.equal(r.counts.packets, 14); assert.equal(r.counts.interfaces, 18);
    assert.equal(r.targetFixtureUsedByDecoder, false); assert.equal(r.full114ChannelEstablished, false); assert.equal(r.fullEsd7Established, false);
  }],
  ['channel-contract-and-first-assembly-step', 'research/strominger/results/channel-assembled-field-sewing.json', r => {
    assert.equal(r.fixture_source, 'research/strominger/results/channel-assembled-native-fixture.json');
    assert.equal(r.check_count, 18); assert.equal(r.counts.interfaces, 18);
    assert.equal(r.counts.rootFieldDimension, 44); assert.equal(r.exitSplits.length, 2);
    assert.ok(r.interfaces.every(e => e.full44FieldSquare && e.full44ReadoutSquare && e.fiveCoefficientBindingSquare));
  }],
  ['native-joint-field-assembly-sewing', 'research/strominger/results/joint-field-assembly-sewing.json', r => {
    assert.equal(r.counts.packets, 14); assert.equal(r.counts.interfaces, 18); assert.equal(r.counts.rootFieldDimension, 44);
    assert.equal(r.exitSplits.length, 2); assert.ok(r.exitSplits.every(e => e.electronRank === 2 && e.retainedBaryonRank === 3 && e.fullFiveRecovery));
  }]
]) {
  const receipt = await load(receiptPath); inputs.add(receiptPath);
  check('bounded evidence disposition: ' + nodeId, () => {
    assert.ok(by.get(nodeId).raw.evidence.includes(receiptPath)); assert.equal(receipt.status, 'passed'); validate(receipt);
  });
  const hashes = receipt.sourceHashes ?? receipt.sourceSha256 ?? receipt.source_sha256;
  assert.ok(hashes);
  for (const [p, digest] of Object.entries(hashes)) {
    inputs.add(p);
    assert.equal(createHash('sha256').update(await fs.readFile(path.join(root, p))).digest('hex'), digest, 'Stale direct evidence input: ' + p);
  }
}
checks.push('new result receipts have live direct-input hashes (not transitive proof closure)');
for (const link of raw.connections) {
  assert.ok(by.has(link.source_node));
  const target = await load(link.target_contract); inputs.add(link.target_contract);
  const ids = new Set(target.conjectures.map(x => x.id));
  check('external nodes: ' + link.target_contract, () => {
    assert.ok(link.target_nodes.every(id => ids.has(id)));
    assert.ok(link.relation && link.scope);
  });
}
for (const n of raw.conjectures) for (const p of n.evidence ?? []) {
  await fs.access(path.join(root, p)); inputs.add(p);
}
checks.push('all declared evidence locators exist');
const catalog = await load('src/conjecture-nets/catalog.json');
check('owner-local branch registered for public explorer', () => assert.ok(catalog.nets.some(x => x.path === contractPath)));
for (const n of raw.conjectures) {
  if (!n.external_dependency) continue;
  const {contract, node} = n.external_dependency;
  assert.ok(catalog.nets.some(x => x.path === contract));
  const target = await load(contract); inputs.add(contract);
  assert.ok(target.conjectures.some(x => x.id === node));
}
checks.push('public external context resolves to bundled producer');
for (const [name, mutate] of [
  ['existing parent cell replaced by scalar reconstruction', r => { r.conjectures.find(x => x.id === 'f736-boundary-witness-record-graph-lift').scalar_to_cell_reconstruction_required = true; }],
  ['compositor and boundary identifications dropped', r => { r.conjectures.find(x => x.id === 'f736-boundary-witness-record-graph-lift').compositor_and_native_boundary_comparisons_required = false; }],
  ['finite representative recovered from quotient alone', r => { r.conjectures.find(x => x.id === 'prior-signed-asymptotic-h234-filler').finite_representative_recoverable_from_quotient_class_alone = true; }],
  ['deferred current model reactivated without typing', r => { r.conjectures.find(x => x.id === 'f736-cutoff-current-transgression-witness-conjecture').actionable = true; }],
  ['scalar groupoid made mandatory for higher transport', r => { r.conjectures.find(x => x.id === 'f736-boundary-witness-record-graph-lift').depends_on.push('derived-retained-rapid-readout-comparison-on-grid'); }],
  ['additive defect model made mandatory for completion', r => { r.conjectures.find(x => x.id === 'f736-source-retaining-common-target-comparison').depends_on.push('prior-typed-tetrahedral-presentation-defect-identity'); }],
  ['one-sector normalization reopened as unestablished', r => { r.conjectures.find(x => x.id === 'f736-physical-spectral-diagonal-pv-normalization').one_sector_diagonal_pv_normalization_match_established = false; }],
  ['automatic conjecture proof', r => { r.conjectures.find(x => x.id === 'persistent-seam-pe').outcome = '++'; }],
  ['operator confirmation as evidence', r => { r.boundary.operator_confirmation_is_evidence = true; }],
  ['global cover made prerequisite', r => { r.conjectures.find(x => x.id === 'persistent-seam-pe').depends_on.push('polarity-cover-audit'); }],
  ['parent proof promotion', r => { r.connections[0].discharges_parent_obligation = true; }],
  ['serial rival silently rejected', r => { r.conjectures.find(x => x.id === 'serial-shared-coordinate-rival').status = 'rejected'; }],
  ['native-source obstruction silently withdrawn', r => { r.conjectures.find(x => x.id === 'counteroriented-synchronous-rival').source_binding_status = 'admitted'; }],
  ['counteroriented rival silently rejected', r => { r.conjectures.find(x => x.id === 'counteroriented-synchronous-rival').status = 'rejected'; }],
  ['bounded rejection silently withdrawn', r => { r.conjectures.find(x => x.id === 'seam-invariants-select-same-orientation').status = 'proved'; }],
  ['rung4 hypothesis silently proved', r => { r.conjectures.find(x => x.id === 'rung4-double-observation-readout').status = 'proved'; }],
  ['rung assignment inferred from count', r => { r.conjectures.find(x => x.id === 'rung4-double-observation-readout').rung_assignment_established = true; }],
  ['work promoted to global stages', r => { r.conjectures.find(x => x.id === 'nested-double-observation-certificate').global_28_stages_established = true; }],
  ['consistency promoted to physical reality', r => { r.conjectures.find(x => x.id === 'rung4-double-observation-readout').physical_reality_established = true; }],
  ['stale empty frontier', r => { r.frontier = []; }],
  ['missing recommended node', r => { r.recommended_start = 'missing'; }],
  ['local selection failure made global prerequisite', r => { r.conjectures.find(x => x.id === 'channel-contract-and-first-assembly-step').depends_on.push('native-intrinsic-selector-audit'); }],
  ['conditional sewing promoted to all assemblies', r => { r.conjectures.find(x => x.id === 'native-joint-field-assembly-sewing').all_assemblies_established = true; }],
  ['failed scalar candidate promoted to endpoint success', r => { r.conjectures.find(x => x.id === 'scalar-global-fcc-candidate').native_endpoint_match = true; }],
  ['assembly conjecture silently proved', r => { r.conjectures.find(x => x.id === 'single-channel-esd7-assembly').status = 'proved'; }],
  ['assistant synthesis attributed to operator', r => { r.conjectures.find(x => x.id === 'assembler-as-global-evolution').proposal_origin = 'operator'; }],
  ['evolution binding inferred from assembly existence', r => { r.conjectures.find(x => x.id === 'assembler-as-global-evolution').evolution_binding_established = true; }],
  ['completed bounded task left on frontier', r => { r.frontier = ['channel-contract-and-first-assembly-step']; r.recommended_start = r.frontier[0]; }],
  ['23 records promoted to full114 channel', r => { r.conjectures.find(x => x.id === 'channel-contract-and-first-assembly-step').full114_channel_established = true; }],
  ['native fixture promoted to full esd7', r => { r.conjectures.find(x => x.id === 'channel-contract-and-first-assembly-step').full_esd7_established = true; }],
  ['geometric incidence promoted to analytical fillers', r => { r.conjectures.find(x => x.id === 'esd7-generated-geometric-channel').analytical_coherence_discharged = true; }],
  ['345-record construction promoted to114 records', r => { r.conjectures.find(x => x.id === 'esd7-generated-geometric-channel').full114_channel_established = true; }],
  ['geometric embedding promoted to global field transport', r => { r.conjectures.find(x => x.id === 'esd7-generated-geometric-channel').global_field_transport_established = true; }],
  ['prototype labels promoted to analytical fillers', r => { r.conjectures.find(x => x.id === 'esd7-analytical-prototype-bridge').analytical_coherence_discharged = true; }],
  ['prototype bridge promoted to global field transport', r => { r.conjectures.find(x => x.id === 'esd7-analytical-prototype-bridge').global_field_transport_established = true; }],
  ['synthetic gate control promoted to actual face verification', r => { r.conjectures.find(x => x.id === 'esd7-retained-face-comparison-gate').actual_face_comparison_established = true; }],
  ['synthetic controls silently presented as source operators', r => { r.conjectures.find(x => x.id === 'esd7-retained-face-comparison-gate').synthetic_controls_only = false; }],
  ['failed parent substitution promoted to refinement no-go', r => { r.conjectures.find(x => x.id === 'esd7-bare-parent-chart-substitution').refinement_impossible = true; }],
  ['failed substitution made constructive prerequisite', r => { r.conjectures.find(x => x.id === 'esd7-channel-attachment-construction').depends_on.push('esd7-bare-parent-chart-substitution'); }],
  ['structural nerve lift promoted to analytical realization', r => { r.conjectures.find(x => x.id === 'esd7-simplicial-fine-vertex-refinement').analytical_realization_established = true; }],
  ['28 lifted positions promoted to114-record producer', r => { r.conjectures.find(x => x.id === 'esd7-simplicial-fine-vertex-refinement').full114_channel_established = true; }],
  ['strict chart evaluation promoted to intended analytical witnesses', r => { r.conjectures.find(x => x.id === 'esd7-strict-parent-evaluation').intended_witness_binding_established = true; }],
  ['source inverse hypotheses promoted to fresh analytic proof', r => { r.conjectures.find(x => x.id === 'esd7-strict-parent-evaluation').source_identities_freshly_proved = true; }],
  ['joint-graph evaluation extended to independent completion', r => { r.conjectures.find(x => x.id === 'esd7-strict-parent-evaluation').completion_extension_established = true; }],
  ['formal comparison family promoted to an observer encoder', r => { r.conjectures.find(x => x.id === 'strict-native-witness-comparison').encoder_supplied = true; }],
  ['native fixture comparison promoted to full-esd7 transport', r => { r.conjectures.find(x => x.id === 'strict-native-witness-comparison').full_esd7_native_transport_established = true; }],
  ['finite packet promoted to full observer-domain encoding', r => { r.conjectures.find(x => x.id === 'finite-observer-encoder-candidate').full_observer_domain_encoded = true; }],
  ['residual reconstructibility promoted to evaluated face residual', r => { r.conjectures.find(x => x.id === 'finite-observer-encoder-candidate').specific_analytical_residual_evaluated = true; }],
  ['candidate encoder promoted to physical preparation', r => { r.conjectures.find(x => x.id === 'finite-observer-encoder-candidate').physical_preparation_established = true; }],
  ['endpoint term promoted to full regulated residual', r => { r.conjectures.find(x => x.id === 'finite-packet-signed-endpoint-form').full_regulated_residual_evaluated = true; }],
  ['signed endpoint form promoted to positivity', r => { r.conjectures.find(x => x.id === 'finite-packet-signed-endpoint-form').positivity_established = true; }],
  ['ideal signed readout promoted to apparatus evidence', r => { r.conjectures.find(x => x.id === 'finite-packet-signed-endpoint-form').physical_readout_established = true; }],
  ['chosen Volterra lift promoted to the full physical mixed polarization', r => { r.conjectures.find(x => x.id === 'finite-packet-green-trace-subproblem').full_physical_mixed_polarization_identified = true; }],
  ['seam pairing promoted to physical cutoff residual', r => { r.conjectures.find(x => x.id === 'finite-packet-green-trace-subproblem').physical_cutoff_residual_evaluated = true; }],
  ['five-reading protocol promoted to physical probes', r => { r.conjectures.find(x => x.id === 'finite-packet-green-trace-subproblem').physical_probe_protocol_established = true; }],
  ['finite trace controls promoted to physical cutoff evaluation', r => { r.conjectures.find(x => x.id === 'corrected-cutoff-observer-legs').full_physical_cutoff_evaluated = true; }],
  ['failed leg rewrite promoted to failure of unitary transport', r => { r.conjectures.find(x => x.id === 'cutoff-leg-cyclicity-shortcut').source_unitary_transport_refuted = true; }],
  ['off-diagonal bounds promoted to a diagonal finite part', r => { r.conjectures.find(x => x.id === 'archimedean-physical-cutoff-enclosures').diagonal_finite_part_evaluated = true; }],
  ['one even sector promoted to all semilocal sectors', r => { r.conjectures.find(x => x.id === 'archimedean-physical-cutoff-enclosures').all_semilocal_sectors_established = true; }],
  ['bounded packet entries promoted to full analytical filler', r => { r.conjectures.find(x => x.id === 'archimedean-physical-cutoff-enclosures').full_analytical_filler_established = true; }],
  ['finite-part formula promoted to numerical quadrature value', r => { r.conjectures.find(x => x.id === 'archimedean-centered-packet-limit').numerical_finite_part_value_computed = true; }],
  ['centered matrix convergence promoted to a higher witness', r => { r.conjectures.find(x => x.id === 'archimedean-centered-packet-limit').analytical_higher_witness_established = true; }],
  ['centered limit promoted to positivity', r => { r.conjectures.find(x => x.id === 'archimedean-centered-packet-limit').positivity_established = true; }],
  ['geometric filling substituted for Pb construction', r => { r.conjectures.find(x => x.id === 'pb208-retained-native-construction').geometric_fill_sufficient = true; }],
  ['completed Pb answer admitted as constructor input', r => { r.conjectures.find(x => x.id === 'pb208-retained-native-construction').completed_target_input_allowed = true; }],
  ['rejected substitutes promoted to task completion', r => { r.conjectures.find(x => x.id === 'pb208-process-substitution-criticism').substitutes_discharge_task = true; }],
  ['failed attempts promoted to impossibility', r => { r.conjectures.find(x => x.id === 'pb208-process-substitution-criticism').construction_impossible = true; }],
  ['native batch control promoted to Pb construction', r => { r.conjectures.find(x => x.id === 'native-retained-joint-attachment-attempt').full_pb_construction_established = true; }],
  ['primitive conflict promoted to whole-assembly refutation', r => { r.conjectures.find(x => x.id === 'native-retained-joint-attachment-attempt').whole_assembly_presentation_refuted = true; }],
  ['exploratory batching promoted to physical selection', r => { r.conjectures.find(x => x.id === 'native-retained-joint-attachment-attempt').physical_selection_established = true; }],
  ['invertible reader map promoted to native arrow', r => { r.conjectures.find(x => x.id === 'native-ne-nn-reader-comparison').native_cross_species_arrow_established = true; }],
  ['active-reader loss hidden by coefficient invertibility', r => { r.conjectures.find(x => x.id === 'native-ne-nn-reader-comparison').active_reader_only_factorization = true; }],
  ['different particle counts silently identified', r => { r.conjectures.find(x => x.id === 'native-ne-nn-reader-comparison').current_composition_readout_preserved = true; }],
  ['failed inventory candidate credited as a bridge', r => { r.conjectures.find(x => x.id === 'pb208-inventory-fibration-attempt').inventory_bridge_established = true; }],
  ['candidate failure promoted to fibration refutation', r => { r.conjectures.find(x => x.id === 'pb208-inventory-fibration-attempt').generic_fibration_refuted = true; }],
  ['candidate failure promoted to all-model no-go', r => { r.conjectures.find(x => x.id === 'pb208-inventory-fibration-attempt').all_whole_assembly_models_refuted = true; }],
  ['whole inventory credited as pair admission', r => { r.conjectures.find(x => x.id === 'pb208-native-whole-fixture-attempt').pair_binding_established = true; }],
  ['fixture binding failure promoted to all-model refutation', r => { r.conjectures.find(x => x.id === 'pb208-native-whole-fixture-attempt').all_whole_assembly_models_refuted = true; }],
  ['fixture result promoted to Pb construction', r => { r.conjectures.find(x => x.id === 'pb208-native-whole-fixture-attempt').full_pb_construction_established = true; }],
  ['N-only obstruction promoted to all native routes', r => { r.conjectures.find(x => x.id === 'pb208-octahedral-reader-atlas-attempt').all_native_routes_excluded = true; }],
  ['reader atlas promoted to whole neutron admission', r => { r.conjectures.find(x => x.id === 'pb208-octahedral-reader-atlas-attempt').whole_neutron_admission_established = true; }],
  ['finite atlas used to erase absolute histories', r => { r.conjectures.find(x => x.id === 'pb208-octahedral-reader-atlas-attempt').absolute_histories_identified = true; }],
  ['screw native sewing promoted to esd7 face binding', r => { r.conjectures.find(x => x.id === 'pb208-screw-field-attempt').actual_esd7_face_binding_established = true; }],
  ['finite capped screw promoted to infinite extension', r => { r.conjectures.find(x => x.id === 'pb208-screw-field-attempt').infinite_retained_extension_established = true; }],
  ['screw sewing promoted to Pb construction', r => { r.conjectures.find(x => x.id === 'pb208-screw-field-attempt').full_pb_construction_established = true; }],
  ['reference-envelope obstruction promoted to all geometric embeddings excluded', r => { r.conjectures.find(x => x.id === 'screw-esd7-geometric-attachment-attempt').all_geometric_embeddings_excluded = true; }],
  ['reference-envelope obstruction promoted to coherence-presentation refutation', r => { r.conjectures.find(x => x.id === 'screw-esd7-geometric-attachment-attempt').coherence_presentation_interpretation_refuted = true; }],
  ['relative native completion promoted to analytical domain extension', r => { r.conjectures.find(x => x.id === 'screw-esd7-relative-attachment-attempt').analytical_domain_extension_established = true; }],
  ['relative native attachment promoted to F006 binding', r => { r.conjectures.find(x => x.id === 'screw-esd7-relative-attachment-attempt').actual_f006_binding_established = true; }],
  ['external C0 flux promoted to endpoint-only sufficiency', r => { r.conjectures.find(x => x.id === 'external-c0-finite-trace-attempt').endpoint_only_sufficient = true; }],
  ['finite C0 trace promoted to analytical domain extension', r => { r.conjectures.find(x => x.id === 'external-c0-finite-trace-attempt').analytical_domain_extension_established = true; }],
  ['actual NE face replaced by unrelated F006', r => { r.conjectures.find(x => x.id === 'native-ne-fine-face-attempt').face = 'F006'; }],
  ['native face identity promoted to analytical homotopy', r => { r.conjectures.find(x => x.id === 'native-ne-fine-face-attempt').analytical_homotopy_established = true; }],
  ['physical readout covariance promoted to triangular filler', r => { r.conjectures.find(x => x.id === 'f736-physical-readout-attempt').analytical_face_filler_established = true; }],
  ['one physical sector promoted to all semilocal sectors', r => { r.conjectures.find(x => x.id === 'f736-physical-readout-attempt').all_semilocal_sectors_established = true; }],
  ['local role substituted for correlated-word component role', r => { r.conjectures.find(x => x.id === 'f736-correlated-word-edges-attempt').nondegenerate_component_role = 'H134'; }],
  ['conditional word realization promoted to intended homotopy', r => { r.conjectures.find(x => x.id === 'f736-correlated-word-edges-attempt').intended_homotopy_binding_established = true; }],
  ['dangling contextual reference', r => { r.conjectures.find(x => x.id === 'single-channel-esd7-assembly').related_nodes.push('missing'); }],
  ['dependency cycle', r => { r.conjectures.find(x => x.id === 'shared-edge-source').depends_on.push('persistent-seam-pe'); }]
]) {
  const bad = structuredClone(raw); mutate(bad);
  check('reject ' + name, () => assert.throws(() => boundaries(bad)));
}
const hashes = {};
for (const p of [...inputs].sort()) hashes[p] = createHash('sha256').update(await fs.readFile(path.join(root, p))).digest('hex');
const receipt = {status: 'passed', checks, check_count: checks.length, source_sha256: hashes,
  scope: 'Structural integration and typed boundaries only; conjecture remains open and no formal attempt outcome is imported.'};
const output = path.join(root, 'research/strominger/results/persistent-seam-pe-net.json');
await fs.mkdir(path.dirname(output), {recursive: true});
await fs.writeFile(output, JSON.stringify(receipt, null, 2) + '\n');
console.log(JSON.stringify({status: 'passed', checks: checks.length, result: output}));
