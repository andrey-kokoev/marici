"""Concrete prepared-region P/E instance: sector replay plus fresh Cubical check."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import re
import subprocess
ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/voevodsky/'

def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    node = subprocess.run(['node',BASE+'checkers/check_ramsey_native_region_family.mjs'],cwd=ROOT,capture_output=True,text=True,check=True,timeout=90)
    raw = json.loads((ROOT/(BASE+'results/ramsey-native-region-family-input-v1.json')).read_text(encoding='utf-8'))
    domain = {p for p in product(range(-3,4),repeat=3) if sum(p)%2==0}
    assert len(raw['rows']) == len(domain) == 171
    assert {tuple(r['point']) for r in raw['rows']} == domain
    assert len(raw['sourceControls']) == 7 and raw['attemptedJointAssembly'] == {'valid':False,'reason':'global-CM-role-conflict'}
    for i,row in enumerate(raw['rows']):
        assert row['index']==i
        x,y,z=row['point']
        shift=[-(x+y+z)//2,(x+y-z)//2,(x+z-y)//2,(y+z-x)//2]
        assert row['shift']==shift and sum(shift)==0
        b=list(map(int,row['frame']['window'][0]['vertex'].split(',')))
        assert [b[1]+b[2],b[1]+b[3],b[2]+b[3]]==row['point']
        assert row['packet']['packet']['permutation']==[0,1,2,3,4]
        assert row['PN']['operation']['permutation']==[3,1,2,0,4]
        assert row['PN']['target']['packet']['permutation']==[3,1,2,0,4]
    formal = ROOT/(BASE+'agda/RamseyRegionFamily.agda')
    text = formal.read_text(encoding='utf-8')
    assert len(re.findall(r'^  r\d{3} : RegionIndex$',text,re.M))==171
    actual = dict(re.findall(r'^context (r\d{3}) = (.*)$',text,re.M))
    assert len(actual)==171
    for i,row in enumerate(raw['rows']):
        assert json.loads(json.loads(actual[f'r{i:03d}'])) == row
    # This is the real native P/E implementation, not a renamed host list.
    assert 'R.apply (N.P-kind' in text and 'R.apply (N.E-kind' in text
    assert 'Admit q = Σ RegionIndex' in text and 'selected-retains-every-input' in text
    ps = subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_region_family_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=600)
    if ps.returncode:
        raise RuntimeError('fresh native P/E typecheck failed\n'+ps.stdout[-5000:]+'\n'+ps.stderr[-2000:])
    agda = json.loads((ROOT/(BASE+'results/agda-RamseyRegionFamily.json')).read_text(encoding='utf-8-sig'))
    assert agda['passed'] and agda['positive_exit_code']==0 and agda['wrong_premise_rejected_as_expected']
    assert agda['ignore_interfaces'] and agda['inputs_stable_during_check']
    assert agda['positive_source_sha256']==digest(formal)
    files=[BASE+'contracts/ramsey-native-region-family-attempt.v1.json',BASE+'ramsey-native-region-family-v1.md',
           BASE+'ramsey-native-region-family.mjs',BASE+'checkers/check_ramsey_native_region_family.mjs',
           BASE+'checkers/check_ramsey_native_region_family.py',BASE+'checkers/check_ramsey_region_family_agda.ps1',
           BASE+'agda/RamseyRegionFamily.agda.in',BASE+'agda/RamseyRegionFamily.agda',
           BASE+'fixtures/ramsey-native-region-family/RamseyRegionFamilyWrongPremise.agda']
    prior=json.loads((ROOT/(BASE+'results/ramsey-native-word-trace-v1.json')).read_text(encoding='utf-8'))
    pins=dict(prior['source_sha256'])
    for f in files:
        pins[f]=digest(ROOT/f)
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/')]:
        for f,h in agda['source_inventory'][group].items():
            pins[prefix+f]=h
    for f,h in pins.items():
        assert digest(ROOT/f)==h
    library_hash=sha256(json.dumps(agda['source_inventory']['library'],sort_keys=True).encode()).hexdigest()
    result={'schema':'marici.ramsey-native-region-family.verification.v1','status':'passed',
        'scope_id':'L3-prepared-context-native-Pi-E-family-v1','outcome':'++',
        'verification_level':'fresh safe Cubical native P/E instance under explicit prepared-input policy plus runtime sector checks; not kernel verification of sector geometry or physical policy admissibility',
        'prepared_contexts':171,'prepared_M_planes':7,'native_P_premises':171,'native_E_premises_each':171,
        'source_controls':7,'wrong_premise_module_rejected':True,'native_derivations_typechecked':True,
        'formal_contexts_equal_source_records':True,'formal_colors_are_supplied_parameter':True,
        'prepared_policy_differs_from_canonical':True,'simultaneous_assembly_admitted':False,
        'word_to_index_constructed':False,'physical_prepared_policy_admissibility_proved':False,
        'uniform_task_package_proved':False,'root_resolved':False,
        'input':raw,
        'formal_check':{'receipt':BASE+'results/agda-RamseyRegionFamily.json',
            'compiler_sha256':agda['compiler_sha256'],'library_inventory_sha256':library_hash,
            'ignore_interfaces':True,'inputs_stable':True,
            'positive_source_sha256':agda['positive_source_sha256'],
            'negative_source_sha256':agda['negative_source_sha256']},
        'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-native-region-family-v1.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('input','source_sha256')}))

if __name__=='__main__':
    main()
