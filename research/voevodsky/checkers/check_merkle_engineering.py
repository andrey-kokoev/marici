"""Unified dispatch, cache isolation, hostile input controls and reproducible timings."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from statistics import median
from time import perf_counter
import json
import subprocess
import sys

from merkle_identity_kernel import Builder
from merkle_verify import verify, strict_loads, VerifiedCache
from check_merkle_identity_surface import cube, encode
from check_merkle_torus_holonomy import torus
from merkle_gluing_search import face_packet, search
from check_merkle_gluing_search import detached_cube_faces
from merkle_cone_filler import construct as fill
from merkle_witness_transport import construct as transport

BASE=Path(__file__).resolve().parents[1]
MODULE=Path(__file__).with_name('merkle_verify.py')

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError,ZeroDivisionError,RecursionError,AttributeError): return True
    return False

def batch(n=128,edit=False):
    b=Builder(); x,y=b.var('x'),b.var('y'); leaves=[]
    for i in range(n):
        c=b.const(i if not edit or i else n+1)
        left=b.term('add',b.term('add',x,y),c)
        right=b.term('add',x,b.term('add',y,c))
        leaves.append((left,right,b.proof('ring',left,right)))
    while len(leaves)>1:
        following=[]
        for i in range(0,len(leaves),2):
            if i+1==len(leaves): following.append(leaves[i]); continue
            a,z=leaves[i:i+2]; left=b.term('add',a[0],z[0]); right=b.term('add',a[1],z[1])
            following.append((left,right,b.proof('congruence',left,right,premises=[a[2],z[2]])))
        leaves=following
    return b.artifact(['x','y'],{},leaves[0][2])

def main():
    original,edited=batch(),batch(edit=True); cache=VerifiedCache()
    cold=verify(original,cache); warm=verify(original,cache); changed=verify(edited,cache)
    checks={'cold_proof_accepted':cold['accepted'],
            'warm_cache_avoids_semantic_recomputation':warm['cache_hits']>0 and warm['cache_misses']==0,
            'edit_reuses_unaffected_subproofs':changed['cache_hits']>0 and 0<changed['cache_misses']<cold['cache_misses'],
            'changed_judgment_root_not_confused_with_old':original['root']!=edited['root'],
            'all_current_dependencies_preflighted_on_warm_hit':warm['reachable_objects']==cold['reachable_objects']}
    corrupted=deepcopy(original); term=next(k for k,r in corrupted['objects'].items() if r.get('op')=='const'); corrupted['objects'][term]['value']='999'
    checks['warm_cache_cannot_hide_corrupted_object']=rejected(lambda:verify(corrupted,cache))
    missing=deepcopy(original); del missing['objects'][term]
    checks['warm_cache_cannot_hide_missing_dependency']=rejected(lambda:verify(missing,cache))
    b=Builder(); x,y=b.var('x'),b.var('y'); h=b.proof('assumption',x,y,label='h')
    conditional=b.artifact(['x','y'],{'h':[x,y]},h); verify(conditional,cache)
    rescoped=b.artifact(['x','y'],{'h':[x,x]},h)
    checks['changed_context_cannot_reuse_assumption_proof']=rejected(lambda:verify(rescoped,cache))
    checks['unconditional_policy_enforced']=rejected(lambda:verify(conditional,cache,require_unconditional=True))
    checks['unknown_schema_rejected']=rejected(lambda:verify({'schema':'trust-anything'}))
    checks['duplicate_json_keys_rejected']=rejected(lambda:strict_loads('{"root":1,"root":2}'))
    checks['nan_rejected']=rejected(lambda:strict_loads('{"x":NaN}'))
    checks['floating_point_scalar_rejected']=rejected(lambda:strict_loads('{"x":0.5}'))
    checks['oversized_string_rejected']=rejected(lambda:strict_loads(json.dumps({'x':'a'*4097})))
    checks['excessive_json_nesting_rejected']=rejected(lambda:strict_loads('['*100+'0'+']'*100))
    enormous=b.const(2)
    for _ in range(13): enormous=b.term('mul',enormous,enormous)
    huge=b.artifact(['x','y'],{},b.proof('refl',enormous,enormous))
    checks['coefficient_growth_bounded']=rejected(lambda:verify(huge))
    version_cache=VerifiedCache(); verify(original,version_cache); version_cache.namespace='different-implementation'
    checks['implementation_namespace_invalidates_cache']=verify(original,version_cache)['cache_misses']>0
    tiny=VerifiedCache(limit=8); verify(original,tiny)
    checks['cache_size_bounded']=len(tiny.entries)<=8
    cube_store=encode(cube()); torus_store=encode(torus())
    checks['unified_surface_verification']=verify(cube_store,require_global=True)['accepted']
    checks['local_torus_accepted_but_global_policy_refused']=verify(torus_store)['accepted'] and rejected(lambda:verify(torus_store,require_global=True))
    checks['unified_filler_verification']=verify(fill(cube_store))['accepted']
    source=face_packet(detached_cube_faces()); found=search(source)['solutions'][0]
    checks['unified_unglued_face_verification']=verify(source)['result']['gluing']=='not supplied or inferred'
    bundle={'schema':'marici.gluing-proof-bundle.v1','source':source,'certificate':found['certificate'],'surface':found['surface']}
    checks['unified_gluing_certificate_verification']=verify(bundle)['accepted']
    target=Builder(); w=target.var('w'); rw=target.proof('ring',w,w)
    transported=transport(conditional,target,['w'],{},{'x':w,'y':w},{'h':rw})
    checks['unified_transport_verification']=verify(transported)['accepted']
    checks['irrelevant_policy_is_not_silently_ignored']=rejected(lambda:verify(fill(cube_store),require_unconditional=True))
    # Timings include integrity preflight. No ratio is a test assertion.
    samples={'cold':[],'warm':[],'one_leaf_edit':[]}
    for _ in range(5):
        session=VerifiedCache()
        for name,artifact in [('cold',original),('warm',original),('one_leaf_edit',edited)]:
            start=perf_counter(); verify(artifact,session); samples[name].append((perf_counter()-start)*1000)
    benchmark={'fixture':'128 independently witnessed leaves combined by a balanced congruence DAG',
               'supplied_objects':len(original['objects']),'repetitions':5,
               'median_ms':{k:median(v) for k,v in samples.items()},'samples_ms':samples,
               'semantic_counts':{k:{'hits':r['cache_hits'],'misses':r['cache_misses']} for k,r in [('cold',cold),('warm',warm),('one_leaf_edit',changed)]},
               'serialized_bytes':len(json.dumps(original).encode()),
               'scope':'Local timings, not a portable speed guarantee; full current-object hashing remains linear in supplied store size.'}
    out=BASE/'results'; out.mkdir(exist_ok=True)
    path=out/'merkle_engineering_proof.json'; path.write_text(json.dumps(original,indent=2)+'\n',encoding='utf-8')
    (out/'merkle_gluing_proof_bundle.json').write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')
    cli=subprocess.run([sys.executable,str(MODULE),str(path),'--require-unconditional'],capture_output=True,text=True)
    checks['fresh_unified_cli_verification']=cli.returncode==0 and json.loads(cli.stdout)['accepted']
    receipt={'schema':'marici.merkle-engineering-check.v1','passed':all(checks.values()),'checks':checks,'benchmark':benchmark,
             'gateway_sha256':sha256(MODULE.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (out/'merkle_engineering.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    if not receipt['passed']: raise SystemExit(1)

if __name__=='__main__': main()
