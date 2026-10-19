"""Live naturality-branch registration audit, not physical certification."""
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[3]
NET=ROOT/'research/strominger/contracts/packet-handoff-naturality-conjecture-net.v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-net-audit-v1.json'


def digest(p):return sha256(p.read_bytes()).hexdigest()


def audit(net):
    assert net['owner']=='marici.Strominger' and net['instruction_is_evidence'] is False
    assert net['objective']['status']=='blocked_not_complete' and net['objective']['completed'] is False
    assert net['objective']['physical_assignment_verified'] is False and net['objective']['formal_outcome'] is None
    assert net['iteration']=={'completed':10,'budget':10,'next':None}
    for key in ('unique_pair_only_handoff_selected','intrinsic_active_payload_sector_partition_constructed',
                'full_source_identity_from_pair_duality','dormant_change_preserves_full_preparation_task',
                'source_native_handoff_constructed','physical_particle_assignment_verified',
                'M_C_physical_codimension_verified','source_selected_cycle_origin','source_selected_terminal_format',
                'M_C_are_single_fixed_full_objects','stationary_two_atomic_arrow_cycle_law_constructed','primitive_phase_is_physical_clock',
                'capacity_M_identified_with_common_unmarked_spatial_main_space','neutron_geometric_module_identification_unique',
                'quadratic_electron_readout_is_full_coherent_task_equivalence',
                'proton_relative_bulk_filling_is_given_primitive_handoff',
                'neutron_twelve_geometric_edge_occurrences_are_native_alignment_channels',
                'neutron_cap_completion_preserves_full_native_task',
                'electron_native_doublet_is_ordinary_invertible_transport_top_cycle',
                'all_capacity_M_C_labels_are_same_ambient_geometric_grading',
                'opposite_edge_chart_involution_selected_by_native_stage_commands',
                'opposite_edge_chart_involution_is_natively_lifted_without_new_sign_choice',
                'pair_chart_is_full_native_C_preparation_equivalence','active_chart_atlas_selects_primitive_phase_origin',
                'native_selected_baryon_lines_are_pure_Cartan_squares','native_proton_packet_identified_with_electron_spinorial_square',
                'flat_code_transport_equals_projection_line_transport','normalized_projection_move_is_existing_native_unitary',
                'finite_line_holonomy_selects_physical_spin_or_clock',
                'circularization_preserves_full_native_preparation_task','native_baryon_corner_cycles_are_original_metric_isometries',
                'cycle_metric_change_is_only_coordinate_gauge_with_fixed_geometric_preparations',
                'character_idempotent_is_native_baryon_local_preparation','derived_corner_cycle_is_given_native_primitive',
                'native_sewing_requires_fitted_per_port_phases','native_symmetry_and_local_lines_uniquely_determine_full_protocol',
                'neutron_geometric_pair_matching_is_unique','opposite_electron_polarity_is_same_fixed_reader_task',
                'character_polarity_selects_primitive_phase_origin','branch_reversal_antiunitary_is_given_complex_linear_primitive',
                'homogeneous_source_corner_equals_centered_inverse_on_full_ambient_space',
                'zero_overlap_uniquely_selects_electron_like_role','branch_scalar_alone_determines_full_preparation_task',
                'projective_character_twists_are_original_native_protocol','source_naturality_selects_proposed_indexed_origins'):
        assert net[key] is False
    for key in ('common_metric_partial_isometry_interface_constructed','conditional_source_bound_typed_path_realizations_constructed',
                'native_base_family_path_witnesses_without_endpoint_retyping','source_native_typed_geometric_alternatives_constructed',
                'native_geometric_boundary_modules_constructed','proton_source_frame_cycle_and_relative_bulk_bridge_constructed',
                'common_metric_minimal_cover_gluing_reconstructs_native_N','electron_native_G_from_uniform_six_pair_reconstruction',
                'electron_natural_nonidentity_chart_base_involution_constructed',
                'initial_pure_square_rival_scientifically_falsified','geometric_triangle_Fourier_constructor_explains_all_baryon_mode_lines',
                'source_derived_cycle_complex_structures_and_metric_rays_constructed',
                'circularization_preserves_native_active_image_and_norm','full_protocol_equivalence_bold_conjecture_rejected',
                'native_directed_geometric_full_stage_reconstruction_constructed','native_source_envelope_disposed',
                'general_coherent_centroid_fan_identity_constructed','full_source_metric_reader_and_antilinear_transport_constructed',
                'conditional_capacity_role_windows_are_natural_with_retained_origin'):
        assert net[key] is True
    assert net['minimal_native_phase_contexts']==3
    assert net['native_active_minimum_faithful_geometric_face_cover_sizes']=={'proton':1,'neutron':1,'electron':2}
    assert net['formal_outcome'] is None and net['nonredundant_executable_continuation'] is False
    assert net['source_natural_origin_policy_count']==27
    stop=net['execution_stop'];assert stop['status']=='blocked_not_complete' and stop['scope'] and stop['reason']
    assert stop['budget_is_stop_reason'] is False and stop['no_nonredundant_executable_continuation_at_declared_scope'] is True
    assert len(stop['reopen_when'])==2 and net['objective']['native_source_investigation']=='disposed_with_constructed_interfaces_and_exact_nonselection'
    nodes={n['id']:n for n in net['conjectures']}
    assert len(nodes)==len(net['conjectures'])==45
    visiting=set();done=set()
    def visit(k):
        assert k in nodes and k not in visiting
        if k in done:return
        visiting.add(k)
        for d in nodes[k]['depends_on']:visit(d)
        visiting.remove(k);done.add(k)
    for k in nodes:visit(k)
    assert nodes['source-pair-census']['verdict']=='constructed'
    assert nodes['alignment-redundancy-distinction']['verdict']=='constructed_preparation_property'
    for key in ('pair-only-intrinsic-payload-sectors','unique-active-handoff-predicate'):
        assert nodes[key]['verdict']=='rejected_at_scope' and nodes[key]['residual']
    completed=nodes['full-source-interface-naturality']
    assert completed['status']=='resolved' and completed['verdict']=='constructed_interface_with_exact_task_boundary'
    assert completed['actionable'] is False and completed['evidence_iteration']==2
    assert nodes['native-geometric-tensor-preparations']['verdict']=='constructed_baryon_duality_and_electron_obstruction'
    assert nodes['tetrahedral-native-face-code']['verdict']=='constructed'
    assert completed['successor']=='cycle-origin-and-primitive-history'
    phase=nodes['cycle-origin-and-primitive-history']
    assert phase['status']=='resolved' and phase['verdict']=='constructed_native_windows_unselected_entry'
    assert phase['evidence_iteration']==3 and phase['actionable'] is False
    assert nodes['primitive-native-base-family-windows']['verdict']=='constructed_conditional_role_windows'
    assert nodes['stationary-two-arrow-native-law']['verdict']=='rejected_at_atomic_phase_scope'
    assert nodes['stationary-two-arrow-native-law']['residual']
    assert phase['successor']=='geometric-base-versus-fiber-role-naturality'
    geometric=nodes['geometric-base-versus-fiber-role-naturality']
    assert geometric['status']=='resolved' and geometric['verdict']=='rejected_literal_capacity_M_with_typed_alternatives'
    assert geometric['evidence_iteration']==4 and geometric['actionable'] is False
    assert nodes['proton-native-body-frame-family']['verdict']=='constructed_port_indexed_geometric_fiber'
    assert nodes['neutron-centroid-and-invariant-axis']['verdict']=='constructed_nonunique_geometric_completion'
    assert nodes['electron-quadratic-spatial-bridges']['verdict']=='constructed_quadratic_not_coherent_equivalence'
    boundary=nodes['source-native-boundary-module-and-role-grading']
    assert boundary['status']=='resolved' and boundary['verdict']=='constructed_chain_bridges_with_role_and_local_system_obstructions'
    assert boundary['evidence_iteration']==5 and boundary['actionable'] is False
    assert geometric['successor']=='source-native-boundary-module-and-role-grading'
    assert nodes['proton-native-twisted-cycle-relative-bulk']['verdict']=='constructed_G_as_native_flat_cycle_projector_and_relative_bulk_bridge'
    assert nodes['neutron-geometric-patch-boundary-native-mismatch']['verdict']=='rejected_twelve_edge_occurrences_as_native_alignment_channels'
    assert nodes['electron-code-not-invertible-transport-top-cycle']['verdict']=='rejected_ordinary_local_system_top_cycle_for_full_native_doublet'
    assert nodes['native-active-geometric-reconstruction-cover-census']['verdict']=='constructed_minimum_faithful_cover_sizes_one_one_two'
    atlas=nodes['minimal-geometric-reconstruction-cover-atlas']
    assert atlas['status']=='resolved' and atlas['verdict']=='constructed_metric_gluing_and_native_edge_atlas_with_handoff_obstructions'
    assert atlas['evidence_iteration']==6 and atlas['actionable'] is False
    assert boundary['successor']=='minimal-geometric-reconstruction-cover-atlas'
    assert nodes['common-metric-minimal-cover-return-gluing']['verdict']=='constructed_all_native_returns_from_independent_source_encoders_and_metric_cover_gluing'
    assert nodes['electron-native-six-edge-code-atlas']['verdict']=='constructed_faithful_metric_atlas_and_unique_native_equivariant_decoder'
    assert nodes['electron-opposite-edge-involution-native-lift-obstruction']['verdict']=='constructed_unique_nonidentity_base_policy_without_selected_native_spin_lift'
    assert nodes['full-preparation-and-phase-boundary-of-chart-descent']['verdict']=='rejected_pair_chart_as_full_preparation_or_primitive_phase_selector'
    lines=nodes['source-native-line-transport-versus-flat-code-atlas']
    assert lines['status']=='resolved' and lines['verdict']=='rejected_pure_square_with_geometric_Fourier_shape_and_transport_obstructions'
    assert lines['evidence_iteration']==7 and lines['actionable'] is False
    assert atlas['successor']=='source-native-line-transport-versus-flat-code-atlas'
    assert nodes['geometric-triangle-Fourier-mode-shape']['verdict']=='constructed_all30_native_lines_and_exact_shape_defects'
    assert nodes['pure-spinorial-square-baryon-rival']['verdict']=='scientifically_rejected_by_non_null_native_modes'
    assert nodes['actual-native-block-versus-projection-holonomy']['verdict']=='constructed_curved_electron_face_blocks_and_distinct_flat_baryon_code_transport'
    assert nodes['circular-helicity-control-global-sewing']['verdict']=='rejected_circular_control_as_native_local_or_global_packet'
    cycle=nodes['native-corner-cycle-metric-versus-Pauli-null-geometry']
    assert cycle['status']=='resolved' and cycle['verdict']=='constructed_cycle_metric_with_full_native_reader_obstruction'
    assert cycle['evidence_iteration']==8 and cycle['actionable'] is False
    assert lines['successor']=='native-corner-cycle-metric-versus-Pauli-null-geometry'
    assert nodes['triangle-corner-cycle-invariant-metric-and-complex-structure']['verdict']=='constructed_metric_ray_and_Euclidean_support_not_native_rotation'
    assert nodes['cycle-metric-active-equivalence-full-reader-obstruction']['verdict']=='rejected_full_task_equivalence_despite_same_active_image_norm_and_geometry'
    assert nodes['electron-equilateral-character-and-Pauli-branch']['verdict']=='constructed_equilateral_native_spatial_cycle_with_opposite_directed_Pauli_character'
    sewing=nodes['source-oriented-character-selection-and-sewing']
    assert sewing['status']=='resolved' and sewing['verdict']=='constructed_full_native_sewing_with_grouping_phase_and_polarity_boundaries'
    assert sewing['evidence_iteration']==9 and sewing['actionable'] is False
    assert cycle['successor']=='source-oriented-character-selection-and-sewing'
    assert nodes['native-directed-geometric-full-stage-reconstruction']['verdict']=='constructed_all_native_baryon_stages_without_fitted_per_port_phases'
    assert nodes['neutron-native-sewing-matching-and-phase-rivals']['verdict']=='rejected_unique_full_protocol_from_local_lines_and_native_symmetry'
    assert nodes['inverse-character-and-Pauli-polarity-reader-boundary']['verdict']=='constructed_covariant_branch_reversals_not_fixed_reader_equivalences'
    assert nodes['homogeneous-versus-centered-corner-extension']['verdict']=='constructed_same_tangent_inverse_character_with_nonzero_ambient_residual'
    next_node=nodes['source-branch-descent-of-indexed-role-windows']
    assert next_node['status']=='resolved' and next_node['verdict']=='constructed_general_fan_and_full_source_naturality_with_exact_role_origin_nonselection'
    assert next_node['actionable'] is False and next_node['source_available'] is True and next_node['evidence_iteration']==10
    assert sewing['successor']=='source-branch-descent-of-indexed-role-windows'
    assert nodes['general-centroid-fan-overlap-law']['verdict']=='constructed_general_coherent_fan_identity_not_particle_constant'
    assert nodes['native-character-stabilizer-and-null-baryon-rivals']['verdict']=='constructed_covariant_null_baryons_and_rejected_scalar_role_selector'
    assert nodes['full-source-semilinear-reader-naturality']['verdict']=='constructed_full_metric_action_reader_and_antilinear_transport'
    assert nodes['natural-capacity-windows-with-unselected-indexed-origins']['verdict']=='constructed_eleven_protocol_windows_with_twentyseven_natural_origin_policies'
    disposed=nodes['native-source-envelope-disposition']
    assert disposed['verdict']=='disposed_native_constructors_and_nonselection_with_external_reopening_gate'
    assert disposed['status']=='resolved' and disposed['evidence_iteration']==10 and disposed['actionable'] is False
    assert next_node['successor']==disposed['id'] and len(disposed['reopen_when'])==2
    assert net['frontier']==[] and net['recommended_start'] is None
    blocked=nodes['grounded-indexed-handoff-law']
    assert blocked['status']=='open' and blocked['actionable'] is False
    assert blocked['depends_on']==[disposed['id']] and blocked['blocker']['status']=='requires_new_source_attachment'
    assert len(blocked['blocker']['missing'])==2
    references={NET.relative_to(ROOT).as_posix(),Path(__file__).resolve().relative_to(ROOT).as_posix(),net['parent_net'],net['indexed_conjecture']}
    references.update(next_node['source_paths'])
    assert len(net['iterations'])==10
    results=[]
    for number,(iteration,count) in enumerate(zip(net['iterations'],(17,21,24,23,23,25,31,28,30,36)),1):
        assert iteration['number']==number and iteration['status']=='checks_passed' and iteration['exact_check_groups']==count
        assert iteration['positive'] and iteration['negative'] and iteration['task_boundary']
        assert iteration['physical_assignment_verified'] is False
        references.update(iteration[k] for k in ('contract','receipt','prospective_freeze','packet'))
        result=json.loads((ROOT/iteration['receipt']).read_text(encoding='utf-8'))
        assert result['status']=='pass' and result['iteration']==number
        assert len(result['checks'])==count and all(result['checks'].values())
        assert all(digest(ROOT/p)==h for p,h in result['source_sha256'].items()),'stale iteration science'
        references.update(result['source_sha256']);results.append(result)
    first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth=results
    expected={'proton':[1,11,2,22],'neutron':[1,2,11,22],'electron':[2,2,0,4]}
    assert {n:r['joint_dimensions'] for n,r in first['source_pair_census'].items()}==expected
    assert first['source_intrinsic_preparation_redundancy_distinction_constructed'] is True
    for key in ('unique_handoff_mode_selected_by_projection_pair','intrinsic_active_payload_M_C_partition_constructed',
                'full_source_geometry_identified_by_joint_signature','physical_particle_assignment_verified','source_native_handoff_constructed'):
        assert first[key] is False
    auto=first['electron_automorphism_obstruction']
    assert auto['commutant_dimension']==1 and auto['group_generated_by_order_three_elements']==24
    assert auto['whole_dormant_alignment_extension_preserves_all_native_actions']==24
    dormant=first['dormant_alignment_countermodel']
    assert dormant['same_active_return_operator'] is dormant['same_active_metric_and_stage_action'] is True
    assert dormant['same_full_preparation_readers'] is dormant['changed_source_is_native_original'] is False
    assert dormant['whole_dormant_extension']['all24_original_native_spin_face_actions_preserved'] is True
    assert dormant['whole_dormant_extension']['same_full_preparation_readers'] is False
    assert {n:r['M_C_dimensions'] for n,r in second['native_interfaces'].items()}=={'proton':[3,12],'neutron':[3,12],'electron':[2,4]}
    for key in ('conditional_source_bound_typed_path_realizations_constructed','common_partial_isometry_interface_constructed'):
        assert second[key] is True
    for key in ('source_selected_cycle_origin','source_selected_terminal_format','full_C_task_identified_with_return_code',
                'source_native_handoff_constructed','physical_particle_assignment_verified'):
        assert second[key] is False
    assert second['electron_native_face_code']['effect_linear_span_dimension']==4
    assert second['native_action_squares']['electron']['checked_actions']==24
    tensor=second['geometric_tensor_preparations']['tensor_rank_identity']
    assert tensor['proton']['independent_tensor_preparation'] is tensor['neutron']['independent_tensor_preparation'] is True
    assert tensor['electron']['independent_tensor_preparation'] is False
    tasks=second['cycle_tasks']
    assert tasks['proton']['role_by_phase_with_declared_N_adapter']==tasks['electron']['role_by_phase_with_declared_N_adapter']
    policy=tasks['electron']['encode_then_persist_vs_decode']
    assert policy['equal_all_raw_endpoint_readers_for_every_M_input'] is True
    assert policy['equivalent_full_M_and_full_C_preparation_tasks'] is False
    assert third['native_base_family_path_witnesses_without_endpoint_retyping'] is True
    assert third['pure_proton_source_assembler_executed_in_memory'] is True
    for key in ('source_selected_proposed_window_origins','M_C_are_single_fixed_full_objects',
                'stationary_two_atomic_arrow_cycle_law_constructed','initial_phase_recoverable_from_active_payload_alone',
                'source_native_handoff_constructed','physical_particle_assignment_verified','native_producer_entrypoints_executed'):
        assert third[key] is False
    assert third['source_reconstruction']['proton_pure_constructor']['exact_typed_manifest_match'] is True
    assert third['native_action_square_counts']=={'proton':2,'neutron':1,'electron':24}
    assert third['proposed_window_initial_phases']=={'proton':1,'neutron':1,'electron':2}
    assert {n:r['phase_dimensions'] for n,r in third['typed_phase_protocols'].items()}=={'proton':[36,12,3],'neutron':[36,3,12],'electron':[8,4,2]}
    for row in third['typed_phase_protocols'].values():
        assert row['primitive_N_output_remains_full_raw_type'] is True
        assert row['minimal_role_preserving_deterministic_phase_states']==3
        assert row['role_partition_is_markov_at_atomic_phase_clock'] is False
        assert all(s['minimal_phase_and_role_period']==3 for s in row['two_atomic_arrow_strobes'])
    assert third['history_comparison']['electron']['native_archive_has_alignment_entry_field'] is False
    assert {n:r['dimension'] for n,r in fourth['M_to_spatial_Hom'].items()}=={'proton':0,'neutron':3,'electron':0}
    assert fourth['source_native_typed_geometric_alternatives_constructed'] is True
    for key in ('capacity_M_identified_with_common_unmarked_spatial_main_space','neutron_geometric_module_identification_unique',
                'quadratic_electron_readout_is_full_coherent_task_equivalence','source_native_handoff_constructed',
                'physical_particle_assignment_verified','native_producers_executed'):
        assert fourth[key] is False
    p=fourth['proton_native_body_frame_family'];n=fourth['neutron_native_centroid_and_axis'];e=fourth['electron_quadratic_spatial_bridges']
    assert p['marked_evaluation_invertible_count']==p['source_spatial_group_size']==12 and p['unmarked_sum']==[]
    assert n['centroid_rank']==2 and n['centroid_annihilates_active_return'] is True
    assert n['completions_have_opposite_active_axis_sign'] is n['equal_metric_calibration_up_to_common_positive_scale'] is True
    assert e['density_bridge_Hom']['dimension']==e['symmetric_square_bridge_Hom']['dimension']==1
    assert e['native_action_count']==24 and e['quadratic_readout_is_coherent_packet_equivalence'] is False
    assert e['symbolic_quadratic_identities']['identities_checked_symbolically'] is True
    assert e['density_reconstruction_is_full_matrix_identity'] is True
    bases=fifth['geometric_boundary_modules']
    assert {n:b['betti'] for n,b in bases.items()}=={'proton':[1,0,1],'neutron':[1,1,0],'electron':[1,0,1]}
    assert {n:b['counts'] for n,b in bases.items()}=={'proton':[8,18,12],'neutron':[12,30,18],'electron':[4,6,4]}
    for base in bases.values():
        assert all(p['base_dimension']==2 and p['codimension_in_fixed_ambient3']==1 and p['betti']==[1,0,0] for p in base['native_local_port_patches'])
    assert {n:r['untwisted_active_boundary_rank'] for n,r in fifth['ordinary_boundary_native_encoder_comparison'].items()}=={'proton':1,'neutron':1,'electron':2}
    p=fifth['proton_native_flat_cycle_and_bulk_bridge']
    assert p['G_is_exact_metric_projector_onto_twisted_boundary_cycles'] is p['N_is_local_line_selected_subspace_of_twisted_cycles'] is True
    assert p['cycle_kernel_dimension']==p['relative_bulk_H3_with_native_vector_fiber']==3
    assert p['bulk_boundary_restrict_then_L_equals_native_N_on_all_raw_inputs'] is True
    assert p['bulk_filling_is_a_given_primitive_protocol_operation'] is False
    n=fifth['neutron_patch_boundary_and_rim']
    assert [n['geometric_patch_to_boundary_rank'],n['native_M_to_C_rank']]==[3,1]
    assert [n['geometric_boundary_occurrence_fixed_dimension'],n['native_C_fixed_dimension']]==[4,12]
    assert [n['uncapped_relative_bulk_H3'],n['uncapped_relative_bulk_H2']]==[0,1]
    assert n['two_cap_completion_betti']==[1,0,1] and n['cap_completion_is_same_native_preparation_task'] is False
    e=fifth['electron_invertible_local_system_obstruction']
    assert len(e['zero_face_nonzero_global_code_witnesses'])==4 and e['dual_face_graph_connected'] is True
    assert e['ordinary_invertible_transport_cycle_model_for_entire_native_doublet'] is False
    assert e['general_sheaf_or_noninvertible_code_constraint_model_excluded'] is False
    covers=fifth['minimal_geometric_reconstruction_covers']
    assert {n:r['minimum_faithful_face_count'] for n,r in covers.items()}==net['native_active_minimum_faithful_geometric_face_cover_sizes']
    assert {n:len(r['minimal_covers']) for n,r in covers.items()}=={'proton':12,'neutron':18,'electron':6}
    for key in ('all_capacity_M_C_labels_are_same_ambient_geometric_grading','neutron_cap_completion_preserves_full_native_task',
                'electron_native_doublet_is_ordinary_invertible_transport_top_cycle','source_native_handoff_constructed',
                'physical_particle_assignment_verified','native_producers_executed'):
        assert fifth[key] is False
    glue=sixth['metric_minimal_cover_gluing']
    assert all(r['native_return_reconstructed_on_all_raw_inputs'] and r['all_stage_actions_on_active_chart_values_are_identity'] for r in glue.values())
    assert {n:r['uniform_average_is_native_return'] for n,r in glue.items()}=={'proton':True,'neutron':False,'electron':True}
    assert glue['neutron']['uniform_return_minus_native']
    a=sixth['electron_native_edge_chart_atlas']
    assert len(a['charts'])==6 and a['coordinate_cocycles_checked']==a['nonmonomial_gauge_cocycles_checked']==216
    assert a['native_chart_action_squares']==144 and a['native_group_multiplication_and_base_action_checks']==576
    assert a['central_minus_retained_at_every_chart'] is True and a['raw_Euclidean_chart_transitions_are_isometries'] is False
    assert a['uniform_six_pair_decoder_average_equals_native_decoder_on_all_raw_inputs'] is True
    assert a['full_C_to_logical_Hom']['dimension']==1 and a['equivariant_retraction_unique_at_actual_native_module_scope'] is True
    assert len(a['pair_raw_decoder_full_C_counterexamples'])==6 and a['pair_chart_is_full_native_C_preparation_equivalence'] is False
    assert a['density_only_equivariant_edge_selector_obstruction']['no_fixed_pair'] is True
    policies=sixth['source_equivariant_chart_successors_and_native_lift']
    assert [policies[n]['equivariant_bijective_base_successor_count'] for n in ('proton','neutron')]==[12,524880]
    e=policies['electron']
    assert len(e['equivariant_base_endomorphisms'])==2 and e['unique_nonidentity_base_policy_is_complement'] is True
    assert [e['complement_coordinate_return_order'],e['stabilizer_native_spin_order']]==[2,4]
    assert e['native_stabilizer_conjugates_every_complement_move_to_its_negative'] is True
    assert e['conjugation_equivariant_native_spin_lift_of_complement_exists'] is e['coordinate_complement_is_given_primitive_command'] is False
    assert all(r['all_chart_values_are_still_insufficient_for_phase_origin'] for r in sixth['chart_reader_phase_obstruction'].values())
    for key in ('common_metric_minimal_cover_gluing_reconstructs_native_N','electron_native_G_from_uniform_six_pair_reconstruction',
                'electron_natural_nonidentity_chart_base_involution_constructed'):
        assert sixth[key] is True
    for key in ('opposite_edge_chart_involution_selected_by_native_stage_commands',
                'opposite_edge_chart_involution_is_natively_lifted_without_new_sign_choice',
                'pair_chart_is_full_native_C_preparation_equivalence','active_chart_atlas_selects_primitive_phase_origin',
                'source_native_handoff_constructed','physical_particle_assignment_verified','native_producers_executed'):
        assert sixth[key] is False
    types=seventh['geometric_mode_line_types']
    assert [types[n]['pure_Cartan_square_count'] for n in ('proton','neutron')]==[0,0]
    assert [types[n]['nondecomposable_symmetric_matrix_count'] for n in ('proton','neutron')]==[12,18]
    assert types['proton']['circularity_classes'][0]['value']=={'0':'16/25'}
    assert all(r['ordered_geometric_Fourier_line_matches_native'] for n in types.values() for r in n['lines'])
    sew=seventh['local_spinorial_square_and_global_sewing']
    assert sew['matched_helicity'] is None and sew['pure_square_rival_rejected'] is True
    assert sew['native_elliptic_overlap_weights']=={'negative_Pauli_square':{'0':'1/5'},'positive_Pauli_square':{'0':'4/5'}}
    assert sew['circular_controls_are_native_proton_local_lines'] is False
    assert len(sew['three_distinct_ellipse_projectors_per_face_and_rank2_average'])==4
    assert all(not r['local_L_preserves_adapter'] and r['source_G_and_N_annihilate_entire_quadratic_module'] for r in sew['both_helicity_sewing_adapters'])
    h=seventh['tetrahedral_line_holonomy_and_native_word_comparison']
    assert all(r['normalized_phase']=={'8':'-1'} for r in h['electron_oriented_loops'])
    assert len(h['electron_projection_moves_not_native_spin_unitary_restrictions'])==12
    assert h['circular_control_is_actual_native_proton_mode'] is False
    assert h['circular_control_projection_connection_gauge_equivalent_to_flat_body_connection'] is False
    tr=seventh['baryon_native_block_and_projection_transport']
    assert [tr[n]['nontrivial_projection_cycles_in_declared_spanning_tree_basis'] for n in ('proton','neutron')]==[7,6]
    assert all(len(r['fundamental_cycles'])==7 and all(c['native_code_phase']=={'0':'1'} for c in r['fundamental_cycles']) for r in tr.values())
    assert seventh['initial_pure_square_rival_scientifically_falsified'] is True
    assert seventh['geometric_triangle_Fourier_constructor_explains_all_baryon_mode_lines'] is True
    assert net['iterations'][6]['preserved_failed_source']==seventh['failed_rival_source']
    for key in ('local_source_spinorial_square_relation_constructed','native_proton_packet_identified_with_electron_spinorial_square',
                'normalized_projection_move_is_existing_native_unitary','flat_code_transport_equals_projection_line_transport',
                'finite_line_holonomy_selects_physical_spin_or_clock','source_native_handoff_constructed',
                'physical_particle_assignment_verified','native_producers_executed'):
        assert seventh[key] is False
    assert eighth['invariant_plane_metric_ray']['dimension']==1
    assert eighth['S3_relabelling_checks']==204 and eighth['native_spatial_metric_squares']==294
    readers=eighth['cycle_metric_full_native_reader_comparison']
    assert readers['proton']['reader_residual_ranks']=={'L':12,'G':0,'N':1}
    assert readers['neutron']['reader_residual_ranks']=={'L':3,'G':0,'N':1}
    for name,count in (('proton',12),('neutron',18)):
        r=readers[name];assert len(r['all_conjugate_port_preparation_witnesses'])==count
        assert r['original_G_preserved'] is r['native_active_image_and_its_metric_preserved'] is True
        assert r['original_L_and_N_preserved_on_all_raw_inputs'] is r['original_L_commutes_with_derived_corner_cycle'] is False
        assert r['metric_change_is_only_coordinate_gauge_with_fixed_preparations'] is False
        assert all(w['native_return_decoded_scalar'] and not w['cycle_metric_return_decoded_scalar'] and w['native_L_output_nonzero'] and w['cycle_metric_L_output_zero'] for w in r['all_conjugate_port_preparation_witnesses'])
    assert all(r['outward_ordered_triangle_character_matches']=='opposite_positive_Pauli_square' and r['inverse_character_matches']=='native_negative_Pauli_square' for r in eighth['electron_oriented_character_branches'])
    for key in ('source_derived_cycle_complex_structures_and_metric_rays_constructed',
                'circularization_preserves_native_active_image_and_norm','full_protocol_equivalence_bold_conjecture_rejected'):
        assert eighth[key] is True
    for key in ('circularization_preserves_full_native_preparation_task','native_baryon_corner_cycles_are_original_metric_isometries',
                'cycle_metric_change_is_only_coordinate_gauge_with_fixed_geometric_preparations',
                'character_idempotent_is_native_baryon_local_preparation','derived_corner_cycle_is_given_native_primitive',
                'source_native_handoff_constructed','physical_particle_assignment_verified','native_producers_executed'):
        assert eighth[key] is False
    reconstruction=ninth['full_native_geometric_reconstruction']
    assert reconstruction['proton']['native_vector_to_geometric_Fourier_global_scale']=={'0':'-1/10'}
    assert reconstruction['neutron']['native_vector_to_geometric_Fourier_global_scale']=={'0':'1'}
    assert all(r['all_L_G_N_reconstructed_on_all_raw_inputs'] and r['no_per_port_phase_fit'] for r in reconstruction.values())
    reversal=ninth['proton_directed_seed_reversal']
    assert reversal['original_typed_transfers']==reversal['reversed_typed_transfers']==1836
    assert reversal['entire_reversed_protocol_equals_conjugate_after_port_adapter'] is True
    assert reversal['source_arrow_reversal_is_not_the_same_directed_input'] is True
    assert len(ninth['proton_homogeneous_versus_centered_corner_extensions'])==12
    assert all(r['rank']==1 and r['homogeneous_minus_centered_inverse'] for r in ninth['proton_homogeneous_versus_centered_corner_extensions'])
    matching=ninth['neutron_geometric_matching_rival']
    assert len(matching['matchings'])==2 and matching['same_G_and_N'] is matching['same_original_metric_and_geometry'] is True
    assert matching['L_reader_witness']['difference_rank']==4 and matching['L_reader_witness']['old_output']!=matching['L_reader_witness']['new_output']
    phase=ninth['native_phase_sewing_and_rival']
    assert {n:r['scalar_equivariant_phase_parameters'] for n,r in phase['native_port_phase_orbit_census'].items()}=={'proton':1,'neutron':6,'electron':1}
    rival=phase['neutron_nonconstant_orbit_phase']
    assert rival['source_metric_G_and_native_actions_preserved'] is rival['all_local_selected_projectors_preserved'] is rival['stage_supports_preserved'] is True
    assert [rival['L_difference_rank'],rival['N_difference_rank']]==[6,2]
    assert rival['fixed_geometric_Fourier_representatives_preserved'] is False
    assert rival['N_reader_witness']['old_output']!=rival['N_reader_witness']['new_output']
    branches=ninth['inverse_character_and_Pauli_polarity_rivals']
    assert branches['proton']['inverse_character_residual_ranks']=={'L':24,'G':0,'N':2}
    assert branches['neutron']['inverse_character_residual_ranks']=={'L':6,'G':0,'N':2}
    assert all(branches[n]['conjugate_return_overlap']=={'0':'16/25'} and branches[n]['branch_reversal_antilinear_square']=='+I' for n in ('proton','neutron'))
    assert branches['electron']['opposite_Pauli_polarity_residual_ranks']=={'L':8,'G':4,'N':4}
    assert branches['electron']['opposite_rank2_returns_are_orthogonal'] is branches['electron']['all24_native_geometry_action_squares'] is True
    assert branches['electron']['branch_reversal_antilinear_square']=='-I'
    assert branches['electron']['native_negative_vs_positive_polarization_eigenvalues']==[-1,1]
    assert {n:r['source_derived_directed_seam_comparisons'] for n,r in ninth['source_derived_geometric_seam_comparisons'].items()}=={'proton':36,'neutron':48}
    assert ninth['native_directed_geometric_full_stage_reconstruction_constructed'] is ninth['pure_proton_assembler_executed_in_memory'] is True
    for key in ('native_sewing_requires_fitted_per_port_phases','native_symmetry_and_local_lines_uniquely_determine_full_protocol',
                'neutron_geometric_pair_matching_is_unique','opposite_electron_polarity_is_same_fixed_reader_task',
                'character_polarity_selects_primitive_phase_origin','branch_reversal_antiunitary_is_given_complex_linear_primitive',
                'source_native_handoff_constructed','physical_particle_assignment_verified','native_producer_entrypoints_executed','formal_proof_recompiled'):
        assert ninth[key] is False
    fan=tenth['general_centroid_fan_coefficient_certificate']
    assert fan['bilinear_coefficients']==[{'0':'-4'}]*3 and fan['Hermitian_coefficients']==[{'0':'5'}]*3
    assert [len(fan['native_comparisons'][n]['fans']) for n in ('proton','neutron')]==[4,6]
    assert all(r['native_bilinear_over_norm']=={'0':'-4/5'} and r['native_overlap']=={'0':'16/25'} for r in fan['native_comparisons'].values())
    phase=tenth['neutron_native_covariant_face_phase_family'];assert phase['same_native_G_actions_metric_local_lines_and_stage_supports'] is True
    assert [r['overlap'] for r in phase['variants']]==[{'0':'16/25'},{'0':'16/25'},{},{'0':'4/25'}]
    assert all(r['reader_residual_ranks']=={'L':6,'G':0,'N':2} and r['N_reader_witness']['old_output']!=r['N_reader_witness']['new_output'] for r in phase['variants'][1:])
    chars=tenth['scalar_port_character_and_stabilizer_classification']
    assert [len(chars[n]['allowed_scalar_port_character_branches']) for n in ('proton','neutron','electron')]==[3,3,1]
    assert [chars[n]['independent_unit_phases_per_allowed_character'] for n in ('proton','neutron','electron')]==[1,6,1]
    assert all(r['reader_residual_ranks']=={'L':0,'G':6,'N':2} and r['overlap']=={} for r in chars['proton']['branch_reader_residuals'])
    assert all(r['reader_residual_ranks']=={'L':6,'G':24,'N':2} and r['overlap']=={} for r in chars['neutron']['branch_reader_residuals'])
    assert chars['electron']['central_minus_is_an_actual_commutator'] is chars['electron']['all_linear_spin_characters_factor_through_spatial_A4'] is True
    transports=tenth['full_source_coordinate_naturality']
    assert all(r['full_raw_geometric_reader_and_native_action_squares'] and r['branch_scalar_before']==r['correctly_transported_scalar'] and not r['naive_untransported_comparison_is_equal'] for r in transports.values())
    assert transports['proton']['untransported_branch_scalar']=={'0':'5329/8100'}
    assert transports['electron']['untransported_branch_scalar']=={'0':'-13/768'}
    role=tenth['source_branch_and_primitive_role_descent'];assert len(role['source_family_rectangular_protocols'])==11
    assert len(role['source_neutral_origin_policies'])==27 and len({tuple(p) for p in role['source_neutral_origin_policies']})==27
    assert role['policy_matching_requested_words_if_those_words_are_imposed']==[1,1,2]
    assert role['all27_policies_preserve_frame_naturality_and_primitive_guards_when_origin_is_retained'] is True
    assert role['naturality_selects_that_policy'] is role['character_branch_selects_primitive_origin'] is False
    assert all(r['all_native_action_and_full_reader_squares'] and r['minimal_primitive_phase_contexts']==r['two_atomic_arrow_strobe_role_period']==3 for r in role['source_family_rectangular_protocols'])
    correction=tenth['scope_correction'];assert correction['first_frozen_checker_sha256']=='55a0a2b664bdea02eb2a7020ed263e16b7de802ad0233c4917f49d14d047391e'
    assert net['iterations'][9]['preserved_failed_source']==correction['first_frozen_checker']
    for key in ('general_coherent_centroid_fan_identity_constructed','full_source_metric_reader_and_antilinear_transport_constructed',
                'conditional_capacity_role_windows_are_natural_with_retained_origin'):
        assert tenth[key] is True
    for key in ('zero_overlap_uniquely_selects_electron_like_role','branch_scalar_alone_determines_full_preparation_task',
                'projective_character_twists_are_original_native_protocol','source_naturality_selects_proposed_indexed_origins',
                'stationary_two_atomic_arrow_law_constructed','physical_M_C_grading_constructed','source_native_handoff_constructed',
                'physical_particle_assignment_verified','native_producer_entrypoints_executed','pure_proton_assembler_executed_in_memory','formal_proof_recompiled'):
        assert tenth[key] is False
    assert len(tenth['reopening_gate'])==2
    for path in references:assert (ROOT/path).is_file(),path
    return references


