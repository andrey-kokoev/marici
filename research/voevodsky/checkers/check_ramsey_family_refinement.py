"""Source extension, actual native policy map, then overlap query checks."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import re
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from research.voevodsky.checkers.check_ramsey_native_word_trace import independent_decode
BASE='research/voevodsky/'
def digest(p): return sha256(p.read_bytes()).hexdigest()

def main():
    subprocess.run(['node',BASE+'checkers/check_ramsey_family_refinement.mjs'],cwd=ROOT,capture_output=True,text=True,check=True,timeout=180)
    raw=json.loads((ROOT/(BASE+'results/ramsey-family-refinement-input-v1.json')).read_text(encoding='utf-8'))
    data=raw['data'];old=data['oldRows'];new=data['newRows']
    for n,rows in [(3,old),(4,new)]:
        expected={p for p in product(range(-n,n+1),repeat=3) if sum(p)%2==0}
        assert len(rows)==len(expected) and {tuple(r['point']) for r in rows}==expected
        for i,row in enumerate(rows):
            assert row['index']==i
            x,y,z=row['point'];assert row['shift']==[-(x+y+z)//2,(x+y-z)//2,(x+z-y)//2,(y+z-x)//2]
            b=list(map(int,row['frame']['window'][0]['vertex'].split(',')))
            assert [b[1]+b[2],b[1]+b[3],b[2]+b[3]]==row['point']
            assert row['packet']['packet']['permutation']==[0,1,2,3,4]
            assert row['PN']['target']['packet']['permutation']==[3,1,2,0,4]
    assert len(old)==171 and len(new)==365 and new[:171]==old and data['embedding']==list(range(171))
    assert data['oldLiveContextsUnchanged'] and not data['joint3']['valid'] and not data['joint4']['valid']
    assert raw['comparisons']==raw['freshReadoutComparisons']==81 and raw['freshLiteralMismatches']==171
    assert len(raw['sourceControls'])==6
    assert {tuple(c['word']) for c in raw['cases']}==set(product(range(3),repeat=3))
    for c in raw['cases']:
        assert independent_decode(c['request'])==c['word']
        p=[sum([[0,0,0],[1,1,0],[1,0,1]][i][j] for i in c['word']) for j in range(3)]
        assert c['point']==p and new[c['newIndex']]==old[c['oldIndex']]
        assert new[c['newIndex']]['point']==p
    text=(ROOT/(BASE+'agda/RamseyFamilyRefinement.agda')).read_text(encoding='utf-8')
    assert len(re.findall(r'^  n\d{3} : NewIndex$',text,re.M))==365
    contexts=dict(re.findall(r'^new-context (n\d{3}) = (.*)$',text,re.M))
    assert len(contexts)==365
    for i,row in enumerate(new): assert json.loads(json.loads(contexts[f'n{i:03d}']))==row
    assert 'seed-inclusion' in text and 'map-derivation' in text and 'history-preserved' in text and 'transported-history-retained' in text
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_family_refinement_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode: raise RuntimeError('native refinement proof failed\n'+ps.stdout[-6500:]+'\n'+ps.stderr[-2000:])
    formal=json.loads((ROOT/(BASE+'results/agda-RamseyFamilyRefinement.json')).read_text(encoding='utf-8-sig'))
    assert formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check']
    codes=formal['module_exit_codes'];assert codes['RamseyFamilyRefinement']==codes['RamseyFamilyFreshNativeOnly']==0
    assert all(codes[n]!=0 for n in ['RamseyFamilyFreshRebuild','RamseyFamilyWrongSeed','RamseyFamilyWrongQuery'])
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-word-family-selection-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for f in ['contracts/ramsey-family-refinement-attempt.v1.json','ramsey-family-refinement-v1.md','ramsey-family-refinement.mjs',
              'checkers/check_ramsey_family_refinement.mjs','checkers/check_ramsey_family_refinement.py',
              'checkers/check_ramsey_family_refinement_agda.ps1','agda/RamseyFamilyRefinement.agda.in','agda/RamseyFamilyRefinement.agda']:
        pins[BASE+f]=digest(ROOT/(BASE+f))
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-family-refinement/')]:
        for f,h in formal['source_inventory'][group].items():pins[prefix+f]=h
    for f,h in pins.items():assert digest(ROOT/f)==h
    result={'schema':'marici.ramsey-family-refinement.verification.v1','status':'passed',
        'scope_id':'prepared-L3-L4-native-refinement-query-compatibility-v1','outcome':'++',
        'verification_level':'fresh safe Cubical concrete seed inclusion, native derivation/history transport and overlap squares; runtime sector binding under prepared-input policies, not physical or all-region completion',
        'old_contexts':171,'new_contexts':365,'added_contexts':194,'common_words':27,'overlap_checks':81,
        'source_controls':6,'fresh_rebuild_literal_mismatches':171,'fresh_rebuild_readout_checks':81,
        'typed_seed_inclusion':True,'native_derivation_map':True,'constructor_history_preserved':True,
        'both_route_histories_retained':True,'fresh_rebuild_native_only_typechecks':True,
        'fresh_rebuild_identity_transport_rejected':True,'wrong_seed_rejected':True,'wrong_direct_query_rejected':True,
        'whole_family_equivalence_claimed':False,'cofinal_all_region_theorem_proved':False,
        'physical_policy_admissibility_proved':False,'uniform_task_package_proved':False,'root_resolved':False,
        'witness':raw,
        'formal_check':{'receipt':BASE+'results/agda-RamseyFamilyRefinement.json','compiler_sha256':formal['compiler_sha256'],
          'module_source_sha256':formal['module_source_sha256'],'ignore_interfaces':True,'inputs_stable':True,
          'library_inventory_sha256':sha256(json.dumps(formal['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
        'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-family-refinement-v1.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('witness','source_sha256')}))

if __name__=='__main__':main()
