"""Native chart interpretation with independent source/target policies and Number rival."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[3];BASE='research/voevodsky/'
def main():
    js=subprocess.run(['node',BASE+'checkers/check_ramsey_chart_interpretation.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=120)
    if js.returncode:raise RuntimeError(js.stdout+'\n'+js.stderr)
    raw=json.loads((ROOT/(BASE+'results/ramsey-chart-interpretation-input-v1.json')).read_text(encoding='utf-8'))
    assert (raw['inputCases'],raw['referenceComparisons'],raw['programCases'],len(raw['controls']))==(613,3065,30,4)
    assert raw['binding']['wholeOriginalRetained'] and raw['canonical']['PN']['operation']['kind']=='PN'
    n=raw['numberPort'];u=2**53
    assert n['referenceMismatch'] and n['shift']==list(map(str,[-u,u,0,0]))
    assert n['expectedM0']==list(map(str,[-u,u+1,0,0])) and n['actualM0']!=n['expectedM0']
    assert list(map(int,raw['chartLargePoint']))==[u,u,0]
    assert raw['targetSeedsOnlyCanonicalContextAndInputColors'] and not raw['exactContextAtomsAssumedAsTargetSeeds']
    assert raw['infiniteIndexDomainExplicit'] and not raw['finiteFullShiftUnfoldingClaimed'] and not raw['physicalTrajectoryClaimed'] and not raw['wholeCacheEquivalenceClaimed']
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_chart_interpretation_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:raise RuntimeError('chart interpretation proof closure failed\n'+ps.stdout[-7500:]+'\n'+ps.stderr[-1500:])
    f=json.loads((ROOT/(BASE+'results/agda-RamseyChartInterpretation.json')).read_text(encoding='utf-8-sig'))
    assert f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check']
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-exact-source-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for p in ['contracts/ramsey-uniform-task-package-attempt.v1.json','contracts/ramsey-chart-interpretation-attempt.v1.json','ramsey-chart-interpretation-v1.md','agda/RamseyChartInterpretation.agda',
              'checkers/check_ramsey_chart_interpretation.mjs','checkers/check_ramsey_chart_interpretation.py','checkers/check_ramsey_chart_interpretation_agda.ps1']:
        pins[BASE+p]=sha256((ROOT/(BASE+p)).read_bytes()).hexdigest()
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-chart-interpretation/')]:
        for p,h in f['source_inventory'][group].items():pins[prefix+p]=h
    for p,h in pins.items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h
    r={'schema':'marici.ramsey-chart-interpretation.verification.v1','status':'passed','scope_id':'exact-input-query-to-canonical-native-WG-charts-v1','outcome':'++',
      'verification_level':'fresh safe Cubical source-factored P/E chart interpretation, value/reference cells and actual uniform query-package correspondence; unbounded Shift index explicit, not full operational or physical equivalence',
      'target_derived_without_exact_context_seed':True,'source_target_policies_separate':True,'PE_operation_interpretation_proved':True,
      'actual_uniform_query_package_correspondence':True,'full_reference_and_color_cells':True,'selector_and_program_structure_retained':True,
      'unbounded_Shift_index_explicit':True,'constant_premise_generator_explicit':True,'absolute_Number_port_refuted':True,
      'finite_full_Shift_unfolding_proved':False,'all_twelve_generators_interpreted':False,'full_uniform_task_package_proved':False,
      'particle_trajectory_proved':False,'whole_cache_equivalence_claimed':False,'physical_policy_admissibility_proved':False,'root_resolved':False,
      'input_chart_cases':613,'reference_comparisons':3065,'program_cases':30,'runtime_controls':4,
      'formal_check':{'receipt':BASE+'results/agda-RamseyChartInterpretation.json','compiler_sha256':f['compiler_sha256'],'module_source_sha256':f['module_source_sha256'],
       'ignore_interfaces':True,'inputs_stable':True,'library_inventory_sha256':sha256(json.dumps(f['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
      'remaining_witness':'Declare which intended operational input interface is required beyond this existing native WG P/E chart fragment, and supply those additional admission/continuation cells without assuming finite Shift unfolding.',
      'witness':raw,'source_sha256':dict(sorted(pins.items()))}
    target=ROOT/(BASE+'results/ramsey-chart-interpretation-v1.json')
    target.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    contract=json.loads((ROOT/(BASE+'contracts/ramsey-uniform-task-package-attempt.v1.json')).read_text(encoding='utf-8'))
    exact=ROOT/(BASE+'results/ramsey-exact-source-v1.json')
    corollary={'schema':'marici.ramsey-uniform-task-package.verification.v1','status':'passed',
      'scope_id':contract['scope_id'],'claim_sha256':sha256(contract['claim'].encode()).hexdigest(),'outcome':'++',
      'verification_level':'written all-index finite-region/source construction plus fresh safe Cubical actual native WG chart policy, uniform query/refusal/substitution and source-target correspondence; explicit higher-index arity, not whole-space or physical forcing',
      'source_policy':'canonical local-context/supplied-color literal inputs indexed by the complete finite Region N, with native E-retained exact shifts',
      'all_pattern_palette_region_word_quantifiers':True,'source_policy_independent_of_answer':True,'no_exact_context_target_seed_assumed':True,
      'native_query_refusal_and_substitution':True,'target_full_reference_and_color_binding':True,'higher_index_arity_explicit':True,
      'kernel_D3_enumerator_completeness_proved':False,'whole_space_admission_proved':False,'finite_Shift_premise_unfolding_proved':False,
      'physical_policy_admissibility_proved':False,'autonomous_native_forcing_proved':False,'root_resolved':False,
      'chart_interpretation':{'receipt':BASE+'results/ramsey-chart-interpretation-v1.json','sha256':sha256(target.read_bytes()).hexdigest()},
      'exact_source':{'receipt':BASE+'results/ramsey-exact-source-v1.json','sha256':sha256(exact.read_bytes()).hexdigest()},
      'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-uniform-task-package-v1.json')).write_text(json.dumps(corollary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('witness','source_sha256')}))
if __name__=='__main__':main()