def main():
    net=json.loads(NET.read_text(encoding='utf-8'));references=audit(net)
    cases=(('premature_completion',lambda n:n['objective'].update(completed=True)),
        ('pair_predicate_promoted_to_unique_handoff',lambda n:n.update(unique_pair_only_handoff_selected=True)),
        ('payload_split_promoted',lambda n:n.update(intrinsic_active_payload_sector_partition_constructed=True)),
        ('pair_duality_promoted_to_full_identity',lambda n:n.update(full_source_identity_from_pair_duality=True)),
        ('dormant_change_promoted_to_same_task',lambda n:n.update(dormant_change_preserves_full_preparation_task=True)),
        ('native_handoff_promoted',lambda n:n.update(source_native_handoff_constructed=True)),
        ('physical_assignment_promoted',lambda n:n.update(physical_particle_assignment_verified=True)),
        ('fabricated_executable_frontier_after_scoped_disposition',lambda n:n.update(frontier=['source-branch-descent-of-indexed-role-windows'])),
        ('cycle_origin_promoted',lambda n:n.update(source_selected_cycle_origin=True)),
        ('terminal_format_promoted',lambda n:n.update(source_selected_terminal_format=True)),
        ('physical_codimension_promoted',lambda n:n.update(M_C_physical_codimension_verified=True)),
        ('constructed_interface_erased',lambda n:n.update(common_metric_partial_isometry_interface_constructed=False)),
        ('raw_local_full_types_identified',lambda n:n.update(M_C_are_single_fixed_full_objects=True)),
        ('window_promoted_to_two_arrow_cycle',lambda n:n.update(stationary_two_atomic_arrow_cycle_law_constructed=True)),
        ('primitive_phase_promoted_to_physical_clock',lambda n:n.update(primitive_phase_is_physical_clock=True)),
        ('three_phase_context_erased',lambda n:n.update(minimal_native_phase_contexts=2)),
        ('capacity_M_promoted_to_geometric_main',lambda n:n.update(capacity_M_identified_with_common_unmarked_spatial_main_space=True)),
        ('neutron_axis_sign_promoted_to_unique',lambda n:n.update(neutron_geometric_module_identification_unique=True)),
        ('quadratic_readout_promoted_to_coherent_equivalence',lambda n:n.update(quadratic_electron_readout_is_full_coherent_task_equivalence=True)),
        ('typed_geometric_alternatives_erased',lambda n:n.update(source_native_typed_geometric_alternatives_constructed=False)),
        ('flat_bulk_adapter_promoted_to_primitive_handoff',lambda n:n.update(proton_relative_bulk_filling_is_given_primitive_handoff=True)),
        ('neutron_twelve_occurrences_promoted_to_native_channels',lambda n:n.update(neutron_twelve_geometric_edge_occurrences_are_native_alignment_channels=True)),
        ('cap_completion_promoted_to_same_task',lambda n:n.update(neutron_cap_completion_preserves_full_native_task=True)),
        ('spinor_code_promoted_to_ordinary_local_system_cycle',lambda n:n.update(electron_native_doublet_is_ordinary_invertible_transport_top_cycle=True)),
        ('capacity_roles_promoted_to_common_ambient_grading',lambda n:n.update(all_capacity_M_C_labels_are_same_ambient_geometric_grading=True)),
        ('source_flat_cycle_bridge_erased',lambda n:n.update(proton_source_frame_cycle_and_relative_bulk_bridge_constructed=False)),
        ('single_electron_face_promoted_to_faithful_cover',lambda n:n['native_active_minimum_faithful_geometric_face_cover_sizes'].update(electron=1)),
        ('source_metric_gluing_erased',lambda n:n.update(common_metric_minimal_cover_gluing_reconstructs_native_N=False)),
        ('native_six_pair_decoder_erased',lambda n:n.update(electron_native_G_from_uniform_six_pair_reconstruction=False)),
        ('nonidentity_chart_policy_promoted_to_source_selected',lambda n:n.update(opposite_edge_chart_involution_selected_by_native_stage_commands=True)),
        ('coordinate_complement_promoted_to_native_spin_lift',lambda n:n.update(opposite_edge_chart_involution_is_natively_lifted_without_new_sign_choice=True)),
        ('pair_chart_promoted_to_full_C_preparation',lambda n:n.update(pair_chart_is_full_native_C_preparation_equivalence=True)),
        ('active_atlas_promoted_to_primitive_phase_selector',lambda n:n.update(active_chart_atlas_selects_primitive_phase_origin=True)),
        ('pure_square_falsifier_erased',lambda n:n.update(initial_pure_square_rival_scientifically_falsified=False)),
        ('geometric_Fourier_shape_rule_erased',lambda n:n.update(geometric_triangle_Fourier_constructor_explains_all_baryon_mode_lines=False)),
        ('elliptical_baryons_promoted_to_pure_Cartan_squares',lambda n:n.update(native_selected_baryon_lines_are_pure_Cartan_squares=True)),
        ('circular_control_promoted_to_native_proton_packet',lambda n:n.update(native_proton_packet_identified_with_electron_spinorial_square=True)),
        ('flat_code_identified_with_projection_transport',lambda n:n.update(flat_code_transport_equals_projection_line_transport=True)),
        ('normalized_block_promoted_to_native_unitary',lambda n:n.update(normalized_projection_move_is_existing_native_unitary=True)),
        ('finite_holonomy_promoted_to_physical_spin_clock',lambda n:n.update(finite_line_holonomy_selects_physical_spin_or_clock=True)),
        ('cycle_metric_constructor_erased',lambda n:n.update(source_derived_cycle_complex_structures_and_metric_rays_constructed=False)),
        ('cycle_metric_active_norm_agreement_erased',lambda n:n.update(circularization_preserves_native_active_image_and_norm=False)),
        ('full_equivalence_falsifier_erased',lambda n:n.update(full_protocol_equivalence_bold_conjecture_rejected=False)),
        ('cycle_metric_promoted_to_same_full_native_task',lambda n:n.update(circularization_preserves_full_native_preparation_task=True)),
        ('baryon_corner_cycle_promoted_to_native_spatial_isometry',lambda n:n.update(native_baryon_corner_cycles_are_original_metric_isometries=True)),
        ('metric_change_promoted_to_fixed_preparation_gauge',lambda n:n.update(cycle_metric_change_is_only_coordinate_gauge_with_fixed_geometric_preparations=True)),
        ('oblique_character_idempotent_promoted_to_native_preparation',lambda n:n.update(character_idempotent_is_native_baryon_local_preparation=True)),
        ('derived_corner_cycle_promoted_to_primitive',lambda n:n.update(derived_corner_cycle_is_given_native_primitive=True)),
        ('full_geometric_stage_reconstruction_erased',lambda n:n.update(native_directed_geometric_full_stage_reconstruction_constructed=False)),
        ('relative_phase_fit_inserted_without_source',lambda n:n.update(native_sewing_requires_fitted_per_port_phases=True)),
        ('local_lines_and_symmetry_promoted_to_unique_protocol',lambda n:n.update(native_symmetry_and_local_lines_uniquely_determine_full_protocol=True)),
        ('neutron_pair_matching_promoted_to_unique',lambda n:n.update(neutron_geometric_pair_matching_is_unique=True)),
        ('opposite_Pauli_polarity_promoted_to_same_fixed_reader_task',lambda n:n.update(opposite_electron_polarity_is_same_fixed_reader_task=True)),
        ('character_polarity_promoted_to_primitive_origin',lambda n:n.update(character_polarity_selects_primitive_phase_origin=True)),
        ('branch_antiunitary_promoted_to_complex_linear_primitive',lambda n:n.update(branch_reversal_antiunitary_is_given_complex_linear_primitive=True)),
        ('tangent_cycle_equality_promoted_to_full_ambient_equality',lambda n:n.update(homogeneous_source_corner_equals_centered_inverse_on_full_ambient_space=True)),
        ('general_fan_identity_erased',lambda n:n.update(general_coherent_centroid_fan_identity_constructed=False)),
        ('zero_overlap_promoted_to_unique_electron_role',lambda n:n.update(zero_overlap_uniquely_selects_electron_like_role=True)),
        ('branch_scalar_promoted_to_full_task_identity',lambda n:n.update(branch_scalar_alone_determines_full_preparation_task=True)),
        ('full_source_semilinear_transport_erased',lambda n:n.update(full_source_metric_reader_and_antilinear_transport_constructed=False)),
        ('character_twist_promoted_to_original_native_protocol',lambda n:n.update(projective_character_twists_are_original_native_protocol=True)),
        ('conditional_marked_capacity_windows_erased',lambda n:n.update(conditional_capacity_role_windows_are_natural_with_retained_origin=False)),
        ('naturality_promoted_to_unique_indexed_origin',lambda n:n.update(source_naturality_selects_proposed_indexed_origins=True)),
        ('twentyseven_policies_reduced_to_one_without_source',lambda n:n.update(source_natural_origin_policy_count=1)),
        ('native_envelope_disposition_erased',lambda n:n.update(native_source_envelope_disposed=False)),
        ('budget_exhaustion_substituted_for_scientific_stop',lambda n:n['execution_stop'].update(budget_is_stop_reason=True)),
        ('fabricated_nonredundant_continuation',lambda n:n.update(nonredundant_executable_continuation=True)),
        ('external_reopening_gate_erased',lambda n:n['execution_stop'].update(reopen_when=[])))
    hostiles={}
    for name,mutate in cases:
        bad=deepcopy(net);mutate(bad)
        try:audit(bad)
        except AssertionError:hostiles[name]=True
        else:raise AssertionError('accepted hostile '+name)
    report={'schema':'marici.packet-handoff-naturality-net-audit.v1','status':'pass',
        'iteration_completed':10,'iteration_budget':10,'scientific_check_groups':258,
        'iteration_check_groups':[17,21,24,23,23,25,31,28,30,36],'subconjectures':45,'next_executable_node':None,
        'native_source_envelope_disposed':True,'objective_status':'blocked_not_complete','nonredundant_executable_continuation_at_declared_scope':False,
        'objective_complete':False,'hostiles':hostiles,'registration_audit_only':True,'physical_assignment_verified':False,
        'source_sha256':{p:digest(ROOT/p) for p in sorted(references)}}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))


if __name__=='__main__':main()
