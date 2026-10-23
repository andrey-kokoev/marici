"""All-index written exact-source construction with independent controls and native proof."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[3];BASE='research/voevodsky/'
def main():
    js=subprocess.run(['node',BASE+'checkers/check_ramsey_exact_source.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=180)
    if js.returncode:raise RuntimeError(js.stdout+'\n'+js.stderr)
    raw=json.loads((ROOT/(BASE+'results/ramsey-exact-source-input-v1.json')).read_text(encoding='utf-8'))
    root={'C0':(1,0,0,0),'M0':(0,1,0,0),'C1':(0,0,1,0),'M1':(0,0,0,1),'C2':(-1,1,0,1)}
    def verify(c):
        x,y,z=map(int,c['point']);assert (x+y+z)%2==0
        d=tuple(map(int,c['shift']));assert sum(d)==0
        assert d==(-(x+y+z)//2,(x+y-z)//2,(x+z-y)//2,(y+z-x)//2)
        refs={n:tuple(map(int,v.split(','))) for n,v in c['references'].items()}
        assert refs=={n:tuple(d[j]+v[j] for j in range(4)) for n,v in root.items()}
        b=refs['C0'];assert (b[1]+b[2],b[1]+b[3],b[2]+b[3])==(x,y,z)
        assert len(set(refs.values()))==5
        p=set(c['source']['body']);q=set(c['target']['body']);assert p&q==set(c['transfer']['face']) and len(p&q)==3
        assert c['source']['permutation']==list(range(5)) and c['target']['permutation']==c['transfer']['permutation']==[3,1,2,0,4]
        assert c['source']['origin']==c['target']['origin']==c['transfer']['phaseDelta']=='0'
    for g in raw['regions']:
        n=int(g['radius']);expected={p for p in product(range(-n,n+1),repeat=3) if sum(p)%2==0}
        assert {tuple(map(int,c['point'])) for c in g['rows']}==expected
        assert len(g['rows'])==len(expected)==((2*n+1)**3+(-1)**n)//2
        assert len({c['namespace'] for c in g['rows']})==len(expected)
        for c in g['rows']:verify(c)
    for c in raw['large']:verify(c)
    assert (raw['inclusions'],raw['legacyBindings'],raw['queries'],len(raw['controls']))==(613,365,320,8)
    assert raw['selected']+raw['refused']==320 and raw['selected']>0 and raw['refused']>0
    for w in raw['witnesses']:
        assert w['wholeOriginalRetained'] and len(w['renaming']['cells'])==2 and len(w['renaming']['packets'])==2
        assert w['original']['point']==list(map(int,w['exact']['point']))
    assert raw['exactSourceInterpretationOnly'] and not raw['legacyWholeCacheEquivalenceClaimed'] and not raw['unboundedNumberAPIClaimed'] and not raw['physicalAdmissionProved']
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_exact_source_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:raise RuntimeError('exact source proof closure failed\n'+ps.stdout[-7000:]+'\n'+ps.stderr[-1800:])
    f=json.loads((ROOT/(BASE+'results/agda-RamseyExactSource.json')).read_text(encoding='utf-8-sig'))
    assert f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check']
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-uniform-relative-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for p in ['contracts/ramsey-exact-source-attempt.v1.json','ramsey-exact-source-v1.md','ramsey-exact-source.mjs','agda/RamseyExactSource.agda',
              'checkers/check_ramsey_exact_source.mjs','checkers/check_ramsey_exact_source.py','checkers/check_ramsey_exact_source_agda.ps1']:
        pins[BASE+p]=sha256((ROOT/(BASE+p)).read_bytes()).hexdigest()
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-exact-source/')]:
        for p,h in f['source_inventory'][group].items():pins[prefix+p]=h
    for p,h in pins.items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h
    r={'schema':'marici.ramsey-exact-source.verification.v1','status':'passed','scope_id':'uniform-exact-translated-context-source-realizer-v1','outcome':'++',
      'verification_level':'written all-index exact local-PN source/region construction and fresh safe Cubical derived-context native query/substitution; bounded legacy renaming, not full operational embedding or unbounded Number API',
      'uniform_exact_region_and_context_construction':True,'derived_actual_point_binding':True,'native_input_program_request_histories_retained':True,
      'projected_word_and_substitution_laws':True,'five_slot_PN_preserved':True,'full_legacy_local_records_retained':True,
      'kernel_D3_enumerator_completeness_proved':False,'full_uniform_task_package_proved':False,'intended_operational_space_embedding_proved':False,
      'legacy_whole_cache_equivalence_claimed':False,'unbounded_Number_API_proved':False,'physical_policy_admissibility_proved':False,'root_resolved':False,
      'region_context_controls':1278,'cutoff_reference_comparisons':613,'legacy_local_bindings':365,'query_cases':320,'negative_controls':8,
      'formal_check':{'receipt':BASE+'results/agda-RamseyExactSource.json','compiler_sha256':f['compiler_sha256'],'module_source_sha256':f['module_source_sha256'],
       'ignore_interfaces':True,'inputs_stable':True,'library_inventory_sha256':sha256(json.dumps(f['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
      'remaining_witness':'An incidence- and operation-preserving interpretation of the exact prepared local-PN model into the intended operational source, beyond local PN namespace witnesses.',
      'witness':raw,'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-exact-source-v1.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('witness','source_sha256')}))
if __name__=='__main__':main()
