"""Uniform symbolic relative theorem; deliberately does not close source admission."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[3]
BASE='research/voevodsky/'
def main():
    js=subprocess.run(['node',BASE+'checkers/check_ramsey_uniform_relative.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=120)
    if js.returncode: raise RuntimeError(js.stdout+'\n'+js.stderr)
    raw=json.loads((ROOT/(BASE+'results/ramsey-uniform-relative-input-v1.json')).read_text(encoding='utf-8'))
    assert raw['queryCases']==423 and raw['hits']+raw['misses']==423 and raw['hits']>0 and raw['misses']>0
    assert raw['substitutionCases']==1023 and len(raw['controls'])==4
    for s in raw['samples']:
        p=[sum(int(s['letters'][i][j]) for i in s['word']) for j in range(3)]
        assert p==list(map(int,s['point']))
        assert (s['kind']=='selected') == (max(map(abs,p))<=3 and sum(p)%2==0)
    assert raw['misboundNativeRelativeInterfaceAccepts'] and raw['misboundSectorBindingRejected']
    assert not raw['allRegionContextConstructionProved'] and not raw['fullUniformTaskPackageProved']
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_uniform_relative_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:raise RuntimeError('relative proof closure failed\n'+ps.stdout[-6500:]+'\n'+ps.stderr[-1600:])
    formal=json.loads((ROOT/(BASE+'results/agda-RamseyUniformRelative.json')).read_text(encoding='utf-8-sig'))
    assert formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check']
    codes=formal['module_exit_codes'];assert all(codes[n]==0 for n in ['RamseyUniformRelative','RamseyUniformSigned','RamseyUniformMisbound'])
    assert all(codes[n]!=0 for n in ['RamseyUniformBadBinding','RamseyUniformBadLookup','RamseyUniformBadRefusal','RamseyUniformBadSubstitution'])
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-family-refinement-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for f in ['contracts/ramsey-uniform-relative-attempt.v1.json','ramsey-uniform-relative-v1.md','ramsey-uniform-relative.mjs',
              'checkers/check_ramsey_uniform_relative.mjs','checkers/check_ramsey_uniform_relative.py','checkers/check_ramsey_uniform_relative_agda.ps1',
              'agda/RamseyUniformRelative.agda','agda/RamseyUniformSigned.agda']:
        pins[BASE+f]=sha256((ROOT/(BASE+f)).read_bytes()).hexdigest()
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-uniform-relative/')]:
        for f,h in formal['source_inventory'][group].items():pins[prefix+f]=h
    for f,h in pins.items():assert sha256((ROOT/f).read_bytes()).hexdigest()==h
    result={'schema':'marici.ramsey-uniform-relative.verification.v1','status':'passed',
      'scope_id':'all-finite-relative-native-query-refusal-substitution-v1','outcome':'++',
      'verification_level':'fresh safe Cubical all-finite relative native query/refusal/history constructor and signed-integer substitution laws; opaque-context/source-region binding remains unproved',
      'symbolic_all_finite_parameters_proved':True,'computed_lookup_and_refusal_proved':True,'native_family_program_request_retained':True,
      'same_source_variable_substitution_proved':True,'signed_integer_geometry_laws_proved':True,
      'misbound_native_relative_program_typechecks':True,'misbound_sector_binding_rejected':True,
      'full_uniform_task_package_proved':False,'uniform_complete_sector_family_proved':False,'physical_policy_admissibility_proved':False,'root_resolved':False,
      'runtime_query_cases':423,'runtime_hits':raw['hits'],'runtime_refusals':raw['misses'],'runtime_substitution_cases':1023,'runtime_controls':4,
      'formal_check':{'receipt':BASE+'results/agda-RamseyUniformRelative.json','compiler_sha256':formal['compiler_sha256'],
        'module_source_sha256':formal['module_source_sha256'],'ignore_interfaces':True,'inputs_stable':True,
        'library_inventory_sha256':sha256(json.dumps(formal['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
      'remaining_witness':'A uniformly constructed complete L_N family with actual point/context coupling and source-valid references, not merely independently supplied declared points and opaque context strings.',
      'witness':raw,'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-uniform-relative-v1.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('witness','source_sha256')}))
if __name__=='__main__':main()
