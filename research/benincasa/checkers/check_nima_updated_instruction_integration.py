#!/usr/bin/env python3
"""Nima instruction integration: fresh local replay, typed reopening, owner-write guard."""
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
NET='research/conjecture_net/contracts/weighted-a3-descent-work-net.v1.json'
REOPEN='research/benincasa/contracts/first-simple-root-boundary-reopening.v1.json'
MESSAGE='naradaepistemiccommunication:eeba28638ffe317898f4'


def digest(p):return sha256((ROOT/p).read_bytes()).hexdigest()


def main():
    net=json.loads((ROOT/NET).read_text());pin=net['source_pins']
    protected=[NET,pin,'research/nima/scc-models/weighted-a3-descent-net-v1.json']
    before={p:digest(p) for p in protected}
    nodes={n['id']:n for n in net['conjectures']}
    assert nodes['incidence-is-a3-compatibility']['verdict']=='rejected'
    assert nodes['untransported-simple-forms']['verdict']==nodes['composite-normalization-definition']['verdict']=='open'
    assert nodes['common-oriented-simple-charts']['verdict']==nodes['negative-simple-difference-forms']['verdict']=='open'
    replay=[];paths=[NET,pin,REOPEN,'research/nima/n8-invariant-boundary-programme-completion.md',
        'research/benincasa/first-simple-root-boundary-localization-2026-10-13.md']
    jobs=[('check_history6_current_closure.py','history6_current_closure.json'),
          ('check_three_composite_normalizations.py','three_composite_normalizations.json'),
          ('check_three_composite_boundary_residues.py','three_composite_boundary_residues.json'),
          ('check_first_simple_root_boundary_localization.py','first_simple_root_boundary_localization.json')]
    for filename,resultname in jobs:
        checker='research/benincasa/checkers/'+filename;receipt='research/benincasa/results/'+resultname
        run=subprocess.run([sys.executable,str(ROOT/checker)],cwd=ROOT,capture_output=True,text=True,timeout=1800)
        if run.returncode:raise RuntimeError(f'{checker}\n{run.stdout[-3000:]}\n{run.stderr[-3000:]}')
        evidence=json.loads((ROOT/receipt).read_text());assert evidence['passed']
        assert evidence['checker_sha256']==digest(checker)
        for p,h in evidence['source_sha256'].items():assert digest(p)==h,p
        replay.append({'command':'python '+checker,'receipt':receipt,'receipt_sha256':digest(receipt),
            'checker_sha256':digest(checker),'fresh_returncode':0})
        paths.extend([checker,receipt])
    closure=json.loads((ROOT/'research/benincasa/results/history6_current_closure.json').read_text())
    assert closure['fresh_suite_count']==10 and not closure['physical_admitted']
    simple=json.loads((ROOT/'research/benincasa/results/first_simple_root_boundary_localization.json').read_text())
    assert simple['boundary']['physical_target_divisor']=='not identified'
    reopening=json.loads((ROOT/REOPEN).read_text())
    assert reopening['source']['support']==simple['source_chart']['support']
    assert reopening['source']['source_residue_sign']==simple['boundary']['residue_orientation']
    target_missing=[key for key,value in reopening['missing_target_witness'].items() if value is None]
    assert len(target_missing)==7
    port=next(p for p in net['witness_ports'] if p['id']=='oriented-source-atlas-materialized')
    assert port['required_files']==reopening['source_bundle_attachment']['required_files']
    bundle=[{'path':p,'exists':(ROOT/p).is_file()} for p in port['required_files']]
    # Executable reopening predicate checks REAL supplied data, never a
    # hypothetical successful witness constructed from a scalar.
    def reopening_preflight(packet):
        errors=[]
        missing=[key for key in target_missing if packet.get(key) is None]
        if missing:errors.append('typed_target_witness_incomplete')
        if packet.get('bottom_definition')=='K times source boundary':errors.append('bottom_map_manufactured_from_scalar')
        if packet.get('top_residue_domain')=='existing E_top superfunction as seven-form':errors.append('top_superfunction_form_type_mismatch')
        if packet.get('target_normal_only')=='Delta23 source label':errors.append('source_label_is_not_target_incidence_witness')
        if packet.get('bundle_admission_basis')=='file existence only':errors.append('bundle_not_source_reviewed')
        if packet.get('orientation_control')=='omitted':errors.append('orientation_hostile_missing')
        if any(not item['exists'] for item in bundle):errors.append('owning_source_bundle_missing')
        if reopening['source_bundle_attachment']['owning_source_review'] is None:errors.append('owning_review_absent')
        return {'reopenable':False,'defects':errors,'missing_target_fields':missing}
    current=reopening_preflight({});assert not current['reopenable']
    controls=[]
    for name,packet,defect in [
        ('K_boundary_selector',{'bottom_definition':'K times source boundary'},'bottom_map_manufactured_from_scalar'),
        ('E_top_is_seven_form',{'top_residue_domain':'existing E_top superfunction as seven-form'},'top_superfunction_form_type_mismatch'),
        ('source_minor_is_physical_normal',{'target_normal_only':'Delta23 source label'},'source_label_is_not_target_incidence_witness'),
        ('file_presence_admits_bundle',{'bundle_admission_basis':'file existence only'},'bundle_not_source_reviewed'),
        ('orientation_not_tested',{'orientation_control':'omitted'},'orientation_hostile_missing')]:
        result=reopening_preflight(packet);assert defect in result['defects'] and not result['reopenable']
        controls.append({'id':name,'result':result})
    source_residuals=[{'shift':r['shift'],'c':r['external_coefficient'],
        'orientation_reversal_defect':r['orientation_flip_residual_K0'],
        'unit_substitution_defect':r['unit_normalization_substitution_defect']} for r in simple['runs']]
    assert all(s['orientation_reversal_defect']!='0' and s['unit_substitution_defect']!='0' for s in source_residuals)
    after={p:digest(p) for p in protected};assert before==after
    out={'schema':'marici.benincasa.nima-updated-instruction-integration.v1','request_message':MESSAGE,
        'owning_snapshot':{'source_pins':pin,'frontier':net['frontier'],'recommended_start':net['recommended_start']},
        'fresh_commands':replay,'nested_history6_fresh_checks':10,
        'composite_scope':'Three intrinsic normalized composite candidates and their local differential residue squares freshly replayed; no physical/global boundary-supercomponent or chain attachment inferred.',
        'conditional_history6':{'local_closure':True,'physical_admitted':False,
            'missing_physical_inputs':closure['missing_physical_selection_inputs'],
            'retained_residuals':'Positive endpoint split periods(-1,+1); two radius hierarchies give source periods(1,0)/(0,1); two projective cycle directions remain split-invisible; ordinary blowdown unavailable_not_zero.'},
        'first_simple_root_reopening':{'contract':REOPEN,'actual_source_boundary':simple['boundary'],
            'target_missing':target_missing,'source_bundle_files':bundle,'current_preflight':current,
            'negative_controls':controls,'retained_exact_residuals':source_residuals},
        'preserved_rejections':{'incidence-is-a3-compatibility':'rejected, unchanged','orientation_reversal':'fresh nonzero source defects retained'},
        'proposed_scoped_owner_review':[
            'Attach the integration report and reopening contract as precursor evidence, if reviewed; do not resolve either scientific frontier.',
            'Record history6 local covariance/cycle/typed-boundary mathematics as constructed only on declared localizations; physical selection and global attachment stay open.',
            'Reopen simple oriented-chart/difference comparisons only after the typed target boundary interface and source bundle are supplied and reviewed; then run the coefficientwise square before nine-to-divisor comparison.'],
        'owner_write_guard':{'protected_sha256_before':before,'protected_sha256_after':after,'unchanged':True},
        'measurement_work_reopened':False,'scientific_transition_applied':False,
        'passed':True,'source_sha256':{p:digest(p) for p in paths},'checker_sha256':digest(str(Path(__file__).relative_to(ROOT)).replace('\\','/'))}
    target=ROOT/'research/benincasa/results/nima_updated_instruction_integration.json'
    target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'fresh_commands':len(replay),'nested_local_checks':10,
        'missing_simple_target_fields':len(target_missing),'missing_bundle_files':sum(not item['exists'] for item in bundle),
        'physical_admitted':False,'owner_contract_and_pins_unchanged':True,'measurement_work_reopened':False},indent=2))

if __name__=='__main__':main()
