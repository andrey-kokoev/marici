"""Audit omitted-branch evidence without importing it as new net outcomes.

Replays the shape finite audit in a temporary sandbox. Pentachoron archive and
native-descendant receipts are inspected, not scientifically rerun.
"""
import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
BASE=ROOT/'research/voevodsky'
ARCHIVE=ROOT/'research/scattering/high-energy/pentachoron_autonomous_contact_bundle.zip'
RESULT=HOME/'results/branch-evidence.v1.json'
NOTE=HOME/'BRANCH-EVIDENCE.md'
ADAPTER_REPLAY=HOME/'results/adapter-reproduction.v1.json'
PENTA_GROUND=HOME/'results/pentachoron-ground-sector.v1.json'
PENTA_REVIEW=HOME/'results/pentachoron-threshold-review.v1.json'
SCALAR_COMPARISON=HOME/'results/scalar-c-native-comparison.v1.json'
THREE_HIDDEN=HOME/'results/three-hidden-native-interpolant.v1.json'
GROUND_PROJECTION=HOME/'results/ground-preserving-native-projection.v1.json'
PROJECTION_TIME_ERROR=HOME/'results/native-projection-time-error.v1.json'
PROJECTION_ON_SHELL=HOME/'results/native-projection-on-shell-error.v1.json'
PROJECTION_FULL_BAND=HOME/'results/native-projection-full-band-obstruction.v1.json'
RESONANT_ENRICHMENT=HOME/'results/resonant-native-enrichment.v1.json'
ENRICHED_BOUND=HOME/'results/enriched-bound-sector.v1.json'
CARRIER_WEIGHTS=HOME/'results/carrier-retained-weights.v1.json'
NAMED_WEIGHTS=HOME/'results/named-preparation-weights.v1.json'


def sha(data):return hashlib.sha256(data).hexdigest()
def load(path):return json.loads(path.read_text(encoding='utf-8'))


def validate_boundary(boundary):
    assert boundary['pentachoron_model']=='autonomous_point_contact_20_plus_20'
    assert boundary['shape_model']=='finite_E_C_2_3'
    for key in ('lineage_is_model_identity','numerical_report_is_threshold_proof','new_proposition_outcomes_admitted','physical_output_identified'):
        assert boundary[key] is False,'invalid scope promotion: '+key


