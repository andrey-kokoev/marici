"""Bounded request-to-native-selection trial with fresh positive/adversarial proofs."""
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

def h(path): return sha256(path.read_bytes()).hexdigest()

def main():
    subprocess.run(['node',BASE+'checkers/check_ramsey_word_family_selection.mjs'],cwd=ROOT,capture_output=True,text=True,check=True,timeout=120)
    raw=json.loads((ROOT/(BASE+'results/ramsey-word-family-selection-input-v1.json')).read_text(encoding='utf-8'))
    program=raw['program']; rows=program['prepared']['rows']
    assert program['pattern']==[[0,0,0],[1,1,0],[1,0,1]] and len(rows)==171
    assert {tuple(c['word']) for c in raw['cases']}==set(product(range(3),repeat=3))
    for case in raw['cases']:
        word=case['word']; response=case['response']
        assert independent_decode(response['request'])==word==response['requestWord']
        expected=[sum(program['pattern'][i][j] for i in word) for j in range(3)]
        index=response['regionIndex']; assert rows[index]==response['context'] and rows[index]['point']==expected
        b=list(map(int,response['context']['frame']['window'][0]['vertex'].split(',')))
        assert [b[1]+b[2],b[1]+b[3],b[2]+b[3]]==expected
        assert response['color']==raw['colors'][index]
    assert (raw['queryCases'],raw['recoloringIndexComparisons'],len(raw['sourceControls']))==(81,54,12)
    assert raw['retainedFieldPremiseSlots']==4617 and raw['tableCompiledWithoutColors']
    assert not raw['freeTargetIndexInput'] and not raw['newSeedPolicyIntroduced'] and not raw['autonomousNativeControllerProved'] and not raw['rootResolved']
    text=(ROOT/(BASE+'agda/RamseyWordFamilySelection.agda')).read_text(encoding='utf-8')
    mapping=re.findall(r'^compile-index \(word l([012]) l([012]) l([012])\) = r(\d{3})$',text,re.M)
    assert len(mapping)==27
    for a,b,c,i in mapping:
        w=list(map(int,[a,b,c])); assert next(e['regionIndex'] for e in program['entries'] if e['word']==w)==int(i)
    for i,row in enumerate(rows):
        x,y,z=[v+3 for v in row['point']]
        assert f'region-point r{i:03d} = ({x} , ({y} , {z}))' in text
    traces=re.findall(r'^canonical-trace \(word l([012]) l([012]) l([012])\) = (.*)$',text,re.M)
    assert len(traces)==27
    for a,b,c,s in traces:
        word=list(map(int,[a,b,c])); expected=next(x['response']['request'] for x in raw['cases'] if x['word']==word)
        assert json.loads(json.loads(s))==expected
    assert 'R.seed' not in text and 'Admit' not in text and 'B.family' in text and 'word-premise' in text
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_word_family_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:
        raise RuntimeError('word-family native proof check failed\n'+ps.stdout[-6000:]+'\n'+ps.stderr[-2000:])
    formal=json.loads((ROOT/(BASE+'results/agda-RamseyWordFamilySelection.json')).read_text(encoding='utf-8-sig'))
    assert formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check']
    codes=formal['module_exit_codes']
    assert codes['RamseyWordFamilySelection']==codes['RamseyWordFamilyWrongIndexNative']==0
    assert codes['RamseyWordFamilyWrongIndex']!=0 and codes['RamseyWordFamilyWrongPremise']!=0
    sources=dict(json.loads((ROOT/(BASE+'results/ramsey-native-region-family-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    files=['contracts/ramsey-word-family-selection-attempt.v1.json','ramsey-word-family-selection-v1.md',
      'ramsey-word-family-selection.mjs','checkers/check_ramsey_word_family_selection.mjs',
      'checkers/check_ramsey_word_family_selection.py','checkers/check_ramsey_word_family_agda.ps1',
      'agda/RamseyWordFamilySelection.agda.in','agda/RamseyWordFamilySelection.agda']
    for f in files: sources[BASE+f]=h(ROOT/(BASE+f))
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-word-family-selection/')]:
        for f,d in formal['source_inventory'][group].items(): sources[prefix+f]=d
    for f,d in sources.items(): assert h(ROOT/f)==d
    result={'schema':'marici.ramsey-word-family-selection.verification.v1','status':'passed',
      'scope_id':'L3-native-word-request-to-E-selection-v1','outcome':'++',
      'verification_level':'fresh safe Cubical native word-indexed P/E program and declared-point square, with runtime sector/trace binding; host compiler and decoder retained, not autonomous control or physical policy admission',
      'word_cases':27,'query_cases':81,'recoloring_index_comparisons':54,'runtime_controls':12,
      'word_premises':27,'region_premises_each':171,'retained_field_premise_slots':4617,
      'native_program_typechecked':True,'wrong_index_native_program_typechecks':True,
      'wrong_index_task_square_rejected':True,'wrong_word_premise_rejected':True,
      'request_and_canonical_trace_observation_preserved':True,'free_target_index_input':False,
      'new_seed_policy_introduced':False,'host_table_compiler_retained':True,'host_sector_trace_decoder_retained':True,
      'sector_geometry_kernel_proved':False,'autonomous_native_controller_proved':False,
      'physical_policy_admissibility_proved':False,'uniform_task_package_proved':False,'root_resolved':False,
      'witness':raw,
      'formal_check':{'receipt':BASE+'results/agda-RamseyWordFamilySelection.json',
       'compiler_sha256':formal['compiler_sha256'],'module_source_sha256':formal['module_source_sha256'],
       'library_inventory_sha256':sha256(json.dumps(formal['source_inventory']['library'],sort_keys=True).encode()).hexdigest(),
       'ignore_interfaces':True,'inputs_stable':True},
      'source_sha256':dict(sorted(sources.items()))}
    (ROOT/(BASE+'results/ramsey-word-family-selection-v1.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('witness','source_sha256')}))

if __name__=='__main__': main()
