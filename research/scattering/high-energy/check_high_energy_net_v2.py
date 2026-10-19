"""Validate sharpened propositions and historical source boundaries, not physics."""
import argparse
import copy
import json
from pathlib import Path
from fractions import Fraction
from zipfile import ZipFile
from high_energy_scattering_net import ROOT,HOME,validate as historical_validate,digest

CONTRACT=HOME/'contracts/high-energy-scattering-conjectures.v2.json'
RESULT=HOME/'results/high-energy-conjectures.v2.json'


def validate(net):
    assert net['schema']=='marici.scattering.high-energy-conjectures.v2'
    assert net['physical_explanation_outcome'] is None and net['objective']['outcome'] is None
    nodes={n['id']:n for n in net['conjectures']}
    assert len(nodes)==len(net['conjectures'])==10
    assert {n['label'] for n in nodes.values()}=={'H'+str(i) for i in range(1,11)}
    assert net['objective']['target'] in nodes
    graph={k:[] for k in nodes}
    for n in nodes.values():
        assert n['status']==('refuted' if n['label'] in ('H9','H10') else 'established' if n['label'] in ('H1','H2','H3','H4','H5') else 'open')
        if n['label']=='H9':assert n['result']['certificate']=='research/scattering/high-energy/results/high-energy-conjectures.v2.json'
        assert all(n.get(k) for k in ('statement','quantifiers','falsifier','sources','next_action'))
        assert 'acceptance' not in n
    edges=set()
    for e in net['edges']:
        assert e['from'] in nodes and e['to'] in nodes and e['kind'] in ('premise','target_definition')
        key=(e['from'],e['to'],e['kind']);assert key not in edges;edges.add(key)
        graph[e['from']].append(e['to'])
    assert ('local-full-spinor-switch','ordered-switch-composition','premise') in edges
    assert ('fixed-contact-self-adjointness','prepared-packet-continuity','target_definition') in edges
    assert not any(e['from']=='fixed-response-quadrature-one-percent' and e['to']=='packet-refinement-limit' for e in net['edges'])
    active=set();done=set()
    def visit(k):
        assert k not in active
        if k in done:return
        active.add(k)
        for child in graph[k]:visit(child)
        active.remove(k);done.add(k)
    for k in graph:visit(k)
    assert len(net['deferred_obligations'])==3
    assert all(x['id'] not in nodes for x in net['deferred_obligations'])
    return nodes