def build():
    boundary={'pentachoron_model':'autonomous_point_contact_20_plus_20','shape_model':'finite_E_C_2_3',
              'lineage_is_model_identity':False,'numerical_report_is_threshold_proof':False,
              'new_proposition_outcomes_admitted':False,'physical_output_identified':False}
    validate_boundary(boundary)
    refused=[]
    for key in ('lineage_is_model_identity','numerical_report_is_threshold_proof','new_proposition_outcomes_admitted','physical_output_identified'):
        bad=copy.deepcopy(boundary);bad[key]=True
        try:validate_boundary(bad)
        except AssertionError:refused.append(key)
        else:raise AssertionError('scope hostile accepted: '+key)
    paths={Path(__file__),NOTE,ARCHIVE,
           ROOT/'research/scattering/high-energy/pentachoron_autonomous_contact_note.md',
           ROOT/'research/scattering/high-energy/pentachoron_geometric_entrance_note.md',
           HOME/'contracts/low-energy-scattering-work-net.v3.json',
           HOME/'contracts/low-energy-scattering-conjectures.v4.json'}
    # Do not extract/execute the high-energy source archive or spend its live protocol.
    with zipfile.ZipFile(ARCHIVE) as z:
        manifest=json.loads(z.read('SHA256.json'))
        for name,h in manifest.items():assert sha(z.read(name))==h,'archive member drift: '+name
        penta=json.loads(z.read('pentachoron_autonomous_contact_results.json'))
        assert penta['script_sha256']==sha(z.read('pentachoron_autonomous_contact.py'))
        assert penta['check_count']==len(penta['checks'])
        assert all(c['passed'] is True for c in penta['checks'])
        for c in penta['checks']:
            if 'residual' in c and 'tolerance' in c:assert abs(c['residual'])<=c['tolerance']
        archive_audit={'member_sha256':manifest,'reported_checks':len(penta['checks']),
                       'reported_check_kinds':dict(sorted(Counter(c['kind'] for c in penta['checks']).items())),
                       'source_script_binding_verified':True,'scientific_solver_replayed':False,
                       'first_excitation_threshold_reported':penta['first_excitation_threshold_exact'],
                       'threshold_theorem_imported':False}
    ground=json.loads(PENTA_GROUND.read_text(encoding='utf-8'))
    assert ground['status']=='pass' and ground['ground_dimension']==4
    assert ground['ground_contact_rank']==ground['ground_contact_kernel_dimension']==2
    assert ground['Ho_minus_ground_psd_rank']==16 and ground['bright_threshold_regularity_proved'] is False
    assert ground['symbolic_receipt_sha256']=='256b0a03239fb3e86053d8b905a8d5ed551a212484343fb24aacf3ec7fcbc1d5'
    for relative,h in ground['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale exact ground certificate: '+relative
        paths.add(path)
    paths.add(PENTA_GROUND)
    reviewed=load(PENTA_REVIEW)
    assert reviewed['scope_verdict']=='established' and reviewed['physical_outcomes_admitted'] is False
    assert reviewed['protocol']['remaining_effort_units']==0 and reviewed['protocol']['renewed'] is False
    for relative,h in reviewed['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale C12 review: '+relative
        paths.add(path)
    paths.add(PENTA_REVIEW)
    # Exactly the supplied checker and its supplied note, executed outside the
    # repository; no monkey-patching and no owner receipt writes.
    checker=BASE/'checkers/check_shape_interaction_finite_operators.py'
    source=BASE/'braid-composition-effective-shape-interaction-operators.md'
    stored=BASE/'results/shape_interaction_finite_operators.json'
    paths.update((checker,source,stored))
    with tempfile.TemporaryDirectory(prefix='low-energy-shape-audit-') as temp:
        sandbox=Path(temp);(sandbox/'checkers').mkdir();(sandbox/'results').mkdir()
        shutil.copy2(checker,sandbox/'checkers'/checker.name);shutil.copy2(source,sandbox/source.name)
        subprocess.run([sys.executable,str(sandbox/'checkers'/checker.name)],check=True,
                       capture_output=True,text=True,timeout=120)
        fresh=load(sandbox/'results'/stored.name)
    assert fresh==load(stored),'shape finite replay differs from stored owner receipt'
    assert fresh['verification_passed'] is True and all(v is True for v in fresh['checks'].values())
    shape_audit={'finite_checks_freshly_replayed':len(fresh['checks']),
                 'owner_receipt_reproduced_exactly':True,'covered_note_sections':fresh['covered_note_sections'],
                 'complete_35_section_investigation_certified':False,
                 'lineage_relation':'declared_native_successor_not_model_identity'}
    lineage=[];drifts=[]
    for name,note in (
        ('native_rim_phase_adapter','native-rim-phase-adapter.md'),
        ('native_adapter_collective_closure','native-adapter-collective-closure.md'),
        ('native_joint_generator_resolvent','native-joint-generator-resolvent.md'),
        ('native_port_scattering','native-port-scattering.md')):
        receipt=BASE/'results'/f'{name}.json';r=load(receipt)
        assert r['verification_passed'] is True and all(v is True for v in r['checks'].values())
        bindings={};mismatches=[]
        for relative,h in r['source_hashes'].items():
            p=BASE/relative;actual=sha(p.read_bytes());paths.add(p)
            if actual==h:bindings[p.relative_to(ROOT).as_posix()]=h
            else:
                finding={'receipt':receipt.relative_to(ROOT).as_posix(),'source':p.relative_to(ROOT).as_posix(),
                         'expected_sha256':h,'actual_sha256':actual}
                mismatches.append(finding);drifts.append(finding)
        paths.update((receipt,BASE/note))
        lineage.append({'receipt':receipt.relative_to(ROOT).as_posix(),'source_hashes_verified':bindings,
                        'source_hash_mismatches':mismatches,'scientific_checker_replayed':False})
    # Separate current-source replay: verify its bindings without pretending
    # that this checker executed the adapter or refreshed historical parents.
    replay=load(ADAPTER_REPLAY)
    assert replay['status']=='pass_scoped_reproduction' and replay['matching_mathematical_payload'] is True
    assert replay['passed_checks']==24 and replay['historical_receipt_rewritten'] is False
    assert replay['historical_source_binding_fresh'] is False and replay['all_ancestors_reproduced'] is False
    for relative,h in replay['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale current-adapter replay: '+relative
        paths.add(path)
    paths.add(ADAPTER_REPLAY)
    assert len(drifts)==len(replay['provenance_differences'])==1
    difference=replay['provenance_differences'][0]
    assert drifts[0]['source']=='research/voevodsky/'+difference['source']
    assert drifts[0]['expected_sha256']==difference['historical_sha256']
    assert drifts[0]['actual_sha256']==difference['current_sha256']
    # These are different operator libraries, not contradictory closure claims.
    collective=load(BASE/'results/native_adapter_collective_closure.json')
    joint=load(BASE/'results/native_joint_generator_resolvent.json')
    port=load(BASE/'results/native_port_scattering.json')
    assert collective['collective_minimal_closure_dimension']==9
    assert collective['independent_local_input_closure_dimension']==27
    assert joint['joint_cyclic_dimension']==11 and joint['hidden_dimension']==8
    assert port['central_source_dimension']==11 and port['retained_hidden_dimension']==8
    current=load(HOME/'contracts/low-energy-scattering-conjectures.v4.json')
    c2=next(n for n in current['conjectures'] if n['label']=='C2')
    assert 'research/voevodsky/native-port-scattering.md' in c2['sources']
    for name in ('shape-interaction-finite-operator-audit.md','braid-shape-interaction-implications.md'):
        paths.add(BASE/name)
    comparison=load(SCALAR_COMPARISON)
    assert comparison['scope_verdict']=='quantitative_obstruction_in_declared_class'
    assert comparison['endpoint_error_floor']=='1/8192' and comparison['candidate_hidden_dimension_maximum']==2
    assert comparison['physical_outcomes_admitted'] is False and comparison['all_reductions_excluded'] is False
    for relative,h in comparison['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale scalar-C comparison: '+relative
        paths.add(path)
    paths.add(SCALAR_COMPARISON)
    fitted=load(THREE_HIDDEN)
    assert fitted['scope_verdict']=='positive_minimal_endpoint_interpolant_not_threshold_faithful'
    assert fitted['minimal_hidden_dimension_for_exact_two_point_fit']==3 and fitted['weighted_core_inertia']==[6,0,0]
    assert fitted['native_zero_mode_preserved'] is False and fitted['physical_outcomes_admitted'] is False
    for relative,h in fitted['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale three-hidden interpolant: '+relative
        paths.add(path)
    paths.add(THREE_HIDDEN)
    projected=load(GROUND_PROJECTION)
    assert projected['scope_verdict']=='positive_endpoint_and_ground_preserving_native_projection'
    assert projected['hidden_dimension']==5 and projected['weighted_core_inertia']==[7,0,1]
    assert projected['native_ground_in_projection'] is True and projected['conditional_chain_threshold_limit_matches_native'] is True
    assert projected['all_energy_full_response_identical'] is False and projected['physical_outcomes_admitted'] is False
    for relative,h in projected['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale native ground-preserving projection: '+relative
        paths.add(path)
    paths.add(GROUND_PROJECTION)
    timed=load(PROJECTION_TIME_ERROR)
    assert timed['scope_verdict']=='finite_time_preparation_sensitive_error_certificate'
    assert timed['certified_residual_norm_upper_bound']==3 and timed['state_error_bound']=='alpha min(2,3|t|)'
    assert timed['asymptotic_scattering_bound_claimed'] is False and timed['physical_outcomes_admitted'] is False
    for relative,h in timed['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale native projection time-error bound: '+relative
        paths.add(path)
    paths.add(PROJECTION_TIME_ERROR)
    on_shell=load(PROJECTION_ON_SHELL)
    assert on_shell['scope_verdict']=='conditional_low_window_on_shell_and_outgoing_packet_error'
    assert on_shell['energy_window_upper']=='1/64' and on_shell['on_shell_norm_error_bound']=='(2/3)sqrt(E)'
    assert on_shell['symmetric_scattering_exact_on_open_band'] is True
    assert on_shell['full_band_small_error_claimed'] is False and on_shell['physical_outcomes_admitted'] is False
    for relative,h in on_shell['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale native projection on-shell bound: '+relative
        paths.add(path)
    paths.add(PROJECTION_ON_SHELL)
    full_band=load(PROJECTION_FULL_BAND)
    assert full_band['scope_verdict']=='maximal_full_band_discrepancy_for_fixed_native_projection'
    assert full_band['maximal_common_frame_full_band_scattering_norm_error']==2
    assert full_band['root_bracket']==['39/100','2/5'] and full_band['preceding_low_window_bound_still_valid'] is True
    assert full_band['all_reductions_excluded'] is False and full_band['physical_outcomes_admitted'] is False
    for relative,h in full_band['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale native projection full-band obstruction: '+relative
        paths.add(path)
    paths.add(PROJECTION_FULL_BAND)
    enriched=load(RESONANT_ENRICHMENT)
    assert enriched['scope_verdict']=='nine_state_endpoint_ground_and_full_band_controlled_native_projection'
    assert enriched['full_core_dimension']==9 and enriched['full_band_scattering_norm_error_upper_bound']=='1/4'
    assert enriched['ground_direction_and_norm_preserved'] is True and enriched['bernstein_degree']==18
    assert enriched['global_minimum_among_arbitrary_fitted_models_claimed'] is False
    assert enriched['native_bound_counts_inherited'] is False and enriched['physical_outcomes_admitted'] is False
    for relative,h in enriched['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale resonant native enrichment: '+relative
        paths.add(path)
    paths.add(RESONANT_ENRICHMENT)
    bound=load(ENRICHED_BOUND)
    assert bound['scope_verdict']=='enriched_conditional_point_sector_differs_from_native'
    assert bound['native']['point_dimension']==5 and bound['enriched']['point_dimension']==3
    assert bound['ambient_lifted_bound_projection_norm_gap']==1
    assert bound['symmetric_preparation_bound_weights_exactly_preserved'] is True
    assert bound['named_antisymmetric_retained_weights_evaluated'] is False and bound['physical_outcomes_admitted'] is False
    for relative,h in bound['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale enriched bound-sector certificate: '+relative
        paths.add(path)
    paths.add(ENRICHED_BOUND)
    carrier=load(CARRIER_WEIGHTS)
    assert carrier['scope_verdict']=='full_tail_named_carrier_retained_weight_comparison'
    assert carrier['native']['mode_count']==3 and carrier['enriched']['mode_count']==1
    assert carrier['all_antisymmetric_point_modes_accounted'] is True
    assert carrier['physical_capture_or_branching_ratio_claimed'] is False and carrier['physical_outcomes_admitted'] is False
    for relative,h in carrier['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale carrier retained-weight certificate: '+relative
        paths.add(path)
    paths.add(CARRIER_WEIGHTS)
    named=load(NAMED_WEIGHTS)
    assert named['scope_verdict']=='absolute_named_central_full_tail_point_weights'
    assert named['all_named_point_contributions_accounted'] is True and named['absolute_named_weights_evaluated'] is True
    assert named['symmetric_point_dimension']==2 and named['symmetric_contact_rank']==2
    assert named['full_visible_retained_quadratic_form_certified'] is False
    assert named['physical_capture_or_branching_ratio_claimed'] is False and named['physical_outcomes_admitted'] is False
    for relative,h in named['source_sha256'].items():
        path=ROOT/relative;assert sha(path.read_bytes())==h,'stale named preparation-weight certificate: '+relative
        paths.add(path)
    paths.add(NAMED_WEIGHTS)
    for p in paths:assert p.is_file(),str(p)
    return {'schema':'marici.scattering.low-energy-branch-evidence.v1',
            'status':'pass_with_source_drift' if drifts else 'pass',
            'native_lineage_source_bindings_fresh':not drifts,'upstream_source_drift':drifts,
            'adapter_current_source_reproduction':{'receipt':ADAPTER_REPLAY.relative_to(ROOT).as_posix(),
                'all_source_hashes_verified':True,'matching_mathematical_payload':True,'checks':24,
                'executed_in_this_checker':False,'historical_mismatch_remains':True},
            'boundary':boundary,'pentachoron_archive':archive_audit,
            'pentachoron_exact_ground_sector':{'receipt':PENTA_GROUND.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'ground_dimension':4,'contact_dark_dimension':2,
                'dark_transmission_is_identity':True,'bright_threshold_regularity_proved':False,
                'executed_in_this_checker':False},
            'pentachoron_bright_threshold_review':{'receipt':PENTA_REVIEW.relative_to(ROOT).as_posix(),
                'scope_verdict':'established','source_hashes_verified':True,'executed_in_this_checker':False,
                'protocol_remaining_units':0,'physical_outcomes_admitted':False},
            'scalar_C_native_comparison':{'receipt':SCALAR_COMPARISON.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'endpoint_error_floor':comparison['endpoint_error_floor'],
                'candidate_hidden_dimension_maximum':2,'all_reductions_excluded':False},
            'three_hidden_interpolant':{'receipt':THREE_HIDDEN.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'minimal_hidden_dimension_for_exact_two_point_fit':3,'native_zero_mode_preserved':False},
            'ground_preserving_native_projection':{'receipt':GROUND_PROJECTION.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'core_dimension':8,'native_ground_preserved':True,'threshold_limit_matches':True,
                'exact_symmetric_core_dimension':5,'global_intertwining_claimed':False},
            'native_projection_time_error':{'receipt':PROJECTION_TIME_ERROR.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'residual_norm_upper_bound':3,'state_error_bound':'alpha min(2,3|t|)',
                'asymptotic_scattering_bound_claimed':False},
            'native_projection_on_shell_error':{'receipt':PROJECTION_ON_SHELL.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'energy_window_upper':'1/64','on_shell_norm_error_bound':'(2/3)sqrt(E)',
                'endpoint_outgoing_packet_error_per_alpha_in':'1/12','full_band_small_error_claimed':False},
            'native_projection_full_band_obstruction':{'receipt':PROJECTION_FULL_BAND.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'maximal_scattering_norm_error':2,'phase_opposition_bracket':['39/100','2/5'],
                'preceding_low_window_bound_still_valid':True,'all_reductions_excluded':False},
            'resonant_native_enrichment':{'receipt':RESONANT_ENRICHMENT.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'core_dimension':9,'full_band_scattering_norm_error_upper_bound':'1/4',
                'minimum_dimension_in_native_endpoint_projection_class_for_submaximal_error':9,
                'native_bound_counts_inherited':False},
            'enriched_bound_sector':{'receipt':ENRICHED_BOUND.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'native_point_dimension':5,'enriched_point_dimension':3,
                'ambient_lifted_bound_projection_norm_gap':1,
                'named_antisymmetric_retained_weights_evaluated':False},
            'carrier_retained_weights':{'receipt':CARRIER_WEIGHTS.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'native_antisymmetric_weight_enclosure':carrier['native']['total_rational_enclosure'],
                'enriched_antisymmetric_weight_enclosure':carrier['enriched']['total_rational_enclosure'],
                'single_carrier_difference_enclosure':carrier['single_carrier_native_minus_enriched_enclosure'],
                'absolute_single_carrier_weights_evaluated':False,'physical_capture_or_branching_ratio_claimed':False},
            'named_preparation_retained_weights':{'receipt':NAMED_WEIGHTS.relative_to(ROOT).as_posix(),
                'source_hashes_verified':True,'executed_in_this_checker':False,
                'absolute_named_weight_enclosures':named['absolute_named_weight_enclosures'],
                'exact_symmetric_equality':True,'absolute_named_weights_evaluated':True,
                'full_visible_retained_quadratic_form_certified':False,'physical_capture_or_branching_ratio_claimed':False},
            'shape_finite_audit':shape_audit,
            'native_successor_lineage':lineage,
            'native_successor_current_propositions':['C2','C5','C9','C11'],
            'hostile_scope_promotions_refused':refused,
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p.read_bytes()) for p in sorted(paths)}}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true')
    p.add_argument('--require-fresh-lineage',action='store_true',help='refuse stale upstream source bindings, not just stale audit accounting')
    args=p.parse_args();report=build()
    if args.require_fresh_lineage and not report['native_lineage_source_bindings_fresh']:
        raise SystemExit('Refused fresh-lineage claim: '+json.dumps(report['upstream_source_drift']))
    if args.check:assert load(RESULT)==report,'stale branch-evidence receipt'
    else:RESULT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'shape_checks_replayed':report['shape_finite_audit']['finite_checks_freshly_replayed'],
                      'pentachoron_checks_inspected_not_replayed':report['pentachoron_archive']['reported_checks'],
                      'native_successor_receipts_inspected':len(report['native_successor_lineage']),
                      'upstream_source_drift':report['upstream_source_drift'],
                      'new_proposition_outcomes_admitted':False}))


if __name__=='__main__':main()