def audit():
    net=json.loads(CONTRACT.read_text(encoding='utf-8'));nodes=validate(net)
    old,pins,_=historical_validate()
    assert net['supersedes']=='research/scattering/high-energy/contracts/high-energy-scattering-conjecture-net.v1.json'
    assert net['source_pins']==old['source_pins']
    for n in nodes.values():
        assert set(n['sources'])<=set(pins['sources'])
    refused=[]
    for mode in ('promote','erase-quantifier','conflate-models','promote-finite-refinement'):
        bad=copy.deepcopy(net)
        if mode=='promote':next(n for n in bad['conjectures'] if n['label']=='H6')['status']='established'
        elif mode=='erase-quantifier':bad['conjectures'][0].pop('quantifiers')
        elif mode=='conflate-models':
            next(e for e in bad['edges'] if e['from']=='fixed-contact-self-adjointness')['kind']='premise'
        else:bad['edges'].append({'from':'fixed-response-quadrature-one-percent','to':'packet-refinement-limit','kind':'premise','reason':'hostile shortcut'})
        try:validate(bad)
        except (AssertionError,KeyError):refused.append(mode)
        else:raise AssertionError('hostile accepted: '+mode)
    with ZipFile(HOME/'pentachoron_exit_gate_bundle.zip') as archive:
        matrices=json.loads(archive.read('pentachoron_exit_gate_results.json'))['exact_matrices']
    traces={k:sum(Fraction(row[i]) for i,row in enumerate(matrices[k])) for k in ('HL','HR','Hi','H0','M')}
    assert traces['HL']==136 and traces['HR']==120 and traces['M']==16
    assert traces['Hi']-traces['H0']==traces['HL']-traces['HR']==traces['M']
    assert nodes['participant-exchange-coherence']['definition']=='research/scattering/high-energy/EXIT-AND-EXCHANGE-CONJECTURES.md'
    h1=nodes['local-full-spinor-switch']['result']
    assert h1['checker']=='research/scattering/high-energy/check_local_switches.py'
    assert h1['certificate']=='research/scattering/high-energy/results/local-full-spinor-switches.v1.json'
    receipt=json.loads((ROOT/h1['certificate']).read_text(encoding='utf-8'))
    assert receipt['status']=='pass' and receipt['endpoint_count']==2 and receipt['local_blocks_checked']==16
    for path in (h1['checker'],'research/scattering/high-energy/pentachoron_joint_incoming_bundle.zip'):
        assert receipt['source_sha256'][path]==digest(ROOT/path),'stale H1 certificate source'
    h3=nodes['retained-switch-continuation']['result']
    assert h3['checker']=='research/scattering/high-energy/check_retained_encoder.py'
    assert h3['certificate']=='research/scattering/high-energy/results/retained-encoder.v1.json'
    assert h3['proof']=='research/scattering/high-energy/RETAINED-ENCODER-PROOF.md'
    receipt3=json.loads((ROOT/h3['certificate']).read_text(encoding='utf-8'))
    assert receipt3['status']=='pass' and receipt3['unitary_cycle_links_checked']==10
    assert receipt3['H_post_equals_H_F'] is False
    for path,value in receipt3['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H3 certificate source'
    h2=nodes['ordered-switch-composition']['result']
    assert h2['checker']=='research/scattering/high-energy/check_ordered_composition.py'
    assert h2['certificate']=='research/scattering/high-energy/results/ordered-switch-composition.v1.json'
    receipt2=json.loads((ROOT/h2['certificate']).read_text(encoding='utf-8'))
    assert receipt2['status']=='pass' and receipt2['endpoint_count']==2
    assert receipt2['local_identities_replayed'] is True
    for path,value in receipt2['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H2 certificate source'
    attempt=nodes['prepared-packet-continuity']['attempt']
    assert attempt['disposition']=='inconclusive_for_full_scope'
    assert attempt['receipt']=='research/scattering/high-energy/results/packet-continuity-pilot.v1.json'
    pilot=json.loads((ROOT/attempt['receipt']).read_text(encoding='utf-8'))
    assert pilot['status']=='pass' and len(pilot['records'])==10
    assert pilot['tolerance_is_certified_error_bound'] is False
    for path,value in pilot['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H5 pilot audit'
    h4=nodes['fixed-contact-self-adjointness']['result']
    assert h4['certificate']=='research/scattering/high-energy/results/open-hinge-form.v1.json'
    assert h4['proof']=='research/scattering/high-energy/OPEN-HINGE-FORM-PROOF.md'
    assert h4['checker']=='research/scattering/high-energy/check_open_hinge_form.py'
    form=json.loads((ROOT/h4['certificate']).read_text(encoding='utf-8'))
    assert form['status']=='pass' and form['machine_checked_analytic_proof'] is False
    assert form['finite_record_dimensions']==[168,168]
    for path,value in form['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H4 proof/source binding'
    h10=nodes['participant-exchange-coherence']['result']
    assert h10['certificate']=='research/scattering/high-energy/results/participant-exchange.v1.json'
    assert h10['checker']=='research/scattering/high-energy/check_participant_exchange.py'
    assert h10['proof']=='research/scattering/high-energy/PARTICIPANT-EXCHANGE-OBSTRUCTION.md'
    exchange=json.loads((ROOT/h10['certificate']).read_text(encoding='utf-8'))
    assert exchange['H10_disposition']=='refuted_in_declared_source_constructor_admission_scope'
    assert exchange['universal_exchange_impossibility_claimed'] is False
    assert len(exchange['records'])==2 and all(r['squared_Frobenius_norm']=='25/9' for r in exchange['records'])
    for path,value in exchange['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H10 source obstruction'
    h5=nodes['prepared-packet-continuity']['result']
    assert h5['certificate']=='research/scattering/high-energy/results/response128-continuity.v1.json'
    assert h5['checker']=='research/scattering/high-energy/check_response128_continuity.py'
    assert h5['proof']=='research/scattering/high-energy/PACKET-CONTINUITY-PROOF.md'
    continuity=json.loads((ROOT/h5['certificate']).read_text(encoding='utf-8'))
    assert continuity['status']=='pass' and len(continuity['stationary_records'])==17
    assert continuity['certified_response_error_bound'] is False
    for path,value in continuity['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H5 response128 binding'
    h7=nodes['uniform-corrected-residual-stability']['attempt']
    assert h7['disposition']=='inconclusive'
    assert h7['receipt']=='research/scattering/high-energy/results/resolvent-certificate-attempt.v1.json'
    resolvent=json.loads((ROOT/h7['receipt']).read_text(encoding='utf-8'))
    assert resolvent['status']=='pass' and resolvent['uniform_source_inverse_certified'] is False
    assert resolvent['reported_gap_candidate_is_certified'] is False
    for path,value in resolvent['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 partial certificate audit'
    assert h7['corrected_residual_receipt']=='research/scattering/high-energy/results/corrected-native-leakage.v1.json'
    native=json.loads((ROOT/h7['corrected_residual_receipt']).read_text(encoding='utf-8'))
    assert native['status']=='pass' and native['native_and_interaction_sum_is_full_residual'] is False
    for path,value in native['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 corrected native component'
    assert h7['radial_receipt']=='research/scattering/high-energy/results/radial-envelope.v1.json'
    radial=json.loads((ROOT/h7['radial_receipt']).read_text(encoding='utf-8'))
    assert radial['status']=='pass' and radial['source_gap_certified'] is False
    assert radial['full_coupled_inverse_certified'] is False
    for path,value in radial['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 radial envelope binding'
    assert h7['matching_receipt']=='research/scattering/high-energy/results/corrected-matching-residual.v1.json'
    matching=json.loads((ROOT/h7['matching_receipt']).read_text(encoding='utf-8'))
    assert matching['status']=='pass' and matching['envelope_is_certified'] is False
    assert matching['full_inverse_certified'] is False and matching['full_band_residual_evaluated'] is False
    for path,value in matching['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 central matching audit'
    assert h7['inertia_receipt']=='research/scattering/high-energy/results/inertia-margin.v1.json'
    inertia=json.loads((ROOT/h7['inertia_receipt']).read_text(encoding='utf-8'))
    assert inertia['status']=='pass' and inertia['inertia_certified'] is False
    assert inertia['source_omitted_gap_certified'] is False
    assert inertia['candidate_margin_positive'] is False
    for path,value in inertia['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 inertia-margin attempt'
    assert h7['threshold_receipt']=='research/scattering/high-energy/results/inertia-thresholds.v1.json'
    thresholds=json.loads((ROOT/h7['threshold_receipt']).read_text(encoding='utf-8'))
    assert thresholds['status']=='pass' and thresholds['spectral_gap_certified'] is False
    assert thresholds['retained_response_basis_changed'] is False
    for row in [thresholds]+thresholds['candidates']:
        for path,value in row['source_sha256'].items():
            assert digest(ROOT/path)==value,'stale H7 lower-threshold search'
    assert h7['roundoff_receipt']=='research/scattering/high-energy/results/inertia-roundoff-screen.v1.json'
    roundoff=json.loads((ROOT/h7['roundoff_receipt']).read_text(encoding='utf-8'))
    assert roundoff['status']=='pass' and roundoff['interval_certificate'] is False
    assert roundoff['source_gap_certified'] is False
    assert roundoff['roundoff_margin_model_positive'] is False
    for path,value in roundoff['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 arithmetic screen'
    assert h7['inverse_factor_receipt']=='research/scattering/high-energy/results/inverse-factor-reconstruction.v1.json'
    inverse_factor=json.loads((ROOT/h7['inverse_factor_receipt']).read_text(encoding='utf-8'))
    assert inverse_factor['status']=='pass' and inverse_factor['interval_certificate'] is False
    assert inverse_factor['source_gap_certified'] is False
    assert inverse_factor['factor_robustness_margin_model_positive'] is False
    for path,value in inverse_factor['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 inverse-factor reconstruction'
    assert h7['ball_receipt']=='research/scattering/high-energy/results/ball-factor-residual.v1.json'
    ball=json.loads((ROOT/h7['ball_receipt']).read_text(encoding='utf-8'))
    assert ball['status']=='pass' and ball['factor_residual_enclosed_for_binary_reference'] is True
    assert ball['source_assembly_error_enclosed'] is False and ball['inertia_certified'] is False
    assert ball['source_gap_certified'] is False and h7['budget_status']=='exhausted_eight_cycles'
    for path,value in ball['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H7 ball-factor residual'
    successor=nodes['uniform-corrected-residual-stability']['successor_attempt']
    assert successor['id']=='VF1' and successor['disposition']=='exhausted_inconclusive_full_H7'
    assert successor['budget_cycles']==3 and successor['execution_cycles_spent']==3
    controls=json.loads((ROOT/successor['receipt']).read_text(encoding='utf-8'))
    assert controls['status']=='pass' and controls['source_H7_certified'] is False
    for path,value in controls['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale VF1 design/controls'
    Dblocks=json.loads((ROOT/successor['D_block_receipt']).read_text(encoding='utf-8'))
    assert Dblocks['status']=='pass' and Dblocks['binary_D_inertia_certified'] is True
    assert Dblocks['blocks_covered']==49 and Dblocks['negative_inertia_sum']==130
    assert Dblocks['original_source_gap_certified'] is False and Dblocks['verified_inverse_factor_bound'] is False
    for path,value in Dblocks['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale VF1 D-block certificate'
    inverse_verified=json.loads((ROOT/successor['inverse_receipt']).read_text(encoding='utf-8'))
    assert inverse_verified['status']=='pass' and inverse_verified['leading_factor_inverse_certified'] is True
    assert inverse_verified['block_rows_covered']==41 and inverse_verified['full_binary_factor_inverse_certified'] is False
    assert inverse_verified['original_source_gap_certified'] is False
    for path,value in inverse_verified['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale VF1 leading inverse certificate'
    binary_inertia=json.loads((ROOT/successor['binary_inertia_receipt']).read_text(encoding='utf-8'))
    assert binary_inertia['status']=='pass' and binary_inertia['binary_shifted_H_inertia_certified'] is True
    assert binary_inertia['negative_inertia']==130 and binary_inertia['zero_inertia']==0
    assert binary_inertia['total_rows_verified']==49
    assert binary_inertia['original_source_assembly_enclosed'] is False and binary_inertia['retained_spectral_frame_certified'] is False
    assert binary_inertia['full_band_coupled_inverse_certified'] is False
    for path,value in binary_inertia['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale VF1 binary inertia certificate'
    bridge=nodes['uniform-corrected-residual-stability']['reference_bridge_attempt']
    assert bridge['id']=='RB1' and bridge['budget_cycles']==2 and bridge['execution_cycles_spent']==2
    assert bridge['disposition']=='exhausted_inconclusive_full_H7'
    reference=json.loads((ROOT/bridge['receipt']).read_text(encoding='utf-8'))
    assert reference['status']=='pass' and reference['exact_radical_shift_binary_H_inertia_certified'] is True
    assert reference['source_assembly_certified'] is False and reference['true_ground_energy_enclosed'] is False
    assert reference['retained_spectral_frame_certified'] is False and reference['full_band_coupled_inverse_certified'] is False
    for path,value in reference['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale RB1 exact pose bridge'
    frame=json.loads((ROOT/bridge['frame_receipt']).read_text(encoding='utf-8'))
    assert frame['status']=='pass' and frame['binary_eigenvalue_proximity_certified'] is True
    assert frame['true_ground_identity_certified'] is False and frame['source_assembly_certified'] is False
    assert frame['retained_420_spectral_projector_certified'] is False and frame['full_band_coupled_inverse_certified'] is False
    for path,value in frame['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale RB1 source/frame audit'
    assembly=nodes['uniform-corrected-residual-stability']['assembly_bridge_attempt']
    assert assembly['id']=='AB1' and assembly['budget_cycles']==2 and assembly['execution_cycles_spent']==2
    assert assembly['disposition']=='exhausted_inconclusive_full_H7'
    terminal=json.loads((ROOT/assembly['receipt']).read_text(encoding='utf-8'))
    assert terminal['status']=='pass' and terminal['assembled_reference_inertia_certified'] is True
    assert terminal['blocks_covered']==49 and terminal['negative_inertia']==130
    assert terminal['native_geometry_samples_enclosed'] is False and terminal['original_source_assembly_certified'] is False
    assert terminal['retained_frame_certified'] is False and terminal['full_band_coupled_inverse_certified'] is False
    for path,value in terminal['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale AB1 conditional assembly'
    native=json.loads((ROOT/assembly['native_geometry_receipt']).read_text(encoding='utf-8'))
    assert native['status']=='pass' and native['native_geometry_certified_on_binary_centered_vertices'] is True
    assert native['native_samples_covered']==1225 and native['assembled_geometry_reference_inertia_certified'] is True
    assert native['upstream_vertex_centering_reference_certified'] is False and native['original_source_model_certified'] is False
    assert native['retained_frame_certified'] is False and native['full_band_coupled_inverse_certified'] is False
    for path,value in native['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale AB1 native geometry bridge'
    vertex=nodes['uniform-corrected-residual-stability']['vertex_frame_attempt']
    assert vertex['id']=='VB1' and vertex['budget_cycles']==2 and vertex['execution_cycles_spent']==1
    exact_vertex=json.loads((ROOT/vertex['receipt']).read_text(encoding='utf-8'))
    assert exact_vertex['status']=='pass' and exact_vertex['exact_radical_vertex_centering_enclosed'] is True
    assert exact_vertex['native_source_geometry_assembly_inertia_certified'] is True
    assert exact_vertex['true_ground_identity_certified'] is False and exact_vertex['retained_frame_certified'] is False
    assert exact_vertex['full_band_coupled_inverse_certified'] is False
    for row in (exact_vertex,exact_vertex['native_bridge']):
        for path,value in row['source_sha256'].items():
            assert digest(ROOT/path)==value,'stale VB1 exact vertex bridge'
    h6=nodes['fixed-response-quadrature-one-percent']['attempt']
    assert h6['runner']=='research/scattering/high-energy/run_quadrature_refinement.py'
    assert h6['job_record']=='research/scattering/high-energy/results/quadrature33-job.v1.json'
    assert h6['disposition']=='numerically_supported_pending_error_bounds'
    assert h6['receipt']=='research/scattering/high-energy/results/quadrature-review.v1.json'
    review=json.loads((ROOT/h6['receipt']).read_text(encoding='utf-8'))
    assert review['all_three_numerical_inequalities_pass'] is True
    assert review['solver_to_observable_error_certified'] is False
    assert review['global_peak_interval_certified'] is False
    for path,value in review['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H6 review source'
    assert h6['peak_receipt']=='research/scattering/high-energy/results/peak-enclosure.v1.json'
    peak=json.loads((ROOT/h6['peak_receipt']).read_text(encoding='utf-8'))
    assert peak['status']=='pass' and peak['binary_kernel_global_peak_localized'] is True
    assert peak['stationary_solver_error_certified'] is False and peak['exact_moment_weights_certified'] is False
    for path,value in peak['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H6 binary peak enclosure'
    assert h6['readout_receipt']=='research/scattering/high-energy/results/readout-enclosures.v1.json'
    readout=json.loads((ROOT/h6['readout_receipt']).read_text(encoding='utf-8'))
    assert readout['status']=='pass' and readout['all_three_stored_binary_readout_inequalities_certified'] is True
    assert readout['stationary_solver_error_certified'] is False and readout['exact_preparation_certified'] is False
    for path,value in readout['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H6 readout enclosure'
    assert h6['preparation_receipt']=='research/scattering/high-energy/results/preparation-enclosure.v1.json'
    preparation=json.loads((ROOT/h6['preparation_receipt']).read_text(encoding='utf-8'))
    assert preparation['status']=='pass' and preparation['exact_moment_preparation_enclosed_on_binary_grid'] is True
    assert preparation['stationary_solver_error_certified'] is False and preparation['exact_model_energy_nodes_enclosed'] is False
    for path,value in preparation['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H6 preparation enclosure'
    assert h6['prepared_readout_receipt']=='research/scattering/high-energy/results/prepared-readouts.v1.json'
    prepared=json.loads((ROOT/h6['prepared_readout_receipt']).read_text(encoding='utf-8'))
    assert prepared['status']=='pass' and prepared['exact_moment_preparation_propagated_on_binary_grid'] is True
    assert prepared['all_three_prepared_stored_kernel_inequalities_certified'] is True
    assert prepared['stationary_solver_error_certified'] is False and prepared['exact_model_energy_reference_certified'] is False
    for path,value in prepared['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H6 prepared readout enclosure'
    assert h6['preconditioner_receipt']=='research/scattering/high-energy/results/finite-preconditioner.v1.json'
    preconditioner=json.loads((ROOT/h6['preconditioner_receipt']).read_text(encoding='utf-8'))
    assert preconditioner['status']=='pass' and preconditioner['inverse_bound_certified'] is False
    assert preconditioner['stationary_solver_error_certified'] is False and preconditioner['full_band_covered'] is False
    for path,value in preconditioner['source_sha256'].items():
        assert digest(ROOT/path)==value,'stale H6 finite-preconditioner screen'
    assert h6['polynomial_receipt']=='research/scattering/high-energy/results/polynomial-preconditioner.v1.json'
    polynomial=json.loads((ROOT/h6['polynomial_receipt']).read_text(encoding='utf-8'))
    assert polynomial['status']=='pass' and polynomial['operator_norm_upper_bound_certified'] is False
    assert polynomial['stationary_solver_error_certified'] is False and h6['budget_status']=='exhausted_six_cycles'
    assert h6['bounded_outcome']=='inconclusive'
    for row in (polynomial,polynomial['finite_response_audit']):
        for path,value in row['source_sha256'].items():
            assert digest(ROOT/path)==value,'stale H6 polynomial screen'
    comparison_path='research/scattering/high-energy/results/quadrature17-vs33.v1.json'
    comparison=json.loads((ROOT/comparison_path).read_text(encoding='utf-8'))
    kernels='research/scattering/high-energy/results/quadrature33-kernels.v1.npz'
    assert digest(ROOT/kernels)==comparison['kernel_sha256']
    # Live job state is deliberately not frozen into this mathematical receipt.
    cache_manifest='research/scattering/high-energy/results/scattering-replay-cache.v1.json'
    cache_archive='research/scattering/high-energy/results/scattering-replay-cache.v1.zip'
    cache=json.loads((ROOT/cache_manifest).read_text(encoding='utf-8'))
    assert digest(ROOT/cache_archive)==cache['archive_sha256'],'damaged durable replay cache'
    sources={vertex['protocol'],vertex['checker'],vertex['receipt'],vertex['geometry_snapshot']}|{assembly['native_geometry_review'],assembly['native_geometry_checker'],assembly['native_geometry_receipt'],assembly['native_geometry_inputs']}|{assembly['protocol'],assembly['checker'],assembly['receipt'],assembly['native_samples']}|{bridge['frame_audit'],bridge['frame_checker'],bridge['frame_receipt']}|{bridge['protocol'],bridge['checker'],bridge['receipt']}|{successor['binary_inertia_receipt'],successor['binary_inertia_checker'],successor['binary_inertia_review']}|{successor['inverse_receipt'],successor['inverse_checker'],successor['inverse_review'],successor['inverse_frontier']}|{successor['D_block_receipt'],successor['D_block_checker'],successor['D_block_review'],successor['factor_witness']}|{successor['protocol'],successor['checker'],successor['receipt']}|{h6['polynomial_receipt'],h6['polynomial_checker'],h6['polynomial_review']}|{h6['preconditioner_receipt'],h6['preconditioner_checker'],h6['preconditioner_review']}|{h6['prepared_readout_receipt'],h6['prepared_readout_checker'],h6['prepared_readout_review']}|{h6['preparation_receipt'],h6['preparation_checker'],h6['preparation_review']}|{h6['readout_receipt'],h6['readout_checker'],h6['readout_review']}|{h6['peak_receipt'],h6['peak_checker'],h6['peak_review']}|{h7['ball_receipt'],h7['ball_checker'],h7['ball_review']}|{h7['inverse_factor_receipt'],h7['inverse_factor_checker'],h7['inverse_factor_review']}|{h7['roundoff_receipt'],h7['roundoff_checker'],h7['roundoff_review']}|{h7['threshold_receipt'],h7['threshold_checker'],h7['threshold_review']}|{h7['inertia_receipt'],h7['inertia_checker'],h7['inertia_review']}|{cache_manifest,cache_archive,'research/scattering/high-energy/REPLAY-MAINTENANCE.md','research/scattering/high-energy/preserve_replay_cache.py','research/scattering/high-energy/receipt_replay.py'}|{h7['matching_receipt'],h7['matching_checker'],h7['matching_review']}|{h7['radial_receipt'],h7['radial_checker'],h7['radial_review']}|{h7['corrected_residual_receipt'],h7['corrected_residual_checker'],h7['corrected_residual_review']}|{h6['runner'],h6['review'],h6['checker'],h6['receipt'],comparison_path,kernels,'research/scattering/high-energy/QUADRATURE-REFINEMENT-RUN.md'}|{h7['receipt'],h7['checker'],h7['proof']}|{h5['certificate'],h5['checker'],h5['proof']}|{h10['certificate'],h10['checker'],h10['proof']}|{h4['certificate'],h4['checker'],h4['proof'],attempt['receipt'],attempt['checker'],attempt['proof']}|{h1['checker'],h1['certificate'],h2['checker'],h2['certificate'],h3['checker'],h3['certificate'],h3['proof']}|set(pins['sources'])|{CONTRACT.relative_to(ROOT).as_posix(),net['supersedes'],net['source_pins'],Path(__file__).relative_to(ROOT).as_posix(),nodes['participant-exchange-coherence']['definition']}
    return {'schema':'marici.scattering.high-energy-conjectures-validation.v2','status':'pass',
            'propositions':len(nodes),'edges':len(net['edges']),'deferred_obligations':len(net['deferred_obligations']),
            'source_sha256':{p:digest(ROOT/p) for p in sorted(sources)},'hostiles_refused':refused,
            'H9_trace_obstruction':{'exact_traces':{k:str(v) for k,v in traces.items()},'invertible_intertwiner_impossible':True,'archived_matrix_diagonals_freshly_summed':True,'producer_replayed':False},
            'historical_contract_and_pins_validated':True,'source_solvers_replayed':False,
            'H5_audit':'Analytic all-time downstream identity, with separate pilot and response128 source-binding audits; numerical audits not rerun by this validator.',
            'proof_outcomes_admitted':True,'mathematical_results_validated':['H1 established','H2 established','H3 established','H4 established (analytic proof)','H5 established (downstream identity)','H9 refuted','H10 refuted (constructor admission)'],'H1_exact_checker_replayed_by_this_validator':False,'H2_exact_checker_replayed_by_this_validator':False,'H3_exact_checker_replayed_by_this_validator':False,'physical_explanation_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit();text=json.dumps(result,indent=2)+'\n'
    if args.check:
        assert RESULT.exists() and RESULT.read_text(encoding='utf-8')==text,'stale validation receipt'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','propositions','edges','deferred_obligations','hostiles_refused','proof_outcomes_admitted')}))


if __name__=='__main__':main()
